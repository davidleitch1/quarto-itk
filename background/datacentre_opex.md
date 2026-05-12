---
title: "Data centre operating cost structures: traditional cloud versus AI"
author: "David Leitch"
date: 2026-05-11
format: html
draft: false
category: "datacentres"
lightbox: true
---

# Data centre operating cost structures: traditional cloud versus AI

## Purpose and thesis

This note tests a working thesis:

> Traditional cloud computing data centres have cost structures where fixed costs and people costs are at least as important as energy costs. As we move into AI data centres (training or inference) and capacity utilisation rises, energy costs become increasingly dominant.

The thesis is supported by published data, with three important qualifications:

1. The shift is driven by **utilisation** more than by anything intrinsically "AI" — the same physics applies to any workload that runs the IT load near nameplate.
2. **GPU depreciation** (capex amortisation) still dominates total cluster cost; on a *cash operating cost* basis, electricity becomes the largest line item once depreciation is excluded.
3. Australian energy share is structurally higher than US energy share at any given utilisation, because wholesale and retail power is more expensive.

Throughout, OpEx means **cash operating cost** (electricity, staff, maintenance, consumables, software, lease, insurance). CapEx amortisation is treated separately. TCO is OpEx plus amortised CapEx. The underlying research draft is kept under `background/_research_drafts/datacentre_opex.md` for traceability.

---

## 1. Traditional cloud and colocation OpEx

### Categories of facility OpEx

For a wholesale colocation or hyperscaler-owned facility, published breakdowns identify the same line items, even if the percentages differ:

- Energy (IT load + cooling + lighting + losses)
- People (operations, maintenance, security, management)
- Maintenance and consumables (filters, parts, vendor contracts)
- Connectivity (peering, transit, dark fibre)
- Land / lease / property tax
- Insurance and regulatory compliance
- Software / DCIM / monitoring tools
- Water and sewerage (small but rising with evaporative cooling)

The Uptime Institute Global Data Center Survey 2025 — the most widely cited industry survey, n=879 in the 2024 edition and a comparable sample in 2025 — reports that cost is the single largest concern for operators, driven by inflation, labour shortages and energy prices in roughly that order [@uptime-survey-2025]. Industry-weighted average PUE has been stuck near 1.54-1.56 for six consecutive years across the broader fleet [@uptime-survey-2024]. PUE matters because it is the multiplier between IT load and total facility energy bill.

### Indicative OpEx mix at typical cloud utilisation

Published industry breakdowns (Thunder Said Energy, alpha-matica, network-installer industry guides, MCIM benchmarks) converge on a consistent picture for *facility cash OpEx* — what it costs the operator to run the building, before the tenant's IT spend.

**Table 1: Indicative OpEx mix for a traditional hyperscale or wholesale colocation facility (% of facility cash OpEx, ~50-60% utilisation)**

| Category | Low | Central | High |
|:----------------------------------|----:|--------:|-----:|
| Electricity (IT + cooling + losses) |  20% |     30% |  45% |
| Maintenance and consumables       |  25% |     35% |  45% |
| Staff and security                |  15% |     22% |  30% |
| Software, monitoring, IT tools    |   5% |     8%  |  12% |
| Property, insurance, compliance   |   3% |     5%  |  10% |

*Source: Thunder Said Energy "Data centres: the economics" [@tse-economics]; alpha-matica deconstruction of data centre cost structure [@alpha-matica]; The Network Installers data centre operating costs guide 2026 [@tni-opcosts]; Uptime Institute Survey 2024/2025.*

### OpEx per MW per year

Industry benchmarks give a wide range:

- MCIM and network industry benchmarks: **US\$800-2,000/kW/year** (\$0.8-2.0M per MW/year) for facility OpEx at typical Tier III-IV operation [@mcim-strategies].
- A 100 MW hyperscale facility running at 50-70% utilisation in a US\$0.07-0.10/kWh power market: **US\$40-60M of annual electricity** plus US\$10-25M of maintenance plus US\$5-10M of staff [@alpha-matica].

The right way to read this: at typical 2024-25 utilisation and US wholesale prices, facility cash OpEx for a hyperscale data centre is in the order of **US\$1.0-1.5M per MW per year**, of which electricity is the single largest line item but rarely above 40-45% in temperate-climate, well-managed facilities.

### Facility OpEx versus compute OpEx

For a colocation deployment, the colocation provider runs the facility and the tenant runs the compute:

- **The colocation provider's OpEx** is the building, with electricity passed through "+E" (metered and recharged at cost) [@horizoniq-colo]. The provider's *gross* OpEx includes energy, but their *net* OpEx (after passthroughs) is dominated by maintenance, staff, and lease.
- **The tenant's OpEx** is colocation rent (US\$184-215/kW/month wholesale in primary markets H2 2025 per CBRE) plus pass-through energy plus their own IT staff [@cbre-h1-2025; @aitool-colo]. For the tenant, pass-through energy *is* the variable line item that scales with utilisation, but rent is fixed.
- **For a self-built hyperscaler** (Microsoft, Meta, Google, AWS owning their own halls), all of these collapse into a single internal cost stack. NextDC's Australian disclosures explicitly separate "power passthrough revenue" from base recurring revenue for this reason [@nextdc-fy25-ar].

A fair generalisation: in an owner-operator model, energy is 25-40% of facility cash OpEx at typical cloud utilisation. In a colocation tenant model, the *cash bill* the tenant writes looks much more energy-heavy at high utilisation because rent (the largest fixed component) is paid as kW reservation, not per kWh.

---

## 2. AI data centre OpEx — what's published

### SemiAnalysis / Meta H100 cluster TCO

