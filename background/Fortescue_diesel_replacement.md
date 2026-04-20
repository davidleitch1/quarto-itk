---
title: "Fortescue Diesel Replacement: Fleet Electrification Economics"
author: "David Leitch"
date: 2026-04-13
categories: ["EVs", "Investment"]
bibliography: diesel_electrification_references.bib
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Summary

Fortescue is replacing its entire diesel haul truck fleet across five Pilbara mine sites with battery-electric vehicles. This note examines the fleet composition, truck economics, charging infrastructure requirements and costs, and the role of battery swap packs as distributed energy storage.

The headline finding: at current diesel prices (net of FTC), the fleet replacement generates annual fuel savings of approximately **A\$1.1 billion** against a total investment of **~A\$5–6 billion** (trucks + charging infrastructure + renewables share), implying a payback of **5–6 years** on the diesel replacement component alone. At crisis diesel prices the payback drops to **~3 years**.

---

# The Diesel Baseline

Fortescue consumes approximately **700 million litres of diesel per year** across its Pilbara operations, making it one of Australia's largest diesel consumers. This diesel is delivered by ship from Singapore to Port Hedland, then road-tankered 145–450 km to mine sites. Every 10 cpl movement in diesel prices has a ~\$70M impact on operating costs.

**Delivered diesel cost (net of Fuel Tax Credit):**

| Scenario | Delivered price | Net of FTC (52.6 cpl) | Annual cost (700 ML) |
|:---|---:|---:|---:|
| Normal market | \$1.80–2.10/L | \$1.27–1.57/L | A\$890–1,100M |
| Current crisis (Hormuz) | \$3.20–3.50/L | \$2.67–2.97/L | A\$1,870–2,080M |

*Sources: AIP terminal gate prices; [@australia-institute-ftc-2024]; Fortescue sensitivity disclosure (\$70M per 10 cpl).*

The diesel goes almost entirely into the **mining fleet** — haul trucks (60–70%), excavators and loaders (15–20%), drill rigs, dozers, water carts, and graders (~15–20%). Processing plants, conveyors, and accommodation are already electrically powered.

---

# Fleet Composition by Mine Site

Fortescue has ordered **360 battery-electric haul trucks** from two suppliers — Liebherr (T264 BEV) and XCMG (XDE240 BEV) — plus 100+ ancillary electric vehicles [@fortescue-liebherr-2024; @fortescue-xcmg-2024; @im-xcmg-fortescue-2025].

The allocation across sites is not publicly disclosed. The following estimates are based on relative production volumes, pit complexity, and haul distances:

**Table: Estimated fleet and charging infrastructure by mine site**

| Mine site | Production (Mtpa) | Est. trucks | Charging model | Est. chargers or swap bays | Est. infra cost |
|:---|---:|---:|:---|---:|---:|
| Solomon Hub (Firetail + Kings) | ~70 | 120–150 | MCS + swap | 18–22 chargers + 1–2 swap stations | US\$100–140M |
| Cloudbreak / Christmas Creek | ~60 | 100–120 | MCS + swap | 15–18 chargers + 1–2 swap stations | US\$85–120M |
| Eliwana | ~30 | 60–80 | MCS (first BEV trials here) | 9–12 chargers | US\$45–65M |
| Iron Bridge | ~22 | 20–40 | Swap (shorter hauls) | 1 swap station | US\$15–25M |
| Rail, port, ancillary | — | 60+ ancillary | Depot charging | Various | US\$30–50M |
| **Total** | **~190** | **~360 trucks + 100+ ancillary** | | | **US\$275–400M** |

*Note: Truck allocations are ITK estimates based on production volumes and material movement. Not Fortescue disclosures. Charging infrastructure costs from McKinsey (US\$700k–1M per truck) and ICMM/Mining3 benchmarks.*

---

# Truck Economics

## Vehicle comparison

**Table: 240-tonne class haul truck comparison**

| Specification | Cat 793F (diesel) | Liebherr T264 BEV | XCMG XDE240 BEV |
|:---|---:|---:|---:|
| Payload (tonnes) | 227 | 240 | 230 |
| Engine/motor power (kW) | 1,976 | 3,200 (peak) | 1,865 |
| Battery capacity (MWh) | — | 3.2 | Not disclosed (BYD Blade LFP) |
| Fuel/energy consumption | 137–182 L/hr diesel | ~86% lower cost/tonne | Not disclosed |
| Charging method | Refuel ~15 min | 6 MW MCS (~30 min) | Battery swap (~15 min) |
| Purchase price (est.) | ~US\$5–6M | ~US\$6–8M | ~US\$3–4.5M |

