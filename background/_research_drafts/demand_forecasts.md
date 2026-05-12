---
title: "US Data Centre Electricity Demand: Forecast Reconciliation and Announced Project Pipeline"
author: "David Leitch"
date: 2026-05-10
status: research draft
---

# US data centre electricity demand: forecast reconciliation and announced project pipeline

## 1. Why this matters and what is being forecast

Forecasts of US data centre electricity demand published between mid-2024 and early 2026 differ by more than a factor of three for the same target year. The Lawrence Berkeley National Laboratory (LBNL) base case for 2028 is 325 TWh; Goldman Sachs Research's most recent number for 2030 is roughly 750 TWh of US-only consumption; Morgan Stanley's implied number is higher again. EPRI, the IEA, BloombergNEF, NERC and the EIA sit between these poles.

The spread is not all about underlying disagreement on AI workloads. A substantial part of it comes from inconsistent definitions. Three different quantities are routinely conflated:

- **Annual energy consumption (TWh/year)**: what the meter actually records. This is what LBNL, EIA and IEA primarily report.
- **Coincident peak demand (GW)**: the instantaneous draw the grid must serve at the system peak. This is what NERC, RTOs and utility load forecasts focus on.
- **Contracted or announced capacity (GW)**: nameplate ratings of facilities that developers have signed agreements for, including duplicated requests across multiple utilities. This is what hyperscaler press releases and interconnection queues report.

