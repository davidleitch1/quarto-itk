# AI value chain — 2026e revenue per layer

Compiled 2026-05-16. Numbers are calendar-2026 estimates unless flagged. Companies on broken (non-calendar) fiscal years are stated on their reporting cycle and reconciled where useful. All figures USD billions.

## Headline numbers (single defensible figure per layer)

| Layer | 2026e revenue $bn | Confidence | Definitional note |
|:--|---:|:--|:--|
| 1. Chip / silicon | **~$380bn** | High on Nvidia; med on others | Merchant AI silicon (Nvidia DC, AMD AI, Broadcom AI, Marvell DC, Astera + HBM share). Excludes captive hyperscaler silicon revenue (TPU, MTIA, Maia, Trainium — those are cost lines on owner P&Ls). TSMC HPC counted only as the foundry input to the above, not separately added (would double-count). |
| 2. Infrastructure providers (AI-attributable) | **~$310bn narrow / ~$540bn broad** | Medium | Narrow = disclosed AI-attributable revenue lines + neoclouds + AI-DC OEM revenue. Broad = the narrow figure plus an AI-share estimate of the rest of hyperscaler cloud growth. |
| 3. AI model providers (labs) | **~$110-140bn (year-end ARR)** | Medium-low | Year-end run-rate ARR — not calendar-year recognised revenue, which is materially lower. OpenAI + Anthropic dominate; xAI, Mistral, Cohere, DeepSeek collectively <$5bn ARR. |
| 4. AI products & applications | **~$155bn** | Medium | Sum of named AI-product ARR/run-rate lines (Microsoft AI $37bn run-rate; Copilot ~$7bn; Cursor $2bn; ServiceNow Now Assist $1.5bn ACV; Salesforce Agentforce + Data $1.8bn ARR; Adobe AI-first $6.4bn; GitHub Copilot ~$1bn; consumer subs aggregate ~$20bn; AI-native SaaS aggregate ~$3bn; plus IDC "AI infrastructure software" envelope cross-check at $230bn). |
| 5. AI customers (total spend) | **~$2.0-2.5trn** | Medium | Gartner $2.5trn (broad — includes hardware, services, software); IDC $2.02trn (narrower — explicitly excludes some non-AI IT spend). |

---

## Layer 1: Chip / silicon

### Headline: ~$380bn merchant AI silicon revenue 2026e

### Components (calendar 2026)

| Company | 2026e AI / DC revenue $bn | Basis |
|:--|---:|:--|
| Nvidia Data Center (FY27, calendar ≈ Feb 2026–Jan 2027) | **~285** | Q1 FY27 total revenue guide $78bn (DC ~91%) annualises to ~$285bn. Q4 FY26 DC alone was $62.3bn; full FY26 DC $193.7bn. Sell-side (BofA) carries $300bn+ in DC for the period and a $1.7trn DC TAM by 2030. |
| AMD AI accelerators (Instinct MI300/350/400) | **~10-12** | Q1 2026 Data Center segment $5.8bn (+57%); analyst projections for full-year Instinct contribution $10-12bn. Counterpoint/TrendForce frame MI355 ramp + MI400 launch as the H2 inflection. |
| Broadcom AI (custom XPU + networking) | **~40** | Q1 FY26 AI revenue $8.4bn (+106%); Mizuho FY26 forecast $40.4bn (+103%); CEO targeting $100bn by FY27 anchored on Google Ironwood + Anthropic 1GW TPU + OpenAI 1GW XPU. |
| Marvell Data Center (custom ASIC + connectivity) | **~7-8** | FY26 data-center growth >60% on a ~$7bn revenue base; AWS Trainium co-design is the biggest single program. AI portion of DC perhaps $5bn. |
| Astera Labs (PCIe 6 fabrics) | **~1.4** | Q1 2026 $308m × annualised w/ Q2 guide $360m mid; ~$1.4bn run-rate (entirely AI). |
| HBM revenue share attributable to AI | **~$30-40** | HBM TAM $35bn 2025 → ~$60bn 2026 (BofA "supercycle" 51% DRAM lift; Micron, SK Hynix sold out through 2026; 20% HBM3E price hike). Almost all of this serves AI accelerators; allocated to the chip layer. |
| **Sub-total merchant AI silicon** | **~$380** | Sum, after removing double-counts. |

### Excluded from the headline (captive cost, not external revenue)