*Sources: Cat 793F OEM specifications; Liebherr T264 product data; LECTURA specs (XCMG XDE240); [@fortescue-liebherr-2024] (implied pricing).*

## Per-truck annual economics

| Item | Diesel (Cat 793F) | Electric (BEV) |
|:---|---:|---:|
| Fuel/energy cost | ~A\$1.5M/yr | ~A\$0.25M/yr |
| Maintenance | ~A\$0.48M/yr | ~A\$0.34M/yr |
| **Total operating** | **~A\$2.0M/yr** | **~A\$0.59M/yr** |
| **Annual saving** | | **~A\$1.4M/truck** |

*Assumptions: 6,000 operating hrs/yr, diesel 160 L/hr at \$1.57/L net of FTC, electricity at A\$91/MWh (Phase 1 LCOE), 500 kWh/hr electric consumption, 30% maintenance saving on BEV.*

**BEV premium:** ~A\$2–3M per truck (Liebherr ~A\$3M, XCMG ~A\$1–2M over diesel equivalent).

**Simple payback:** 1.5–2 years per truck at normal diesel prices. Under 1 year at crisis prices.

## Basis for the 500 kWh/hr energy consumption assumption

The 500 kWh/hr figure used above is anchored to the only published real-world measurement for an ultra-class battery-electric haul truck. No operator running 240 t-class BEVs has yet published per-cycle consumption data — Fortescue's Liebherr T264 trials at Eliwana started early 2026 and BHP/Rio's Cat 793 XE Early Learner trials at Jimblebar began December 2025.

**Verifiable BEV haul truck energy data**

| Source | Truck | Measurement |
|:---|:---|---:|
| Boliden Aitik retrofit (peer-reviewed, Energies 2022) | Cat 795F AC, 313 t payload | 361 kWh/cycle measured |
| Vale operational pilot (Brazil/Indonesia) | 72 t electric truck | 525 kWh ÷ 36 cycles ≈ 14.6 kWh/cycle |
| Liebherr T264 BEV (manufacturer spec) | 240 t payload | 3.2 MWh battery, no consumption disclosed |
| XCMG XDE240 BEV | 230 t payload | Not disclosed |

*Sources: [@cyrus-aitik-energies-2022]; [@vale-electric-truck-2022]; Liebherr T 264 BEV product data.*

**Scaling Aitik to the 240 t class:** Cat 795F AC GVW is ~468 t (155 t empty + 313 t payload); the T264/XDE240 GVW is ~385 t. Linear GVW scaling gives ~300 kWh/cycle for a 240 t-class BEV. At typical Pilbara cycle times this becomes:

| Cycle time | Cycles/hr | kWh/hr |
|:---|---:|---:|
| 30 min (short haul) | 2.0 | 600 |
| 35 min (typical) | 1.71 | 510 |
| 40 min (longer/deeper pit) | 1.5 | 450 |

**Cross-check via diesel equivalence:** Cat 793F at 160 L/hr × 10 kWh/L × ~40% engine efficiency = 640 kWh/hr at the wheels; ÷ 90% BEV drivetrain efficiency = 720 kWh/hr battery draw, less ~25% regen on empty descent ≈ 540 kWh/hr.

**Defensible range: 450–600 kWh/hr.** The 500 kWh/hr point estimate sits near the low-middle of this range. It may be slightly conservative for Pilbara iron ore: the orebody is below the ROM pad (loaded uphill, empty downhill — the worst geometry for regen recovery), and Pilbara hauls are typically shorter than Aitik's. A 600 kWh/hr upper-bound case raises fleet electricity cost from ~A\$330M to ~A\$395M — meaningful but does not change the payback conclusion.

## Fleet-wide economics

| Metric | Value |
|:---|---:|
| Fleet size | 360 trucks |
| Annual diesel saving (fleet) | ~A\$500M/yr |
| Annual maintenance saving (fleet) | ~A\$50M/yr |
| **Total annual saving** | **~A\$550M/yr** |
| BEV premium (fleet) | ~A\$900M |
| Charging infrastructure | ~A\$400–600M |
| **Total incremental investment** | **~A\$1.3–1.5B** |
| **Fleet payback** | **2.4–2.7 years** |

---

# Charging Infrastructure

## Two models in the fleet

