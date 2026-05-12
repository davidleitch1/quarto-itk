---
title: "US data centres: operating fleet, construction pipeline and power sources"
author: "David Leitch"
date: 2026-05-10
format: html
draft: false
category: "datacentres"
lightbox: true
---

# US data centres: operating fleet, construction pipeline and power sources

This note compiles the best public estimates as of May 2026 of (a) the size of the operating US data centre fleet, (b) what is physically under construction, (c) the largest individual sites in each category, and (d) where the power is coming from. The compilation draws on three parallel research drafts that are kept under `background/_research_drafts/` for traceability.

A consistent theme runs through all of it: every public number for "data centre capacity" depends entirely on what is being counted. Number-of-facilities estimates differ by a factor of 10. "Megawatts under construction" differ by a factor of 4 between the major brokers. "Operating IT load" for the same hyperscaler campus can differ by 40% between trade-press lists. The note is therefore explicit about definitions and source quality.

---

## 1. Headline numbers

**Table 1: US data centre headline numbers, May 2026**

| Metric | Estimate | Definition / source basis |
|:--------|--------:|:--------------------------|
| All US data centre facilities (broad count) | 4,700–5,400 | Cloudscene and Baxtel directories, 2025–early 2026 |
| US hyperscale-owned facilities | 580 | Synergy Research, end-2025 (~55% of global hyperscale capacity) |
| Operating IT load — entire US fleet | ~50 GW | FERC 2025 State of the Markets, year-end 2025 |
| Operating IT load — colocation in 8 primary metros | 9.4 GW | CBRE H2 2025, year-end 2025 |
| Northern Virginia operating colocation | 4.0 GW | CBRE H2 2025 (37% YoY growth) |
| 2023 baseline electricity consumption | 176 TWh (4.4% of US) | LBNL 2024 Data Center Energy Usage Report |
| Under physical construction, May 2026 | 22–26 GW IT load | Reconciled across CBRE, JLL, Cushman & Wakefield, datacenterHawk |
| Sites of 1 GW+ under construction | At least 10 | JLL 2026 Global Data Center Outlook |
| Pre-committed share of pipeline | ~89–92% | C&W and JLL |
| 2030 demand forecast — defensible range | 500–700 TWh (12–17% of US) | Author's reconciliation across LBNL, EPRI, IEA, Goldman, McKinsey |

*Source: ITK compilation. See sections below for full citations and the caveats that apply to each line.*

The single most defensible "size of the US fleet" number is the FERC 2025 figure of around 50 GW of operating IT load at year-end 2025, derived from interconnection data and quoted in FERC's State of the Markets report released March 2026 [@ferc-som-2025-summary]. The same report notes that the average new facility entering service in 2025 was about 80 MW, three times the 25 MW average of 2020.

---

## 2. Counting operating facilities — three different definitions

The number of US data centres varies by an order of magnitude depending on what is counted:

- **Broad facility count: 4,720 to 5,427.** The Cloudscene database (via Cargoson, November 2025) lists 5,427 US facilities including small enterprise sites; Baxtel's directory at May 2026 lists about 4,720 [@cargoson-cloudscene-2025; @baxtel-us-2026]. Both directories are continuously updated and use different inclusion thresholds; both probably undercount very small enterprise server rooms and overcount facilities that are partially decommissioned.
- **Hyperscale-owned subset: 580.** Synergy Research counts 580 hyperscale-owned facilities in the US at end-2025, against 504 a year earlier. The US holds about 55% of global hyperscale capacity [@synergy-hyperscale-2025].
- **Operating IT load: about 50 GW.** This is the most authoritative single number for what actually draws power. It comes from FERC's 2025 State of the Markets report, summarised by Utility Dive in March 2026 [@ferc-som-2025-summary]. The FERC figure is grounded in transmission interconnection data and is consistent with the lower bound of the LBNL 2024 back-derivation from 176 TWh of 2023 electricity use [@lbnl-2024-dc-report].

Brokers report a different and much smaller number. CBRE's H2 2025 report (published 25 February 2026) puts wholesale colocation operating inventory in the eight North American primary markets at 9,432 MW [@cbre-h2-2025]. That is one of the most-cited "data centre" numbers in the press, but it is roughly 19% of the FERC total because CBRE excludes hyperscaler-owned, behind-the-fence facilities and all secondary markets.

The takeaway is that adding "Synergy hyperscale count" plus "CBRE colocation MW" plus "Baxtel facility count" produces double-counting and does not approximate the FERC 50 GW number. For most published purposes the cleanest framing is:

- *Number of facilities (any size):* about 5,000
- *Operating IT load:* about 50 GW, of which roughly 9.4 GW is multi-tenant colocation in the eight primary metros and the balance is hyperscaler-owned plus colocation in secondary markets.

---

## 3. Largest operating US data centre campuses

There is no authoritative published list of the largest operating US campuses by IT load, because the largest operators (Meta, Google, AWS, Microsoft) do not publish per-site IT load. The ranking below is the best public reconstruction; values flagged with the dagger symbol (†) are external estimates aggregated from utility filings, building permits, satellite imagery and trade-press analysis. They should be treated as upper-bound or planning-envelope numbers rather than energised IT load.

The **Ownership class** column (used in Tables 2 and 5) follows industry convention: *hyperscale self-build* means the cloud/AI giant owns and operates the facility for its own use; *wholesale build-to-suit* means a developer (Vantage, Crusoe, STACK, Related Digital, etc.) builds for a named anchor tenant; *wholesale colocation* means multi-tenant leases at whole-floor or whole-building scale; *retail colocation* means many smaller tenants sharing a facility. The **Primary workload** column distinguishes AI training (sustained high utilisation, single-purpose) from mixed cloud (the historic hyperscaler default of web, storage and inference) and mixed cloud/enterprise (typical colocation). Uptime Institute tier ratings are not shown because they are not disclosed for most hyperscaler self-builds and would require fabrication for the others.

**Table 2: Largest US data centre campuses with at least one operational phase, early 2026**

