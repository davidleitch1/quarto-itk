---
title: "Why Texas Wind Has Stalled: ERCOT Wind Generation 2021-2025"
date: 2026-02-20
author: "ITK - Claude assisted Research"
format: html
draft: false
categories: ["Global", "Wind", "ERCOT"]
lightbox: true
bibliography: ercot_wind_references.bib
---

# Summary

Texas wind electricity generation has plateaued at approximately 108--115 TWh per year from 2021 through 2025, despite Texas operating the largest wind fleet in the United States (approximately 41 GW installed). Over the same period, ERCOT solar generation increased nearly fivefold, from 16 TWh to 76 TWh.

This note examines why wind stalled while the broader ERCOT system grew 17% (437 to 513 TWh). Five reinforcing factors explain the plateau:

1. **New wind construction collapsed** as developers shifted decisively to solar and battery storage.
2. **Wind turbine costs rose approximately 40%** from 2021 lows due to supply chain disruptions and higher interest rates.
3. **CREZ transmission lines are saturated**, constraining output from the best wind zones in West Texas and the Panhandle.
4. **Curtailment has surged**, creating a vicious cycle that further discourages investment in congested zones.
5. **Regulatory friction is increasing** at both state and federal levels, disproportionately affecting wind's longer development timelines.

---

# The Generation Picture

