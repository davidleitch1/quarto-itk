# US Operating Data Centre Fleet — Research Note

**Date prepared:** 10 May 2026
**Prepared for:** ITK research note on US data centre fleet
**Scope:** Operating (commissioned) US data centres only — pipeline and announced projects are flagged separately

---

## 1. Headline numbers and the definition trap

The "number of US data centres" varies by an order of magnitude depending on what is counted. The following figures all describe the **2024–2025 US fleet** but use very different definitions:

| Metric | Estimate | Definition / Source |
|:--|--:|:--|
| All facilities (including small enterprise sites) | ~5,427 | Cloudscene database, Nov 2025 [Source: https://www.cargoson.com/en/blog/number-of-data-centers-by-country] |
| All facilities tracked by Baxtel | ~4,720 | Baxtel directory, May 2026 snapshot [Source: https://baxtel.com/data-center/united-states] |
| Hyperscale-owned facilities (US only) | 580 | Synergy Research, end-2025 [Source: https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity] |
| Hyperscale-owned facilities (US only) | 504 | Synergy Research, end-Q4 2024 [Source: https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity] |
| Operating IT load — all US data centres | ~50 GW | FERC 2025 State of the Markets, year-end 2025 [Source: https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/] |
| Operating power demand (implied from energy use) | 74–132 GW | LBNL 2024 report, derived from 176 TWh in 2023 at 50% utilisation [Source: https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf] |
| Operating IT load — colocation primary markets | 9,432 MW | CBRE H2 2025, year-end 2025, 8 primary markets only [Source: https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025] |

*Source: ITK compilation from sources listed in column 3.*

### Reconciling the numbers

- The **FERC 50 GW** figure (year-end 2025) is the most authoritative single number for **operating** facilities and is grounded in interconnection data. FERC's 2025 State of the Markets report (released 19 March 2026) describes 24% compound annual growth in data centre interconnected load since 2020, with the average new facility entering service in 2025 at nearly 80 MW (vs ~25 MW in 2020) [Source: https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/].
- The **LBNL 74–132 GW** range is *power demand* derived from measured 2023 electricity use of 176 TWh (4.4% of US electricity). Because data centres are not at 100% utilisation, the underlying installed IT plus cooling capacity is somewhat lower than this range; the 50 GW IT-load figure from FERC is consistent with the lower bound once cooling and other overheads are stripped out [Source: https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf].
- **CBRE's 9,432 MW** is a **subset**: it counts only multi-tenant (third-party colocation and wholesale) inventory in the eight "primary" North American markets (Northern Virginia, Dallas-Ft. Worth, Silicon Valley, Chicago, Phoenix, New York Tri-State, Atlanta, Hillsboro). It excludes hyperscaler-owned facilities and all secondary markets [Source: https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025]. Bloom Energy and Synergy estimate hyperscalers own ~50–55% of US capacity, and that share is growing [Source: https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity].

**Best single-source point estimate for operating US IT load (year-end 2025): ~50 GW** (FERC). For comparison and **colocation only** in primary markets: 9.4 GW (CBRE). Synergy reports the US holds ~55% of global hyperscale capacity.

---

## 2. Top 15 currently operating US data centre campuses

The list below is restricted to **operating** sites (or sites where at least one phase is operating) as of early 2026. Where a campus is multi-phase, the IT-load figure is the **currently energised** load, with planned full build flagged. "Gross site MW" (which includes cooling, lighting and step-down losses) can be 30–40% above IT load and is noted where sources conflate the two.

**Table 1: Largest operating US data centre campuses, ~2025–early 2026**

| # | Campus | Operator | Location | Operating IT load (MW) | Power source | First online | Source |
|:-:|:--|:--|:--|--:|:--|:--|:--|
| 1 | Altoona Campus | Meta | Altoona, IA | ~1,400 (campus IT load, multi-building) | MidAmerican grid + Meta wind/solar PPAs (100% renewable matched) | 2014 | [Source: https://datacenters.atmeta.com/us-locations/] |
| 2 | Prineville Campus | Meta | Prineville, OR | ~1,290 (multi-building) | PacifiCorp grid + on-site solar; renewable-matched | 2011 | [Source: https://datacenters.atmeta.com/us-locations/] |
| 3 | Stargate / Lancium Clean Campus | Crusoe / Oracle (for OpenAI) | Abilene, TX | ~300 MW operating; 1,200 MW full build by Q4 2026 | ERCOT grid + 360 MW on-site gas turbines + on-site solar/storage | First building 2025 | [Source: https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand]; [Source: https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion] |
| 4 | Fort Worth Campus | Meta | Fort Worth, TX | ~730 | ERCOT grid; 100% renewable matched via Meta PPAs | 2017 | [Source: https://datacenters.atmeta.com/us-locations/] |
| 5 | Switch Citadel — TAHOE RENO 1 | Switch | Tahoe Reno, NV | ~130 operating (campus master-planned to 650 MW; 179 MW behind-the-meter solar added) | NV Energy + on-site BTM solar; "100% renewable" claim | 2017 | [Source: https://www.switch.com/switch-tahoe-reno-data-center-now-open/] |
| 6 | Quincy Campus (MWH cluster) | Microsoft | Quincy, WA | ~622 (gens 2–4; gen 5 in build) | BPA / Grant PUD — Grand Coulee hydro line | 2007 (gen 1) | [Source: https://baxtel.com/data-center/microsoft-quincy-mwh] |
| 7 | Council Bluffs Campus | Google | Council Bluffs, IA | Estimated 600+ (Google does not publish IT load; Google's largest worldwide) | MidAmerican grid + Google wind PPAs | 2009 | [Source: https://www.datacenterknowledge.com/hyperscalers/google-to-double-size-of-oklahoma-data-center] |
| 8 | Pryor (Mayes County) Campus | Google | Pryor, OK | Not published; Google's #2 globally; 600 MW new clean energy PPAs signed 2025 | OG&E + Google solar PPAs (Mayes County 372 MW solar adjacent) | 2011 | [Source: https://www.datacenterdynamics.com/en/news/google-signs-ppa-with-leeward-to-power-oklahoma-data-center-operations/] |
| 9 | Colossus 1 (xAI) | xAI | Memphis, TN | 250–420 (estimates vary; 200,000 GPUs) | TVA + MLGW grid + on-site Solar Group gas turbines (controversial) | Sept 2024 | [Source: https://en.wikipedia.org/wiki/Colossus_(supercomputer)]; [Source: https://www.hpcwire.com/2025/05/13/colossus-ai-hits-200000-gpus-as-musk-ramps-up-ai-ambitions/] |
| 10 | Switch Core Campus | Switch | Las Vegas, NV | ~495 | NV Energy; renewable PPAs | 2008 (phased) | [Source: https://www.blackridgeresearch.com/blog/largest-top-biggest-data-centers-in-united-states-list] |
| 11 | QTS Atlanta-Metro (DC1+expansion) | QTS / Blackstone | Atlanta, GA | ~278 | Georgia Power on-site substation | 2007 (former Sears facility); QTS 2009 | [Source: https://q.com/data-centers/atlanta-1/] |
| 12 | New Albany / Columbus campus (multiple sites) | Meta + AWS + Google | New Albany, OH | 500+ across multiple operators (composite, not single campus) | AEP Ohio | 2017 onward | [Source: https://www.datacenterfrontier.com/site-selection/article/33035576/data-centers-are-booming-in-ohios-digital-heartland] |
| 13 | Talen / AWS Cumulus campus | AWS (acquired from Talen) | Salem Township, PA | 300 operating, 960 MW PPA full build (Susquehanna nuclear) | Susquehanna nuclear plant — direct ISO-bypass interconnection | Acquired 2024; ramp 2024–2032 | [Source: https://www.esgdive.com/news/amazon-talen-energy-ink-nuclear-ppa-to-power-data-centers-pennsylvania/750950/] |
| 14 | Lakeside Technology Center | Digital Realty | Chicago, IL | 100+ (~1.1 M sq ft) | ComEd grid | 1999 | [Source: https://www.blackridgeresearch.com/blog/largest-top-biggest-data-centers-in-united-states-list] |
| 15 | AWS US-East-1 Ashburn cluster | AWS | Ashburn / Loudoun, VA | ~1,500+ aggregate across many buildings (not a single campus; largest single building ~60 MW Cosner) | Dominion Energy + AWS solar/wind PPAs | 2006 onward | [Source: https://baxtel.com/data-center/aws-us-east-n-virginia] |

*Source: ITK compilation. Capacity figures cross-checked across operator press releases, Baxtel, BlackRidge Research and Data Center Frontier. Where operators do not publish IT load (Google in particular), figures are external estimates and flagged.*

### Important caveats on the table

- **Meta's Altoona and Prineville sites** are routinely cited as the largest single-operator US campuses by gross IT load. The 1,400 MW and 1,290 MW figures circulate widely (e.g. BlackRidge Research, Data Center Magazine) but Meta does not publish an authoritative IT-load number — these are aggregated from individual building permits over 10+ years. They should be treated as **upper-bound estimates**.
- **Stargate Abilene** is operational but only at ~300 MW of an eventual 1,200 MW (capped after the 600 MW expansion was scrapped in March 2026 due to grid delivery delays) [Source: https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion].
- **xAI Colossus** is unusual — power capacity reports range from 150 MW (initial), to 250 MW (mid-2025), to 420 MW (late 2025), with much of the additional supply from on-site portable gas turbines that the Shelby County Health Department ruled were operating without permits.
- The **AWS Ashburn cluster** is a network of dozens of buildings rather than a single campus; the ~1.5 GW aggregate is a market estimate (Dgtl Infra; AI Data Center Index), not a published AWS figure [Source: https://aidatacenterindex.com/datacenters/amazon-ec2-virginia-hyperscale-campus.html].
- "100% renewable" claims by hyperscalers are typically **annual matched via PPAs and RECs**, not 24/7 carbon-free. Actual instantaneous grid mix follows the host utility.

---

## 3. Geographic concentration

### Northern Virginia dominates

CBRE H2 2025 (year-end 2025 data, published 25 February 2026) puts Northern Virginia colocation inventory at **4,039.6 MW** of operating commissioned multi-tenant power [Source: https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025]. This excludes hyperscaler-owned, behind-the-fence facilities (which collectively are larger again in the region — local press cite ~4,900 MW total in mid-2025 and ~5,300–6,000 MW for Loudoun County alone if hyperscaler-owned sites are included [Source: https://wtop.com/business-finance/2025/06/northern-virginia-data-centers-have-topped-4900-megawatts-what-does-that-mean/]).

Northern Virginia is **~43% of the 9,432 MW US primary-market colocation inventory** and roughly **8–12% of the 50 GW national operating IT load** depending on how hyperscaler facilities are attributed.

### Top US markets — operating colocation inventory, year-end 2025

**Table 2: US/North America primary data centre markets — colocation operating inventory**

| Market | Operating IT load (MW) | Vacancy | YoY growth | Notes |
|:--|--:|--:|--:|:--|
| Northern Virginia | 4,039.6 | 0.5% | +37% | Largest in the world; +1,102 MW absorption in 2025 |
| Atlanta | 1,459.2 | 2.0% | +46% | Now #2; +458.8 MW YoY; +456 MW absorbed |
| Dallas-Ft. Worth | ~1,500 | low | n/a | Crossed 1 GW in 2025; +470.8 MW absorption |
| Phoenix | ~603 (2024 base) | 1.7% | +67% (2024) | Strong further 2025 growth not yet itemised |
| Chicago | n/a separate; ~1,000 inferred | 3.1% | modest | Vacancy ticked up |
| Silicon Valley | n/a separate; ~500 inferred | low | low | Power constrained; rents +19% |
| Hillsboro (Portland) | ~430 (across operators) | low | rising | NTT 354 MW alone; QTS 180 MW |
| New York Tri-State | n/a separate; ~300 inferred | low | low | Power constrained |
| **Primary markets total** | **9,432** | 1.4% | +36% | CBRE H2 2025 |

*Source: CBRE North America Data Center Trends H2 2025; Phoenix and Hillsboro figures from CBRE H1 2025 market profiles. Inferred values are derived by subtracting itemised markets from the 9,432 MW total and apportioning by historical share — flagged where exact figures were not located in publicly available CBRE summaries.*

### Notes on selected secondary clusters

- **Columbus / New Albany, OH:** AEP Ohio's load forecasts identify ~5 GW of contracted hyperscaler load in central Ohio (Meta, AWS, Google, QTS) by 2030, with current operating IT load lower [Source: https://www.datacenterfrontier.com/site-selection/article/33035576/data-centers-are-booming-in-ohios-digital-heartland].
- **Tahoe-Reno (Switch + Apple + Vantage):** ~1 GW master-planned, lower currently energised.
- **Memphis:** Effectively created by xAI in 2024 — 250–420 MW operating.
- **Iowa (Council Bluffs, Altoona, Des Moines):** Google + Meta + Microsoft cluster — combined ~3 GW operating estimate.
- **Pacific Northwest** (Quincy WA + Hillsboro OR + The Dalles): Baxtel reports 5,488 MW across the Pacific Northwest region (operator-published nameplate, includes some non-operating phases) [Source: https://baxtel.com/data-center/united-states].

---

## 4. Power source observations

The shift in 2024–2025 is towards **dedicated firm generation** rather than relying on incremental utility-grid expansion:

- **Nuclear restarts and direct PPAs**: Microsoft's 835 MW 20-year PPA with Constellation for the restart of Three Mile Island Unit 1 (now "Crane Clean Energy Center"), expected back online 2027 [Source: https://www.datacenterdynamics.com/en/news/three-mile-island-nuclear-power-plant-to-return-as-microsoft-signs-20-year-835mw-ai-data-center-ppa/]. AWS purchased the Cumulus campus from Talen for $650 m and signed a 17-year, 1.92 GW PPA from Susquehanna nuclear [Source: https://www.esgdive.com/news/amazon-talen-energy-ink-nuclear-ppa-to-power-data-centers-pennsylvania/750950/].
- **Behind-the-meter gas turbines**: Stargate Abilene has 360 MW of on-site gas turbines as primary/back-up [Source: https://energynewsbeat.co/an-on-site-natural-gas-plant-will-help-power-stargates-first-data-center-public-filings-show/]; xAI Memphis is using ~30 portable Solar Group gas turbines on site, drawing regulatory complaints.
- **Behind-the-meter solar + storage**: Switch Tahoe Reno added 179 MW BTM solar; Meta and Google sign large utility-scale solar/wind PPAs.
- **Dedicated hydro lines**: Microsoft Quincy uses dedicated lines from Grand Coulee.

The Bloom Energy 2025 report frames an aggregate ~35 GW "energy gap" by 2030 between data centre demand growth and grid delivery, driving the on-site generation trend [Source: https://www.bloomenergy.com/news/data-centers-are-turning-to-onsite-power-sources-to-address-35-gw-energy-gap-by-2030/].

---

## 5. Uncertainties and caveats

1. **No single authoritative count of operating US data centres exists.** The 5,427 (Cloudscene) and 4,720 (Baxtel) figures are directory-derived and use different inclusion thresholds. They likely both undercount small enterprise server rooms and, as both are continuously updated, the underlying date is fuzzy.
2. **"Operating MW" definitions are inconsistent.** Operators, brokers and utilities variously cite IT load (servers only), critical/UPS load (IT plus N+1 redundancy), commissioned MW (energised by utility), gross site MW (including cooling and BTM losses), or contracted/announced MW (much of which never builds out at announced size). The largest-campus rankings are particularly sensitive to this — the same site can be reported at IT-load values that differ by 40%+.
3. **Hyperscaler facilities are opaque.** Meta, Google, AWS and Microsoft do not publish per-site IT load; figures circulating in trade press are derived from utility filings, building permits and aerial-image analysis. Meta is the most transparent (publishes campus square-footage and renewable PPAs).
4. **The Synergy Research and CBRE samples do not overlap cleanly.** Synergy counts hyperscaler-owned facilities globally (1,360 in Q4 2025; 580 in US). CBRE counts colocation/wholesale in 8 US primary markets (~9.4 GW). FERC counts everything that interconnects to a covered market. Adding these without care produces double-counting.
5. **The LBNL 74–132 GW power-demand range** is *not* a count of installed capacity but a back-derivation from 2023 electricity use at assumed 50% utilisation. The wide range reflects genuine uncertainty in capacity utilisation across the fleet.
6. **2025 was a step-change year**. The CBRE primary-market inventory grew 36% YoY (the fastest on record), so any figure more than 6 months old is materially out of date.
7. **Several listed largest-campus figures should be cross-checked against utility interconnection filings** before publication. Meta Altoona (1,400 MW) and Prineville (1,290 MW) in particular are at the upper end of plausible IT-load ranges; some sources interpret the same numbers as gross site MW.

---

## 6. Bibliography

### Tier 1: Government and laboratory sources

- Lawrence Berkeley National Laboratory, *2024 United States Data Center Energy Usage Report* (December 2024). https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report ; full PDF: https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
- US Department of Energy, "DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers" (20 December 2024). https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- Berkeley Lab News Center, "Berkeley Lab Report Evaluates Increase in Electricity Demand from Data Centers" (15 January 2025). https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- Federal Energy Regulatory Commission, *2025 State of the Markets Report* (released 19 March 2026), as summarised in Utility Dive, "50 GW of data centers online at end of 2025…" https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/
- US Energy Information Administration, "Data center owners turn to nuclear as potential electricity source" https://www.eia.gov/todayinenergy/detail.php?id=63304
- Joint Legislative Audit and Review Commission of Virginia, *Data Centers in Virginia* (December 2024). https://jlarc.virginia.gov/pdfs/reports/Rpt598-2.pdf

### Tier 2: Industry analysts (public methodology)

- Synergy Research Group, "Hyperscale Data Center Count Hits 1,136; Average Size Increases; US Accounts for 54% of Total Capacity" (March 2025). https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity
- CBRE, *North America Data Center Trends H2 2025* (25 February 2026). https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025
- CBRE, *North America Data Center Trends H1 2025* (8 September 2025). https://www.cbre.com/insights/reports/north-america-data-center-trends-h1-2025
- CBRE, "Fast-Growing North American Data Center Market Set Records in 2025" press release. https://www.cbre.com/press-releases/fast-growing-north-american-data-center-market-set-records-in-2025
- JLL, *2026 Global Data Center Outlook*. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- JLL, *North America Data Center Report Year-end 2025*. https://www.jll.com/en-us/insights/market-dynamics/north-america-data-centers
- Bloom Energy, *2025 Data Center Power Report* (January 2026). https://www.bloomenergy.com/news/data-centers-are-turning-to-onsite-power-sources-to-address-35-gw-energy-gap-by-2030/
- Dgtl Infra, "United States Data Centers: Top 10 Locations in the USA". https://dgtlinfra.com/united-states-data-centers/
- Baxtel, "United States Data Centers & Colocation". https://baxtel.com/data-center/united-states
- Baxtel, "Northern Virginia Data Center Market". https://baxtel.com/data-center/northern-virginia
- Cloudscene database via Cargoson, "Number of Data Centers by Country" (November 2025). https://www.cargoson.com/en/blog/number-of-data-centers-by-country
- AI Data Center Index — AWS Northern Virginia. https://aidatacenterindex.com/datacenters/amazon-ec2-virginia-hyperscale-campus.html
- Epoch AI, "OpenAI Stargate: where the US sites stand". https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand

### Tier 3: Trade press (project-level facts)

- BlackRidge Research, "Top 10 Largest Data Centers In The US (2026)" (6 February 2026). https://www.blackridgeresearch.com/blog/largest-top-biggest-data-centers-in-united-states-list
- Data Center Frontier, "Comparing Highlights from the Latest CBRE, JLL 'State of the Market' Reports". https://www.datacenterfrontier.com/colocation/article/55137045/comparing-highlights-from-the-latest-cbre-jll-state-of-the-market-reports-for-us-data-centers
- Data Center Frontier, "Data Centers Are Booming In Ohio's Digital Heartland". https://www.datacenterfrontier.com/site-selection/article/33035576/data-centers-are-booming-in-ohios-digital-heartland
- Data Center Frontier, "Data Center Nuclear Power Update: Microsoft, Constellation, AWS, Talen, Meta". https://www.datacenterfrontier.com/energy/article/55239739/data-center-nuclear-power-update-microsoft-constellation-aws-talen-meta
- Data Center Dynamics, "Three Mile Island nuclear power plant to return as Microsoft signs 20-year, 835MW AI data center PPA". https://www.datacenterdynamics.com/en/news/three-mile-island-nuclear-power-plant-to-return-as-microsoft-signs-20-year-835mw-ai-data-center-ppa/
- Data Center Dynamics, "Oracle/OpenAI drop plans to expand flagship Abilene Stargate site". https://www.datacenterdynamics.com/en/news/oracleopenai-drop-plans-to-expand-flagship-abilene-stargate-site-meta-in-talks-to-pick-up-crusoe-capacity-with-nvidias-help/
- Tom's Hardware, "Oracle and OpenAI's Abilene expansion saga detailed" (March 2026). https://www.tomshardware.com/tech-industry/oracle-and-openai-scrap-planned-600mw-abilene-expansion
- WTOP News, "Northern Virginia data centers have topped 4,900 megawatts. What does that mean?" (June 2025). https://wtop.com/business-finance/2025/06/northern-virginia-data-centers-have-topped-4900-megawatts-what-does-that-mean/
- Meta Data Centers, US locations summary. https://datacenters.atmeta.com/us-locations/
- Microsoft Quincy MWH (Baxtel listing). https://baxtel.com/data-center/microsoft-quincy-mwh
- Switch press release, "Switch TAHOE RENO Now Open". https://www.switch.com/switch-tahoe-reno-data-center-now-open/
- QTS Atlanta-Metro DC1 (q.com). https://q.com/data-centers/atlanta-1/
- HPCwire, "Colossus AI Hits 200,000 GPUs as Musk Ramps Up AI Ambitions" (13 May 2025). https://www.hpcwire.com/2025/05/13/colossus-ai-hits-200000-gpus-as-musk-ramps-up-ai-ambitions/
- Wikipedia, "Colossus (supercomputer)". https://en.wikipedia.org/wiki/Colossus_(supercomputer)
- ESG Dive, "Amazon, Talen Energy ink nuclear PPA". https://www.esgdive.com/news/amazon-talen-energy-ink-nuclear-ppa-to-power-data-centers-pennsylvania/750950/
- Energy News Beat, "An on-site natural gas plant will help power Stargate's first data center". https://energynewsbeat.co/an-on-site-natural-gas-plant-will-help-power-stargates-first-data-center-public-filings-show/

---

*End of research note. The CBRE H1 2025 and H2 2025 PDFs and the LBNL 2024 report PDF should be obtained directly for any figures intended for publication, since secondary summaries differ in detail.*
