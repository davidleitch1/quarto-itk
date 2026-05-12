---
title: "AI training versus AI inference: the technical foundations"
author: "David Leitch"
date: 2026-05-11
format: html
draft: false
category: "datacentres"
lightbox: true
---

# AI training versus AI inference: the technical foundations

This note maps the workloads, silicon, memory, networking, cooling, utilisation, throughput and lifecycle dynamics that distinguish AI **training** from AI **inference**. It deliberately stops short of economics — a follow-up note will pick up data-centre cost-per-token, depreciation, and the implications for grid load and power purchase agreements.

The intended reader is an Australian electricity-market analyst with a grasp of dispatch, capacity factors and engineering economics, but not necessarily of GPU architectures. Where a manufacturer's marketing number departs from real-world performance, that is flagged explicitly. The underlying research draft is kept under `background/_research_drafts/training_v_inference_technical.md` for traceability.

---

## 1. Workload definitions

### Training

**Pre-training** is the dominant compute job. A transformer is initialised with random weights and shown trillions of tokens drawn from web text, code, books and other corpora. Each forward pass produces predictions; each backward pass updates the weights via gradient descent. Training uses an optimiser (Adam or its variants) which itself stores two extra tensors per parameter, so optimiser state typically multiplies the resident memory footprint by ~3-4× the raw parameter count.

The **Chinchilla scaling law** (Hoffmann et al., DeepMind, 2022) established the compute-optimal ratio at roughly 20 training tokens per parameter [@chinchilla-2022]. Frontier labs have pushed well beyond Chinchilla-optimal — Meta's Llama 3.1 405B was trained on 15.6 trillion tokens (≈38 tokens per parameter), at a cost of roughly 3.8 × 10²⁵ FLOPs on ~16,000 H100 GPUs [@llama3-2024]. Epoch AI documents that frontier-model training compute has doubled roughly every 5.2 months since 2020 [@epoch-trends].

**Fine-tuning** adapts a pre-trained model to a narrower task or domain. It uses the same gradient-descent machinery as pre-training but on far smaller datasets — typically thousands to millions of examples — and consumes a tiny fraction (often <1%) of the original pre-training compute.

**RLHF** (reinforcement learning from human feedback) trains a reward model from human-ranked outputs and then uses Proximal Policy Optimization or similar to nudge the policy model toward higher-reward behaviour. Modern variants increasingly use **RLVR** (reinforcement learning from verifiable rewards) — the answer is right or wrong, the code compiles or it doesn't — sidestepping the learned reward model [@redhat-posttraining].

**Reasoning-model RL training** (OpenAI's o1/o3, Anthropic's reasoning Claude models, DeepSeek-R1) is the newest category. The model learns to generate long chains of thought that improve answer quality on hard reasoning tasks. OpenAI's published o1 charts show performance scaling smoothly with both train-time RL compute and test-time inference compute [@openai-o1]. RL post-training is now a material and growing share of the total training compute budget [@rlhfbook].

### Inference

Inference splits into two phases for any transformer LLM:

- **Prefill (prompt processing)** — the model reads the entire input prompt and produces the first token, populating the attention layers' key-value (KV) cache as it goes. This phase is one large matrix multiplication per layer; it is **compute-bound** and can be batched effectively across requests [@tds-prefill-decode].
- **Decode (token generation)** — once prefill is complete, the model emits tokens one at a time. Each new token requires reading the entire model weights and the entire KV cache from memory; the actual arithmetic per token is small. This phase is **memory-bandwidth-bound**. A single user request leaves most of the GPU's compute idle waiting for memory [@nvidia-inference].

### Why reasoning models blur the line

Reasoning models such as o1, o3 and DeepSeek-R1 are *served* as inference workloads, but each query generates 10-100× more output tokens than a non-reasoning model because the model is "thinking out loud" through hidden chains of thought before answering [@raschka-reasoning]. Each of those tokens costs the same memory-bound decode flops as any other inference token. A reasoning-model query that takes 90 seconds and outputs 50,000 tokens occupies a GPU for roughly the same wall-clock as a small fine-tuning job, and on a graph of GPU-seconds-per-query the reasoning-model bar starts to look like training rather than chat.

### Today's training-inference compute split

Disclosed numbers are sparse and the most-cited estimate is from Epoch AI, working from leaked OpenAI cost data: in calendar 2024, **only ~30% of OpenAI's compute spending went to inference**; the remaining 70% went to training, research experiments and amortised R&D [@epoch-openai]. Inference share is rising as user traffic and reasoning-model token volumes grow, with industry analysts projecting inference could claim ~75% of total AI compute by 2030 [@raschka-reasoning]. SemiAnalysis has emphasised that the value of token end-demand is rising rapidly and that inference is now the dominant area of focus for hardware vendors, even as training compute also continues to grow [@semi-value-capture].

The 30/70 split is OpenAI-specific and does not generalise — Anthropic's compute spend skews more heavily to training than inference at this stage; Meta's inference workload is much larger in absolute terms because it serves billions of recommender-system inferences per day on top of LLM workloads.

---

## 2. The hardware

For each chip family below, the note flags where it primarily sits on the training-versus-inference spectrum and the published headline specifications. Where a vendor quotes sparse FP4 or sparse FP8, the dense number is given — sparse compute relies on a 2:4 sparsity pattern that is rarely realised in production for general LLMs and inflates apparent generational uplift.

### Nvidia data centre GPU lineage

**H100 (Hopper, 2022)** — the workhorse of the 2023-2024 training boom. SXM5 variant: 80 GB HBM3, 3.35 TB/s memory bandwidth, ~989 TFLOPS BF16 dense, ~1,979 TFLOPS FP8 dense [@nvidia-h100]. 700 W TDP. This is the chip that trained GPT-4, Llama 3, Claude 3 and DeepSeek-V3.