The most-cited public number is the SemiAnalysis decomposition of Meta's 24,576-GPU H100 cluster (mirrored in PyTorch-to-Atoms write-up):

**Table 2: Meta 24k H100 cluster — 4-year TCO breakdown**

| Component                          | Share of TCO | Notes |
|:-----------------------------------|-------------:|:------|
| H100 GPUs                          |          ~46% | 65.8% of CapEx × 70.7% CapEx share |
| InfiniBand networking, CPU, storage |          ~24% | Remaining CapEx |
| Colocation (rent)                  |          ~20% | OpEx, fixed |
| Electricity                        |           ~9% | OpEx, variable with utilisation |
| Other OpEx                         |           ~1% | |
| **CapEx subtotal**                 |       **~71%** | |
| **OpEx subtotal**                  |       **~29%** | |

*Source: PyTorchToAtoms decomposition of SemiAnalysis Meta cluster TCO [@pytorch-meta]. Cluster: 24,576 H100 SXM5 GPUs, 39-40 MW total facility load, 90% utilisation.*

Inside the OpEx-only subtotal (~US\$435M over four years), electricity is **~32%** of OpEx and colocation rent is the remaining ~68%. That is, of the *cash operating cost* of running an AI training cluster, roughly one-third is the electricity bill and two-thirds is colocation rent — a mostly-fixed pseudo-rent for space, cooling capability, redundant power feed, and security. Per-GPU TCO works out to **US\$1.49/H100-hour** (excluding cost of capital), with **US\$0.16/hour attributable to electricity** — about 11% of headline GPU-hour cost [@pytorch-meta].

The 90% utilisation assumption is critical and consistent with published descriptions of training: a synchronous workload that pushes the GPUs near saturation continuously for weeks at a time.

### SemiAnalysis Datacenter Energy Dilemma

For a cluster with 20,480 GPUs at 80% utilisation and PUE 1.25, SemiAnalysis estimates **~US\$20.7M annual electricity cost** at a US average tariff of \$0.083/kWh [@semi-energy-dilemma]. Per-GPU power, including overheads, is ~1.39 kW — so the cluster runs at ~28 MW continuous. That implies an electricity cost of roughly **US\$0.74M per MW per year** at US wholesale-ish prices.

For comparison, the same cluster in Singapore (US\$0.23/kWh) would cost ~US\$57M/year for the same energy — a 2.8× multiplier from location alone [@semi-energy-dilemma].

### Inference clusters

Inference economics have been mapped at ratio-form rather than absolute-form in most public sources:

- **Martin Alderson's reverse-engineered H100 inference cost analysis**: at \$2/H100/hour blended cost and a 72-H100 cluster running 9 model instances with batch-32 concurrency, the *raw compute* cost is "~\$0.003 per million input tokens, ~\$3.08 per million output tokens" with implied gross margins on API pricing of 80-95% [@alderson-inference]. Using SemiAnalysis-style assumptions (electricity at ~US\$0.16-0.25/H100-hour at US wholesale), electricity is ~8-12% of the inference cluster's all-in hourly cost, with the rest being depreciation and colocation.
- **Spheron / Introl inference cost guides**: place per-H100 cloud rental at \$2.85-3.50/hour with operational overhead "approximately \$2-7 per hour" added for cooling, facilities and maintenance [@introl-inference]. In the higher-overhead scenario (rare-earth power markets, complex liquid cooling), electricity-driven OpEx can lift the all-in to \$5-10/H100-hour.

The crucial difference between inference and training is **utilisation**, not architecture. NVIDIA's own perspective piece on inference cluster economics quantifies the punishment: "a cluster running at 40% utilisation produces twice the effective cost per token compared to the same cluster at 80% utilisation, regardless of the hardware platform" [@nvidia-utilisation]. Real-world inference deployments run at much lower utilisation than training: published examples include a deployment with average GPU utilisation of 22% (idle 7pm-8am and weekends), and the GPT-4 training run on 25,000 A100s where average utilisation was reported at 32-36% [@spheron-inference].

### Liquid cooling and PUE

AI training facilities are pushing PUE down hard via direct-to-chip and immersion cooling:

- Direct-to-chip liquid cooling (DLC): PUE 1.10-1.20 versus 1.55-1.67 air [@kad8-liquid].
- Immersion cooling: PUE 1.03-1.08 at 64-rack scale [@kad8-liquid].
- AirTrunk's Australian campuses report annual operating PUE targets of 1.23-1.28 with design PUE as low as 1.15 [@airtrunk-clean].
- OpenAI's Stargate Abilene campus runs zero-water-evaporation closed-loop liquid cooling on every NVIDIA GB200 rack [@intuition-stargate].

Why this matters for the OpEx mix: at a given IT load, dropping PUE from 1.5 to 1.2 cuts the cooling-attributable electricity by about 60%, which trims the total electricity bill by ~20%. That is a non-trivial efficiency gain but does not change the qualitative thesis — at 90% utilisation, electricity is still the dominant variable cost.

### People intensity

This is where AI facilities differ most starkly from traditional colocation:

**Table 3: Indicative staffing benchmarks (FTE per MW of operating capacity)**

| Facility type                               | FTE per MW |
|:--------------------------------------------|-----------:|
| Mid colocation (3-5 MW, multi-tenant)       |   ~6-12  |
| Large enterprise / Tier III-IV (20-40 MW)  |   ~1.0-1.5 |
| Hyperscale cloud campus (>100 MW)           |   ~0.4-1.0 |
| Highly automated hyperscale (>100 MW)       |   ~0.2-0.3 |
| AI training campus (Stargate-class, GW-scale) | <0.2 (estimated) |

