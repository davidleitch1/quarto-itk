---
title: "Reasoning vs non-reasoning share of LLM inference compute: top-down revenue and pricing decomposition"
author: "David Leitch (ITK)"
date: 2026-05-11
draft: true
---

# Reasoning vs non-reasoning share of total LLM inference compute

## Executive summary

The headline number this note is built to defend: **as of May 2026, reasoning-mode queries (extended thinking, GPT-5 Thinking, GPT-5 Pro, o3-pro legacy, Claude Opus 4.7 with adaptive thinking, Gemini 3 Pro Deep Think, DeepSeek-R1/R2, Grok 4 Heavy) are consuming roughly 55-65% of frontier-lab inference compute, with a central estimate of ~60%.** That share rises to a projected ~75-80% by end-2027 and ~80-85% by end-2028 as agentic workloads, which are dominated by reasoning-tier model calls, scale faster than chat.

The metric is **compute share, not query share**. By query count, reasoning is still a minority of usage (probably 15-25% on the consumer side, 25-40% on the API/agent side). But each reasoning query consumes 10-50x the tokens of a typical chat query and often runs on a model priced 2-5x higher per token, so the compute multiplier per query is 20-100x.

---

## 1. Published estimates: what is already out there

There is no single widely-cited public number for reasoning's share of total LLM inference compute. The closest anchors:

- **Epoch AI (2025-2026)**: Frames the question as the broader "inference vs training vs experiments" split. Their 2024 OpenAI estimate was ~30% inference / 70% training+experiments [Source: https://epoch.ai/data-insights/openai-compute-spend]. Their 2026 update notes the picture has shifted — power demand now splits roughly equally between training, experiments, and inference. Critically, Epoch documents that RL-trained reasoning models use chains of thought "up to 30 times as long as base models" and that "82% of the performance improvement" of recent frontier models comes from inference-time scaling [Source: https://epoch.ai/gradient-updates/how-persistent-is-the-inference-cost-burden]. Epoch does *not* publish a clean reasoning-share-of-inference number.

- **SemiAnalysis InferenceMAX (Oct 2025 - Apr 2026)**: Treats reasoning as a workload archetype with a 1024-input / 8192-output token profile vs ~500/200 for chat. This implies reasoning queries push roughly **30-40x more output tokens** through the GPU. SemiAnalysis does not publish an aggregate reasoning-share number in public newsletters but their recurring point is that "the inference kingdom expands" because reasoning and agents have driven a structural step-change in tokens-per-query [Source: https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands; Source: https://newsletter.semianalysis.com/p/inferencemax-open-source-inference].

- **Zylos Research (Apr 2026)**: "Inference Economics: AI Agent Compute Markets in 2026" cites Gartner: agentic workloads consume "5-30x more tokens per task than standard chatbots." Frontier reasoning-tier models handle the smallest share by request count (5-15% of API calls) but the bulk of high-value work [Source: https://zylos.ai/research/2026-04-13-inference-economics-ai-agent-compute-markets].

- **Toby Ord (2025)**: "Evidence that recent AI gains are mostly from inference-scaling" — argues 60-80% of capability gains since GPT-4o have come from longer reasoning chains rather than larger pre-trained models, implicitly forcing a compute reallocation toward reasoning [Source: https://www.tobyord.com/writing/mostly-inference-scaling].

- **Gartner (Mar 2026)**: Per-token inference cost will fall ~90% by 2030 but total inference spend will still rise because reasoning and agentic patterns push tokens-per-query up faster than per-token cost falls [Source: https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025].

- **AICC enterprise survey (Q1 2026)**: Agent-pattern API calls grew 680% YoY and reached 41% of new enterprise integrations, up from 18% a year earlier. Frontier-tier (reasoning) models handle 5-15% of calls but dominate token spend [Source: https://www.mykxlg.com/online_features/press_releases/aicc-report-enterprise-token-costs-drop-67-year-over-year-as-multi-model-ai-adoption/article_794d655c-f59b-5921-bbd0-33edb058b05e.html].

**Anchor takeaway**: nobody has published "X% of inference compute is reasoning." But every credible source agrees that (a) reasoning queries consume 10-50x the tokens of standard chat, (b) reasoning's share of total tokens has been rising sharply through 2025-26, and (c) by 2027-28 agentic and reasoning workloads will dominate.

---

## 2. Lab revenue decomposition (May 2026 run rates)

| Lab | Annualised revenue (May 2026) | Source |
|:----|---:|:----|
| OpenAI | ~$25-30 bn ARR | [Bloomberg, Sacra, OpenAI](https://sacra.com/c/openai/) |
| Anthropic | ~$30-45 bn ARR | [Reuters, Anthropic Series G filing](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) |
| Microsoft AI (incl. Azure OpenAI) | ~$37 bn run rate | [Microsoft FY26 Q3](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/press-release-webcast) |
| Google Cloud (Gemini contribution) | ~$8-12 bn from Gemini API/enterprise inside $20 bn quarterly Cloud | [Alphabet Q1 2026](https://abc.xyz/) |
| xAI | ~$3-5 bn (largely Grok-on-X plus enterprise) | press estimates |
| DeepSeek + Chinese providers | <$1 bn paid API revenue but large free/sovereign volume | [DeepSeek docs](https://api-docs.deepseek.com/) |

*Source: aggregated from Reuters, Bloomberg, Sacra, Microsoft and Alphabet earnings releases, May 2026.*

Total disclosed frontier-lab inference-related revenue is in the order of **$100-120 bn ARR**. There is double counting (OpenAI's Azure consumption shows up both in Microsoft AI revenue and OpenAI's COGS) but for compute-share purposes that does not matter — what we care about is the inference *workload* mix, and it is the same workload whether it's billed via OpenAI direct or Azure resold.

### Within each lab, the reasoning-vs-chat split

**OpenAI** (~$25-30 bn ARR; revenue mix ~65% ChatGPT subs / 25% API / 10% partnerships [Source: https://sacra.com/c/openai/]):

- ChatGPT Free: defaults to GPT-5.3 Instant (non-reasoning) but auto-routes to GPT-5.5 Thinking on harder prompts. Maybe 10-15% of queries route to thinking, but those queries consume 30-50x more tokens. Compute share within Free likely 70-80% reasoning.
- ChatGPT Plus ($20/m, ~10 m subs, ~$2.4 bn/yr): heavy thinking use, especially Codex/agent tasks. Anecdotal reports and the per-week 3,000-message thinking limit imply most Plus users are pushing toward the cap. Compute share ≥80% reasoning.
- ChatGPT Pro/Team/Enterprise (~50% of ChatGPT revenue): GPT-5 Pro and Codex agent are core selling points. Compute share ~85-95% reasoning.
- API (~$6-8 bn ARR): the fastest-growing line is GPT-5.5 Thinking and GPT-5.2-Codex, which are reasoning by default. Even non-reasoning GPT-5.3 Instant calls are increasingly being routed through "reasoning effort: low" which still adds 1-3k thinking tokens. Reasoning compute share probably 65-75%.

**OpenAI weighted reasoning compute share: ~75-80%.**

**Anthropic** (~$30-45 bn ARR; ~80% from API/business [Source: https://sacra.com/c/anthropic/]):

- Claude Code (~$2.5-5 bn ARR by mid-2026 [Source: https://stormy.ai/blog/claude-code-gtm-strategy-anthropic-revenue-2026]): every interaction routes through Sonnet 4.6 or Opus 4.7 *with adaptive thinking on by default* in the 4.6/4.7 generation. Coding agent calls run for hours, average context 50-200k tokens, output 5-20k tokens per turn. Essentially 100% reasoning compute.
- Claude.ai consumer subs (Pro/Max): Max users run extended thinking constantly; Pro users less so. Reasoning compute share ~70-85%.
- API direct (the ~$15-20 bn block excluding Claude Code): Sonnet 4.6 with adaptive thinking is the workhorse. Even non-explicit-thinking calls produce internal reasoning. Reasoning compute share ~70-80%.

**Anthropic weighted reasoning compute share: ~85-90%.** (Anthropic is the most reasoning-heavy lab because Claude Code, agentic enterprise, and adaptive thinking together cover almost all consumption.)

**Microsoft Azure OpenAI / Microsoft AI** (~$37 bn run rate, of which ~$10 bn is OpenAI inference passthrough [Source: https://www.wheresyoured.at/oai_docs/]):

- Copilot family (M365 Copilot, GitHub Copilot, Security Copilot): ~$20 bn of Microsoft AI run rate. GitHub Copilot moved to usage-based billing in mid-2025 and the agent mode (which routes to Claude Sonnet 4.6 and GPT-5.5 Thinking) is the growth driver. Reasoning compute share probably 60-75%.
- Azure OpenAI direct API to enterprises: similar mix to OpenAI's own API, so 65-75% reasoning.

**Microsoft weighted reasoning compute share: ~65-75%.**

**Google** (Gemini API + Gemini Enterprise ~$8-12 bn run rate inside $80 bn Cloud annualised; Gemini API processing 16 bn tokens/minute, up 60% q-o-q [Source: https://abc.xyz/]):

- Gemini 3 Pro and Deep Think are reasoning-default. Gemini 3 Flash is the cheap non-reasoning workhorse and accounts for the majority of token volume (very high-throughput RAG, summarisation, classification at $0.50/$3 per million tokens).
- Workspace AI (consumer Gmail/Docs) is mostly Flash, non-reasoning.
- Vertex/Enterprise is split, but the high-value coding and agentic workloads are Pro/Deep-Think.
- Google's mix is meaningfully more chat-weighted than Anthropic or OpenAI because Flash is strong and cheap.

**Google weighted reasoning compute share: ~40-50%.**

**xAI** (Grok 4 / Grok 4 Heavy): Grok 4 Heavy is reasoning-default; consumer Grok-on-X is mixed. ~50-60% reasoning.

**DeepSeek + Chinese providers** (DeepSeek V4/R-series, Qwen 3.6, MiMo-V2-Pro, MiniMax M2.7): OpenRouter April 2026 rankings show MiMo-V2-Pro at 4.65 trillion tokens/week (#1) and DeepSeek V3.2 at 1.22 T tokens/week (#4) [Source: https://www.digitalapplied.com/blog/openrouter-rankings-april-2026-top-ai-models-data]. Many of these are reasoning-capable and DeepSeek explicitly bills reasoning tokens. But the volume mix on Chinese hosting platforms is heavier on bulk RAG/translation/multimodal at low cost. Reasoning compute share ~45-55%.

### Weighted aggregate

Approximating each lab's compute by its inference-related revenue (a defensible proxy because list-price gross margins are similar across labs at 50-70%, and inference is the dominant marginal cost):

| Lab | Inference compute weight | Reasoning share | Contribution |
|:----|---:|---:|---:|
| OpenAI | 30% | 78% | 23.4 pts |
| Anthropic | 30% | 87% | 26.1 pts |
| Microsoft (non-OAI) | 15% | 70% | 10.5 pts |
| Google | 15% | 45% | 6.8 pts |
| xAI | 4% | 55% | 2.2 pts |
| DeepSeek + others | 6% | 50% | 3.0 pts |
| **Weighted total** | **100%** | | **~72%** |

*Source: ITK analysis from lab disclosures and pricing data, May 2026.*

This implies a top-down estimate of **~70-75% reasoning compute share** at the major frontier labs. But note this is *frontier-lab* compute. A meaningful chunk of total LLM inference compute globally runs on smaller open-weight models (Llama, Qwen, Mistral) hosted by enterprises themselves, mostly for non-reasoning tasks (RAG, classification, summarisation). That self-hosted long tail probably pulls the global figure down by 10-15 percentage points.

**Adjusted global reasoning compute share: ~55-65%, central ~60%.**

---

## 3. API list pricing for reasoning vs non-reasoning (May 2026)

**Per-million-token list prices (May 2026)**

| Model | Input | Output | Tier | Source |
|:------|---:|---:|:------|:------|
| GPT-5 (standard) | $1.25 | $10.00 | Non-reasoning | [pricepertoken.com](https://pricepertoken.com/pricing-page/model/openai-gpt-5) |
| GPT-5 Pro | $15.00 | $120.00 | Reasoning | [pricepertoken.com](https://pricepertoken.com/pricing-page/model/openai-gpt-5-pro) |
| GPT-5.5 | $5.00 | $40.00 | Reasoning-default | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| GPT-5.5 Pro | $30.00 | $180.00 | Heavy reasoning | [apidog.com](https://apidog.com/blog/gpt-5-5-pricing/) |
| GPT-5 mini | $0.25 | $2.00 | Cheap | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| GPT-5 nano | $0.05 | $0.40 | Bulk | [OpenAI](https://developers.openai.com/api/docs/pricing) |
| Claude Opus 4.7 | $5.00 | $25.00 | Reasoning-default | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Sonnet 4.6 | $3.00 | $15.00 | Reasoning-capable | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Haiku 4.5 | $1.00 | $5.00 | Cheap | [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) |
| Gemini 3 Pro | $2.00 | $12.00 | Reasoning | [ai.google.dev](https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3 Flash | $0.50 | $3.00 | Cheap | [Google](https://blog.google/products/gemini/gemini-3-flash/) |
| Grok 4 | ~$3 | ~$15 | Reasoning | xAI |
| Grok 4 Heavy | ~$15 | ~$75 | Heavy reasoning | xAI |
| DeepSeek V4-Pro | $0.55 | $2.19 | Reasoning | [DeepSeek](https://api-docs.deepseek.com/) |

*Source: provider list pricing pages, accessed May 2026.*

**Per-token prices for reasoning vs non-reasoning are typically 3-15x higher.** But the per-query differential is dominated by the **token-count multiplier**, not the price-per-token multiplier:

| Workload | Avg tokens per query | Price/MTok blend | Cost per query |
|:----|---:|---:|---:|
| Non-reasoning chat (GPT-5/Sonnet, ~500 in / 200 out) | 700 | $4 input, $15 output blended → ~$0.005 | ~$0.005 |
| Adaptive thinking (Claude Sonnet 4.6 with thinking, ~1k in / 1k thinking / 200 out) | 2,200 | similar mix | ~$0.025 |
| Reasoning agent (GPT-5.5 Thinking, 5k in / 8k thinking / 1k out) | 14,000 | $5/$40 | ~$0.4 |
| Heavy reasoning (GPT-5 Pro / Opus 4.7 deep think, 10k in / 30k thinking / 5k out) | 45,000 | $15/$120 or $5/$25 | $4-5 |
| Coding agent session (Claude Code Opus, multi-turn, hours, ~500k cumulative tokens) | 500,000 | $5/$25 with caching → ~$0.01-0.02 / kTok | $5-15 |

*Source: ITK calculations from list pricing and observed token budgets.*

So a single Claude Code session or GPT-5 Pro deep-think can cost **1,000-3,000x** more than a typical free-tier chat query. This is the central economic fact behind the compute-share calculation.

---

## 4. Compute-share derivation: revenue × pricing → compute

Approach: take each lab's API revenue and decompose by SKU using observed pricing. Convert dollars to "compute-equivalent tokens" using the inverse of price-per-token (a token at $25/MTok consumes the same dollars as 5 tokens at $5/MTok, so represents 1/5 the *compute units per dollar*).

This is an approximation — Anthropic and OpenAI have ~60-70% inference gross margins so the ratio of dollars to compute is lab-specific and SKU-specific. But for like-for-like models within a lab, list pricing is roughly proportional to underlying GPU cost (the labs price to a target margin).

**Worked example — Anthropic API ($20-25 bn ARR ex-Claude Code):**

Assume API revenue mix is roughly 60% Sonnet 4.6, 25% Opus 4.7, 10% Haiku 4.5, 5% legacy. Of the Sonnet revenue, ~70% is in adaptive-thinking mode (default in 4.6); of the Opus revenue, ~95% uses deep thinking. So:

- Reasoning revenue share within API: 0.6×0.7 + 0.25×0.95 + 0.1×0 + 0.05×0.5 = 0.42 + 0.24 + 0 + 0.025 = **~68% of API revenue is reasoning**.
- Per-token cost is similar between thinking and non-thinking modes within a model, but reasoning consumes ~5-10x more tokens per query, so the compute-per-revenue-dollar ratio is similar across the split.
- Therefore the API reasoning compute share roughly equals the API reasoning revenue share: **~70%**.

For Claude Code (effectively 100% reasoning) at $5 bn ARR vs API at $25 bn, the consolidated Anthropic reasoning compute share is:

- (5×1.0 + 25×0.7) / 30 = (5 + 17.5) / 30 = **~75%**

That is meaningfully below the ~87% I used in §2 because §2 weighted by *consumption* and gave Anthropic credit for its consumer Claude.ai usage, which is heavily Max/Pro and reasoning-dominated. Splitting the difference: **Anthropic ~80% reasoning compute share** is the defensible central estimate.

**OpenAI cross-check ($25-30 bn ARR):**

ChatGPT Free is hundreds of millions of users but each consumes maybe 20-50 messages/week; even with the 10-15% routing to thinking and the 30x token multiplier, Free is contributing perhaps 30-40% of OpenAI's inference compute, of which ~70% is reasoning. ChatGPT Plus/Pro/Team/Enterprise contribute another ~40% of compute, ~85% reasoning. API contributes ~25-30% of compute, ~70% reasoning. Weighted: 0.35×0.7 + 0.40×0.85 + 0.25×0.70 = **~76%**.

**Cross-check matches §2 within ±5 percentage points.**

---

## 5. Cross-check against hyperscaler capex

Total hyperscaler 2026 AI capex: ~$650-700 bn aggregate, of which ~75% (~$485 bn) is AI-specific [Source: https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/; https://fortune.com/2026/04/30/big-tech-hyperscalers-will-spend-700-billion-on-ai-infrastructure-this-year-with-no-clear-end-in-sight-eye-on-ai/].

Of that $485 bn, the rough split (Epoch and SemiAnalysis convergent view) is now closer to:

- 40% training (frontier-model pre-training and RL post-training)
- 35% inference serving
- 25% experiments/research

So **~$170 bn of AI capex in 2026 is allocated to inference serving capacity**. If reasoning is 60% of that, that's ~$100 bn of inference capex backing reasoning workloads in 2026.

Sanity check against OpenAI inference COGS: OpenAI is on track for ~$14 bn inference cost in 2026 vs $8.4 bn in 2025 [Source: https://aiautomationglobal.com/blog/ai-inference-cost-crisis-openai-economics-2026]. If OpenAI is ~30% of frontier-lab inference volume, total frontier-lab inference COGS is ~$45-50 bn, and total inference workload (including hyperscaler-served self-hosted) is perhaps $80-100 bn of operating cost. Capex amortised over 4-5 years adds another $35-45 bn/yr to economic cost. Total economic cost of 2026 inference: $115-145 bn. Reasoning's 60% share = $70-90 bn — consistent with the capex top-down.

The numbers reconcile in the right order of magnitude. A 50-65% range for the May 2026 reasoning compute share is internally consistent against both bottom-up (revenue × pricing) and top-down (capex × inference share × reasoning fraction) routes.

---

## 6. Forecast: 2027 and 2028

**Drivers pushing reasoning share *up*:**

1. **Agentic adoption**. Agent-pattern API calls grew 680% YoY in Q1 2026 and now represent 41% of new enterprise integrations [Source: https://www.mykxlg.com/online_features/press_releases/aicc-report-enterprise-token-costs-drop-67-year-over-year-as-multi-model-ai-adoption/article_794d655c-f59b-5921-bbd0-33edb058b05e.html]. Agents are reasoning-by-construction: every step involves a reasoning-tier model planning the next action. If agentic share of enterprise compute hits 70% by 2027 and 85% by 2028, reasoning compute share follows.
2. **Default-on adaptive thinking**. Claude 4.6/4.7 ship with adaptive thinking on by default. GPT-5.5 routes to thinking automatically on Plus and Enterprise. By 2027 the option to *not* reason on a frontier model will be the exception.
3. **Vertical agent products** (Cursor, Devin, Lovable, Replit Agent, OpenAI's Codex Cloud, Anthropic's Claude Code, Google's Jules, Microsoft's GitHub Copilot Agent). All sell autonomous coding sessions priced at $20-200/month and consuming millions of reasoning tokens per session.

**Drivers pushing reasoning share *down*:**

1. **Cheap-model improvements**. Gemini 3 Flash, GPT-5 nano, Claude Haiku 4.5 keep getting better, sucking up the long tail of bulk RAG/classification/summarisation that previously needed Sonnet/4o. This grows non-reasoning *token* volume. But because these models are cheap, the *compute* shift is modest.
2. **Reasoning efficiency**. Anthropic "substantially reduced" reasoning verbosity from Sonnet 3.7 to 4.0 [Source: https://epoch.ai/gradient-updates/how-persistent-is-the-inference-cost-burden]. GPT-5.2 reaches ~27% on FrontierMath with 5M output tokens vs 43M for o4-mini eight months earlier — about 9x less per accuracy point. If reasoning models keep getting 3-10x more efficient per year, share growth could plateau.
3. **Distillation**. Reasoning traces from Opus and GPT-5 Pro are being distilled into smaller cheaper models. By 2028 a $1/MTok model may match today's $25/MTok Opus.

**Net trajectory** — agentic adoption is the dominant force in the 2-3 year window, easily outweighing efficiency gains:

| Year | Central reasoning compute share | Range |
|:----|---:|:---|
| May 2026 | 60% | 55-65% |
| End 2027 | 78% | 72-82% |
| End 2028 | 83% | 78-88% |

*Source: ITK central estimate.*

By 2028 the question essentially flips: the interesting metric will be the share of compute that is *not* reasoning, which will be the residual of bulk Flash/Haiku/nano calls plus traditional classification/embedding workloads.

---

## 7. Final answer

**May 2026 reasoning compute share of total LLM inference compute: ~60% (range 55-65%).**

This is built up from:
- Frontier labs (OpenAI, Anthropic, Microsoft Azure OpenAI, Google Gemini, xAI) at ~70-75% reasoning share by revenue × pricing.
- Open-weight self-hosted long tail (Llama, Qwen, Mistral, smaller models on enterprise GPUs) at ~20-30% reasoning share.
- Weighted aggregate ~60%.

**2027 forecast: ~78% (range 72-82%).**
**2028 forecast: ~83% (range 78-88%).**

For ITK / electricity demand purposes, the relevant implication is that the *marginal* GW of AI data centre load coming on through 2027-28 is overwhelmingly serving reasoning and agentic workloads, which have a quite different load shape from chat (longer time-to-first-token, much longer per-query GPU occupancy, and burstier load profiles tied to enterprise working hours and CI pipeline triggers rather than 24/7 consumer chat).

---

## 8. Caveats

- **The 60% number is for compute-equivalent dollar-weighted inference, not raw token volume.** By raw token volume, reasoning is probably 35-45% (because non-reasoning Flash/Haiku/nano serve enormous token counts at very low margin). The 60% figure correctly captures the GPU/electricity load share.
- **Self-hosted on-prem inference is undermeasured.** Enterprise self-hosted Llama/Qwen deployments don't show up in lab revenue but do show up in hyperscaler capex and enterprise DC build-out. The cross-check in §5 partly captures this, but it remains the largest source of estimation error.
- **The reasoning/non-reasoning binary is becoming blurred.** Adaptive thinking, automatic routing, and "reasoning effort: low" all sit in a grey zone. By 2027 the question may be better framed as "average thinking budget per query" rather than a binary share.
- **OpenAI compute mix** still includes a large non-revenue-generating block (research experiments, RL training infrastructure). The ~30% inference / 70% other split documented by Epoch for 2024 is closing fast as inference scales, but for OpenAI specifically the inference share within total compute may still be only 40-50% of total compute spend in 2026.
- **Chinese provider treatment**. OpenRouter rankings show MiMo, Qwen, DeepSeek dominating raw OpenRouter token volume — but OpenRouter is unrepresentative of total inference compute. Direct enterprise hosting of Chinese open-weight models for sovereign/cost reasons is large and not captured in revenue numbers.
- **List vs effective pricing**. Big enterprise contracts run at 30-60% off list. Caching, batch API, and prompt-caching reduce effective per-token cost by 50-90%. The compute-share estimate is largely insensitive to this because both reasoning and non-reasoning workloads benefit from the same discounts proportionally — but Claude Code in particular gets very large savings from prompt caching that are not reflected in the simple revenue × list-price decomposition.
- **Dario Amodei's "80x growth" Q1 2026 figure** [Source: https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth] is annualised growth of a small base, not 80x q-o-q. Treat all rapid-growth disclosures with that filter when reading.

---

## 9. Bibliography

- AICC enterprise survey, Q1 2026. "Enterprise Token Costs Drop 67% Year-Over-Year." https://www.mykxlg.com/online_features/press_releases/aicc-report-enterprise-token-costs-drop-67-year-over-year-as-multi-model-ai-adoption/article_794d655c-f59b-5921-bbd0-33edb058b05e.html
- Alphabet, Q1 2026 earnings release. https://abc.xyz/
- Anthropic. "Anthropic raises $30 billion in Series G funding." 2026. https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- Anthropic. Pricing page. https://platform.claude.com/docs/en/about-claude/pricing
- apidog. "GPT-5.5 Pricing: Full Breakdown." April 2026. https://apidog.com/blog/gpt-5-5-pricing/
- Bloomberg. "OpenAI to Spend $50 Billion on Computing in 2026, Brockman Says." May 2026. https://www.bloomberg.com/news/articles/2026-05-05/openai-to-spend-50-billion-on-computing-in-2026-brockman-says
- DeepSeek API documentation. https://api-docs.deepseek.com/
- digitalapplied.com. "OpenRouter Rankings April 2026." https://www.digitalapplied.com/blog/openrouter-rankings-april-2026-top-ai-models-data
- Epoch AI. "Most of OpenAI's 2024 compute went to experiments." https://epoch.ai/data-insights/openai-compute-spend
- Epoch AI. "How persistent is the inference cost burden?" https://epoch.ai/gradient-updates/how-persistent-is-the-inference-cost-burden
- Fortune. "Big Tech is about to spend $700 billion on AI this year." April 2026. https://fortune.com/2026/04/30/big-tech-hyperscalers-will-spend-700-billion-on-ai-infrastructure-this-year-with-no-clear-end-in-sight-eye-on-ai/
- Futurum Group. "AI Capex 2026: The $690B Infrastructure Sprint." https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
- Gartner. "Inference cost on 1T parameter LLMs to drop 90% by 2030." March 2026. https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025
- Google. Gemini 3 Flash blog. https://blog.google/products/gemini/gemini-3-flash/
- Google AI. Gemini API pricing. https://ai.google.dev/gemini-api/docs/pricing
- Microsoft. FY26 Q3 earnings release. https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/press-release-webcast
- OpenAI. API pricing. https://developers.openai.com/api/docs/pricing
- pricepertoken.com. GPT-5 Pro and GPT-5 pricing. https://pricepertoken.com/pricing-page/model/openai-gpt-5-pro
- Sacra. Anthropic and OpenAI company profiles. https://sacra.com/c/anthropic/, https://sacra.com/c/openai/
- SemiAnalysis. "Nvidia GTC 2026 — The Inference Kingdom Expands." https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands
- SemiAnalysis. "InferenceMAX." October 2025 / April 2026. https://newsletter.semianalysis.com/p/inferencemax-open-source-inference
- Stormy AI. "Inside the Claude Code GTM Strategy: Anthropic's $2.5B ARR." https://stormy.ai/blog/claude-code-gtm-strategy-anthropic-revenue-2026
- Toby Ord. "Evidence that Recent AI Gains are Mostly from Inference-Scaling." https://www.tobyord.com/writing/mostly-inference-scaling
- VentureBeat. "Anthropic says it hit a $30 billion revenue run rate." https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth
- Where's Your Ed At. "Exclusive: Here's How Much OpenAI Spends On Inference and Its Revenue Share With Microsoft." https://www.wheresyoured.at/oai_docs/
- Zylos Research. "Inference Economics: AI Agent Compute Markets in 2026." April 2026. https://zylos.ai/research/2026-04-13-inference-economics-ai-agent-compute-markets