**H200 (Hopper refresh, late 2024)** — same GH100 die as H100, same compute, but the memory subsystem was rebuilt around HBM3e. Capacity rose from 80 GB to 141 GB; bandwidth from 3.35 TB/s to 4.8 TB/s [@nvidia-h200]. Because inference decode is memory-bound, the H200 delivers materially better tokens-per-second-per-GPU than H100 on the same model with no compute change. CoreWeave reported 33,000 tokens/sec on Llama 2 70B for H200, ~40% above their H100 instance result [@coreweave-mlperf]. **Primarily inference-skewed**, though it trains too.

**B200 / B100 (Blackwell, late 2024 / early 2025)** — a new architecture using two reticle-sized dies stitched by Nvidia's NV-HBI interface (10 TB/s die-to-die). 192 GB HBM3e per GPU, 8 TB/s memory bandwidth, native FP4 tensor cores, ~9 PFLOPS sparse FP4 (~4.5 PFLOPS dense FP4), ~2.25 PFLOPS dense FP8 [@nvidia-blackwell]. 1,000 W TDP for B200.

**GB200 NVL72 (rack-scale, 2025)** — 72 Blackwell GPUs and 36 Grace CPUs in a single liquid-cooled rack, all connected via NVLink Switch into one logical 72-GPU domain with 130 TB/s aggregate NVLink bandwidth and 13.4 TB unified GPU memory. Rated 1.44 exaFLOPs sparse FP4 and ~120 kW per rack [@nvidia-gb200; @register-gb200]. **Training and large-model inference**: the rack-scale NVLink domain is what makes a 1-trillion-parameter MoE servable at low latency.

**B300 / Blackwell Ultra (announced GTC 2025, shipping 2H 2025)** — 288 GB HBM3e in 12-high stacks, 8 TB/s, ~15 PFLOPS dense FP4 (~50% lift over B200), 1,400 W TDP, 208 billion transistors [@toms-b300]. Marketed explicitly for reasoning-model inference. The GB300 NVL72 rack delivers ~1.5× GB200 NVL72 [@nvidia-blackwell-ultra].

**Vera Rubin (R100 GPU + Vera CPU, announced GTC 2025-2026)** — Nvidia's next architecture, first detailed at GTC Washington 2025, then expanded at GTC 2026. 288 GB HBM4 per GPU at ~22 TB/s; ~50 PFLOPS sparse FP4 (~25 PFLOPS dense FP4), ~16 PFLOPS dense FP8; NVLink 6 at 3.6 TB/s per GPU; 88-core Arm-based Vera CPU [@nvidia-rubin; @wiki-rubin]. **Pre-shipping at the time of writing — early-access H2 2026, broad availability 2027.** Treat the marketing claim of "5× Blackwell inference at 10× lower cost per token" as roadmap, not delivered.

### AMD challenger lineage

**MI300X (CDNA 3, 2024)** — 192 GB HBM3, 5.3 TB/s, 750 W. Larger memory than H100 made it attractive for serving large models on a single GPU, though the ROCm software stack lagged Nvidia's CUDA [@amd-mi300].

**MI325X (late 2024 / 2025)** — same compute as MI300X, but HBM3e raises capacity to 256 GB and bandwidth to 6 TB/s. Mid-cycle refresh, similar positioning.

**MI355X / MI350 series (CDNA 4, mid-2025)** — 288 GB HBM3e, 8 TB/s, 1,400 W, native FP6/FP4, claimed >20 PFLOPS at low precision. AMD claims 4× the AI compute per chip versus MI300X and 35× inference uplift through architecture and software combined [@amd-mi350; @toms-mi350]. **Both training and inference**, with inference the primary near-term target given the software gap.

### Hyperscaler in-house silicon

**AWS Trainium2** (GA late 2024) — 1.3 PFLOPS dense FP8 per chip, 96 GB HBM, 2.9 TB/s. A Trn2 instance bundles 16 chips; the Trn2 UltraServer scales to 64 chips connected over NeuronLink for 83.2 PFLOPS FP8 [@aws-trainium2]. AWS-Anthropic Project Rainier puts hundreds of thousands of Trainium2 chips into a single training cluster, claimed to deliver 5× the exaFLOPS of Anthropic's prior generation training run [@register-rainier].

**AWS Trainium3** (announced re:Invent 2024, GA late 2025) — first 3 nm AWS AI chip, 2.52 PFLOPS dense FP8 per chip, 144 GB HBM3e, 4.9 TB/s. Trn3 UltraServer scales to 144 chips for 362 FP8 PFLOPS [@aws-trainium3]. **Inferentia2** continues as the dedicated inference part for older workloads.

**Google TPU**: v5p (training-class, 8,960-chip pods), v5e (cost-efficient inference variant). **Trillium (TPU v6e, GA 2024)** delivers 4.7× the peak compute per chip versus v5e with doubled HBM and ICI bandwidth, scaling to 256 chips per pod [@google-trillium]. **Ironwood (TPU v7, announced Google Cloud Next April 2025)** delivers ~4.6 PFLOPS FP8 per chip and scales to either 256-chip or 9,216-chip clusters [@introl-tpu]. Google has gone furthest among hyperscalers in differentiating "training" from "inference" SKUs (v5p vs v5e/v6e).

**Microsoft Maia 100** (deployed 2024) — 64 GB HBM2E, 1.8 TB/s, ~0.8 PFLOPS BF16, 700 W TDP, TSMC N5 [@msft-maia-hotchips]. **Maia 200** (codename "Braga") announced January 2026 — TSMC 3 nm, 216 GB HBM3e, 7 TB/s, native FP8/FP4, >10 PFLOPS FP4, 750 W [@msft-maia200; @toms-maia200]. Mass production was delayed from 2025 to 2026; Microsoft markets Maia 200 explicitly as inference-first.