Fortescue will operate two charging approaches, matching the two truck suppliers:

**Liebherr T264 BEV — MCS fast charging:**

- 6 MW Megawatt Charging System with robotic connection (ABB/Liebherr)
- ~30 minute charge for 3.2 MWh battery
- Chargers located at pit-edge and dump-side
- **US\$3–5M per charger installed** (US\$2–3.5M at scale)
- 1 charger per 6–8 trucks (with redundancy)

**XCMG XDE240 BEV — battery swap:**

- Robotic swap station: depleted pack out, charged pack in
- ~15 minute swap time (vs 30 min MCS charge)
- Standardised 400 kWh BYD Blade LFP packs — same pack across trucks, excavators, and loaders
- **US\$5–10M per swap station** + US\$250–400k per spare pack
- Float ratio: 1.3–1.5 packs per truck

## Why not trolley assist?

Trolley assist (overhead catenary or Liebherr Power Rail on the haul ramp) was considered but is not part of Fortescue's plan. The reasons:

1. **Cost vs battery swap:** A 3 km trolley system for 20 trucks costs US\$43–80M. Swap stations for the same fleet cost roughly the same, but the spare packs double as distributed energy storage (see below). Trolley infrastructure is single-purpose.

2. **Relocation:** Fortescue operates ~5 pits across the Pilbara. Pit ramp geometry changes every 2–5 years as mining advances. Relocating catenary costs 30–60% of initial installation each time (US\$5–10M per event for a 3 km system). Over a 20-year mine life with 4–6 moves, lifecycle relocation costs can equal the original investment. Swap stations are fixed infrastructure.

3. **Energy saving is minimal:** Trolley eliminates ~10% battery charge/discharge losses. At fleet scale that's ~US\$10–15M/yr — not enough to justify the capex and relocation costs.

4. **Speed benefit is narrow:** 1.8× faster on the ramp sounds compelling, but the ramp is only 15–20% of the total haul cycle. Net cycle time improvement is 5–10%.

5. **Fortescue has already chosen:** they ordered XCMG trucks with battery swap and Liebherr trucks with MCS charging. No trolley infrastructure has been announced for any Pilbara site. The 10 April 2026 ASX release mentions battery storage repeatedly but never trolley.

6. **Complexity:** MCS + swap is two charging systems. Adding trolley makes three systems to maintain in a dust/heat environment.

*Sources: Komatsu trolley assist specifications; Liebherr Power Rail technical spotlight (Bauma 2025); Boliden Aitik operating experience.*

---

# Swap Packs as Distributed Energy Storage

This is the most underappreciated aspect of the battery swap model. The spare packs at swap stations are not just truck infrastructure — they are **grid-connected energy storage** that helps the renewable system manage the solar/wind intermittency problem.

## The problem

Fortescue's Phase 1 renewable system (1.2 GW solar + 600 MW wind) produces ~4,836 GWh/yr against ~530 MW average demand. But generation and demand don't match hour by hour:

- **Midday:** solar produces ~1,000 MW. Demand is ~530 MW. Surplus of ~470 MW — needs to be stored or curtailed.
- **Overnight:** solar is zero. Wind averages ~216 MW. Demand is still ~530 MW. Deficit of ~314 MW — needs to come from storage.
- **Multi-day low wind:** if wind drops below 20% CF for 48 hours, the 4.5 GWh grid battery depletes in ~10 hours at 450 MW discharge.

The grid battery (4.5 GWh at 4-hour duration) can shift ~4–5 hours of daytime surplus to the evening, but it cannot cover a full 12-hour overnight gap, let alone a multi-day low-wind event.

## How swap packs help

Each spare battery pack at a swap station is ~3 MWh. With 360 trucks and a 1.5× float ratio, there are **~180 spare packs** in the system — representing **~540 MWh** of additional storage.

But the real flexibility comes from **scheduling when the packs charge:**

- **Daytime (solar surplus):** charge all spare packs at maximum rate. 180 packs × ~1 MW charge rate = ~180 MW of additional demand, absorbing surplus solar that would otherwise be curtailed.
- **Evening/overnight:** freshly charged packs are swapped into trucks. The trucks operate on the charged packs. No grid charging needed during the overnight deficit period.
- **Low-wind events:** maintain a buffer of fully charged packs (say 50 packs = 150 MWh) that can extend truck operations for 4–6 hours beyond normal, buying time for wind to recover.

