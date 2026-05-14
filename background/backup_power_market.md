---
title: "Data centre backup power: market structure, economics and entry plays"
author: "David Leitch"
date: 2026-05-13
categories: ["Demand", "Generation"]
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

## Synthesis note

The AI capex cycle has dragged data centre backup power — a sleepy oligopoly inside heavy industrial equipment — into a structural growth story. Caterpillar's Power & Energy "sales to users" grew 37% in 2025, with power generation alone up 44% and exceeding US\$10 billion. Cummins Power Systems posted 2025 revenue of US\$7.5 billion (+16%) at 22.7% EBITDA margin, rising to 29.5% in Q1 2026. Rolls-Royce mtu's data centre order intake grew almost 50% in 2024 and the company is more than doubling Series 4000 output at Mankato, Minnesota. Backlog at Caterpillar reached US\$63 billion at Q1 2026 (+79% YoY), with the Power & Energy segment most exposed.

The combination of (a) supply-constrained incumbents earning EBITDA margins approaching 30%, (b) lead times stretching into 2028, and (c) a customer base that is desperate, well-capitalised and willing to pre-pay, invites the entry question. The honest answer is that beating Caterpillar, Cummins or mtu on the box is implausible — the structural moat is the dealer service network, not the engine. But adjacent plays exist: independent service, backup-as-a-service, lead-time arbitrage on refurbished kit, and HVO logistics. This note pulls the three underlying research drafts together and frames each.

Underlying drafts: [`backup_gensets_incumbents.md`](_research_drafts/backup_gensets_incumbents.md) (market structure), [`backup_gensets_economics.md`](_research_drafts/backup_gensets_economics.md) (unit economics), [`backup_gensets_alternatives.md`](_research_drafts/backup_gensets_alternatives.md) (alternatives and entry).

---

## 1. The incumbent oligopoly

Above 2 MW per set, the data centre standby market has three serious vendors — Caterpillar, Cummins, Rolls-Royce mtu — plus Kohler/Rehlko at the upper end of the second tier, Mitsubishi (MHI) and Generac as price-positioned alternatives, and a long tail (FG Wilson/Perkins, HD Hyundai Infracore, Volvo Penta) that effectively does not play above 2 MW for hyperscale standby. Wärtsilä sits in a different box — large gas reciprocating engines sold as on-site prime power, not as NFPA 110 standby.

**Table 1. Data centre standby genset product lineup at 1 MW+**

| Supplier | Lead model(s) | Engine | Standby kW (60 Hz) | Notes |
|:---------|:---------------|:--------|-------------------:|:------|
| Caterpillar | 3516E | 78-litre V16 | 2,500–3,000 | Workhorse of US hyperscale. |
| Caterpillar | C175-16 / C175-20 | 85 / 106-litre quad-turbo | 2,500–3,500 | Higher power density; top of diesel range. |
| Cummins | QSK60 / QSK78 / QSK95 | 60 / 78 / 95-litre V16/V18 | 1,500–3,500 | QSK95 (Centum) capacity doubled in 2025. |
| Cummins | S17 (launched 2025) | 17-litre V8 | up to 1,000 | Small-footprint clean-sheet entrant. |
| Rolls-Royce mtu | 16V/20V 4000 DS series | 76 / 95-litre | 2,250–3,250 | Series 4000 is the DC mainstay. |
| Kohler / Rehlko | KD3000/3500/4000 | 78–95-litre | 2,800–4,000 | Engines from Liebherr / mtu collaboration. |
| Generac | SDMD2250–3250 | Baudouin 65 / 87.5-litre | 2,000–3,250 | Launched April 2025; 12-14 month lead time as differentiator. |
| Mitsubishi MHI | MGS-R | 50–60-litre | up to ~2,200 | Singapore-built; APAC strength. |