**Meta MTIA**: v1 (TSMC 7 nm, 25 W, 102 TOPS INT8) and v2 (TSMC 5 nm, 90 W, 354 TOPS INT8 / 177 TFLOPS FP16) [@meta-mtia; @nextplatform-mtia]. Both generations are inference-only in production; Meta uses MTIA for ranking/recommendation and is prototyping software for a future training chip.

### Specialty inference accelerators

**Groq LPU** — bakes model weights into on-chip SRAM and uses a deterministic, compiler-scheduled execution model. Pure inference accelerator. Strong on time-to-first-token; weak on memory capacity (running Llama 70B requires hundreds of LPUs to assemble enough SRAM) [@intuition-chips].

**Cerebras WSE-3** — a single 46,255 mm² silicon wafer with 4 trillion transistors, 900,000 cores and 44 GB on-chip SRAM. The wafer-scale design eliminates inter-chip communication for any model that fits, delivering ~969 tokens/sec on Llama 3.1 405B [@cerebras-405b]. Used for both training and ultra-high-throughput inference but has tiny installed base relative to Nvidia.

**SambaNova RDA / SN40L** — Reconfigurable Dataflow Architecture; the compiler maps neural-network layers onto a spatial array of compute/memory tiles. Three-tier memory hierarchy (on-chip SRAM, HBM, DRAM) supports very large models on small numbers of chips. SambaNova claims ~16 SN40L chips can serve Llama 70B, against hundreds of LPUs.

**Tenstorrent (Wormhole, Blackhole)** — RISC-V-based, ethernet-native, fully open-source software stack (TT-Metalium, TT-Forge). Blackhole: 140 Tensix++ cores, 6 nm, 745 TFLOPS FP8 (peak, single die), 512 GB/s GDDR6 [@tenstorrent-blackhole]. Targets the open-stack inference market; modest production volumes to date.

### CPUs in the AI data centre

CPUs are not direct competitors to GPUs/accelerators for transformer training or large-model inference — the arithmetic intensity and parallelism gap is too large. They remain essential for orchestration, embedding lookups, RAG retrieval, lightweight inference (small models, classical ML), and as host processors driving GPU servers. Intel Xeon 6 "Granite Rapids" reaches 128 P-cores per socket with AMX matrix extensions; AMD EPYC 9005 "Turin" reaches 192 cores per socket [@toms-granite]. For serving frontier LLMs at scale, CPUs are not a substitute for accelerators.

---

## 3. Memory and networking

### HBM — capacity, bandwidth, and the memory wall

High Bandwidth Memory is stacked DRAM with a wide interface to the GPU/accelerator die. Each stack today provides:

**HBM generation specifications**

| HBM generation | Capacity per stack | Bandwidth per stack |
|:---------------|-------------------:|--------------------:|
| HBM3           | 16-24 GB           | ~0.8 TB/s           |
| HBM3e          | 24-36 GB (8H-12H)  | 1.2-1.33 TB/s       |
| HBM4           | up to 64 GB (16H)  | 2.0-3.3 TB/s        |

*Source: industry summaries from Introl and Siemens [@introl-hbm; @siemens-hbm].*

**HBM capacity by data centre GPU**

| GPU                    | HBM type | Capacity | Bandwidth   |
|:-----------------------|:---------|---------:|------------:|
| Nvidia H100 SXM        | HBM3     | 80 GB    | 3.35 TB/s   |
| Nvidia H200            | HBM3e    | 141 GB   | 4.8 TB/s    |
| Nvidia B200            | HBM3e    | 192 GB   | 8.0 TB/s    |
| Nvidia B300            | HBM3e    | 288 GB   | 8.0 TB/s    |
| Nvidia R100 (Rubin)    | HBM4     | 288 GB   | 22 TB/s     |
| AMD MI300X             | HBM3     | 192 GB   | 5.3 TB/s    |
| AMD MI325X             | HBM3e    | 256 GB   | 6.0 TB/s    |
| AMD MI355X             | HBM3e    | 288 GB   | 8.0 TB/s    |
| AWS Trainium2          | HBM      | 96 GB    | 2.9 TB/s    |
| AWS Trainium3          | HBM3e    | 144 GB   | 4.9 TB/s    |
| Microsoft Maia 200     | HBM3e    | 216 GB   | 7.0 TB/s    |

*Source: vendor data sheets cited in §2.*

The pattern is unambiguous: each generation buys memory capacity and bandwidth roughly as aggressively as compute. The reason is the **memory wall** — peak compute has grown faster than memory bandwidth for several generations, and inference decode is bandwidth-bound. For each output token, the GPU must read the entire model weights and the entire attention KV cache from HBM; tokens-per-second is therefore close to **(memory bandwidth) ÷ (bytes read per token)**. A B200 with 8 TB/s bandwidth running a 70 B parameter model at FP8 (~70 GB resident) caps out at ~115 tokens/sec per GPU stream; with FP4 quantisation the cap roughly doubles [@nvidia-inference].

### NVLink and intra-node fabric

Nvidia's NVLink is a coherent GPU-to-GPU link inside a server or rack:

**NVLink bandwidth by generation**

| Generation       | GPU              | Per-GPU bandwidth |
|:-----------------|:-----------------|------------------:|
| NVLink 3 (V100)  | V100             | 300 GB/s          |
| NVLink 3 (A100)  | A100             | 600 GB/s          |
| NVLink 4 (H100)  | H100             | 900 GB/s          |
| NVLink 5 (B200)  | B200             | 1.8 TB/s          |
| NVLink 6 (R100)  | R100 (Rubin)     | 3.6 TB/s          |