The swap model turns 180 spare packs into a **flexible 180 MW / 540 MWh demand response resource** that the grid operator (Fortescue's own AI system) can schedule to absorb solar peaks and avoid overnight charging.

## Comparison: swap buffer vs additional grid battery

| Parameter | Grid battery (BESS) | Swap pack buffer |
|:---|:---|:---|
| Primary purpose | Grid stability, time-shifting | Truck fleet operation |
| Storage per unit | Centralised (50 MW / 250 MWh per unit) | Distributed (3 MWh per pack) |
| Cost | ~A\$250/MWh (BYD Blade) | Already purchased for fleet operation |
| Additional cost for grid service | Zero — the packs exist for truck ops | Zero — scheduling software only |
| Flexibility | Charge/discharge on command | Charge scheduling only (discharge = truck operation) |
| Low-wind coverage | Depletes in ~10 hrs at 450 MW | Extends truck ops 4–6 hrs; doesn't serve other loads |

The key insight: the swap packs provide **free incremental storage** — their capital cost is already justified by the truck fleet economics. The grid-balancing benefit is a bonus that requires only intelligent scheduling software, which Fortescue is developing in-house (the "proprietary AI-driven optimisation systems" mentioned in the 10 April ASX release [@fortescue-green-grid-2026]).

## Scaling the buffer

If Fortescue wanted to extend the swap buffer specifically for grid resilience, additional packs are cheap:

- 50 extra packs × 3 MWh × A\$250/MWh = **A\$37.5M** for 150 MWh of additional storage
- 100 extra packs = **A\$75M** for 300 MWh
- Compare to a standalone 300 MWh BESS at ~A\$75M — same cost, but the swap packs also serve as truck fleet spares

This is why battery swap may prove superior to MCS charging for mining applications where the mine also operates its own renewable grid. The swap infrastructure creates a storage asset that serves double duty.

---

# Total Diesel Replacement Investment

**Table: Fortescue diesel replacement — total cost summary**

| Component | Cost (A\$) | Notes |
|:---|---:|:---|
| 360 BEV trucks (premium over diesel) | ~900M | Liebherr ~A\$3M premium, XCMG ~A\$1.5M premium |
| 100+ ancillary BEV equipment | ~400M | XCMG US\$400M contract (loaders, dozers, water carts) |
| 50+ electric drill rigs | ~530M | Epiroc US\$350M contract |
| MCS chargers (~45 units) | ~250M | US\$3.5M avg installed |
| Swap stations (~5 units) | ~75M | US\$10M avg + 180 packs at 1.5× float |
| Extra swap packs (120 packs for grid storage) | ~90M | 120 × 3 MWh × A\$250/MWh — reduces overnight unserved from 366 to 79 MWh/day |
| Grid connection and distribution | ~100M | Substations, HV cable at each site |
| **Total diesel replacement** | **~A\$2.35B** | |

*Note: The 120 extra swap packs serve double duty — fleet spares and distributed grid storage absorbing daytime solar surplus. This is the cheapest marginal storage in the system at ~A\$250/MWh, compared to standalone BESS at similar cost but without the fleet benefit.*

**Annual savings:**

| Item | A\$/yr |
|:---|---:|
| Diesel fuel avoided (700 ML at \$1.57/L net) | ~1,100M |
| Maintenance reduction (~30% on BEV fleet) | ~50M |
| Less: electricity cost (at A\$91/MWh LCOE) | (350M) |
| **Net annual saving** | **~800M** |

**Simple payback on diesel replacement: ~2.9 years.**

This excludes the renewable generation and transmission investment (separately justified by replacing gas-fired electricity at Solomon Power Station) and the truck chassis cost (which would be incurred regardless as the diesel fleet reaches end of life).

---

# Timeline

| Date | Milestone |
|:---|:---|
| Sep 2024 | US\$2.8B Liebherr partnership announced (360 T264 BEV trucks) |
| Nov 2024 | US\$400M XCMG ancillary equipment contract |
| Apr 2025 | US\$350M Epiroc electric drill rig contract |
| Sep 2025 | XCMG added as second haul truck supplier (150–200 units) |
| Early 2026 | 4 autonomous BEV trucks in validation at Eliwana |
| 2026 | First BEV production trucks operational in Pilbara |
| 2026–2028 | Progressive fleet replacement across all sites |
| 2028–2030 | XCMG BEV deliveries (phased) |
| 2030 | Real Zero target — no diesel in Pilbara operations |

---

# References

::: {#refs}
:::