*Source: Broadstaff Global data centre staffing benchmarks [@broadstaff]; The Fix data centre staffing 2026 guide [@thefix]; Uptime Institute people challenge forecast 2021-2025 [@uptime-people]. AI campus row is an estimate based on published descriptions of single-tenant, single-workload facilities; no published AI-campus FTE/MW disclosure has been located.*

A 100 MW AI training campus at 0.2 FTE/MW employs ~20 people; the same 100 MW spread across colocation halls supporting 50 enterprise customers might employ 200-400 people. The labour OpEx differential at typical AU/US fully-loaded wages of A\$120-180k per FTE is the difference between ~A\$3M/year and ~A\$50M/year in staff cost — a meaningful contributor to why AI-dedicated facilities have a more energy-skewed OpEx mix.

---

## 3. The utilisation-energy share relationship: multi-region worked example

This is where the thesis lives or dies. Take a 100 MW IT-load data centre with PUE 1.3 (mid-range modern). The fixed OpEx structure is similar across geographies, but the *electricity price* varies hugely — and that variation is what determines whether a given location is competitive for AI build-out.

### Fixed OpEx structure

Fixed and quasi-fixed annual OpEx scales with site, not consumption. For a US owner-operator:

- Staff (60 FTE @ US\$130k loaded): **US\$7.8M**
- Maintenance contracts, consumables, parts: **US\$15M** (US\$150k/MW)
- Software, DCIM, security tools: **US\$4M**
- Insurance, property tax, compliance: **US\$3M**
- Connectivity (peering, transit minimum commits): **US\$2M**
- **US fixed OpEx subtotal: ~US\$32M/year**

For an Australian owner-operator at properly-decomposed input prices (NOT a flat FX conversion):

- Staff (60 FTE @ A\$155k loaded — Australian wages, not US wages × FX): **A\$9.3M**
- Maintenance contracts (~60% USD-denominated parts × FX + ~40% AU labour): **A\$20.0M**
- Software / DCIM (USD SaaS × FX): **A\$6.2M**
- Insurance, property tax, compliance (AU-denominated): **A\$5.0M**
- Connectivity (AU-denominated): **A\$3.0M**
- **AU fixed OpEx subtotal: ~A\$43.5M/year**

Australian fixed OpEx is meaningfully *lower* in USD-equivalent terms than US fixed OpEx (A\$43.5M ÷ 1.55 = US\$28M vs US\$32M) because Australian labour is cheaper than US labour at FX-equivalent rates. A flat 1.55× FX conversion would have given A\$50M, over-counting by ~13%.

### Per-region delivered electricity prices for AI data centres, May 2026

The "right" electricity price for the worked example depends on which market the data centre sits in. The five most relevant scenarios:

**Table 4: All-in delivered electricity prices for a hyperscale data centre, May 2026**

| Market / scenario | Wholesale energy | Capacity | Network / T&D | Other | All-in delivered |
|:------------------|----:|----:|----:|----:|----:|
| **Quincy WA** (Microsoft, Grand Coulee hydro via Grant PUD) | US\$25-35 | n/a | US\$5-10 | US\$5 | **US\$45/MWh** |
| **ERCOT West Texas** (Stargate Abilene, energy-only market) | US\$40-55 | n/a | US\$10-20 | US\$5 | **US\$65/MWh** |
| **PJM general** (AEP Ohio, ComEd, PPL) | US\$45-55 | US\$13.70 (RTO 2026/27 cap) | US\$15-25 | US\$5 | **US\$85/MWh** |
| **PJM Dominion** (Northern Virginia data centre cluster) | US\$50-65 | US\$22.50 (Dominion 2025/26 BRA) | US\$15-25 | US\$5 | **US\$105/MWh** |
| **CAISO Silicon Valley** | US\$50-70 | US\$15-25 (RA charges) | US\$15-30 | US\$5 | **US\$110/MWh** |
| **NEM NSW wholesale-flat + network** (transmission-connected, no firming) | A\$76 (US\$49) | n/a | A\$15-25 (US\$10-16) | A\$5-10 | **US\$65/MWh** |
| **NEM NSW firmed retail** (24/7 supply guarantee from large retailer) | bundled | n/a | bundled | bundled | **A\$140/MWh = US\$90/MWh** |
| **NEM NSW PPA + facility BESS** (sophisticated AI campus) | A\$65-85 PPA strike | n/a | A\$15-25 | net of FCAS revenue | **A\$95/MWh = US\$61/MWh** |

*Source: ITK compilation. PJM from PJM IMM and Monitoring Analytics 2025/26 BRA reports; NEM from AEMO and Leading Edge Energy reviews [@leadingedge-nem]; ERCOT and CAISO from EIA data; AU PPA pricing from ACT auctions, NEXTDC and AirTrunk PPA disclosures. Capacity equivalents calculated as $/MW-day × 365 ÷ (8,760 × 0.9 utilisation).*

Two observations from this table that matter for the worked example:

- **PJM Dominion is now the most expensive US market** for delivered electricity to a data centre, after the 2024 capacity auction explosion. The Dominion-zone capacity charge alone adds ~US\$22.50/MWh on top of energy.
- **NEM NSW with PPA + BESS firming** is competitive with the cheapest US locations and **materially cheaper than PJM Dominion**. The Australian "firmed retail" route is more expensive than PPA + BESS by ~A\$45/MWh — a meaningful penalty for paying a retailer to take the firming risk.

### Five-scenario worked example at 90% utilisation

With the same 100 MW IT-load facility at 90% utilisation, PUE 1.3, the OpEx and per-IT-MWh costs work out as:

**Table 5: 100 MW data centre OpEx by location, 90% utilisation, PUE 1.3**