*Source: OEM technical datasheets — Caterpillar, Cummins, Rolls-Royce mtu, Kohler/Rehlko, Generac, MHI. Where the OEM publishes only kVA, kW assumes a 0.8 power factor.*

A point Australian readers usually miss: published 50 Hz ratings are typically 10-15% lower than 60 Hz ratings for the same engine, a consequence of running speed (1,500 vs 1,800 rpm) and thermal limits. Australian sites with the same nameplate MW therefore need slightly more units than US equivalents.

**Table 2. Indicative incumbent share of global data centre standby shipments (>1 MW)**

| Supplier | Indicative share | Geographic strength | Channel structure |
|:---------|----------------:|:--------------------|:------------------|
| Caterpillar | 35–45% | US (dominant), AU/NZ, ME, India | Dealer (WesTrac/EPSA, Foley, Boyd, Toromont) |
| Cummins | 20–30% | US, India, China, UK | Mixed direct + dealer |
| Rolls-Royce mtu | 15–25% | Germany, EU, growing US, AU via Penske | Distributor (AVK in EU, Penske in AU) |
| Kohler / Rehlko | 5–10% | US, EU | Distributor + direct |
| Generac | 2–5% | US sub-1 MW; growing 2–3 MW | Direct + dealer |
| MHI | 2–5% | Japan, SE Asia, ME | Direct |

*Source: Triangulated from Mordor Intelligence, Research and Markets / ABI Research, and OEM-reported segment revenues. Treat as directional — methodology in published surveys is opaque and the widely-cited 42% / 24% / 21% split for Cat/Cummins/mtu is not transaction-verified.*

The combined share of the top five is consistently estimated at 60-75% globally. The remainder is fragmented among regional packagers (FG Wilson with Perkins, AVK with mtu, Himoinsa) and aftermarket repackagers. A useful framing: one tier builds the engine and packages the genset (Cat, Cummins, mtu, MHI, increasingly Generac via Baudouin); another buys engines and packages them. The packaged sub-segment has thinner margins and is the channel through which Chinese and Indian volume could plausibly attack the market.

## 2. Lead times and capacity — the binding constraint

The single most telling fact about this market in 2026 is that order books extend into 2028. Cummins CEO Jennifer Rumsey told the Q4 2025 call that "we're taking orders now well into 2028". Generac, in deliberate market-entry positioning, quotes 50-60 weeks (12-14 months) — half the incumbent lead time.

**Table 3. Data centre genset lead times — 2-3 MW class**

| Period | Typical lead time | Comment |
|:-------|:------------------|:--------|
| Pre-2022 | 10–14 months | Competitive bidding; stable. |
| 2023 | 14–18 months | First AI orders begin queueing. |
| Q4 2024 | 18–22 months | Hyperscalers buying multi-year forward. |
| Q4 2025 | 22–30 months | Cummins QSK95 cited at 18 months pre-expansion. |
| Q1–Q2 2026 | 24–30 months | Generac at 12–14 months for new lineup. |

*Source: OEM earnings transcripts (Cummins, Caterpillar), Mordor Intelligence, Generac press releases.*

Capacity expansions announced 2024-2026 — Caterpillar US\$725 million at Lafayette, Indiana; Cummins US\$150 million at Fridley, Minnesota; mtu US\$24 million at Mankato lifting Series 4000 output by 120%+ — do not close the gap inside the planning horizon. Caterpillar's ~125% nominal capacity lift over two years has been overrun by order intake more than doubling.

New entrants offering credible 2027-2028 delivery would find buyers. The question is whether they can be credible — and the answer is that the customer set for first-time suppliers is mid-tier colocation and edge, not Stargate-class hyperscale.

## 3. Unit economics — the 3 MW reference machine

Two anchor units represent current US and global hyperscale spec. The Caterpillar 3516E HD (2,750 ekW standby, V16, 78.1-litre, 1,800 rpm) is the US workhorse; the mtu 20V4000 DS3000 (3,000 ekW, V20, 95.4-litre) is the European and APAC reference. The Cummins QSK60 (2,500 ekW, V16, 60.2-litre) is the third option.

