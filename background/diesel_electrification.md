---
title: "Australian Diesel Consumption: Where It Goes and What Can Be Electrified"
author: "David Leitch"
date: 2026-03-20
categories: ["EVs", "Energy"]
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

Australia consumed approximately 30 billion litres of diesel in 2022, making it the country's single largest transport fuel [@acapmag-diesel-2024]. About 60% is used on-road (trucks, utes, cars, buses) and 40% off-road (mining, agriculture, construction). This note breaks down where that diesel goes — by vehicle type, by state, and by sector — to frame the relative scale of different electrification opportunities.

The headline finding: buses consume roughly 530 million litres of diesel per year, or **1.8% of total national diesel**. Trucks consume 7.5 billion litres. Mining consumes an estimated 8--10 billion litres. Electrifying the bus fleet is worthwhile for urban air quality and emissions, but it addresses a small fraction of Australia's diesel dependence.

---

# Transport Emissions by Sub-Sector

The Climate Change Authority's 2024 Sector Pathways Review provides the official breakdown of Australia's 90 Mt CO2-e transport emissions (2022 data) by sub-sector [@cca-transport-2024]:

: Emissions in the Transport Sector, 2022 {#tbl-transport-emissions}

| Sub sector | Mt CO2-e | Share |
|:-----------|:--------:|------:|
| Cars (incl. SUVs) | 38 | 42% |
| Light commercial vehicles | 17 | 19% |
| Heavy-duty trucks and buses | 22 | 24% |
| Motorcycles | 0.2 | 0.2% |
| Railways | 4 | 4% |
| Domestic aviation | 6 | 6% |
| Domestic shipping | 2 | 3% |
| Mobile AC and transport refrigeration | 2 | 2% |
| **Total** | **90** | **100%** |

: Source: Climate Change Authority, Sector Pathways Review 2024, Table T.1 [@cca-transport-2024]. Data year 2022.

On-road vehicles account for 85% of transport emissions. Within the heavy vehicle category, the CCA further splits: **rigid trucks 8.7 Mt, articulated trucks 11.7 Mt, and buses 1.6 Mt** — confirming that articulated trucks alone produce more emissions than cars and LCVs produce from diesel.

The CCA identifies light vehicles (cars + LCV) as the most tractable abatement opportunity at 60% of transport emissions, with electric vehicles at "commercial (competitive)" readiness. Heavy vehicles at 24% are assessed as "commercial (supported)" — viable but requiring policy support. Aviation (6%), shipping (3%), and rail (4%) rely on technologies still at "demonstration" stage.

Additional data points from the review:

- Over 23% of all trucks and 14% of all buses on the road are older than 21 years (BITRE, 2023) — fleet turnover is slow
- Over 90% of truck operators are small businesses with fewer than five staff and less than \$2 million in revenue — they cannot absorb BEV price premiums without finance support
- "Return to depot" light rigid truck and bus operations account for approximately **9 Mt CO2-e** per year — the most immediately electrifiable heavy vehicle segment
- Australian road freight can be up to **130 tonnes** (including truck weight) on articulated trucks — globally unique, and beyond the capability of any current BEV
- There is currently "almost no dedicated heavy vehicle public charging available" in Australia
- Tesla's 2024 submission states that Australia is "the most difficult country in the region to install direct current (DC) fast chargers, with transformer upgrades and grid connections often taking over 1 year for utilities to complete, compared to just 6-8 weeks in other countries"

---

# Road Transport Diesel: By Vehicle Type

The ABS Survey of Motor Vehicle Use (year ending June 2020) is the most detailed breakdown of Australian road transport fuel consumption by vehicle type and fuel [@abs-smvu-2020]. It was the final edition of this survey; no update has been published since.

Total road transport fuel consumption was 33,019 megalitres, split almost equally between petrol (49.0%) and diesel (49.1%) — the first time diesel reached parity with petrol.

: Australian Road Transport Fuel Consumption by Vehicle Type, Year Ending June 2020 (megalitres) {#tbl-fuel-by-vehicle}

| Vehicle type | Petrol | Diesel | LPG/CNG/other | Total | Diesel as % of road diesel |
|:-------------|-------:|-------:|---------------:|------:|---------------------------:|
| Rigid trucks | 14 | 3,123 | 1 | 3,138 | 19.3% |
| Articulated trucks | 0 | 4,342 | 0 | 4,342 | 26.8% |
| Light commercial vehicles | 1,578 | 5,014 | 87 | 6,678 | 30.9% |
| Passenger vehicles | 14,455 | 3,128 | 511 | 18,094 | 19.3% |
| Buses | 21 | 530 | 40 | 591 | 3.3% |
| Non-freight trucks | 1 | 74 | 0 | 75 | 0.5% |
| Motor cycles | 102 | 0 | 0 | 102 | 0.0% |
| **Total** | **16,170** | **16,211** | **639** | **33,019** | **100%** |

: Source: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020], Table 5.

Key observations:

- **Trucks (rigid + articulated) account for 46% of road diesel** at 7,465 ML. They are almost exclusively diesel-powered (99.8%).
- **Light commercial vehicles (LCVs) are the second largest** at 5,014 ML (31%). These are utes, vans, and cab-chassis under 3.5 tonnes GVM — HiLux, Ranger, Transit, Sprinter etc. Three-quarters of LCV fuel is diesel.
- **Passenger vehicles** consume 3,128 ML of diesel (19%), reflecting the large number of diesel SUVs and 4WDs.
- **Buses at 530 ML are 3.3%** of road diesel — a useful but modest electrification target.

## Vehicle type definitions

The ABS classification boundary between a light commercial vehicle and a truck is **3.5 tonnes Gross Vehicle Mass (GVM)**. This aligns with the Australian Design Rules (ADRs) heavy vehicle threshold and, broadly, with state driver licence classes.^[Most states allow a car licence holder to drive vehicles up to 4.5 tonnes GVM, but the ABS/ADR statistical classification boundary is 3.5 tonnes.] Trucks are further split into rigid (single body) and articulated (prime mover plus trailer).

---

# Road Transport Diesel: By State

The same ABS survey provides fuel consumption by state of vehicle registration.

: Road Transport Diesel Consumption by State, Year Ending June 2020 (megalitres) {#tbl-diesel-by-state}

| State | Trucks | LCV | Passenger | Buses | Other | Total diesel | % of national |
|:------|-------:|----:|----------:|------:|------:|-------------:|--------------:|
| NSW | 1,955 | 1,429 | 797 | 177 | 15 | 4,373 | 27.0% |
| VIC | 1,932 | 1,174 | 794 | 102 | 25 | 4,027 | 24.8% |
| QLD | 1,828 | 1,182 | 709 | 107 | 19 | 3,844 | 23.7% |
| WA | 985 | 672 | 409 | 73 | 7 | 2,147 | 13.2% |
| SA | 519 | 297 | 250 | 36 | 4 | 1,105 | 6.8% |
| TAS | 153 | 144 | 81 | 12 | 2 | 393 | 2.4% |
| NT | 67 | 65 | 48 | 11 | 1 | 191 | 1.2% |
| ACT | 25 | 52 | 41 | 14 | 1 | 131 | 0.8% |
| **Australia** | **7,465** | **5,014** | **3,128** | **530** | **74** | **16,211** | **100%** |

: Source: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020], Table 5. "Trucks" combines rigid and articulated. "Other" includes non-freight trucks and motorcycles (negligible diesel).

Key observations:

- **NSW, VIC, and QLD** each consume 4,000--4,400 ML of road diesel — together accounting for 75% of the national total.
- **WA is disproportionately truck-heavy** relative to its population, reflecting long-haul freight distances and mining-related road transport.
- **Bus diesel is concentrated in NSW** (177 ML, 33% of national bus diesel), consistent with NSW operating the largest state bus fleet (~8,000 vehicles).

---

# Off-Road Diesel: Mining, Agriculture, Construction

Road transport accounts for approximately 60% of total Australian diesel consumption. The remaining 40% — roughly 12 billion litres — is consumed off-road and is not captured in the ABS motor vehicle use survey [@acapmag-diesel-2024].

The three major off-road sectors are:

**Mining** is the dominant off-road diesel consumer. The mining industry claims approximately 45% of the \$7.8 billion Fuel Tax Credits Scheme (FY 2022-23), implying credits on roughly \$3.5 billion worth of diesel [@australia-institute-ftc-2024]. At current diesel prices, this implies mining diesel consumption of approximately **8--10 billion litres per year** — comparable in scale to all road freight combined.^[This is an author estimate derived from fuel tax credit claims. The \$3.5 billion in mining FTC at ~\$0.48/L credit rate and ~\$1.80/L diesel price implies approximately 7--10 billion litres, depending on assumptions about credit rates and non-diesel claims. The ATSE report confirms mining as the dominant off-road diesel sector [@atse-diesel-2024].]

**Agriculture, forestry, and fishing** are significant but much smaller diesel consumers. These sectors combined claim approximately \$1.3 billion in fuel tax credits — roughly one-third of mining's share [@australia-institute-ftc-2024]. Diesel accounts for 84% of on-farm energy consumption, powering tractors, harvesters, irrigation pumps, and generators.

**Construction** relies on diesel for earthmoving equipment, cranes, and generators, but is less well-quantified in public data than mining or agriculture.

---

# Total Diesel Budget

Combining road and off-road consumption:

: Estimated Australian Diesel Consumption by Sector, ~2022 {#tbl-diesel-total}

| Sector | Diesel (billion litres) | Share |
|:-------|------------------------:|------:|
| Road freight (rigid + articulated trucks) | 7.5 | 25% |
| Light commercial vehicles (utes, vans) | 5.0 | 17% |
| Passenger vehicles (diesel cars, SUVs) | 3.1 | 10% |
| Buses | 0.5 | 2% |
| Mining | 8--10 | 28--33% |
| Agriculture, forestry, fishing | 2--3 | 7--10% |
| Construction and other off-road | 2--3 | 7--10% |
| **Total** | **~30** | **100%** |

: Sources: Road transport from ABS Cat. 9208.0 [@abs-smvu-2020]; total diesel and 60/40 road/off-road split from ACAPMA [@acapmag-diesel-2024]; mining and agriculture shares from Australia Institute analysis of fuel tax credit claims [@australia-institute-ftc-2024]; ATSE decarbonising diesel report [@atse-diesel-2024]. Off-road figures are author estimates and should be treated as indicative.

---

# Electrification Implications

The relative scale of these sectors frames the electrification opportunity:

**Buses (0.5 BL, 2%)** — smallest of the road transport categories but the most tractable. Electric buses are commercially available, depot-based charging is straightforward, and routes are predictable. Every state has at least announced a ZEB program. The emissions benefit is concentrated in urban areas where air quality matters most. But even complete bus electrification would displace less than 2% of national diesel.

**Light commercial vehicles (5.0 BL, 17%)** — the fastest-growing diesel segment and the next major electrification frontier. Electric utes (e.g. BYD Shark, LDV eT60) and electric vans (e.g. Mercedes eSprinter, Ford E-Transit) are entering the Australian market. Fleet turnover is faster than for trucks, but the diversity of use cases (tradies, farmers, couriers) makes a single solution harder.

**Trucks (7.5 BL, 25%)** — the largest road transport diesel consumer. Battery-electric trucks are viable for urban delivery (rigid trucks), but long-haul articulated routes face range and charging infrastructure challenges. Hydrogen fuel cells may play a role for interstate freight. This is a harder, longer electrification task than buses.

**Mining (8--10 BL, 28--33%)** — the single largest diesel sector. Mine electrification is underway (battery-electric haul trucks, electric underground loaders) but is at an earlier stage than bus electrification. The prize is enormous: eliminating mining diesel would be equivalent to electrifying the entire national bus fleet roughly 18 times over. The Fuel Tax Credits Scheme, which subsidises mining diesel at approximately \$0.48/litre, is a significant policy lever.

**Agriculture (2--3 BL, 7--10%)** — electrification is at an early stage. Electric tractors exist but are not yet at scale for broadacre farming. Diesel generators for irrigation are more readily replaceable with solar+battery systems.

---

# Trucks: The Largest Road Diesel Consumer

Trucks consume 7,465 ML of diesel per year — 46% of road diesel and 25% of total national diesel. The ABS data allows us to break this down by weight class, body type, and area of operation, which matters because each segment faces very different electrification prospects [@abs-smvu-2020].

## By weight class

The ABS distinguishes rigid trucks (single body) from articulated trucks (prime mover plus trailer), and further subdivides each by gross vehicle mass (GVM) or gross combination mass (GCM):

: Truck Diesel Consumption by Weight Class, Year Ending June 2020 (megalitres) {#tbl-truck-diesel-weight}

| Category | Diesel (ML) | Share of truck diesel | Typical vehicles |
|:---------|------------:|----------------------:|:-----------------|
| Rigid ≤8t GVM | 746 | 10.0% | Light delivery, furniture movers |
| Rigid 8--20t GVM | 813 | 10.9% | Medium rigids, tippers, concrete agitators |
| Rigid >20t GVM | 1,564 | 20.9% | Heavy rigids, garbage trucks, tankers |
| **Rigid total** | **3,123** | **41.8%** | |
| Articulated ≤30t GCM | 22 | 0.3% | Light semis (rare) |
| Articulated 30--40t GCM | 281 | 3.8% | Standard semitrailers |
| Articulated >40t GCM | 4,040 | 54.1% | B-doubles, road trains, heavy haulage |
| **Articulated total** | **4,342** | **58.2%** | |
| **All trucks** | **7,465** | **100%** | |

: Source: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020], Table 18. Diesel only; petrol truck consumption is negligible (14 ML total).

The dominant segment is clear: **articulated trucks over 40 tonnes** consume 4,040 ML — more than half of all truck diesel, and more than all rigid trucks combined. These are the B-doubles and road trains on the Hume, Pacific, and interstate highways.

## By area of operation

Where trucks operate determines whether electrification is feasible with current battery technology:

: Truck Kilometres by Area of Operation, Year Ending June 2020 (million km) {#tbl-truck-km-area}

| Area | Rigid (M km) | Rigid % | Articulated (M km) | Artic % |
|:-----|-------------:|--------:|--------------------:|--------:|
| Capital city | 5,536 | 50% | 1,717 | 21% |
| Other urban | 2,193 | 20% | 901 | 11% |
| Other areas (rural) | 2,768 | 25% | 3,517 | 43% |
| Interstate | 479 | 4% | 2,047 | 25% |
| **Total** | **10,976** | **100%** | **8,181** | **100%** |

: Source: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020], Table 7.

The split is striking:

- **Rigid trucks are overwhelmingly urban** — 70% of rigid truck km are in capital cities or other urban areas. These are the delivery trucks, waste collection vehicles, and construction trucks that operate from urban depots with predictable daily routes.
- **Articulated trucks are overwhelmingly non-urban** — 68% of articulated km are in rural areas or interstate. These are the long-haul vehicles doing 500--1,500 km per day on highways.

## Electrification implications by segment

This data suggests truck electrification will proceed in two distinct waves:

**Urban rigids (near-term, ~3,100 ML diesel)** — rigid trucks under 20 tonnes operating in capital cities are the most tractable segment. Daily routes of 150--250 km with return-to-depot overnight are well within battery-electric range. Fuso eCanter, Volvo FL Electric, and Mercedes eActros are already on sale in Australia. Australia Post operates electric delivery trucks. Garbage trucks (heavy rigids) are an excellent use case: stop-start urban routes with regenerative braking, and councils can install depot charging. This segment alone consumes more diesel than the entire national bus fleet (3,123 ML vs 530 ML).

**Long-haul articulated (harder, ~4,340 ML diesel)** — articulated trucks over 40 tonnes doing interstate runs face fundamental challenges: 4,040 ML of diesel at typical consumption rates implies routes that require 1,000+ km range under load. Battery weight displaces payload. Highway charging infrastructure for megawatt-scale charging barely exists. This segment may require hydrogen fuel cells, catenary wires on key corridors, or battery-swap systems — none of which are commercially proven at scale in Australia.^[The National Heavy Vehicle Regulator (NHVR) has allowed an additional 0.5 tonne GVM for zero-emission heavy vehicles to partly offset battery weight, but this does not solve the range challenge for long-haul routes.]

The policy implication is clear: urban rigid truck electrification is achievable with current technology and should be prioritised alongside bus electrification. It addresses six times more diesel than buses.

---

# International Comparison: Truck and LCV Electrification

Australia is a laggard in commercial vehicle electrification. Comparing electric truck and van adoption rates across major markets reveals how far behind Australia sits — and which markets offer leading indicators.

## Electric truck adoption by market

: Electric Truck Share of New Registrations, Selected Markets {#tbl-intl-truck-ev}

| Market | Electric truck share (new sales) | Year | Key driver |
|:-------|:--------------------------------:|:----:|:-----------|
| China | ~15% (NEV heavy trucks) | 2025 | Battery-swap infrastructure, purchase subsidies, urban access restrictions |
| EU | 4.2% (electric + plug-in) | Q1--Q3 2025 | CO2 standards, urban LEZs, fleet mandates |
| UK | 1.4% | 2025 | ZEV mandate (10% of new trucks by 2030) |
| Australia | <1% | 2025 | No heavy vehicle CO2 standard; NVES covers only vehicles <4.5t GVM |

: Sources: ACEA commercial vehicle registrations [@acea-cv-registrations-2025]; SMMT [@smmt-ev-vans-2025]; author estimates for China and Australia based on industry reports.

### China: scale through battery-swap and policy

China dominates global electric truck deployment. Chinese manufacturers — led by BYD, Foton, FAW Jiefang, and Sinotruk — produce electric trucks at price points well below Western equivalents, supported by CATL's battery-swap network (see charging infrastructure section below). Urban access restrictions in major cities provide a powerful demand-pull: diesel trucks face curfews or outright bans in city centres, while electric trucks receive exemptions and preferential registration [@catl-swap-route-2025].

China's approach differs fundamentally from the West: rather than relying solely on battery capacity for range, the battery-swap model separates the battery from the vehicle, reducing upfront cost by 30--40% and enabling 5-minute refuelling stops. This makes electric trucks cost-competitive with diesel for fixed urban and regional routes.

### European Union: mandate-driven transition

The EU's CO2 standards for heavy-duty vehicles require a **45% reduction in fleet-average CO2 by 2030** (from 2019 baseline) and **90% by 2040**. These are the world's most stringent heavy vehicle emissions standards. Combined with proliferating urban low-emission zones and road tolling differentials, they are driving rapid fleet investment.

The Milence joint venture (Daimler Truck, Traton/VW, Volvo) is building a dedicated heavy vehicle charging network across Europe, with 30 public charging hubs operational as of early 2026 and plans for 1,700 charging points by 2027 [@milence-solutrans-2025]. Every major European truck OEM (Mercedes-Benz, Volvo, Scania, MAN, DAF) now offers battery-electric models.

A landmark signal: **Simon Loos**, one of Europe's largest refrigerated transport companies, ordered 210 battery-electric trucks in March 2026 — moving from pilot to fleet-scale procurement [@simon-loos-2026].

### United Kingdom

The UK's ZEV mandate targets 10% zero-emission truck sales by 2030 and 100% by 2040. At 1.4% in 2025, the UK is behind the EU but ahead of Australia. Urban clean air zones (London ULEZ, Birmingham, Bristol) provide additional incentive for urban delivery fleets.

### Australia: no heavy vehicle standard

Australia has **no CO2 standard for heavy vehicles** above 4.5 tonnes GVM. The NVES covers passenger vehicles and light commercial vehicles but explicitly excludes trucks and buses. This is the single most significant policy gap. Without a mandate or pricing signal, Australian fleet operators face no regulatory pressure to transition from diesel.

The few electric trucks operating in Australia are pilot deployments: Australia Post's Fuso eCanters, Woolworths' Zenobe-leased last-mile trucks [@cefc-zenobe-2025], and New Energy Transport's Windrose E1400s on the Sydney--Hunter corridor [@net-windrose-480km-2025]. These demonstrate viability but represent a negligible share of the ~600,000 registered trucks.

### Vietnam and emerging markets

VinFast, Vietnam's largest automaker, has focused its electric vehicle strategy on passenger cars, buses, and taxis rather than freight trucks. VinFast's VF Wild electric pickup targets the US market and is positioned as a lifestyle vehicle rather than a commercial workhorse. Vietnam's commercial vehicle electrification is at a very early stage, with most progress in electric buses for urban transit.

The more relevant emerging-market development is China's export of electric trucks and battery-swap technology. Chinese OEMs including BYD and Windrose are now selling electric trucks in Southeast Asia, the Middle East, Latin America, and Oceania — potentially bypassing the traditional Western OEM pathway.

---

# Charging Infrastructure for Heavy Trucks

The viability of long-haul electric trucking depends on charging infrastructure as much as on vehicle technology. Two competing models have emerged: **battery-swap** (dominant in China) and **megawatt conductive charging** (the emerging global standard). Tesla Semi and Windrose — the two vehicles most relevant to the Australian market — have both chosen fast charging.

## Battery-swap: China's approach

CATL, the world's largest battery manufacturer, operates a heavy-truck battery-swap network through its subsidiary Qiji Energy. The system uses a standardised "75#" swap block with a capacity of **171 kWh per module** — trucks carry one to three modules depending on range requirements. Each swap station holds 24 battery packs and is compatible with over 95% of mainstream Chinese heavy-truck models [@catl-swap-standard-2025].

Key metrics:

- **Swap time:** approximately 5 minutes
- **Stations operational:** ~305 heavy-truck stations at end 2025, targeting 900 by end 2026
- **OEM partners:** 30+ truck models from Sinotruk, FAW Jiefang, Foton, DeepWay, and SAIC
- **Longest route:** 1,250 km Shanghai--Chengdu Expressway corridor with 12 stations [@catl-swap-route-2025]
- **2030 target:** coverage of ~180,000 km of routes and 80% of China's truck transport corridors

Under the "separation of vehicle and battery" model, truck buyers pay only for the vehicle, reducing upfront capital by 30--40%. CATL claims each truck saves 30,000--60,000 yuan (A\$6,500--13,000) per year in operating costs.

**Outside China, battery-swap for heavy trucks barely exists.** The only significant initiative is Germany's eHaul research project, which built Europe's first automated truck battery-swap station at Lubbenau — swapping 440 kWh batteries in approximately 10 minutes for trucks up to 40 tonnes [@ehaul-2026]. A DIN standard (DIN SPEC 91533) for truck battery swapping is expected in Q1 2026, with NIO contributing. But this remains at research stage, not commercial deployment.

## Megawatt Charging System (MCS): the global standard

The Megawatt Charging System (MCS) is an open standard developed by CharIN e.V., the same industry body behind the CCS charging standard. MCS is designed specifically for heavy-duty commercial vehicles [@charin-mcs-2025].

**Specifications:**

- Maximum power: **3.75 MW** (3,000 A at 1,250 V DC)
- Purpose-built connector with liquid cooling, larger than CCS
- Formally published standard; vehicles shipping with MCS ports from 2026

**Current and planned deployments:**

: MCS Charging Network Deployments, Early 2026 {#tbl-mcs-deployments}

| Operator | Geography | MCS hubs operational | MCS points planned | Target date |
|:---------|:----------|---------------------:|--------------------:|:------------|
| Milence (Daimler/Traton/Volvo JV) | 8 EU countries | 3 | 284 across 71 locations | 2027 |
| E.ON / Voltix / GreenWay (HDV-E) | 9 EU countries | 0 | 330 across 55 locations | 2028 |
| Tesla (Megacharger) | US | 0 | 66 sites identified | 2026--27 |

: Sources: Milence [@milence-solutrans-2025]; E.ON [@eon-mcs-2025]; Tesla [@tesla-megacharger-2026].

Milence's three operational MCS hubs — at Zwolle (Netherlands), Port of Antwerp-Bruges (Belgium), and Landvetter (Sweden) — are building towards **Europe's first MCS corridor** from Antwerp to Stockholm, over 1,500 km along TEN-T freight routes.

**Truck OEM support for MCS:**

Every major Western truck OEM has committed to MCS:

- **Scania** (Traton): MCS commercially available from early 2026 [@scania-mcs-2026]
- **Volvo Trucks:** FH Aero Electric with 780 kWh battery, 600 km range, orders open Q2 2026 [@volvo-electric-longhaul-2025]
- **Mercedes-Benz:** eActros 600 in production since November 2024, MCS customer trials in H2 2026 [@daimler-eactros-mcs-2026]
- **MAN** (Traton): successful MCS interoperability tests with Kempower chargers

## Tesla Semi and Megacharger

Tesla has chosen a **proprietary Megacharger** system rather than the CharIN MCS standard, though power levels are comparable. In December 2025, Tesla released footage showing a Semi drawing **1,206 kW (1.2 MW)** during a live charging session — sufficient to replenish approximately 640 km of range in 30 minutes [@tesla-semi-charging-2025].

Tesla has identified 66 Megacharger sites across the US, with 37 expected to open in 2026 and a target of 46 operational by early 2027. Sites are planned at Pilot Travel Centers along major freight corridors in California, Georgia, Nevada, New Mexico, and Texas.

**Production status:** Tesla's dedicated Semi factory in Nevada is nearing completion, with volume production targeted for 2026. Currently only ~100 pre-production units operate (primarily with PepsiCo). Tesla's proprietary connector — separate from both CCS and MCS — raises interoperability questions, though Tesla has historically opened its passenger vehicle Supercharger network.

## Windrose: fast charging comes to Australia

Windrose Technology is a Chinese-origin electric truck company (founded in Hefei, now headquartered in Antwerp) that is particularly relevant to Australia through its partnership with **New Energy Transport (NET)**.

**The Windrose E1400:**

- 1,400 hp peak (1,044 kW) from four motors across dual drive axles
- 729 kWh LFP battery (860 kWh option for Australian B-double configuration)
- 670 km range at 49 tonnes GCW
- 68-tonne B-double capability for Australian operations
- 800V high-voltage platform

Windrose has firmly chosen conductive fast charging over battery swap, demonstrating multiple high-power approaches:

- **Dual CCS2:** two 350 kW chargers delivering >650 kW simultaneously (demonstrated with Terawatt Infrastructure, June 2025) [@windrose-terawatt-2025]
- **MCS standard:** demo with Autel MaxiCharger in Roosendaal, Netherlands (March 2026) delivering 1.2 MW via MCS connector [@windrose-autel-mcs-2026]

**Australian deployments:** NET completed Australia's longest single-charge electric truck delivery — a 480 km round trip from Picton (south of Sydney) to Beresfield (Hunter region) carrying 36 tonnes, arriving 40 minutes faster than diesel due to superior uphill performance [@net-windrose-480km-2025]. NET has secured a site at Wilton (80 km southwest of Sydney) for Australia's largest heavy electric trucking depot, supporting up to 50 trucks, with plans to expand to Adelaide--Melbourne--Sydney--Canberra--Brisbane routes and a fleet of 200+ trucks by 2031.

## Which approach is winning?

**Megawatt conductive charging is the emerging global standard.** Every major Western truck OEM (Daimler, Volvo, Traton/Scania/MAN) has aligned behind MCS. Tesla is at comparable power levels with a proprietary connector. Windrose supports both CCS2 and MCS.

Battery swap is a viable and rapidly scaling solution within China — where CATL can enforce standardisation across domestic OEMs, government policy supports the model, and 305 stations already operate. But outside China, no commercial battery-swap network for heavy trucks exists.

: Battery Swap vs Megawatt Charging: Head-to-Head Comparison {#tbl-swap-vs-mcs}

| Dimension | Battery swap (CATL/China) | MCS / fast charging (global) |
|:----------|:--------------------------|:-----------------------------|
| Turnaround time | ~5 minutes | 20--45 minutes (improving) |
| Upfront truck cost | Lower (battery leased) | Higher (battery included) |
| Infrastructure cost per site | Very high (24 packs at 171 kWh each) | Lower, but grid upgrades needed |
| Grid impact | Lower (batteries charged off-peak) | Higher (MW-scale demand spikes) |
| OEM buy-in | Chinese domestic OEMs only | All major global OEMs |
| Standardisation | Single standard within China | CharIN MCS (open); Tesla proprietary |
| Geographic reach | China only (as of 2026) | Europe, North America, Australia |

The charging speed gap is narrowing. BYD's 1.5 MW "Flash Charging" technology — demonstrated for passenger vehicles but applicable to trucks — achieves 10--97% charge in 9 minutes. At these power levels, the time penalty of conductive charging versus swap becomes marginal when including time to enter and exit a swap station.

The most likely long-term outcome is **regional bifurcation**: battery swap in China (where it has critical mass and government support), and MCS conductive charging everywhere else. For Australia, this means the relevant technology pathway is MCS — and the critical gap is not vehicle availability but **charging infrastructure on key freight corridors**.^[Australia has no publicly accessible heavy-vehicle megawatt charging stations as of March 2026. NET's Wilton depot will be the first significant installation.]

---

# Long-Haul Electric Trucks: The Contenders

The articulated truck segment — 4,040 ML of diesel per year, 54% of truck diesel, 13% of total national diesel — is the hardest to electrify and the biggest prize. As of early 2026, five manufacturers offer or have announced battery-electric trucks for long-haul operations at 40+ tonnes GCW. Their specifications, charging capabilities, and Australian availability differ markedly.

## Head-to-head comparison

: Long-Haul Battery-Electric Trucks: Specifications Comparison {#tbl-longhaul-trucks}

| | Mercedes eActros 600 | Volvo FH Aero Electric | Scania R 450e | DAF XF/XG Electric | Windrose E1400 | Tesla Semi |
|:---|:---|:---|:---|:---|:---|:---|
| Battery (kWh) | 621 (3×207 LFP) | 780 (8 packs) | 240--728 (modular) | 210--525 (LFP) | 729--860 (LFP) | ~900 (est.) |
| Range (km) | 500 | 600 | 390--520 | 500+ | 670 (at 49t) | 800 (at 37t) |
| Peak charge (kW) | 400 (CCS2) | MCS-ready | 375 CCS / 750 MCS | 325 (CCS only) | 650 dual-CCS / 1,200 MCS | 1,200 (proprietary) |
| Max GCW (tonnes) | 44 | 48 | 64 | 50 | 68 (B-double) | 37 (US Class 8) |
| Peak power (kW) | 400 (continuous) | 490 | 450 | 350 | 1,044 (4 motors) | ~750 (est.) |
| MCS support | Customer trials H2 2026 | Yes (from launch) | Ex-works early 2026 | No (CCS only) | Demonstrated Mar 2026 | No (proprietary) |
| Production status | Series Nov 2024 | Orders Q2 2026 | In production late 2023 | XD/XF Sep 2025, XG Jan 2026 | Pre-production | ~100 units (pre-prod) |
| Price (est.) | EUR 400k | EUR 255k (est.) | Not disclosed | Not disclosed | Not disclosed | US\$250k (est.) |
| In Australia | No | Yes (FH Electric) | Yes (approved May 2025) | Trial models shown | Yes (NET fleet) | No |

: Sources: Mercedes-Benz [@daimler-eactros-mcs-2026; @daimler-eactros-vandijck-2025]; Volvo [@volvo-electric-longhaul-2025; @volvo-linfox-2025]; Scania [@scania-mcs-2026; @scania-australia-2025]; DAF [@daf-electric-2026]; Windrose [@windrose-autel-mcs-2026; @windrose-electrive-2025]; Tesla [@tesla-semi-charging-2025].

## European sales: who is winning?

The EU registered approximately 4,991 battery-electric heavy trucks (>16 tonnes) in 2025 — a ~70% increase year-on-year but still only 2.0% of total heavy truck registrations. The biggest story of the year was Mercedes seizing market leadership from Volvo, which had led the segment for five consecutive years [@acea-ze-trucks-2025; @icct-hdv-2025].

: Battery-Electric Heavy Truck Registrations in the EU, 2025 {#tbl-eu-etruck-sales}

| Rank | Manufacturer | Est. ZE heavy truck sales | EU segment share | Key model | Notes |
|:-----|:-------------|:-------------------------:|:----------------:|:----------|:------|
| 1 | Mercedes-Benz | ~1,750 | 35% | eActros 600 | From ~10% share in 2024 to 35%; 1,400 units in Q3--Q4 alone |
| 2 | Volvo | ~1,000--1,200 | 20--25% | FH Electric | Led 2019--2024 (47% share); 5,700+ cumulative worldwide |
| 3 | Renault (Volvo Group) | ~750--900 | 15--18% | E-Tech range | Strong in France and Benelux |
| 4 | MAN | ~620 | 12--15% | eTGX | Series production mid-2025; +168% YoY (trucks + buses) |
| 5 | Scania | ~602 (global, all ZE) | modest | R 450e + others | +126% YoY from 266 in 2024; figure includes all ZE types |
| 6 | DAF | low hundreds | <1% | XD/XF Electric | Series production only began Q4 2025 |

: Sources: ACEA full-year 2025 commercial vehicle registrations [@acea-ze-trucks-2025]; ICCT Race to Zero EU HDV market report [@icct-hdv-2025]. Renault estimates are author calculations from Volvo Group combined share. Scania figure is global all zero-emission vehicles, not EU heavy trucks only.

The top three national markets were Germany (1,398 registrations, +38% YoY), Netherlands (878, +83%), and France (861, +28%) — together accounting for roughly two-thirds of all EU electric heavy truck registrations.

The EU's CO2 reduction target for heavy vehicles (15% cut effective 1 July 2025) was a key driver, pushing manufacturers — particularly Mercedes — to accelerate deliveries in H2 2025. The eActros 600 accounted for approximately 90% of Mercedes' zero-emission heavy truck sales, with major fleet orders from Amazon (200+ units) and Simon Loos (210 units) signalling the shift from pilot to fleet-scale procurement.

## Mercedes eActros 600

The eActros 600 entered series production in November 2024 at the Worth am Rhein plant and has accumulated over 2,000 orders — the largest backlog of any European electric truck [@daimler-eactros-mcs-2026]. Key metrics:

- **621 kWh** usable from three 207 kWh LFP packs, mounted below the chassis
- **500+ km range** at 40-tonne GCW, verified in third-party testing
- **Kerb weight** ~11.7 tonnes — comparable to a diesel Actros (the LFP battery chemistry is heavier than NMC but cheaper and safer)
- **CCS2 at 400 kW** currently, with MCS customer trials scheduled for H2 2026 at tested rates of 1 MW
- **International Truck of the Year 2025**

Real-world validation: Belgian logistics company Vandijck completed a 1,530 km multi-day trip from Belgium to southern France in an eActros 600, averaging 96.3 kWh/100 km — within 5% of Mercedes' quoted efficiency and demonstrating the truck can handle hub-to-hub linehaul on European routes [@daimler-eactros-vandijck-2025]. Amazon has ordered 200 units for European distribution.

**Australian relevance:** The eActros 600 is not sold in Australia and no local introduction has been announced. At 44-tonne GCW it is designed for European regulations and cannot operate as a B-double (68t) or even a standard Australian semi (42.5t GCM without B-double trailer). It remains an important benchmark for technology maturity.

## Volvo FH Aero Electric and FH Electric

Volvo offers two long-haul platforms:

**FH Aero Electric** (announced May 2025, orders from Q2 2026): the next-generation platform with 780 kWh battery, 600 km range, and MCS from launch. Full charge in approximately 40 minutes at megawatt rates. At 48-tonne GCW it exceeds the eActros but remains below Australian B-double requirements [@volvo-electric-longhaul-2025].

**FH Electric** (current generation, already in Australia): Volvo is the clear market leader in Australian electric heavy vehicles:

- **Linfox** has ordered 30 Volvo FH Electric trucks — the largest electric truck order in Australian history, backed by AUD 70 million in CEFC concessional finance [@volvo-linfox-2025; @cefc-volvo-2025]
- Volvo has committed to **local manufacturing** at its Wacol (Brisbane) facility from 2026, with electric trucks assembled alongside diesel models
- Current FH Electric models operate at up to 44-tonne GCW in Australia

Volvo's strategy of local manufacturing plus government-backed fleet finance is the most mature pathway to electric truck adoption in Australia.

## Scania R 450e

Scania (Traton Group) takes a modular approach:

- **Modular battery**: 240--728 kWh in increments, allowing operators to size the battery to their route rather than paying for excess capacity
- **64-tonne GCW** — the highest of any European OEM, making it the closest to Australian B-double capability (though still 4 tonnes short of the 68t limit)
- **MCS ex-works from early 2026** at up to 750 kW, alongside CCS2 at 375 kW
- In production since late 2023 for the European market

**Australian relevance:** The Scania R 450e was approved for Australian operations in May 2025, with initial deployments in South Australia using the 624 kWh configuration [@scania-australia-2025]. Scania's modularity means it can configure trucks for specific Australian corridors — lighter battery for shorter Melbourne--Geelong runs, full 728 kWh for Melbourne--Sydney.

## DAF XF/XG/XG+ Electric

DAF (PACCAR Group) is the latest European entrant:

- **210--525 kWh LFP** battery options, 500+ km range
- **50-tonne GCW** (XG+ variant)
- **CCS only at 325 kW** — DAF is the only major European OEM with no announced MCS support, a significant limitation for long-haul operations
- XD/XF production from September 2025; XG announced January 2026
- **International Truck of the Year 2026** (XG+ Electric)

**Australian relevance:** DAF displayed trial electric models at the 2025 Brisbane Truck Show, but no Australian sales or timelines have been announced [@daf-electric-2026]. The absence of MCS support is a particular concern for Australian operations, where charging stops need to be fast given the vast distances between depots.

## The B-double problem

Australia's unique regulatory environment allows heavy vehicles up to **68 tonnes GCW** in B-double configuration — far beyond the 40--50 tonne limits in Europe and the 36-tonne (80,000 lb) US Class 8 standard. Road trains in outback Australia can exceed 130 tonnes.

**No European or American electric truck is rated for 68-tonne B-double operations.** The closest is Scania at 64 tonnes. This matters because B-doubles carry the bulk of Australian interstate freight — the 4,040 ML diesel segment that dominates truck fuel consumption.

Only the **Windrose E1400** is explicitly designed for 68-tonne B-double operation, with its 1,044 kW quad-motor drivetrain and 860 kWh battery option configured for Australian GCW requirements. New Energy Transport's 480 km round trip carrying 36 tonnes (in a single-trailer configuration) demonstrates the platform works, but the full B-double payload and range combination has not yet been publicly validated.

This creates a near-term market structure where:

- **Urban rigid trucks** (3,123 ML diesel) can be electrified with existing European models (eActros, Volvo FL/FE Electric, Scania P/L series)
- **Regional articulated** operations at <50t (portion of the 4,040 ML) can use Volvo FH Electric, Scania R 450e, or eActros 600
- **Full B-double interstate** operations (the core of the 4,040 ML) currently have only one viable BEV option: Windrose, via NET

The European OEMs will likely develop higher-GCW variants for the Australian market, particularly as Volvo establishes local manufacturing. But as of March 2026, there is a genuine product gap at the top end of the Australian weight spectrum.

---

# Bus Kilometres by State and Service Type

The ABS survey also provides bus kilometres by state and service type.

: Bus Kilometres by State and Service Type, Year Ending June 2020 (millions of km) {#tbl-bus-km}

| State | Route service | School | Charter | Total |
|:------|-------------:|-------:|--------:|------:|
| NSW | 234 | 118 | 95 | 447 |
| VIC | 184 | 79 | 80 | 343 |
| QLD | 147 | 71 | 115 | 333 |
| WA | 121 | 39 | 48 | 208 |
| SA | 59 | 28 | 14 | 101 |
| TAS | 19 | 11 | 6 | 36 |
| NT | 9 | 12 | 10 | 31 |
| ACT | 19 | 9 | 9 | 37 |
| **Australia** | **790** | **367** | **376** | **1,533** |

: Source: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020], Table 31. Total km may not sum exactly due to rounding.

Route services account for 52% of bus-km, school services for 24%, and charter for 25%. NSW leads in route service km (234 million), consistent with its larger metro fleet.

---

# Light Commercial Vehicles: The Overlooked Diesel Segment

Light commercial vehicles consume 5 billion litres of diesel per year — 31% of road diesel and 17% of total national diesel. This makes them the second-largest road diesel category after trucks, yet they receive far less policy attention than either trucks or buses. The LCV fleet is also growing: utes and vans have been the fastest-growing vehicle segment in Australia for over a decade.

## What counts as an LCV

The ABS defines light commercial vehicles as goods-carrying vehicles with a Gross Vehicle Mass (GVM) under 3.5 tonnes. This encompasses three broad body types:

- **Utes** (dual-cab and single-cab pickups) — Toyota HiLux, Ford Ranger, Isuzu D-Max, Mitsubishi Triton, GWM Cannon. Utes account for roughly 60% of LCV sales and dominate the diesel share.
- **Vans** — Toyota HiAce, Ford Transit and Transit Custom, Mercedes Sprinter, Renault Master. Used by couriers, delivery fleets, tradies, and service operators.
- **Light cab-chassis** — truck-like bodies on light frames, used for tray-backs, service bodies, and specialist fit-outs.

Three-quarters of LCV fuel is diesel (5,014 ML diesel vs 1,578 ML petrol in 2020). Utes are overwhelmingly diesel; vans are more mixed.

## Who buys them

LCVs serve a wider range of buyers than any other vehicle category:

- **Tradies and small business** — electricians, plumbers, builders use utes and vans as mobile workshops. The vehicle is both transport and toolbox.
- **Fleets** — courier and delivery companies (Australia Post, Toll, StarTrack), utilities, government agencies, and rental companies.
- **Agriculture** — farm utes are the dominant light vehicle in rural Australia.
- **Mining support** — site vehicles, crew transport, light maintenance.
- **Private/recreational** — dual-cab utes have become Australia's default family vehicle in many regions, used for towing caravans, boats, and horse floats.

This diversity of use cases — from 20 km urban courier runs to 500 km rural property access — makes a single electrification solution harder than for buses, where routes are fixed and vehicles return to depot nightly.

## Electrification status

### PHEV utes: the near-term story

Plug-in hybrid utes are arriving at near-parity with diesel equivalents and are proving commercially viable:

: PHEV Utes Available in Australia, 2025 {#tbl-phev-utes}

| Model | Price (before on-roads) | EV range | Towing | Key feature |
|:------|------------------------:|:---------|-------:|:------------|
| BYD Shark 6 | $57,900 | ~80 km | 2,500 kg | Near diesel price parity |
| GWM Cannon Alpha PHEV | $61,490--$71,090 | ~85 km | 3,500 kg | DC fast charge, full 4WD |
| Ford Ranger PHEV | $71,990--$86,990 | ~48 km | 3,500 kg | 6.9 kW V2L (Pro Power Onboard) |

: Sources: BYD Australia [@byd-shark6-2025]; GWM Australia [@gwm-cannon-alpha-2025]; NRMA [@nrma-ranger-phev-2025].

The BYD Shark 6 reached 4th best-selling 4x4 ute within months of launch — a significant market signal [@carexpert-shark-not-bev-2025]. Vehicle-to-load (V2L) capability, which allows tradies to power tools directly from the vehicle battery, is a genuine differentiator over diesel.

### BEV utes: coming but compromised

Full battery-electric utes are arriving in 2025--2026 but remain expensive and limited:

: BEV Utes Available or Announced for Australia {#tbl-bev-utes}

| Model | Status | Price estimate | Range (WLTP) | Towing | Limitation |
|:------|:-------|---------------:|:-------------|-------:|:-----------|
| LDV eT60 | On sale | $92,990 | 330 km | 1,000 kg | 2WD only, low towing |
| Toyota HiLux BEV | H1 2026 | ~$70,000+ | 300+ km | 2,000 kg | Urban fleet focus |
| LDV eTerron 9 | 2025--26 | TBA | 430 km | 3,500 kg | First 4WD BEV ute |
| Isuzu D-Max BEV | TBA | ~$100,000+ | 263 km | 3,500 kg | 50 kW DC charge only |

: Sources: CarExpert [@carexpert-hilux-bev-2026]; RAC [@rac-electric-utes-2026]; CarExpert [@carexpert-dmax-bev-2026].

The LDV eT60 (\$93k, 2WD only, 1 tonne towing) has been a difficult sell at more than double the price of a diesel equivalent. Toyota is positioning its HiLux BEV explicitly for "back-to-base" urban fleet operations — not for touring or heavy towing [@fleetev-hilux-2026]. The LDV eTerron 9 and Isuzu D-Max BEV are the first to match the 3,500 kg diesel towing benchmark, but at high prices.

### Electric vans: more viable than utes

Electric vans suit electrification better than utes: they operate on predictable urban routes, return to depot for overnight charging, and carry loads rather than tow them.

: Electric Vans Available in Australia, 2025 {#tbl-electric-vans}

| Model | Price | Range (WLTP) | Payload | Diesel equivalent price | Premium |
|:------|------:|:-------------|--------:|------------------------:|--------:|
| LDV eDeliver 7 | $69,463 | 318--362 km | ~1,350 kg | ~$48,000 | ~$21,000 |
| Ford E-Transit Custom | $77,590 | 301--307 km | ~1,100 kg | ~$56,000 | ~$22,000 |
| Ford E-Transit | $89,990 | 317 km | ~1,500 kg | ~$65,000 | ~$25,000 |
| Mercedes eSprinter | $104,313 | 264 km | 1,523 kg | ~$72,000 | ~$32,000 |

: Sources: CarExpert [@carexpert-etransit-custom-2025]; CarsGuide [@carsguide-ev-vans-2026].

Australia Post claims over 5,600 electric delivery vehicles, but the vast majority are electric motorcycles and three-wheelers (such as the Rapide 3) that replaced petrol postie bikes — the fleet includes only ~36 eVito vans and ~20 Fuso eCanter trucks [@auspost-ev-fleet-2026]. The more significant fleet signal is Woolworths' commitment to all-electric last-mile delivery by 2030, with CEFC investing \$6 million in 60 battery-electric trucks through Zenobe [@cefc-zenobe-2025].

### Real-world electric van performance

Reviews from the UK and US — markets where electric vans have been in fleet service for longer — provide a reality check on the gap between manufacturer claims and daily use.

**Mercedes eSprinter** (113 kWh battery): real-world range of 220--320 km loaded, with DC fast charging (115 kW) from 10--80% in 42 minutes. The critical weakness is payload: at 3.5t GVW the eSprinter carries only ~650 kg — less than half the diesel Sprinter's ~1,700 kg. Moving to the 4.25t rating recovers payload to ~1,000 kg but triggers tachograph and driver-hours regulations in some jurisdictions. Running costs are roughly 60--65% lower than diesel per km. Reviewers praise the driving experience but note the payload penalty makes it a parcel van, not a trades van [@insideevs-esprinter-2024; @electrifying-esprinter-2025].

**Ford E-Transit** (68 kWh battery): the weakest range of the three — independent testing at maximum payload (1,340 kg) in cold weather yielded just 153 km at highway speed. Ford notes the average US commercial van covers 119 km per day, positioning the E-Transit as adequate for most urban delivery work. The payload penalty vs diesel is much less severe than the eSprinter's (~300--500 kg less rather than 1,000+ kg). No heat pump means winter range drops sharply [@evpulse-etransit-2024].

**Ford E-Transit Custom** (71 kWh battery): hits the best overall balance for a medium van — official 370 km range, real-world ~270--300 km, payload penalty of only ~240 kg vs diesel, and the load bay dimensions match the diesel Transit Custom exactly. Widely rated as the best-driving van in its class, electric or diesel [@parkers-etransit-custom-2024].

All three save roughly 55--65% on fuel costs per km compared to diesel, but purchase premiums of \$20,000--35,000 mean payback periods of 3--6 years depending on daily kilometres and local electricity prices.

### Barriers to LCV electrification

The key barriers differ from buses and are more varied:

- **Towing under load** — BEV range drops 30--50% when towing. A 400 km rated vehicle may achieve only 200--250 km with a loaded trailer. Most diesel utes tow 3,500 kg; early BEV utes were limited to 1,000--2,500 kg (now improving).
- **Worksite charging** — construction sites, rural properties, and remote locations often lack the electrical infrastructure for EV charging. Depot-based fleets with overnight AC charging are the natural first adopters.
- **Payload penalty** — battery weight reduces available payload by 200--400 kg in vans and 100--300 kg in utes. Critical for trades carrying heavy tools and materials.
- **Price premium** — BEV utes carry a \$45,000--\$51,000 premium over diesel. Electric vans are \$20,000--\$35,000 more. Whole-of-life cost calculations narrow the gap but depend heavily on kilometres driven.
- **Rural range** — many agricultural and mining-support applications require multi-day autonomy without returning to a depot. Diesel utes offer 800+ km from a single tank.

### UK and EU as leading indicators

The UK and EU are 3--5 years ahead of Australia on electric LCV adoption:

: Electric Van Market Share, UK and EU {#tbl-uk-eu-ev-vans}

| Market | 2023 | 2024 | 2025 |
|:-------|-----:|-----:|-----:|
| UK | ~6% | 6.3% | 9.5% |
| EU | 7.2% | 6.1% | ~10% |

: Sources: SMMT [@smmt-ev-vans-2025]; ACEA [@acea-cv-registrations-2025].

Even with strong mandates (the UK's ZEV mandate requires 24% of new van sales to be zero-emission by 2026), LCV electrification lags passenger car electrification by 5--10 percentage points. The EU saw a temporary dip in 2024 before recovering in 2025. This pattern — slower than cars, mandate-driven, concentrated in urban depot-based fleets first — is likely to repeat in Australia.

### Policy levers

The main policy mechanisms affecting LCV electrification in Australia are:

- **New Vehicle Efficiency Standard (NVES)** — in effect from January 2025 with separate (less stringent) targets for LCVs. The LCV target starts at 210 g/km CO2 in 2025, dropping ~50% by 2029. Penalties of \$100 per g/km per vehicle for non-compliance force manufacturers to supply low-emission utes and vans or pay penalties [@nves-regulator-2025].
- **FBT exemption** — zero fringe benefits tax on eligible BEVs below the luxury car tax threshold (\$91,387). PHEVs excluded from 1 April 2025. The exemption must carry under 1 tonne payload and under 9 passengers, which excludes some larger LCVs [@ato-fbt-ev-2025].
- **NSW EV Fleet Incentive** — up to \$50,000 per heavy commercial vehicle for fleet electrification [@nsw-ev-fleet-2025].
- **Fuel Tax Credits Scheme** — the existing \$0.48/litre rebate on off-road diesel (claimed heavily by mining and agriculture) acts as a countervailing subsidy that reduces the relative cost advantage of electrification for off-road LCV use.

---

# Data Gaps

1. **Off-road diesel by sector** — the 60/40 road/off-road split is from ACAPMA; precise sector-by-sector volumes (mining, agriculture, construction) are not published in an accessible form. The fuel tax credit data provides a proxy but mixes diesel with other fuels.
2. **State-level off-road diesel** — no published breakdown of mining or agricultural diesel by state, though WA and QLD likely dominate mining diesel.
3. **Updated road transport data** — the ABS Survey of Motor Vehicle Use was discontinued after 2020. No equivalent dataset exists for more recent years.
4. **LCV electrification rates** — no published data on electric ute/van uptake as a share of the LCV fleet. FCAI VFACTS reports total EV sales but does not break out LCVs separately.
5. **LCV sub-segmentation** — the ABS groups all vehicles under 3.5t GVM as "light commercial" without distinguishing utes from vans from cab-chassis. FCAI sales data provides model-level detail but not fuel consumption.
6. **Fleet vs private LCV split** — no published breakdown of LCV diesel consumption by fleet versus private ownership, though fleet vehicles likely drive more kilometres and consume disproportionately more fuel.
7. **Australian electric truck registrations** — no published data on the number of electric trucks registered or sold in Australia. FCAI does not break out electric heavy vehicles separately.
8. **Heavy vehicle charging infrastructure** — no public megawatt-class charging stations exist in Australia as of March 2026. The timeline for MCS deployment on key freight corridors (Hume, Pacific, Newell) is unknown.

---

# References