| Scenario | Energy ($/MWh) | Annual energy cost | Fixed OpEx | Total OpEx | OpEx per IT-MWh |
|:---------|----:|----:|----:|----:|----:|
| Quincy WA hydro | US$45 | US$46M | US$32M | US$78M | US$99 |
| NSW NEM, PPA + BESS | A$95 | A$97M | A$43.5M | A$140.5M | A$178 = **US$115** |
| ERCOT West Texas | US$65 | US$67M | US$32M | US$99M | US$126 |
| NSW NEM, firmed retail | A$140 | A$143M | A$43.5M | A$187M | A$237 = **US$153** |
| PJM Dominion (NoVa) | US$105 | US$108M | US$32M | US$140M | **US$178** |

*Source: ITK calculation. Fixed OpEx properly priced (not flat FX). Energy cost = utilisation × 100 MW × 8,760 h × 1.3 PUE × $/MWh. OpEx per IT-MWh = total OpEx ÷ 788,400 MWh of IT energy. FX 1 USD = 1.55 AUD.*

**The cheapest US site (Quincy WA hydro) is the cheapest overall.** Among the rest, the ranking is:

1. NSW PPA + BESS at US\$115/MWh-IT
2. ERCOT West Texas at US\$126/MWh-IT
3. NSW firmed retail at US\$153/MWh-IT
4. PJM Dominion at US\$178/MWh-IT

A sophisticated Australian AI campus using a PPA + facility BESS structure is **cheaper than ERCOT West Texas** (where Stargate is being built) and **35% cheaper than PJM Dominion** (where most US construction is concentrated). The Australian "lazy" approach — a long-term firmed retail contract — is the worst Australian option but still cheaper than PJM Dominion.

**Energy share of OpEx by scenario:**

| Scenario | Energy as % of OpEx |
|:---------|--------------------:|
| Quincy WA hydro | 59% |
| ERCOT West Texas | 67% |
| NSW PPA + BESS | 69% |
| NSW firmed retail | 76% |
| PJM Dominion | 77% |

The thesis still holds — energy is dominant at 90% utilisation in every case — but the *level* of dominance varies from 59% (cheapest power) to 77% (most expensive power). The ranking of competitiveness inverts the ranking of energy share: cheap-power sites have lower energy share *because their fixed costs are a larger fraction of a smaller total*.

### Sensitivity: PUE × electricity price

**Table 6: Energy as % of facility OpEx at 60% utilisation, 100 MW**

| US$/MWh ↓  / PUE → |   1.1 |   1.3 |   1.5 |
|:-------------------|------:|------:|------:|
| $45                | 41%   | 46%   | 51%   |
| $65                | 53%   | 57%   | 61%   |
| $85                | 60%   | 64%   | 68%   |
| $105               | 65%   | 69%   | 72%   |

*Source: ITK calculation; fixed OpEx held at US$32M/year.*

Two takeaways: PUE matters less than commonly assumed when energy is already dominant (~5pp impact across a wide PUE range). Electricity price matters much more — moving from Quincy WA hydro (US\$45) to PJM Dominion (US\$105) shifts energy share by ~25pp at the same utilisation.

### Water — small dollar line, big constraint

Water belongs in the OpEx mix even though it rarely moves the dollar totals. Three lenses matter:

**Direct water cost is small.** A typical evaporative-cooled hyperscale uses 0.5-3 L per kWh of IT load. For a 100 MW facility at 80% utilisation, that's roughly 1 GL/year, billed at industrial rates of US\$1-5 per kilolitre — about **US\$1-2M/year, or 1-2% of facility OpEx**. A closed-loop liquid-cooled AI facility (the Stargate Abilene model) uses near-zero direct water; the line falls to US\$100-300k/year, essentially a rounding error.

**Indirect cost via cooling architecture is bigger.** Water and energy substitute for each other through the choice of cooling design:

| Cooling architecture | Water (L/kWh) | PUE | Energy bill penalty |
|:--|:--|:--|:--|
| Evaporative (legacy hyperscale) | 1-3 | 1.10-1.20 | None — best PUE |
| Closed-loop chillers | ~0.05 | 1.30-1.45 | +20-25% on energy |
| Direct-to-chip liquid (closed) | near zero | 1.10-1.20 | None — capex premium |
| Air-cooled | 0 | 1.50-1.70 | +35-50% on energy |
| Dry coolers (radiator-style) | 0 | 1.40-1.55 | +25-35% on energy |

For the 100 MW worked example at US\$85/MWh, going from PUE 1.2 to PUE 1.5 costs **~US\$20M/year in extra energy** — roughly 10× the direct water cost. So in any market where you can get the water permit, evaporative cooling is the economic answer.

**Permitting cost is the binary one.** This is where water actually matters. Tucson Project Blue (originally AWS-anchored) was rejected 7-0 in August 2025 over a 2,000 ac-ft/yr water draw; Amazon withdrew. Chandler AZ rejected a US\$2.5bn project 7-0 in December 2025 over 100 million gallons/year proposed. Phoenix, Mesa and Avondale all now cap industrial water and require developers to source supplemental supplies above the cap. In water-stressed jurisdictions, water is a build/no-build constraint, not a P&L line — and the engineering response has been to default to closed-loop liquid cooling specifically to dodge the water permitting question. Microsoft's 2024 commitment to "next-generation zero-water-cooling" and Stargate Abilene's zero-water GB200 racks are the leading examples [@kad8-liquid; @intuition-stargate].

