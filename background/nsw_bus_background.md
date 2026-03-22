---
title: "Australian Bus Fleet Electrification: Background and Statistics"
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

**Buses as a share of total diesel:** The same ABS survey records total Australian road transport fuel consumption at 33,019 megalitres, of which 49.1% (approximately 16.2 billion litres) is diesel [@abs-motor-vehicle-use-2020]. At 535 million litres, buses account for roughly **3.3% of road transport diesel**. The breakdown by vehicle type is shown below.

: Australian Road Transport Diesel Consumption by Vehicle Type, 2020 {#tbl-diesel-by-vehicle}

| Vehicle type | Total fuel (ML) | Diesel share | Diesel (ML) | % of road diesel |
|:-------------|----------------:|:-------------|------------:|-----------------:|
| Rigid and articulated trucks | 7,480 | 99.8% | 7,465 | 46% |
| Light commercial vehicles | 6,678 | 75.1% | 5,015 | 31% |
| Passenger vehicles | 18,094 | 20.1% | 3,637 | 22% |
| Buses | ~770 | ~70% | 535 | 3.3% |
| **Road transport total** | **33,019** | **49.1%** | **~16,200** | **100%** |

: Source: ABS Survey of Motor Vehicle Use, year ending June 2020 [@abs-motor-vehicle-use-2020]. Bus fuel figure is the ABS-reported 534.8 million litres diesel; bus total fuel estimated as residual. Diesel share for buses derived from diesel/total.

Road transport accounts for only about 60% of total Australian diesel. The remaining 40% — roughly 12 billion litres — is consumed off-road, primarily by mining (~8.2 billion litres in 2021-22), agriculture, and construction [@acapmag-diesel-2024; @atse-diesel-2024]. Total Australian diesel consumption across all sectors was approximately 30 billion litres in 2022 [@acapmag-diesel-2024].

Against total national diesel consumption of ~30 billion litres, buses represent approximately **1.8%** — a small target for decarbonisation relative to the effort required. Trucks (road freight) at ~7.5 billion litres and mining at ~8.2 billion litres are each roughly 15 times larger than the bus fleet's diesel consumption.

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

# National Comparison: Patronage and Electrification by State

## Public transport patronage by mode

The table below compiles 2023-24 patronage data for the five largest Australian capital city metropolitan areas. All figures are annual boardings in millions.

: Public Transport Patronage by Mode, 2023-24 (millions of boardings) {#tbl-patronage-by-mode}

| City | Rail | Bus | Tram / Light Rail | Ferry | Total |
|:-----|-----:|----:|------------------:|------:|------:|
| Sydney | 288 | ~300 | 39 | 14 | ~641 |
| Melbourne | 183 | ~120\* | 152 | — | ~455 |
| Perth | 62 | 84 | — | 1 | ~147 |
| Brisbane-GC | 27 | 59 | 7 | 4 | ~97 |
| Adelaide | 12 | 46 | 9 | — | ~67 |

: Sources: Sydney — NSW Bus Industry Taskforce third report [@nsw-bus-taskforce-2024] and Sydney Trains annual report [@sydney-trains-annual-report-2024]; Melbourne — Victorian Government transport patronage data [@vic-transport-patronage-2024] and Yarra Trams [@yarra-trams-facts-2025]; Perth — Public Transport Authority of WA annual report [@pta-wa-annual-report-2024]; Brisbane — Charting Transport analysis of TransLink data [@charting-transport-patronage-2025]; Adelaide — SA Department for Infrastructure and Transport annual report [@dit-sa-annual-report-2024].

\*Melbourne bus patronage is an estimate. Pre-COVID patronage was approximately 128 million [@infrastructure-vic-bus-report-2024]; the post-COVID figure has not been published in an accessible summary form. Monthly data is available from the Victorian Government open data portal [@vic-data-patronage-monthly-2025] but requires download and aggregation.

Sydney's rail figure includes Sydney Metro (21 million). Brisbane figures include Gold Coast services. All figures are boardings (not passenger-kilometres); passenger-km data by city and mode is not published in accessible form outside the BITRE yearbook [@bitre-yearbook-2024].

## Bus operator structure

All five capital cities now use **contracted private operators** for bus services — no government-operated bus fleets remain in metropolitan areas [@bic-fleet-stats-2020]:

- **Sydney** — fully privatised between 2020 and 2023. Patronage data is published by contract area but TfNSW treats per-operator patronage figures as commercial-in-confidence [@nsw-audit-bus-contracts-2024]. The operator breakdown by fleet size is shown below.
- **Melbourne** — always contracted private. Major operators: Kinetic, Dysons, Ventura, CDC Victoria. Approximately 1,800 route buses across multiple franchise areas.
- **Brisbane** — private operators under TransLink contracts (Transdev, Kinetic, others).
- **Perth** — Transperth contracts to private operators.
- **Adelaide** — Adelaide Metro contracts to private operators.

### NSW operators by fleet size

Sydney's metropolitan bus network is divided into 10 contract regions (Greater Sydney Bus Contracts, GSBC), each awarded to a private operator. Per-operator patronage figures are not published (treated as commercial-in-confidence) [@nsw-audit-bus-contracts-2024], but fleet size provides a reasonable proxy for service share. The NSW fleet totals approximately 8,000 buses across metropolitan, outer metropolitan, and regional services [@bic-fleet-stats-2020].

: NSW Bus Operators — Top 3 by Fleet Size, February 2026 {#tbl-nsw-operators}

| Operator | Buses | Electric | GSBC Regions | Area served |
|:---------|------:|---------:|:-------------|:------------|
| Transit Systems | 1,264 | 151 | 2, 3, 6 | Inner West, Parramatta, Liverpool, Macarthur |
| Busways | 1,236 | 59 | 1, 7 | Northern Beaches, North Shore, Hills, Macquarie Park |
| CDC NSW | 743 | 10 | 4, 14 | Eastern Suburbs, South, Sutherland |
| All other operators | ~4,760 | ~0 | 8, 9, 10 + outer metro + regional | Western Sydney, outer metro, regional NSW |
| **NSW total** | **~8,000** | **~220** | | |

: Sources: Transit Systems [@transit-systems-nsw-2026], Busways and CDC NSW fleet data from Wikipedia and operator websites [@busways-wiki-2026; @cdc-nsw-wiki-2026]. Electric bus counts include vehicles on order or in commissioning. NSW total from BIC [@bic-fleet-stats-2020]. "All other operators" is the residual; it includes GSBC regions 8, 9, 10, all six outer metropolitan bus contracts, and regional operators.

**Estimated patronage shares:** The three largest operators (Transit Systems, Busways, CDC NSW) together run approximately 3,240 buses — about 41% of the statewide fleet. These three cover the highest-patronage inner and middle suburban corridors, so their share of the ~300 million annual trips is likely well above 41% of the total.^[This is an author estimate. Inner-city routes have higher passenger loads per bus than outer metro and regional services. The NSW Audit Office noted that Opal tap-on accuracy is approximately 78% due to fare evasion and school students not tapping [@nsw-audit-bus-contracts-2024], so total boardings may be understated. The ~300 million figure from the Bus Industry Taskforce [@nsw-bus-taskforce-2024] covers all NSW, not just metro Sydney.]

The Bus Industry Confederation reports 43,684 commercial-use buses nationally, of which 76% are operated by private companies and 7.6% by government fleets (primarily non-metro) [@bic-fleet-stats-2020].

A public/private patronage split is therefore not meaningful for metropolitan services — it is all privately delivered under government contract. The relevant distinction between cities is fleet size and electrification pace.

## Electrification progress by state

: Bus Fleet Electrification Status, Early 2026 {#tbl-electrification-status}

| City | Total fleet | Electric in service | ZEB target | Key milestone |
|:-----|------------:|--------------------:|:-----------|:--------------|
| Sydney | ~8,000 | ~180 | All Sydney by 2035; all NSW by 2047 | 921 ordered; \$3 bn Stage 1 budget |
| Melbourne | ~4,500 | ~80 | 600 by 2035; all new ZEB from Jul 2025 | Ivanhoe, Preston depots operational |
| Brisbane | ~3,500 | ~75 trial + 60 Metro | 50% emissions by 2030; all new SEQ ZEB from 2025 | 400+ locally manufactured committed |
| Perth | ~2,000 | — | Not published | No ZEB program announced |
| Adelaide | ~1,000 | 2 | No full fleet target; 60 on order | First 2 Scania delivered Dec 2025 |

: Sources: Fleet sizes from BIC [@bic-fleet-stats-2020]; NSW — TfNSW [@tfnsw-zeb-2025; @tfnsw-zeb-3bn-2025]; Victoria — Victorian Premier [@vic-premier-600-zeb-2024; @vic-premier-zeb-roadmap-2024]; Brisbane — Queensland Government [@qld-zeb-program-2025; @qld-400-ebus-local-2024]; Adelaide — SA DIT [@dit-sa-ebus-2025; @electrive-adelaide-ebus-2025]; Perth — no published ZEB target as of March 2026.

### Victoria

Victoria's target of 600 electric buses by 2035 covers roughly 13% of the fleet — strikingly modest compared to NSW's commitment to electrify all of Greater Sydney by the same date [@vic-premier-600-zeb-2024]. A road map for full fleet electrification was published in November 2024 but sets no final target date [@vic-premier-zeb-roadmap-2024]. All new bus purchases must be zero-emission from 1 July 2025.

As of early 2026, approximately 80 electric buses are in service: 27 at Ventura's Ivanhoe depot and the first of 58 arriving at Kinetic's Preston depot [@electrive-kinetic-preston-2026]. A third depot at Dysons' Bundoora site (Melbourne's largest, built by Zenobe) is expected to complete in June 2026 [@zenobe-bundoora-depot-2025].

Melbourne's tram network — the world's largest urban tram system — carries 152 million trips per year on electric power across 24 routes and 250 km of track [@yarra-trams-facts-2025]. This already electrifies a substantial share of the city's surface public transport task, particularly in the inner city where bus routes would otherwise carry the densest loads. This may partly explain the lower urgency around bus electrification compared to Sydney, where no equivalent electric surface network exists.

### Queensland

Queensland's Zero Emission Bus Program targets a 50% reduction in bus fleet emissions by 2030 and 80% by 2035 [@qld-zeb-program-2025]. All new buses for the south-east Queensland urban network must be zero-emission from 2025, with regional fleets following by 2030.

Approximately 75 zero-emission buses were in trial across eight Queensland depots as of early 2025. Separately, the Brisbane Metro launched 60 Hess 24-metre electric articulated buses in October 2024, operating on dedicated busways with wireless fast charging (under 3 minutes per charge) [@brisbane-metro-fleet-2025]. The Metro vehicles are functionally equivalent to a tram system — grade-separated, high-frequency, fully electric — in a city that has no light rail network.^[The Gold Coast light rail (G:link) carries approximately 7 million trips per year but operates independently of the Brisbane bus network.]

The Queensland government committed to procure over 400 locally manufactured electric buses [@qld-400-ebus-local-2024].

### South Australia

Adelaide is the latest starter among the major capitals. The first two electric buses (Scania) were delivered in December 2025, with 60 on order for delivery through mid-2026 [@dit-sa-ebus-2025; @electrive-adelaide-ebus-2025]. These will displace an estimated 4,500 tonnes of CO~2~ per year. South Australia stopped procuring diesel-only buses in September 2022; new vehicles are now either diesel-electric hybrids or battery electric [@sa-ebus-energy-mag-2025].

No target date for full fleet electrification has been published. Adelaide's single tram line (Glenelg to Entertainment Centre, ~12 km) carries approximately 9 million trips per year [@dit-sa-annual-report-2024] — less than 20% of bus patronage. Unlike Melbourne, the tram network is too small to materially offset the need for bus electrification.

### The tram factor

Melbourne and Adelaide both operate electric tram networks, but the scale difference is decisive. Melbourne's tram carries 152 million trips — more than its bus network — across the densest parts of the city. Adelaide's tram carries 9 million on a single line. For Melbourne, the existing electric tram network genuinely reduces the emissions case for rapid bus electrification in the inner city. For Adelaide, the tram is too small to be relevant.

Brisbane presents a counterpoint: it has no tram system but has adopted more aggressive electrification targets than Melbourne, suggesting that political commitment and fleet age are stronger determinants of pace than the existence of trams. Brisbane's Metro project demonstrates that tram-equivalent electrification outcomes can be achieved with electric buses on dedicated infrastructure.

---

# Data Gaps

Several key metrics are not publicly reported in an accessible form:

1. **Total bus-km per year** — not in the TfNSW annual report or project pages
2. **Total fleet diesel consumption** — not published at state level; only available at the national level from the ABS motor vehicle use survey (last conducted for year ending June 2020)
3. **Electric bus energy consumption** — no published data on kWh/km for the NSW electric fleet in service
4. **Depot conversion costs** — Brookvale retrofit was \$25 million (23 bays); Macquarie Park new-build is \$145 million (~150 bays). Costs for the other 10 retrofit depots are not publicly itemised
5. **Interim charging arrangements** — where the ~127 electric buses not based at Brookvale or Leichhardt are charging is not documented
6. **Melbourne bus patronage** — no published annual total for 2023-24; monthly data exists in the Victorian Government open data portal but has not been aggregated in any accessible report
7. **Passenger-kilometres by mode and city** — only available in the BITRE yearbook; not broken out by city in any accessible online source
8. **Perth ZEB plans** — no published electrification target or program as of March 2026

These gaps make it difficult to quantify the full energy and cost implications of the transition without relying on estimates.

## Useful contacts for patronage data

The following analysts and organisations publish independent analysis of Australian public transport patronage and may be able to assist with data queries:

- **Daniel Bowen** (danielbowen.com) — patronage trends, per-capita analysis, pandemic recovery tracking
- **Philip Mallis** (philipmallis.com) — station-level patronage, Melbourne bus route data
- **Charting Transport** (chartingtransport.com) — Australian transport trends, BITRE data visualisation
- **Infrastructure Victoria** — published "Fast, frequent, fair" Melbourne bus network report [@infrastructure-vic-bus-report-2024]
- **Bus Industry Confederation** (bic.asn.au) — national fleet statistics, industry census [@bic-fleet-stats-2020]

---

# References