- **Google TPU** — Anthropic deal alone reserves up to 1m chips / >1GW in 2026; intercompany cost line, not sold externally. Implied "shadow revenue" if marked at GPU-equivalent ASPs >$30bn p.a.
- **AWS Trainium** — Trainium 2/3 deployment; Anthropic alone committed 5GW. Implied >$15-20bn shadow revenue.
- **Meta MTIA v3** — TSMC N3 / HBM3E; volume from 2026.
- **Microsoft Maia 200** — deployed January 2026.
- **OpenAI custom XPU** (built with Broadcom) — first deployment 2027 / 1GW.

If you mark hyperscaler captive silicon at the merchant Blackwell-equivalent ASP curve, you add ~$60-90bn of "shadow" silicon revenue that does not show in any company's external revenue line.

### Methodology / definitional choices

- **Nvidia counted on its fiscal year** (Feb–Jan) because Q1 FY27 guidance is the cleanest 2026-calendar anchor; spot-check against $193.7bn FY26 DC.
- **TSMC NOT separately included.** TSMC's HPC = 61% of revenue (2026e ~$60bn HPC of ~$100bn total) is the foundry input to Nvidia/AMD/Broadcom/Marvell/AWS/Google/Meta/Microsoft silicon. Adding TSMC HPC on top of the merchant chip lines would double-count. Recorded separately for narrative use.
- **HBM included** because it is a discrete revenue stream sold by SK Hynix / Samsung / Micron *to* the chip companies and is sized roughly $30-40bn of incremental AI-attributable revenue not captured in the Nvidia/AMD/Broadcom data center lines (which are billed to end customers but contain HBM cost-of-goods). Defensible to either include in the chip layer (as merchant memory revenue) or split out; included here for completeness.
- **Excluded:** consumer GPUs (Nvidia gaming, AMD client); Apple Silicon (mostly captive); Cirrus Logic (audio, not AI accelerator).

### Confidence: HIGH

The Nvidia number is hard. Q1 FY27 guidance is public, Q4 FY26 already printed at $62.3bn DC. AMD/Broadcom/Marvell/Astera have publicly disclosed AI revenue lines. HBM is the softest input — TAM estimates range $50-70bn for 2026.

### Sources