**Australian context.** NSW/VIC/QLD coastal sites are not water-stressed in the way Phoenix or Tucson are. The Western Sydney data centre cluster (Mamre Road, Marsden Park, Eastern Creek) faces local water-supply scrutiny but has not seen AWS-Tucson-style rejections. AirTrunk reports water-positive targets in its sustainability disclosures; NextDC's FY25 commentary lists "increased water and sewerage expenses" as one of several cost-growth drivers but doesn't quantify the share [@nextdc-fy25-ar; @airtrunk-clean]. The political risk in Australia is more around renewable PPA underwriting than water — the "must power itself" coalition framing pulls the political conversation toward energy.

**Where water belongs in the model.** A flat ~US\$1-2M/year line in the facility OpEx mix; a binary site-disqualification overlay in arid US locations (Phoenix, Tucson, Chandler); a trigger for closed-loop cooling design with its own PUE and capex consequences. Water never dominates the dollar economics, but it can stop the project.

### Scale economies on fixed costs

The 100 MW worked example understates the energy share at hyperscale because **fixed costs do not scale linearly** with capacity. At 500 MW vs 100 MW (same operator, same model, same utilisation):

| Cost line | 100 MW | 500 MW | Scaling factor |
|:--|--:|--:|--:|
| Staff (with shared functions / supervisory layers) | $7.8M | ~$23M | 3.0× |
| Maintenance & consumables | $15M | ~$62M | 4.1× |
| Software / DCIM (site licences) | $4M | ~$9M | 2.3× |
| Insurance, property tax, compliance | $3M | ~$11M | 3.7× |
| Connectivity (peering + transit) | $2M | ~$6M | 3.0× |
| **Fixed OpEx subtotal** | **$31.8M** | **~$111M** | **~3.5×** |

*Source: ITK estimate; staff scaling reflects supervisory layers and shared functions (Broadstaff Global benchmarks); maintenance scales near-linearly per unit serviced; software has site-licence economies.*

Fixed cost per MW falls from US\$318k/MW at 100 MW to ~US\$222k/MW at 500 MW — **a ~30% saving in unit fixed cost from going hyperscale**. Re-running the worked example at 500 MW, US\$85/MWh, 90% utilisation, PUE 1.3:

- Energy: 500 × 8,760 × 0.9 × 1.3 × 85 = **US\$435M/year**
- Fixed: **~US\$111M/year**
- Total OpEx: **US\$546M/year**
- **Energy share: 80%** (vs 73% at 100 MW)

So at the largest GW-scale campuses (Stargate Abilene 1.2 GW, Hyperion 5 GW, Mt Pleasant Fairwater 3.3 GW) **energy share is closer to 80-85% of cash OpEx** because of these fixed-cost economies. Marginal MWh is what dominates the operating economics, and competitiveness on PPA pricing matters even more at hyperscale.

### Memo: depreciation context

Depreciation is not OpEx, but the relative size matters. For a 100 MW H100-class AI cluster:

| Component | CapEx (US\$bn) | Useful life | Annual depreciation |
|:--|--:|:--|--:|
| IT equipment (GPUs + networking + storage) | 2.7 | 5 years | $540M/yr |
| Building / facility (M&E, cooling, electrical) | 1.1 | 20 years | $55M/yr |
| **Total annual depreciation** | **3.8** | mixed | **~$595M/yr** |

*Source: IT CapEx anchored to SemiAnalysis Meta H100 cluster decomposition [@pytorch-meta]; building CapEx at US\$11M/MW per `data_centres_usa.md` §7.*

Depreciation at US\$595M/year is **~5× the cash OpEx** of US\$119M at 90% utilisation. Energy as % of TCO (cash OpEx + depreciation) collapses from 73% (cash OpEx basis) to ~12% (TCO basis). The thesis "energy is dominant at high utilisation" is correctly framed about cash operating cost; on a total-cost basis, GPU depreciation still dominates.

**On the depreciation life choice.** The current literature is split:

- **Microsoft, Meta, Google extended to 6 years** in 2023-24 SEC filings; Meta booked a US\$2.9bn 2025 depreciation reduction; Google US\$3.4bn in 2023.
- **AWS shortened from 6 back to 5 years** in February 2025, citing "increased pace of technology development" — took a US\$700m hit to operating income.
- The economic argument for **shorter** life: each new chip generation is 2-3× better at training the next frontier model, so old chips become uneconomic for training quickly. Cloud H100 prices fell 64-75% from peak in 2 years.
- The argument for **longer** life: capacity scarcity + trickle-down dynamic means H100 fleet that trained GPT-4 in 2023-24 is now serving inference for older models economically. The chip's purpose shifts but its earning power persists.

In current conditions of extreme capacity scarcity, **5 years is the defensible central case** — the trickle-down is real but the right length is uncertain, and 5 years balances the two views. A 4-year sensitivity (US\$675M/yr IT depreciation) shows what happens if trickle-down breaks; a 6-year case (US\$450M/yr IT) shows the hyperscaler bet. Either way the answer dwarfs cash OpEx.

---

## 4. People intensity in dollar terms

The Uptime Institute survey finds operators continue to report staffing pressures — North America and Europe report difficulty filling junior operator roles; women remain ~10% or less of operations staff in 80% of respondents [@uptime-survey-2024].

In dollar terms, staff is meaningful but rarely dominant:

- A 12 MW facility employing 20 FTE at fully-loaded US\$120k = **US\$2.4M/year**, ~5-8% of facility OpEx.
- A 40 MW facility employing 45 FTE at US\$120k = **US\$5.4M/year**, similar share.
- A 100 MW hyperscale at 0.4 FTE/MW (40 FTE) = **US\$4.8M/year**, ~5% of OpEx at typical utilisation.
- A 100 MW AI training campus at 0.2 FTE/MW (20 FTE) = **US\$2.4M/year**, ~2-3% of OpEx [@broadstaff; @thefix].

