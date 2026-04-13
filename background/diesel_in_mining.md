---
title: "Diesel in Mining: Consumption, Electrification, and the Fortescue Model"
author: "David Leitch"
date: 2026-04-13
categories: ["EVs", "Climate"]
bibliography: diesel_electrification_references.bib
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Mining's Share of Australian Diesel

Mining is Australia's single largest diesel-consuming sector. The IEEFA estimates mining consumed **9.6 billion litres** in FY2023-24, producing 22 Mt CO2-e [@ieefa-mining-diesel-2026]. This represents roughly 29% of national diesel consumption (~33.5 BL).

The commodity split is:

- **Coal mining**: 48% (~4.6 BL)
- **Iron ore**: 26% (~2.5 BL)
- **Other mining** (gold, copper, lithium, bauxite): 26% (~2.5 BL)

These shares are broadly confirmed by independent government data. The Australian Energy Statistics Table F [@aes-table-f-2025] records mining diesel consumption of 299.6 PJ in FY2023-24, equivalent to approximately 7.8 BL using the standard conversion of 38.6 MJ/litre. The discrepancy with IEEFA's 9.6 BL likely reflects differences in scope — IEEFA may include contracted mining support services classified under other ANZSIC divisions, or use NGER reporting which captures a broader boundary than the energy statistics framework.

Crucially, the **coal share is consistent across both sources**: AES Table F shows coal mining at 151.4 PJ out of 299.6 PJ total (50.5%), closely matching IEEFA's 48%. The AES data also confirms the growth trend: coal mining diesel consumption rose from 97.4 PJ in FY2014-15 to 151.4 PJ in FY2023-24 — a **55% increase in 10 years**. This is driven by deeper pits, rising strip ratios (~20:1 average in open-cut coal), and the progressive replacement of efficient electric draglines with diesel haul trucks as mines move to truck-and-shovel operations.

Mining diesel intensity has been *rising*, not falling. Coal mining diesel intensity increased 50% between FY2010-11 and FY2023-24 [@ieefa-mining-diesel-2026]. Total mining diesel consumption rose 23% between 2018 and 2024 while extraction volumes grew only 16%.

## Where does the diesel go on a mine site?

On a typical open-cut mine, diesel is consumed by:

- **Haul trucks**: 30-40% of site consumption. A single Cat 793F (240-tonne class) burns 200-450 litres per hour depending on grade and load, consuming approximately 1.8 million litres per year at 6,000 operating hours.
- **Excavators and loaders**: 15-20%
- **Ancillary equipment** (dozers, water trucks, graders, drill rigs): ~40%

## The Fuel Tax Credits subsidy

The Fuel Tax Credits Scheme provides a \$0.48/litre rebate on off-road diesel. Mining claims approximately \$4.6 billion per year in FTC, with coal mining alone receiving ~\$1.7 billion [@australia-institute-ftc-2024]. This subsidy blunts the economic incentive to electrify — it reduces the fuel-cost advantage of electric equipment by approximately 30%.

---

# Fortescue: The First Fleet-Scale Electrification

Fortescue is the first major miner to commit to fleet-scale replacement of diesel haul trucks with battery-electric vehicles. Its Pilbara iron ore operations consume approximately **700 million litres of diesel per year** — roughly 28% of the IEEFA iron ore total and 7% of all Australian mining diesel.

## The Liebherr partnership

In September 2024, Fortescue signed a **US\$2.8 billion** partnership with Liebherr [@fortescue-liebherr-2024] for 475 zero-emission machines, including:

- **360 autonomous battery-electric T264 haul trucks** (240-tonne class)
- Electric excavators
- Supporting equipment

