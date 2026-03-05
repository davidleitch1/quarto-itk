---
title: "Heavy Truck Charging Stations: Costs, Charge Rates and Global Deployment"
author: "David Leitch"
date: 2026-03-05
categories: ["EVs", "Investment"]
bibliography: truck_charging_references.bib
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Summary

Electrifying heavy-duty trucking requires purpose-built charging infrastructure far beyond anything needed for passenger vehicles. A single Class 8 semi-truck draws as much power as a big-box retail store, and a depot serving 50--100 trucks simultaneously needs 20 MW or more of grid connection --- equivalent to a small industrial substation [@nrel-hpc-trucking-2025].

This note surveys the current state of heavy truck charging across the USA, Europe/UK, and China, focusing on two questions:

1. **What does it cost to build a purpose-designed facility?**
2. **What maximum charge rates are available or imminent?**

The short answers: a large public truck charging station costs US\$20--60 million depending on scale and grid works; and the Megawatt Charging System (MCS) standard supports up to 3.75 MW per connector, with 1.0--1.44 MW chargers now deployed commercially.

---

# The Megawatt Charging System (MCS) Standard

The MCS connector, developed by the CharIN industry consortium, defines the global standard for high-power truck charging [@charin-mcs-2025]. Its headline specifications are:

**MCS Connector Ratings**

| Parameter | Specification |
|:----------|:--------------|
| Maximum voltage | 1,250 V DC |
| Maximum current | 3,000 A |
| Maximum power | 3.75 MW |
| Cooling | Liquid-cooled cable and connector |
| Charge time (20--80%) | <30 minutes at full rate |

*Source: CharIN MCS specification [@charin-mcs-2025]*

The 3.75 MW ceiling is a theoretical maximum. Commercial deployments in 2025--26 operate at lower power levels, reflecting both charger supply and truck battery acceptance rates.

**Current Commercial Charge Rates (2025--2026)**

| OEM / Operator | Power (kW) | Status |
|:---------------|:-----------|:-------|
| ABB (MCS charger) | 1,200 | Shipping 2025 [@wikipedia-mcs-2025] |
| Huawei (truck supercharger) | 1,440 | Deployed Aug 2025 [@huawei-100mw-2025] |
| Tesla Megacharger (Semi) | 1,200 | Operational at 2 sites [@tesla-semi-1200kw-2025] |
| Mercedes eActros 600 + ABB | 1,000 | Demonstrated [@wikipedia-mcs-2025] |
| Scania MCS (first generation) | 750 | Trucks from mid-2026 [@scania-mcs-2025] |
| BYD Flash Charging | 1,000--1,500 | Rolling out Apr 2025 [@byd-megawatt-2025] |
| Kempower MCS | 1,000+ | Available 2025 [@kempower-mcs-2025] |

*Sources: as cited per row*

At 1 MW, a truck can charge from 20% to 80% state of charge in under 30 minutes, which aligns with mandatory driver rest periods under EU and US hours-of-service regulations [@volvo-mcs-2025]. This is the critical design constraint: the charge rate must fit within a 30--45 minute driver break.

---

# United States

## Facility Costs

US projects provide the clearest cost data because federal grant applications are public.

**Kettleman City, California.** A 56-charger heavy truck station on Interstate 5, budgeted at US\$58.2 million. The site includes a 1 MW / 4 MWh battery storage system and a 3.86 MW solar canopy. Federal funding covers \$35.6 million; the balance comes from tax credits, PG&E rebates, and sponsor equity. Construction expected to complete in 2026 [@kettleman-city-2024].

**DOE SuperTruck Charge programme.** The Department of Energy allocated US\$68 million across multiple sites near ports, distribution hubs, and major freight corridors [@doe-supertruck-2025].

**University of Chicago estimate.** An academic analysis found that installing a 100-truck charging site costs approximately US\$21.2 million for charger hardware and electrical infrastructure alone. The 20-year total cost of ownership (including electricity, maintenance, and grid demand charges) exceeds US\$100 million [@uchicago-etrucking-2022].

**McKinsey US-wide estimate.** Total public charging infrastructure for commercial vehicles to 2030 is estimated at US\$12 billion, within a broader US\$97 billion national charging buildout [@mckinsey-us-charging-2023].

**Estimated Per-Site Cost Summary (USA)**

| Site Scale | Chargers | Estimated Cost (US\$M) | Source |
|:-----------|:---------|:----------------------|:-------|
| Large public hub (I-5 corridor) | 56 dual-port | 58 | Kettleman City [@kettleman-city-2024] |
| Large depot (100 trucks) | 100 | 21 (hardware only) | U of Chicago [@uchicago-etrucking-2022] |
| Tesla Megacharger hub (Pilot) | 4--8 stalls | Not disclosed | Tesla/Pilot [@tesla-pilot-2026] |