**Table 4. Reference standby gensets, 2.5–3 MW class**

| Parameter | Caterpillar 3516E | mtu 20V4000 DS3000 | Cummins QSK60-G23 |
|:----------|------------------:|-------------------:|------------------:|
| Standby rating (ekW) | 2,750 | 3,000 | 2,500 |
| Engine configuration | V16 | V20 | V16 |
| Displacement (L) | 78.1 | 95.4 | 60.2 |
| Specific power (kW/L) | 35.2 | 31.4 | 41.5 |
| Dry weight, set + radiator (t) | ~19.8 | ~21.5 | ~23.0 |
| Footprint L×W×H (m) | 7.5 × 2.2 × 3.4 | 7.7 × 2.3 × 3.6 | 8.0 × 2.3 × 3.7 |
| EPA standby tier | Tier 2 | Tier 2 | Tier 2 |
| Tier 4 Final aftertreatment option | SCR + DPF + DEF | SCR + DPF + DEF | SCR + DPF + DEF |

*Source: Caterpillar 3516E datasheet LEHE1351-09; mtu Onsite Energy 20V4000 DS3000 G04 spec; Cummins QSK60-G23 standby spec sheet, Rev-03 (May 2023).*

### Fuel consumption — the curve that matters

Caterpillar publishes the following at 2,750 ekW standby for the 3516E. This is the single most-cited dataset because it sizes both bulk fuel inventory and operating cost.

**Table 5. Caterpillar 3516E HD fuel consumption (2,750 ekW standby, 60 Hz)**

| Load | Fuel rate (L/hr) | Fuel rate (US gph) | Specific fuel consumption (g/kWh) |
|:-----|-----------------:|-------------------:|----------------------------------:|
| 25% (687 kW) | 184.4 | 48.7 | 225 |
| 50% (1,375 kW) | 309.0 | 81.6 | 188 |
| 75% (2,063 kW) | 431.8 | 114.1 | 175 |
| 100% (2,750 kW) | 563.8 | 148.9 | 172 |

*Source: Caterpillar 3516E specification sheet LEHE1351-09. Cummins QSK60 confirmed at 535 L/hr at full standby load; mtu 20V4000 DS3000 sits at roughly 690-720 L/hr at 3,000 ekW. All three OEMs converge near 0.20-0.22 L/kWh at full load.*

The conservative sizing rule is **0.22 L/kWh at full standby load**, equivalent to 660 L/hr for a 3 MW set. That is the number used below to size hyperscale fuel inventory.

### Pricing — bare box and installed

**Table 6. Indicative installed cost — 3 MW data centre standby genset, US/AU 2026**

| Cost component | US\$/kW | Comment |
|:---------------|------:|:--------|
| Bare genset (engine + alternator + radiator + base controls) | 550–700 | 2026 spot; +30-40% vs 2022. |
| Sound-attenuated weatherproof enclosure | 80–150 | Singapore/HK higher (65 dBA boundary limit). |
| Day tank + sub-base belly tank | 60–100 | Excludes bulk farm. |
| Critical-grade exhaust + silencer | 40–70 | Tier 4 Final would add +100-150. |
| Switchgear, paralleling, ATS, MV interface | 200–350 | Site-dependent. |
| Installation labour, foundation, integration | 150–300 | US union markets at top end. |
| Commissioning, load-bank test, freight | 60–120 | |
| **Total installed, Tier 2 emergency standby** | **1,500–2,200** | A 3 MW unit lands at ~US\$4.5–6.5M installed. |
| Add for Tier 4 Final (SCR/DPF/DEF) | +200–350 | CA, parts of NY/NJ, EU Stage V. |
| Add for medium-voltage paralleling switchgear | +100–250 | Hyperscale 13.8/22 kV bus. |

