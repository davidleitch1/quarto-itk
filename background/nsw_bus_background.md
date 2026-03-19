---
title: "NSW Bus Fleet Electrification: Background and Statistics"
author: "David Leitch"
date: 2026-03-16
categories: ["EVs"]
bibliography: nsw_bus_references.bib
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Summary

NSW operates around 8,000 diesel and gas buses — the largest state bus fleet in Australia [@bic-fleet-stats-2020]. The state government has committed to replacing all of them with zero-emission vehicles by 2047, with Greater Sydney completing the transition by 2035 [@tfnsw-zeb-2025]. As of late 2025, roughly 180 electric buses are in service, representing about 2% of the fleet [@cleantechnica-ebus-2025].

This note compiles available statistics on the NSW bus fleet — size, kilometres travelled, fuel consumption — and the current state of the electrification program. A notable gap in available data is that neither Transport for NSW's annual report nor its project pages publish total fleet bus-kilometres or diesel consumption figures [@tfnsw-annual-report-2024].

---

# Fleet Size and Composition

The Bus Industry Confederation's most recent fleet census (2020 data) puts the NSW public transport bus fleet at approximately 8,000 vehicles [@bic-fleet-stats-2020]. Diesel accounts for 92.7% of the fleet, with the remainder being compressed natural gas (CNG) and a small number of hybrids.

**NSW Bus Fleet Composition (2020)**

| Fuel type | Share |
|:----------|------:|
| Diesel | 92.7% |
| CNG / other | 7.3% |

*Source: Bus Industry Confederation [@bic-fleet-stats-2020]*

NSW's fleet is substantially larger than Queensland's or Victoria's — approximately 4,500 more buses than either state [@bic-fleet-stats-2020].

---

# Kilometres Travelled and Fuel Consumption

## Bus-kilometres

There is no readily accessible published figure for total annual bus-kilometres in NSW. The TfNSW Annual Report 2023-24 does not report this metric [@tfnsw-annual-report-2024].

The best available data comes from BITRE (2010), which reports average annual kilometres per bus by service type [@bitre-urban-bus-2010]:

**Average Annual Kilometres per Bus by Service Type**

| Service type | km/bus/year |
|:-------------|------------:|
| Contracted route services | 48,900 |
| Charter | 23,600 |
| Dedicated school services | 18,000 |

*Source: BITRE Information Sheet 33 [@bitre-urban-bus-2010]. Note: this data is from 2010 and covers national averages, not NSW specifically.*

**Estimated total:** Assuming a blended average of ~35,000 km/bus/year across 8,000 buses (reflecting the mix of high-utilisation route and lower-utilisation school services), total NSW bus-kilometres would be in the range of **250--300 million km per year**. This is an author estimate; official figures are not published.^[The blended average of 35,000 km reflects a fleet mix of approximately 60% route services and 40% school/charter. The BITRE data is from 2010 and utilisation patterns may have shifted.]

## Diesel consumption

The ABS Survey of Motor Vehicle Use (year ending June 2020) estimates total Australian diesel bus fuel consumption at **534.8 million litres per year** [@abs-motor-vehicle-use-2020]. This is a national figure covering all bus types.

Typical fuel consumption for a metro bus is 40--45 L/100km [@usyd-zero-emission-buses-2021], though this varies with route type, terrain, and age of vehicle.

**Estimated NSW diesel consumption:** Applying 40--45 L/100km to an estimated 250--300 million km gives a range of **100--135 million litres per year** for the NSW bus fleet. This represents roughly 20--25% of the national total, broadly consistent with NSW operating the largest state fleet.^[At current diesel prices (~\$1.80/L), this represents \$180--240 million per year in fuel costs for the NSW bus fleet.]

---

# Zero Emission Bus Program

## Targets and timeline

Transport for NSW's Zero Emission Buses Transition Plan sets the following milestones [@tfnsw-zeb-2025]:

**Zero Emission Bus Transition Targets**

| Region | Target year |
|:-------|:------------|
| Greater Sydney | 2035 |
| Outer metropolitan | 2040 |
| Regional NSW | 2047 |

*Source: Transport for NSW [@tfnsw-zeb-2025]*