*Source: Introl and Wikipedia NVLink summaries [@introl-nvlink; @wiki-nvlink].*

The **NVLink Switch** chip (5th-generation in the GB200 NVL72) creates a non-blocking 130 TB/s fabric across 72 GPUs in one rack. From the model's perspective the rack behaves as one logical accelerator with 13.4 TB unified HBM. This is what makes serving a multi-trillion-parameter MoE feasible at low latency, and it is what training a frontier model across an NVL72 node looks like in practice.

### Inter-node networking — InfiniBand vs Ethernet

Within a data hall, training clusters need a back-end network that connects every GPU to every other GPU at near-line-rate. InfiniBand NDR 400 Gb has historically dominated. Ethernet has been catching up via RoCE (RDMA over Converged Ethernet) and Nvidia's **Spectrum-X**, which ports adaptive routing and congestion control from InfiniBand onto Ethernet silicon.

Real-world numbers from NCCL all-reduce on 8×H100 SXM: InfiniBand NDR 400 G achieves ~350 GB/s effective bus bandwidth; the same cluster on 400 GbE RoCEv2 achieves 270-290 GB/s [@spheron-networking]. Meta has stated they tuned both fabrics to deliver equivalent training performance and that their largest models were trained on RoCE.

### Why training needs the fabric and inference largely doesn't

Training is fundamentally a synchronous distributed algorithm. After every micro-batch, every GPU's gradients must be **all-reduced** with every other GPU's so the next forward pass uses consistent weights. AllReduce is bandwidth- and latency-sensitive; the slowest GPU and the slowest link gates the whole cluster. This is why training fabric matters and why fabric tuning is a discipline of its own.

Inference does not need any of this. Each user request is independent; a 70 B model can be served by a single 8-GPU server, and serving 10,000 simultaneous users is a horizontal-scale problem solved by load-balancing requests across nodes. Inter-node bandwidth requirements for inference are modest compared with training. The exception is very large MoE inference, where the model itself spans many GPUs and expert-parallel all-to-all communication becomes a hot spot — DeepSeek-V3 inference at 671 B parameters uses 32 redundant experts in prefill and runs all-to-all over 8×400 Gb InfiniBand NICs at >40 GB/s [@deepseek-v3].

---

## 4. Power density and cooling

The single biggest physical change in the data centre over the 2024-2026 period is rack power density.

**Rack power density by class**

| Workload                            | Rack density        |
|:------------------------------------|--------------------:|
| Traditional CPU hyperscale          | 5-15 kW             |
| H100 air-cooled (8-GPU server)      | up to ~40 kW        |
| GB200 NVL72 training                | 120-130 kW          |
| Inference cluster (mixed GPUs)      | 30-60 kW            |
| Frontier 2026-27 (Rubin and beyond) | 250-900 kW projected |

*Sources: Introl, The Register, Fluence [@introl-density; @register-gb200; @fluence-gpu].*

ASHRAE's direct-to-chip cooling recommendation kicks in above 20 kW per rack — every serious AI training deployment in 2025 crossed that threshold [@toms-cooling]. The GB200 NVL72 ships only as a liquid-cooled rack: coolant enters at 25 °C at ~2 L/sec and exits ~20 °C warmer [@tonecooling-gb200]. Air cooling tops out somewhere in the 40-60 kW range with aggressive design; 130 kW is 5-15× beyond that ceiling, hence direct-to-chip liquid is now the default for training-class racks. Two-phase immersion is in trial deployments but has not displaced direct-to-chip as the production standard.

The downstream implications for data-centre engineering are substantial — chilled-water plants instead of CRAH units, structural changes to support liquid manifold and rack weight, redesigned power distribution to push 415 V three-phase into each rack — and they are why a 1 GW "AI factory" is not a 10× scale-up of a hyperscale data centre but a different building entirely. Those implications are economic rather than technical and belong in the follow-up note.

---

## 5. Capacity utilisation profiles

### Training utilisation

Frontier training jobs run at high effective utilisation. Meta's Llama 3 paper documents that the 16K-H100 training cluster achieved **90% effective training time** despite roughly one interruption per day, with **38-43% Model FLOPS Utilization (MFU)** for the BF16 workload [@llama3-2024]. Of those two numbers:

- **Effective training time** (≈90%) is what looks "baseload" to the grid — the cluster is drawing power continuously while it trains.
- **MFU** (≈40%) is the share of the GPU's theoretical peak FLOPS actually realised in arithmetic — the rest is lost to memory stalls, communication overhead, pipeline bubbles and so on.

Both are honest numbers. For grid-load purposes, the relevant figure is effective training time: a frontier training cluster looks like a constant load of 70-90% of its rated power draw for weeks at a time.

### Inference utilisation

Inference clusters are diurnal and bursty. McKinsey reports inference racks run at 30-150 kW with utilisation that varies heavily by hour of day; typical industry estimates put average utilisation in the 30-50% range against installed peak [@mckinsey-workloads]. Enterprise estimates from VentureBeat report many fleets running at <40%, with some <10% [@vb-utilisation]. Hyperscaler utilisation is materially higher than enterprise but still well below training-class utilisation.

### Reasoning models change the picture

A reasoning-model query that runs for 90 seconds and emits 50,000 tokens occupies a GPU at near-100% memory-bandwidth utilisation for that whole time. A campus serving heavy reasoning-model traffic looks more "training-like" in its load profile than a campus serving classical chat completions. The blurring is not yet clean enough to support a sharp claim, but the direction of travel is from peaky inference toward smoother, more sustained load — which in electricity terms means inference workloads are starting to look more like baseload than mid-merit.