*Source: Cummins technical brief on data centre gensets; Latitude Media vendor pricing benchmarks; EIA generator construction cost data. ±20% on the 2026 spot — OEMs do not publish.*

Direction of travel since 2022: roughly +30-40% on the bare box, around +50% on the integrated package. Copper (alternator windings), electronics (engine controls, paralleling), specialist labour and unmatched pricing power on the supply side are the drivers. Australian-installed pricing sits at the upper end of the global range — typically US\$2,000-2,500/kW for a 3 MW unit, reflecting transport, lower local fabrication content, acoustic and bushfire compliance loads.

### 96-hour autonomy — the TIA-942 number

ANSI/TIA-942 Rated-4 specifies 96 hours of on-site fuel storage (AHJ may substitute contracted refuelling for some inventory). NFPA 110 Level 1 reaches the same number via a different route. Note: this is a **TIA-942 design requirement, not an Uptime Institute Tier IV requirement** — the Uptime spec is only 12 hours and the conflation is common in trade press.

At 660 L/hr per 3 MW set running at full load, one set running 96 hours needs 63,360 L of usable fuel, or ~84,300 L of nameplate tank capacity once the NFPA 110 133% ullage factor is applied.

### Hyperscale build-up — 100 MW IT, Rated-4, 2N

For a 100 MW IT facility at PUE 1.3, the backed-up load is ~130 MW. At 2.75 MW per Cat 3516E mission-critical rating, a 2N+1 design lands at roughly 100 sets totalling ~275 MW nameplate. Larger 4 MW C175-20 or 20V4000 DS4000 architectures reduce set count to ~68 sets.

**Table 7. Backup power system capex — 100 MW IT, Rated-4, 2N**

| Component | Total (US\$ million) |
|:----------|---------------------:|
| Gensets (100 × 2.75 MW Tier 2 with enclosure and sub-base tank) | 100–140 |
| Medium-voltage switchgear, paralleling (two sides) | 10–16 |
| Automatic transfer switches and distribution | 6–10 |
| Paralleling controls, EMCP, synchronisers | 2–4 |
| Bulk fuel tanks (~4 ML self-bunded steel) | 10–14 |
| Day tanks, transfer pumps, fuel polishing | 2–4 |
| Fuel-oil piping, valves, leak detection | 2–4 |
| Civils, foundations, enclosures, exhaust stacks | 8–14 |
| Engineering, commissioning, witness testing | 7–14 |
| **Total backup power system** | **147–220** |
| **Per MW IT installed** | **US\$1.5–2.2M/MW** |

*Source: Author build-up using OEM list prices and Cushman & Wakefield Data Center Development Cost Guide 2025. The gensets themselves are 65-70% of system cost; switchgear and paralleling 10-15%; fuel storage and distribution 12-15%.*

For context, the backup power slice is 8-12% of total air-cooled hyperscale capex (US\$11M/MW IT anchor) — third or fourth-largest line item, roughly the same size as the UPS-and-battery system. For an AI-optimised liquid-cooled build at US\$22M/MW IT, the backup slice falls proportionally to 4-6% but the absolute size is similar because the joules backed up are similar.

### Fuel inventory and Australian dangerous-goods envelope

At 660 L/hr × 50 paralleled sets per side × 96 hours, one-side inventory comes to ~3.17 million litres. Practical specification rounds to **4 million litres of bulk diesel** for a 100 MW Rated-4 facility, distributed across 30-50 tanks. Some operators size for full 2N × 96-hour (~6 ML). At AU\$1.80/L wholesale, that fuel inventory represents AU\$7-11M of working capital.

The Australian regulatory envelope under AS 1940:2017 and the model Work Health and Safety regulations:

**Table 8. Australian above-ground diesel storage thresholds (Class C1 combustible)**