The *qualitative* importance of staff (talent shortages, certifications, 24/7 cover) is substantial; the *cost* importance is a single-digit share even in colocation. The thesis should be refined: it is not that "people costs are at least as important as energy costs" in absolute dollar terms — they typically aren't, even in traditional cloud. It is that **fixed costs collectively** (staff + maintenance + software + tax + insurance) are at least as important as energy in low-utilisation environments.

---

## 5. Australian competitive position — PPA + BESS as the key

The headline question is whether Australian data centres can compete with US ones for AI build-out. On the energy line — the dominant operating cost at AI utilisation — the answer hinges almost entirely on whether the operator uses a sophisticated **renewable PPA plus facility-contracted battery** structure or a lazy long-term firmed retail contract. The two routes produce A\$45/MWh of difference, which translates to ~US\$30/MWh-IT or US\$36M/year on a 100 MW facility.

### The Australian PPA + facility BESS structure

The structure that delivers Australian competitiveness is:

1. **Long-term renewable PPA** — typically 10-15 years, fixed-strike with CPI escalation. Recent Australian solar PPA strike prices: **A\$65-85/MWh**; wind PPAs: **A\$70-95/MWh** (NEXTDC, Microsoft Walla Walla 300 MW, AirTrunk-Google-OX2 Riverina, ACT renewables auctions, large enterprise C&I PPAs).
2. **Facility-contracted BESS** that does double-duty:
   - **Firms the renewable PPA** by time-shifting solar/wind output to match the data centre's flat load profile (~50-100 MWh per 100 MW load is typical sizing).
   - **Earns FCAS revenue** by bidding fast-frequency response into AEMO markets (~A\$5-50k/MW-year for the fastest products); thinner spinning-reserve revenue.
   - **Provides ride-through and back-up** at facility level, partially or fully replacing diesel UPS.
   - **Reduces network demand charges** by peak-shaving the 4CP-equivalent contributions.

The current best Australian example is **Quinbrook Supernode** at Brendale QLD: a US\$2.5 billion data centre adjacent to the South Pine substation, co-located with a 780 MW / 3,074 MWh BESS contracted to Origin (Stages 1-2: 520 MW / 1,856 MWh) and Stanwell (Stage 3) [@quinbrook-supernode]. The BESS is third-party owned/operated under a tolling model, but the principle generalises: the BESS earns NEM dispatch and FCAS revenue while providing facility-level firming.

**AWS's April 2026 Australian PPAs** make the structural pattern explicit: 9 new contracts totalling 430 MW, **eight of nine include co-located BESS at the renewable site** [@energy-storage-news-aws]. This is the first time AWS has signed solar-plus-storage PPAs outside the US, and it's the most operationally significant Australian data-centre flexibility instrument to date. Microsoft signed a 15-year PPA for 100% offtake of FRV's 300 MW Walla Walla solar farm, commissioned October 2025 [@pvtech-walla-walla].

### Effective energy cost build-up for an AU PPA + BESS data centre

| Component | Cost (A\$/MWh) | Notes |
|:----------|--------------:|:------|
| Solar PPA strike (notional) | 70 | 10-year fixed; mix of generation profile |
| BESS firming layer (capex amortised + arbitrage) | 25 | 4-hour BESS at A\$300-400/kWh installed; ~A\$15-30/MWh-firmed |
| Network charges (transmission-connected, typical) | 18 | NSW TUOS + DUOS for industrial |
| FCAS revenue offset | -8 | A\$15-50k/MW-year FCAS divided by full energy throughput |
| Other (market fees, RERT, ancillaries) | 5 | |
| **Effective firmed renewable price (delivered)** | **~A\$110/MWh** | ~ US\$71/MWh |

*Source: ITK build-up; PPA strike from ACT auctions and AirTrunk/Microsoft disclosures; BESS firming layer derived from CSIRO GenCost 2024-25 BESS LCOE; FCAS offset from AEMO 2024-25 FCAS market data; network charges from AER.*

This puts an Australian PPA + BESS data centre at delivered ~**US\$71/MWh** all-in, against PJM Dominion at ~US\$105/MWh and ERCOT West Texas at ~US\$65/MWh. **Australia is competitive with the cheap US locations and decisively cheaper than the expensive ones.**

### NextDC FY25 — the only listed-co disclosure

NextDC reported FY25 net revenue of **A\$350.2M** (+14% YoY) and underlying EBITDA of **A\$216.7M** (+6%), on billing utilisation of **110.9 MW** at year-end and contracted utilisation of **244.8 MW** (+42% pro-forma) [@proactive-nextdc; @nextdc-fy25-ar]. Net revenue is gross revenue less direct costs, where "direct costs" are predominantly customer power passthrough.

NextDC's commentary on FY25 direct costs is informative: "Direct costs fell in FY25, reflecting the benefit of lower contracted energy prices compared with FY24." Facility cost growth was attributed to "higher facility staff costs from new data centre openings, expanded capacity and investments in physical security and systems, increased water and sewerage expenses aligned with customer consumption growth, higher maintenance costs due to significant increase in built and operating capacity to meet demand, and increased property costs reflecting land banks, new site acquisitions, and land revaluations" [@nextdc-fy25-ar]. The list is a textbook traditional-colo OpEx mix: staff, security, water, maintenance, property — energy is conspicuously *not* in the list, because it's a passthrough to tenants.

### AirTrunk and Quinbrook — the two structural plays

