---
title: "Token throughput and the memory wall: why decode is bandwidth-bound"
author: "David Leitch"
date: 2026-05-11
format: html
draft: false
category: "datacentres"
lightbox: true
---

# Token throughput and the memory wall

This is a short technical note expanding on a paragraph in `background/training_v_inference.md` (§3 — Memory and networking). The headline claim there was:

> tokens-per-second is therefore close to **(memory bandwidth) ÷ (bytes read per token)**. A B200 with 8 TB/s bandwidth running a 70 B parameter model at FP8 (~70 GB resident) caps out at ~115 tokens/sec per GPU stream; with FP4 quantisation the cap roughly doubles.

This note unpacks what is actually happening physically inside the GPU during decode, why memory bandwidth matters more than compute for inference, and why this drives so much of the recent hardware roadmap (H200, B300, Rubin) toward more HBM and more bandwidth rather than more FLOPs.

---

## What happens in a single decode step

To generate one token, a transformer runs a forward pass through every layer. For each layer the GPU must:

- **Attention**: read the resident KV cache for this request, do a small matmul (one new query against many cached keys), append the new key and value to the cache.
- **Feed-forward (MLP)**: read the layer's two big weight matrices, multiply against the just-attended hidden vector, output the next hidden vector.

Then it repeats for all layers, samples a token from the final logits, and the next decode step does the entire thing again — including reading every weight matrix from HBM from scratch.

The defining feature of decode is that **for one request, batch size is 1**. Each weight matrix is loaded from memory and used for exactly one matrix-vector multiply (instead of one matrix-matrix multiply at higher batch size). The FLOPs per byte loaded are very low — roughly 2 FLOPs per byte for a single-stream decode step. Compare that to a B200's hardware peak of ~280 FLOPs/byte at FP8, and the GPU's compute pipeline is sitting almost entirely idle waiting for memory.

That is the technical definition of "memory-bandwidth-bound": the bottleneck is how fast bytes move from HBM to the tensor cores, not how fast the tensor cores can do arithmetic.

---

## The math made concrete

The simplified formula is:

```
tokens per second per stream  ≈  HBM bandwidth ÷ bytes that must be read per token
```

For a 70-billion-parameter model on a single B200 (8 TB/s = 8,000 GB/s of HBM bandwidth):

**Tokens/sec for a 70 B-parameter model on one B200**

| Precision | Bytes per parameter | Resident size | Bytes read per token | Tokens/sec |
|:----------|--------------------:|--------------:|---------------------:|-----------:|
| BF16      | 2                   | 140 GB        | 140 GB               | ~57        |
| FP8       | 1                   | 70 GB         | 70 GB                | ~115       |
| FP4 (NVFP4) | 0.5               | 35 GB         | 35 GB                | ~230       |

*Source: ITK calculation; bandwidth from B200 spec sheet, ignores small KV-cache contribution per token.*

This is exactly the math behind the headline claim. FP4 doesn't make the chip faster at arithmetic — it halves the bytes that have to flow through the memory bus, and tokens-per-second roughly doubles. FP8 to FP4 is essentially a 2× memory-bandwidth multiplier purchased through quantisation.

The same arithmetic explains why **H200 sells as an inference chip even though it has the same compute as H100**:

| GPU  | Compute (BF16 dense) | HBM bandwidth | Tokens/sec on 70 B FP8 |
|:-----|---------------------:|--------------:|-----------------------:|
| H100 | 989 TFLOPS           | 3.35 TB/s     | ~48                    |
| H200 | 989 TFLOPS           | 4.8 TB/s      | ~69                    |

*Source: ITK calculation from vendor spec sheets.*

Same TFLOPS, 43% more bandwidth → 43% more tokens/sec on memory-bound workloads. Pure bandwidth uplift.

---

## Why "the memory wall" — the historical pattern

Compute has grown faster than bandwidth for several Nvidia generations:

**Compute and bandwidth, Nvidia data centre lineage**

| Generation     | Year | Dense FP8/BF16    | HBM bandwidth | Hardware FLOPs/byte |
|:---------------|-----:|------------------:|--------------:|--------------------:|
| A100 SXM       | 2020 | 312 TFLOPS BF16   | 2.0 TB/s      | 156                 |
| H100 SXM       | 2022 | 989 TFLOPS BF16   | 3.35 TB/s     | 295                 |
| H200 SXM       | 2024 | 989 TFLOPS BF16   | 4.8 TB/s      | 206                 |
| B200           | 2025 | 2,250 TFLOPS FP8  | 8.0 TB/s      | 281                 |
| R100 (Rubin)   | 2027 | ~16,000 TFLOPS FP8 | 22 TB/s      | 727                 |

*Source: ITK derivation from vendor spec sheets cited in `training_v_inference.md`. Note: hardware "FLOPs/byte" is the peak ratio; actual workloads sit at 2-50 depending on type — training large matmuls is high arithmetic intensity (50+), single-stream decode is low (~2).*