: ERCOT Electricity Generation by Fuel (TWh) {#tbl-ercot-generation}

| Fuel Source     | 2021  | 2022  | 2023  | 2024  | 2025  | Change |
|-----------------|------:|------:|------:|------:|------:|-------:|
| Natural Gas     | 173.0 | 182.2 | 210.3 | 212.5 | 216.7 | +44    |
| Wind            | 114.2 | 114.7 | 108.4 | 111.0 | 115.4 | +1     |
| Solar           | 15.7  | 24.1  | 32.1  | 52.4  | 76.0  | +60    |
| Coal            | 74.8  | 69.1  | 61.8  | 63.4  | 61.5  | -13    |
| Nuclear         | 39.4  | 41.2  | 41.6  | 41.5  | 41.7  | +2     |
| Other/Storage   | 19.7  | 0.9   | 1.1   | 1.2   | 1.5   | -18    |
| **Total**       | **437** | **432** | **455** | **482** | **513** | **+76** |

: Source: ERCOT generation data. 2025 figures are actual.

Wind's share of ERCOT generation has declined from 26% in 2021 to 23% in 2025 --- not because output fell, but because total demand grew 17% and all the incremental generation came from solar (+60 TWh) and gas (+44 TWh).

---

# Factor 1: New Wind Construction Collapsed

The most direct explanation is that developers stopped building wind farms in Texas. ERCOT wind capacity additions fell to just **253 MW in the 2023--24 period**, compared with **5,395 MW of solar** over the same timeframe [@ieefa-ercot-transition-2025].

: ERCOT Capacity Additions 2023-2024 {#tbl-capacity-additions}

| Technology      | Additions (MW) | Share |
|-----------------|---------------:|------:|
| Solar           | 5,395          | 57%   |
| Battery Storage | 3,821          | 40%   |
| Wind            | 253            | 3%    |

: Source: IEEFA analysis of ERCOT data [@ieefa-ercot-transition-2025]

The interconnection queue confirms that this is not a temporary pause. As of mid-2025, ERCOT's queue contained 1,864 projects totalling approximately 408 GW [@interconnection-fyi-ercot-2025]:

: ERCOT Interconnection Queue by Technology (mid-2025) {#tbl-queue}

| Technology      | Queued Capacity (GW) | Share  |
|-----------------|---------------------:|-------:|
| Battery Storage | 174                  | 42.5%  |
| Solar           | 158                  | 38.7%  |
| Wind            | 41                   | 10.0%  |
| Gas             | 32                   | 7.9%   |

: Source: Interconnection.fyi ERCOT queue data [@interconnection-fyi-ercot-2025]. Queue figures overstate likely build-out due to high attrition rates.

Wind represents only 10% of queued capacity. Even accounting for the queue's notoriously high attrition rate, the pipeline signals that wind's share of future ERCOT capacity will continue to decline.

---

# Factor 2: Wind Turbine Costs Rose Sharply

Onshore wind turbine costs increased approximately 40% from their 2021 lows, driven by several converging pressures [@doe-wind-market-2024]:

- **Supply chain disruptions** from COVID and the Ukraine conflict elevated steel, rare earth, and component costs.
- **Turbine manufacturer pricing** recovered after years of unsustainable competitive discounting, with turbine prices reaching approximately $1,000/kW.
- **Higher interest rates** added an estimated $27/MWh to wind project levelised costs. Wind is more sensitive to capital costs than solar because of longer development timelines (approximately 4.5 years in ERCOT versus 2--3 years for solar).
- **Equipment shortages**, particularly large power transformers, created extended lead times that disproportionately affected wind projects.

The national picture underscores the severity: the US installed only 5.4 GW of wind in 2024 --- the lowest annual figure in a decade [@doe-wind-market-2024].

By contrast, solar LCOE continued to decline, reaching approximately $39/MWh by 2022, and solar projects offer shorter construction periods, simpler permitting, and straightforward co-location with battery storage. The economics shifted decisively.

---

# Factor 3: CREZ Transmission Lines Are Saturated

Texas's Competitive Renewable Energy Zones (CREZ) programme --- 3,600 miles of transmission lines carrying 18,500 MW, completed around 2014 --- was transformational for the initial build-out of West Texas wind [@industrial-sun-crez-2025; @texas-comptroller-wind-2023]. However, wind and solar capacity in the CREZ zones has since outgrown this infrastructure.

The Panhandle and West zones, which contain the best wind resources in ERCOT, now face the worst transmission congestion in the system [@modo-ercot-curtailment-2025]. Wind generators in these zones routinely experience curtailment exceeding the industry-standard 2% threshold. Stage 1 Panhandle upgrades, completed several years ago, proved insufficient to accommodate continued growth.

**The response --- ERCOT's 765 kV STEP plan:**

In April 2025, the Public Utility Commission of Texas (PUCT) approved ERCOT's first extra-high-voltage (765 kV) transmission lines under the State Transmission Expansion Plan [@puct-765kv-approval-2025]:

- Three 765 kV import paths into the Permian Basin were approved, plus potential Panhandle extensions.
- AEP Texas will construct approximately 300 miles connecting Fort Stockton to San Antonio.
- The ERCOT Board endorsed both western and eastern loop projects in December 2025 [@epe-ercot-765kv-2025].
- **Estimated total cost: $33 billion.**

However, construction timelines are long. Meaningful transmission relief is unlikely before the late 2020s at earliest. Until then, the constraint on wind output from the best resource areas remains binding.

---

# Factor 4: Curtailment Is a Vicious Cycle

Even where wind capacity exists, rising curtailment is eroding effective output. In 2024, combined wind and solar curtailment in ERCOT exceeded 8 TWh --- equivalent to approximately 1.2 GW of average hourly curtailment [@factset-ercot-curtailments-2025; @modo-ercot-curtailment-2025].

Key curtailment data:

- 44 of the top 50 curtailed generators in ERCOT saw year-on-year increases in curtailment in 2024.
- The West zone experienced 3.1 TWh of wind curtailment and 2.2 TWh of solar curtailment.
- The most heavily curtailed wind farms lose approximately 200 GWh per year each.
- **64% of curtailments** occur when renewable supply exceeds system demand; **36%** are due to transmission congestion [@modo-ercot-curtailment-2025].

The EIA projects that without grid upgrades, wind curtailment could nearly triple by 2035, reaching approximately 13% of available wind generation [@eia-texas-curtailments-2023; @windpower-monthly-curtailment-2025].

This creates a vicious cycle: rising curtailment reduces wind farm revenues, which discourages new investment, which prevents the scale benefits that might otherwise justify transmission upgrades. New wind in congested areas would simply be curtailed away, so developers avoid these zones entirely.

---

# Factor 5: Regulatory and Market Headwinds

## Texas state legislation

The Texas Legislature has introduced progressively stricter requirements for wind and solar development:

- **SB 624 (2023)** proposed onerous permitting requirements including environmental assessments, public meetings, and PUCT permits. Wind setbacks of 3,000 feet from property lines were proposed [@mintz-texas-permitting-2023].
- **SB 819 (2025)** passed the Texas Senate and creates a new siting and permitting regime. Wind setbacks of twice the turbine height from property lines and solar setbacks of 100--200 feet are required [@ve-texas-renewables-2025].

While less extreme than initial proposals, these measures add development friction and reflect growing local opposition to wind turbines in rural Texas communities.

## Federal uncertainty

The Trump administration has slowed permitting on federal land and tightened eligibility for clean energy tax credits. Potential IRA rollbacks create investment uncertainty, though the Production Tax Credit ($27.50/MWh in 2024) and Investment Tax Credit (30%) remain available for projects commencing construction before 2032 [@texas-tribune-clean-energy-2025].

## ERCOT's energy-only market

ERCOT operates without a capacity market, meaning generators earn revenue only from energy sales and ancillary services. As wind and solar increasingly push wholesale prices toward zero (or negative) during high-output periods, wind revenue per MWh declines [@eia-ercot-solar-wind-batteries-2025; @eia-texas-solar-shape-2024].

Most renewable power purchase agreements settle on an "as-produced" basis --- curtailed energy earns nothing, creating direct financial losses for wind farms in congested zones. This market structure disproportionately penalises variable generators in oversupplied areas.

---

# Outlook

The structural plateau in Texas wind generation is unlikely to break in the near term. The factors reinforcing it --- cost disadvantage versus solar, saturated transmission, rising curtailment, and regulatory friction --- are mutually reinforcing.

The $33 billion 765 kV STEP transmission build represents the most significant potential catalyst, but relief is years away (late 2020s at earliest). In the interim, ERCOT's growth will continue to be met primarily by solar, battery storage, and natural gas.

Two developments could alter this trajectory:

1. **Offshore wind in the Gulf of Mexico** could access different transmission corridors and load centres, though no commercial projects are currently under construction in Texas waters.
2. **Wind turbine cost declines** and resolution of supply chain constraints could restore wind's competitiveness, particularly if paired with co-located battery storage to mitigate curtailment losses.

For the 2021--2025 period, however, the conclusion is clear: ERCOT wind hit a plateau defined by saturated transmission, unfavourable cost trends, and developer preference for solar.

---

# References

::: {#refs}
:::
