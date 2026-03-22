---
title: "Utility-Scale Battery Storage: Pricing, Cell Formats, and Market Structure in 2025–26"
date: 2026-03-19
bibliography: battery_storage_pricing_references.bib
---

# Utility-Scale Battery Storage: Pricing, Cell Formats, and Market Structure in 2025–26

## Summary

Utility-scale battery energy storage system (BESS) costs have fallen roughly 70% since their 2022 peak, reaching a global weighted-average turnkey price of \$117/kWh in 2025 [@volta-battery-report-2025; @ess-news-volta-2026]. Three reinforcing trends — larger cell formats (500 Ah+), higher-density containerised systems (5–10 MWh), and fierce Chinese manufacturing competition — continue to push system-level costs down even as upstream lithium carbonate prices have ticked upward. The removal of China's VAT export rebate (phased to zero by January 2027) and firming lithium prices create real but manageable upward pressure. The structural conditions that drove the 2022 price shock are absent: contracts now index key inputs, ESS commands 20–25% of global battery demand, and sodium-ion is emerging as a credible alternative chemistry [@kubik-linkedin-pricing-2026].

---

## 1. Pricing Trends

### 1.1 Current Cost Stack

The cost of a utility-scale BESS can be decomposed into three layers: cells, core equipment (cells + enclosure + power conversion + thermal management), and all-in turnkey (adding EPC, grid connection, and soft costs).