| Threshold | Quantity (L) | Trigger |
|:----------|-------------:|:--------|
| AS 1940 "minor storage" upper limit | 10,000 | Full AS 1940 fire-protection, bunding, separation distances |
| Placard quantity (notification) | ~10,000 | State dangerous-goods regulator notified; placards |
| High-level alarm required | 25,000 | AS 1940:2017 update |
| Manifest quantity (full notification) | 100,000 | Manifest to regulator and fire brigade |
| Major Hazard Facility threshold | ~6,000,000 (5,000 t C1) | MHF licensing under model WHS Schedule 15 |

*Source: AS 1940:2017; Bulk Fuel Australia 2019 Guide; Safe Work Australia Schedule 15 to model WHS Regulations. The diesel-only MHF threshold is not reached at a 4 ML site, but a 100 MW campus is comfortably above placard and manifest quantities.*

A hyperscale operator at 4-8 ML is firmly inside dangerous-goods territory but below MHF for diesel alone. The compliance load — licensed dangerous-goods premises, AS 1940 bunding, NFPA 30 fire water, hot-work permits, pre-incident plans — is real and is a meaningful barrier to entry for sub-scale operators.

### Operating cost

**Table 9. Annual opex per MW IT, backup power system (100 MW Rated-4)**

| Cost item | US\$/year | US\$/MW IT/yr |
|:----------|---------:|--------------:|
| Routine PMs and parts | 1,200,000 | 12,000 |
| Annual stepped load-bank testing | 250,000 | 2,500 |
| Diesel consumed in load-bank tests (~1.65 ML/yr) | 500,000 | 5,000 |
| Fuel polishing and quality testing | 200,000 | 2,000 |
| Fuel inventory turnover (every 18-24 months) | 600,000 | 6,000 |
| Lube oil, coolant, filters | 200,000 | 2,000 |
| OEM 24/7 service contract | 1,500,000 | 15,000 |
| Insurance, dangerous-goods compliance, spill response | 400,000 | 4,000 |
| Operator labour allocation | 800,000 | 8,000 |
| **Total annual opex** | **5,650,000** | **56,500** |
| As % of installed capex | ~3.4% | |

*Source: Author build-up. Routine maintenance from Cummins and Caterpillar service literature; fuel polishing from Bell Performance and Mojo Fuel; diesel pricing from Australian Institute of Petroleum terminal-gate data.*

Two observations. First, the working-capital cost of holding 4 million litres is itself material: AU\$7-11M at 6% pre-tax cost of funds is ~AU\$450,000/year. Second, fuel inventory turnover is a substantive cost — diesel cannot sit indefinitely; operators rotate every 18-24 months at AU\$0.20-0.40/L of capacity per flush. Quarterly load-bank tests burn ~1.65 ML of diesel per year per 100-set facility, costing AU\$2.5-3M at 2026 prices.

The DC standby service market is ~US\$3-4 billion globally and growing 15-20% as the installed base catches up with the build pipeline. Aftermarket gross margins of 35-45% (vs 15-25% on the box) explain why Caterpillar's dealer footprint — WesTrac/EPSA in Australia, Foley/Boyd/Toromont in North America — is the real structural moat.

## 4. The aftermarket moat

A new entrant could plausibly compete on the genset. Competing on the 20-year service relationship is the harder problem. Service requirements at hyperscale typically include:

- Quarterly inspection (visual, fluid, controls)
- Semi-annual oil and filter change even on low hours
- Annual load-bank test at 100% rated load for 2-4 hours (NFPA 110 explicit)
- Annual fuel testing and triennial polishing (diesel degrades from ~6 months; polishing extends to 5+ years)
- 10-year major overhaul depending on starts and run hours

A typical service contract for a 3 MW unit runs US\$25,000-50,000/year for parts and labour, US\$5,000-15,000/year for fuel testing and polishing, plus load-bank events at US\$5,000-10,000 each. A hyperscale fleet of 30-40 units therefore generates US\$1-2 million/year per site in recurring revenue, almost all flowing through the original OEM's authorised channel.