AirTrunk operates >2.6 GW across six markets; Australian operating capacity (SYD1+SYD2+SYD3+MEL1+MEL2) will exceed **1.2 GW** when fully built [@airtrunk-mel2]. AirTrunk's FY24 sustainability report puts annual operating PUE on a downward path toward a **1.23-1.28 target** with design PUE of 1.15 — best-in-region [@airtrunk-clean]. AirTrunk has signed renewable PPAs but does not publicly disclose facility-BESS arrangements. Financial statements are not public following the September 2024 sale to Blackstone.

Quinbrook Supernode (above) is the most explicit Australian instance of co-locating BESS at hyperscale data centre site. The model is replicable elsewhere if (a) the developer can secure a substation interconnection that supports both load and generation, and (b) a battery operator wants the tolling counterparty.

### What the colocation rent comparison shows

CBRE H2 2025 colocation pricing data shows Sydney core zone wholesale rates pushing past **US\$150/kW/month** (~A\$232/kW/month) — high but still below Silicon Valley (\$230-270) and similar to Northern Virginia [@cbre-h1-2025; @aitool-colo]. **Colocation rent is in the same ballpark globally.** Where Australia differs is the energy line — and as the worked examples show, that energy difference can run *either way* depending on whether the AU operator goes PPA + BESS (cheaper than PJM Dominion) or firmed retail (still cheaper than PJM Dominion but by less).

The competitive Australian story therefore depends on:

- **Operators choosing PPA + BESS structures** (AWS, Microsoft, Quinbrook, AirTrunk are doing this; smaller operators less so).
- **Sufficient transmission interconnection** to deliver the renewable + BESS output to the data centre site (the Macquarie Park substation upgrades and AEMO IASR interconnection-queue management both matter).
- **AEMC IPRR rule (effective May 2027)** to formalise BESS participation in NEM dispatch markets, opening more revenue streams for the facility BESS.
- **The Wisconsin PSC May 2026 ruling-style cost-allocation** not crossing into Australia. NEM data centres currently escape PJM-style capacity-cost socialisation; that needs to remain the case.

---

## 6. Are Australian data centres competitive?

The over-arching question is whether Australian data centres can compete with US ones for AI build-out. On the energy line — the dominant operating cost at AI utilisation — the answer breaks into three parts.

### On energy cost: yes, with the right structure

The corrected per-region analysis shows:

- **Australia's NSW/VIC/QLD with PPA + facility BESS** delivers all-in electricity at **~US\$71/MWh** — competitive with ERCOT West Texas (US\$65), cheaper than PJM general (US\$85), much cheaper than PJM Dominion (US\$105) and CAISO Silicon Valley (US\$110).
- **Australia's "lazy" route** (long-term firmed retail at A\$140/MWh = US\$90/MWh) is more expensive than ERCOT but still cheaper than PJM Dominion.
- **The Australian disadvantage is against the cheapest US locations only** — Microsoft Quincy WA at US\$45/MWh on Grand Coulee hydro is the floor, and no Australian site matches it.

For the data centre operating economics that matter for AI, **Australia is competitive with the US average and cheaper than the US incumbent hubs**. The Quinbrook Supernode model (data centre + co-located BESS + renewable PPA at the substation) is the structural play.

### On other operating costs: yes, modestly

Australian fixed OpEx is ~12% lower than the US in USD-equivalent terms once labour costs are properly priced (AU staff cheaper than US staff at FX-equivalent rates). Australian colocation rent is in the same ballpark as US Tier-1 markets. Australian PUE for new builds (AirTrunk 1.15-1.28) matches global best-in-class.

### On the things that could undermine the position

- **Transmission interconnection.** AEMO has 44 GW of data centre connection requests against 6 GW required under Step Change — a queue-management problem the AEMC Package 2 rule (draft March 2026, final mid-2026) is trying to address. Without timely transmission, the PPA + BESS competitive advantage cannot be physically delivered.
- **NEM does not have a PJM-style capacity market** that data centres pay into. If the Capacity Investment Scheme evolves toward a per-MW levy that captures large loads, Australian electricity competitiveness narrows. Worth watching.
- **Political tolerance.** The "must power itself" coalition (Feb 2026 industry/union/environment letter) and the *National AI Plan Expectations* set the political frame at "build the renewables you consume". A PPA + BESS structure satisfies that expectation cleanly; firmed retail from the existing grid does not.
- **Talent and scale.** Australian data centre operating talent pools are smaller than US clusters, and the largest single Australian campus is roughly one-quarter the scale of the largest named US under-construction project. Some hyperscaler deployments will go elsewhere on scale grounds regardless of energy cost.

### Net read

For training clusters and inference workloads at high utilisation, **Australian electricity is competitive at the level that matters** — the marginal MWh delivered to a sophisticated AI campus running PPA + BESS is among the cheaper options globally, and meaningfully cheaper than the PJM Dominion zone where most US capacity is currently being added.

The Australian competitive position is *not* obvious from headline retail electricity prices (which are higher than US averages), but it *is* obvious from the per-region delivered prices an AI operator actually faces. The Australian operator's job is to use the structure (PPA + BESS) that delivers the competitive price; the Australian regulator's job is to keep the transmission interconnection moving fast enough to enable it.

## 7. Implications for the economics of AI data centres

Setting up the forthcoming economics piece, five conclusions follow:

1. **For training clusters at 80-95% utilisation, energy is the dominant cash operating cost — between 67% in Quincy and 77% in PJM Dominion.** A 100 MW training campus spends US$46-108M/year on electricity against ~US$30M/year on everything else combined. The competitiveness of any given site is overwhelmingly determined by its delivered electricity price, not its labour or maintenance costs.

2. **PPA pricing matters more for AI than for cloud.** A 10% improvement in \$/MWh contracted price improves training-cluster cash margin by ~7% directly. The same improvement for a 30%-utilised cloud facility moves margin by only ~3-4%. That is why hyperscalers are willing to pay massive premia (Microsoft's Three Mile Island restart, Stargate's on-site gas) to lock in firm, low-priced power — and why Australian operators with PPA + BESS structures have a real advantage over PJM Dominion-bound competitors.

