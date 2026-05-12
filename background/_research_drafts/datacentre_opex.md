# Data Centre Operating Cost Structures: Traditional Cloud versus AI

*Research draft, May 2026 — input to a forthcoming piece on the economics of AI data centres.*

## Purpose and thesis

This note tests a working thesis:

> Traditional cloud computing data centres have cost structures where fixed costs and people costs are at least as important as energy costs. As we move into AI data centres (training or inference) and capacity utilisation rises, energy costs become increasingly dominant.

The thesis is largely supported by published data, but with three important qualifications:

1. The shift is driven by **utilisation** more than by anything intrinsically "AI" — the same physics applies to any workload that runs the IT load near nameplate.
2. **GPU depreciation** (capex amortisation) still dominates total cluster cost; on a *cash operating cost* basis, electricity becomes the largest line item once depreciation is excluded.
3. Australian energy share is structurally higher than US energy share at any given utilisation, because wholesale and retail power is more expensive.

Throughout, OpEx means **cash operating cost** (electricity, staff, maintenance, consumables, software, lease, insurance). CapEx amortisation is treated separately. TCO is OpEx + amortised CapEx.

---

## 1. Published OpEx breakdowns — traditional cloud and colocation

### 1.1 Categories of facility OpEx

For a wholesale colocation or hyperscaler-owned facility, published breakdowns identify roughly the same line items, even if the percentages differ:

- Energy / electricity (IT load + cooling + lighting + losses)
- People / staff (ops, maintenance, security, management)
- Maintenance and consumables (filters, parts, vendor contracts)
- Connectivity / network (peering, transit, dark fibre)
- Land / lease / property tax
- Insurance and regulatory compliance
- Software / DCIM / monitoring tools
- Water and sewerage (small but rising with evaporative cooling)