The interim target is approximately 1,700 zero-emission buses on Sydney roads by end 2028 [@sustainable-bus-151-2025].

## Current fleet and orders

The TfNSW Annual Report 2023-24 records 100 zero emission buses ordered as at June 2024 [@tfnsw-annual-report-2024]. Subsequent announcements through 2025 have substantially increased that figure:

- By September 2025, the government reported 921 electric buses ordered since the March 2023 election, including a batch of 151 for Leichhardt and Kingsgrove depots [@electrive-151-order-2025].
- As of late 2025, approximately 180 electric buses were operating in Greater Sydney, plus 3 in Newcastle [@cleantechnica-ebus-2025].

**Estimated annual procurement rate required:** To reach 1,700 by end 2028 from a base of ~180 in late 2025, NSW needs to commission roughly **500 buses per year** over 2026--2028. To reach full Sydney fleet replacement by 2035 (say ~5,000 metro buses), the sustained rate would need to be similar or higher through the 2030s.

## Depot infrastructure

Depot conversion is the binding constraint on the electrification program — electric buses need overnight charging infrastructure, electrical switchgear, and grid connections that diesel depots don't have [@thedriven-depot-2025]. Stage 1 of the ZEB program has a budget of approximately \$3 billion, covering depot conversions, ~1,500 new electric buses, and \$25 million for regional trials [@tfnsw-zeb-3bn-2025].

### Program scope

The program includes 11 existing depots for full conversion, 4 for partial conversion, and one new-build [@tfnsw-depot-conversions-2025]:

- **Full conversion (11)**: Brookvale, Kingsgrove, Leichhardt, Tempe, North Sydney, Willoughby, Penrith, Smeaton Grange, South Granville, Taren Point, Menai
- **Partial conversion (4)**: Mona Vale, Waverley, Port Botany, Randwick (planning stage)
- **New-build**: Macquarie Park

### Operational depots and charging bays

As of early 2026, only two depots have operational electric bus charging infrastructure:

**Brookvale** — completed September 2025, \$25 million conversion [@nsw-brookvale-depot-2025]:

- 13 pantograph fast-charging positions (gantry-mounted, first in Australia)
- 10 plug-in chargers
- **23 charging bays total**
- 250 kW rooftop solar
- Capacity for 229 electric buses; 13 currently operational
- Fast charger can recharge a 300 km-range bus in 20 minutes to 1 hour

**Leichhardt** — fully commissioned May 2025 (Zenobe/ARENA next-generation depot trial) [@zenobe-leichhardt-2025; @arena-leichhardt-2025]:

- 5 × 120 kW DC fast chargers
- 31 × 80 kW AC chargers
- **36 charging bays total**
- 2.5 MW / 4.9 MWh stationary battery storage
- 387 kW rooftop solar PV
- 40 electric buses with 368 and 422 kWh batteries

**Total operational charging bays across Sydney: ~59**, supporting approximately 53 electric buses at those two depots. The remaining ~127 of the 180 electric buses in service across Greater Sydney are presumably using interim plug-in arrangements at other depots or operator-managed facilities — the details are not publicly documented.

### Upcoming depots

**Kingsgrove** — charging infrastructure expected to complete in 2026 [@electrive-151-order-2025]. No charger count or cost published.

**Macquarie Park** (new-build) — \$145 million purpose-built depot for ~165 electric buses, operated by Busways [@sustainable-bus-151-2025; @macquarie-park-depot-2025]:

- Mix of standard 75 kW and fast 150 kW plug-in chargers
- ~150 bus bays for standard and articulated buses
- Construction from early 2026, operational ~end 2027 to early 2028
- Former factory site

The remaining 9 depots in the full conversion list (Tempe, North Sydney, Willoughby, Penrith, Smeaton Grange, South Granville, Taren Point, Menai, and the Kingsgrove detail beyond 2026) have no published individual timelines or cost breakdowns.

## Regional trials

Twelve electric buses have been trialling in regional NSW since April 2024, operating in Armidale and the Tweed [@tfnsw-regional-ebus-2025]:

**Regional Electric Bus Trial Results (to November 2025)**

