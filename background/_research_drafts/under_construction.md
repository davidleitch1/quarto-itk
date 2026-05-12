---
title: "US Data Centre Pipeline Under Construction — May 2026 Snapshot"
author: "David Leitch"
date: 2026-05-10
status: research draft
---

## Methodology note: what counts as "under construction"

The figure most often quoted in the trade press for US data centre construction in early 2026 is roughly **25 GW** of IT/critical load. That number — used by Cushman & Wakefield, datacenterHawk and broadly consistent with JLL — includes any project where vertical construction (steel, foundations or shell) is in progress in primary, secondary and tertiary North American markets. By contrast, **CBRE's H2 2025 report cites 5,994 MW under construction** at the end of 2025, down from 6,350 MW a year earlier [Source: https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025, 25 Feb 2026]. The difference is definitional: CBRE's tracked universe is wholesale colocation in eight primary markets (Northern Virginia, Dallas-Ft Worth, Atlanta, Phoenix, Chicago, Silicon Valley, Hillsboro, New York Tri-State), excluding hyperscaler-owned/built campuses, behind-the-meter "AI factories" outside those metros (Abilene, Shackelford County, Richland Parish, etc.) and tertiary markets such as West Texas, central Wisconsin and rural Indiana.

For this note "under construction" means **physical construction underway** (foundation work, steel, shell, mechanical/electrical fit-out) as of approximately May 2026 — distinct from "planned/announced" (zoning, land option, MOU). I exclude projects whose only public milestone to date is an interconnection request, a land option or a press release. Several mega-campus announcements (Crusoe Project Jade in Wyoming, Sailfish Comanche Circle in Hood County TX, Anthropic-Fluidstack Mitchell County TX) have site approvals but limited evidence of vertical construction, so I flag them as "early-stage".

A critical pitfall: a "$25 billion data centre" press release frequently bundles a 10-year campus build-out into a single announcement. The numbers below distinguish **first-phase under construction** from **full campus build-out**.

## Pipeline aggregates: reconciling the trackers

**Table 1 — Major tracker estimates of US/Americas under-construction capacity, late 2025 / early 2026**

| Source | Headline figure | Geography | Date | Definition notes |
|:-------|:----------------|:----------|:-----|:-----------------|
| Cushman & Wakefield H2 2025 | **25.3 GW** under construction; 89% pre-committed | Americas | Feb 2026 | All asset types; Virginia 6.3 GW (~25%), West Texas 2.9 GW |
| datacenterHawk | **25.3 GW** under construction; 89% pre-leased | North America | Q1 2026 | Methodology aligns with C&W |
| JLL 2026 Global Outlook | **35 GW** total US construction pipeline; 92% pre-committed; **>10 sites ≥1 GW** under construction; Texas 6.5 GW alone | US | Jan 2026 | Includes near-term (≤24 mo) plus active sitework |
| CBRE H2 2025 | **5,994 MW** under construction | North America primary markets | Feb 2026 | Wholesale colocation only, 8 primary metros |
| Newmark 2025 Outlook | $31.5 bn annualised data centre construction spend | US | Feb 2025 | Capex-based, not MW-based |
| Synergy Research | Hyperscale capex $142 bn in Q3 2025 (+180% YoY); ~800 hyperscale facilities in pipeline globally | Global | Q4 2025 | Hyperscale only |