PG&E published analysis showing data centre peak load runs at about 67% of nameplate, and average load is lower again [Source: https://www.powerpolicy.net/p/the-puzzle-of-low-data-center-utilization]. So a 1 GW "announced campus" might translate to about 670 MW of coincident peak and roughly 5–6 TWh/year of energy at high utilisation — not the 8.76 TWh implied by 1 GW × 8,760 hours.

The "phantom load" problem compounds this. ERCOT's large-load interconnection queue grew from 63 GW at the end of 2024 to 226 GW by October 2025, but only 1.8% of that queued capacity was actually operational and drawing power [Source: https://www.latitudemedia.com/news/phantom-data-centers-are-flooding-the-load-queue/]. Industry observers estimate speculative interconnection requests outnumber real projects by 5–10x [Source: https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/].

The rest of this note (a) presents the major forecasts on a comparable basis where possible, (b) catalogues the largest announced campuses that are not yet under construction or are in early build, and (c) reconciles the spread.

---

## 2. Forecast comparison

The table below presents the headline US data centre demand numbers from each source. Where a source publishes a range, the central or "base" case is shown with the range in parentheses. Definitions vary — see the methodology notes that follow.

**Table 1. US data centre electricity demand forecasts (selected sources)**

| Source | Publication date | 2028 TWh | 2030 TWh | 2035 TWh | Peak GW addition by 2030 | Notes |
|:-------|:-----------------|---------:|---------:|---------:|-------------------------:|:------|
| LBNL (DOE) | Dec 2024 | 325 (low) – 580 (high), midpoint ~450 | n/a (forecast ends 2028) | n/a | n/a | Energy basis; 2023 baseline 176 TWh |
| EPRI (Powering Intelligence) | May 2024; updated Feb 2026 | n/a | 380–790 (2026 update) | ~900 (medium) | n/a | 2026 update is 60% higher than 2024 |
| IEA (Energy and AI) | Apr 2025 | n/a | ~425 (US share) | n/a | n/a | US increase 240 TWh from 185 TWh 2024 |
| EIA (AEO 2025 / 2026) | Jan 2026 / Apr 2026 | n/a | n/a explicit | n/a | n/a | Reference case: commercial computing 8% (2024) → 20% (2050) of commercial sector |
| Morgan Stanley | Aug 2025 | n/a | implied ~720 (~18% of US) | implied ~800+ | ~150 GW new DCs by 2030 (global) | 18% of US elec by 2030 |
| Goldman Sachs | Sep 2025 (revised Apr 2026) | n/a | ~750 (US); 1,350 global | n/a | US capacity 95 GW by 2030 (+197% from 2025) | Lifted 220% global growth |
| McKinsey | 2024–2025 | n/a | 606 (~11.7% of US) | n/a | 80 GW (US, from 25 GW in 2024) | Mid scenario; AI workload triples 2025–2030 |
| BloombergNEF | Dec 2025 | n/a | ~78 GW implied | n/a (energy) | n/a | 106 GW US peak by 2035; 8.6% of US elec |
| NERC (LTRA 2025) | Jan 2026 | n/a | n/a | n/a | +224 GW summer peak North America by 2035 (10-yr) | 65% increase vs LTRA 2024 |
| Grid Strategies | Dec 2025 | n/a | n/a | n/a | +166 GW US peak by 2030 (~90 GW from DCs) | 6x revision vs 2022 forecast |
| PJM Long-Term Load Forecast | Jan 2025 | n/a | +30 GW peak (2025–2030) | 1,328 TWh total RTO energy 2035 | +32 GW peak 2024–2030; 94% from DCs | RTO-wide |
| ERCOT Long-Term Load Forecast | Apr 2025; queue update Dec 2025 | n/a | 130–148 GW planning capacity | n/a | 138 GW large loads on grid by 2030 | 226 GW in queue, ~75% data centres |
| MISO | 2025 | n/a | n/a | 163 GW peak by 2035 (+35% vs 2025) | n/a | 2.7% CAGR mid case |
| SPP | 2025 | n/a | n/a | n/a | ~90 GW DC-linked of 166 GW total peak growth | Among RTOs |
| Dominion Energy (VA IRP) | Dec 2024; updated Oct 2025 | n/a | ~9 GW DC peak in 10 yrs | +20,000 MW DC growth in Dominion Zone by 2037 | n/a | 47.2 GW contracted DC pipeline |
| Georgia Power (2025 IRP) | Jan 2025; approved Jul 2025 | n/a | ~8,500 MW load growth by 2030 | n/a | 6,000–8,500 MW certified production additions | 2,600 MW above 2023 IRP |
| Entergy | 2025 | n/a | ~7 GW Meta Hyperion alone by 2030 | n/a | 13% near-term annual industrial sales growth | 80% CapEx expansion since 2023 |

Sources are listed individually under §5.

### How to read the table

- **TWh columns**: annual electricity consumption.
- **Peak GW addition**: incremental coincident peak demand (or equivalent) above 2024 baseline.
- "n/a" means the source did not publish a number for that year on the relevant basis. Most do not publish 2035 numbers explicitly; LBNL stops at 2028.

---

## 3. Where the forecasts agree, where they diverge, and why

### Areas of broad agreement

1. **Direction and magnitude**: every major source projects US data centre electricity consumption at least doubling from the 2023 baseline of 176 TWh by 2030 [Source: https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/]. The lowest 2030 number (LBNL low case extrapolated) is roughly 350 TWh; the highest (Goldman/Morgan Stanley) is roughly 750 TWh.
2. **AI is the dominant driver post-2024**. EPRI assumes AI queries draw roughly ten times the electricity of a traditional search [Source: https://www.utilitydive.com/news/artificial-intelligence-doubles-data-center-demand-2030-EPRI/717467/]. McKinsey expects AI workloads to more than triple between 2025 and 2030 [Source: https://www.mckinsey.com/industries/private-capital/our-insights/how-data-centers-and-the-energy-sector-can-sate-ais-hunger-for-power].
3. **PJM and ERCOT are the epicentres**. Every source places the largest absolute load growth in those two footprints, with MISO third on the latest data [Source: https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/].
4. **Resource adequacy is at risk in 13 of 23 NERC assessment areas** over the next five years [Source: https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf].

### Where they disagree, and why

**The Goldman / Morgan Stanley vs LBNL gap (~$2x by 2030)**:

Goldman Sachs Research lifted its global 2030 forecast to 1,350 TWh in September 2025, with the US share at approximately 750 TWh [Source: https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030]. That implies 95 GW of US capacity by 2030, up 197% from 2025. Morgan Stanley implies a similar magnitude — 18% of US electricity by 2030, which on EIA's 2030 generation projection is roughly 720 TWh [Source: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/data-center-electricity-consumption-michelle-weaver-david-arcaro].

LBNL's central 2028 case is 450 TWh, which on the same growth trajectory would reach roughly 550–600 TWh by 2030 — about 20% below Goldman.

The gap is driven by three assumption differences:

1. **AI server share and intensity**: investment-bank forecasts assume AI servers reach 27%+ of total data centre power by 2027; LBNL's mid case assumes a slower diffusion path with significant gains in chip-level efficiency.
2. **Build rate**: Goldman and Morgan Stanley take announced hyperscaler capex commitments largely at face value. LBNL applies historical build-rate constraints and a more cautious view on supply chain bottlenecks (transformers, switchgear, GPU supply).
3. **Cooling and PUE**: LBNL assumes continued PUE improvements, particularly in liquid cooling adoption. The bank forecasts assume more modest efficiency gains because AI training clusters run at sustained high utilisation that limits cooling efficiency headroom.

**The peak-GW vs annual-TWh translation**:

NERC, Grid Strategies and the RTOs report peak GW. Converting to annual TWh requires a load factor assumption. At a 65% data-centre load factor (consistent with PG&E's metered evidence), Grid Strategies' 90 GW of data-centre peak growth by 2030 implies ~510 TWh of new annual energy, on top of the ~150 TWh consumed by data centres in 2023 — a 2030 total of ~660 TWh. That sits between LBNL's high case and Goldman's number, and inside EPRI's 2026 update range of 380–790 TWh [Source: https://restservice.epri.com/publicattachment/97025].

**The phantom-load discount**:

Utility and RTO interconnection queues are massively oversubscribed. Three pieces of evidence:

- ERCOT: 226 GW in the queue, 1.8% operational [Source: https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/].
- Dominion: 47.2 GW contracted, against a forecast peak data-centre demand of 9 GW in 10 years [Source: https://virginiabusiness.com/dominion-data-center-power-demand-virginia-scc/].
- Industry estimates: speculative interconnection requests run at 5–10x the number of projects actually built [Source: https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/].

This is partly developers genuinely shopping the same load to multiple utilities, and partly a rational response to long interconnection queues — a developer who only puts a single application in cannot be sure of getting served. Texas passed legislation in 2025 requiring large-load customers to disclose duplicate filings [Source: https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/].

If utility forecasts are taken at face value, the US will need 166 GW of additional peak capacity by 2030 [Source: https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf]. If 30–50% of that is phantom (a defensible estimate given the ratios above), the build requirement is 80–115 GW, much closer to BloombergNEF's bottom-up 2035 number of 106 GW [Source: https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/].

### My read on the spread

The most defensible 2030 US data centre energy consumption range is **500–700 TWh** (12–17% of US electricity). The investment-bank top end (~750 TWh) requires both rapid AI build-out and resolution of supply chain bottlenecks; the LBNL low case (~350 TWh) requires AI training to plateau or efficiency gains to outrun workload growth, which the 2024–2026 trajectory does not support. EPRI's mid scenario, BloombergNEF's bottom-up, and the discounted Grid Strategies number all cluster in the 500–650 TWh band.

For 2035 the range widens because few primary sources publish that far ahead. BloombergNEF's 106 GW peak implies roughly 600–750 TWh at typical load factors — broadly consistent with EPRI's "around 900 TWh by 2050" central case [Source: https://restservice.epri.com/publicattachment/97025].

---

## 4. Largest announced US data centre projects not yet operational

The table below covers campuses of 500 MW or larger that have been publicly announced for commercial operation in 2027 or later. Some have early phases already energised; the "expected MW" column refers to full build-out.

**Table 2. Largest announced US data centre campuses (500 MW+, full COD 2027+)**

| Owner / partners | Location | Expected full MW | Expected full COD | Power source / utility | Status |
|:-----------------|:---------|-----------------:|:------------------|:-----------------------|:-------|
| Meta (Hyperion) | Richland Parish, LA | 5,000 (ultimate); 1,500 by end-2027 | 2030 (full); summer 2028 (initial ops) | Entergy Louisiana — 10 gas plants, ~7.2 GW, plus 1.5 GW solar | Site work since Dec 2024; financing closed Oct 2025 |
| Amazon / Anthropic (Project Rainier Phase 2) | NW Indiana (NIPSCO) | 2,400 (Phase 2 expansion) | 2027–2028 | NIPSCO — gas + renewables | Phase 1 (2.2 GW, New Carlisle) operational Oct 2025; Phase 2 announced Nov 2025 |
| OpenAI / Oracle / Crusoe (Stargate Abilene) | Abilene, TX | 1,200 | Q4 2026 (full); 0.6 GW mid-2026 | Crusoe-procured gas + renewables; ERCOT | Two of eight buildings live Sep 2025 |
| OpenAI / Oracle / SB Energy (Stargate Milam County) | Milam County, TX | 1,200 | Initial 2026; full 2027 | ERCOT | Site work underway |
| OpenAI / Oracle / STACK (Stargate New Mexico, "Project Jupiter") | Doña Ana County, NM | 1,000+ (ultimate up to 1.5 GW) | Initial 2027 | El Paso Electric / SPS | Foundation work underway |
| OpenAI / Related Digital / Oracle (Stargate Michigan) | Saline Township, MI | 1,000 | 2027 | DTE / METC | Announced Sep 2025 |
| OpenAI / Oracle / Vantage (Stargate Wisconsin) | Port Washington, WI | 1,300 by end-2027; 3,500 long-term | End-2027 | We Energies | Site work underway |
| OpenAI / SoftBank (Stargate Lordstown) | Lordstown, OH | up to 1,500 (with Milam) | 2026–2027 | AEP Ohio | Ground broken Sep 2025 |
| Microsoft (Fairwater Mount Pleasant) | Mount Pleasant, WI | ~3,300 (4-building build-out) | Late 2027 | We Energies | Phase 1 live; investment $7.3B |
| Microsoft (Fairwater Atlanta — East US 3) | Fulton / Douglas counties, GA | ~2,000 (multi-site) | Phase 1 by 2026; full by 2027 | Georgia Power | Under construction |
| Meta (Lebanon, Ohio) | Lebanon, OH (LEAP District) | 1,000 | Late 2027 / early 2028 | AEP Ohio | Construction Feb 2026 |
| AWS (Salem Township) | Luzerne County, PA | up to 960 (initial); expansion via grid-connected PPA up to 1,920 | Phased through 2028+ | Talen / Susquehanna nuclear (1.92 GW PPA via FERC-approved retail structure) | Operating; expansion subject to FERC outcome |
| AWS (Mississippi — Madison County) | Madison County, MS | Multi-GW (within $25B commitment) | 2027+ | Entergy Mississippi (Vicksburg + Traceview gas plants) | Construction underway |
| AWS (NC, Sherwood Smith complex) | North Carolina | 2,240 | Full by 2027–2028 | Duke Energy | Ground Oct 2025 |
| Hut 8 (Beacon Point) | Texas (AEP Texas) | 1,000 | Q1 2027 initial energization | AEP Texas — interconnection agreement signed | First 352 MW IT lease signed |
| CleanArc | Virginia | 900 | Initial 300 MW early 2027 | Dominion / PJM | Under development |
| Amazon / X-energy SMR fleet | Multiple US sites | 5,000+ (by 2039) | First units mid-2030s | X-energy Xe-100 SMRs | $500M Series C-1; KHNP/Doosan partnership 2026 |
| Google / Kairos Power SMRs | Multiple US sites | 500 (7 SMRs) | First unit 2030; complete by 2035 | Kairos KP-FHR | Agreement Oct 2024 |

Sources for project entries are listed in §5.

### Key observations on the announced pipeline

- **Phase delivery vs full COD**: most "gigawatt campuses" deliver in 100–300 MW phases over 3–5 years. The full nameplate is rarely energised before 2028.
- **Power source skew**: of the 18 listed, 9 are anchored by new gas-fired generation (overwhelmingly Entergy and Georgia Power footprints). Only the AWS-Talen Susquehanna deal and the SMR programmes are anchored on nuclear, and the SMR units do not arrive at scale until the early-to-mid 2030s.
- **Stargate alone** (Abilene + 5 new sites + Michigan + ongoing development) is on track to add about 7 GW by 2027 [Source: https://openai.com/index/five-new-stargate-sites/] — a single programme equal to roughly 6% of BloombergNEF's entire 2035 US data centre forecast.
- **The Susquehanna case** illustrates the regulatory friction: FERC rejected the original behind-the-meter co-location structure in November 2024, forcing a restructure to a grid-connected PPA with retail provision [Source: https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/]. FERC subsequently directed PJM to write new co-location rules in late 2025 [Source: https://www.ferc.gov/news-events/news/fact-sheet-ferc-directs-nations-largest-grid-operator-create-new-rules-embrace].

---

## 5. Sources

### Primary forecasts

- **LBNL (2024 United States Data Center Energy Usage Report)**, December 2024. Lead author Arman Shehabi. Key finding: 176 TWh in 2023 (4.4% of US electricity), 325–580 TWh by 2028 (6.7–12%). https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf and https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- **EPRI Powering Intelligence (2024)**, May 2024. Four scenarios with 3.7–15% CAGR; 9% of US electricity by 2030 base case. https://www.epri.com/about/media-resources/press-release/q5vu86fr8tkxatfx8ihf1u48vw4r1dzf
- **EPRI Powering Intelligence 2026 update**, February 2026. Revised range 380–790 TWh by 2030 (60% above 2024 numbers), 9–17% of US electricity by 2030, 10–20% by 2035, ~900 TWh by 2050 medium scenario. https://restservice.epri.com/publicattachment/97025 and https://powering-intelligence.epri.com/
- **IEA Energy and AI**, April 2025. Global 945 TWh by 2030 (up from 485 TWh in 2025); US increase ~240 TWh (130% rise from ~185 TWh 2024 baseline). https://www.iea.org/reports/energy-and-ai and https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf
- **EIA AEO 2025**, March 2025. Reference case: commercial computing 8% of commercial sector electricity in 2024 → 20% by 2050. https://www.eia.gov/todayinenergy/detail.php?id=65564
- **EIA AEO 2026**, April 2026. Reference case projects total US generation grows 25–50% through 2050; data centres dominant driver; high case 818 TWh of server consumption by 2050. https://www.eia.gov/pressroom/releases/press587.php and https://www.eia.gov/outlooks/aeo/pdf/AEO2026_Release_Presentation.pdf
- **EIA Press Release 13 Jan 2026**: strongest four-year electricity demand growth since 2000. https://www.eia.gov/pressroom/releases/press582.php
- **NERC 2025 Long-Term Reliability Assessment**, December 2025 / January 2026. Summer peak +224 GW over 10 years (vs +132 GW in LTRA 2024); winter +245 GW. https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf and infographic https://www.nerc.com/globalassets/our-work/assessments/ltra_infographic_2025.pdf
- **NERC 2024 LTRA (corrected July 2025)**. https://www.nerc.com/globalassets/our-work/assessments/2024-ltra_corrected_july_2025.pdf
- **Goldman Sachs Research**, September 2025 update (revised April 2026). Global 1,350 TWh by 2030 (220% increase); US ~750 TWh / 95 GW capacity. https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030 and https://www.goldmansachs.com/insights/goldman-sachs-research/data-center-power-demand-the-6-ps-driving-growth-and-constraints
- **Morgan Stanley**, 2025. 18% of US electricity by 2030, 20% by early 2030s; ~150 GW new global data centres by 2030. https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/data-center-electricity-consumption-michelle-weaver-david-arcaro
- **McKinsey & Company**, October 2024 / 2025 updates. US 25 GW (2024) → 80+ GW (2030); 606 TWh in 2030 (11.7% of US). https://www.mckinsey.com/industries/private-capital/our-insights/how-data-centers-and-the-energy-sector-can-sate-ais-hunger-for-power and https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/ai-power-expanding-data-center-capacity-to-meet-growing-demand
- **BloombergNEF**, December 2025. US 106 GW by 2035 (36% above April 2025 number); 8.6% of US electricity. Press summary at https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/ — primary BNEF report paywalled.
- **Grid Strategies National Load Growth Report**, December 2025. Aggregate US 2030 peak forecast +166 GW (vs +30 GW forecast in 2022); ~90 GW from data centres. https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf

### RTO and utility forecasts

- **PJM 2025 Long-Term Load Forecast Report**, January 2025. +32 GW peak 2024–2030 (94% data centres); 2035 RTO energy 1,328 TWh. https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf and summary https://insidelines.pjm.com/2025-long-term-load-forecast-report-predicts-significant-increase-in-electricity-demand/
- **ERCOT Long-Term Load Forecast Update 2025–2031**, April 2025. https://www.ercot.com/files/docs/2025/04/07/8.1-Long-Term-Load-Forecast-Update-2025-2031-and-Methodology-Changes.pdf
- **ERCOT 2025 Report on Existing and Potential Electric System Constraints and Needs**, December 2025. 226 GW large-load queue, ~75% data centres. https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf
- **MISO MTEP25 Report**, 2025. Peak load to 163 GW by 2035 (+35% vs 2025 baseline of 121 GW); 2.7% CAGR mid case. https://cdn.misoenergy.org/MTEP25%20Report731648.pdf
- **MISO Long-Term Resource Adequacy Update**, September 2025. https://cdn.misoenergy.org/06_2025-09-16_SPC_Open_Long%20Term%20Resource%20Adequacy%20%20Interconnection%20Queue%20Update_FINAL717559.pdf
- **Dominion Energy 2024 Virginia IRP**, December 2024. https://www.dominionenergy.com/-/media/content/about/our-company/irp/pdfs/2024-irp-w_o-appendices.pdf
- **Dominion Long-Range Projections**, October 2025. 47.2 GW DC contracted; +7 GW since Dec 2024 IRP; 9 GW DC peak by ~2034. https://virginiabusiness.com/dominion-data-center-power-demand-virginia-scc/
- **JLARC Virginia Data Center Study**, December 2024. https://jlarc.virginia.gov/pdfs/presentations/JLARC%20Virginia%20Data%20Center%20Study_FINAL_12-09-2024.pdf
- **Georgia Power 2025 IRP**, January 2025 (PSC approval July 2025). 8,500 MW load growth by 2030; 9,885 MW new resources approved. https://www.georgiapower.com/content/dam/georgia-power/pdfs/company-pdfs/2025-Integrated-Resource-Plan.pdf and PSC fact sheet https://psc.ga.gov/site/downloads/datacenterfactsheet.pdf
- **Entergy data centre announcements**, 2025. https://www.entergy.com/datacenters and https://www.utilitydive.com/news/gas-continues-to-dominate-entergy-plans-as-data-center-pipeline-grows/804521/

### Phantom load and queue dynamics

- "Load queue flooded by phantom data centers", Latitude Media, 2025. https://www.latitudemedia.com/news/phantom-data-centers-are-flooding-the-load-queue/
- "ERCOT's large load queue has nearly quadrupled in a single year", Latitude Media. https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/
- "ERCOT's large load queue jumped almost 300% last year", Utility Dive. https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/
- "A fraction of proposed data centers will get built", Utility Dive. https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/
- "The Puzzle of Low Data Center Utilization Rates" (PG&E metering analysis). https://www.powerpolicy.net/p/the-puzzle-of-low-data-center-utilization
- E3, "Forecasting Large Loads in the Age of AI and Data Centers", December 2025. https://www.ethree.com/wp-content/uploads/2025/12/E3Whitepaper_DataCenterForecasting.pdf

### Project announcements (Table 2 sources)

- **Meta Hyperion**: https://www.datacenterdynamics.com/en/news/meta-purchases-additional-1400-acres-for-hyperion-mega-data-center-expansion/ and https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/ and https://www.entergy.com/news/entergy-louisiana-announces-a-new-agreement-with-meta-that-will-deliver-an-additional-2b-in-customer-savings
- **AWS Project Rainier**: https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html and https://www.datacenterfrontier.com/hyperscale/article/55295967/amazon-doubles-down-on-ai-infrastructure-with-30b-in-new-us-data-center-investments
- **AWS Mississippi**: https://www.datacenterdynamics.com/en/news/aws-scales-up-investment-commitment-for-mississippi-data-centers-to-25bn/
- **AWS Salem Township PA / Talen Susquehanna**: https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/ and https://www.datacenterdynamics.com/en/news/aws-talen-sign-ppa-for-192gw-of-power-from-pennsylvania-nuclear-plant/
- **FERC Susquehanna ruling**: https://www.utilitydive.com/news/ferc-interconnection-isa-talen-amazon-data-center-susquehanna-exelon/731841/ and https://www.ans.org/news/2025-04-16/article-6937/
- **FERC PJM colocation order Dec 2025**: https://www.ferc.gov/news-events/news/fact-sheet-ferc-directs-nations-largest-grid-operator-create-new-rules-embrace and https://www.bakerbotts.com/thought-leadership/publications/2025/december/ferc-issues-order-providing-guidance-for-co-locating-power-plants-with-data-centers-within-pjm
- **Stargate / OpenAI five new sites**: https://openai.com/index/five-new-stargate-sites/ and https://group.softbank/en/news/press/20250924 and https://www.datacenterfrontier.com/machine-learning/article/55319132/scaling-stargate-openais-five-new-us-data-centers-push-toward-10-gw-ai-infrastructure
- **Stargate Abilene operational**: https://www.datacenterdynamics.com/en/news/crusoes-abilene-data-center-officially-live-serving-oracle-and-openais-stargate/ and https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
- **Stargate Michigan**: https://www.datacenterdynamics.com/en/news/related-digitals-michigan-1gw-data-center-project-to-serve-openai-oracle/
- **Stargate Wisconsin (Port Washington)**: https://www.datacenterdynamics.com/en/news/openai-announces-five-more-us-stargate-data-centers-with-oracle-and-softbank/
- **Microsoft Fairwater Mount Pleasant**: https://local.microsoft.com/blog/mount-pleasant-datacenter-project-update/ and https://www.datacenterdynamics.com/en/news/microsoft-ceo-says-fairwater-data-center-site-is-going-live-ahead-of-schedule/ and https://epoch.ai/data-insights/fairwater-power-usage
- **Microsoft Atlanta (East US 3)**: https://www.datacenterdynamics.com/en/news/microsoft-to-launch-new-cloud-region-in-atlanta-georgia-in-2027/ and https://www.datacenterfrontier.com/hyperscale/article/55126626/details-emerge-on-microsofts-18-billion-investment-in-atlanta-data-centers-amid-tax-development-wrangles
- **Meta Lebanon, Ohio**: https://www.blackridgeresearch.com/blog/upcoming-largest-data-center-projects-in-united-states-usa
- **Hut 8 Beacon Point**: https://www.prnewswire.com/news-releases/hut-8-commercializes-first-phase-of-1-gw-beacon-point-ai-data-center-campus-with-15-year-352-mw-it-lease-with-base-term-contract-value-of-9-8-billion-302763484.html
- **Amazon-X-energy SMR**: https://www.datacenterdynamics.com/en/news/amazon-x-energy-partner-with-south-korean-consortium-to-advance-smr-development-across-us/ and https://www.theregister.com/2025/11/24/x_energy_700m_smr/
- **Google-Kairos SMR**: https://www.datacenterfrontier.com/energy/article/55235902/google-and-amazon-make-major-inroads-with-smrs-to-bring-nuclear-energy-to-data-centers and https://spectrum.ieee.org/nuclear-powered-data-center

---

## 6. Methodology and definitional notes

**Geographic scope**: figures are US-only unless explicitly noted as "global". Goldman Sachs and IEA publish global numbers and a US share; the US share is reported here.

**Energy vs power**: TWh is annual energy consumption from the meter. GW is instantaneous power draw. Converting between them requires a load factor (annual average / peak). Hyperscale data centres typically run at 60–75% load factor; AI training clusters can reach 80%+ when continuously loaded.

**Nameplate vs metered**: announcement press releases give nameplate / contracted capacity. Actual peak draw is typically 60–75% of nameplate (PG&E evidence). Forecasters that aggregate announced campuses without applying a discount over-state the grid impact.

**Phantom load adjustment**: there is no industry-standard discount factor. Texas's 1.8% operational ratio is an extreme. A more defensible adjustment for forward forecasting is to take 30–50% of utility-stated demand as duplicative or speculative, based on the 5–10x ratio of requests to actual builds.

**What's not in this note**: residential AI inference at the edge, crypto mining (which the EIA tracks separately and which has been absorbed by AI compute capacity in some cases), and demand response / load flexibility programmes that could shave coincident peak. Industrial decarbonisation electrification (EVs, heat pumps, electrolyser hydrogen) is the other major source of US load growth — Grid Strategies attributes ~45% of its 166 GW number to non-data-centre sources.

**What I would not extrapolate**: most sources do not publish 2035 numbers explicitly. EPRI's medium 900 TWh by 2050 and BloombergNEF's 106 GW by 2035 are the only direct mid-2030s primary numbers I located. Anything else for 2035 is either implied or back-cast.
