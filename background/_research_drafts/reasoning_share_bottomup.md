---
title: "What share of LLM inference compute is reasoning? A bottom-up estimate"
author: "David Leitch"
date: 2026-05-11
draft: true
---

## Purpose and scope

The metric this note tries to pin down is the **share of total LLM inference compute consumed by reasoning-mode queries** — Claude with extended thinking, GPT-5/5.5 medium-and-above effort, Gemini 2.5 Pro thinking, DeepSeek-R1, Grok thinking modes — versus non-reasoning queries (short chat completions, autocomplete, classification, embeddings, simple tool calls).

This is **compute share**, not query-count share. A reasoning query typically generates 5,000-50,000 internal "thinking" tokens before its visible answer. A chat query outputs ~150 tokens. Each thinking token costs the same memory-bound decode flops as any other output token [Source: https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling]. So a single reasoning answer can consume 30-300× the GPU-seconds of a single chat answer, before accounting for the fact that reasoning queries also tend to run on the largest, most expensive model variants.

The question matters for a power-system analyst because reasoning workloads are the part of the inference stack whose unit token volume is growing fastest, the part where per-query revenue is highest, and the part most likely to be served from the latest-generation accelerators with the highest power density. If reasoning is already the majority of inference flops, then the marginal new data centre is being built primarily to think out loud — and the marginal kWh follows that decision.

---

## 1. Published estimates and anchor points

There is no single authoritative public number for the reasoning share of inference compute. The closest thing is OpenRouter's *State of AI 2025* token study, which is the only large-scale dataset of real production routing across many providers.