3. **Inference utilisation variability is itself a cost-structure problem.** A frontier inference cluster oscillating between 20% utilisation overnight and 90% utilisation during peak hours faces the worst of both worlds — it pays for fixed cost continuously but only earns revenue when utilised. NVIDIA's own analysis shows the cost-per-token doubles at 40% utilisation versus 80% [@nvidia-utilisation]. This is the economic argument for batching, multi-tenant inference, and time-shifting workloads to track cheap power. The PPA + BESS structure helps because it allows wholesale arbitrage *within* the firmed PPA envelope.

4. **Per-token sensitivity to electricity price.** Using the SemiAnalysis Meta-cluster numbers as anchor (US\$0.16/H100-hour electricity), a Hopper-class GPU producing ~500-1,000 output tokens/sec at saturation generates ~1.8-3.6M tokens/hour, putting electricity at roughly **US\$0.04-0.09 per million output tokens** at US wholesale prices. Anthropic and OpenAI publicly charge US\$3-25 per million output tokens [@finout-pricing]. Electricity is therefore on the order of **0.2-3% of revenue per token** at API list prices — but a much larger share of *cost*, which is why inference gross margin expansion correlates so tightly with model efficiency improvements (Blackwell's claimed ~35× lower cost per million tokens vs Hopper [@nvidia-tokenomics]).

5. **GPU depreciation remains the elephant.** The Meta cluster TCO is **71% CapEx amortisation, 29% OpEx**, of which two-thirds of OpEx is rent. Electricity is "only" ~9% of TCO. So while energy is the dominant *operating* cost at high utilisation, it is still well behind GPU depreciation in any total-cost framing. The thesis is correctly framed as about *cash operating cost*, not total cost of operating. The Australian electricity advantage of US\$30/MWh-IT against PJM Dominion translates to ~US\$24M/year on a 100 MW facility — material, but small against the ~US\$200-300M/year of GPU depreciation on a Blackwell-class fleet.

---

## 8. Caveats

- **OpEx-versus-TCO confusion is endemic in industry sources.** Many "energy is X% of cost" claims silently lump in amortised IT refresh; most of those should be read as TCO statements, not OpEx statements.
- **Wholesale-versus-retail distinction matters.** A US\$50/MWh wholesale price typically becomes US\$70-100/MWh delivered after T&D, capacity, demand charges, and retailer margin. AU NEM prices behave similarly. Delivered/retail prices are used throughout the worked examples.
- **PUE is a deceptive simplification.** Real-world AI facilities can show PUE drift up under partial load (cooling systems lose efficiency below design point). The 1.10-1.20 numbers cited are *design* PUE; published *operating* PUE for the same facility class typically runs 1.20-1.35.
- **Tenant-versus-operator perspective produces different OpEx mixes.** The same physical kWh shows up as passthrough revenue for the colocation provider, as cost-of-goods for the tenant, and as "energy" in industry survey aggregates — hence apparent contradictions across sources.
- **GPU depreciation is the elephant in the room for AI.** This note is about *cash operating cost*; total cost of operating an AI cluster is still dominated by GPU CapEx amortisation over a 4-6 year life.
- **Australian disclosures are thin.** NextDC is the only ASX-listed pure-play; AirTrunk and CDC publish sustainability metrics but not OpEx breakdowns. The numbers in §5 are necessarily inferred from rate cards, sustainability reports and the comparable US data.

### Gaps that would need commissioning to fill

- A bottom-up OpEx model for an Australian 50-100 MW AI campus benchmarked against AirTrunk rate cards and AEMO retail tariff data (~3 weeks of analyst time).
- Direct discussion with a colo operator (NextDC, CDC, AirTrunk) under NDA on per-MW cost of power passthrough and net energy share for AI tenants.
- SemiAnalysis institutional subscription to access their AI Cloud TCO Model with explicit Australian electricity price scenarios.

---

## 9. References

The full bibliography is below. URLs are listed in plain markdown and would convert to BibTeX entries (`@org-topic-year`) for any subsequent published article. The underlying research draft is kept under `background/_research_drafts/datacentre_opex.md` for traceability.

### Industry surveys and authoritative sources

- Uptime Institute, *Global Data Center Survey 2025*. https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2025
- Uptime Institute, *Global Data Center Survey 2024*. https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.Report.pdf
- Uptime Institute, *People Challenge: Global Data Center Staffing Forecast 2021-2025*. https://intelligence.uptimeinstitute.com/resource/people-challenge-global-data-center-staffing-forecast-2021-2025
- Lawrence Berkeley National Laboratory, *2024 United States Data Center Energy Usage Report* (Dec 2024). https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- IEA, *Energy and AI* (2025). https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- CBRE, *North America Data Center Trends H1 2025*. https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025
- CBRE, *North America Data Center Trends H2 2025*. https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025
- JLL, *2026 Global Data Center Outlook*. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
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
- Finout, *OpenAI vs Anthropic API Pricing Comparison*. https://www.finout.io/blog/openai-vs-anthropic-api-pricing-comparison

### Cooling, PUE, infrastructure

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

---

*End of OpEx note. The forthcoming economics piece on AI data centres will build on this foundation, combining the energy-share trajectory above with the per-token bandwidth math from `token_memory.md`, the workload split from `training_v_inference.md`, and the reasoning compute-share from `_research_drafts/reasoning_share_*.md`. The underlying research draft is at `background/_research_drafts/datacentre_opex.md` for full source-level traceability.*