Caterpillar's competitive edge is not the engine — it is the dealer footprint, larger by a factor of 3-5× versus Cummins or mtu in most regions. WesTrac/EPSA in Australia is a billion-dollar service business in its own right, with technicians within a 4-hour drive of essentially every Caterpillar standby genset they have ever sold. Penske is the equivalent for mtu in Australia, with NEXTDC as the marquee customer (40+ 20V4000 units across the M-series).

## 5. Alternatives reshaping the segment

Diesel remains incumbent for the strict NFPA 110 emergency-standby role. Three pressures are reshaping the broader on-site power market:

1. **Lead-time stretch:** Cummins and Caterpillar effectively on allocation since mid-2024.
2. **Permitting friction:** Virginia DEQ moved presumptive BACT for new DC gensets to Tier 4-equivalent from July 2026. California already requires CARB DG certification. NSW EPA is scrutinising NOx/SOx assumptions on Project Mars (Lane Cove West).
3. **Scope 1 accounting:** Hyperscaler net-zero commitments sit awkwardly with on-site combustion even at 10-50 hours/year.

The result is that alternatives are taking adjacent roles — prime power, grid bridging, longer-duration ride-through — rather than displacing diesel one-for-one.

**Table 10. Commercial maturity of diesel-genset alternatives at hyperscale data centres, May 2026**

| Technology | Maturity | Lead time | Indicative capex (US\$/kW) | Role |
|:-----------|:--------:|:---------|:--------------------------|:------|
| Diesel reciprocating | Mature | 18–24 months | 700–1,100 (box) / 1,500–2,200 (installed) | Reference standby |
| Gas reciprocating, high-speed (Jenbacher J624) | Commercial | 15–24 months | 1,700–2,000 | Prime + standby microgrid |
| Gas reciprocating, medium-speed (Wärtsilä 34SG/50SG) | Commercial | 15–24 months | 1,700–2,000 | Hyperscale BTM prime |
| Aero gas turbine (GE LM2500XPRESS, Mitsubishi FT8) | Commercial | 18–36 months | 1,700–2,000 | BTM prime, large hyperscale |
| Heavy-duty gas turbine (GE 7HA/9HA) | Commercial, supply-constrained | 36–60+ months | 800–1,200 | Utility-built behind contract |
| Industrial gas turbine (Solar, Siemens SGT-800) | Commercial | 12–36 months | 1,500–1,800 | Hot-climate hyperscale |
| Bloom SOFC fuel cell | Commercial | 90 days from order | 3,000–4,000 | Permit-constrained sites |
| FuelCell Energy MCFC | Approaching commercial | 18–24 months | ~3,000–4,000 | Korean DC market |
| BESS for ride-through (Megapack, Quantum) | Mature | 6–12 months | 400–500/kWh | UPS extension; PPA firming |
| HVO drop-in fuel | Commercially supplied | — | 30–60% fuel premium | Decarbonisation optics |
| Mainspring linear generator | Early-commercial | <12 months | n/d | Niche, fuel-flexible |
| Hydrogen reciprocating | Pilot | — | — | Demonstrations only |
| Hydrogen PEM fuel cell | Pilot | — | — | Demonstrations only |

*Source: SemiAnalysis "Onsite Gas Deep Dive" Oct 2025; OEM datasheets; trade-press deployment announcements (Wärtsilä, INNIO, Cat, Cummins, GE Vernova, Solar Turbines, Bloom Energy, Mainspring); AWS Australia PPA disclosures.*

The single largest dollar flow today is **behind-the-meter natural gas reciprocating** at hyperscale — Wärtsilä has booked over 1.6 GW of 34SG/50SG units for US data centres (412 MW Ohio, 790 MW Texas, 507 MW elsewhere); VoltaGrid is delivering 2.3 GW of Jenbacher J624-based QPac modules for Oracle and >1 GW for Vantage. Meta's Louisiana Hyperion campus is taking 2,250 MW of new gas turbines via Entergy. This is not displacing standby diesel — it's replacing the **grid connection** that the operator can't get.

