---
title: "Iron Bridge Magnetite: Project Economics and Power Demand"
author: "David Leitch"
date: 2026-04-13
categories: ["Investment", "Generation"]
bibliography: diesel_electrification_references.bib
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Project Overview

Iron Bridge is Fortescue's first magnetite operation, located 145 km south of Port Hedland in the Pilbara, Western Australia. It is an unincorporated joint venture between FMG Magnetite Pty Ltd (69%) and Formosa Steel IB Pty Ltd (31%). The project produces a high-grade 67% Fe magnetite concentrate suitable for direct steelmaking feed, priced at a premium to the standard Platts 62% Fe index [@fortescue-iron-bridge-2023].

Iron Bridge is significant for the electrification story because it is the **single largest electricity consumer** in Fortescue's Pilbara system at **225 MW** [@mining-tech-iron-bridge-2024], and its processing plant was electrically powered from day one — the electrification question is about the *source* of that electricity (gas → renewables), not the end-use technology.

# Processing Method

Iron Bridge uses an innovative dry crushing and grinding circuit that is the subject of several Fortescue patents. The process is designed to reduce both energy consumption and water use relative to conventional wet SAG/ball mill magnetite circuits.

![Iron Bridge OPF process flow. Tonnage numbers refer to life-of-mine average.](../media/iron_bridge_opf_process_flow.png){#fig-ib-process-flow}

*Source: Fortescue Iron Bridge project approval [@fortescue-iron-bridge-approval-2019].*

The Ore Processing Facility (OPF) takes in **67 dmt of ore** plus **39 dmt of waste** (106 Mtpa total material movement). The processing chain:

1. **Primary and secondary crushing** — jaw and cone crushers reduce rock from ~1m to ~50mm
2. **HPGR tertiary crushing and primary grinding** — 12 High Pressure Grinding Rolls with **93 MW total installed power** dry-grind the ore to 80 µm. This is the dominant energy consumer, accounting for ~41% of plant power
3. **Air classification** — dry screening separates particles by size; oversize recirculates to the HPGR. This stage has been the primary source of ramp-up problems (see below)
4. **Dry magnetic separation** — 20 drum separators reject ~34 dmt/yr of non-magnetic gangue to tailings. Only **13 dmt** passes to the wet circuit
5. **Rougher and re-cleaner wet magnetic separation** — secondary grinding and wet magnetic cleaning upgrades the concentrate from ~50% Fe to 67% Fe
6. **Slurry pipeline** — 135 km pipeline pumps wet concentrate to Port Hedland for dewatering and ship loading

**Table: Estimated OPF power breakdown**

| Stage | Equipment | Installed MW | Share |
|:---|:---|---:|---:|
| Primary & secondary crushing | Jaw + cone crushers | ~10–15 | ~5% |
| HPGR grinding | 12 High Pressure Grinding Rolls | 93 | 41% |
| Dry magnetic separation | 20 drum separators | ~10–15 | ~5% |
| Secondary grinding + cleaning | Fine mills + wet mag sep | ~40–60 | ~22% |
| Conveyors, pumps, water, services | Various | ~30–40 | ~15% |
| **Total processing plant** | | **~225** | **100%** |

*Sources: [@mining-tech-iron-bridge-2024] (225 MW total, 12 HPGR at 93 MW, 20 magnetic drums); [@fortescue-iron-bridge-approval-2019] (process flow and tonnages).*

The HPGR dry process saves approximately **30% of comminution energy** and **75% of water** versus a conventional SAG + ball mill wet circuit. A conventional circuit for 22 Mtpa would require ~120–140 MW for grinding alone. However, the dry process creates dust, abrasion, and material handling challenges that do not exist in wet circuits — these have been the primary source of ramp-up delays.

# Capital Cost and Overruns

| Milestone | Capital cost | Date |
|:---|---:|:---|
| Original approval | US\$2.6B | February 2019 |
| First escalation | ~US\$3.0B | Pre-2021 |
| Second escalation | US\$3.3–3.5B | 2021 |
| Updated estimate | US\$3.9B | 2022 |
| Final reported | US\$4.0B | August 2023 |
| **Overrun** | **US\$1.4B (+54%)** | |

*Sources: Fortescue FY2023 results presentation (August 2023); [@fortescue-iron-bridge-approval-2019]; Mining Weekly; MINING.COM.*

Fortescue's 69% share of the US\$4.0B capex is approximately **US\$3.1B**. The original book value of the Iron Bridge Cash Generating Unit was US\$3.5B as at 30 June 2023.

# Impairment

In the **FY2023 full-year results** (announced 28 August 2023), Fortescue recognised a **US\$1.0 billion pre-tax** (US\$726 million post-tax) non-cash impairment charge on Iron Bridge.

Management cited:

- Increasing discount rates
- Industry-wide inflation on construction costs and supply chain delays
- Less tangible capitalised costs (pilot/demonstration plants, capitalised interest) that do not generate productive value

The impairment effectively wrote off ~US\$1B of "learning costs" — the price of being first-of-kind with the dry HPGR process at this scale.

# Water Pipeline Failure

In January 2024, leaks were discovered in the **220 km raw water supply pipeline** from the West Canning Basin to the mine site. More than 30% (~65 km) of steel pipe required replacement, at a cost of approximately **US\$100 million**. This is additional to the US\$4.0B capex.

The pipeline supplies process water for the wet magnetic separation stages. The failure directly constrained FY2024 production to 2–4 Mtpa against a target of 5 Mtpa, with an estimated **A\$1.3 billion in lost sales revenue**.

# Air Classification Ramp-Up Issues

The air classification circuit — sitting between the HPGR and dry magnetic separation — has been the primary bottleneck in the production ramp. Two specific problems:

1. **Premature erosion** of classifier internals — magnetite is extremely abrasive (iron oxide). The original liner material wore out faster than expected, degrading separation efficiency. Fortescue redesigned the units in-house and installed **upgraded ceramic liners**
2. **Aerobelt conveyor performance** — the downstream air-cushion conveyors had throughput and reliability issues with the abrasive magnetite fines

These are first-of-kind engineering problems. HPGR + air classification + dry magnetic separation at 62.5 Mtpa feed rate has never been attempted before.

# Production Timeline

| Period | Shipments (Mtpa) | Status |
|:---|---:|:---|
| FY2024 | 2–4 | Pipeline leaks, ramp-up issues |
| FY2025 | 7 | Air classifier fixes improving throughput |
| FY2026 target | 10–12 | |
| H2 FY2027 target | 16–20 (annualised) | |
| FY2028 target | **22 (nameplate)** | 5 years after first production |

*Source: Fortescue revised Iron Bridge timeline, May 2025 (Mining Weekly).*

The 5-year ramp from first production to nameplate is extraordinary for a processing plant — most conventional plants reach nameplate within 12–18 months.

# Revenue and Operating Economics

From Fortescue's FY2025 annual report:

| Metric | FY2025 | FY2024 |
|:---|---:|---:|
| Magnetite shipments | 7 Mwmt | 1 Mwmt |
| Platts 65% Fe CFR index | US\$114/dmt | US\$131/dmt |
| Realised magnetite price | US\$113/dmt | US\$137/dmt |

**At nameplate (22 Mwmt = 20 Mdmt):**

| Metric | Value |
|:---|---:|
| Annual revenue at US\$113/dmt | ~US\$2.3B |
| Annual revenue at US\$120/dmt | ~US\$2.4B |
| C1 cost (life of mine, real 2023) | US\$45/wmt |
| Implied EBITDA margin at US\$113 | ~US\$68/wmt |
| Implied EBITDA at nameplate | ~US\$1.4B/yr |
| Simple payback on US\$4.0B capex | ~2.9 years |

*Note: C1 cost is quoted "net of fees for port and power services" — Iron Bridge pays Fortescue's energy division a transfer price for electricity.*

At current FY2025 shipments of 7 Mtpa with ~US\$400M/yr opex (Fortescue share), the actual C1 is well above the LOM target. The economics only work at or near nameplate.

# Power Supply

Iron Bridge is powered from the **Solomon Power Station** via the Pilbara Energy Connect (PEC) 220 kV transmission network.

**Solomon Power Station:**

- 14 gas-fired reciprocating engines (original), ~165 MW installed
- 150 MW additional gas generation added for Iron Bridge (Pilbara Generation Project, 2020)
- Total capacity: ~315 MW
- Gas supplied via **Fortescue River Gas Pipeline** — 270 km, 16-inch line from Dampier

**Current gas consumption (estimated):**

| Parameter | Value |
|:---|---:|
| Heat rate (reciprocating engine) | ~8 GJ/MWh |
| Current gas generation | ~230 MW average |
| Annual gas consumption | ~16 million GJ/yr |
| Fortescue stated gas consumption | 15 million GJ/yr |
| Gas cost at A\$8/GJ | ~A\$130M/yr |

*Note: North Star Junction 100 MW solar (operational H2 2024) is already displacing ~28 MW average of gas generation.*

**At full capacity (530 MW total Pilbara demand):**

| Scenario | Gas (M GJ/yr) | Cost at A\$8/GJ |
|:---|---:|---:|
| Counterfactual — all gas, no renewables | 37 | A\$296M/yr |
| With Phase 1 renewables (1.2 GW solar + 600 MW wind + 4.5 GWh battery) | ~4 | ~A\$34M/yr |
| **Gas avoided** | **~33 (89%)** | **~A\$262M/yr** |

The gas engines transition from baseload to peaking/backup role, running perhaps 10–15% of hours to fill overnight and low-wind gaps that the 4.5 GWh battery cannot cover. Complete gas elimination requires the Phase 2 expansion (~2 GW additional renewable generation + 4 GWh storage).

# Significance for Mining Electrification

Iron Bridge demonstrates both the promise and the pain of first-of-kind industrial electrification:

- **The processing is already electric** — 225 MW of electric motors, not diesel. The question is where the electrons come from
- **The HPGR innovation works** — 30% energy savings vs SAG mills, 75% water savings. But the ancillary systems (air classification, water pipeline) caused most of the cost and schedule pain
- **The capital cost (\>US\$4B + impairment) is a warning** — novel process technology at scale carries enormous execution risk
- **The revenue potential is real** — 67% Fe concentrate at US\$113+/dmt, ~US\$1.4B/yr EBITDA at nameplate
- **The power demand dominates** — at 225 MW, Iron Bridge is ~43% of the total Pilbara mine-site electricity demand and the primary justification for the Pilbara Energy Connect transmission build

# References

::: {#refs}
:::