---

## 6. Token throughput — the technical layer

### Prefill versus decode

Prefill processes the entire input prompt in parallel — one big matmul per layer — and is **compute-bound**. A 10,000-token prompt prefills on an H100 in roughly 200-400 ms [@morph-llm]. Prefill batches well: throwing more concurrent requests at a GPU during prefill scales roughly linearly until compute saturates.

Decode is the per-token generation phase and is **memory-bandwidth-bound**. Per GPU, decode runs at roughly 30-150 tokens/sec for typical 7-70 B parameter models, depending on quantisation and batching [@morph-llm]. Concurrency helps but with diminishing returns: each additional request adds a copy of the KV cache.

### Tokens-per-second — published benchmarks

Llama 3.1 405B is a useful reference point because it cannot fit on a single 8×H100 80 GB node at BF16 — it needs 8×H200 or quantisation to FP8/FP4. Documented throughput numbers:

- **8×H100 (FP8 quantised)**: cluster typically struggles to exceed 10-15 tokens/sec [@valdi-h100].
- **8×H200**: 1.5× higher throughput than tensor-parallel on H100, NVLink-Switch enabled [@nvidia-h200-throughput].
- **GB200 NVL72**: ~3.4× per-GPU performance of 8×H200 on Llama 3.1 405B [@nvidia-mlperf].
- **Cerebras WSE-3**: ~969 tokens/sec on Llama 3.1 405B [@cerebras-405b].
- **TensorRT-LLM on H100, 100 concurrent requests, Llama 70B-class**: ~2,780 output tokens/sec total throughput [@morph-llm].

These are not directly comparable: some are per-GPU, some are aggregate, some are at low concurrency, some at high. The general lesson is that hardware generation, model fit (does it fit?), quantisation and serving stack all matter at least as much as raw chip TFLOPS.

### Quantisation

The training default is BF16 (two bytes per number). Modern training has moved aggressively to FP8 (Hopper and Blackwell support; AWS Trainium2/3 native; AMD MI355X native). FP4 is **inference-only** in production today — Blackwell ships native NVFP4 tensor cores and is the first widely-deployed FP4 accelerator [@nvidia-nvfp4]. NVFP4 quantisation typically loses ≤1% accuracy on standard benchmarks against FP8, while delivering ~1.32× throughput and a 1.8× memory footprint reduction [@nvidia-nvfp4; @spheron-fp4]. NVidia's headline "5× Blackwell vs Hopper" generational claim relies in part on comparing FP4 (Blackwell) with FP8 (Hopper); on like-for-like FP8 the uplift is closer to 2.5×.

### KV cache and concurrency

The KV cache is the per-request scratchpad of attention keys and values. It scales linearly with sequence length and batch size:

- Llama 3 70 B at 8K context: ~320 KB KV cache per token, ~2.56 GB per request.
- 32 concurrent requests at 8K context = ~82 GB — more than an A100 80 GB GPU [@brenndoerfer-kvcache].

The KV cache is therefore the practical limit on concurrency in inference serving. Optimisations stack: Grouped Query Attention (GQA) reduces cache size 8×; FP8 or NVFP4 KV-cache quantisation gives another 2-4×; PagedAttention (used by vLLM) eliminates 60-80% fragmentation waste. Combined, these enable 10-30× more concurrent users on the same hardware versus a naïve baseline [@vllm-optim].

### Optimisation techniques

**Speculative decoding** (and its variants EAGLE, MEDUSA) uses a small "draft" model to propose multiple tokens which the large model verifies in a single forward pass. If most drafts are accepted, throughput rises 2-3× with no quality loss [@premai-spec]. EAGLE-3 reaches ~80% draft acceptance, MEDUSA ~60%.

**Serving frameworks**: vLLM (open source, broad model coverage, PagedAttention origin), TensorRT-LLM (Nvidia, lowest latency, hardest to deploy), SGLang (open source, strong on MoE and long context). Production benchmarks at 100 concurrent requests on H100 show TensorRT-LLM ~2,780 output tok/sec, SGLang ~2,460, vLLM ~2,400 [@spheron-vllm].

**Prefill-decode disaggregation** (Meta, NVIDIA Dynamo) physically separates the compute-bound prefill phase onto one set of GPUs and the memory-bound decode phase onto another, raising goodput because each set runs at its own bottleneck rather than averaging over both [@jarvis-disagg].

---

## 7. Hardware lifecycle and trickle-down

When the next chip generation offers 2-3× the training throughput per dollar of capex and per kWh, the older chip becomes uneconomic for **training** the next frontier model — but it remains useful for **inference** of older or smaller models, fine-tuning, batch jobs and research workloads. This is the trickle-down dynamic.

### The H100 is the worked example

Cloud H100 on-demand prices have fallen 64-75% from their 2023 peak, now in the US\$1.50-4.00/hour range [@thunder-h100]. Blackwell B200 delivers ~2.5-3× H100 training throughput, so a hyperscaler training a new frontier model in 2026 will allocate Blackwell to that job. The H100 fleet that trained GPT-4, Claude 3 and Llama 3 in 2023-24 is now serving inference for those same models, plus smaller models, plus batch workloads. The A100 fleet from 2020-22 is still serving — it delivers 80-90% of an H100's value for memory-bound inference at 70% of H100 cost.

### Useful-life accounting

The trickle-down dynamic supports the recent move by hyperscalers to extend the useful-life assumption for AI servers from 4-5 years to 6 years for depreciation purposes:

- **Microsoft, Google, Meta** all extended useful life to ~6 years in SEC filings during 2023-2024. Meta's 2025 disclosure expects a **US\$2.9 billion reduction in 2025 depreciation expense** from the change [@yahoo-meta-deprec]. Google's earlier extension delivered ~US\$3.4 billion of 2023 depreciation reduction [@dcd-google-deprec].
- **Amazon (AWS)** went the other way in February 2025: shortened useful life for a subset of servers and networking equipment from 6 years back to 5 years, citing "the increased pace of technology development, particularly in the area of artificial intelligence and machine learning". The change took a US\$700 million hit to operating income [@deepquarry-amazon].

The two positions are not as inconsistent as they look. Hyperscalers can extend useful life if they have a credible second life for the hardware as inference fleet — Meta, Google and Microsoft all serve substantial inference traffic on older silicon. Amazon's rationale highlights the opposite risk: that AI silicon depreciates faster than CPU servers because the next chip is meaningfully better and pricing pressure on older inference is real. The accounting choice is an explicit bet on whether the trickle-down is durable. Critics argue the 6-year assumption flatters earnings and that real economic life is closer to 3-4 years [@thecube-deprec].

The economics of all this — what depreciation schedule is defensible, what the second-hand market for H100s clears at, how to model cost-per-token over the chip's full life — is the subject of the follow-up note.

---

## 8. The line is blurring

Three technical developments are blurring what was, two years ago, a clean training-versus-inference distinction.

**Mixture-of-experts inference.** A dense 671 B parameter model is impractical to serve at low latency. DeepSeek-V3 has 671 B total parameters but only 37 B activated per token via top-8 expert selection from 256 experts per layer, plus a shared expert and Multi-head Latent Attention [@deepseek-v3]. This collapses the per-token compute by ~18× while preserving the parameter capacity, but introduces all-to-all expert-routing communication that looks more like training fabric requirements than classical inference. MoE architectures move inference closer to training in network and memory profile.

**Reasoning models.** Per the discussion in §5, a reasoning-model query consumes 10-100× more tokens than a chat-model query and runs the GPU near saturation for tens of seconds. Test-time compute scaling (more thinking tokens → better answers) is now a published axis of model improvement — OpenAI's o1 chart shows accuracy scaling smoothly with both train-time RL compute and test-time inference compute [@openai-o1]. From an electricity-load perspective, heavy reasoning-model traffic on a campus shifts the load shape from peaky-diurnal toward sustained-flat.

**Speculative decoding and serving advances** can shift effective tokens-per-second by 2-3× without changing the underlying hardware. EAGLE-3 and similar techniques are now production defaults in vLLM, SGLang and TensorRT-LLM. The same physical hardware delivers materially different effective throughput depending on the serving stack and the workload mix.

**The same physical hardware now serves both.** A B200 deployed in a GB200 NVL72 can train a frontier model on Monday and serve trillion-parameter MoE inference on Tuesday. The workload mix on a campus may shift hour-by-hour. This makes static "training capacity" vs "inference capacity" classifications increasingly suspect — the relevant unit of analysis is the campus and its workload schedule.

---

## 9. Caveats