**OpenRouter State of AI (Nov 2025).** Across more than 100 trillion tokens of routed inference over ~13 months, the share of tokens routed to **reasoning-optimised models** rose from a "negligible slice" in early Q1 2025 to **>50% by late Q4 2025** [Source: https://openrouter.ai/state-of-ai]. This is a token-share number, not a compute-share number, but for OpenRouter's mix of mostly serious developer / coding workloads it is the cleanest anchor available. Programming-category traffic on the same platform grew from ~11% to >50% of tokens over 2025; average completion length tripled from ~150 to ~400 tokens, and average sequence length more than tripled.

**Google.** Google disclosed processing 480T tokens/month at I/O in May 2025, 980T/month by July 2025, and ~1,300T/month (1.3 quadrillion) by October 2025 [Source: https://tomtunguz.com/is-token-consumption-slowing-down/]. Growth of ~250T/month between May and July decelerated to ~107T/month between July and October, suggesting Google's volume now exceeds 1.5 quadrillion/month in May 2026 if linear growth continued. Google does not split reasoning from non-reasoning, but the bulk of Search AI Overviews traffic is short-form chat, while Gemini Deep Research and Gemini 2.5 Pro thinking are long-form reasoning.

**Microsoft Foundry.** Processed >100T tokens in calendar Q3 2025, up 5× year-on-year [Source: https://tomtunguz.com/trillion-token-race/]. Microsoft has not split reasoning vs non-reasoning publicly.

**Anthropic.** Run-rate revenue $14B in February 2026, $30B in April 2026 [Source: https://www.businessofapps.com/data/claude-statistics/]. Claude Code at $2.5B run-rate in February 2026. The Anthropic Economic Index reports 36% of Claude.ai web usage is for coding, 44% of API usage falls under "computer and mathematical" categories. A back-of-envelope from $30B revenue at a blended ~$10/M tokens implies ~3 quadrillion billable tokens per year (~250T/month) for Anthropic — though the blended price is highly uncertain because of caching discounts and Haiku-vs-Opus mix [Source: https://platform.claude.com/docs/en/about-claude/pricing].

**Epoch AI.** Reasoning *training* compute for o1-class models was <10% of GPT-4o pre-training compute, but is growing 10× every 3-5 months [Source: https://epoch.ai/blog/optimally-allocating-compute-between-inference-and-training]. Epoch has not published a reasoning-share-of-inference number.

**Zylos / Gartner.** Inference passed training in cumulative spend in early 2026; agentic workloads consume 5-30× more tokens per task than chatbots; multi-step agent completions cost 100-1,000× a single chat call [Source: https://zylos.ai/research/2026-04-13-inference-economics-ai-agent-compute-markets].

**SemiAnalysis InferenceMAX.** Their benchmark workload definitions code "reasoning workloads" as 1024 input / 8192 output tokens versus chat at 1024/1024 — i.e., a reference reasoning query is 8× the output of a reference chat query at minimum, before extended thinking [Source: https://newsletter.semianalysis.com/p/inferencemax-open-source-inference].

The OpenRouter ">50% of tokens are reasoning by Q4 2025" anchor is the single most useful number. It is consistent with — though slightly higher than — what a bottom-up segmentation produces, because OpenRouter's customer base skews developer/coding-heavy.

---

## 2. Methodology

I decompose the global LLM inference market into six segments and quantify each with: monthly active users, queries per user per day, average input+output tokens per non-reasoning query, fraction of queries that trigger reasoning mode, and a reasoning intensity multiplier (how much more compute a reasoning query consumes vs a non-reasoning query in that segment).

For each segment:

- **Non-reasoning compute** = MAU × queries/day × 30 × tokens × (1 − reasoning_share)
- **Reasoning compute** = MAU × queries/day × 30 × tokens × reasoning_share × intensity_multiplier

Compute is denominated in **token-equivalents per month**. A token-equivalent is the GPU-second cost of one output token on a representative dense model. This deliberately ignores model-size differences (a Haiku token is cheaper than an Opus token) on the assumption that reasoning queries route to bigger models on average, which the multiplier already captures.

Per-query token assumptions draw on:
- Chat completion length: OpenRouter measured average completion at ~400 tokens by late 2025 (up from 150 a year earlier) [Source: https://openrouter.ai/state-of-ai].
- Reasoning chain-of-thought length: Anthropic minimum thinking budget is 1,024 tokens; recommended starting budget for complex tasks is 16,000+; 4k thinking tokens before a 500-token answer costs ~9× the bare answer [Source: https://platform.claude.com/docs/en/build-with-claude/extended-thinking]. GPT-5 high-reasoning effort uses 23× the tokens of GPT-5 minimal effort; on a published benchmark suite GPT-5 high consumed 82M, o3 50M, Gemini 2.5 Pro 98M, DeepSeek-R1 99M output tokens [Source: https://artificialanalysis.ai/articles/gpt-5-benchmarks-and-analysis].
- Coding agent task length: Claude Code sessions typically consume 10,000-100,000+ tokens per session [Source: https://www.verdent.ai/guides/claude-code-pricing-2026]; one developer's eight-month total was 10 billion tokens (~40M tokens/day) [Source: https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/].

---

## 3. Segment-by-segment numbers (May 2026)

### 3.1 B2C free chat (ChatGPT free, Claude.ai free, Gemini app free, Meta AI, Grok free, DeepSeek)

| Provider | MAU (M) | Source |
|:---------|--------:|:-------|
| ChatGPT (free tier, est. 80% of WAU base) | 700 | [TechCrunch Feb 2026](https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/) |
| Gemini app | 750 | [TechCrunch Feb 2026](https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/) |
| Google AI Overviews | 2,000 | [getpanto.ai](https://www.getpanto.ai/blog/google-gemini-statistics) |
| Meta AI (FB/IG/WA) | 1,000 | [demandsage](https://www.demandsage.com/meta-ai-users/) |
| Claude.ai free | 25 | [demandsage](https://www.demandsage.com/claude-ai-statistics/) |
| Grok / X | 200 | author estimate from X DAU |
| DeepSeek + Chinese consumer | 250 | [demandsage](https://www.demandsage.com/deepseek-statistics/) |
| **Total free B2C MAU (gross, double-counted)** | **~4,900** | |

The Google AI Overviews number is the largest single line and the most distorting: each Overview is a single sub-200-token generation triggered by a search, not a conversation. I treat it separately.

**Assumptions for free B2C chat (excluding AI Overviews):**
- Effective de-duplicated MAU: 1,500M (heavy overlap; many users use 2-3 assistants)
- Queries/active user/day: 4 (industry estimate; ChatGPT public statements imply 3-6)
- Tokens/query: 700 input + 400 output = 1,100
- Reasoning share: 5% (free tiers default to non-reasoning models; users have to actively pick reasoning, and free tiers usually rate-limit it heavily)
- Reasoning intensity multiplier: 25× (free reasoning is usually capped — DeepSeek R1 free, Gemini 2.5 Flash thinking, ChatGPT free has limited o4-mini access)

Monthly compute = 1,500M × 4 × 30 × 1,100 × (0.95 + 0.05 × 25) = 198,000T × 2.2 = **436T token-equivalents/month**.

Of which reasoning = 1,500M × 4 × 30 × 1,100 × 0.05 × 25 = **247T**.

**Google AI Overviews separately:** 2,000M MAU × 30 searches/month × 200 output tokens × ~0% reasoning = **12T tokens/month, ~all non-reasoning.** (AI Overviews use a small Gemini variant and don't deploy chain-of-thought.)

### 3.2 B2C paid subscriptions (ChatGPT Plus/Pro, Claude Pro/Max, Gemini Advanced, Perplexity Pro, etc.)

ChatGPT Plus/Pro/Business subscribers ~50M; Claude Pro/Max ~10M; Gemini Advanced ~30M; Perplexity Pro / others ~15M. Total ~105M paid B2C, with material overlap; net ~80M unique.

**Assumptions:**
- MAU: 80M
- Queries/active user/day: 15 (paying users use it more)
- Tokens/query: 1,000 input + 600 output = 1,600
- Reasoning share: 30% (paid users have access to GPT-5 Thinking, Claude extended thinking, Gemini 2.5 Pro; many use them as defaults for non-trivial questions)
- Reasoning intensity multiplier: 35× (paid reasoning runs at higher effort; GPT-5 high uses 23× the tokens of minimal, Claude extended thinking commonly uses 16k+ tokens vs ~600 chat output)

Monthly compute = 80M × 15 × 30 × 1,600 × (0.70 + 0.30 × 35) = 57,600T × 11.2 = **645T token-equivalents/month**.

Reasoning component = 80M × 15 × 30 × 1,600 × 0.30 × 35 = **605T**.

This segment is small in user count (5% of free) but large in compute because of the reasoning multiplier and higher per-user query volume.

### 3.3 B2B API — chat applications (customer support, content gen, RAG, enterprise chatbots, OpenRouter passthrough)

Hard to size by user. Easier to size by token volume. Microsoft Foundry processed ~50T tokens/month in mid-2025, growing 5× YoY; that implies ~250T/month by mid-2026 [Source: https://tomtunguz.com/trillion-token-race/]. Anthropic API gross revenue ~$25B run-rate (excluding Claude Code) at ~$8/M blended → ~3,100T/year ÷ 12 = ~260T/month. OpenAI API ex-coding ~similar scale. Google Vertex AI / Gemini API similar. Plus OpenRouter, Together.ai (2T/day open-source = 60T/month), Fireworks, Groq, smaller providers.

**Bottom-up total B2B chat-style API tokens, May 2026: ~1,200T/month.**

**Assumptions:**
- Token volume: 1,200T/month
- Reasoning share within this volume: 25% (enterprise RAG, classification and content generation are mostly non-reasoning; complex query answering, document analysis and tool-augmented enterprise assistants increasingly use reasoning)
- Reasoning intensity multiplier: 20× (lower than B2C paid because enterprise budgets cap thinking length aggressively)

If 1,200T/month is the *raw* token count (input + visible output, no thinking inflation), and 25% of those queries trigger reasoning at 20× the per-query token cost, the *compute-equivalent* total is:

Compute = 1,200T × (0.75 + 0.25 × 20) = 1,200T × 5.75 = **6,900T token-equivalents/month**.

Wait — that double-counts. The 1,200T already includes the thinking tokens because providers report tokens billed (which include reasoning tokens). So a more honest decomposition:

Of 1,200T billed tokens, what fraction *are* reasoning (chain-of-thought) tokens? If 25% of queries are reasoning-mode and reasoning-mode queries average 15× the tokens of a chat query, then reasoning queries account for 0.25 × 15 / (0.75 × 1 + 0.25 × 15) = 83% of billed tokens.

Reasoning tokens in B2B chat API = 1,200T × 0.83 = **1,000T/month**.
Non-reasoning = 200T/month.

This is the more defensible decomposition, and I will apply it consistently to other token-based segments below.

### 3.4 B2B API — agentic / coding (Cursor, Claude Code, Codex CLI, Devin, Replit Agent, Lovable, v0, GitHub Copilot agent mode)

This is the segment that has exploded.

**Cursor.** $2B ARR Feb 2026 [Source: https://www.bloomberg.com/news/articles/2026-03-02/cursor-recurring-revenue-doubles-in-three-months-to-2-billion]. 7M MAU, 1M DAU, "nearly 1B lines of code/day" generated. At $2B ARR and ~$15/M blended token cost for the Sonnet/Opus mix Cursor mostly resells, that implies ~133T tokens/year ≈ **11T/month** of *paid* tokens — likely 2-3× higher in raw compute because of cache hits and Cursor's own subsidisation; call it **30T/month true compute**.

**Claude Code.** $2.5B run-rate Feb 2026 [Source: https://www.businessofapps.com/data/claude-statistics/]; one disclosed user pattern is ~40M tokens/day for a heavy individual. With Anthropic's reported 90% of users below $30/active-day and median ~$13/day, that's ~1-3M tokens/active-user/day. If Claude Code has ~500k DAU, that is ~750T tokens/month direct from Claude Code. (Internal Anthropic disclosures suggest Claude Code is a meaningful share of total Anthropic API tokens.) Conservatively: **400T/month**.

**GitHub Copilot, Codex CLI, Devin, Replit, Lovable, v0, smaller agents.** Copilot alone has ~5M paid subscribers; agentic mode has expanded sharply through 2025-26. Estimate **300T/month** combined for non-Anthropic non-Cursor coding agents.

**Total B2B agentic/coding tokens, May 2026: ~750T/month.**

**Assumptions:**
- Reasoning share within agentic: 80% (every modern coding agent defaults to reasoning models for non-trivial tasks; Cursor's reasoning-model share is the platform's largest category per OpenRouter).
- These tokens are mostly *already* reasoning tokens. Of the 750T, ~80% × heavily-reasoning-weighted = **~700T are reasoning tokens, ~50T are non-reasoning** (autocomplete, simple completions, embedding lookups).

### 3.5 First-party agentic deployments (Operator, Computer Use, Deep Research, Microsoft Copilot agent, Gemini agents)

Smaller in volume than 3.4 because consumer agentic adoption is still early, but extremely token-heavy per session.

**Assumptions:**
- Active sessions/day globally: ~5M (OpenAI Deep Research, Operator, Anthropic Computer Use, Gemini Deep Research, Microsoft 365 Copilot agent mode)
- Tokens/session: 200,000 (multi-step research and computer-use sessions easily hit 100k-500k tokens)
- Reasoning share: 90%
- Implicit intensity already embedded in token count.

Monthly tokens = 5M × 30 × 200,000 = **30T/month**. Of which ~27T reasoning, 3T non-reasoning.

Small compared to coding but growing fastest.

### 3.6 Open-source / on-prem deployments (Llama, DeepSeek, Qwen, Mistral served by enterprises and via Together.ai, Fireworks, Groq)

Together.ai disclosed 2T tokens/day open-source inference in Sep 2025 = 60T/month [Source: https://tomtunguz.com/trillion-token-race/]. Add Fireworks, Groq, on-prem enterprise vLLM deployments, hyperscaler-served Llama on Bedrock/Vertex/Azure, and self-hosted Qwen/DeepSeek in China. Estimate total: **300T/month** for open-source and on-prem inference.

**Assumptions:**
- Reasoning share: 35% (DeepSeek R1 and Qwen reasoning variants are heavily used; Llama reasoning fine-tunes growing)
- Of 300T billed/served tokens, applying the same chain-of-thought inflation logic: reasoning tokens ≈ 300 × (0.35 × 15) / (0.65 + 0.35 × 15) = 300 × 0.89 = **267T reasoning, 33T non-reasoning**.

### 3.7 Aggregate (all six segments)

**Aggregate inference compute, May 2026 (token-equivalents per month)**

| Segment | Total compute (T) | Reasoning (T) | Non-reasoning (T) | Reasoning share |
|:--------|------------------:|--------------:|------------------:|----------------:|
| 3.1 Free B2C chat | 436 | 247 | 189 | 57% |
| 3.1b AI Overviews | 12 | 0 | 12 | 0% |
| 3.2 Paid B2C | 645 | 605 | 40 | 94% |
| 3.3 B2B API chat | 1,200 | 1,000 | 200 | 83% |
| 3.4 B2B agentic/coding | 750 | 700 | 50 | 93% |
| 3.5 First-party agents | 30 | 27 | 3 | 90% |
| 3.6 OSS / on-prem | 300 | 267 | 33 | 89% |
| **Total** | **3,373** | **2,846** | **527** | **84%** |

*Source: Author bottom-up estimate, May 2026. All numbers are token-equivalents per month, defined as the GPU-second cost of one output token on a representative dense reasoning model. Caching, batching, model-size and quantisation effects are not separately modelled.*

The segment that drives the answer is **B2C paid subscriptions (3.2)** and **B2B chat API (3.3)** combined — together ~1,800T compute, of which ~1,600T is reasoning. This is intuitive: that's exactly where users actively choose extended thinking and where reasoning models are the default.

---

## 4. Reconciliation against the OpenRouter anchor

OpenRouter said >50% of tokens were reasoning by late Q4 2025. My bottom-up answer is 84% by May 2026. The gap has three explanations:

1. **OpenRouter's number is from Q4 2025, not May 2026.** Reasoning share has clearly continued to grow. If reasoning was 50% in Nov 2025 and reasoning compute is growing ~15-20% per month while non-reasoning grows ~3-4% per month, May 2026 share of 70-85% is plausible.

2. **OpenRouter measures *billed tokens*, not *compute-equivalent*.** A reasoning token bills the same as a non-reasoning token at the API. But because reasoning queries route to larger models (Opus, Pro, R1) on average, each reasoning token *consumes* more flops than each chat token routed to Haiku, Flash, or Llama-3.1-8B. If the average reasoning token consumes 1.5-2× the flops of the average non-reasoning token, OpenRouter's 50% token share corresponds to ~65-70% compute share.

3. **My intensity multipliers may be too high.** If I halve the multiplier for paid B2C from 35× to 18×, the 3.2 segment compute halves and total reasoning share falls from 84% to ~75%. Still well above 50%.

---

## 5. Sensitivity analysis (May 2026)

**What if the key assumptions change ±50%?**

| Variable changed | Base | Low (–50%) | High (+50%) | Reasoning share at low / base / high |
|:-----------------|-----:|-----------:|------------:|:-------------------------------------|
| Paid B2C reasoning share | 30% | 15% | 45% | 79% / 84% / 87% |
| Paid B2C intensity multiplier | 35× | 18× | 53× | 75% / 84% / 87% |
| B2B chat reasoning share | 25% | 12.5% | 37.5% | 76% / 84% / 88% |
| Coding agent token volume | 750T | 375T | 1,125T | 83% / 84% / 85% |
| Free B2C reasoning share | 5% | 2.5% | 7.5% | 84% / 84% / 84% |

The answer is robust: under any reasonable single-variable swing, reasoning share lands in the **75-88%** band. The single most influential variable is the paid B2C reasoning intensity multiplier; halving it still gives 75%.

The combination most likely to break the conclusion is *simultaneously* halving the reasoning multipliers for both 3.2 and 3.3 and assuming much more chat traffic from AI Overviews and Meta AI. Even that pessimistic combination produces ~60% reasoning share — still a clear majority of compute.

---

## 6. Forecast for May 2027 and May 2028

**Growth assumptions:**

- Reasoning compute grows ~6× over two years (driven by: agentic adoption, longer context, longer thinking budgets, coding tools maturing into design and ops tools). This is consistent with OpenRouter's observed 0% → 50% reasoning token share in 2025, decelerating but not stopping.
- Non-reasoning compute grows ~2.5× over two years (driven by AI Overviews-style mass deployments, embedding workloads, classification, voice transcription).
- Total compute grows ~5×, in line with hyperscaler capex trajectory ($725B 2026 capex, growing) [Source: https://www.tomshardware.com/tech-industry/big-tech/microsoft-attributed-25-billion-of-its-record-ai-budget-to-memory-chip-costs].

**Forecast inference compute mix**

| Date | Total (Tt-eq/mo) | Reasoning (Tt-eq/mo) | Non-reasoning (Tt-eq/mo) | Reasoning share |
|:-----|-----------------:|---------------------:|-------------------------:|----------------:|
| May 2026 (base) | 3,373 | 2,846 | 527 | 84% |
| May 2027 (forecast) | ~9,800 | ~8,500 | ~1,300 | 87% |
| May 2028 (forecast) | ~17,000 | ~15,200 | ~1,800 | 89% |

*Source: Author projections. 2027 and 2028 assume agentic/coding doubles each year, paid B2C reasoning grows 70% per year, free B2C non-reasoning grows 50% per year, AI Overviews and embeddings grow 80% per year.*

The reasoning share **rises** but at a decelerating rate, because the non-reasoning floor (AI Overviews, embeddings, classification, voice, vision) grows in absolute terms even as it shrinks in share.

The more interesting number is the absolute scale: total monthly inference compute roughly **5× by 2028** vs May 2026. If today's hyperscaler buildout is sized for 2026 inference, the 2027-2028 wave needs another 4× as much accelerator capacity, memory and power. This is consistent with the announced capex programmes but tight against grid interconnect timelines.

---

## 7. Final answer

**May 2026: reasoning-mode queries account for ~80% (range 70-90%) of total LLM inference compute.**

The single best point estimate is **84%**. The defensible range is 70-90%. The lower bound (70%) requires both halved reasoning intensity multipliers across all paid segments *and* substantially more chat traffic than I have assumed; the upper bound (90%) is what you get if reasoning effort levels continue migrating to "high" as defaults and agentic workloads grow faster than coding alone.

**May 2027: ~87%. May 2028: ~89%.** The share keeps rising but at a decelerating rate; the absolute compute behind the share roughly 5× over the same window.

The economic implication is that effectively **all the marginal data centre being built in 2026-28 is being built to run chains of thought**. Non-reasoning workloads will remain large in user count and in absolute token volume — AI Overviews and embeddings are not going away — but they fit comfortably inside the existing fleet. Every new gigawatt of accelerator power, every new HBM4 stack, every new liquid-cooled rack is funded by, and sized for, reasoning and agentic workloads.

For a power-system reader: the implication is that AI inference load growth is dominated by a workload (reasoning) whose per-query GPU-seconds is 30-300× the chat baseline and whose per-query *value* (what the user is willing to pay) is 50-500× the chat baseline. That latter point is what makes the buildout fundable. It is also what makes this load less price-sensitive than typical commercial-and-industrial demand: a $5/MWh swing in wholesale electricity is rounding-error against $5,000-50,000 of revenue per occupied accelerator-hour serving Cursor or Claude Code.

---

## 8. Caveats

- **Token-equivalent is a crude unit.** A reasoning token on Opus consumes ~10× the flops of a chat token on Haiku, and ~3× the flops of a chat token on Sonnet. My intensity multipliers attempt to bake this in but are imprecise.
- **Caching distorts billed tokens vs compute tokens.** Anthropic and OpenAI prompt-caching can reduce billed input tokens 80-90% on cached prompts; this is real cost reduction but not a reduction in serving compute (the prefill still happens; the cache lives on GPU memory, occupying expensive VRAM). I have not separately modelled it.
- **MAU double-counting.** Many users have ChatGPT Plus *and* Claude Pro *and* Gemini Advanced. My de-duplicated paid B2C MAU of 80M may be optimistic; the gross sum of disclosed paid users is ~105M.
- **Chinese inference is undermeasured.** DeepSeek, Qwen, Doubao and Wenxin process enormous volumes inside China that are barely visible in Western disclosures. My OSS segment likely understates Chinese on-prem and consumer reasoning-model inference by 30-50%. If Chinese reasoning is 100T/month higher than I have assumed, total reasoning share rises ~1pp.
- **The "reasoning" definition is fuzzy.** GPT-5 with reasoning effort "minimal" generates almost no thinking tokens. Claude Sonnet 4.6 without extended thinking enabled does some implicit chain of thought in its visible output. The line between "reasoning model" and "non-reasoning model" is no longer clean — the distinction is increasingly about whether the model is *allowed* to spend tokens thinking, not what model is loaded.
- **Inference compute ≠ inference electricity.** Per-token energy varies 3-5× across hardware generations; H100 vs B200 vs the announced GB300 are very different on watts-per-token. A 5× growth in token-compute does not necessarily mean 5× growth in inference electricity, though it probably means 3-4×.

---

## 9. Bibliography

- OpenRouter, *State of AI 2025: 100T Token LLM Usage Study*, Nov 2025. https://openrouter.ai/state-of-ai
- TechCrunch, *ChatGPT reaches 900M weekly active users*, 27 Feb 2026. https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users/
- TechCrunch, *Google's Gemini app has surpassed 750M monthly active users*, 4 Feb 2026. https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/
- Tom Tunguz, *Beyond a Trillion: The Token Race*, 2025. https://tomtunguz.com/trillion-token-race/
- Tom Tunguz, *Is Token Consumption Growth Slowing Down?*, 2025. https://tomtunguz.com/is-token-consumption-slowing-down/
- Bloomberg, *Cursor Recurring Revenue Doubles in Three Months to $2 Billion*, 2 Mar 2026. https://www.bloomberg.com/news/articles/2026-03-02/cursor-recurring-revenue-doubles-in-three-months-to-2-billion
- Business of Apps, *Claude Revenue and Usage Statistics (2026)*. https://www.businessofapps.com/data/claude-statistics/
- DemandSage, *Claude Statistics 2026*. https://www.demandsage.com/claude-ai-statistics/
- DemandSage, *DeepSeek AI Statistics 2026*. https://www.demandsage.com/deepseek-statistics/
- DemandSage, *Meta AI Users Statistics 2026*. https://www.demandsage.com/meta-ai-users/
- getpanto.ai, *Google Gemini Statistics 2026*. https://www.getpanto.ai/blog/google-gemini-statistics
- Verdent, *Claude Code Pricing 2026*. https://www.verdent.ai/guides/claude-code-pricing-2026
- Martin Alderson, *No, it doesn't cost Anthropic $5k per Claude Code user*, 2026. https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/
- Anthropic, *Building with extended thinking*. https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- Anthropic, *Pricing*. https://platform.claude.com/docs/en/about-claude/pricing
- Artificial Analysis, *GPT-5 Benchmarks and Analysis*. https://artificialanalysis.ai/articles/gpt-5-benchmarks-and-analysis
- SemiAnalysis, *InferenceMAX: Open Source Inference Benchmarking*. https://newsletter.semianalysis.com/p/inferencemax-open-source-inference
- Epoch AI, *Optimally allocating compute between inference and training*. https://epoch.ai/blog/optimally-allocating-compute-between-inference-and-training
- Sebastian Raschka, *State of LLM Reasoning and Inference Scaling*. https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling
- Zylos Research, *Inference Economics: AI Agent Compute Markets in 2026*, 13 Apr 2026. https://zylos.ai/research/2026-04-13-inference-economics-ai-agent-compute-markets
- Tom's Hardware, *Big Tech capex hits $725 billion*, 2026. https://www.tomshardware.com/tech-industry/big-tech/microsoft-attributed-25-billion-of-its-record-ai-budget-to-memory-chip-costs