A useful Australian framing: AWS Australia's 8-of-9 PPAs with co-located BESS is a renewable-firming play (BESS at the generator site doing PPA shape-firming, FCAS and arbitrage), **not** a behind-the-meter campus backup play. AWS data centres themselves still use conventional UPS+diesel for true ride-through. The "BESS replaces gensets" narrative is overstated.

Hydrogen at hyperscale is pre-commercial in every dimension that matters: green H2 fuel cost in Australia at A\$8-15/kg translates to A\$400-820/MWh of electricity through a 55-60% efficient PEM fuel cell, against gas at ~A\$80-120/MWh and diesel at A\$140-180/MWh. Engines are certified or ready; fuel supply, storage and cost are not.

## 6. Where the entry gap sits

The market today rewards capacity. Incumbents are not under price pressure. Aftermarket margins are protected by long-tail dealer networks. Lead times are quoted on a multi-year basis and customers pre-pay.

Entry as an OEM is implausible inside a 5-year window. Four adjacent plays are credible, ranked here on capital intensity and time-to-revenue:

### 6.1 Independent data-centre-grade service operator — capital-light, high margin

The third-party hardware maintenance market is fragmented globally and almost absent in Australia for data-centre-grade gensets. Existing AU independents (Cirrus Power on Jenbacher; regional diesel servicers) serve mining, hospitals and telcos rather than hyperscale critical-power.

A focused DC-grade service operator with NATA-accredited fuel quality testing, predictive-maintenance instrumentation, 24/7 emergency response SLA and OEM-parts supply agreements could win mid-tier business (colocation, edge, secondary hyperscale) at 30-40% below OEM service contracts. Service annuities are valuable on a multiple at exit; counterparty credit is the main risk.

The catch: hyperscalers stay with the OEM service contract on warranty/insurance grounds for the first 5-10 years of asset life. The window opens as fleets age — perhaps 7-10 years out from major Australian build dates (so 2030-2035 for the current AirTrunk/NEXTDC wave). Building the service infrastructure now is a long-horizon play.

### 6.2 Backup-as-a-service (BaaS) operator — capital-medium

Most colocation and mid-tier DC operators do not want to own, maintain, fuel-manage, run quarterly load tests, manage emissions reporting, or carry the capital line for their backup fleet. A BaaS operator owns the gensets, BESS, controls and fuel supply, and charges \$/MW/year for guaranteed availability under SLA.

Existing players who partially do this — Aggreko (short-term rental), Enchanted Rock (microgrid-as-primary with energy charge), some utility-affiliated providers — do not offer "long-term availability-fee BaaS" as the headline product.

Why this fits Australia: NEXTDC, CDC, DCI, Macquarie and Equinix are capital-constrained relative to US peers. A leasing/BaaS model relieves the balance sheet. The model fits a financial-sponsor profile (infra debt, super funds) needing long-duration availability-linked cash flows. Anchor with 1-2 colocation customers, then scale.

The catch: capital-heavy build (US\$700-1,200/kW funded by the BaaS operator); SLA underwriting depends on insurance/reinsurance comfort; stranded-asset risk if the DC tenant exits. Counterparty diligence is everything.

### 6.3 DC-specialised HVO supply and logistics — capital-medium, fuel-supply margin

Australian HVO supply is currently entirely imported (RD2Go, Delta Spec, Viva). BP's Kwinana biorefinery is targeted at 2026-27 first oil with SAF and HVO output. The 30-60% premium versus fossil diesel is paid by hyperscalers willing to monetise Scope 1 reductions; Microsoft Sweden, Equinix EU sites, AWS Ireland and Bridge Data Centres (APAC pilot 2026) are early adopters.