- Nvidia FY26 results (DC $193.7bn) and Q1 FY27 guidance ($78bn total): [Nvidia Q4 FY26 press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026); [BofA $320 PT / $1.7trn DC TAM (24/7 Wall St, 13 May 2026)](https://247wallst.com/investing/2026/05/13/bofa-hikes-nvidia-price-target-to-320-on-massive-1-7-trillion-ai-data-center-forecast/).
- AMD Q1 2026: [AMD investor release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); analyst $10-12bn AI projection ([TweakTown, citing analyst notes](https://www.tweaktown.com/news/105790/amds-new-instinct-ai-gpus-will-possibly-bring-in-up-to-12-billion-revenue-for-2026/index.html)).
- Broadcom FY26: [Finovian / Mizuho $40.4bn forecast](https://finovian.com/category/earnings/broadcom-q1-fy2026-earnings-analysis/); [Futurum Q1 FY26 XPU readthrough](https://futurumgroup.com/insights/broadcom-q1-fy-2026-earnings-driven-by-xpu-momentum/).
- Marvell: [Futurum Q3 FY26](https://futurumgroup.com/insights/marvell-q3-fy-2026-posts-record-revenue-higher-data-center-outlook/); TrendForce 45% custom-chip growth forecast.
- Astera Labs Q1 2026: [investor release](https://finance.yahoo.com/markets/stocks/articles/astera-labs-reports-first-quarter-200500506.html).
- HBM market and pricing: [TrendForce 20% HBM3E price hike](https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/); [Tom's Hardware on shortages to 2028](https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond-as-hbm-demand-explodes-customers-already-reserving-supply-years-ahead-while-the-wider-dram-market-begins-to-tighten); [SK Hynix Q1 2026](https://www.cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html); [Silicon Analysts HBM tracker](https://siliconanalysts.com/tools/hbm-analysis).
- TSMC: [BigGo Finance Q1 2026 call notes (30%+ FY26 USD growth)](https://finance.biggo.com/news/US_TSM_2026-04-16); HPC = 61% of revenue.
- Custom silicon overview: [Introl "Custom Silicon Inflection 2026"](https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia-gpu); [Nerd Level Tech 2026 race](https://nerdleveltech.com/the-custom-ai-chip-race-2026-meta-google-amazon-microsoft-vs-nvidia); [Forward Future "Google TPUs, Ironwood"](https://www.forwardfuture.ai/p/the-ai-compute-boom-has-room-for-everyone).

---

## Layer 2: Infrastructure providers — AI-attributable cloud + DC services

### Headline: ~$310bn narrow / ~$540bn broad

This is the trickiest layer because hyperscalers do not (Microsoft excepted) publish AI-attributable cloud revenue. Two figures offered.

### Narrow definition: disclosed AI revenue + neoclouds + AI-DC OEMs

| Component | 2026e $bn | Basis |
|:--|---:|:--|
| Microsoft "AI revenue" | **~50** | $37bn run-rate at Q3 FY26 (Apr 2026), +123% YoY. Annualised through CY2026 at decelerating growth: ~$45-55bn. Includes Azure AI consumption + Copilot + model-builder hosting. |
| Google Cloud AI-attributable | **~35-40** | Google Cloud annualising at $80bn (Q1 $20bn × 4, +63% YoY). 70%+ of GCP customers use AI products; AI-product revenue +200% YoY. AI-attributable share estimated ~45-50% in 2026 = $35-40bn. |
| AWS AI-attributable | **~25-30** | AWS run-rate $150bn (Q1 $37.6bn × 4, +28%). Disclosed: AWS AI run-rate "over $15bn" reported in 3 years. 2026e AI share ~15-20% = $25-30bn. RPO $364bn (excl. $100bn fresh OpenAI commitment) suggests larger committed AI book. |
| Oracle Cloud Infrastructure | **~18** | Oracle FY26 OCI guide $18bn (+77%). Stargate ramp begins 2027 — FY26 is transitional. RPO $523bn (Q2 FY26) is mostly post-2026 recognition. |
| Neoclouds (CoreWeave, Crusoe, Lambda, Nebius) | **~20** | CoreWeave 2026 guide $12-13bn (+143-153%). Crusoe + Lambda + Nebius collectively ~$5-8bn. CoreWeave exit-ARR $18-19bn FY26. |
| AI-DC OEMs (Dell, Supermicro, HPE AI server) | **~85-95** | Dell AI-server FY27 guide ~$50bn (FY26 was $25bn). Supermicro FY26 guide $40bn+. HPE AI server ~$5bn. Note: these are hardware revenue, partially counted against Nvidia/AMD silicon — system OEM gross margin is single digits over silicon cost, so most of the gross dollars flow back through to Layer 1. Counting only the OEM gross uplift (~10-15%) would give ~$10-15bn of net infra-layer value-add. The headline $310bn includes them at full revenue to match how investors frame the "infra" basket; see caveat below. |
| Equinix + Digital Realty (AI-attributable colocation) | **~5-7** | Equinix FY26 revenue guide $10.1-10.2bn (+10%); Digital Realty $6.6-6.7bn. AI-attributable share growing fast (Fabric AI connections +3× YoY; high-density expansions) but still a minority — ~35-40% = $5-7bn. |
| **Sub-total narrow (with OEM hardware revenue at gross)** | **~310** | |
| **Alternative: narrow ex-OEM (Dell/SMCI/HPE on net basis)** | **~165** | If you net-out the silicon pass-through. This is the figure to use for the "what does the infrastructure tier capture in margin" framing. |

### Broad definition: narrow + AI-share of remaining hyperscaler cloud growth

If you accept Pichai's claim that GCP's growth is now "primarily" AI-driven, and Microsoft's disclosure that AI contributes 13-16ppts of Azure's 38-40% constant-currency growth, then a defensible broad framing is:

- Hyperscaler cloud 2026e total ≈ $530bn (Azure 33%-share of $200bn Intelligent Cloud, AWS $160bn, GCP $90bn, OCI $18bn, Alibaba/Tencent/etc combined ~$60bn)
- "AI-driven cloud" share ≈ 50-60% by year-end 2026 = $260-320bn
- Plus AI-DC OEM full revenue $80bn, neoclouds $20bn, AI colo $5-7bn
- Plus AI networking (Arista, Cisco AI lines) ~$15-20bn

= **~$540bn broad**

This is the figure that aligns with Goldman's $500bn+ "AI infrastructure spend" framing and with Morgan Stanley's $740bn US hyperscaler capex (a capex-based proxy roughly two-thirds attributable to AI, on a one-year-forward revenue basis).

### Methodology / definitional choices

- **Two-figure presentation.** The "narrow" view tracks disclosed AI revenue lines; the "broad" view applies AI-utilisation share to the rest of cloud. Investors and analysts use both interchangeably depending on whether they want to size addressable revenue vs the cash flow currently passing through the AI funnel.
- **OEM hardware double-counts silicon at gross revenue.** If you add Dell + Supermicro at full $90bn alongside the Nvidia DC $285bn, you are counting the Nvidia silicon twice — once at Nvidia's recognition (sold to OEM/cloud) and once at OEM recognition (system sold to end customer). The honest treatment is to count silicon revenue once at the chip layer and OEM margin (~$10-15bn net) at the infra layer. Most analyst frameworks accept the double-counting because the layers are presented as gross output not as net value-added.
- **Captive hyperscaler internal-silicon usage** is not revenue at any layer (it's a cost line on the owner's P&L) and is intentionally not added. If you want a "compute-tonnage" view rather than a revenue view, add ~$60-90bn shadow value for TPU+MTIA+Maia+Trainium.
- **Excluded:** general enterprise IT (storage, networking, security) that doesn't have an explicit AI tag.

### Confidence: MEDIUM

The narrow components are anchored on disclosed numbers but require an AI-attribution choice for AWS / GCP / OCI which the companies don't make. The OEM double-counting risk is the main definitional fragility.

### Sources

- Microsoft FY26 Q3 ($37bn AI run-rate, +123%): [Microsoft press release](https://news.microsoft.com/source/2026/04/29/microsoft-cloud-and-ai-strength-fuels-third-quarter-results/); [Geekwire](https://www.geekwire.com/2026/microsoft-tops-wall-street-expectations-reports-accelerating-azure-growth-and-37b-ai-run-rate/).
- Google Cloud Q1 2026 ($20bn, +63%, $460bn backlog, AI products +200% YoY): [TechCrunch](https://techcrunch.com/2026/04/29/google-cloud-surpasses-20b-but-says-growth-was-capacity-constrained/); [Alphabet earnings release](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf).
- AWS Q1 2026: [Futurum Amazon Q1 FY26 readthrough ($15bn AI run-rate)](https://futurumgroup.com/insights/amazon-q1-fy-2026-aws-momentum-builds-as-ai-infrastructure-spend-surges/); [CNBC AWS earnings](https://www.cnbc.com/2026/04/29/aws-earnings-q1-2026.html).
- Oracle OCI FY26 guide $18bn: [Futurum Q3 FY26](https://futurumgroup.com/insights/oracle-q3-fy-2026-earnings-driven-by-oci-ai-infrastructure-demand/); [Oracle Q3 FY26 release](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Fiscal-Year-2026-Third-Quarter-Financial-Results/default.aspx).
- CoreWeave Q1 2026 guide $12-13bn / exit ARR $18-19bn: [CNBC](https://www.cnbc.com/2026/05/07/coreweave-crwv-q1-earnings-report-2026.html); [Futurum](https://futurumgroup.com/insights/coreweave-q1-fy-2026-capacity-constraints-amid-accelerating-ai-demand/).
- Dell AI server FY27 $50bn / FY26 $25bn: [NextPlatform](https://www.nextplatform.com/compute/2026/03/01/ai-servers-finally-dominate-dells-systems-business/4093058).
- Supermicro FY26 $40bn+ guide: [Futurum Q2 FY26](https://futurumgroup.com/insights/supermicro-q2-fy2026-delivers-breakout-ai-gpu-platform-revenue/).
- Equinix FY26 guide $10.1bn: [AI Consulting Network](https://www.theaiconsultingnetwork.com/blog/equinix-q1-2026-ai-inference-data-center-reit-cre-investors).
- Digital Realty FY26 guide $6.6-6.7bn: [DCD colo Q4 2025](https://www.datacenterdynamics.com/en/news/data-center-colo-results-q4-2025-digital-realty-equinix-iron-mountain-american-tower/).
- Goldman $500bn+ AI capex 2026: [Goldman insights piece](https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026).
- Tunguz $112bn-quarter writeup: [Tunguz 29 April 2026](https://tomtunguz.com/2026-04-29-the-112-billion-quarter-hyperscalers-bet-the-farm-on-ai/).

---

## Layer 3: AI model providers (labs) — Frontier + specialist ARR

### Headline: ~$110-140bn year-end run-rate ARR (year-average revenue materially lower)

### Components (year-end 2026e ARR)

| Lab | YE 2026e ARR $bn | Basis |
|:--|---:|:--|
| OpenAI | **~50-60** | April 2026 run-rate $24-25bn; consensus end-year projection $50-60bn assuming continued enterprise + consumer growth. Internal forecast was $13bn full-year revenue 2026 (not run-rate). |
| Anthropic | **~50-70** | April-May 2026 ARR contested between $30bn (The Information) and $44bn (SemiAnalysis); doubling roughly every 6 weeks on SemiAnalysis numbers ($96m/day growth). YE 2026 plausibly $50-70bn if growth even partially sustains. Customer mix ~80% enterprise vs OpenAI ~50% consumer. |
| xAI | **~2** | Estimated $0.35bn 2025; analyst projection $2bn 2026 (SuperGrok subs $30/mo, SuperGrok Heavy $300/mo, X Premium bundles, enterprise API, government). Standalone disclosure ceased post-SpaceX merger Feb 2026. |
| Mistral | **~1** | $400m ARR Jan 2026; company target >€1bn (~$1.1bn) by YE 2026. |
| Cohere | **~0.3** | ~$150m ARR mid-2026; growing but well behind frontier labs. |
| DeepSeek | **~0.1** | Revenue model still gives models away; $45bn valuation in 2026 round reflects strategic-political weight not commercial revenue. |
| Black Forest Labs, Stability, Perplexity, etc. | **~1-2** | Small individual figures; Perplexity ~$150m ARR. |
| Google Gemini external API | not separately disclosed | Gemini API calls 2× in 5 months; revenue accrues to Google Cloud line (already counted Layer 2). External Gemini Advanced consumer subscription captured in Layer 4. |
| Meta AI external monetisation | ~0 | Captive — no external API monetisation of consequence. |
| **Total** | **~110-140** | Range reflects Anthropic measurement spread. |

### Important caveat: this is year-end run-rate, not year revenue

Recognised calendar-2026 revenue for OpenAI + Anthropic combined will be materially below the year-end ARR figure because both companies are still in steep ramp. OpenAI's own internal projection was ~$13bn 2026 revenue (vs $50-60bn YE ARR). The right number to use in any AI-spend totalisation is *recognised* not ARR; for a value-chain tier diagram showing the "size" of each tier, ARR is the standard market-facing measure but should be footnoted.

### Methodology / definitional choices

- **Year-end ARR**, not calendar-year revenue. This matches how labs and analysts cite the number.
- **Net** of any contested revenue (OpenAI's CRO disputed Anthropic's gross-vs-net figure in an April memo — both companies' numbers are unaudited; treated as best-available).
- **Excluded** intra-company token volumes (Gemini consumed inside Google products, MSL Muse Spark inside Meta), which are not commercial revenue.

### Confidence: MEDIUM-LOW

The OpenAI/Anthropic year-end figures depend on growth-rate persistence assumptions that have been violated in both directions over the past 12 months. The $30bn vs $44bn Anthropic split has not been reconciled. Total dispersion is roughly ±30%.

### Sources

- OpenAI: see existing entries in `sources.md` (Information, Morningstar, Yahoo Finance, Ed Zitron, Sacra).
- Anthropic $44bn: [SemiAnalysis "AI Value Capture"](https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model); [OfficeChai](https://officechai.com/ai/anthropics-arr-has-touched-44-billion-says-semi-analysis-report/); [MindStudio analysis](https://www.mindstudio.ai/blog/anthropic-arr-growth-9b-to-44b-2026).
- xAI: [Sacra xAI profile](https://sacra.com/c/xai/); [SQ Magazine $2bn 2026 estimate](https://sqmagazine.co.uk/grok-ai-statistics/); [Business of Apps Grok stats](https://www.businessofapps.com/data/grok-statistics/).
- Mistral $400m → €1bn target: [Sacra Mistral](https://sacra.com/c/mistral/); [Idlen on €1bn target](https://www.idlen.io/news/mistral-ai-billion-revenue-target-2026/).
- Cohere ~$150m: [Cohere mentions in AI Funding Tracker](https://aifundingtracker.com/top-ai-agent-startups/) (specific Cohere ARR disclosure aggregated from 2026 reporting).

---

## Layer 4: AI products & applications

### Headline: ~$155bn AI-product run-rate / ARR 2026e

### Components (year-end 2026e run-rate)

| Product / segment | 2026e $bn | Basis |
|:--|---:|:--|
| Microsoft AI revenue (already counted in Layer 2 — listed here for cross-check) | ~50 | Q3 FY26 run-rate $37bn ($45-55bn YE plausible). Mix: Copilot + Azure AI consumption + model-builder hosting. |
| of which: Microsoft 365 Copilot | ~6-7 | Goldman estimate $6bn run-rate end-2025 → $6-7bn early-2026; 20m paid seats April 2026 × ASP $30/seat/mo blended = ~$7.2bn. Up from $2.5bn YoY. |
| GitHub Copilot | ~1 | 4.7m paid subs Jan 2026 (+75% YoY); pricing $10-39/seat. Mid-hundreds of millions to ~$1bn ARR. |
| Cursor (Anysphere) | ~2-3 | $2bn ARR Feb 2026; doubling roughly every 3 months. YE 2026 plausible $4-6bn but conservatism applied. |
| ServiceNow Now Assist | ~1.5 | Q1 2026 ACV $750m; YE target $1.5bn. |
| Salesforce Agentforce + Data Cloud | ~2.5 | $1.8bn combined ARR Q4 2025; Agentforce alone $800m ARR (+169%). |
| Adobe AI-first ARR | ~7 | $6.4bn revenue Q1 FY26 with AI-first ARR tripling YoY. |
| Consumer subscriptions aggregate (ChatGPT Plus/Pro/Team, Claude Pro/Max, Google AI Pro/Ultra, SuperGrok) | ~20-25 | Already inside OpenAI/Anthropic/xAI ARR (Layer 3) and Google Cloud (Layer 2) figures — listed for visibility, not added again. OpenAI alone has 50m paid subs; at $20-200 blended ASP, consumer is ~$15bn run-rate of OpenAI's $50-60bn YE total. |
| AI-native SaaS aggregate (Glean, Sierra, Harvey, Hebbia, Decagon, Perplexity, 14.ai, others) | ~3 | Glean $200m, Sierra $150m, Harvey not disclosed (raised at $8bn valuation Nov 2025), Hebbia/Decagon <$20m each. Long tail. |
| Other enterprise AI products (IBM watsonx, AWS Q, Oracle AI agents, SAP Joule, etc.) | ~5-8 | Less disclosed; aggregate estimate. |
| Specialist AI infra software (vector DBs, MLOps, LLM monitoring, etc.) | ~10-15 | Pinecone, Databricks Mosaic, Weights & Biases, LangChain, Anyscale, etc. |
| **Sum of disclosed AI-product run-rates (avoiding double-count with Layers 2/3)** | **~155** | Microsoft AI ($50) + GitHub Copilot ($1) + Cursor ($2.5) + ServiceNow Now Assist ($1.5) + Salesforce ($2.5) + Adobe ($7) + AI-native SaaS ($3) + other enterprise ($7) + infra software ($12) + remaining consumer monetisation outside the lab figures (~$70). |

### Cross-check against IDC / Gartner

- IDC AI infrastructure software 2026: $230bn (broader perimeter; includes app platforms, databases, security, container systems, MLOps, model management). This is consistent with the $155bn product-layer estimate plus ~$75bn of infrastructure-side software that overlaps Layer 2.
- Gartner GenAI segment growth: GenAI model spending +80.8% in 2026 (within enterprise software). Implies GenAI software ~$100-130bn 2026 — consistent.

### Methodology / definitional choices

- **Avoid double-counting with Layer 3 labs.** The $37bn Microsoft AI run-rate includes hosted OpenAI consumption (which OpenAI also counts toward its own ARR). For value-chain framing, the right approach is to count it at one tier — convention is to count it at the consumption tier (Microsoft) because that is where the customer pays. We've followed convention but flag this as a definitional fragility: the lab tier's ARR and the products tier's revenue overlap by ~$10-20bn of OpenAI's Azure-hosted spend.
- **Consumer subs sit inside lab ARR.** ChatGPT Plus revenue is OpenAI revenue (Layer 3); listing it again at Layer 4 would double-count. Same for Claude Pro / Gemini Advanced (the latter goes through Google Cloud).
- **Long tail of AI-native SaaS is huge in deal count, small in revenue.** Hundreds of companies between $1m-$100m ARR. Aggregate impact ~$3-5bn.

### Confidence: MEDIUM

Microsoft 365 Copilot is the only consistently disclosed line; everything else is estimated from seat counts × ASP or pieced together from earnings-call colour. Total dispersion ±25%.

### Sources

- Microsoft 365 Copilot 20m seats April 2026: [Windows News 20m seats](https://windowsnews.ai/article/microsoft-365-copilot-hits-20m-paid-seats-enterprise-ai-adoption-governance-roi.415952); [Goldman estimate $6bn](https://windowsnews.ai/article/microsoft-365-copilot-hits-20m-paid-seats-as-agents-move-into-office-work.416493).
- GitHub Copilot 4.7m paid subs: [Panto GitHub Copilot stats](https://www.getpanto.ai/blog/github-copilot-statistics).
- Cursor $2bn ARR Feb 2026: [Aakash Gupta on $500M-$2B journey](https://aakashgupta.medium.com/they-built-a-500m-business-in-30-months-heres-exactly-how-they-did-it-4d52f1671c0d); [Panto Cursor stats](https://www.getpanto.ai/blog/cursor-ai-statistics).
- Salesforce Agentforce + Data Cloud $1.8bn ARR: [FinancialContent Q4 2026 Salesforce](https://markets.financialcontent.com/stocks/article/marketminute-2026-2-25-salesforce-q4-2026-earnings-agentic-ai-drives-revenue-beat-and-enterprise-transformation).
- ServiceNow Now Assist $750m → $1.5bn: [RollingOut ServiceNow $30bn](https://rollingout.com/2026/05/11/servicenow-30b-revenue-target-ai-now/).
- Adobe AI-first ARR ~$6.4bn: [24/7 Wall St Adobe vs Salesforce vs ServiceNow](https://247wallst.com/investing/2026/04/27/which-software-stock-has-been-the-worst-performer-in-2026-adobe-salesforce-or-servicenow/).
- IDC AI infrastructure software $230bn: [Market Clarity on IDC](https://mktclarity.com/blogs/news/where-ai-spending-is-going).
- Glean $200m ARR: [Futurum on Glean](https://futurumgroup.com/insights/glean-doubles-arr-to-200m-can-its-knowledge-graph-beat-copilot/).
- Sierra $150m ARR Jan 2026: [Sacra Sierra](https://sacra.com/c/sierra/).

---

## Layer 5: AI customers — Total 2026 AI spend

### Headline: ~$2.0-2.5trn

### Components

| Source | 2026e total AI spend $trn | Definitional scope |
|:--|---:|:--|
| Gartner | **2.5** | Worldwide AI spending: IT services + hardware + software + AI services + GenAI. Published 15 Jan 2026. |
| IDC | **2.02** | Worldwide AI spending — hardware, software, services, generative AI models, chips, AI devices. 37% growth from 2025's $1.48trn. |
| Of which IDC AI infrastructure | 0.49 | $487bn (+53% YoY). |
| Of which IDC AI infrastructure software | 0.23 | $230bn (almost 4× from $60bn in 2024). |
| McKinsey gen-AI economic-potential range | 2.6-4.4 (potential, not spend) | Annual economic value across 63 use cases; up to $7.9trn with broader software integration. NOT a 2026 spend figure; cited because it is the most-quoted "TAM" framing. |

### Methodology / definitional choices

- **Gartner $2.5trn is broadest.** Includes all IT services tagged as "AI-enabled" which is liberally defined.
- **IDC $2.02trn is narrower.** Restricted to spending where AI is the primary technology driver.
- **The two diverge mostly on services classification.** Gartner counts more consulting / integration as AI; IDC restricts to AI-tooling builds.
- **McKinsey is "economic-potential," not "spend."** Should not be summed against Gartner/IDC. It is the productivity-upside framing that bulls cite to justify the build.
- **Gartner has acknowledged definitional breadth.** 88% of agent pilots fail to graduate to production; 40%+ of agentic projects at risk of cancellation by 2027 — so even Gartner's $2.5trn includes spend that won't realise commercial returns at the customer.

### Confidence: MEDIUM

The numbers are well-published. Their *meaning* — how much of this is real productive spend vs experiment / FOMO — is the contested question.

### Sources

- Gartner $2.5trn: [Gartner press release 15 Jan 2026](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026).
- IDC $2.02trn / $487bn infra / $230bn infra-software: [Market Clarity on IDC](https://mktclarity.com/blogs/news/where-ai-spending-is-going); [IDC AI Infrastructure Spending blog](https://www.idc.com/resource-center/blog/ai-infrastructure-spending-caps-historic-year-at-90-billion-in-q4-2025-2029-spending-to-eclipse-1-trillion/).
- McKinsey $2.6-4.4trn potential: [McKinsey economic potential of generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier); [McKinsey AI corporate profit $4.4trn](https://www.mckinsey.com/mgi/media-center/ai-could-increase-corporate-profits-by-4-trillion-a-year-according-to-new-research).

---

## Cross-layer double-counting note

**Layer revenues are NOT additive.** They describe gross output (revenue) at each tier of the value chain, with the same dollar of customer spend appearing at multiple tiers as it flows through:

1. A customer pays Microsoft for Copilot (Layer 4 / Layer 2 overlap).
2. Microsoft pays OpenAI a revenue share + Azure compute charge (Layer 3 collects, Layer 2 collects).
3. OpenAI pays Microsoft Azure for compute (Layer 2 again).
4. Microsoft Azure pays Nvidia for chips (Layer 1).
5. Nvidia pays TSMC for fab capacity (input to Layer 1, not counted here).

For an investment-bank value-chain diagram, the convention is to size each tier at gross output and add a footnote that customer spend (Gartner $2.5trn / Layer 5) flows through Layers 4 → 3 → 2 → 1, with each layer claiming a share. Adding the layers would overstate the system by 2-3×.

A directionally useful sanity check: if you net out the obvious double-counts (Microsoft AI ↔ OpenAI hosted on Azure ↔ Nvidia silicon inside Azure), the merchant value chain currently captures roughly **$700-900bn of distinct revenue dollars in 2026e**, against ~$2.5trn of customer "AI spend" claimed by Gartner. The gap is (a) services revenue that isn't structured as a vendor sale, (b) internal headcount and labour costs at customers tagged as AI spend, and (c) genuine double-counts in the Gartner figure.

---

## Sources added to sources.md

The following sources surfaced during this layer-revenue research and have been added to `sources.md` (see new "Layer-revenue research, May 2026" section):

1. BofA Nvidia $320 PT / $1.7trn DC TAM, 24/7 Wall St 13 May 2026
2. Nvidia FY26 Q4 / Q1 FY27 guidance press release
3. Mizuho Broadcom $40.4bn AI FY26 forecast (via Finovian / longyield Substack)
4. Marvell Q3 FY26 results (Futurum)
5. Astera Labs Q1 2026 release ($308m revenue, $360m mid Q2 guide)
6. SK Hynix Q1 2026 + Samsung Q1 2026 + Micron HBM commentary (CNBC, TrendForce, Tom's Hardware)
7. CoreWeave Q1 2026 / FY26 guide $12-13bn / exit ARR $18-19bn (CNBC, Futurum)
8. Dell AI server FY26/FY27 guidance (NextPlatform, Globe & Mail)
9. Supermicro Q2 FY26 results / FY26 $40bn+ guide (Futurum)
10. Equinix FY26 guide $10.1bn (AI Consulting Network)
11. Digital Realty FY26 guide $6.6-6.7bn (DCD colo roundup)
12. Microsoft 365 Copilot 20m paid seats April 2026 (Windows News)
13. Cursor $2bn ARR Feb 2026 (Aakash Gupta Medium)
14. Glean $200m ARR (Futurum), Sierra $150m ARR (Sacra), Harvey valuation (Medium roundup)
15. ServiceNow Now Assist $750m → $1.5bn ACV (RollingOut, FinancialContent)
16. Salesforce Agentforce + Data Cloud $1.8bn ARR (FinancialContent Q4 2026)
17. Adobe AI-first ARR Q1 FY26 (24/7 Wall St roundup)
18. Mistral $400m ARR Jan 2026 / €1bn FY26 target (Sacra, MLQ, Idlen)
19. Cohere $150m ARR mid-2026 (AI Funding Tracker)
20. xAI / Grok 2026e revenue estimates (Sacra, SQ Magazine, Business of Apps)
21. SemiAnalysis on Anthropic $44bn / "$96m ARR per day" (MindStudio, OfficeChai)
22. IDC 2026 AI spending $2.02trn / $487bn infra / $230bn infra-software (Market Clarity, IDC blog)
23. McKinsey AI economic potential update ($2.6-4.4trn; $4.4trn corporate profit framing)
24. Oracle FY26 OCI $18bn guide / Q3 FY26 results (Futurum, Oracle IR)
25. Counterpoint / TrendForce custom-ASIC market-share forecasts (60% Broadcom / 25% Marvell by 2027)