*Sources: [Cushman & Wakefield](https://www.cushmanwakefield.com/en/united-states/news/2026/02/americas-data-center-market-shifts-to-managed-growth); [JLL 2026 Global Data Center Outlook](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook); [CBRE H2 2025](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025); [Newmark 2025 US Data Center Outlook](https://www.nmrk.com/insights/market-report/2025-us-data-center-market-outlook); [Synergy Research](https://www.srgresearch.com/articles/hyperscale-spending-spree-is-driving-dramatic-growth-in-data-center-capacity).*

**Reconciliation.** The CBRE 6 GW and the C&W/Hawk 25 GW figures are not contradictory — they describe different universes. The CBRE number is the most defensible "wholesale colo space being built in the eight legacy hubs"; the 25 GW figure adds hyperscaler-owned campuses (Meta Hyperion, Amazon Project Rainier, Microsoft Mt Pleasant, xAI Colossus, all the Stargate sites) and emerging power-advantaged regions (Abilene, Shackelford County, Richland Parish, southern Wyoming, Mt Pleasant WI, New Carlisle IN). JLL's 35 GW is the broadest, including projects where construction begins in 2026 H1.

For an "actually-under-construction in mid-2026" working number, **22–28 GW of IT/critical load in the United States** is a reasonable range, with the central estimate around **24–26 GW**.

## Top under-construction projects (top 20)

The table below catalogues the largest individual projects with verifiable construction underway. Capacity refers to first-phase IT/critical load under construction unless noted; full campus build-out is in the notes column where larger.

**Table 2 — Top US data centre projects under physical construction, May 2026**

| # | Project / Campus | Owner-Developer / Anchor | Location (Utility / ISO) | UC capacity (MW) | First power / COD | Power source | Source |
|---:|:-----------------|:-------------------------|:-------------------------|---:|:----------------|:-----------|:-------|
| 1 | Stargate Abilene (Lancium Clean Campus) | Crusoe / Oracle / OpenAI | Abilene, TX (Oncor / ERCOT) | 1,200 (8 buildings; 4 live, 4 finishing) | 4 buildings live Sep 2025; balance mid-2026 | On-site natural gas + ERCOT grid (some local wind) | [DCD](https://www.datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas/); [CNBC](https://www.cnbc.com/2025/09/23/openai-first-data-center-in-500-billion-stargate-project-up-in-texas.html) |
| 2 | Hyperion (Richland Parish) | Meta / own use | Richland Parish, LA (Entergy / MISO South) | 2,000 first phase (campus scales to 5 GW) | Phase 1 partial energisation 2027; full first-phase 2028 | 3 new Entergy CCGTs totalling ~2.3 GW + 240 mi 500-kV line; Meta-funded utility-scale renewables; LOI for nuclear | [Entergy/DCD](https://www.datacenterdynamics.com/en/news/entergy-obtains-approval-to-construct-three-gas-facilities-to-serve-metas-2gw-data-center-in-louisiana/); [Meta](https://datacenters.atmeta.com/richland-parish-data-center/); [ENR](https://www.enr.com/articles/62766-27b-meta-data-center-pushes-louisiana-toward-massive-power-expansion) |
| 3 | Project Rainier | AWS / Anthropic | New Carlisle, IN (AEP / I&M / MISO Indiana) | 2,200+ campus; 7 of 30 buildings already live (~500 MW operational) | Operational since Oct 2025; balance through 2026-27 | AEP grid; AWS PPAs incl. nuclear (Susquehanna), wind, solar | [CNBC](https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana); [AWS](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/) |
| 4 | Frontier (Shackelford County) | Vantage Data Centers / Oracle / OpenAI (Stargate) | Shackelford County, TX (Oncor / ERCOT) | 1,400 (10 buildings, 3.7 M sqft) | First building H2 2026 | 700 MW behind-the-meter natural gas microgrid (Voltagrid) — off-grid initially | [DCD](https://www.datacenterdynamics.com/en/news/vantage-breaks-ground-on-texas-gigawatt-data-center-campus-for-openai/); [Construction Owners](https://www.constructionowners.com/news/oracle-and-openai-to-power-new-texas-data-center-off-the-grid) |
| 5 | Saline Township (Stargate Michigan) | Related Digital / Oracle / OpenAI | Saline Township, MI (DTE / MISO) | 1,400 (3 buildings) | Construction started early 2026; first power 2027–28 | DTE grid + battery storage | [Related](https://www.related.com/press-releases/2025-10-30/openai-oracle-and-related-digital-announce-stargate-data-center-site); [Fortune](https://fortune.com/2026/05/06/ai-data-center-michigan-saline-politics-farmland/) |
| 6 | Project Jupiter (Stargate New Mexico) | STACK Infrastructure / BorderPlex / Oracle / OpenAI | Doña Ana County (Santa Teresa), NM (El Paso Electric / WECC) | 2,200 planned, 4 buildings phase 1 | Late 2026 first energisation | Bloom Energy solid-oxide fuel-cell microgrid (revised Apr 2026 from gas turbines) | [DCD](https://www.datacenterdynamics.com/en/news/stack-joins-multi-billion-dollar-data-center-microgrid-project-in-new-mexico/); [Source NM](https://sourcenm.com/2026/04/27/nm-project-jupiter-data-center-developers-announce-new-plans-for-generating-power/) |
| 7 | Stargate Milam County | SB Energy / SoftBank / OpenAI / Oracle | Milam County, TX (Oncor / ERCOT) | 1,200 | First building Oct 2026 | On-site generation (type undisclosed); ERCOT grid | [Epoch AI](https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand); [DCD](https://www.datacenterdynamics.com/en/news/openai-announces-five-more-us-stargate-data-centers-with-oracle-and-softbank/) |
| 8 | Stargate Port Washington | Vantage Data Centers / Oracle / OpenAI | Port Washington, WI (We Energies / MISO) | 1,300 | First power 2027 | Grid + ~70% solar/wind/battery PPAs | [Epoch AI](https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand); [Data Center Frontier](https://www.datacenterfrontier.com/hyperscale/article/55326357/vantage-data-centers-pours-15b-into-wisconsin-ai-campus-as-it-builds-global-giga-scale-footprint) |
| 9 | Microsoft Mt Pleasant (former Foxconn site) | Microsoft / own use | Mount Pleasant, WI (We Energies / MISO) | First DC online; 15 more buildings approved Jan 2026 (~9 M sqft) | First DC late 2025; phase 2 ground 2026 | We Energies grid (incl. unused legacy Foxconn capacity), Microsoft renewable PPAs | [CNBC](https://www.cnbc.com/2026/01/26/microsoft-wins-approval-for-15-data-centers-at-wisconsin-foxconn-site.html); [DCD](https://www.datacenterdynamics.com/en/news/microsoft-given-greenlight-for-15-more-data-center-buildings-in-mount-pleasant-wisconsin/) |
| 10 | Cumulus / Susquehanna Campus | AWS (acquired from Talen 2024) / Talen Energy | Berwick (Salem Twp), PA (PPL / PJM) | 960 currently sited; PPA scales to 1,920 by 2032 | Front-of-meter transition Spring 2026 | Susquehanna nuclear (PPA), then PJM-delivered via PPL | [Utility Dive](https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/); [Talen IR](https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-expands-nuclear-energy-relationship-amazon) |
| 11 | xAI Colossus 1 + Colossus 2 | xAI (Musk) / own use | South Memphis, TN (TVA / MLGW) and Southaven, MS | ~750 operational; permit for 1,200 self-gen approved | Colossus 1 live; Colossus 2 came online late 2025 / Jan 2026 | 18+ on-site Solar Turbines/Mitsubishi gas turbines (495 MW operating; 41 more permitted in MS); some TVA/MLGW grid; planned 168 MWh Megapack BESS | [SemiAnalysis](https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter); [DCD](https://www.datacenterdynamics.com/en/news/musks-xai-gets-go-ahead-for-41-natural-gas-turbines-in-mississippi-to-power-colossus-data-centers/); [SELC](https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/) |
| 12 | Meta El Paso (Project Ranger) | Meta / own use | El Paso, TX (El Paso Electric / WECC; not ERCOT) | 1,000 (12 buildings, ~1.2 M sqft) | Phase 1 by 2028; ground broken Oct 2025 | 813 modular gas-fired generators (~366 MW) on-site; El Paso Electric grid; matching renewables | [Meta](https://datacenters.atmeta.com/2025/10/hello-el-paso/); [CNBC](https://www.cnbc.com/2026/03/26/meta-to-spend-10-billion-on-ai-data-center-in-el-paso-1gw-by-2028.html); [Texas Tribune](https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/) |
| 13 | Microsoft Palmetto / Atlanta Cluster | Microsoft / own use | Palmetto / Douglasville / East Point, GA (Georgia Power / SERC) | $1.8 bn invested; Palmetto ~116 acres + multiple sub-campuses | Palmetto in active construction since Apr 2024; finishes by 2028 | Georgia Power grid (heavy gas + nuclear Vogtle); Microsoft renewable PPAs | [Data Center Frontier](https://www.datacenterfrontier.com/hyperscale/article/55126626/details-emerge-on-microsofts-18-billion-investment-in-atlanta-data-centers-amid-tax-development-wrangles); [Microsoft Local](https://local.microsoft.com/blog/palmetto-datacenter-construction-update/) |
| 14 | Microsoft Quincy WA expansion | Microsoft / own use | Quincy, Malaga, East Wenatchee, WA (Grant PUD / Chelan PUD / WECC) | 622 MW existing; further expansion permitted Jan 2026 | Continuous build-out | Grand Coulee hydro via Grant PUD; new closed-loop cooling | [OPB](https://www.opb.org/article/2026/01/17/quincy-washington-microsoft-data-center/); [DCD](https://www.datacenterdynamics.com/en/analysis/inside-microsofts-quincy-data-center/) |
| 15 | Crane Clean Energy Center (TMI Unit 1) | Constellation / Microsoft (PPA) | Londonderry Twp, PA (PJM / PPL) | 835 MW reactor restart (entirely PPA-dedicated to MS data centres) | Restart targeted 2027 | Restarted nuclear (PPA, 20-yr) | [Constellation](https://www.constellationenergy.com/newsroom/2025/09/one-year-later-crane-clean-energy-center-still-in-the-spotlight-and-ahead-of-schedule.html); [World Nuclear News](https://www.world-nuclear-news.org/articles/constellation-seeks-regulators-help-for-2027-plant-restart) |
| 16 | Duane Arnold restart | NextEra / Google (PPA) | Palo, IA (MISO / Alliant) | 600 MW reactor restart | Targeted Q1 2029 | Restarted nuclear (Google PPA, 25-yr) | [ANS](https://www.ans.org/news/article-7501/nextera-and-google-ink-a-deal-to-restart-duane-arnold/); [Iowa PR](https://www.iowapublicradio.org/ipr-news/2026-04-29/what-restarting-the-duane-arnold-power-plant-tells-us-about-nuclear-energy-under-the-trump-administration) |
| 17 | Palisades restart | Holtec / unsigned offtake | Covert Twp, MI (MISO / Consumers) | 800 MW PWR restart | Restart slipped from late 2025 to Q1/Q2 2026; SMR-300 twin units early 2030s | Restarted nuclear; SMR phase under licensing | [Power Magazine](https://www.powermag.com/palisades-nuclear-plant-moved-to-operations-status-ready-to-receive-fuel/); [Neutron Bytes](https://neutronbytes.com/2026/01/11/holtec-submits-license-application-to-nrc-for-the-palisades-twin-smr-300s/) |
| 18 | QTS PW Digital Gateway | QTS (Blackstone) | Prince William County, VA (Dominion / PJM) | Up to 800 acres planned; rezoning blocked Mar 2026, appeal pending | Stalled by court ruling | Dominion (PJM) | [Bisnow](https://www.bisnow.com/washington-dc/news/data-center-development/blackstones-qts-appeals-court-decision-blocking-huge-virginia-project-134390) |
| 19 | Equinix Loudoun expansion (LD-15-class) | Equinix / colocation | Ashburn, VA (Dominion / PJM) | 1.1 M sqft, 6 new buildings filed late 2025 | Permitting / early site works | Dominion grid | [Virginia Business](http://www.virginiabusiness.com/news/article/equinix-wants-to-build-another-large-data-center-in-loudoun-county) |
| 20 | EdgeConneX New Albany OH | EdgeConneX / hyperscaler tenant | New Albany, OH (AEP Ohio / PJM) | 700,000 sqft, MW undisclosed (likely 100–250 MW) | Construction Q4 2025; live Q1 2026 | AEP Ohio grid | [DCD](https://www.datacenterdynamics.com/en/news/edgeconnex-files-to-convert-warehouse-and-build-new-700000-sq-ft-data-center-in-new-albany-ohio/) |

*Notes: "UC capacity" is what is currently under construction (i.e. shell or fit-out in progress as of May 2026), not the full multi-decade campus envelope. Several projects (Hyperion, Project Rainier, Mt Pleasant, Quincy) sit on land approved for far larger build-outs that should not be conflated with what is being built today.*

### Items I could not verify as physically under construction in May 2026

- **Crusoe Project Jade (southeast Wyoming)** — county approval and 2.7 GW gas plant approved January 2026; first buildings expected 2027. Listed by Crusoe and Tallgrass as advancing but no public evidence of vertical construction yet [Source: https://www.datacenterdynamics.com/en/news/crusoe-gets-go-ahead-for-18gw-data-center-campus-and-power-plant-in-cheyenne-wyoming/].
- **Sailfish Comanche Circle (Hood County, TX)** — 5 GW master-planned; first 600 MW behind-the-meter envisaged in 24 months but ground-up status not confirmed in public reporting [Source: https://www.datacenterdynamics.com/en/news/sailfish-plans-multi-gigawatt-data-center-park-outside-dfw-texas/].
- **Anthropic-Fluidstack (Mitchell County TX, Niagara County NY, southeast LA, Haskell County TX)** — announced Nov 2025; sites coming online "throughout 2026" but only some are confirmed as under construction. Google's $5 bn financing of a Texas Anthropic site (Nexus operator) was reported in late March 2026 [Source: https://www.cnbc.com/2025/11/12/anthropic-ai-data-centers-texas-new-york.html; https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure].
- **Stargate Lordstown OH** — SoftBank claims groundbreaking but DCD/Epoch reporting indicates land clearance only, not data centre construction [Source: https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand].
- **Meta-Oklo Pike County OH (1.2 GW SMR campus)** — first reactors not expected until 2030; classify as planned [Source: https://carboncredits.com/meta-signs-three-nuclear-deals-of-up-to-6-6-gw-to-fuel-ai-data-center-growth/].

## Geographic and utility concentration

**Top markets by under-construction MW (combining trackers, May 2026):**

| Region | UC capacity (MW) | Primary utility / ISO | Stress notes |
|:-------|---:|:----------------------|:-------------|
| Northern Virginia (Loudoun + PW) | ~6,300 | Dominion / PJM | PJM Dominion zone forecast +20 GW data centre load by 2037 [Source: PJM 2025 LTLF]; capacity auction cleared $14.7 bn for 2025-26, ~63% attributed to data centre demand [Source: IEEFA] |
| West Texas (Abilene, Shackelford, Milam) | ~2,900–3,500 | Oncor / ERCOT | ERCOT large-load queue 233 GW, +269% YoY; ~77% data centre [Source: https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/] |
| Central Texas / DFW | ~1,000–1,500 colo + Sailfish/PowerHouse adds | Oncor / ERCOT | Same large-load queue dynamics; gas turbine supply-chain backlog |
| Atlanta / Georgia | ~2,076 (CBRE) | Georgia Power / SERC | Georgia Power asking for 9 GW more capacity; Vogtle 3/4 already commissioned |
| Phoenix | ~1,000–1,500 | APS / SRP / WECC | Water and transmission constraints |
| Hillsboro / Portland | ~600 | PGE / Bonneville / WECC | Constrained by Bonneville interconnection queue |
| Chicago / NW Indiana | ~1,500 (incl. Project Rainier) | AEP / NIPSCO / Commonwealth Edison / MISO/PJM | Indiana load growth pushing AEP/I&M into emergency capacity contracts |
| Louisiana (Richland Parish + DeSoto Parish) | ~2,000 (Hyperion phase 1) | Entergy / MISO South | Entergy data-centre customer pipeline 7–12 GW; PSC approved 2.3 GW new gas |
| Wisconsin (Mt Pleasant + Port Washington) | ~2,500–3,000 | We Energies / MISO | Microsoft + Vantage stacking on adjacent counties |
| Memphis MSA | ~750–1,200 (xAI) | TVA / MLGW + on-site | Air-quality and unpermitted-turbine litigation (Earthjustice/SELC) |

**Headline grid-stress takeaway.** PJM (Dominion zone), ERCOT (Oncor west Texas), MISO (Entergy Louisiana, Indiana, Wisconsin) and the Georgia Power service area are the four most acute concentrations. PJM's 2025 Long-Term Load Forecast attributes 94% of the projected 32 GW of incremental peak load from 2024-2030 to data centres [Source: https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf]. ERCOT begins 2026 with 233 GW in its large-load interconnection queue, of which ~77% (~180 GW) is data centre [Source: https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/]. MISO utilities collectively forecast 61 GW of new demand, more than half of MISO's 2025 peak [Source: https://southernrenewable.org/news-updates/what-miso-souths-grid-markets-transmission-buildout-mean-for-ersc-in-2026].

## Notable behind-the-meter / off-grid power deals

A pronounced shift in 2025-26 is the move to **on-site / behind-the-meter generation** to escape multi-year interconnection queues:

- **Vantage Frontier (Shackelford TX)**: 700 MW Voltagrid natural-gas microgrid, off-grid initially [Source: https://www.constructionowners.com/news/oracle-and-openai-to-power-new-texas-data-center-off-the-grid].
- **xAI Colossus 1+2 (Memphis/Southaven)**: 18+ on-site gas turbines (~495 MW) operational; 41 more permitted in Mississippi; Earthjustice/SELC filed suit over unpermitted air emissions [Source: https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus].
- **Meta El Paso**: 813 modular Caterpillar/Cummins-class gensets totalling 366 MW on-site [Source: https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/].
- **Project Jupiter (Doña Ana NM)**: Bloom Energy solid-oxide fuel cells (April 2026 redesign replacing original gas turbines) [Source: https://sourcenm.com/2026/04/27/nm-project-jupiter-data-center-developers-announce-new-plans-for-generating-power/].
- **Crusoe Abilene**: hybrid on-site gas + Oncor grid + local wind [Source: https://www.datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas/].
- **Crusoe-Tallgrass Cheyenne (Project Jade)**: 2.7 GW dedicated gas plant approved Jan 2026 (planned, not yet built) [Source: https://www.powermag.com/wyoming-approves-data-center-campus-that-includes-2-7-gw-of-new-natural-gas-fired-generation/].

## Notable nuclear-PPA deals (most are restarts or new-build, not under physical construction at the data centre level)

- **Crane Clean Energy Center / Three Mile Island Unit 1** — Constellation / Microsoft 20-yr PPA, restart targeted 2027 (accelerated from 2028); 835 MW [Source: https://www.constellationenergy.com/newsroom/2025/09/one-year-later-crane-clean-energy-center-still-in-the-spotlight-and-ahead-of-schedule.html].
- **Susquehanna / Cumulus** — Amazon/Talen 1,920 MW PPA through 2042; transitions to front-of-meter Spring 2026 [Source: https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/].
- **Duane Arnold** — Google / NextEra 25-yr PPA; restart Q1 2029; 600 MW [Source: https://www.ans.org/news/2025-10-28/article-7501/nextera-and-google-ink-a-deal-to-restart-duane-arnold/].
- **Palisades** — Holtec restart slipped to Q1/Q2 2026; no signed data centre offtake confirmed publicly. Twin SMR-300 application filed Jan 2026, in service early 2030s [Source: https://neutronbytes.com/2026/01/11/holtec-submits-license-application-to-nrc-for-the-palisades-twin-smr-300s/].
- **Energy Northwest / X-energy / Amazon** — 320 MW Phase 1 (option to 960 MW), in service late 2030s [Source: https://www.aboutamazon.com/news/sustainability/amazon-nuclear-small-modular-reactor-net-carbon-zero].
- **Meta-Oklo Pike County, OH** — 1.2 GW (16 × 75 MW Aurora units), Phase 1 150 MW by 2030 [Source: https://carboncredits.com/meta-signs-three-nuclear-deals-of-up-to-6-6-gw-to-fuel-ai-data-center-growth/].

**Important interpretive caveat:** none of the SMR or restart projects above are themselves "under construction" in the conventional sense, except for Palisades (refurbishment) and the Crane Clean Energy Center (refurbishment + grid reconfiguration). The SMR pipeline is at licensing/early-engineering stage; first commercial NRC SMR construction permits are expected in calendar 2026 [Source: https://www.eia.gov/todayinenergy/detail.php?id=67584].

## Reconciliation summary and confidence ranking

1. **Highest confidence** (verifiably steel/concrete in ground in May 2026): Stargate Abilene, Project Rainier, Hyperion, Microsoft Mt Pleasant phase 1, Microsoft Palmetto, xAI Colossus 1, Microsoft Quincy expansion, Frontier (Shackelford) site preparation, Crane CEC restart works, Susquehanna transmission reconfiguration, EdgeConneX New Albany, Equinix Ashburn (existing buildings).
2. **Medium confidence** (announced ground-breaking, partial verification): Stargate Saline Township, Stargate Doña Ana (foundation work confirmed Mar 2026), Stargate Milam County (steel framing per March 2026 satellite imagery), Meta El Paso, xAI Colossus 2 third building, Vantage Frontier vertical construction.
3. **Lower confidence — early stage / pre-construction**: Crusoe Project Jade Wyoming, Sailfish Comanche Circle, Anthropic-Fluidstack sites beyond first lease, Stargate Lordstown OH, QTS PW Digital Gateway (court-blocked), Meta-Oklo Pike County (planning).

The **best central estimate** for US data centre IT/critical load physically under construction in May 2026 is **22–26 GW**, spread across approximately 35–50 individual campuses, of which **at least 10 individual sites are 1 GW or larger** (consistent with JLL's count of "more than 10 ≥1 GW projects under construction"). Roughly **89–92% is pre-committed** (preleased or owner-occupied), so this is a supply pipeline aimed at known customers, not speculative capacity.

## Bibliography

### Tier 1 — Government, ISO, regulator filings

- PJM Interconnection. (2025). *2025 Long-Term Load Forecast Report*. https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.pdf
- PJM Inside Lines. (2025). *2025 Long-Term Load Forecast Report Predicts Significant Increase in Electricity Demand*. https://insidelines.pjm.com/2025-long-term-load-forecast-report-predicts-significant-increase-in-electricity-demand/
- ERCOT. (2026, April). *Public ERCOT Update — Senate Committee on Business & Commerce*. https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf
- ERCOT. (2026, April 15). *ERCOT Releases Preliminary Long-Term Load Forecast for Years 2026-2032*. https://www.ercot.com/news/release/04152026-ercot-releases-preliminary
- US EIA. (2025). *Small modular reactors and microreactors under development in the United States*. https://www.eia.gov/todayinenergy/detail.php?id=67584
- US EIA. (2025). *We expect rapid electricity demand growth in Texas and the mid-Atlantic*. https://www.eia.gov/todayinenergy/detail.php?id=65844
- Virginia JLARC. (2024, December). *Virginia Data Center Study*. https://jlarc.virginia.gov/pdfs/presentations/JLARC%20Virginia%20Data%20Center%20Study_FINAL_12-09-2024.pdf
- Grid Strategies LLC. (2025). *Power Demand Forecasts Revised Up for Third Year Running*. https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf

### Tier 2 — Real-estate / industry trackers

- CBRE. (2026, February 25). *North America Data Center Trends H2 2025*. https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025
- CBRE. (2025, October). *North America Data Center Trends H1 2025*. https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025
- Cushman & Wakefield. (2026, February). *Americas Data Center Market Shifts to "Managed Growth" — H2 2025 Update*. https://www.cushmanwakefield.com/en/united-states/news/2026/02/americas-data-center-market-shifts-to-managed-growth
- Cushman & Wakefield. (2026). *Americas Data Center Update H2 2025*. https://www.cushmanwakefield.com/en/insights/americas-data-center-update
- JLL. (2026, January). *2026 Global Data Center Outlook*. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- JLL. (2026). *North America Data Center Report Year-end 2025: Texas prepares to dethrone Virginia*. https://www.jll.com/en-us/newsroom/jll-north-america-data-center-report-year-end-2025
- Newmark. (2025, February). *2025 U.S. Data Center Market Outlook*. https://www.nmrk.com/insights/market-report/2025-us-data-center-market-outlook
- Synergy Research Group. (2025). *Hyperscale Data Center Count Hits 1,136*. https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity
- Synergy Research Group. (2026). *Hyperscale Operators to Account for 67% of all Data Center Capacity by 2031*. https://www.srgresearch.com/articles/hyperscale-operators-to-account-for-67-of-all-data-center-capacity-by-2031
- DC Byte. (2025). *2025 Global Data Centre Index*. https://www.dcbyte.com/global-data-centre-index/2025-global-data-centre-index/
- DC Byte. (2026). *2026 Data Centre Outlook: The Top Five Trends*. https://www.dcbyte.com/news-blogs/2026-data-centre-outlook-top-five-trends/
- datacenterHawk. (2025). *3Q 2025 Data Center Market Recap*. https://datacenterhawk.com/resources/market-insights/3q-2025-data-center-market-recap
- datacenterHawk. (2026). *Behind-the-Meter Power Solutions: The Data Center Industry's New Reality*. https://datacenterhawk.com/resources/market-insights/behind-the-meter-power-solutions-the-data-center-industry-s-new-reality
- Avison Young. (2025). *US Data Center Update Q2 2025*. https://www.avisonyoung.us/documents/d/us/q2-2025-us-data-center-update
- IEEFA. (2025). *Projected data center growth spurs PJM capacity prices by factor of 10*. https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
- Wood Mackenzie. (2026). *Reality bytes: the US data centre pipeline additions halved in Q4 2025*. https://www.woodmac.com/news/opinion/reality-bytes-the-us-data-centre-pipeline-additions-halved-in-q4-2025-compared-to-the-previous-quarter/

### Tier 3 — Project-level reporting

- Crusoe. (2025, September 30). *Crusoe announces flagship Abilene data center is live*. https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
- Data Center Dynamics. (2026). *Crusoe tops out final building at OpenAI Stargate data center campus in Abilene, Texas*. https://www.datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas/
- CNBC. (2025, September 23). *OpenAI's first data center in $500 billion Stargate project is open in Texas*. https://www.cnbc.com/2025/09/23/openai-first-data-center-in-500-billion-stargate-project-up-in-texas.html
- Epoch AI. (2026, April 17). *OpenAI Stargate: where the US sites stand*. https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand
- OpenAI. (2025, September). *OpenAI, Oracle, and SoftBank expand Stargate with five new AI data center sites*. https://openai.com/index/five-new-stargate-sites/
- Meta. (n.d.). *Richland Parish Data Center*. https://datacenters.atmeta.com/richland-parish-data-center/
- Meta. (2025, October). *Hello, El Paso!*. https://datacenters.atmeta.com/2025/10/hello-el-paso/
- Meta. (2025, December). *One Year In: Meta's Richland Parish Data Center Supports Louisiana Economy With $875M In Contracts*. https://about.fb.com/news/2025/12/metas-richland-parish-data-center-supports-louisiana-economy-875-million-in-contracts/
- Engineering News-Record. (2026). *$27B Meta Data Center Pushes Louisiana Toward Massive Power Expansion*. https://www.enr.com/articles/62766-27b-meta-data-center-pushes-louisiana-toward-massive-power-expansion
- Data Center Dynamics. (2026). *Entergy obtains approval to construct three gas facilities to serve Meta's 2GW data center in Louisiana*. https://www.datacenterdynamics.com/en/news/entergy-obtains-approval-to-construct-three-gas-facilities-to-serve-metas-2gw-data-center-in-louisiana/
- Data Center Dynamics. (2026). *Entergy to build $1.2bn 500kV transmission line to serve Meta mega data center*. https://www.datacenterdynamics.com/en/news/entergy-to-build-12bn-500kv-transmission-line-to-serve-meta-mega-data-center-in-louisiana/
- CNBC. (2025, October 29). *Amazon opens $11 billion AI data center Project Rainier in Indiana*. https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html
- Converge Digest. (2025). *AWS Activates Project Rainier Data Center Campus*. https://convergedigest.com/aws-activates-project-rainier-data-center-campus/
- Utility Dive. (2024). *Talen to sell Amazon 1.9 GW from Susquehanna nuclear plant*. https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/
- Talen Energy. (2025, June 11). *Talen Energy Expands Nuclear Energy Relationship with Amazon*. https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-expands-nuclear-energy-relationship-amazon
- World Nuclear News. (2025). *New supply agreement expands Talen-Amazon partnership*. https://www.world-nuclear-news.org/articles/new-supply-agreement-expands-talen-amazon-partnership
- Constellation Energy. (2025, September). *One Year Later: Crane Clean Energy Center Still in the Spotlight and Ahead of Schedule*. https://www.constellationenergy.com/newsroom/2025/09/one-year-later-crane-clean-energy-center-still-in-the-spotlight-and-ahead-of-schedule.html
- World Nuclear News. (2025). *Constellation seeks regulator's help for 2027 plant restart*. https://www.world-nuclear-news.org/articles/constellation-seeks-regulators-help-for-2027-plant-restart
- ANS. (2025, October 28). *NextEra and Google ink a deal to restart Duane Arnold*. https://www.ans.org/news/2025-10-28/article-7501/nextera-and-google-ink-a-deal-to-restart-duane-arnold/
- Power Magazine. (2025). *Palisades Nuclear Plant Moved to Operations Status, Ready to Receive Fuel*. https://www.powermag.com/palisades-nuclear-plant-moved-to-operations-status-ready-to-receive-fuel/
- Neutron Bytes. (2026, January 11). *Holtec Submits License Application to NRC for the Palisades Twin SMR-300s*. https://neutronbytes.com/2026/01/11/holtec-submits-license-application-to-nrc-for-the-palisades-twin-smr-300s/
- SemiAnalysis. (2025). *xAI's Colossus 2 — First Gigawatt Datacenter In The World*. https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter
- Data Center Dynamics. (2026). *Elon Musk's xAI gets go-ahead for 41 natural gas turbines in Mississippi*. https://www.datacenterdynamics.com/en/news/musks-xai-gets-go-ahead-for-41-natural-gas-turbines-in-mississippi-to-power-colossus-data-centers/
- Earthjustice. (2025). *Illegal Pollution from Data Center Power Plants Shouldn't Harm Our Communities. We're Suing xAI*. https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus
- SELC. (2025). *xAI built an illegal power plant to power its data center*. https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/
- Data Center Dynamics. (2025). *Vantage breaks ground on Texas gigawatt data center campus for OpenAI*. https://www.datacenterdynamics.com/en/news/vantage-breaks-ground-on-texas-gigawatt-data-center-campus-for-openai/
- Vantage Data Centers. (2025). *Vantage Data Centers Unveils Plans for "Frontier"*. https://vantage-dc.com/news/vantage-data-centers-unveils-plans-for-frontier-a-25b-mega-campus-in-texas-to-meet-unprecedented-ai-demand/
- Construction Owners. (2025). *Oracle and OpenAI's New Off-Grid Data Center in Texas to Run on 700MW Natural Gas Microgrid*. https://www.constructionowners.com/news/oracle-and-openai-to-power-new-texas-data-center-off-the-grid
- Data Center Frontier. (2025). *Vantage Data Centers Pours $15B Into Wisconsin AI Campus*. https://www.datacenterfrontier.com/hyperscale/article/55326357/vantage-data-centers-pours-15b-into-wisconsin-ai-campus-as-it-builds-global-giga-scale-footprint
- CNBC. (2026, January 26). *Microsoft's plans for 15 more data centers win approval at former Wisconsin Foxconn site*. https://www.cnbc.com/2026/01/26/microsoft-wins-approval-for-15-data-centers-at-wisconsin-foxconn-site.html
- Data Center Dynamics. (2026). *Microsoft given greenlight for 15 more data center buildings in Mount Pleasant, Wisconsin*. https://www.datacenterdynamics.com/en/news/microsoft-given-greenlight-for-15-more-data-center-buildings-in-mount-pleasant-wisconsin/
- OPB. (2026, January 17). *A small town in Central Washington is Microsoft's answer to the data center backlash*. https://www.opb.org/article/2026/01/17/quincy-washington-microsoft-data-center/
- Data Center Frontier. (2025). *Details Emerge On Microsoft's $1.8 Billion Investment In Atlanta Data Centers*. https://www.datacenterfrontier.com/hyperscale/article/55126626/details-emerge-on-microsofts-18-billion-investment-in-atlanta-data-centers-amid-tax-development-wrangles
- Data Center Dynamics. (2026). *Sailfish plans multi-gigawatt data center park outside DFW, Texas*. https://www.datacenterdynamics.com/en/news/sailfish-plans-multi-gigawatt-data-center-park-outside-dfw-texas/
- Data Center Dynamics. (2026). *Crusoe gets go-ahead for 1.8GW data center campus and power plant in Cheyenne, Wyoming*. https://www.datacenterdynamics.com/en/news/crusoe-gets-go-ahead-for-18gw-data-center-campus-and-power-plant-in-cheyenne-wyoming/
- Power Magazine. (2026). *Wyoming Approves Data Center Campus That Includes 2.7 GW of New Natural Gas-Fired Generation*. https://www.powermag.com/wyoming-approves-data-center-campus-that-includes-2-7-gw-of-new-natural-gas-fired-generation/
- Data Center Dynamics. (2025). *Stack joins multi-billion-dollar data center & microgrid project in New Mexico*. https://www.datacenterdynamics.com/en/news/stack-joins-multi-billion-dollar-data-center-microgrid-project-in-new-mexico/
- Source NM. (2026, April 27). *NM Project Jupiter data center developers announce new plans for generating power*. https://sourcenm.com/2026/04/27/nm-project-jupiter-data-center-developers-announce-new-plans-for-generating-power/
- Anthropic. (2025, November 12). *Anthropic invests $50 billion in American AI infrastructure*. https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure
- CNBC. (2025, November 12). *Anthropic to spend $50 billion on U.S. AI infrastructure*. https://www.cnbc.com/2025/11/12/anthropic-ai-data-centers-texas-new-york.html
- Texas Tribune. (2026, January 26). *Plan to run El Paso data center on natural gas sparks concern*. https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/
- Bisnow. (2025). *Blackstone's QTS Files Appeal To Save Massive Virginia Data Center Campus*. https://www.bisnow.com/washington-dc/news/data-center-development/blackstones-qts-appeals-court-decision-blocking-huge-virginia-project-134390
- Data Center Dynamics. (2026). *EdgeConneX files to convert warehouse and build new 700,000 sq ft data center in New Albany, Ohio*. https://www.datacenterdynamics.com/en/news/edgeconnex-files-to-convert-warehouse-and-build-new-700000-sq-ft-data-center-in-new-albany-ohio/
- Utility Dive. (2026). *ERCOT's large load queue jumped almost 300% last year*. https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/
- Utility Dive. (2025). *Gas continues to dominate Entergy plans as data center pipeline grows*. https://www.utilitydive.com/news/gas-continues-to-dominate-entergy-plans-as-data-center-pipeline-grows/804521/
- The Center Square. (2026). *Entergy seeks more big projects in 2026 as Louisiana load surges*. https://www.thecentersquare.com/louisiana/article_7675e48d-c161-49a6-9e42-0f18ed188cc6.html
- Carbon Credits. (2026). *Meta Signs Three Nuclear Deals of Up to 6.6 GW to Fuel AI Data Center Growth*. https://carboncredits.com/meta-signs-three-nuclear-deals-of-up-to-6-6-gw-to-fuel-ai-data-center-growth/
- Amazon. (2024). *Amazon signs agreements for innovative nuclear energy projects*. https://www.aboutamazon.com/news/sustainability/amazon-nuclear-small-modular-reactor-net-carbon-zero
- Virginia Business. (2025). *Equinix wants to build another large data center in Loudoun County*. http://www.virginiabusiness.com/news/article/equinix-wants-to-build-another-large-data-center-in-loudoun-county
- Fortune. (2026, May 6). *A Michigan farm town voted down plans for a giant OpenAI-Oracle data center. Weeks later, construction began*. https://fortune.com/2026/05/06/ai-data-center-michigan-saline-politics-farmland/
- Related Companies. (2025, October 30). *OpenAI, Oracle and Related Digital announce Stargate data center site in Michigan*. https://www.related.com/press-releases/2025-10-30/openai-oracle-and-related-digital-announce-stargate-data-center-site
- Microsoft Local. (n.d.). *Palmetto datacenter construction update*. https://local.microsoft.com/blog/palmetto-datacenter-construction-update/

### Limitations and caveats

- CBRE, Cushman & Wakefield, JLL and Newmark publications are partly paywalled or aggregated; numerical extracts above are taken from publicly summarised press releases, secondary news coverage, and the publicly accessible chapter pages.
- DC Byte and datacenterHawk full datasets are subscription-only; their headline figures here come from publicly issued summary reports and trade press citation.
- Several "MW" figures for hyperscaler-owned campuses (xAI, Meta, AWS, Microsoft) are estimates from satellite imagery, county filings, generator permits and gas-turbine permits because the operators do not publish IT load directly.
- For projects where construction was confirmed via single-source reporting, I have flagged "medium" or "low" confidence above; do not cite a single trade-press item as evidence of vertical construction without corroboration.