The interesting Australian wedge is **DC-grade HVO logistics** rather than competing for the bulk fuel margin: ISO-tank delivery, NATA-certified fuel testing, certificate-of-origin chain-of-custody, on-site polishing and blended-product delivery at premium pricing. Volumes per site are modest (10-30 ML/year per major DC) but unit margins are well above bulk fuel. Operational, not technology; capital scales with tank fleet.

The catch: dependent on BP Kwinana hitting timeline, or on continued import availability. Fuel-supply position is a commodity exposure not a technology moat.

### 6.4 Lead-time arbitrage — refurbished gensets, fast-track packaging — time-limited

Cat 3516 and Cummins QSK60/95 lead times of 18-24+ months out of OEM new-build channels create a 12-18 month gap. Used and refurbished 2-3 MW units trade actively in the US (Woodstock Power, Central States, USP&E, Crusader, IMP). A reseller with rigorous data-centre-grade testing, warranty, and load-bank certification can sell into the gap.

The Australian opportunity is sharper because no domestic refurbisher operates at DC scale. With AirTrunk Kemps Creek, NEXTDC S7 (the OpenAI 550 MW Stargate AU), and Microsoft Sydney expansion all building inside the OEM lead-time window, a purpose-built Sydney/Melbourne refurbishment yard with OEM-parts supply agreements and 12-month delivery guarantees would have a defensible price/lead-time wedge in colocation and tier-2 hyperscale.

The catch: hyperscalers refuse refurbished kit on warranty/insurance grounds. The buyer pool is mid-tier colocation and edge. Duration of the opportunity is 3-5 years before OEM new-build supply catches up.

### What to discount

- **A hydrogen-ecosystem-for-DCs play.** Pre-commercial fuel, unresolved storage, unappealing economics. Unlikely to commercialise at scale before 2030.
- **A small-modular-reactor-for-DCs play.** Every 2025-2026 nuclear-DC press release is 2030-2035 horizon at the earliest.
- **A head-on-with-VoltaGrid microgrid packaging play.** Too capital-intensive against entrenched ERCOT competition. An adjacent NEM-region strategy is more plausible but needs the Australian gas-supply piece to be solved.

## 7. Open questions where the synthesis is weakest

- **Precise market shares** — public sources differ by 5-15 percentage points per OEM; the directional ranking is reliable, the decimals are not.
- **2026 spot pricing per kW** — OEMs do not publish; the US\$550-700/kW bare-genset range is RFP-level chatter in trade press, not transaction-verified.
- **Tier 4 Final cost premium** — triangulated from sub-component costs rather than from OEM disclosure; the 15-25% range is indicative.
- **Australian operator brand alignment for AirTrunk, CDC, Macquarie Data Centres** — partial public disclosure only.
- **Fuel-inventory sizing convention** — some operators size 4 ML (one side × 96 hr), others 6 ML (full 2N × 96 hr). The choice swings capex by ~US\$5M per site.
- **MHF threshold for diesel** — Schedule 15 to the model WHS Regulations is paywalled in detail; the ~5,000 t (~6 ML) C1 combustible threshold should be verified before being cited externally.
- **Aftermarket service margins** — drawn from heavy-equipment industry analogues; DC-specific segment reporting is too coarse to isolate cleanly.

---

*See the underlying drafts for the deeper buildup:*
- *[`backup_gensets_incumbents.md`](_research_drafts/backup_gensets_incumbents.md) — market structure, OEM share, capacity expansions, Australian channel detail*
- *[`backup_gensets_economics.md`](_research_drafts/backup_gensets_economics.md) — fuel curves, 96-hour sizing, capex build-up, opex line items, AS 1940 thresholds*
- *[`backup_gensets_alternatives.md`](_research_drafts/backup_gensets_alternatives.md) — gas reciprocating, turbines, fuel cells, BESS, HVO, hydrogen reality check, entry-play detail*