: Utility-Scale BESS Cost Stack, 2025 {#tbl-cost-stack}

| Cost Layer | Global Average | China | Saudi Arabia | Europe | United States |
|------------|---------------:|------:|-----------:|-------:|--------------:|
| Cell (LFP, ex-works) | — | $40/kWh | — | — | — |
| Pack (stationary) | $70/kWh | — | — | — | — |
| Core equipment (ex-China) | $75/kWh | — | $73–75/kWh | — | — |
| Turnkey system (4h) | $117/kWh | $63–73/kWh | $120/kWh | $177–275/kWh | $236/kWh |

: Source: BNEF [@bnef-battery-prices-2025; @energy-storage-news-bnef-2025], Ember [@ember-battery-storage-2025], Volta [@volta-battery-report-2025]. Saudi figures from August 2025 tenders deploying 1,175 Ah cells in 6.25 MWh containers.

Stationary storage pack prices at \$70/kWh are the lowest of any battery market segment, reflecting the dominance of cost-optimised LFP chemistry and the scale efficiencies of large-format cells [@energy-storage-news-bnef-2025].

The gap between Chinese domestic pricing (\$63–73/kWh) and Western markets (\$177–275/kWh in Europe, \$236/kWh in the US) reflects tariffs, local content requirements, labour costs, permitting complexity, and grid connection fees rather than fundamental technology differences [@ember-battery-storage-2025]. Installation and grid connection alone add approximately \$50/kWh in most markets outside China, and can reach \$100/kWh in high-cost jurisdictions.

### 1.2 Historical Trajectory

: BESS Turnkey System Price Trajectory {#tbl-price-trajectory}

| Year | Approximate Global Average | Year-on-Year Change |
|------|---------------------------:|--------------------:|
| 2022 | ~$390/kWh | — |
| 2023 | ~$280/kWh | −28% |
| 2024 | ~$169/kWh | −40% |
| 2025 | $117/kWh | −31% |

: Source: Volta [@volta-battery-report-2025], BNEF [@bnef-battery-prices-2025]. 2022–2023 figures are approximate, rounded from various industry estimates.

The 2024 decline of 40% was the steepest single-year drop on record. The 2025 decline of 31% is slower in percentage terms but represents continued rapid cost reduction. Since the 2022 peak, cumulative reductions approach 70% [@ess-news-volta-2026].

### 1.3 Forward Projections

BNEF projects continued declines, though the rate of fall is expected to moderate:

: BNEF 2035 BESS System Price Projections (4-hour duration) {#tbl-forward-projections}

| Region | 2025 Actual | 2035 Projection | Implied Decline |
|--------|------------:|----------------:|----------------:|
| China | $63–73/kWh | $41/kWh | ~37–44% |
| Europe | $177–275/kWh | $101/kWh | ~43–63% |
| United States | $236/kWh | $108/kWh | ~54% |

: Source: BNEF via [@energy-storage-news-system-prices-2025].

At \$41/kWh for a 4-hour system in China by 2035, battery storage approaches the cost of the cells alone today. This implies continued innovation in system integration, manufacturing scale, and potentially chemistry shifts (sodium-ion, solid-state).

---

## 2. Cell Format Evolution: The 500 Ah+ Generation

### 2.1 From 280 Ah to 600 Ah+

The 280 Ah prismatic LFP cell that dominated utility storage from 2022 to 2024 is being rapidly superseded. The 314 Ah format served as a brief transition. In 2025–26, leading Chinese manufacturers are mass-producing cells in the 530–1,175 Ah range [@ess-news-500ah-cells-2026].

: Large-Format LFP Cell Landscape, 2025–26 {#tbl-cell-formats}

| Manufacturer | Cell Capacity | Energy Density | Production Status |
|-------------|-------------:|---------------:|-------------------|
| CATL | 587 Ah | 434 Wh/L | Mass production; 60 GWh/yr capacity; >2 GWh shipped by Dec 2025 |
| EVE Energy | 628 Ah | — | Mass production since Dec 2024 ("Mr. Big") |
| Sunwoda | 684 Ah | ≥440 Wh/L | 1 millionth cell produced Dec 2025 |
| CALB | 588–640 Ah | — | Shipments targeting early 2026 |
| HiTHIUM | 587 Ah | — | Deliveries from Aug 2025 |
| HiTHIUM | 1,175 Ah | — | Mass production since Jun 2025 ("∞Cell") |
| Envision AESC | 530 Ah | — | Launched Apr 2025 |
| REPT BATTERO | 587 Ah | 430 Wh/L | In production ("Wending") |
| Cornex | 588 Ah | — | In production |

: Source: ESS News [@ess-news-500ah-cells-2026; @ess-news-catl-587ah-2025], InfoLink [@infolink-intersolar-2025].

### 2.2 Why Larger Cells Matter

The shift to 500 Ah+ cells is not merely incremental. Larger cells reduce the number of units per container, which in turn reduces:

- **Interconnects and welds** — fewer cell-to-cell connections
- **Sensors and BMS channels** — fewer cells to monitor
- **Assembly complexity** — faster manufacturing, lower labour cost
- **Failure modes** — fewer joints that can degrade

Systems using 300 Ah+ cells are approximately **50% cheaper** at system level than those using smaller cells. Containers with 4 MWh+ capacity are approximately **39% cheaper** than 2–4 MWh configurations [@energy-storage-news-system-prices-2025; @ember-battery-storage-2025]. These are substantial step-changes, not marginal improvements.

### 2.3 Container Sizes: Towards 5–10 MWh

The combination of larger cells and denser packaging is driving container capacities upward:

- **Standard 20 ft containers**: now house 5–6 MWh with 500 Ah+ cells
- **HiTHIUM 1,175 Ah systems**: 6.25 MWh per container (deployed in Saudi tenders at \$73–75/kWh)
- **Trina Elementa 2 Pro**: 10 MWh (2-hour) and 20 MWh (4-hour) configurations, launched August 2025

The trend toward 7 MWh+ per container is well established and accelerating. This has direct implications for project-level balance-of-system costs: fewer containers per GWh means fewer footings, fewer cable runs, and simpler site layouts.

---

## 3. Upward Price Pressures

### 3.1 Lithium Carbonate

Lithium carbonate prices have risen from their 2024 trough. Following the VAT rebate announcement, the Guangzhou Futures Exchange lithium carbonate contract jumped 9% to 156,060 yuan/t (~\$21,650/t), the highest since November 2023 [@ess-news-vat-rebate-2026].

Fastmarkets' Q4-2025 outlook projects lithium carbonate gradually rising from \$10/kg to \$25/kg by 2029 — roughly where it sat pre-COVID [@fastmarkets-lithium-outlook-2025]. This is a meaningful increase from 2024 lows but far below the \$80/kg+ panic levels of 2022.

### 3.2 China VAT Export Rebate Removal

China's Ministry of Finance and State Taxation Administration announced a phased removal of the VAT export rebate on battery products [@scio-vat-rebate-2026]:

- **From April 2026**: rebate reduced from 9% to 6%
- **From January 2027**: rebate eliminated entirely (0%)

This directly squeezes Chinese exporter margins by up to 9 percentage points unless passed through to buyers. The policy aims to reduce aggressive export price discounting, stabilise overseas market pricing, and mitigate trade retaliation risk [@ess-news-vat-rebate-2026]. Some front-loading of shipments occurred in Q1 2026 as exporters accelerated deliveries ahead of the April deadline.

### 3.3 Anti-Involution Policy

China's government has signalled opposition to "involution" — the destructive below-cost competition that characterised domestic ESS pricing in 2023–24. This pricing discipline, if sustained, would put a floor under export prices [@kubik-linkedin-pricing-2026].

### 3.4 Net Assessment of Price Pressures

These three pressures are real. However, as Kubik argues persuasively, the structural conditions that enabled the 2022 price shock are absent [@kubik-linkedin-pricing-2026]:

1. **Contract structure has matured**: contracts now routinely index lithium carbonate, unlike the fixed-price arrangements common in 2022
2. **ESS market share has grown**: ESS now represents 20–25% of global battery demand, giving the sector meaningful pricing power and supply chain priority
3. **Innovation absorbs cost increases**: system-level $/kWh has remained broadly flat in recent months despite cell cost movement, because higher-density enclosures and larger format cells continue to improve system integration efficiency
4. **Demand elasticity is understood**: suppliers recognise that sharp price spikes destroy demand; maintaining moderate, predictable pricing supports the long-term growth trajectory
5. **Alternative chemistries provide a ceiling**: sodium-ion is emerging as a credible drop-in alternative, particularly for longer-duration applications

Benchmark Mineral Intelligence data (cited by Kubik via Crispin McCutcheon) shows system pricing remaining broadly flat despite recent cell cost movement. The next 12 months are more likely to bring **price stabilisation** than a repeat of the 2022 supercycle.

---

## 4. Deployment Scale

### 4.1 Global Deployment

Global BESS deployment crossed the 100 GW threshold for the first time in 2025 [@volta-battery-report-2025; @globenewswire-volta-2026]:

- **2025 additions**: 104 GW / 257 GWh
- **Cumulative capacity**: 267 GW / 610 GWh
- **40% of all cumulative capacity** was installed in 2025 alone

This is extraordinary growth. The BESS sector recorded the strongest demand growth of any major battery market segment in 2025 [@energy-storage-news-bnef-2025].

### 4.2 China's Dominance

China continues to set the global pace on project scale, deployment speed, and system-level learning-by-doing [@kubik-linkedin-china-bess-2026]:

- **December 2025 alone**: China installed more BESS than the US (the second-largest market) did in all of 2025^[Benchmark Mineral Intelligence data cited by @kubik-linkedin-china-bess-2026.]
- **Jingyi Chagan Hada**: 4 GWh single-site project in Inner Mongolia, supplied by Envision ESS — briefly the world's largest
- **Inner Mongolia cluster**: 12.8 GWh across seven sites, all supplied by Envision in 2025, to be "fully integrated into the electricity spot market" [@cnesa-inner-mongolia-2025]
- **Saudi Arabia**: targeting 22 GWh operational by 2026, expanding to 48 GWh by 2030 [@highjoule-bess-forecast-2026]

### 4.3 Long-Duration Energy Storage

Falling cell costs have unlocked economically viable 8–12 hour storage applications. LDES deployment figures soared in 2025, though only 0.5 GW is operational outside China [@volta-battery-report-2025]. The growing share of LDES in the pipeline drives down the weighted-average $/kWh of deployed storage, because longer-duration systems amortise fixed balance-of-system costs over more kilowatt-hours.

---

## 5. Sodium-Ion: The Emerging Hedge

Sodium-ion battery technology is advancing from pilot to commercial scale:

- **CATL** confirmed large-scale sodium-ion deployment across multiple sectors in 2026, including grid storage
- **BYD** is also accelerating sodium-ion development
- Current capex is slightly above LFP, but learning rates are steep
- Key advantage: **zero lithium price exposure**, abundant raw materials (sodium, iron, manganese)
- Primary target markets: grid storage in China and India, where cost sensitivity is highest

Sodium-ion provides a credible ceiling on lithium-ion pricing. If LFP prices rise materially, project developers can substitute sodium-ion for many stationary storage applications without redesigning systems — the voltage profiles and form factors are designed for drop-in compatibility [@kubik-linkedin-pricing-2026].

---

## 6. Implications for Australian NEM Modelling

For the ITK NEM price forecasting model, several implications follow:

1. **BESS capital costs should continue declining in base-case assumptions**, though the rate of decline will moderate from the 30–40% annual falls seen in 2024–25 toward 10–15% annually through the late 2020s

2. **The 4-hour duration sweet spot is shifting toward 8 hours** as cell costs fall and the value of longer-duration shifting increases with higher renewable penetration. The LP model's inclusion of 4h and 8h BESS classes is well-aligned with market direction

3. **System-level costs matter more than cell costs** for CAPEX assumptions. The 50% cost advantage of 300 Ah+ cell systems and the 39% advantage of 4 MWh+ containers are structural shifts that will persist

4. **The VAT rebate removal adds approximately 5–9% to Chinese export prices** from 2027 onward, partially offsetting ongoing technology-driven cost reductions. This should be factored into near-term CAPEX assumptions but does not alter the long-run trajectory

5. **Sodium-ion provides a soft ceiling** on battery storage costs from the late 2020s onward. If lithium prices spike, sodium-ion substitution limits the upside in storage CAPEX

6. **Australian BESS project costs sit between global average and US levels**, reflecting local labour costs, grid connection complexity, and distance from Chinese manufacturing — but are significantly below US levels due to the absence of tariffs on Chinese battery imports

---

## References