The hardware ratio drifts upward over time — each new generation makes more compute "available" per byte of memory bandwidth. For training workloads (large matmuls, high arithmetic intensity, lots of FLOPs per byte) this is fine and welcome. For decode (low arithmetic intensity), it means the compute side is increasingly idle. That mismatch is **the memory wall** — the hardware has the FLOPs sitting there but the workload cannot feed them fast enough.

The memory wall is why:

- Nvidia ships H200 (just more HBM on the H100 silicon) as a dedicated inference SKU.
- Each Blackwell generation roughly doubles HBM capacity (192 → 288 GB) and bandwidth (8 → 22 TB/s on Rubin) faster than compute would otherwise dictate.
- FP4 inference matters disproportionately — it is effectively a 2× bandwidth multiplier purchased through compression, not silicon.
- Specialty inference chips like Cerebras WSE-3 win on tokens/sec by sidestepping HBM entirely — they fit the model in 21 PB/s on-chip SRAM (≈3,000× HBM bandwidth), and tokens/sec for Llama 3.1 405B is correspondingly 5-10× what a top-end Nvidia setup does.

---

## Two important corrections to the simple formula

### Batching amortises weight reads

If you serve 16 concurrent requests on the same GPU, the weight matrices are loaded once from HBM and used 16 times — each request still gets its own per-token decode, but the weight-read cost is shared. Aggregate throughput per GPU rises with batch size up to a limit set by KV cache memory pressure.

This is why **aggregate tokens/sec on a busy inference server is 5-20× the single-stream number**. The 115 tokens/sec FP8 figure for one B200 is per concurrent request, not the GPU's max output. A well-batched server might hit ~2,000-3,000 tokens/sec aggregate on the same hardware.

This is also why "tokens per second per GPU" benchmarks are slippery — the same chip running the same model at the same precision can report a 10× range of throughput depending on concurrency, the serving stack and the prompt mix.

### KV cache reads add to the per-token cost as context grows

A short prompt has trivial KV cache; a 100K-token chat has many gigabytes of cache that must also stream through HBM each decode step. The fuller formula is:

```
tokens/sec ≈ bandwidth ÷ (weight bytes + KV cache bytes per token)
```

This is why long-context inference performance falls off sharply once the KV cache approaches or exceeds the weight size, and why **Grouped Query Attention (GQA), Multi-head Latent Attention (MLA) and KV-cache quantisation are now baseline optimisations rather than nice-to-haves**. They reduce KV cache size 4-8× and keep long-context decode in the regime where weights dominate the bandwidth bill.

DeepSeek-V3's MLA is the clearest current example — it shrinks the KV cache by an order of magnitude, which is much of why DeepSeek can serve a 671 B-parameter MoE at competitive cost.

---

## Implication for hardware purchasing

For training a frontier model: buy GPUs with the most FLOPs you can get connected by the fastest fabric you can wire. Bandwidth matters but compute-density matters more.

For serving inference: buy GPUs with the most HBM bandwidth and capacity per dollar. The H200 looks worse than B200 on FLOPs but better than B200 per dollar on memory-bound inference. The A100 is uneconomic for training a 2026 frontier model but still excellent value for serving Llama 3 70B inference, where its 2 TB/s bandwidth is the limiting factor either way.

This is the "trickle-down" dynamic from §7 of `training_v_inference.md` in mechanical form: **the bandwidth that matters for inference does not fall off as fast as the compute that matters for training**, so older chips keep their inference value longer than their training value. That is what supports the Microsoft / Meta / Google decision to extend AI server depreciation life from 4-5 years to 6 years — the implicit bet that the trickle-down is durable because the H100 and A100 fleets still serve inference economically even as the next training cluster moves to Blackwell or Rubin.

---

## A worked physics check

For sanity: a B200 has 8 TB/s of HBM bandwidth = 8 × 10¹² bytes/sec. A 70 B-parameter FP8 model has weights of 70 × 10⁹ bytes. Time to read weights once = 70 × 10⁹ ÷ 8 × 10¹² = 8.75 ms. Tokens per second = 1 ÷ 0.00875 ≈ 114. Matches the headline claim.

The same calculation for FP4 weights (35 GB): 35 × 10⁹ ÷ 8 × 10¹² = 4.4 ms ≈ 230 tokens/sec. Roughly double, also as claimed.

The compute side is irrelevant in this calculation. Even if the GPU had 100× more FLOPs, the answer wouldn't change unless bandwidth changed. That asymmetry is the entire point of the memory wall.

---

*See also: `training_v_inference.md` for the broader treatment of training and inference workloads, hardware lineage, networking and lifecycle dynamics. A follow-up note will tackle the cost economics — cost-per-token, depreciation schedules and grid-load implications.*