| # | Campus | Operator | Location | Ownership class | Primary workload | Estimated operating IT load (MW) | Power source | First online | Notes |
|--:|:--|:--|:--|:--|:--|--:|:--|:--|:--|
| 1 | Altoona | Meta | Altoona, IA | Hyperscale self-build | Cloud + AI (mixed) | up to ~1,400† (master-plan envelope) | MidAmerican Energy + Meta wind/solar PPAs (renewable matched) | 2014 | 10-building, ~5 M sqft campus; original 2014 building was ~60 MW |
| 2 | Prineville | Meta | Prineville, OR | Hyperscale self-build | Cloud + AI (mixed) | up to ~1,290† (master-plan envelope) | PacifiCorp + 977 MW Meta-funded renewables; renewable matched | 2011 | ~4.6 M sqft, $2B+ invested per Meta info sheet |
| 3 | AWS US-East-1 (Loudoun cluster) | AWS | Ashburn / Loudoun, VA | Hyperscale self-build | Cloud (mixed; AI growing) | ~1,500† (aggregate across dozens of buildings, not a single campus) | Dominion Energy + AWS solar/wind PPAs | 2006 onward | Largest single Dominion building reported at ~60 MW |
| 4 | Fort Worth | Meta | Fort Worth, TX | Hyperscale self-build | Cloud + AI (mixed) | up to ~730† | Oncor / ERCOT; renewable matched via Meta PPAs | 2017 | |
| 5 | Microsoft Quincy (MWH cluster) | Microsoft | Quincy, WA | Hyperscale self-build | Cloud + AI (mixed) | ~622† (gens 2–4; gen 5 in build) | Bonneville / Grant PUD via Grand Coulee hydro | 2007 | Continuous build-out; further expansion permitted Jan 2026 |
| 6 | Council Bluffs | Google | Council Bluffs, IA | Hyperscale self-build | Cloud + AI (mixed) | ~600+† (Google's largest worldwide; figure not published) | MidAmerican + Google wind PPAs | 2009 | |
| 7 | Switch Core Campus | Switch | Las Vegas, NV | Wholesale colocation | Mixed cloud / enterprise | ~495 | NV Energy; renewable PPAs | 2008, phased | |
| 8 | xAI Colossus 1 + 2 | xAI | Memphis TN + Southaven MS | Hyperscale self-build | AI training (single tenant) | ~750 (Colossus 1 + 2 combined; estimates vary) | TVA + MLGW grid + ~18 on-site Solar Turbines/Mitsubishi gas turbines (~495 MW); 41 more permitted in MS | Sept 2024 | Subject of Earthjustice/SELC litigation over unpermitted air emissions |
| 9 | Stargate Abilene (Lancium Clean Campus) | Crusoe / Oracle / OpenAI | Abilene, TX | Wholesale build-to-suit (Crusoe / Oracle for OpenAI) | AI training | ~600 operating (4 of 8 buildings live); 1,200 at full build mid-2026 | On-site natural gas + ERCOT (Oncor) + local wind; some on-site solar/storage | First building 2025 | March 2026: planned 600 MW expansion cancelled |
| 10 | AWS Cumulus / Susquehanna | AWS (acquired from Talen 2024) | Salem Township, PA | Hyperscale self-build (acquired) | AI training (Anthropic anchor) | ~300 operating; 960 MW PPA with eventual scale to 1,920 MW by 2032 | Susquehanna nuclear plant (PPA, restructured to grid-delivered after FERC ruling) | Acquired 2024; ramp 2024–2032 | |
| 11 | Pryor (Mayes County) | Google | Pryor, OK | Hyperscale self-build | Cloud + AI (mixed) | not published | OG&E + Google solar PPAs (Mayes County 372 MW solar adjacent) | 2011 | 600 MW of new clean energy PPAs signed 2025 |
| 12 | QTS Atlanta-Metro | QTS / Blackstone | Atlanta, GA | Wholesale colocation | Mixed cloud | ~278 | Georgia Power on-site substation | 2007 (former Sears facility) | |
| 13 | New Albany / Columbus cluster (multi-operator) | Meta + AWS + Google | New Albany, OH | Hyperscale self-build (multiple operators) | Cloud + AI (mixed) | 500+ across multiple operators (composite) | AEP Ohio | 2017 onward | AEP Ohio 5 GW contracted by 2030 |
| 14 | Lakeside Technology Center | Digital Realty | Chicago, IL | Retail/wholesale colocation (carrier hotel) | Mixed; interconnection-heavy | 100+ | ComEd | 1999 | ~1.1 M sqft; iconic colocation hub |
| 15 | Switch Citadel — Tahoe Reno 1 | Switch | Tahoe Reno, NV | Wholesale colocation | Mixed cloud / enterprise | ~130 operating (campus master-planned to 650 MW) | NV Energy + 179 MW behind-the-meter solar | 2017 | Listed for context; operating load is far below master plan |

*Source: ITK compilation drawing on operator press releases, Meta's Prineville Data Center info sheet (Feb 2025), Baxtel, Data Center Frontier, Data Center Dynamics, BlackRidge Research, Epoch AI's Stargate tracker (April 2026), and SemiAnalysis. Values flagged † are external estimates because the operator does not publish per-site IT load.*

### What the dagger figures actually mean

The Meta Altoona "1,400 MW" and Prineville "1,289 MW" numbers circulate widely in trade-press lists. Meta's own Prineville info sheet (February 2025) discloses dollar investment, headcount and 977 MW of *renewable supply added to PacifiCorp's grid*, but it does not state site IT load. The 1,400 / 1,289 MW figures appear to be aggregated from multi-decade building permits and represent a *master-plan envelope*, not currently energised IT load. The original 2014 Altoona building was reported at 60 MW; the campus has since grown to 10 buildings and ~5 M sqft, and at typical hyperscaler densities of 250–350 W per square foot of white space, an upper bound is plausibly in the high hundreds of MW rather than 1.4 GW. Without primary verification from utility interconnection filings or Meta's own data, the IT-load figures should be treated as upper bounds.

By contrast, Stargate Abilene, Susquehanna/Cumulus and xAI Colossus have IT loads that are more reliably bounded — Abilene by Crusoe's own building-by-building reporting, Susquehanna by the FERC-disclosed PPA structure, and Colossus by the gas-turbine permits Earthjustice and SELC have litigated over.

---

## 4. Geographic concentration

Northern Virginia remains by far the single largest cluster. CBRE's H2 2025 report (year-end 2025 data) puts Northern Virginia colocation operating inventory at 4,039.6 MW, which is about 43% of the 9.4 GW US primary-market colocation total [@cbre-h2-2025]. Hyperscaler-owned, behind-the-fence facilities are not in that number; including them, Loudoun County alone is reported at 5,300–6,000 MW [@wtop-loudoun-2025]. Northern Virginia is therefore roughly 8–12% of the 50 GW national operating IT load.

**Table 3: US/North America primary data centre markets — colocation operating inventory, year-end 2025**

| Market | Operating IT load (MW) | Vacancy | YoY growth | Notes |
|:--|--:|--:|--:|:--|
| Northern Virginia | 4,039.6 | 0.5% | +37% | World's largest cluster; +1,102 MW absorption in 2025 |
| Atlanta | 1,459.2 | 2.0% | +46% | Now #2; +458.8 MW YoY |
| Dallas–Fort Worth | ~1,500 | low | n/a | Crossed 1 GW in 2025 |
| Phoenix | ~603 | 1.7% | +67% (2024 base) | Strong further 2025 growth |
| Chicago | ~1,000 (inferred) | 3.1% | modest | Vacancy ticked up |
| Silicon Valley | ~500 (inferred) | low | low | Power constrained; rents +19% |
| Hillsboro / Portland | ~430 | low | rising | NTT 354 MW alone; QTS 180 MW |
| New York Tri-State | ~300 (inferred) | low | low | Power constrained |
| **Primary markets total** | **9,432** | **1.4%** | **+36%** | CBRE H2 2025 |

*Source: CBRE North America Data Center Trends H2 2025 [@cbre-h2-2025]; market-level figures for Phoenix and Hillsboro from CBRE H1 2025 market profiles. Inferred values are residuals after subtracting itemised markets.*

Notable secondary clusters include central Ohio (AEP Ohio reports about 5 GW of contracted hyperscaler load by 2030 across Meta, AWS, Google and QTS [@dcf-ohio]), Iowa (Google + Meta + Microsoft cluster of about 3 GW combined), the Pacific Northwest (5,488 MW reported by Baxtel across Quincy WA, Hillsboro OR and The Dalles OR), and Memphis (created effectively by xAI in 2024).

---

## 5. Construction pipeline — what is actually being built

The most-quoted "under construction" figure in the trade press is roughly 25 GW, used by Cushman & Wakefield, datacenterHawk and broadly consistent with JLL. The CBRE figure for the same date is 5,994 MW, a factor of four lower. The two are not contradictory — they describe different universes:

- **CBRE 5,994 MW (year-end 2025):** wholesale colocation under construction in the eight primary metros only [@cbre-h2-2025].
- **C&W and datacenterHawk 25.3 GW (H2 2025):** all asset types across primary, secondary and tertiary North American markets, including hyperscaler-owned and behind-the-meter "AI factories" [@cw-h2-2025; @hawk-3q25].
- **JLL 35 GW US construction pipeline (January 2026):** broader still, including projects starting within 24 months as well as active site work [@jll-2026-outlook].

**Table 4: Reconciling the construction pipeline trackers**

| Source | Headline figure | Geography | Date | Definition |
|:--|--:|:--|:--|:--|
| Cushman & Wakefield H2 2025 | 25.3 GW under construction; 89% pre-committed | Americas | Feb 2026 | All asset types; Virginia 6.3 GW; West Texas 2.9 GW |
| datacenterHawk Q1 2026 | 25.3 GW under construction; 89% pre-leased | North America | Q1 2026 | Methodology aligns with C&W |
| JLL 2026 Global Outlook | 35 GW pipeline; 92% pre-committed; >10 sites at 1 GW+ | US | Jan 2026 | Includes near-term starts plus active construction |
| CBRE H2 2025 | 5,994 MW under construction | NA primary markets | Feb 2026 | Wholesale colocation only, 8 metros |
| Newmark 2025 Outlook | $31.5 bn annualised data centre construction spend | US | Feb 2025 | Capex basis, not MW |

*Source: ITK compilation from each tracker's H2 2025 report or equivalent. Brokers' detailed datasets are subscription products; figures here are from publicly issued summary releases and trade-press citations.*

A defensible working number for IT/critical load physically under construction in May 2026 is **22–26 GW**, with at least 10 individual sites at 1 GW or larger and around 89–92% pre-committed (preleased or owner-occupied). This is a supply pipeline aimed at known customers, not speculative inventory.

---

## 6. Largest individual projects under construction

The table below catalogues the largest US data centre projects with verifiable physical construction underway in May 2026. "Under construction MW" refers to first-phase IT/critical load with steel, foundations or shell in progress; full campus build-out is in the notes column where larger.

**Table 5: Top US data centre projects under physical construction, May 2026**

| Project / campus | Owner / anchor | Location (utility / ISO) | Ownership class | Primary workload | Under-construction MW | Full campus envelope | Power source | First power | Source notes |
|:--|:--|:--|:--|:--|--:|--:|:--|:--|:--|
| Hyperion | Meta (own use) | Richland Parish, LA (Entergy / MISO South) | Hyperscale self-build | AI training | 2,000 (Phase 1) | 5,000 ultimate | 3 new Entergy combined-cycle gas plants ~2.3 GW + 240-mile 500 kV line; Meta-funded renewables; LOI for nuclear | Partial energisation 2027; full Phase 1 2028 | [@dcd-entergy-meta; @meta-richland; @enr-meta-louisiana] |
| Project Rainier | AWS (anchor: Anthropic) | New Carlisle, IN (AEP I&M / MISO) | Hyperscale self-build (Anthropic anchor) | AI training | 2,200+ campus; 7 of 30 buildings live (~500 MW operational) | 2,200+ | AEP grid; AWS PPAs include Susquehanna nuclear, wind, solar | Operational since Oct 2025; balance through 2026–27 | [@cnbc-rainier; @converge-rainier] |
| Frontier | Vantage Data Centers / Oracle / OpenAI (Stargate) | Shackelford County, TX (Oncor / ERCOT) | Wholesale build-to-suit (Vantage / Oracle for OpenAI) | AI training | 1,400 (10 buildings, 3.7 M sqft) | 1,400 | 700 MW behind-the-meter Voltagrid natural-gas microgrid (off-grid initially) | First building H2 2026 | [@dcd-vantage-frontier; @co-oracle-offgrid] |
| Stargate Doña Ana ("Project Jupiter") | STACK Infrastructure / BorderPlex / Oracle / OpenAI | Doña Ana County, NM (El Paso Electric / WECC) | Wholesale build-to-suit (STACK / Oracle for OpenAI) | AI training | 2,200 (4 buildings Phase 1) | 2,200 | Bloom Energy solid-oxide fuel-cell microgrid (April 2026 redesign replacing original gas turbines) | Late 2026 first energisation | [@dcd-stack-jupiter; @sourcenm-jupiter] |
| Stargate Saline Township | Related Digital / Oracle / OpenAI | Saline Township, MI (DTE / MISO) | Wholesale build-to-suit (Related / Oracle for OpenAI) | AI training | 1,400 (3 buildings) | 1,400 | DTE grid + battery storage | First power 2027–28 | [@related-stargate-mi; @epoch-stargate-2026] |
| Stargate Port Washington | Vantage Data Centers / Oracle / OpenAI | Port Washington, WI (We Energies / MISO) | Wholesale build-to-suit (Vantage / Oracle for OpenAI) | AI training | 1,300 | 1,300 (Wisconsin scaling envisaged to 3,500 long-term) | We Energies grid + ~70% solar/wind/battery PPAs | First power 2027 | [@dcf-vantage-wi; @epoch-stargate-2026] |
| Stargate Milam County | SB Energy / SoftBank / Oracle / OpenAI | Milam County, TX (Oncor / ERCOT) | Wholesale build-to-suit (SB Energy / Oracle for OpenAI) | AI training | 1,200 | 1,200 | On-site generation (type undisclosed) + ERCOT grid | First building Oct 2026 | [@epoch-stargate-2026; @dcd-five-stargate] |
| Stargate Abilene (Lancium) | Crusoe / Oracle / OpenAI | Abilene, TX (Oncor / ERCOT) | Wholesale build-to-suit (Crusoe / Oracle for OpenAI) | AI training | 600 (4 of 8 buildings live; 4 finishing) | 1,200 (capped after March 2026 expansion cancellation) | On-site natural gas + ERCOT + local wind | Balance mid-2026 | [@dcd-crusoe-tops-out; @cnbc-stargate-tx] |
| Microsoft Mt Pleasant (Fairwater) | Microsoft (own use) | Mt Pleasant, WI (We Energies / MISO) | Hyperscale self-build | AI training | First Fairwater building (~1 GW) live; 15 more buildings approved Jan 2026 | ~3,300 MW projected 4-building Fairwater build by late 2027; broader campus larger | We Energies grid (incl. unused Foxconn legacy capacity) + Microsoft renewable PPAs | First Fairwater building late 2025; phase 2 ground 2026 | [@cnbc-mtpleasant; @epoch-fairwater] |
| Cumulus / Susquehanna | AWS (acquired from Talen 2024) | Salem Township, PA (PPL / PJM) | Hyperscale self-build (acquired) | AI training (Anthropic anchor) | 960 | 1,920 by 2032 | Susquehanna nuclear (PPA, transitioning to front-of-meter Spring 2026 after FERC restructure) | Scaling | [@ud-talen-amazon; @talen-ir-2025] |
| Colossus 1 + 2 | xAI (own use) | South Memphis TN + Southaven MS (TVA / MLGW + on-site) | Hyperscale self-build | AI training (single tenant) | ~750 operating; permit for 1,200 self-gen approved | scaling | 18+ on-site Solar Turbines / Mitsubishi gas turbines (~495 MW); 41 more permitted in MS; 168 MWh Megapack BESS planned; some TVA grid | Colossus 1 live; Colossus 2 online late 2025 / Jan 2026 | [@semianalysis-colossus2; @dcd-xai-41-turbines; @selc-xai] |
| Meta El Paso ("Project Ranger") | Meta (own use) | El Paso, TX (El Paso Electric / WECC, *not* ERCOT) | Hyperscale self-build | AI training | 1,000 (12 buildings, ~1.2 M sqft) | 1,000+ | 813 modular gas-fired generators (~366 MW) on-site; El Paso Electric grid; matching renewables | Phase 1 by 2028 | [@meta-el-paso; @cnbc-meta-elpaso; @ttribune-elpaso] |
| Microsoft Palmetto / Atlanta cluster | Microsoft (own use) | Palmetto, Douglasville, East Point, GA (Georgia Power / SERC) | Hyperscale self-build | Cloud + AI (mixed) | $1.8 bn invested across multiple sub-campuses; MW not disclosed | ~2,000+ multi-site | Georgia Power (heavy gas + Vogtle nuclear); Microsoft renewable PPAs | Active construction since Apr 2024; finishes 2028 | [@dcf-ms-atlanta; @ms-local-palmetto] |
| Microsoft Quincy expansion | Microsoft (own use) | Quincy, Malaga, East Wenatchee, WA (Grant PUD / Chelan PUD) | Hyperscale self-build | Cloud + AI (mixed) | 622 MW existing; further expansion permitted Jan 2026 | continuous | Grand Coulee hydro via Grant PUD; closed-loop cooling | Continuous | [@opb-quincy; @dcd-quincy] |
| Crane Clean Energy Center (TMI Unit 1) | Constellation; Microsoft 20-yr PPA | Londonderry Township, PA (PJM / PPL) | Power asset (not data centre); offtake to Microsoft | n/a — power supply | 835 MW reactor restart works | 835 MW (entirely PPA-dedicated to Microsoft) | Restarted nuclear | Restart targeted 2027 | [@constellation-crane; @wnn-crane] |
| Duane Arnold restart | NextEra; Google 25-yr PPA | Palo, IA (MISO / Alliant) | Power asset (not data centre); offtake to Google | n/a — power supply | 600 MW reactor restart (engineering / licensing) | 600 MW | Restarted nuclear | Q1 2029 | [@ans-duane-arnold; @ipr-duanearnold] |
| Palisades restart | Holtec | Covert Township, MI (MISO / Consumers) | Power asset (not data centre); offtake unsigned | n/a — power supply | 800 MW PWR restart (refurbishment underway) | 800 MW + twin SMR-300 by early 2030s | Restarted nuclear; SMR phase under licensing | Q1/Q2 2026 (slipped from late 2025) | [@powermag-palisades; @neutronbytes-smr300] |
| Equinix Loudoun expansion (LD-15 class) | Equinix (colocation) | Ashburn, VA (Dominion / PJM) | Retail/wholesale colocation (interconnection) | Mixed cloud / interconnection | 1.1 M sqft, 6 new buildings filed late 2025 | scaling | Dominion grid | Permitting / early site works | [@vabusiness-equinix] |
| EdgeConneX New Albany OH | EdgeConneX (hyperscaler tenant) | New Albany, OH (AEP Ohio / PJM) | Wholesale build-to-suit (single hyperscaler tenant) | Cloud + AI (likely) | 700,000 sqft (likely 100–250 MW) | scaling | AEP Ohio grid | Construction Q4 2025; live Q1 2026 | [@dcd-edgeconnex] |

*Source: ITK compilation. "Under-construction MW" is what is currently under construction, not the full multi-decade campus envelope. Several projects sit on land approved for far larger build-outs that should not be conflated with what is being built today.*

### Projects flagged but not yet verifiably under physical construction

The following high-profile announcements have site approvals or financial commitments but limited evidence of vertical construction as of May 2026:

- **Crusoe Project Jade (Cheyenne, Wyoming)** — county approval and a 2.7 GW dedicated gas plant approved January 2026; first buildings expected 2027 [@powermag-jade].
- **Sailfish Comanche Circle (Hood County, TX)** — 5 GW master-planned; first 600 MW behind-the-meter envisaged in 24 months [@dcd-sailfish].
- **Anthropic / Fluidstack sites (Mitchell County TX, Niagara County NY, southeast LA, Haskell County TX)** — announced November 2025; rolling commissioning through 2026 with only some sites confirmed under construction [@anthropic-50bn; @cnbc-anthropic-dc].
- **Stargate Lordstown OH** — SoftBank claims groundbreaking but Epoch AI's April 2026 tracker reports land clearance only, not data centre construction; the site is primarily a server-manufacturing facility, with less than 0.3 GW of data centre capacity envisaged [@epoch-stargate-2026].
- **QTS PW Digital Gateway (Prince William County, VA)** — rezoning voided by Circuit Court Aug 2025; upheld by VA Court of Appeals 31 Mar 2026; Compass dropped its appeal; Prince William County Board voted unanimously 15 Apr 2026 to withdraw from defending the rezoning; QTS filed a Virginia Supreme Court appeal 30 Apr 2026 — project effectively dead [@bisnow-qts-appeal; @wtop-pwc-withdraws].
- **Meta–Oklo Pike County OH (1.2 GW SMR campus)** — first reactors not expected until 2030 [@carboncredits-meta-nuclear].

---

## 7. Power source trends

The most striking shift in 2024–2026 has been towards **dedicated firm generation** rather than incremental utility-grid expansion. Bloom Energy's 2025 report frames an aggregate 35 GW "energy gap" by 2030 between data centre demand growth and utility-grid delivery [@bloom-2025].

### Who pays for the power: financing the 17 GW under construction

Aggregating the project-by-project supply arrangements in §5, the ~17 GW of physical IT load currently under construction across the named US mega-campuses splits four ways by who pays for and who absorbs cost risk on the generation:

**Table 7: 17 GW US data centre pipeline by power-supply financing model, May 2026**

| Bucket | What it means | Projects | MW | Share |
|:--|:--|:--|--:|--:|
| **On-site / behind-the-meter** | Data centre operator builds and finances generation on the same site; full cost falls on the operator | Vantage Frontier (Voltagrid 1,400); Stargate Doña Ana / Project Jupiter (Bloom fuel cells 2,200); Stargate Milam County (1,200, on-site type undisclosed); Stargate Abilene (Crusoe BTM 360 of 600); xAI Colossus (~500 of 750); Meta El Paso (Enchanted Rock 366 of 1,000) | ~6,000 | **36%** |
| **Utility-built but contractually allocated** | Regulated utility builds new generation specifically to serve one customer; cost recovered through utility rate base, with stranded-cost risk shared with other ratepayers if the customer walks | Hyperion (Entergy 2.3 GW dedicated CCGTs + 240-mile 500 kV line; Meta contracted 15–20 yr against ~30 yr asset life — Commissioner Lewis dissented on stranded-cost risk) | ~2,000 | **12%** |
| **Bilateral private PPA** | Existing or restarted generation contractually locked to one customer through an arms-length PPA, not via the regulated utility tariff | Cumulus / Susquehanna (AWS–Talen 960 MW PPA today, scaling to 1,920 MW by 2032 — restructured to grid-delivered after FERC rejected behind-the-meter co-location in November 2024) | ~960 | **6%** |
| **Generic utility grid** | Standard interconnection drawing from the host utility's pool of generation, shared with all other customers; new generation and transmission built to serve the load is recovered through general rate base unless rate cases create separate large-load classes | Project Rainier (AEP I&M, 2,200); Stargate Saline Twp (DTE, 1,400); Stargate Port Washington (We Energies, 1,300); Microsoft Mt Pleasant (We Energies, 1,000); Microsoft Quincy (Grant PUD hydro, 622); Stargate Abilene grid balance (240); Colossus TVA (250); Meta El Paso grid balance (634); EdgeConneX New Albany (AEP Ohio, 175) | ~7,800 | **47%** |
| **Total** | | | **~16,800** | 100% |

*Source: ITK calculation from §5 of this note. Where two sources are documented for one site (Stargate Abilene, xAI Colossus, Meta El Paso), MW are split between on-site and grid components per the disclosed mix. The "generic utility grid" share assumes the new large loads are taken into the host utility's standard rate base unless a separate large-load tariff is in force; the Wisconsin PSC's May 2026 ruling that We Energies and Alliant must allocate full cost of new generation to data centres would, once implemented, shift Mt Pleasant, Port Washington and Beaver Dam from socialised to dedicated cost recovery for any new build attributable to those loads.*

The combined share where data centres "provide their own power or have power dedicated to them" — buckets 1, 2 and 3 — is **53%**. The share drawing from a generic utility grid where costs are at least partly socialised to other customers is **47%**.

This is the structural anatomy of the rate-impact backlash documented in `data_centres_community.md`. Nearly half the under-construction capacity sits on shared utility grids in PJM (Project Rainier in AEP I&M zone) and MISO (Saline, Port Washington, Mt Pleasant on DTE and We Energies, plus Hyperion's MISO South footprint). It is precisely those grids where the Virginia SCC's new GS-5 large-load class, AEP Ohio's 85% minimum-take tariff, the PPL Pennsylvania settlement, and the Wisconsin PSC's May 2026 ruling are now moving cost recovery from the "generic grid" bucket toward the "dedicated" bucket — typically through minimum-bill provisions and stranded-cost protection rather than full physical separation.

The "utility-built but contractually allocated" bucket (Hyperion is the leading example) is the most legally and politically contested middle ground. The generation is dedicated in operational fact but the cost flows through the regulated utility's rate base, which is why Louisiana PSC Commissioner Davante Lewis's dissents on the Meta CCGT approvals have framed the stranded-cost risk in residential-customer-protection terms.

### Behind-the-meter natural gas

The fastest-growing supply category. Examples in the construction pipeline include:

- **Vantage Frontier (Shackelford TX):** 700 MW Voltagrid natural-gas microgrid, off-grid initially.
- **xAI Colossus 1 + 2 (Memphis / Southaven):** 18+ on-site Solar Turbines / Mitsubishi gas turbines (~495 MW) operational; 41 more permitted in Mississippi. The Memphis turbines have drawn Earthjustice and SELC litigation over unpermitted air emissions.
- **Meta El Paso:** 813 modular gas gensets totalling 366 MW on-site.
- **Crusoe Abilene:** hybrid on-site gas + Oncor grid + local wind.
- **Crusoe–Tallgrass Cheyenne (Project Jade):** 2.7 GW dedicated gas plant approved January 2026 (planned, not yet built).

### Utility-built gas

Where the host utility builds the gas plants rather than the data centre operator, the most prominent case is Entergy Louisiana's 2.3 GW of new combined-cycle gas plants and a $1.2 bn 500 kV line built specifically to serve Meta's Hyperion campus, with Public Service Commission approval in 2025 [@dcd-entergy-meta]. Georgia Power's 2025 IRP added 6,000–8,500 MW of certified new resources (heavily gas) to serve 8,500 MW of forecast load growth by 2030, primarily data centre [@gpc-irp-2025].

### Nuclear restarts

Three retired US nuclear units are being brought back to serve hyperscaler load:

- **Three Mile Island Unit 1 / Crane Clean Energy Center:** 835 MW; Constellation–Microsoft 20-year PPA; restart targeted 2027 [@dcd-tmi-microsoft; @constellation-crane].
- **Duane Arnold (Iowa):** 600 MW; NextEra–Google 25-year PPA; restart Q1 2029 [@ans-duane-arnold].
- **Palisades (Michigan):** 800 MW; Holtec; offtake unsigned publicly; restart slipped to Q1/Q2 2026 [@powermag-palisades].

### Existing nuclear PPAs

- **Susquehanna / Cumulus:** AWS–Talen 1,920 MW PPA through 2042; transitioning to front-of-meter Spring 2026 after FERC rejected the original behind-the-meter co-location structure in November 2024 [@ud-talen-amazon; @ud-ferc-talen]. FERC subsequently directed PJM to write new co-location rules in late 2025 [@ferc-pjm-colo-2025].

### SMR offtake agreements (no scale before early 2030s)

- **Amazon–Energy Northwest–X-energy:** 320 MW Phase 1 (option to 960 MW), in service late 2030s.
- **Amazon–Dominion–X-energy:** South Korean (KHNP/Doosan) consortium agreement late 2025.
- **Google–Kairos Power:** 500 MW (7 KP-FHR units); first unit 2030, complete by 2035.
- **Meta–Oklo:** Pike County OH, 1.2 GW (16 × 75 MW Aurora units); Phase 1 150 MW by 2030.

None of the SMR projects above are themselves "under construction" — they are at licensing or early-engineering stage. First commercial NRC SMR construction permits are expected in calendar 2026 [@eia-smr-2025].

### Renewable PPAs (annual matched rather than 24/7)

Hyperscaler "100% renewable" claims are typically annual matched via PPAs and Renewable Energy Certificates, not 24/7 carbon-free supply. Actual instantaneous grid mix follows the host utility. Meta funded 977 MW of new renewables for Prineville on PacifiCorp's grid; AWS, Google and Microsoft each procure several GW per year of new solar and wind PPAs.

---

## 8. Demand forecasts to 2030

Forecasts of US data centre electricity demand published between mid-2024 and early 2026 differ by more than a factor of two for the same target year. The defensible 2030 US data centre energy range is **500–700 TWh** (12–17% of US electricity consumption). Investment-bank top-end forecasts (Goldman Sachs ~750 TWh; Morgan Stanley implied ~720 TWh) require both rapid AI build-out and resolution of supply-chain bottlenecks. The LBNL 2024 low case (~350 TWh extrapolated to 2030) requires AI training to plateau or efficiency gains to outrun workload growth, which the 2024–2026 trajectory has not supported.

**Table 6: Selected US data centre electricity demand forecasts**

| Source | Publication | 2028 TWh | 2030 TWh | 2035 TWh / GW | Notes |
|:--|:--|:--|:--|:--|:--|
| LBNL (DOE) | Dec 2024 | 325–580 (mid ~450) | n/a (forecast ends 2028) | n/a | 2023 baseline 176 TWh |
| EPRI (Powering Intelligence 2026 update) | Feb 2026 | n/a | 380–790 | ~900 TWh medium case to 2050 | 60% above 2024 numbers |
| IEA (Energy and AI) | Apr 2025 | n/a | ~425 (US share of 945 TWh global) | n/a | Increase of ~240 TWh from 185 TWh in 2024 |
| Goldman Sachs Research | Sep 2025 (rev. Apr 2026) | n/a | ~750 | n/a | Implies 95 GW US capacity by 2030 (+197% from 2025) |
| Morgan Stanley | Aug 2025 | n/a | ~720 (18% of US) | implied ~800+ | ~150 GW new global DCs by 2030 |
| McKinsey | 2024–2025 | n/a | 606 (~11.7% of US) | n/a | 80 GW US (from 25 GW in 2024) |
| BloombergNEF | Dec 2025 | n/a | n/a | 106 GW US peak by 2035 (8.6% of US) | Bottom-up |
| NERC (LTRA 2025) | Jan 2026 | n/a | n/a | +224 GW summer peak North America by 2035 | 65% increase vs LTRA 2024 |
| Grid Strategies | Dec 2025 | n/a | +166 GW US peak by 2030 (~90 GW from DCs) | n/a | 6× revision vs 2022 forecast |
| PJM Long-Term Load Forecast | Jan 2025 | n/a | +30 GW peak (94% from DCs) | 1,328 TWh RTO energy 2035 | RTO-wide |
| ERCOT | Dec 2025 update | n/a | 130–148 GW planning capacity | n/a | 226 GW in queue (~75% data centre) |
| MISO | 2025 | n/a | n/a | 163 GW peak by 2035 (+35% vs 2025) | 2.7% CAGR mid case |
| Dominion Energy (VA IRP) | Oct 2025 update | n/a | ~9 GW DC peak in 10 yrs | +20,000 MW DC in zone by 2037 | 47.2 GW contracted DC pipeline |
| Georgia Power 2025 IRP | Jul 2025 (PSC approval) | n/a | ~8,500 MW load growth by 2030 | n/a | 6,000–8,500 MW new resources approved |

*Source: ITK compilation across the cited sources. "TWh" is annual energy, "GW" is peak demand or contracted capacity — conversion between them requires a load-factor assumption, typically 60–75% for hyperscale and 80%+ for AI training clusters.*

### Phantom load

The single most important caveat on grid-operator and utility forecasts is that interconnection queues are massively oversubscribed. ERCOT's large-load queue grew from 63 GW at end-2024 to 226 GW by October 2025, of which only 1.8% was actually operational [@latitude-phantom]. Dominion has 47.2 GW of contracted data centre pipeline against a forecast peak data centre demand of about 9 GW in ten years [@vabusiness-dominion]. Industry estimates put speculative interconnection requests at 5–10× the number of projects that will be built [@ud-fraction]. Texas legislated disclosure requirements for duplicate filings in 2025.

A defensible adjustment to utility-stated demand for forward forecasting is to discount 30–50% as duplicative or speculative. Applying this to the Grid Strategies 166 GW US 2030 peak number takes the data-centre share from 90 GW down to 50–65 GW of net new build — close to BloombergNEF's bottom-up 106 GW by 2035.

---

## 9. Caveats and uncertainties

1. **Definitional inconsistency dominates the differences in headline numbers.** "Number of facilities" can be 580 (Synergy hyperscale-only) or 5,427 (Cloudscene broad). "Operating MW" can be 9.4 GW (CBRE primary-market colocation) or 50 GW (FERC interconnection-derived). "Under construction" can be 6 GW (CBRE) or 35 GW (JLL). None of these are wrong; they describe different universes.
2. **Hyperscaler IT loads are opaque.** Meta, Google, AWS and Microsoft do not publish per-site IT load. Trade-press values are aggregated from utility filings, building permits, satellite imagery and gas-turbine permits. Meta's own published Prineville info sheet discloses dollar investment, headcount and renewable supply but not IT capacity. The "1,400 MW Altoona" and "1,289 MW Prineville" numbers should be treated as master-plan envelopes, not currently energised IT load.
3. **Stargate Abilene capacity has shifted.** The campus was originally announced as scaling beyond 1.2 GW; the 600 MW expansion was cancelled in March 2026 after grid delivery delays. The 1.2 GW full build is the current cap.
4. **Microsoft Mt Pleasant figures.** Epoch AI reports each Fairwater building at ~1 GW of total power consumption (not pure IT load), and the 4-building Fairwater build at 3.3 GW by late 2027. The January 2026 village approval for 15 additional buildings is a separate, larger envelope. The 3.3 GW number is a published estimate, not a Microsoft disclosure.
5. **Susquehanna PPA structure was restructured.** The original 960 MW behind-the-meter co-location Interconnection Service Agreement was rejected by FERC in November 2024. The current arrangement is a grid-delivered PPA scaling to 1,920 MW by 2032; FERC has directed PJM to write new co-location rules.
6. **xAI Colossus capacity is contested.** Estimates of operating IT load span 250–750 MW. Much of the supply is on-site portable gas turbines that the Shelby County Health Department ruled were operating without permits.
7. **2025 was a step-change year.** The CBRE primary-market inventory grew 36% year-on-year, the fastest on record. Any number more than six months old is materially out of date.
8. **CBRE, JLL, Cushman & Wakefield, Newmark, DC Byte and datacenterHawk are subscription products.** The numbers used here come from publicly issued summary releases, the brokers' published chapter pages, and trade-press citations. The full PDF reports should be obtained directly for any figures intended for publication.
9. **Forecast spread is not all uncertainty.** Roughly half the gap between LBNL low and Goldman high reflects different assumptions about AI server share (banks assume AI hits 27%+ of DC power by 2027; LBNL assumes slower diffusion), build-rate constraints (banks take hyperscaler capex at face value; LBNL applies historical supply-chain limits), and PUE/cooling efficiency.

---

## 10. References

The full bibliography is below. URLs are listed in plain markdown and would convert to BibTeX entries in the form `@org-topic-year` for any subsequent published article. The three underlying research drafts are kept under `background/_research_drafts/` (`operating_fleet.md`, `under_construction.md`, `demand_forecasts.md`) for full source-level traceability.

### Government, regulator and laboratory sources

- LBNL, *2024 United States Data Center Energy Usage Report* (Dec 2024). https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
- US DOE, "DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers" (20 Dec 2024). https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- FERC, *2025 State of the Markets Report* (19 Mar 2026), summarised: https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/
- US EIA, "Data center owners turn to nuclear as potential electricity source". https://www.eia.gov/todayinenergy/detail.php?id=63304
- US EIA, "Small modular reactors and microreactors under development in the United States". https://www.eia.gov/todayinenergy/detail.php?id=67584
- NERC, *2025 Long-Term Reliability Assessment* (Dec 2025 / Jan 2026). https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf
- PJM, *2025 Long-Term Load Forecast Report*. https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf
- ERCOT, *2025 Report on Existing and Potential Electric System Constraints and Needs* (Dec 2025). https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf
- ERCOT large-load queue update (Apr 2026). https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf
- MISO, *MTEP25 Report*. https://cdn.misoenergy.org/MTEP25%20Report731648.pdf
- Dominion Energy, *2024 Virginia Integrated Resource Plan*. https://www.dominionenergy.com/-/media/content/about/our-company/irp/pdfs/2024-irp-w_o-appendices.pdf
- Dominion Long-Range Projections (Oct 2025) — coverage: https://virginiabusiness.com/dominion-data-center-power-demand-virginia-scc/
- Georgia Power, *2025 Integrated Resource Plan* (PSC approved Jul 2025). https://www.georgiapower.com/content/dam/georgia-power/pdfs/company-pdfs/2025-Integrated-Resource-Plan.pdf
- Virginia JLARC, *Data Centers in Virginia* (Dec 2024). https://jlarc.virginia.gov/pdfs/reports/Rpt598-2.pdf
- Grid Strategies, *National Load Growth Report 2025*. https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf
- E3, *Forecasting Large Loads in the Age of AI and Data Centers* (Dec 2025). https://www.ethree.com/wp-content/uploads/2025/12/E3Whitepaper_DataCenterForecasting.pdf
- FERC, "Fact sheet: FERC directs nation's largest grid operator to create new rules to embrace co-location" (Dec 2025). https://www.ferc.gov/news-events/news/fact-sheet-ferc-directs-nations-largest-grid-operator-create-new-rules-embrace

### Industry analysts

- Synergy Research Group, "Hyperscale Data Center Count Hits 1,136" (Mar 2025). https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity
- CBRE, *North America Data Center Trends H2 2025* (25 Feb 2026). https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025
- CBRE, *North America Data Center Trends H1 2025* (8 Sep 2025). https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025
- Cushman & Wakefield, *Americas Data Center Market Shifts to "Managed Growth" — H2 2025 Update* (Feb 2026). https://www.cushmanwakefield.com/en/united-states/news/2026/02/americas-data-center-market-shifts-to-managed-growth
- JLL, *2026 Global Data Center Outlook* (Jan 2026). https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- Newmark, *2025 US Data Center Market Outlook* (Feb 2025). https://www.nmrk.com/insights/market-report/2025-us-data-center-market-outlook
- DC Byte, *2026 Data Centre Outlook*. https://www.dcbyte.com/news-blogs/2026-data-centre-outlook-top-five-trends/
- datacenterHawk, *3Q 2025 Data Center Market Recap*. https://datacenterhawk.com/resources/market-insights/3q-2025-data-center-market-recap
- Bloom Energy, *2025 Data Center Power Report* (Jan 2026). https://www.bloomenergy.com/news/data-centers-are-turning-to-onsite-power-sources-to-address-35-gw-energy-gap-by-2030/
- IEEFA, "Projected data center growth spurs PJM capacity prices by factor of 10". https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
- Wood Mackenzie, "Reality bytes: the US data centre pipeline additions halved in Q4 2025". https://www.woodmac.com/news/opinion/reality-bytes-the-us-data-centre-pipeline-additions-halved-in-q4-2025-compared-to-the-previous-quarter/
- Baxtel, US directory. https://baxtel.com/data-center/united-states
- Cloudscene database via Cargoson (Nov 2025). https://www.cargoson.com/en/blog/number-of-data-centers-by-country
- Epoch AI, "OpenAI Stargate: where the US sites stand" (Apr 2026). https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
- Epoch AI, "Microsoft Fairwater Power Usage". https://epoch.ai/data-insights/fairwater-power-usage

### Major forecasts and analyses

- EPRI, *Powering Intelligence (2026 update)* (Feb 2026). https://restservice.epri.com/publicattachment/97025
- IEA, *Energy and AI* (Apr 2025). https://www.iea.org/reports/energy-and-ai
- Goldman Sachs Research, "AI to drive 165% increase in data center power demand by 2030" (Sep 2025; rev. Apr 2026). https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030
- Morgan Stanley, "Data center electricity consumption" podcast (2025). https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/data-center-electricity-consumption-michelle-weaver-david-arcaro
- McKinsey, "How data centers and the energy sector can sate AI's hunger for power". https://www.mckinsey.com/industries/private-capital/our-insights/how-data-centers-and-the-energy-sector-can-sate-ais-hunger-for-power
- BloombergNEF (Dec 2025), summarised: https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/
- "Phantom data centers are flooding the load queue", Latitude Media. https://www.latitudemedia.com/news/phantom-data-centers-are-flooding-the-load-queue/
- "ERCOT's large load queue jumped almost 300%", Utility Dive. https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/
- "A fraction of proposed data centers will get built", Utility Dive. https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/
- "The puzzle of low data center utilization rates", Power Policy. https://www.powerpolicy.net/p/the-puzzle-of-low-data-center-utilization

### Project-level reporting

- Meta, "Prineville Data Center" info sheet (Feb 2025). https://datacenters.atmeta.com/wp-content/uploads/2025/02/Metas-Prineville-Data-Center.pdf
- Meta, "Richland Parish Data Center". https://datacenters.atmeta.com/richland-parish-data-center/
- Meta, "Hello, El Paso!" (Oct 2025). https://datacenters.atmeta.com/2025/10/hello-el-paso/
- Meta, "One Year In: Meta's Richland Parish Data Center..." (Dec 2025). https://about.fb.com/news/2025/12/metas-richland-parish-data-center-supports-louisiana-economy-875-million-in-contracts/
- Engineering News-Record, "$27B Meta Data Center Pushes Louisiana Toward Massive Power Expansion". https://www.enr.com/articles/62766-27b-meta-data-center-pushes-louisiana-toward-massive-power-expansion
- Data Center Dynamics, "Entergy obtains approval to construct three gas facilities to serve Meta's 2GW data center in Louisiana". https://www.datacenterdynamics.com/en/news/entergy-obtains-approval-to-construct-three-gas-facilities-to-serve-metas-2gw-data-center-in-louisiana/
- CNBC, "Amazon opens $11 billion AI data center Project Rainier in Indiana" (29 Oct 2025). https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html
- Converge Digest, "AWS Activates Project Rainier Data Center Campus". https://convergedigest.com/aws-activates-project-rainier-data-center-campus/
- Data Center Dynamics, "Crusoe tops out final building at OpenAI Stargate data center campus in Abilene, Texas". https://www.datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas/
- CNBC, "OpenAI's first data center in $500 billion Stargate project is open in Texas" (23 Sep 2025). https://www.cnbc.com/2025/09/23/openai-first-data-center-in-500-billion-stargate-project-up-in-texas.html
- Tom's Hardware, "Oracle and OpenAI scrap planned 600MW Abilene expansion". https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion
- OpenAI, "Five new Stargate sites" (Sep 2025). https://openai.com/index/five-new-stargate-sites/
- Data Center Dynamics, "Vantage breaks ground on Texas gigawatt data center campus for OpenAI". https://www.datacenterdynamics.com/en/news/vantage-breaks-ground-on-texas-gigawatt-data-center-campus-for-openai/
- Construction Owners, "Oracle and OpenAI to Power New Texas Data Center Off the Grid". https://www.constructionowners.com/news/oracle-and-openai-to-power-new-texas-data-center-off-the-grid
- Data Center Dynamics, "Stack joins multi-billion-dollar data center & microgrid project in New Mexico". https://www.datacenterdynamics.com/en/news/stack-joins-multi-billion-dollar-data-center-microgrid-project-in-new-mexico/
- Source NM, "NM Project Jupiter data center developers announce new plans for generating power" (Apr 2026). https://sourcenm.com/2026/04/27/nm-project-jupiter-data-center-developers-announce-new-plans-for-generating-power/
- Data Center Frontier, "Vantage Data Centers Pours $15B Into Wisconsin AI Campus". https://www.datacenterfrontier.com/hyperscale/article/55326357/vantage-data-centers-pours-15b-into-wisconsin-ai-campus-as-it-builds-global-giga-scale-footprint
- Related Companies, "OpenAI, Oracle and Related Digital announce Stargate data center site in Michigan" (Oct 2025). https://www.related.com/press-releases/2025-10-30/openai-oracle-and-related-digital-announce-stargate-data-center-site
- CNBC, "Microsoft's plans for 15 more data centers win approval at former Wisconsin Foxconn site" (26 Jan 2026). https://www.cnbc.com/2026/01/26/microsoft-wins-approval-for-15-data-centers-at-wisconsin-foxconn-site.html
- Data Center Frontier, "Details Emerge On Microsoft's $1.8 Billion Investment In Atlanta Data Centers". https://www.datacenterfrontier.com/hyperscale/article/55126626/details-emerge-on-microsofts-18-billion-investment-in-atlanta-data-centers-amid-tax-development-wrangles
- OPB, "A small town in Central Washington is Microsoft's answer to the data center backlash" (Jan 2026). https://www.opb.org/article/2026/01/17/quincy-washington-microsoft-data-center/
- Utility Dive, "Talen to sell Amazon 1.9 GW from Susquehanna nuclear plant". https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/
- Talen Energy, "Talen Energy Expands Nuclear Energy Relationship with Amazon" (Jun 2025). https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-expands-nuclear-energy-relationship-amazon
- Utility Dive, "FERC interconnection ISA Talen Amazon data center Susquehanna Exelon". https://www.utilitydive.com/news/ferc-interconnection-isa-talen-amazon-data-center-susquehanna-exelon/731841/
- Constellation Energy, "One Year Later: Crane Clean Energy Center Still in the Spotlight" (Sep 2025). https://www.constellationenergy.com/newsroom/2025/09/one-year-later-crane-clean-energy-center-still-in-the-spotlight-and-ahead-of-schedule.html
- World Nuclear News, "Constellation seeks regulator's help for 2027 plant restart". https://www.world-nuclear-news.org/articles/constellation-seeks-regulators-help-for-2027-plant-restart
- ANS, "NextEra and Google ink a deal to restart Duane Arnold" (Oct 2025). https://www.ans.org/news/2025-10-28/article-7501/nextera-and-google-ink-a-deal-to-restart-duane-arnold/
- Power Magazine, "Palisades Nuclear Plant Moved to Operations Status, Ready to Receive Fuel". https://www.powermag.com/palisades-nuclear-plant-moved-to-operations-status-ready-to-receive-fuel/
- Neutron Bytes, "Holtec Submits License Application to NRC for the Palisades Twin SMR-300s" (Jan 2026). https://neutronbytes.com/2026/01/11/holtec-submits-license-application-to-nrc-for-the-palisades-twin-smr-300s/
- SemiAnalysis, "xAI's Colossus 2 — First Gigawatt Datacenter In The World". https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter
- Data Center Dynamics, "Elon Musk's xAI gets go-ahead for 41 natural gas turbines in Mississippi". https://www.datacenterdynamics.com/en/news/musks-xai-gets-go-ahead-for-41-natural-gas-turbines-in-mississippi-to-power-colossus-data-centers/
- Earthjustice, "Illegal Pollution from Data Center Power Plants — We're Suing xAI". https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus
- SELC, "xAI built an illegal power plant to power its data center". https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/
- CNBC, "Meta to spend $10 billion on AI data center in El Paso, 1GW by 2028" (Mar 2026). https://www.cnbc.com/2026/03/26/meta-to-spend-10-billion-on-ai-data-center-in-el-paso-1gw-by-2028.html
- Texas Tribune, "Plan to run El Paso data center on natural gas sparks concern" (Jan 2026). https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/
- Microsoft Local, "Palmetto datacenter construction update". https://local.microsoft.com/blog/palmetto-datacenter-construction-update/
- Microsoft Local, "Mount Pleasant datacenter project update". https://local.microsoft.com/blog/mount-pleasant-datacenter-project-update/
- Power Magazine, "Wyoming Approves Data Center Campus That Includes 2.7 GW of New Natural Gas-Fired Generation". https://www.powermag.com/wyoming-approves-data-center-campus-that-includes-2-7-gw-of-new-natural-gas-fired-generation/
- Data Center Dynamics, "Sailfish plans multi-gigawatt data center park outside DFW, Texas". https://www.datacenterdynamics.com/en/news/sailfish-plans-multi-gigawatt-data-center-park-outside-dfw-texas/
- Anthropic, "Anthropic invests $50 billion in American AI infrastructure" (Nov 2025). https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure
- CNBC, "Anthropic to spend $50 billion on U.S. AI infrastructure" (12 Nov 2025). https://www.cnbc.com/2025/11/12/anthropic-ai-data-centers-texas-new-york.html
- Bisnow, "Blackstone's QTS Files Appeal To Save Massive Virginia Data Center Campus". https://www.bisnow.com/washington-dc/news/data-center-development/blackstones-qts-appeals-court-decision-blocking-huge-virginia-project-134390
- Data Center Dynamics, "EdgeConneX files to convert warehouse and build new 700,000 sq ft data center in New Albany, Ohio". https://www.datacenterdynamics.com/en/news/edgeconnex-files-to-convert-warehouse-and-build-new-700000-sq-ft-data-center-in-new-albany-ohio/
- Carbon Credits, "Meta Signs Three Nuclear Deals of Up to 6.6 GW to Fuel AI Data Center Growth". https://carboncredits.com/meta-signs-three-nuclear-deals-of-up-to-6-6-gw-to-fuel-ai-data-center-growth/
- Amazon, "Amazon signs agreements for innovative nuclear energy projects". https://www.aboutamazon.com/news/sustainability/amazon-nuclear-small-modular-reactor-net-carbon-zero
- Virginia Business, "Equinix wants to build another large data center in Loudoun County". http://www.virginiabusiness.com/news/article/equinix-wants-to-build-another-large-data-center-in-loudoun-county
- WTOP News, "Northern Virginia data centers have topped 4,900 megawatts. What does that mean?" (Jun 2025). https://wtop.com/business-finance/2025/06/northern-virginia-data-centers-have-topped-4900-megawatts-what-does-that-mean/
- Data Center Frontier, "Data Centers Are Booming In Ohio's Digital Heartland". https://www.datacenterfrontier.com/site-selection/article/33035576/data-centers-are-booming-in-ohios-digital-heartland
- BlackRidge Research, "Top 10 Largest Data Centers In The US (2026)" (Feb 2026). https://www.blackridgeresearch.com/blog/largest-top-biggest-data-centers-in-united-states-list

---

*End of background note. Three underlying research drafts are kept under `background/_research_drafts/` for traceability: `operating_fleet.md`, `under_construction.md`, `demand_forecasts.md`. The CBRE H1/H2 2025 PDFs, the LBNL 2024 PDF, and the EPRI 2026 update PDF should be obtained directly for any figures intended for citation in published work.*