The Uptime Institute Global Data Center Survey 2025 — the most widely cited industry survey, n=879 in the 2024 edition and a comparable sample in 2025 — reports that cost is the single largest concern for operators, driven by *inflation, labour shortages and energy prices* in roughly that order of importance [Source: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2025]. Industry-weighted average PUE has been stuck near 1.54-1.56 for six consecutive years across the broader fleet [Source: https://uptimeinstitute.com/uptime_assets/7425ec68d479c5d78a743df94a79b114ed9f9c73f13b6460949d2b8e73373209-GA-2024-07-uptime-institute-global-data-center-survey-results-2024.pdf]. This matters because PUE is the multiplier between IT load and total facility energy bill.

### 1.2 OpEx composition — traditional facility

Published industry breakdowns (Thunder Said Energy, alpha-matica, network installer industry guides, MCIM benchmarks) converge on a similar picture for a *facility OpEx* lens — that is, what it costs the operator to run the building, before the tenant's IT spend:

**Table 1: Indicative OpEx mix for a traditional hyperscale or wholesale colocation facility (% of facility cash OpEx, ~50-60% utilisation)**

| Category | Low | Central | High |
|:----------------------------------|----:|--------:|-----:|
| Electricity (IT + cooling + losses) |  20% |     30% |  45% |
| Maintenance and consumables       |  25% |     35% |  45% |
| Staff and security                |  15% |     22% |  30% |
| Software, monitoring, IT tools    |   5% |     8%  |  12% |
| Property, insurance, compliance   |   3% |     5%  |  10% |

*Source: Thunder Said Energy "Data centres: the economics" [https://thundersaidenergy.com/downloads/data-centers-the-economics/]; alpha-matica deconstruction of data centre cost structure [https://www.alpha-matica.com/post/deconstructing-the-data-center-a-look-at-the-cost-structure-1]; The Network Installers data centre operating costs guide 2026 [https://thenetworkinstallers.com/blog/data-center-operating-costs/]; Uptime Institute Survey 2024/2025.*

Two published anchor points are worth quoting verbatim. Thunder Said Energy: "opex costs are dominated by maintenance (c40%), electricity (c15-25%), labour, water, G&A and other" [Source: https://thundersaidenergy.com/downloads/data-centers-the-economics/]. The Network Installers benchmark, in contrast, places energy at "40-60% of total operational costs" with labour at 20-25% and hardware/maintenance at 40-50% — but that is arithmetic over 100% because their "hardware" line includes amortised IT refresh, not a pure cash OpEx view [Source: https://thenetworkinstallers.com/blog/data-center-operating-costs/]. The reconciliation is the OpEx-vs-TCO confusion warned about earlier.

### 1.3 OpEx per MW per year

Industry benchmarks give a wide range:

- MCIM and network industry benchmarks: **US$800-2,000/kW/year** ($0.8M–$2.0M per MW/year) for facility OpEx at typical Tier III–IV operation [Source: https://mcim24x7.com/resources/successful-capex-opex-strategies/].
- A 100 MW hyperscale facility running at 50–70% utilisation in a US$0.07-0.10/kWh power market: **US$40–60M of annual electricity** plus US$10–25M of maintenance plus US$5–10M of staff [Source: https://www.alpha-matica.com/post/deconstructing-the-data-center-a-look-at-the-cost-structure-1].

The right way to read this: at typical 2024-25 utilisation and US wholesale prices, facility cash OpEx for a hyperscale data centre is in the order of **US$1.0–1.5M per MW per year**, of which electricity is the single largest line item but rarely above 40-45% in temperate-climate, well-managed facilities.

### 1.4 Critical distinction — facility OpEx versus compute OpEx

For a *colocation* deployment, the colocation provider runs the facility and the tenant runs the compute:

- **The colocation provider's OpEx** is the building, with electricity passed through "+E" (metered and recharged at cost) [Source: https://horizoniq.com/blog/colocation-pricing-guide/]. The provider's *gross* OpEx includes energy, but their *net* OpEx (after passthroughs) is dominated by maintenance, staff, and lease — energy almost disappears from the provider's economics because it is a pure passthrough.
- **The tenant's OpEx** is colocation rent (US$184–$215/kW/month wholesale in primary markets H2 2025, per CBRE) plus pass-through energy plus their own IT staff [Source: https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025; https://www.aitooldiscovery.com/ai-infra/colocation-data-center-explained]. For the tenant, pass-through energy *is* the variable line item that scales with utilisation, but rent is fixed.
- **For a self-built hyperscaler** (Microsoft, Meta, Google, AWS owning their own halls), all of these collapse into a single internal cost stack. NextDC's Australian disclosures explicitly separate "power passthrough revenue" from base recurring revenue for this reason [Source: https://nextdc.com/hubfs/ASX%20Announcements/Annual%20Report%20FY25.pdf].

A fair generalisation: in an owner-operator model, energy is 25-40% of facility cash OpEx at typical cloud utilisation. In a colocation tenant model, the *cash bill* the tenant writes looks much more energy-heavy at high utilisation because rent (the largest fixed component) is paid as kW reservation, not per kWh.

---

## 2. Published OpEx breakdowns — AI data centres

Published OpEx breakdowns for purpose-built AI data centres are sparser than for traditional cloud, but a handful of credible decompositions exist.

### 2.1 SemiAnalysis / Meta H100 cluster TCO

The most-cited public number is the SemiAnalysis decomposition of Meta's 24,576-GPU H100 cluster (later mirrored in PyTorch-to-Atoms write-up):

**Table 2: Meta 24k H100 cluster — 4-year TCO breakdown**

| Component                          | Share of TCO | Notes |
|:-----------------------------------|-------------:|:------|
| H100 GPUs                          |          ~46% | 65.8% of CapEx × 70.7% CapEx share |
| InfiniBand networking, CPU, storage |          ~24% | Remaining CapEx |
| Colocation (rent)                  |          ~20% | OpEx, fixed |
| Electricity                        |          ~9% | OpEx, variable with utilisation |
| Other OpEx                         |          ~1% | |
| **CapEx subtotal**                 |          **~71%** | |
| **OpEx subtotal**                  |          **~29%** | |

*Source: PyTorchToAtoms decomposition of SemiAnalysis Meta cluster TCO [https://pytorchtoatoms.substack.com/p/metas-24k-h100-cluster-capextco-and]. Cluster: 24,576 H100 SXM5 GPUs, 39-40 MW total facility load, 90% electricity utilisation rate assumed.*

Inside the OpEx-only (~$435M over four years) split, electricity is **~32%** of OpEx and colocation rent is the remaining ~68%. That is, of the *cash operating cost* of running an AI training cluster, roughly one-third is the electricity bill and two-thirds is colocation rent — a mostly-fixed pseudo-rent for space, cooling capability, redundant power feed, and security. Per-GPU TCO works out to **US$1.49/H100-hour** (excluding cost of capital), with **US$0.16/hour attributable to electricity** — about 11% of headline GPU-hour cost [Source: https://pytorchtoatoms.substack.com/p/metas-24k-h100-cluster-capextco-and].

The 90% utilisation assumption is critical and is consistent with published descriptions of what a training run actually looks like: a synchronous workload that pushes the GPUs near saturation continuously for weeks at a time.

### 2.2 SemiAnalysis AI Datacenter Energy Dilemma — facility energy intensity

For a cluster with 20,480 GPUs at 80% utilisation and PUE 1.25, SemiAnalysis estimates **~US$20.7M annual electricity cost** at a US average tariff of **$0.083/kWh** [Source: https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race]. Per-GPU power, including overheads, is ~1.39 kW — so the cluster runs at ~28 MW continuous. That implies an electricity cost of roughly **US$0.74M per MW per year** at US wholesale-ish prices.

For comparison, the same cluster in Singapore (US$0.23/kWh) would cost ~US$57M/year for the same energy — a 2.8x multiplier from location alone [Source: https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race].

### 2.3 Inference clusters

Inference economics have been mapped at ratio-form rather than absolute-form in most public sources. Two public decompositions stand out:

- **Martin Alderson's reverse-engineered H100 inference cost analysis**: at $2/H100/hour blended cost and a 72-H100 cluster running 9 model instances with batch-32 concurrency, the *raw compute* cost is "~$0.003 per million input tokens, ~$3.08 per million output tokens" with implied gross margins on API pricing of 80-95% [Source: https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/]. Alderson does not separately decompose electricity within that $2/H100-hour, but using SemiAnalysis-style assumptions (electricity at ~$0.16-0.25/H100-hour at US wholesale) implies electricity is ~8-12% of the inference cluster's *all-in* hourly cost, with the rest being depreciation and colocation.

- **Spheron / Introl inference cost guides**: place per-H100 cloud rental at $2.85-3.50/hour with operational overhead "approximately $2-7 per hour" added for cooling, facilities and maintenance [Source: https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide]. In the higher-overhead scenario (rare-earth power markets, complex liquid cooling), electricity-driven OpEx can lift the all-in to $5-10/H100-hour.

The crucial difference between inference and training is **utilisation**, not architecture. NVIDIA's own perspective piece on inference cluster economics quantifies the punishment: "a cluster running at 40% utilisation produces twice the effective cost per token compared to the same cluster at 80% utilisation, regardless of the hardware platform" [Source: https://perspectives.nvidia.com/utilization-rates-inference-cluster-economics-hardware/]. Real-world inference deployments run at much lower utilisation than training: published examples include a deployment with average GPU utilisation of 22% (idle 7pm-8am and weekends), and the GPT-4 training run on 25,000 A100s where average utilisation was reported at 32-36% [Source: https://www.spheron.network/blog/ai-inference-cost-economics-2026/].

### 2.4 Liquid cooling and PUE

AI training facilities are pushing PUE down hard via direct-to-chip and immersion cooling:

- Direct-to-chip liquid cooling (DLC): **PUE 1.10-1.20** versus 1.55-1.67 air [Source: https://www.kad8.com/server/data-center-liquid-cooling-for-ai-workloads-2026/].
- Immersion cooling: **PUE 1.03-1.08** at 64-rack scale [Source: https://www.kad8.com/server/data-center-liquid-cooling-for-ai-workloads-2026/].
- AirTrunk's Australian campuses report annual operating PUE targets of **1.23-1.28** with design PUE as low as 1.15 [Source: https://airtrunk.com/sustainability/clean-energy/].
- OpenAI's Stargate Abilene campus runs zero-water-evaporation closed-loop liquid cooling on every NVIDIA GB200 rack [Source: https://intuitionlabs.ai/articles/openai-stargate-datacenter-details].

Why this matters for the OpEx mix: at a given IT load, dropping PUE from 1.5 to 1.2 cuts the *cooling-attributable* electricity by about 60%, which trims the total electricity bill by ~20%. That is a non-trivial efficiency gain but does not change the qualitative thesis — at 90% utilisation, electricity is still the dominant variable cost.

### 2.5 People intensity

This is where AI facilities differ most starkly from traditional colocation:

**Table 3: Indicative staffing benchmarks (FTE per MW of operating capacity)**

| Facility type                               | FTE per MW |
|:--------------------------------------------|-----------:|
| Mid colocation (3-5 MW, multi-tenant)       |   ~6-12  |
| Large enterprise / Tier III-IV (20-40 MW)  |   ~1.0-1.5 |
| Hyperscale cloud campus (>100 MW)           |   ~0.4-1.0 |
| Highly automated hyperscale (>100 MW)       |   ~0.2-0.3 |
| AI training campus (Stargate-class, GW-scale) | <0.2 (estimated) |

*Source: Broadstaff Global data centre staffing benchmarks [https://broadstaffglobal.com/data-center-staffing-levels-how-many-people-does-a-facility-need]; The Fix data centre staffing 2026 guide [https://blog.thefix.it.com/how-many-employees-are-needed-to-run-a-data-center-2026-guide/]; Uptime Institute people challenge forecast 2021-2025 [https://intelligence.uptimeinstitute.com/resource/people-challenge-global-data-center-staffing-forecast-2021-2025]. AI campus row is an estimate based on published descriptions of single-tenant, single-workload facilities; we are not aware of a published AI-campus FTE/MW disclosure.*

A 100 MW AI training campus at 0.2 FTE/MW employs ~20 people; the same 100 MW spread across colocation halls supporting 50 enterprise customers might employ 200-400 people. The labour OpEx differential at typical AU/US fully-loaded wages of A$120-180k per FTE is the difference between ~A$3M/year and ~A$50M/year in staff cost — a meaningful contributor to why AI-dedicated facilities have a more energy-skewed OpEx mix.

---

## 3. The utilisation-energy share relationship: worked example

This is where the thesis lives or dies. Take a 100 MW IT-load data centre with PUE 1.3 (mid-range modern), in a US wholesale market paying **US$80/MWh** all-in retail (commercial tariff including transmission, capacity, demand charges).

Fixed and quasi-fixed annual OpEx, regardless of utilisation:

- Staff (60 FTE @ US$130k loaded): **US$7.8M**
- Maintenance contracts, consumables, parts: **US$15M** (US$150k/MW)
- Software, DCIM, security tools: **US$4M**
- Insurance, property tax, compliance: **US$3M**
- Connectivity (peering, transit minimum commits): **US$2M**
- **Fixed OpEx subtotal: ~US$32M/year**

(Land/lease excluded — assumed owner-operator. For a colo tenant, add ~US$220M/year at ~US$185/kW/month.)

Variable OpEx scales with utilisation: energy = utilisation × 100 MW × 8760 h × 1.3 PUE × $80/MWh.

**Table 4: 100 MW US owner-operated facility — OpEx by utilisation (PUE 1.3, US$80/MWh all-in)**

| Utilisation                        |    30% |    60% |    90% |
|:-----------------------------------|-------:|-------:|-------:|
| IT energy (MWh/yr)                 | 262,800 | 525,600 | 788,400 |
| Total facility energy (PUE 1.3)    | 341,640 | 683,280 | 1,024,920 |
| Annual energy cost (US$M)          |   $27.3 |   $54.7 |   $82.0 |
| Fixed OpEx (US$M)                  |   $32.0 |   $32.0 |   $32.0 |
| **Total facility OpEx (US$M)**     |   **$59.3** |   **$86.7** | **$114.0** |
| **Energy as % of OpEx**            |   **46%** |   **63%** |   **72%** |

*Source: author's calculation; benchmarks from Thunder Said Energy and alpha-matica for fixed-OpEx categories.*

The thesis holds quantitatively. At 30% utilisation (representative of typical underutilised cloud or sporadic inference), energy is ~46% of OpEx — meaningful but not dominant. At 90% utilisation (steady-state training), energy is ~72% — clearly dominant. The crossover from "fixed-cost-dominated" to "energy-dominated" happens around 30-40% utilisation in a US$80/MWh environment.

### 3.1 Same example at Australian prices

Repeat with Australian retail commercial pricing — say **A$140/MWh** all-in (this is reasonable for a NextDC- or AirTrunk-scale customer in NSW or QLD pulling firmed retail; spot wholesale averaged A$76/MWh in NSW and A$63/MWh in QLD in November 2025 [Source: https://leadingedgeenergy.com.au/news/electricity-market-review-latest/], but firmed retail with network charges roughly doubles that). Convert fixed OpEx to AUD at 1 USD = 1.55 AUD: ~A$50M/year fixed.

**Table 5: 100 MW Australian owner-operated facility — OpEx by utilisation (PUE 1.3, A$140/MWh all-in)**

| Utilisation                        |    30% |    60% |    90% |
|:-----------------------------------|-------:|-------:|-------:|
| Total facility energy (MWh/yr)     | 341,640 | 683,280 | 1,024,920 |
| Annual energy cost (A$M)           |   $47.8 |   $95.7 | $143.5 |
| Fixed OpEx (A$M)                   |   $50.0 |   $50.0 |   $50.0 |
| **Total facility OpEx (A$M)**      |   **$97.8** | **$145.7** | **$193.5** |
| **Energy as % of OpEx**            |   **49%** |   **66%** |   **74%** |

*Source: author's calculation; AEMO/AER NEM wholesale price data for FY25-26 underpinning A$140/MWh firm retail assumption.*

The Australian numbers are qualitatively similar to the US case at the higher utilisation end because energy share is driven by the *ratio* of energy cost to fixed cost, not the absolute level. But the **dollar OpEx is ~70% higher** in absolute terms — a much bigger absolute exposure to electricity price.

### 3.2 Sensitivity — moving PUE and electricity price

**Table 6: Energy as % of facility OpEx, 100 MW at 60% utilisation, sensitivity**

| US$/MWh ↓  / PUE → |   1.1 |   1.3 |   1.5 |
|:-------------------|------:|------:|------:|
| $50                | 45%   | 49%   | 53%   |
| $80                | 59%   | 63%   | 66%   |
| $120               | 69%   | 72%   | 74%   |

*Source: author's calculation, fixed OpEx at US$32M/year held constant.*

Two takeaways: PUE matters less than commonly assumed when energy is already dominant (~5pp impact across a wide PUE range). Electricity price matters a lot — moving from US$50/MWh (Quincy WA, hydro) to US$120/MWh (NYISO, ConEd commercial) shifts energy share by ~25pp at the same utilisation.

---

## 4. People intensity: traditional vs AI

The Uptime Institute survey finds that operators continue to report staffing pressures — North America and Europe report difficulty filling junior operator roles; women remain ~10% or less of operations staff in 80% of respondents [Source: https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf].

In dollar terms, staff is a meaningful but rarely dominant line:

- A 12 MW facility employing 20 FTE at fully-loaded US$120k = **US$2.4M/year**, ~5-8% of facility OpEx.
- A 40 MW facility employing 45 FTE at US$120k = **US$5.4M/year**, similar share.
- A 100 MW hyperscale at 0.4 FTE/MW (40 FTE) = **US$4.8M/year**, ~5% of OpEx at typical utilisation.
- A 100 MW AI training campus at 0.2 FTE/MW (20 FTE) = **US$2.4M/year**, ~2-3% of OpEx.

[Source: https://broadstaffglobal.com/data-center-staffing-levels-how-many-people-does-a-facility-need; https://blog.thefix.it.com/how-many-employees-are-needed-to-run-a-data-center-2026-guide/]

The *qualitative* importance of staff (talent shortages, certifications, 24/7 cover) is substantial; the *cost* importance is a single-digit share even in colocation. The thesis should be refined: it is not that "people costs are at least as important as energy costs" in absolute dollar terms — they typically aren't, even in traditional cloud. It is that **fixed costs collectively** (staff + maintenance + software + tax + insurance) are at least as important as energy in low-utilisation environments.

---

## 5. Australian comparison

### 5.1 NextDC FY25 — the only listed-co disclosure available

NextDC reported FY25 net revenue of **A$350.2M** (+14% YoY) and underlying EBITDA of **A$216.7M** (+6%), on billing utilisation of **110.9 MW** at year-end and contracted utilisation of **244.8 MW** (+42% pro-forma) [Source: https://www.proactiveinvestors.com/companies/news/1077497/nextdc-rallies-17-on-fy25-results-and-upbeat-ai-driven-outlook-1077497.html; https://nextdc.com/hubfs/ASX%20Announcements/Annual%20Report%20FY25.pdf]. Net revenue is *gross revenue less direct costs*, where "direct costs" are predominantly customer power passthrough and a small cost-of-sales tail.

NextDC's commentary on FY25 direct costs is informative: "Direct costs fell in FY25, reflecting the benefit of lower contracted energy prices compared with FY24." Facility cost growth was attributed to "higher facility staff costs from new data centre openings, expanded capacity and investments in physical security & systems, increased water and sewerage expenses aligned with customer consumption growth, higher maintenance costs due to significant increase in built and operating capacity to meet demand, and increased property costs reflecting land banks, new site acquisitions, and land revaluations" [Source: https://nextdc.com/hubfs/ASX%20Announcements/Annual%20Report%20FY25.pdf]. The list is a textbook traditional-colo OpEx mix: staff, security, water, maintenance, property — energy is conspicuously *not* in the list, because it's a passthrough.

A back-of-envelope: gross revenue ≈ A$350M net + A$200-300M power passthrough ≈ A$550-650M; with billing of ~111 MW that's ~A$5-6M revenue per operating MW — consistent with reported wholesale colocation rates pushing past A$220/kW/month in Sydney's core zones [Source: per Australian colo market commentary].

### 5.2 AirTrunk

AirTrunk operates >2.6 GW across six markets; Australian operating capacity (SYD1+SYD2+SYD3+MEL1+MEL2) will exceed **1.2 GW** when fully built [Source: https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/]. AirTrunk's FY24 sustainability report puts annual operating PUE on a downward path toward a **1.23-1.28 target** with design PUE of 1.15 — best-in-region [Source: https://airtrunk.com/sustainability/clean-energy/]. AirTrunk does not break out OpEx by category in its sustainability reports; financial statements are not public following the September 2024 sale to Blackstone.

### 5.3 The Australian energy share premium

The CBRE H2 2025 colocation pricing data shows Sydney core zone wholesale rates pushing past **US$150/kW/month** (~A$232/kW/month) — high but still below Silicon Valley ($230-270) and similar to Northern Virginia [Source: https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025; https://www.aitooldiscovery.com/ai-infra/colocation-data-center-explained]. So *colocation rent* is in the same ballpark globally.

What differs is the **electricity cost per MWh** that flows through to the tenant. With NSW/QLD firmed retail commercial supply running roughly A$120-160/MWh against US Tier-1 markets at US$60-100/MWh (~A$95-155/MWh), Australian energy share at any given utilisation is **~30-50% higher** than the US equivalent in absolute dollar terms — which is what makes the Australian operating economics of an AI cluster particularly sensitive to PPA pricing.

---

## 6. Implications for the economics of AI data centres

If the thesis is right — and the worked examples support it at 30/60/90% utilisation — there are a small number of consequential downstream implications for the planned economics piece:

1. **For training clusters at 80-95% utilisation, energy is the dominant cash operating cost.** A 100 MW training campus running 90% utilisation in a US$80/MWh market is spending ~US$80M/year on electricity against ~US$30M/year on everything else combined. At Australian prices this is ~A$140M against ~A$50M.

2. **PPA pricing matters more for AI than for cloud.** A 10% improvement in $/MWh contracted price improves training-cluster cash margin by ~7% directly. The same improvement for a 30%-utilised cloud facility moves margin by only ~3-4%. That is why hyperscalers are willing to pay massive premia (e.g. Microsoft's Three Mile Island deal, Stargate's onsite gas) to lock in firm, low-priced power.

3. **Inference utilisation variability is itself a cost-structure problem.** A frontier inference cluster oscillating between 20% utilisation overnight and 90% utilisation during peak hours faces the worst of both worlds — it pays for fixed cost continuously but only earns revenue when utilised. NVIDIA's own analysis shows the cost-per-token doubles at 40% utilisation versus 80% [Source: https://perspectives.nvidia.com/utilization-rates-inference-cluster-economics-hardware/]. This is the economic argument for batching, multi-tenant inference, and time-shifting workloads to track cheap power.

4. **Per-token sensitivity to electricity price.** Using the SemiAnalysis Meta-cluster numbers as anchor (US$0.16/H100-hour electricity), a Hopper-class GPU producing ~500-1000 output tokens/sec at saturation generates ~1.8-3.6M tokens/hour, putting electricity at roughly **US$0.04-0.09 per million output tokens** at US wholesale prices. Anthropic and OpenAI publicly charge US$3-25 per million output tokens [Source: https://www.finout.io/blog/openai-vs-anthropic-api-pricing-comparison]. Electricity is therefore on the order of **0.2-3% of revenue per token** at API list prices — but a much larger share of *cost*, which is why inference gross margin expansion correlates so tightly with model efficiency improvements (Blackwell's claimed ~35x lower cost per million tokens vs Hopper [Source: https://blogs.nvidia.com/blog/lowest-token-cost-ai-factories/]).

5. **GPU depreciation remains the elephant.** The Meta cluster TCO is **71% CapEx amortisation, 29% OpEx**, of which two-thirds of OpEx is rent. Electricity is "only" ~9% of TCO. So while energy is the dominant *operating* cost at high utilisation, it is still well behind GPU depreciation in any total-cost framing. The thesis is correctly framed as about *cash operating cost*, not total cost of operating.

---

## 7. Caveats

- **OpEx-versus-TCO confusion is endemic in industry sources.** Many "energy is X% of cost" claims silently lump in amortised IT refresh; most of those should be read as TCO statements, not OpEx statements.
- **Wholesale-versus-retail distinction matters.** A US$50/MWh wholesale price typically becomes US$70-100/MWh delivered after T&D, capacity, demand charges, and retailer margin. AU NEM prices behave similarly. We have used delivered/retail throughout the worked examples.
- **PUE is a deceptive simplification.** Real-world AI facilities can show PUE drift up under partial load (cooling systems lose efficiency below design point). The 1.10-1.20 numbers cited are *design* PUE; published *operating* PUE for the same facility class typically runs 1.20-1.35.
- **Tenant-versus-operator perspective produces different OpEx mixes.** The same physical kWh shows up as passthrough revenue for the colo provider, as cost-of-goods for the tenant, and as "energy" in industry survey aggregates — hence apparent contradictions across sources.
- **GPU depreciation is the elephant in the room for AI.** The thesis is about *cash operating cost*; total cost of operating an AI cluster is still dominated by GPU CapEx amortisation over a 4-6 year life. This note treats that as out-of-scope.
- **Australian disclosures are thin.** NextDC is the only ASX-listed pure-play; AirTrunk and CDC publish sustainability metrics but not OpEx breakdowns. The numbers in section 5 are necessarily inferred from rate cards, sustainability reports, and the comparable US data.

### What David would need to commission to fill the gaps

- A bottom-up OpEx model for an Australian 50-100 MW AI campus benchmarked against AirTrunk rate cards and AEMO retail tariff data (estimated ~3 weeks of analyst time).
- Direct discussion with a colo operator (NextDC, CDC, AirTrunk) under NDA on per-MW cost of power passthrough and net energy share for AI tenants — feasible if a research-relationship NDA can be set up.
- SemiAnalysis institutional subscription to access their AI Cloud TCO Model with explicit Australian electricity price scenarios (US$30k+/year list, but high-quality data for a one-off piece could be obtained via per-report purchase).

---

## 8. Bibliography

### Industry surveys and authoritative sources

- Uptime Institute, *Global Data Center Survey 2025*. https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2025
- Uptime Institute, *Global Data Center Survey 2024*. https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf
- Uptime Institute, *People Challenge: Global Data Center Staffing Forecast 2021-2025*. https://intelligence.uptimeinstitute.com/resource/people-challenge-global-data-center-staffing-forecast-2021-2025
- Lawrence Berkeley National Laboratory, *2024 United States Data Center Energy Usage Report* (Dec 2024). https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- US DOE press release on LBNL 2024 report. https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- IEA, *Energy and AI* (2025). https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- CBRE, *North America Data Center Trends H1 2025*. https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025
- CBRE, *North America Data Center Trends H2 2025*. https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025
- JLL, *2026 Global Data Center Outlook*. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- JLL, *North America Data Center Report Year-end 2025*. https://www.jll.com/en-us/insights/market-dynamics/north-america-data-centers
- Cushman & Wakefield, *US Data Center Development Cost Guide*. https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide

### AI cluster TCO and energy

- SemiAnalysis (via PyTorchToAtoms), *Meta's 24k H100 Cluster CapEx/TCO and BoM Analysis*. https://pytorchtoatoms.substack.com/p/metas-24k-h100-cluster-capextco-and
- SemiAnalysis, *AI Datacenter Energy Dilemma — Race for AI Datacenter Space*. https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race
- SemiAnalysis, *AI Cloud TCO Model*. https://newsletter.semianalysis.com/p/ai-cloud-tco-model
- SemiAnalysis, *How Much Do GPU Clusters Really Cost?* https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost
- SemiAnalysis, *H100 vs GB200 NVL72 Training Benchmarks — Power, TCO, and Reliability*. https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks
- Aschenbrenner, L., *Situational Awareness — Racing to the Trillion-Dollar Cluster*. https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/
- NVIDIA Perspectives, *How Utilization Drives AI Inference ROI*. https://perspectives.nvidia.com/utilization-rates-inference-cluster-economics-hardware/
- NVIDIA blog, *Rethinking AI TCO: Why Cost per Token Is the Only Metric That Matters*. https://blogs.nvidia.com/blog/lowest-token-cost-ai-factories/
- Alderson, M., *Are OpenAI and Anthropic Really Losing Money on Inference?* https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/
- Introl, *Inference Unit Economics: The True Cost Per Million Tokens*. https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide
- Introl, *Power Purchase Agreements (PPAs) for AI Data Centers*. https://introl.com/blog/power-purchase-agreements-ai-data-centers-renewable-energy-strategies
- Spheron, *AI Inference Cost Economics in 2026: GPU FinOps Playbook*. https://www.spheron.network/blog/ai-inference-cost-economics-2026/

### Industry cost decompositions

- Thunder Said Energy, *Data centres: the economics*. https://thundersaidenergy.com/downloads/data-centers-the-economics/
- alpha-matica, *Deconstructing the Data Center: A Look at the Cost Structure*. https://www.alpha-matica.com/post/deconstructing-the-data-center-a-look-at-the-cost-structure-1
- The Network Installers, *Data Center Operating Costs: Complete Guide (2026)*. https://thenetworkinstallers.com/blog/data-center-operating-costs/
- MCIM, *5 CapEx & OpEx Strategies For Data Center Cost Reduction*. https://mcim24x7.com/resources/successful-capex-opex-strategies/
- BroadStaff Global, *Data Center Staffing Levels: How Many People Does a Facility Need?* https://broadstaffglobal.com/data-center-staffing-levels-how-many-people-does-a-facility-need
- The Fix, *How Many Employees Are Needed to Run a Data Center? (2026 Guide)*. https://blog.thefix.it.com/how-many-employees-are-needed-to-run-a-data-center-2026-guide/
- AI Tool Discovery, *Colocation Data Center Costs: $196/kW and Rising in 2026*. https://www.aitooldiscovery.com/ai-infra/colocation-data-center-explained
- HorizonIQ, *Colocation Pricing Guide: Power, Space and Key Questions to Ask Your Provider*. https://www.horizoniq.com/blog/colocation-pricing-guide/

### Cooling, PUE, and infrastructure

- KAD8, *Data Center Liquid Cooling for AI Workloads (2026)*. https://www.kad8.com/server/data-center-liquid-cooling-for-ai-workloads-2026/
- IntuitionLabs, *OpenAI's Stargate Project: A Guide to the AI Infrastructure*. https://intuitionlabs.ai/articles/openai-stargate-datacenter-details

### Hyperscaler self-disclosure

- Microsoft, *2024 Environmental Sustainability Report*. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Microsoft-2024-Environmental-Sustainability-Report.pdf
- Microsoft, *2025 Environmental Sustainability Report*. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report.pdf
- DCD, *Meta data center electricity consumption hits 14,975 GWh*. https://www.datacenterdynamics.com/en/news/meta-data-center-electricity-consumption-hits-14975gwh-leased-data-center-use-nearly-doubles/

### Australian sources

- NextDC, *FY25 Annual Report and Appendix 4E* (Aug 2025). https://nextdc.com/hubfs/ASX%20Announcements/Annual%20Report%20FY25.pdf
- NextDC, *FY25 Full Year Results Presentation*. https://www.nextdc.com/hubfs/ASX%20Announcements/FY25%20Full%20Year%20Results%20Presentation.pdf
- ProactiveInvestors, *NextDC rallies 17% on FY25 results and upbeat AI-driven outlook*. https://www.proactiveinvestors.com/companies/news/1077497/nextdc-rallies-17-on-fy25-results-and-upbeat-ai-driven-outlook-1077497.html
- AirTrunk, *Clean Energy*. https://airtrunk.com/sustainability/clean-energy/
- AirTrunk, *FY24 Sustainability Report*. https://airtrunk.com/wp-content/uploads/2024/10/FY24-Sustainability-Report-by-AirTrunk.pdf
- AirTrunk, *Australian platform expansion announcements* (2025). https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/
- Leading Edge Energy, *November 2025 Electricity Market Rates Review* (NEM wholesale prices). https://leadingedgeenergy.com.au/news/electricity-market-review-latest/
- AEMO, *NEM Data Dashboard*. https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem/data-dashboard-nem

### Utilisation analysis

- powerpolicy.net, *The Puzzle of Low Data Center Utilization Rates*. https://www.powerpolicy.net/p/the-puzzle-of-low-data-center-utilization
- aixenergy.io, *Managing Data Center Uncertainty Part III — The Utilization Paradox*. https://www.aixenergy.io/managing-data-center-uncertainty-part-iii-the-utilization-paradox-scarcity-and-waste-inside-ai-infrastructure/
- arxiv:2509.07218, *Electricity Demand and Grid Impacts of AI Data Centers*. https://arxiv.org/html/2509.07218v2