- **Marketing peak FLOPS overstate deployed performance.** A B200's "9 PFLOPS FP4" is sparse, with 2:4 structured sparsity rarely realised in production. Dense FP4 is roughly half. Real-world MFU for training is 30-50%; sustained inference throughput is typically 30-60% of marketing peak. Where a quoted number is sparse or marketing-peak, this note flags it.
- **Pre-shipping product is roadmap.** Vera Rubin / R100 is announced for early-access H2 2026 with broad availability in 2027. Maia 200 is announced for 2026 production. Trainium3 UltraServers reached general availability in late 2025. Specifications for not-yet-shipped product are vendor claims.
- **Inference utilisation numbers are estimated, not disclosed.** Hyperscalers do not publish GPU utilisation for inference fleets. The 30-50% range cited above is industry estimate (VentureBeat, McKinsey, GPU-cloud operator commentary), not operator disclosure. Training-cluster utilisation (Meta's 90% effective training time / 38-43% MFU on Llama 3) is one of very few public numbers from a frontier training run.
- **The 30% inference / 70% training compute split is OpenAI-2024.** Epoch AI's number is from leaked OpenAI cost data and does not necessarily generalise to Anthropic, Google or Meta. Anthropic's compute spend is heavier on training than inference at this stage; Meta's inference workload is much larger because it serves billions of recommender-system inferences per day on top of LLM workloads.
- **SemiAnalysis citations are paywalled.** Where this note cites SemiAnalysis pieces, the URL and headline are public but the substantive numbers and interpretation are behind paywall. Treat their compute-split and workload-mix estimates as well-informed industry analysis rather than primary disclosure.

---

## 10. References

The full bibliography is below. URLs are listed in plain markdown and would convert to BibTeX entries (`@org-topic-year`) for any subsequent published article. The underlying research draft is kept under `background/_research_drafts/training_v_inference_technical.md` for full source-level traceability.

### Primary sources — vendor specifications, technical papers, MLPerf

- Hoffmann J et al. (DeepMind). "Training Compute-Optimal Large Language Models" (Chinchilla). arXiv 2203.15556, 2022. https://arxiv.org/abs/2203.15556
- Llama Team, Meta AI. "The Llama 3 Herd of Models". arXiv 2407.21783, 2024. https://ar5iv.labs.arxiv.org/html/2407.21783
- DeepSeek-AI. "DeepSeek-V3 Technical Report". arXiv 2412.19437, 2024. https://arxiv.org/pdf/2412.19437
- Microsoft (Sherry Xu et al.). "Inside Maia 100", Hot Chips 2024. https://hc2024.hotchips.org/assets/program/conference/day2/81_HC2024.Microsoft.Xu.Ramakrishnan.final.v2.pdf
- NVIDIA. "H100 Tensor Core GPU Datasheet". https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf
- NVIDIA. "H200 GPU product page". https://www.nvidia.com/en-us/data-center/h200/
- NVIDIA. "GB200 NVL72 product page". https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA. "Blackwell architecture page". https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
- NVIDIA Newsroom. "NVIDIA Vera Rubin Opens Agentic AI Frontier", GTC 2025. https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform
- NVIDIA Developer Blog. "Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era". https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/
- NVIDIA Developer Blog. "Mastering LLM Techniques: Inference Optimization". https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/
- NVIDIA Developer Blog. "Introducing NVFP4 for Efficient and Accurate Low-Precision Inference". https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
- NVIDIA Developer Blog. "Boosting Llama 3.1 405B Throughput by Another 1.5x on NVIDIA H200". https://developer.nvidia.com/blog/boosting-llama-3-1-405b-throughput-by-another-1-5x-on-nvidia-h200-tensor-core-gpus-and-nvlink-switch/
- NVIDIA Developer Blog. "NVIDIA Blackwell Delivers Massive Performance Leaps in MLPerf Inference v5.0". https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/
- AMD. "Instinct MI300 Series Accelerators". https://www.amd.com/en/products/accelerators/instinct/mi300.html
- AMD. "Instinct MI350 Series GPUs". https://www.amd.com/en/products/accelerators/instinct/mi350.html
- AWS. "Amazon EC2 Trn2 Instances and Trn2 UltraServers" (re:Invent 2024). https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/
- AWS. "Trainium3 UltraServers GA" (Dec 2025). https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
- Google Cloud Blog. "Trillium TPU is GA". https://cloud.google.com/blog/products/compute/trillium-tpu-is-ga
- Microsoft Blog. "Maia 200: The AI accelerator built for inference" (Jan 2026). https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
- Meta AI. "Our next generation Meta Training and Inference Accelerator" (MTIA v2). https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/
- Tenstorrent. "Wormhole" and "Blackhole" product pages. https://tenstorrent.com/en/hardware/wormhole ; https://tenstorrent.com/en/hardware/blackhole
- MLCommons. "MLPerf Inference v5.0 results" (April 2025). https://mlcommons.org/2025/04/mlperf-inference-v5-0-results/
- Cerebras. "Llama 3.1 405B at 969 tokens/s". https://www.cerebras.ai/blog/llama-405b-inference

### Analysis, benchmarks, deep dives

- Epoch AI. "Most of OpenAI's 2024 compute went to experiments". https://epoch.ai/data-insights/openai-compute-spend
- Epoch AI. "Trends in Artificial Intelligence". https://epoch.ai/trends
- Epoch AI. "How persistent is the inference cost burden?". https://epoch.ai/gradient-updates/how-persistent-is-the-inference-cost-burden
- SemiAnalysis (paywalled). "AI Value Capture — The Shift to Model Labs". https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model
- SemiAnalysis (paywalled). "100,000 H100 Clusters". https://newsletter.semianalysis.com/p/100000-h100-clusters-power-network
- SemiAnalysis (paywalled). "AWS Trainium3 Deep Dive". https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential
- SemiAnalysis (paywalled). "NVIDIA GTC 2025 — Built for Reasoning, Vera Rubin, Kyber, CPO, Dynamo Inference". https://newsletter.semianalysis.com/p/nvidia-gtc-2025-built-for-reasoning-vera-rubin-kyber-cpo-dynamo-inference-jensen-math-feynman
- The Next Platform. "With MTIA v2 Chip, Meta Can Do AI Inference, But Not Training". https://www.nextplatform.com/2024/04/10/with-mtia-v2-chip-meta-can-do-ai-training-as-well-as-inference/
- The Register. "A closer look at Nvidia's 120 kW DGX GB200 NVL72 rack system". https://www.theregister.com/2024/03/21/nvidia_dgx_gb200_nvk72/
- The Register. "Amazon Project Rainier: AI supercomputer for Anthropic". https://www.theregister.com/2025/07/04/project_rainier_deep_dive/
- Tom's Hardware. "Nvidia announces Blackwell Ultra B300". https://www.tomshardware.com/pc-components/gpus/nvidia-announces-blackwell-ultra-b300-1-5x-faster-than-b200-with-288gb-hbm3e-and-15-pflops-dense-fp4
- Tom's Hardware. "AMD announces MI350X and MI355X AI GPUs". https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350x-and-mi355x-ai-gpus-claims-up-to-4x-generational-gain-up-to-35x-faster-inference-performance
- Tom's Hardware. "Microsoft Maia 200 introduction". https://www.tomshardware.com/pc-components/cpus/microsoft-introduces-newest-in-house-ai-chip-maia-200-is-faster-than-other-bespoke-nvidia-competitors-built-on-tsmc-3nm-with-216gb-of-hbm3e
- Tom's Hardware. "Data center cooling state of play 2025". https://www.tomshardware.com/pc-components/cooling/the-data-center-cooling-state-of-play-2025-liquid-cooling-is-on-the-rise-thermal-density-demands-skyrocket-in-ai-data-centers-and-tsmc-leads-with-direct-to-silicon-solutions
- Tom's Hardware. "Granite Rapids Xeon 6900P 120 cores". https://www.tomshardware.com/pc-components/cpus/intel-launches-granite-rapids-xeon-6900p-series-with-120-cores-matches-amd-epycs-core-counts-for-the-first-time-since-2017
- McKinsey. "The next big shifts in AI workloads and hyperscaler strategies". https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-next-big-shifts-in-ai-workloads-and-hyperscaler-strategies
- DataCenterDynamics. "Google increases server life to six years". https://www.datacenterdynamics.com/en/news/google-increases-server-life-to-six-years-will-save-billions-of-dollars/
- Yahoo Finance / Bloomberg. "Meta Accounting Move on AI Servers". https://finance.yahoo.com/news/meta-accounting-move-ai-servers-124059775.html
- DeepQuarry. "Amazon revises server lifespan amid AI shift". https://deepquarry.substack.com/p/amazon-revises-server-lifespan-amid

### Supporting trade press, secondary sources

- Introl Blog. "HBM evolution: from HBM3 to HBM4 and the AI memory war". https://introl.com/blog/hbm-evolution-hbm3-hbm3e-hbm4-memory-ai-gpu-2025
- Introl Blog. "NVLink and scale-up networking". https://introl.com/blog/nvlink-scale-up-networking-gpu-interconnect-infrastructure-2025
- Introl Blog. "Google TPU Architecture: 7 Generations Explained". https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations
- Introl Blog. "High-Density Racks: 100kW+ Designs". https://introl.com/blog/high-density-racks-100kw-ai-data-center-ocp-2025
- Spheron. "GPU Networking for AI Clusters: InfiniBand vs RoCE vs Spectrum-X Decision Guide". https://www.spheron.network/blog/gpu-networking-infiniband-roce-spectrum-x-guide/
- Spheron. "vLLM vs TensorRT-LLM vs SGLang: H100 Benchmarks". https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/
- Spheron. "FP4 Quantization on Blackwell GPUs". https://www.spheron.network/blog/fp4-quantization-blackwell-gpu-cost/
- Morph LLM. "LLM Inference: Prefill, Decode, KV Cache & Cost Guide (2026)". https://www.morphllm.com/llm-inference
- IntuitionLabs. "Cerebras vs SambaNova vs Groq: AI Chip Comparison (2025)". https://intuitionlabs.ai/articles/cerebras-vs-sambanova-vs-groq-ai-chips
- Brenndoerfer. "KV Cache Memory: Calculating GPU Requirements for LLM Inference". https://mbrenndoerfer.com/writing/kv-cache-memory-calculation-llm-inference-gpu
- VentureBeat. "5% GPU utilization: The \$401 billion AI infrastructure problem". https://venturebeat.com/infrastructure/5-gpu-utilization-the-401-billion-ai-infrastructure-problem-enterprises-cant-keep-ignoring
- Sebastian Raschka. "The State of LLM Reasoning Model Inference". https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling
- OpenAI. "Learning to reason with LLMs" (o1 announcement). https://openai.com/index/learning-to-reason-with-llms/
- Nathan Lambert. "RLHF Book". https://rlhfbook.com/
- Towards Data Science. "Prefill Is Compute-Bound. Decode Is Memory-Bound". https://towardsdatascience.com/prefill-is-compute-bound-decode-is-memory-bound-why-your-gpu-shouldnt-do-both/
- The Cube. "Resetting GPU depreciation". https://thecuberesearch.com/298-breaking-analysis-resetting-gpu-depreciation-why-ai-factories-bend-but-dont-break-useful-life-assumptions/
- TechCrunch. "AWS Trainium2 chips for building LLMs are now generally available". https://techcrunch.com/2024/12/03/aws-trainium2-chips-for-building-llms-are-now-generally-available-with-trainium3-coming-in-late-2025/
- Tonecooling. "NVIDIA GB200 NVL72 Cooling Requirements". https://tonecooling.com/nvidia-gb200-nvl72-cooling-requirements/
- ThunderCompute. "NVIDIA A100 vs H100 for AI Training and Inference (May 2026)". https://www.thundercompute.com/blog/nvidia-a100-vs-h100
- Premai. "Speculative Decoding 2-3× Faster LLM Inference (2026)". https://blog.premai.io/speculative-decoding-2-3x-faster-llm-inference-2026/
- Wikipedia. "Rubin (microarchitecture)". https://en.wikipedia.org/wiki/Rubin_(microarchitecture)
- Wikipedia. "NVLink". https://en.wikipedia.org/wiki/NVLink
- Red Hat Developer. "Post-training methods for language models" (Nov 2025). https://developers.redhat.com/articles/2025/11/04/post-training-methods-language-models
- Fluence. "Designing GPU Clusters, Memory & Scaling for AI Workloads (2026)". https://www.fluence.network/blog/designing-ai-gpu-workloads/
- vLLM documentation. "Optimization and Tuning". https://docs.vllm.ai/en/stable/configuration/optimization/
- Jarvis Labs. "Disaggregated Prefill-Decode: The Architecture Behind Meta's LLM Serving". https://jarvislabs.ai/blog/llm-optimization-disaggregated-prefill-decode
- VALDI Docs. "H100 Performance — Llama 3.1 inference testing". https://docs.valdi.ai/llms/performance/gpu/H100/llama3.1-inference-testing/
- CoreWeave. "Breakthrough AI performance with NVIDIA GB200 and H200 GPUs in MLPerf Inference v5.0". https://www.coreweave.com/blog/coreweave-delivers-breakthrough-ai-performance-with-nvidia-gb200-and-h200-gpus-in-mlperf-inference-v5-0
- HPCwire. "MLPerf v5.0 Reflects the Shift Toward Reasoning in AI Inference". https://www.hpcwire.com/2025/04/02/mlperf-v5-0-reflects-the-shift-toward-reasoning-in-ai-inference/

---

*End of technical note. A follow-up piece on the economics — cost-per-token, depreciation schedules, second-hand markets, and grid-load implications — will build on this foundation. The underlying research draft is at `background/_research_drafts/training_v_inference_technical.md` for full source-level traceability.*