*Sources: as cited per row*

## Tesla Megacharger Network

Tesla has identified 66 Megacharger sites across 15 US states, concentrated along major freight corridors from coast to coast. Texas leads with 19 planned sites and California with 17 [@tesla-megacharger-2026; @electrive-tesla-66-2026]. A partnership with Pilot Travel Centers (the largest US truck stop operator) will see construction begin in H1 2026, with the first sites opening by summer 2026. Each Pilot hub features 4--8 charging stalls delivering up to 1.2 MW per dispenser [@tesla-pilot-2026].

Tesla's Q4 2025 shareholder report targeted 37 locations entering service during 2026 and 46 Megacharger stations operational by early 2027.

---

# Europe and United Kingdom

## Investment Scale

McKinsey estimates that Europe's electric truck charging infrastructure requires approximately EUR 40 billion of capital investment to 2040, with EUR 7 billion needed by 2030 for direct-charging hardware, planning, engineering, and installation [@mckinsey-europe-trucks-2024]. The ICCT projects that the EU will need 150,000--175,000 private depot chargers and 60,000--80,000 public chargers by 2030 [@icct-eu-trucks-2025].

The first phase of deployment (to 2030) is concentrated in private fleet depots and semi-public hubs close to logistics centres. Public corridor charging scales in a second phase after 2030 [@mckinsey-europe-trucks-2024].

## Milence: The OEM Joint Venture

Milence, a joint venture of Daimler Truck, Traton Group (MAN/Scania), and Volvo Group, received EUR 500 million in initial funding and targets 1,700 high-performance public charging points across Europe by 2027 [@milence-network-2025]. As of early 2026, Milence operates 30 hubs in eight countries.

The implied capital cost is approximately EUR 294,000 per charging point (EUR 500M / 1,700 points), which covers charger hardware, grid connection, civil works, and site development. Milence's initial pan-European tariff was EUR 0.399/kWh (excl. VAT), shifting to market-based pricing from January 2026 [@milence-network-2025].

Milence opened its first UK hub in March 2025 at 39p/kWh, with BP Pulse planning MCS-capable chargers at Ashford International Truckstop by 2026 [@milence-uk-2025; @bp-pulse-mcs-2025].

## Daimler Truck's Own Network

Separately from Milence, Daimler Truck announced plans to build Europe's largest semi-public charging network, leveraging its dealer locations. This network targets existing depot sites where grid connection and land are already available, reducing per-site costs significantly compared to greenfield corridor stations [@daimler-charging-2025].

---

# China

China is the clear global leader in deployed heavy truck charging infrastructure and is moving fastest on megawatt-scale systems.

## Scale of Deployment

China now has more than 9,000 public charging stations dedicated to heavy-duty electric trucks, covering major logistics corridors, industrial clusters, ports, and mining zones [@china-9000-stations-2025]. This is an order of magnitude ahead of either the US or Europe.

## The Huawei 100 MW Hub

The most impressive single facility is the "Sichuan Yuanqi Xingguang Heavy-Duty Truck Megawatt Supercharging Station" in Beichuan, Sichuan Province, which commenced operations in August 2025 [@huawei-100mw-2025; @huawei-electrive-2025].

**Huawei 100 MW Facility Specifications**

| Parameter | Value |
|:----------|:------|
| Total designed capacity | 100 MW |
| Supercharging bays | 18 at 1.44 MW each |
| Fast charging bays | 108 at 600 kW each |
| Site area | 11.5 acres (4.7 hectares) |
| Construction cost | US\$20.9 million |
| Daily throughput | 700 trucks / 300,000+ kWh |
| On-site solar | ~1 MW photovoltaic canopy |
| Charge speed (3.5C trucks) | ~100 km range in 5 minutes |

*Source: Huawei / Interesting Engineering [@huawei-100mw-2025]*

At US\$20.9 million for a 126-bay, 100 MW facility, the cost per charging point is approximately US\$166,000 --- substantially below Western equivalents. This reflects China's lower construction costs, vertically integrated supply chains (Huawei manufactures the power electronics), and likely state subsidy for the grid connection.

## BYD Megawatt Network

BYD is rolling out 1,000 kW "Flash Charging" stations across China, with the first 500 units deployed from April 2025 and a target of 4,000 stations. BYD has partnered with Xiaoju Charging (10,000 stations) and LongShine (5,000 stations) for further expansion [@byd-megawatt-2025].