| Metric | Value |
|:-------|------:|
| Buses in trial | 12 |
| Bus-days of operation | 1,627 |
| Total km covered | 300,000+ |
| Tailpipe CO~2~ saved | ~200 tonnes |

*Source: Transport for NSW [@tfnsw-regional-ebus-2025]*

The trials are continuing through at least Term 1 2026.

---

# Bus Manufacturers and Specifications

## TfNSW procurement panel

Transport for NSW's Zero Emission Buses program sources vehicles from four manufacturers. The 319-bus order (announced January 2025) was split across all four; the 151-bus follow-on (September 2025) went to Custom Denning and Volgren, both with >50% local manufacturing content [@electrive-151-order-2025; @tfnsw-319-order-2025].

**NSW Zero Emission Bus Suppliers — Key Specifications**

| Manufacturer | Battery | Chemistry | Range | Motor | Built where |
|:---|---:|:---|---:|:---|:---|
| Custom Denning Element 2 | 382 kWh (5×76 kWh); opt. 456 kWh | NMC (Forsee Power) | ~400 km; ~500 km (6-pack) | ZF Cetrax, 300 kW | St Marys, western Sydney |
| Volvo BZL / Volgren Optimus | 282 / 376 / 470 kWh (94 kWh packs) | NCA | Up to 250 km (470 kWh) | 200 kW peak; dual to 400 kW | Chassis imported, Volgren body in AU |
| VDI-Yutong E12 | 374--423 kWh | LFP | 230--360 km | 215 kW permanent magnet | Imported (China) |
| Foton Mobility | ~350 kWh (CATL) | LFP | Not confirmed | Not confirmed | New factory, Nowra NSW (from late 2025) |

*Sources: Custom Denning [@custom-denning-150th-2025; @forsee-custom-denning-2025], Volvo Buses [@volvo-bzl-specs-2025], VDI Australia [@vdi-yutong-e12-2025], Foton/NSW Government [@nsw-foton-nowra-2025]*

## Notes on manufacturers

**Custom Denning** is the only fully Australian-built electric bus. The Element 2 uses Forsee Power ZEN PLUS NMC battery modules and a ZF Cetrax driveline. Over 150 have been delivered across Australia as of early 2025 [@custom-denning-150th-2025]. The company has also demonstrated pantograph fast charging, with 462 kWh battery configurations designed for opportunity charging routes [@custom-denning-pantograph-2025].

**Volvo BZL / Volgren** is the main international competitor. Over 140 BZL-chassis buses with Volgren bodies are in service in Australia [@volvo-bzl-specs-2025]. The lower range figure (250 km for a 470 kWh battery) compared to Custom Denning likely reflects a heavier chassis and more conservative rating methodology.

**VDI-Yutong** uses lithium iron phosphate (LFP) batteries, which are cheaper per kWh but heavier than the NMC chemistry used by Custom Denning. Yutong is the world's largest electric bus manufacturer by volume.

**Foton Mobility** has a contract for 126 buses and plans to build a 6,000 m² factory in South Nowra, subject to council approval [@nsw-foton-nowra-2025]. If delivered, this would be the second NSW electric bus manufacturing site after Custom Denning's St Marys plant.

## Deployment allocation

Of the 319-bus order, 276 are destined for **Northern Beaches and North Shore** depot regions, with the remaining 43 for services to **Western Sydney International Airport** [@tfnsw-319-order-2025].

---

# Data Gaps

Several key metrics are not publicly reported in an accessible form:

1. **Total bus-km per year** — not in the TfNSW annual report or project pages
2. **Total fleet diesel consumption** — not published at state level; only available at the national level from the ABS motor vehicle use survey (last conducted for year ending June 2020)
3. **Electric bus energy consumption** — no published data on kWh/km for the NSW electric fleet in service
4. **Depot conversion costs** — Brookvale retrofit was \$25 million (23 bays); Macquarie Park new-build is \$145 million (~150 bays). Costs for the other 10 retrofit depots are not publicly itemised
5. **Interim charging arrangements** — where the ~127 electric buses not based at Brookvale or Leichhardt are charging is not documented

These gaps make it difficult to quantify the full energy and cost implications of the transition without relying on estimates.

---

# References