Each T264 BEV carries a **3.2 MWh battery pack** — over 40 times the capacity of a typical passenger EV. The battery-electric power system is developed by Fortescue Zero (Fortescue's green technology division).

At an implied price of ~US$7.8 million per truck (~A$12 million), the BEV premium over a diesel T264 (~A$10 million) is approximately **A$2 million per unit**. Against an annual diesel bill of ~$3 million per truck (at 1.8 ML × $1.65/L), this implies a payback period of **under one year** — the strongest electrification economics of any vehicle segment in Australia.

## XCMG as second supplier

In September 2025, Fortescue expanded its plans by adding **XCMG** as a second supplier, with up to half the future fleet sourced from the Chinese manufacturer. Phased deliveries are planned from **2028 to 2030**. A separate November 2024 contract with XCMG for ancillary equipment was valued at US$400 million.

## Other electric equipment

- **$350 million deal with Epiroc** (April 2025) for 50+ autonomous electric drill rigs
- Partnerships with **BYD** (energy storage), **LONGi** (solar), and **Envision Energy** (wind turbines) for on-site renewable power generation

## Current status (early 2026)

- First diesel-powered T264 chassis delivered to Eliwana mine (Pilbara) — arriving ahead of the battery systems
- 4 autonomous trucks in validation testing at Fortescue's test site
- Full autonomous battery-electric validation expected **early 2026**
- First BEV deliveries targeted for **2026**, from both Liebherr and XCMG
- Target: eliminate all Scope 1 & 2 terrestrial emissions by **2030**

## Other miners

Fortescue is not alone, though it is furthest advanced:

- **BHP**: partnered with Caterpillar on zero-emission haul trucks (battery and hydrogen); trials underway at BMA coal operations in Queensland
- **Rio Tinto**: partnered with Caterpillar for autonomous zero-emission trucks; trialling battery-electric at Gudai-Darri iron ore mine
- **Anglo American**: developed the nuGen hydrogen-powered ultra-class haul truck, tested at Mogalakwena platinum mine (South Africa)

In China, **XCMG** deployed electric mining trucks (XDE240 BEV, 240-tonne class) at Huaneng's Yimin open-cut coal mine in Inner Mongolia, operational from 2023. The China National Coal Association targets 10,000 autonomous electric mining trucks by 2026.

---

# Diesel vs Electric Haul Trucks: Comparative Specifications

The 240-tonne class haul truck is the workhorse of Australian open-cut mining. Three vehicles define the current competitive landscape: the diesel incumbent (Cat 793F), and two battery-electric alternatives being supplied to Fortescue.

**Table: 240-Tonne Class Haul Truck Comparison**

| Specification | Cat 793F (diesel) | Liebherr T264 BEV | XCMG XDE240 BEV |
|:---|---:|---:|---:|
| Payload (tonnes) | 227 | 240 | 230 |
| Gross vehicle weight (tonnes) | 390 | 416 | ~400 |
| Empty weight (tonnes) | ~163 | ~176 | ~165 |
| Engine/motor power (kW) | 1,976 | 3,200 (peak) | 1,865 |
| Drive system | Mechanical | Battery-electric AC | Battery-electric AC |
| Battery capacity (MWh) | — | 3.2 | Not disclosed (BYD Blade LFP) |
| Fuel/energy consumption | 137–182 L/hr diesel | ~86% lower cost/tonne (Liebherr claim) | Not disclosed |
| Charging method | Refuel ~15 min | 6 MW MCS (~30 min); trolley compatible | Battery swap; also conductive |
| Purchase price (est.) | ~US$5–6M | ~US$6–8M (implied from deal) | ~US$3–4.5M (diesel); BEV est. US$3–5M |
| Annual fuel/energy cost | ~US$0.8–1.2M | ~US$0.1–0.2M (est.) | Not disclosed |
| Production status | In production, thousands deployed | Pre-production; 4 units in testing | BEV in development; diesel-electric in production |

*Sources: Cat 793F OEM specifications; Liebherr T264 product data and Fortescue deal terms; XCMG XDE240 LECTURA specs; International Mining; SRK Consulting.*

Key observations:

- The BEV trucks are **heavier empty** (~176t vs ~163t for the Cat) due to battery mass, but the Liebherr compensates with higher payload (240t vs 227t).
- The Liebherr's **6 MW MCS charger** with robotic connection enables ~30 minute charges. It also supports dynamic power transfer (trolley/pantograph) for in-pit charging while hauling.
- The XCMG uses **BYD Blade LFP cells** and supports **battery swap**, matching the approach proven at the Yimin mine fleet.
- **Regenerative braking** on the Liebherr recovers up to 3,300 kW on loaded downhill hauls — significant on deep pit ramp cycles.
- At ~US\$1M/yr diesel cost per truck vs ~US\$150k/yr electricity, the **annual saving is ~US\$850k per truck**. Against a BEV premium of ~US\$2M, payback is **under 2.5 years**.

## Other electric truck programs

| OEM | Model | Payload | Type | Status |
|:---|:---|---:|:---|:---|
| Caterpillar | 793 XE | 240 t | Full BEV | 7 "Early Learner" units testing at BHP, Rio Tinto, Newmont, Freeport, Vale |
| Komatsu | 930E Power Agnostic | 290 t | Diesel-trolley / BEV / H2 | Diesel-trolley in field test (Jul 2025); BEV pilot Q2 2026 |
| SANY | SET320S | 300 t | Hybrid (diesel + battery) | Launched Jul 2024 |
| XCMG | ZNK95 | 90 t | Full BEV (autonomous, cabless) | 100 units at Yimin mine (May 2025) |

*Sources: Caterpillar MinExpo 2024 announcements; Komatsu press releases 2025; SANY launch data; International Mining.*

---

# XCMG: A Serious Contender?

XCMG (Xuzhou Construction Machinery Group) is a Chinese state-owned enterprise founded in 1943. It is **not a newcomer** — it ranks **3rd or 4th globally** among construction and mining equipment manufacturers, with ~US$14.5 billion revenue in 2025 (~38% of Caterpillar's ~US$38 billion).

**Global equipment manufacturer rankings (KHL Yellow Table 2025):**

| Rank | Company | Revenue (approx) |
|:---:|:---|---:|
| 1 | Caterpillar | ~US$38B |
| 2 | Komatsu | ~US$25B |
| 3–4 | XCMG | ~US$14.5B |
| 3–4 | SANY | ~US$14B |
| 5 | John Deere | ~US$13B |

*Source: KHL Yellow Table 2025, Construction Briefing.*

## Mining product range

XCMG claims to be the only Chinese manufacturer offering a complete mining equipment package. Rigid haul trucks span 110–440 tonnes payload (XDE110 through XDE440). Mining excavators range from 70 to 700 tonnes. The XDE440 at 400 tonnes is the world's largest rear-drive rigid mining truck.

## Installed base

- **Inner Mongolia**: XCMG claims 50% of large-tonnage mining equipment in eastern Inner Mongolia. In the Wuhai coal region alone: 500+ mining trucks and 200+ excavators (70–300t class).
- **China Energy Investment Corp** (world's largest coal producer): fleet of XDE240 trucks.
- **International sales** (post-2019): XDE120 fleet in Australia since 2019; XDE130 recently arrived. Rio Tinto/SimFer ordered dozens of XDE240s for Simandou (Guinea). Exxaro ordered 7 XDE260s for Grootegeluk coal (South Africa). Zijin Mining operates XDE150 and XDE260 fleets in Serbia.
- **Australian service**: 8 dealers, 15 service outlets nationwide; Emeco/Force Equipment appointed as preferred service provider (5-year deal, May 2025).

## Electric mining truck deployment

The ZNK95 fleet at **Huaneng Yimin coal mine** (Inner Mongolia) is the world's largest operational electric mining truck deployment:

- 100 autonomous battery-electric trucks (90t payload, 509 kWh LFP battery, cabless)
- Operational from May 2025; up to 22 hours/day; rated to –40°C
- By November 2025: 47,800 battery swaps, 21.5 million kWh exchanged, 100M+ cubic metres hauled
- Diesel saved: 7,500 tonnes; CO2 avoided: 24,000 tonnes
- Efficiency: 120%+ vs equivalent manned diesel trucks (autonomous operation eliminates shift changes, driver fatigue)
- Planned expansion to 300 units within 3 years
- Connected via Huawei 5G-A network (500 Mbps uplink, 20ms latency)

*Sources: International Mining (Nov 2025); electrive.com (May 2025); Manila Times.*

## Quality and reliability

Industry commentary positions XCMG as **"85% performance at 60% cost"** versus Caterpillar and Komatsu. Cat and Komatsu are reported to burn 15–20% less fuel at equivalent payloads — a meaningful advantage in diesel trucks, but largely irrelevant in BEVs where energy cost is a fraction of diesel. For electric trucks, the competitive dynamic shifts from fuel efficiency to battery durability, charging infrastructure, and autonomous systems — areas where XCMG's Yimin deployment gives it more operational data than any Western OEM.

## The Fortescue contracts

Two distinct agreements:

1. **US$400 million** (November 2024): 100+ zero-emission ancillary equipment (battery-electric loaders, dozers, water carts, graders). First deployments from 2026.
2. **150–200 battery-electric haul trucks** (September 2025): XDE240 BEV, phased deliveries 2028–2030. Fortescue Zero designs the battery powertrain; XCMG manufactures the chassis.

Total Fortescue commitment to XCMG likely exceeds US$1 billion — China's largest green mining equipment export order.

## XCMG pricing

XCMG does not publicly list prices and most sales are by direct negotiation. Available data points:

- **China Energy Investment Corp** (Oct 2020) ordered a fleet of XDE240s for ~US$45 million, implying roughly **US$3–4.5M per unit** for the diesel-electric version.
- The **"85% performance at 60% cost"** industry positioning implies US$2.5–3.6M against the Cat 793F (US$5–6M) or US$3.5–4.8M against the Liebherr T264 (US$7–8M).
- Chinese domestic wide-body trucks (50–100t class) show a 70–81% cost advantage over imported equivalents.
- **Best estimate for the XDE240**: US$2.5–3.5M domestic, US$3–4.5M export (diesel-electric). The BEV version is likely US$3–5M, priced aggressively for strategic market entry.
- For comparison, used XCMG off-highway trucks average ~US$450k on MachineryTrader (all models/sizes).

*Sources: International Mining (Oct 2020, China Energy order); TNR International (wide-body market review 2025); Plant & Equipment; MachineryTrader.*

---

# The Fortescue Battery Pivot

Fortescue's approach to battery technology has undergone a significant strategic reversal that illuminates both the difficulty of competing with China's battery supply chain and the likely direction of mining electrification globally.

## Williams Advanced Engineering acquisition

In March 2022, Fortescue acquired **Williams Advanced Engineering** (WAE) — the technology spinoff of the Williams F1 team — for A\$310 million. WAE brought deep expertise in high-performance battery pack design, thermal management, and power electronics developed for Formula E and Extreme E racing. The rationale was compelling: no OEM had a production-ready multi-MWh battery pack for 240-tonne haul trucks, and Fortescue wanted to control the IP.

WAE's proprietary **Scalable Battery Module (SBM)** technology could independently scale voltage and capacity from a single building block, enabling custom-configured packs for different mining vehicles. The 3.2 MWh pack for the T264 comprises eight sub-packs, with module-level energy density >240 Wh/kg — almost certainly NMC chemistry rather than LFP.

## What went wrong

The battery program has been **three years behind schedule**. When Fortescue unveiled its first electric truck at Eliwana mine in October 2023, it was running on XCMG's own battery because the WAE pack was not ready — and wouldn't be for another three years.

The manufacturing scale-up proved far harder than anticipated:

- **January 2024**: Fortescue announced a US\$210 million Advanced Manufacturing Centre in Detroit to produce SBM-based battery packs (600 jobs)
- **September 2025**: Detroit plant **scrapped**, citing US policy changes (IRA tax credit uncertainty under the Trump administration)
- **October 2025**: UK manufacturing at WAE's Kidlington and Banbury facilities **wound down** — hundreds of the ~1,000 UK staff affected. Sites pivoting to R&D only

CEO Dino Otranto stated bluntly: ***"The reality is that we just can't compete with the supply chain out of China when it comes to price and speed."***

## The new model

Fortescue Zero is becoming an **integrator, not a manufacturer**:

- Battery cells and packs will come from Chinese suppliers (CATL and BYD are the likely sources)
- Fortescue Zero retains the IP in systems integration, thermal management, and power system architecture for Pilbara conditions
- The XCMG trucks arriving from February 2026 will use Chinese battery systems with Fortescue Zero integration
- Liebherr and Fortescue's ecosystem will be offered to other miners — but the battery manufacturing is Chinese

This pivot has broader implications. If the world's most committed mining electrification company — with A\$310 million invested in battery expertise and a A\$3+ billion equipment order — concluded it cannot compete with Chinese battery manufacturing, it is unlikely that any mining-specific Western battery venture can either. The supply chain for electric mining trucks will be Chinese, whether the chassis comes from Liebherr, XCMG, or eventually Caterpillar.

*Sources: The Driven (Oct 2023, "three year wait for WAE battery"); electrive.com (Fortescue acquires WAE, Jan 2022); International Mining (WAE rebrands, Jan 2023; Fortescue diversifying supply chain, Dec 2025); Automotive News / Crain's Detroit (Detroit plant scrapped, Sep 2025); Fortescue.com (Detroit manufacturing centre announcement, Jan 2024); Liebherr T264 BEV product page (Bauma 2025).*

---

# Electric Mining Trucks in China: Fleet Scale

China's electric mining truck fleet is far larger than commonly understood outside the industry. While Fortescue is testing 4 autonomous BEV trucks in the Pilbara, and Caterpillar has 7 BEV "Early Learner" units at customer sites, China has **thousands of electric mining trucks in daily operation**.

## Estimated total fleet

There is no single authoritative count. Aggregating from multiple industry sources, the total Chinese BEV mining truck fleet (all sizes) is estimated at **3,000–5,000 units** as of early 2026. The wide-body 50–100t class dominates numerically; the ultra-class 200t+ segment is smaller (likely a few hundred units), with the Yimin 100-truck fleet being the flagship.

## Major deployments

| Mine | Location | Trucks | OEM | Notes |
|:---|:---|---:|:---|:---|
| Xinjiang Zijin Zinc | Xinjiang | 250 | Various | World's largest single-mine BEV fleet; 80% of haulage |
| Huaneng Yimin | Inner Mongolia | 100 | XCMG ZNK95 | Autonomous, cabless, battery swap |
| Zhundong Coal | Xinjiang | 120 | Tonly TLE138 | EACON autonomous system |
| Zhibula Copper | Tibet | 60 | SANY | High altitude |
| Fushan | — | 40 | Yutong YTK90E | Autonomous |
| Dashihe Iron Ore | — | 16 | Yutong/EACON | — |
| Huolinhe Coal | Inner Mongolia | 12 | — | — |

*Sources: International Mining (Zijin Mining, Jan 2026; Zhundong, Mar 2026; Yimin, Nov 2025); electrive.com (Yimin, May 2025); EACON press releases.*

**Zijin Mining** alone has expanded from 13 electric vehicles in 2020 to **1,183 EVs** across all its mines [@im-zijin-ev-2026]. It has begun manufacturing its own electric mining trucks in partnership with Longking.

## Manufacturer market positions

| Manufacturer | Key data |
|:---|:---|
| **LGMG (Lingong)** | #1 in new energy mining trucks (2024); ~1,600 cumulative units sold by mid-2025; sales +197% H1 2025; RMB 1B revenue from new energy mining equipment |
| **XCMG** | Leads in ultra-class (200t+) BEV; 100-unit Yimin fleet; Fortescue export deal |
| **SANY** | RMB 4B revenue from new energy products (2024); 60 BEV trucks at Zhibula |
| **Yutong** | Strong in autonomous BEV; 40 units at Fushan; 31M+ operational km |
| **Tonly** | Wide-body market leader by installed base; 120 BEV trucks at Zhundong |
| **Others** | Inner Mongolia North Hauler, Aerospace Heavy Industry, Zoomlion, Longking (new entrant with Zijin) |

*Sources: International Mining (various 2025–2026); EACON press releases; chinatrucks.org (2024 sales data).*

## EACON autonomous fleet

EACON, a Chinese autonomous mining technology company, operates **800+ trucks across 19 projects** using 14 truck models from 6 OEMs. 99% of its fleet is low-emission. Total autonomous distance exceeds 27 million kilometres.

*Source: PR Newswire (EACON milestone announcement, 2024).*

## Government policy

- **April 2024 joint policy** (7 departments including Ministry of Natural Resources): targets **90% of large mines and 80% of medium mines** to meet "green mine" standards by **2028** [@us-commercial-china-mining-2024]
- 1,200+ mines nationally certified as "Green Mines"; 3,000+ at provincial level
- Green mine certification promotes electrification as one pathway to compliance (not a strict mandate)
- Operating cost economics are doing as much as policy: electric trucks run at roughly **13% of the diesel running cost**, with payback periods of ~3 years

*Sources: US Commercial Service (China green mining sector, 2024); China 14th Five-Year Plan; Work Plan for Carbon Emission Peak in Mining Industry.*

## Context for the national fleet

China's total new energy heavy truck sales (all types, not just mining) reached **82,000 units in 2024** (+140% year-on-year), of which 77,100 were pure electric (94%). Mining-specific electric truck sales are a subset of this — likely in the low thousands per year for 2024–2025, based on LGMG's 1,600 cumulative units and 197% growth rate.

*Source: chinatrucks.org (2024 heavy truck sales statistics).*

---

# Fortescue Pilbara Renewable Energy Program

Fortescue's electric fleet cannot run on diesel-generated electricity — the "Real Zero" strategy requires a parallel build-out of renewable generation and transmission across the Pilbara. The original Uaroo mega-project (5.4 GW, primarily for hydrogen export) was abandoned in October 2023, replaced by a distributed, mine-proximate approach.

Fortescue's ASX release of 10 April 2026 [@fortescue-green-grid-2026] confirms a two-phase approach:

- **Phase 1** (deployment underway, within existing decarbonisation budget): ~2 GW generation (1.2 GW solar + >600 MW wind) + 4–5 GWh battery storage. Full completion by **end 2028** (accelerated from original 2030 target). 290 MW installed by early 2027 for daytime "green processing"; 24-hour renewable power later in 2027.
- **Phase 2** (subject to FID): a further ~2 GW generation + 4 GWh batteries, deliverable in ~18 months, for **less than US\$2.5 billion**. Enabled by proprietary AI optimisation, patented technologies, and deployment experience from Phase 1.

The system is fully standalone, islanded, and off-grid — no connection to any external power system. It supports processing facilities, rail, ports, logistics, mobile fleet charging, and accommodation for ~10,000 personnel. At completion, the scale is equivalent to powering a full metropolitan residential area.

## Solar projects

| Project | Capacity | Status | Expected completion |
|:---|---:|:---|:---|
| North Star Junction | 100 MW | Operational | H2 2024 |
| Cloudbreak | 190 MW | Under construction (Apr 2025 start) | 2027 |
| Solomon Airport | 440 MW | Construction started Mar 2026 | 2028 |
| Turner River | 644 MW | Federal EPBC approval Jan 2026 | TBD |
| **Solar total** | **~1,374 MW** | | |

All solar projects use single-axis tracker technology. The **Pilbara Solar Innovation Hub** (co-funded by ARENA, \$45M) is testing autonomous piling, 5B Maverick rapid-deployment, and robotic installation across three sites.

*Sources: Fortescue.com (Solomon Airport announcement, Mar 2026); PV Magazine (Turner River approval, Jan 2026; Cloudbreak construction, Apr 2025); Mining Weekly (1.3 GW solar target, Mar 2026); ARENA (\$45M Solar Innovation Hub).*

## Wind projects

**Nullagine Wind Farm** (under construction):

- **133 MW**: 17 × Envision Energy 7.8 MW turbines
- **Nabrawind "Nabralift" self-erecting towers**: 188 m hub height — tallest onshore wind towers globally
- Construction commenced January 2026; prototype turbine at Envision test facility in China, relocating to Pilbara by June 2026

**East Pilbara Generation Hub** (EPA assessment stage):

- Up to **2.1 GW**: ~200 wind turbines (Envision + Nabrawind towers)
- Location: ~40 km SE of Marble Bar, ~90 km E of Iron Bridge mine
- Development envelope: 98,773 hectares (2,319 ha disturbance)
- EPA referral May 2025; approval expected late 2026; 32-month construction → operational ~mid 2029

*Sources: RenewEconomy (Nullagine wind farm, Jan 2026); Fortescue.com (wind construction start); EPA WA (East Pilbara Generation Hub referral); Boiling Cold (2.1 GW wind plans).*

## Battery storage

| System | Capacity | Chemistry / Supplier | Status |
|:---|---:|:---|:---|
| Solomon BESS | 16 MW | Not disclosed | Operational (2023) |
| Iron Bridge BESS | 26 MW | Not disclosed | Operational (2023) |
| North Star Junction | 50 MW / 250 MWh | BYD Blade LFP, liquid cooled | Installed Dec 2025 |
| Eliwana | 20 MW / 120 MWh | Not disclosed | Early 2026 |

Target: **4–5 GWh** total across the Pilbara network.

*Sources: PV Magazine (North Star battery delivery, Dec 2025); Fortescue.com.*

## Transmission: Pilbara Energy Connect

- **620+ km** of 220 kV transmission lines planned (480+ km already built)
- Investment: **US\$700 million**
- Connects North Star, Iron Bridge, Cloudbreak, Solomon, Eliwana, and rail network

## Electricity demand

- Current consumption: ~700 ML diesel/yr + 15 million GJ gas → ~3 Mt CO2-e/yr (88% of company emissions)
- North Star 100 MW solar generates ~250 GWh/yr ≈ 30% of Iron Bridge mine demand
- Full 2–3 GW renewable system targets 100% of stationary electricity plus mobile fleet charging
- Target: "full days of renewable power" across all ore processing by late 2027; Real Zero by 2030

### Iron Bridge magnetite: the dominant electrical load

Iron Bridge is a **225 MW** magnetite processing operation — by far the single largest electricity consumer in Fortescue's Pilbara system [@mining-tech-iron-bridge-2024]. It produces 22 Mtpa of 67% Fe magnetite concentrate from ~62.5 Mtpa of raw ore feed [@fortescue-iron-bridge-2023]. First production July 2023; ramp to nameplate expected FY2028 (delayed from original mid-2023 target).

![Iron Bridge OPF process flow. Tonnage numbers refer to LOM average.](../media/iron_bridge_opf_process_flow.png){#fig-opf-process-flow}

*Source: Fortescue Iron Bridge project approval [@fortescue-iron-bridge-approval-2019].*

The OPF (Ore Processing Facility) takes in 67 dmt of ore plus 39 dmt of waste (106 Mtpa total material movement). After dry crushing, HPGR grinding, and dry magnetic separation, 34 dmt is rejected to tailings. Only 13 dmt passes to the wet circuit (rougher and re-cleaner magnetic separation), producing 20 dmt of concentrate (22 wmmt) which is pumped via a 135 km slurry pipeline to Port Hedland.

The processing chain and its approximate power breakdown:

| Stage | Equipment | Installed MW | Share | Notes |
|:---|:---|---:|---:|:---|
| Primary & secondary crushing | Jaw + cone crushers | ~10–15 | ~5% | Rock from ~1m to ~50mm |
| **HPGR grinding** | **12 High Pressure Grinding Rolls** | **93** | **41%** | Fortescue patent; dry grinding to 80µm |
| Dry magnetic separation | 20 drum separators | ~10–15 | ~5% | First-stage rejection of ~65% of mass |
| Secondary grinding + cleaning | Fine mills + wet mag sep | ~40–60 | ~22% | Upgrade from ~50% to 67% Fe |
| Conveyors, pumps, water, services | Various | ~30–40 | ~15% | Water recovery, dewatering, stockpiling |
| **Total processing plant** | | **~225** | **100%** | |

*Sources: [@mining-tech-iron-bridge-2024] (225 MW, 12 HPGR at 93 MW installed, 20 magnetic drums); [@fortescue-iron-bridge-2023]; [@fortescue-iron-bridge-approval-2019] (OPF process flow).*

**Key insight:** grinding consumes ~60–65% of processing plant power. The 93 MW HPGR installation alone is larger than most wind farms. Conventional SAG + ball mill circuits for the same throughput would need ~120–140 MW for grinding — Fortescue's dry HPGR process saves ~30% of comminution energy and ~75% of water versus conventional wet processing.

The **mining fleet** (haul trucks, excavators, drill rigs) is separate — this is the diesel demand that the truck electrification program targets. At Iron Bridge specifically, the mining fleet is relatively small (shorter haul distances than Solomon or Eliwana), but across all Fortescue sites the fleet consumes ~700 ML diesel/yr.

## Total investment

- Pilbara Energy Connect transmission: US\$700M
- 2 GW generation + 4 GWh storage: US\$2.5B
- Total decarbonisation budget: ~A\$6.2B
- US\$2B loan secured August 2025
- Expected savings: >US\$100M/yr in fossil fuel costs; US\$2–4/wmt operating cost reduction

*Sources: Fortescue ASX announcements; Energy News (US\$2B loan, Aug 2025); ESG News; ICN Gateway (Pilbara Generation Project).*

## LCOE estimate (Phase 1 including transmission)

Using the ASX release split (1.2 GW solar + 600 MW wind) and including transmission:

| Component | Value |
|:---|---:|
| Generation + battery capex | A$3.2B (aggressive est.) |
| Transmission (620 km 220 kV) | A$1.1B (US$700M) |
| **Total capex** | **A$4.3B** |
| Solar generation (28% CF) | 2,943 GWh/yr |
| Wind generation (36% CF) | 1,892 GWh/yr |
| **Total generation** | **4,836 GWh/yr** |
| Blended CF | 30.7% |
| Annualised capex (25yr, 6% real WACC) | A$334M/yr |
| Blended O&M | A$22/MWh |
| Annual O&M | A$108M/yr |
| **LCOE** | **A$91/MWh** |

*Note: The US\$2.5B in the 10 April ASX release is Phase 2 (expansion, subject to FID), not Phase 1. Phase 1 is within the existing decarbonisation budget.*

**Capital cost reconciliation:** The budget only works at Chinese-adjacent pricing — solar ~A\$0.8M/MW, wind ~A\$1.8M/MW, battery ~A\$250/MWh. At standard Australian benchmarks (solar A\$1.3M/MW, wind A\$2.5M/MW, battery A\$500/MWh) the budget blows by ~50%. Battery cost is the key swing: 4.5 GWh at A\$500/MWh = A\$2.25B vs A\$250/MWh = A\$1.13B. Fortescue is using Envision turbines, BYD batteries, and Chinese solar panels — buying at the China price.

**Diesel comparison:**

| Scenario | Annual diesel (net of FTC) | Annual electricity | Saving | Payback on A$4.3B |
|:---|---:|---:|---:|---:|
| Normal market ($1.50/L net) | A$1,050M | ~A$350M | A$700M | 6.1 yr |
| Current crisis ($2.80/L net) | A$1,960M | ~A$350M | A$1,610M | 2.7 yr |

Fortescue's diesel is delivered by ship from Singapore to Port Hedland, then road-tankered 145–450 km to mine sites. Every 10 cpl movement = ~\$70M impact on operating costs.

---

# Charging Infrastructure Costs

The electric fleet requires substantial charging infrastructure whose cost must be added to the truck and generation economics.

## MCS (Megawatt Charging System) — Liebherr/ABB approach

**Per charger (6 MW, robotic connection):**

| Component | Cost (US$M) |
|:---|---:|
| Power electronics + rectifier | 1.5–2.5 |
| Transformer (33 kV to DC) | 0.3–0.5 |
| Robotic connection system | 0.2–0.5 |
| Controls, enclosure, cooling | 0.2–0.4 |
| **Charger unit subtotal** | **2.5–4.0** |
| Civil works (reinforced pad) | 0.2–0.4 |
| Cable trenching, grid connection | 0.2–0.5 |
| Commissioning | 0.1–0.2 |
| **Total installed per charger** | **3.0–5.0** |

At scale (50+ units) this likely drops to US$2–3.5M per charger.

**Charger-to-truck ratio:** ~1 charger per 6–8 trucks (at 75% utilisation, 3.5 charges/day × 30 min, with redundancy). A 360-truck fleet needs ~50–60 chargers.

**Grid connection:** A 10–20 MW block at a remote mine site costs US$5–10M (substation, switchgear, HV cable). The full fleet needs 200–400 MW of charging capacity, requiring US$60–120M in substations and distribution.

**Total MCS infrastructure for a 360-truck fleet:** ~US$250–350M, or **~US$700–1,000k per truck**.

*Sources: ABB eMine MCS charger specifications; McKinsey mining electrification report 2024 (US$500k–1M per truck infrastructure); ICMM/Mining3 (charging = 15–25% of total BEV fleet CAPEX); CharIN MCS standard.*

## Battery swap stations — XCMG approach

| Component | Cost |
|:---|---:|
| Swap station structure + robotics | US$5–10M per station |
| Spare battery packs (1.3–1.5× float) | US$250–400k per pack |
| Grid connection | US$1–3M per station |
| **Total infrastructure per truck** | **US$1.0–1.8M** |

Swap time: 5–8 minutes (vs 30 min MCS charge). Throughput: 5–7 swaps/hour per bay. A 20-truck fleet needs a 2-bay station.

**Key advantage for reliability:** extra battery packs at swap stations act as **distributed storage** during low-wind/cloudy periods — the user's observation that "the easy solution if there is enough transmission capacity is to have extra batteries for low wind days" is precisely the benefit of the swap model.

*Sources: XCMG product data; Chinese mining industry reports (Yimin mine operations, 2024–2025).*

## Trolley assist / dynamic power transfer

**Traditional overhead catenary:**

| Component | Cost (US$M/km) |
|:---|---:|
| Poles & overhead contact line | 1.0–1.5 |
| Substations (prorated, every 1.5–3 km) | 1.5–2.5 |
| Civil works & road preparation | 0.5–1.5 |
| Signalling, controls | 0.2–0.5 |
| **Total per km** | **3–6** |

Typical installation: 1.5–4 km (main pit ramp only). A 3 km system for 20 trucks costs US$43–80M total including truck retrofits (pantograph + electrical: US$1–2M per truck).

**Liebherr Power Rail** (side-mounted rail, not overhead): estimated 20–40% cheaper at US$2–3.5M/km. Easier to relocate. Demonstrated at MINExpo 2024 and Bauma 2025, no full-scale mine installation yet.

**Critical practical issue:** pit ramps advance every 2–5 years. Relocation costs 30–60% of initial installation (US$5–10M per event for a 3 km system). Over a 20-year mine life with 4–6 moves, lifecycle relocation costs can equal the original investment.

**Energy note:** trolley assist does not reduce total energy consumed — it shifts energy delivery from battery (charged at a pad) to direct grid supply (via catenary during haul). It eliminates ~10% battery charge/discharge losses and enables faster truck speeds on grade (1.8× on 10% grade with Power Rail). The grid still needs to supply the same total energy.

**Operating mines with trolley:** Aitik (Boliden, Sweden, 2018+); Collahuasi (Anglo American/Glencore, Chile, 2023+). Komatsu achieved the first autonomous trolley operation in May 2025.

*Sources: ABB/Hitachi Energy mining electrification publications 2022–2024; Komatsu MINExpo 2024 and autonomous trolley milestone (May 2025); Liebherr Power Rail technical spotlight (Bauma 2025); SME Mining Engineering Handbook.*

## Total mine-site electricity demand (Fortescue Pilbara)

Beyond truck charging, the renewable grid must power the entire operation:

| Load | Continuous (MW) | Notes |
|:---|---:|:---|
| Truck charging (360 trucks, avg) | ~190 | Peak 290–380 MW at shift changes |
| Iron ore processing (DSO, ~190 Mtpa) | ~25–50 | Crush & screen only; low intensity |
| Iron Bridge magnetite (22 Mtpa) | **225** | 12 HPGR (93 MW) + secondary grinding + mag sep (Fortescue/Mining Technology) |
| Rail (if electrified, ~200 Mtpa) | ~120 | Currently diesel locos; BEV locos in trial |
| Port operations (Port Hedland) | ~20–30 | Ship loaders, reclaimers, conveyors |
| Accommodation (10,000 personnel) | ~25–35 | A/C dominated in Pilbara heat |
| **Total** | **~535–660** | **Excl. rail electrification** |

Annual demand at ~600 MW continuous: ~5,256 GWh/yr — **exceeds** Phase 1 generation of ~4,836 GWh/yr. This confirms the need for Phase 2 expansion (~2 GW additional). This explains the Phase 2 expansion (additional ~2 GW) and the need for the East Pilbara 2.1 GW wind hub.

*Sources: ABB mining electrification publications; ARENA mine energy audits; Fortescue ASX release 10 April 2026; Pilbara processing plant energy benchmarks from DISER.*

---

# References

::: {#refs}
:::