Liquid-cooled charging units cost 80,000--120,000 yuan (US\$11,200--16,800) per unit, which is 3--5 times the cost of traditional air-cooled chargers [@byd-flash-pricing-2025]. BYD's charging tariff is 1.3 yuan/kWh (US\$0.18/kWh), split between 1.0 yuan for electricity and 0.3 yuan for a service fee.

Note that BYD's megawatt network primarily targets passenger vehicles and light commercial vehicles (using the Flash Charging platform), while Huawei and State Grid focus on heavy-duty truck applications.

---

# Cost Comparison Across Regions

**Estimated Purpose-Built Truck Charging Facility Costs**

| Region | Facility | Scale | Cost (US\$M) | Cost per Bay (US\$k) |
|:-------|:---------|:------|:------------|:-------------------|
| USA | Kettleman City (CA) | 56 chargers, 1 MW BESS, 3.9 MW solar | 58 | ~1,040 |
| USA | Generic 100-truck depot | 100 chargers (hardware only) | 21 | ~210 |
| Europe | Milence network (implied) | 1,700 points across 30+ hubs | 500 (EUR) | ~294 (EUR) |
| China | Huawei 100 MW hub | 126 bays (18x1.44MW + 108x600kW) | 21 | ~166 |
| China | BYD charger unit only | Per liquid-cooled unit | --- | 11--17 |

*Sources: as cited in body text. Milence figure is total JV funding divided by target charge points.*

The range is wide. The Kettleman City project at US\$58 million includes substantial on-site generation and storage, land acquisition on an interstate corridor, and California construction costs. The Huawei facility at US\$21 million is a much larger installation by bay count but benefits from Chinese cost structures and an existing industrial site. The University of Chicago's US\$21 million estimate for a 100-truck depot covers hardware and electrical infrastructure only, excluding land, buildings, and on-site generation.

A reasonable estimate for a **purpose-built, grid-connected truck charging hub** with 20--50 high-power (1+ MW) charging bays is:

- **USA:** US\$25--60 million (depending on grid works, on-site generation, and state)
- **Europe:** EUR 15--40 million (similar drivers, plus higher labour costs in some markets)
- **China:** US\$10--25 million (lower construction and equipment costs, state grid support)

The single largest variable is **grid connection cost**. A 20 MW grid connection can require transformer and switchgear upgrades costing US\$3--8 million, with lead times of 12--24 months for electrical equipment [@nrel-hpc-trucking-2025; @terawatt-buy-build-2025]. Sites with existing heavy industrial grid connections (ports, mining sites, former factories) have a major cost advantage.

---

# Maximum Charge Rates: Summary

**Peak Charge Rates by System (2025--2026)**

| System | Max Power (MW) | Status | Region |
|:-------|:--------------|:-------|:-------|
| MCS standard (theoretical max) | 3.75 | Standard published | Global |
| Huawei supercharger | 1.44 | Deployed | China |
| Tesla Megacharger | 1.20 | Operational (2 sites) | USA |
| ABB MCS charger | 1.20 | Shipping | Global |
| BYD Flash Charging | 1.00--1.50 | Deploying | China |
| Kempower MCS | 1.00+ | Available | Europe |
| Scania MCS (Gen 1) | 0.75 | Trucks from mid-2026 | Europe |

*Sources: as cited in body text*

The practical ceiling for deployed truck chargers in early 2026 is **1.44 MW** (Huawei), with the MCS standard allowing headroom to 3.75 MW as battery technology and grid infrastructure mature. Most OEMs are targeting 1.0--1.2 MW as the initial commercial sweet spot, which delivers a 20--80% charge in under 30 minutes for current battery capacities (typically 600--900 kWh for a Class 8 truck).

---

# Implications

1. **Grid is the binding constraint, not charger technology.** Chargers capable of 1+ MW are commercially available. The bottleneck is getting 10--100 MW of grid capacity to the right locations, which involves transformers, switchgear, and utility coordination with lead times measured in years.

2. **China is 5+ years ahead on deployment.** With 9,000+ truck charging stations already built and megawatt-scale hubs operational, China has moved from pilot to industrial scale. The US and Europe remain in the early buildout phase.

3. **Depot charging will dominate initially.** Both McKinsey and the ICCT project that 70--80% of truck charging electricity will be delivered at private fleet depots or semi-public hubs through 2030, with public corridor charging scaling later.

4. **Costs will fall but remain substantial.** Chinese cost structures (US\$166k per bay) suggest where Western costs may trend as supply chains mature, but grid connection costs are largely site-specific and less amenable to industrialisation.

5. **The 30-minute break constraint shapes everything.** Charging must fit within mandatory driver rest periods, which sets a floor on required charge rates (~750 kW to 1 MW depending on battery size) and drives the entire MCS standard.
