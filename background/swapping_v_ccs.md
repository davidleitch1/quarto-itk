---
title: "Battery Swapping vs Conductive Fast Charging for Heavy Trucks"
author: "David Leitch"
date: 2026-03-21
draft: true
bibliography: swapping_v_ccs_references.bib
---

# Summary

Two competing models have emerged for refuelling electric heavy trucks: **battery swapping** (dominant in China) and **megawatt conductive charging** (the emerging global standard). Both solve the same problem --- getting enough energy into a 40+ tonne truck within a 30-minute driver break --- but they differ fundamentally in cost structure, infrastructure requirements, and OEM alignment.

The most likely long-term outcome is **regional bifurcation**: battery swap in China (where it has critical mass and government support), and MCS conductive charging everywhere else. For Australia, this means the relevant technology pathway is MCS --- and the critical gap is not vehicle availability but charging infrastructure on key freight corridors.

# Battery Swap: China's Approach

CATL, the world's largest battery manufacturer, operates a heavy-truck battery-swap network through its subsidiary Qiji Energy. The system uses a standardised "75#" swap block with a capacity of **171 kWh per module** --- trucks carry one to three modules depending on range requirements. Each swap station holds 24 battery packs and is compatible with over 95% of mainstream Chinese heavy-truck models [@catl-swap-standard-2025].

**Key metrics:**

- **Swap time:** approximately 5 minutes
- **Stations operational:** ~305 heavy-truck stations at end 2025, targeting 900 by end 2026
- **OEM partners:** 30+ truck models from Sinotruk, FAW Jiefang, Foton, DeepWay, and SAIC
- **Longest route:** 1,250 km Shanghai--Chengdu Expressway corridor with 12 stations [@catl-swap-route-2025]
- **2030 target:** coverage of ~180,000 km of routes and 80% of China's truck transport corridors

## The Vehicle-Battery Separation Model

Under the "separation of vehicle and battery" model, truck buyers pay only for the glider (cab and chassis), reducing upfront capital by 30--40%. CATL retains ownership of the batteries and charges a per-swap or per-kWh service fee. This is the critical economic innovation: it transforms the battery from a capital cost into an operating cost, making electric trucks cost-competitive with diesel on day one for fixed urban and regional routes. CATL claims each truck saves 30,000--60,000 yuan (A\$6,500--13,000) per year in operating costs.

The model also enables battery lifecycle management --- CATL can rotate packs across the fleet, replacing degraded cells before they affect truck range, and repurpose retired packs for stationary storage. This addresses the fleet operator's largest anxiety: battery degradation risk over a 10--15 year vehicle life.

## Outside China

**Battery swap for heavy trucks barely exists outside China.** The only significant initiative is Germany's eHaul research project, which built Europe's first automated truck battery-swap station at Lubbenau --- swapping 440 kWh batteries in approximately 10 minutes for trucks up to 40 tonnes [@ehaul-2026]. A DIN standard (DIN SPEC 91533) for truck battery swapping is expected in Q1 2026, with NIO contributing. But this remains at research stage, not commercial deployment.

The fundamental barrier is **standardisation**. Within China, CATL can enforce a single swap-block standard across domestic OEMs, backed by government policy. Globally, no equivalent coordination exists. Daimler, Volvo, and Scania each have different battery architectures; standardising a physical swap interface across competing OEMs would require the kind of industry alignment that took a decade for CCS passenger vehicle charging.

# Megawatt Charging System (MCS): The Global Standard

The MCS connector, developed by CharIN e.V. (the same industry body behind the CCS charging standard), defines the emerging global standard for heavy-duty vehicle charging [@charin-mcs-2025].

**MCS Specifications:**

| Parameter | Specification |
|:----------|:--------------|
| Maximum voltage | 1,250 V DC |
| Maximum current | 3,000 A |
| Maximum power | 3.75 MW |
| Cooling | Liquid-cooled cable and connector |
| Charge time (20--80%) | <30 minutes at full rate |

The 3.75 MW ceiling is a theoretical maximum. Commercial deployments in 2025--26 operate at lower power levels, reflecting both charger supply and truck battery acceptance rates.

## Current Commercial Charge Rates

| OEM / Operator | Power (kW) | Status | Region |
|:---------------|:-----------|:-------|:-------|
| Huawei (truck supercharger) | 1,440 | Deployed Aug 2025 | China |
| Tesla Megacharger (Semi) | 1,200 | Operational at 2 sites | USA |
| ABB (MCS charger) | 1,200 | Shipping 2025 | Global |
| BYD Flash Charging | 1,000--1,500 | Rolling out Apr 2025 | China |
| Kempower MCS | 1,000+ | Available 2025 | Europe |
| Mercedes eActros 600 + ABB | 1,000 | Demonstrated | Europe |
| Scania MCS (first generation) | 750 | Trucks from mid-2026 | Europe |

At 1 MW, a truck can charge from 20% to 80% state of charge in under 30 minutes, which aligns with mandatory driver rest periods under EU and US hours-of-service regulations [@volvo-mcs-2025]. This is the critical design constraint: **the charge rate must fit within a 30--45 minute driver break.**

## OEM Alignment

Every major Western truck OEM has committed to MCS:

- **Scania** (Traton): MCS commercially available from early 2026 [@scania-mcs-2026]
- **Volvo Trucks:** FH Aero Electric with 780 kWh battery, 600 km range, orders open Q2 2026 [@volvo-electric-longhaul-2025]
- **Mercedes-Benz:** eActros 600 in production since November 2024, MCS customer trials in H2 2026 [@daimler-eactros-mcs-2026]
- **MAN** (Traton): successful MCS interoperability tests with Kempower chargers

## Charging Network Deployments

| Operator | Geography | MCS hubs operational | MCS points planned | Target date |
|:---------|:----------|---------------------:|--------------------:|:------------|
| Milence (Daimler/Traton/Volvo JV) | 8 EU countries | 3 | 284 across 71 locations | 2027 |
| E.ON / Voltix / GreenWay (HDV-E) | 9 EU countries | 0 | 330 across 55 locations | 2028 |
| Tesla (Megacharger) | US | 0 | 66 sites identified | 2026--27 |

: Sources: Milence [@milence-solutrans-2025]; E.ON [@eon-mcs-2025]; Tesla [@tesla-megacharger-2026].

Milence's three operational MCS hubs --- at Zwolle (Netherlands), Port of Antwerp-Bruges (Belgium), and Landvetter (Sweden) --- are building towards Europe's first MCS corridor from Antwerp to Stockholm, over 1,500 km along TEN-T freight routes.

# Tesla Semi and Megacharger

Tesla has chosen a **proprietary Megacharger** system rather than the CharIN MCS standard, though power levels are comparable. In December 2025, Tesla released footage showing a Semi drawing **1,206 kW (1.2 MW)** during a live charging session --- sufficient to replenish approximately 640 km of range in 30 minutes [@tesla-semi-charging-2025].

Tesla has identified 66 Megacharger sites across the US, with 37 expected to open in 2026 and a target of 46 operational by early 2027. Sites are planned at Pilot Travel Centers along major freight corridors in California, Georgia, Nevada, New Mexico, and Texas [@tesla-megacharger-2026; @tesla-pilot-2026].

Tesla's proprietary connector --- separate from both CCS and MCS --- raises interoperability questions. Tesla has historically opened its passenger vehicle Supercharger network to non-Tesla vehicles, but whether this extends to the Megacharger remains to be seen.

# Windrose: Fast Charging Comes to Australia

Windrose Technology (founded in Hefei, headquartered in Antwerp) is the electric truck manufacturer most relevant to Australia through its partnership with New Energy Transport (NET). Windrose has firmly chosen conductive fast charging over battery swap.

**The Windrose E1400:**

| Parameter | Value |
|:----------|:------|
| Peak power | 1,400 hp (1,044 kW), four motors |
| Battery | 729 kWh LFP (860 kWh option for B-double) |
| Range | 670 km at 49t GCW |
| B-double capability | 68 tonnes |
| Platform voltage | 800V |

**Charging demonstrations:**

- **Dual CCS2:** two 350 kW chargers delivering >650 kW simultaneously (demonstrated with Terawatt Infrastructure, June 2025) [@windrose-terawatt-2025]
- **MCS standard:** demo with Autel MaxiCharger in Roosendaal, Netherlands (March 2026) delivering 1.2 MW via MCS connector [@windrose-autel-mcs-2026]

**Australian deployments:** NET completed Australia's longest single-charge electric truck delivery --- a 480 km round trip from Picton (south of Sydney) to Beresfield (Hunter region) carrying 36 tonnes, arriving 40 minutes faster than diesel due to superior uphill performance [@net-windrose-480km-2025]. NET has secured a site at Wilton (80 km southwest of Sydney) for Australia's largest heavy electric trucking depot, supporting up to 50 trucks, with plans to expand to Adelaide--Melbourne--Sydney--Canberra--Brisbane routes and a fleet of 200+ trucks by 2031.

# Janus Electric: Battery Swap for Australian Retrofits

Janus Electric (ASX: JNS) is Australia's only company pursuing battery swap for heavy trucks. Unlike CATL's purpose-built Chinese trucks or Windrose/Volvo's new-build approach, Janus converts **existing diesel prime movers** to electric drivetrains with swappable battery packs. The company listed on the ASX in May 2025 via a reverse takeover of ReNu Energy, raising A\$8.8 million [@janus-asx-2025].

## The Retrofit Model

Janus removes the diesel engine, fuel tanks, and exhaust system from an existing prime mover and replaces them with an electric motor (540 kW in the latest version) and two swappable battery packs totalling 620 kWh. The packs (2 m x 1.2 m each) mount where the fuel tanks sat. Converted trucks retain their original gearbox (typically Volvo or Eaton 12-speed) and chassis. Models converted include the Kenworth T410, Kenworth T610, Volvo FH16, and Freightliner Coronado [@janus-fleet-hv-2025; @janus-driven-2022].

**Conversion cost:** \$150,000--200,000 depending on vehicle specification --- compared with ~\$750,000 for a new-build electric prime mover [@janus-fleet-hv-2025]. This is the core value proposition: a 70--75% capital saving over a new electric truck, applied to a vehicle that already exists in the fleet.

**Specifications:**

| Parameter | Value |
|:----------|:------|
| Motor | 540 kW (latest); 350 kW (earlier versions) |
| Battery | 2 x 310 kWh swappable packs (620 kWh total) |
| Range (single trailer) | 400--600 km |
| Range (B-double) | 300--500 km |
| Swap time | ~4 minutes (forklift-based) |
| Weight penalty | ~1 tonne heavier than diesel equivalent |

The weight penalty created a regulatory barrier: Australian Design Rules (ADR 80/03) set a 6.0-tonne steer axle limit that was written for diesel trucks and did not contemplate the extra mass of batteries. After months of negotiation with the NHVR, Janus obtained registration approval in September 2022, and NSW has since granted extra-mass provisions for electric trucks on state roads [@janus-bigrigs-2022; @nsw-moorebank-2024].

## Operating Economics

Janus claims operating costs of approximately \$0.33/km versus \$0.96/km for diesel --- a 66% saving [@janus-apac-outlook-2025]. This figure appears to reflect electricity-only costs versus diesel fuel costs, and likely excludes the battery lease/swap service fee and conversion amortisation. No independent TCO analysis has been published.

For a truck doing 95,000 km/yr, the claimed fuel saving alone is ~\$60,000/yr. At a conversion cost of \$175,000, simple payback on the conversion is ~3 years if the fuel saving figure is accurate. However, this must be weighed against:

- The **battery lease cost** (Janus retains battery ownership under their swap model, but per-swap or per-kWh pricing has not been publicly disclosed)
- The **residual life** of the donor vehicle (a 5--10 year old prime mover has limited remaining chassis life)
- **Maintenance costs** for the electric drivetrain on an adapted chassis designed for diesel

## Deployment Status (March 2026)

| Metric | Value |
|:-------|:------|
| Trucks converted | 23 |
| Contracted orders | 142 |
| Charge & Change Stations | 9 |
| Total battery swaps | 3,500+ |
| Total km driven | 600,000+ |

: Source: Janus Electric company reports and ASX announcements [@janus-asx-2025; @janus-fleet-hv-2025].

Fleet customers include Qube, Cement Australia, Symons Clark Logistics, and Fennell Forestry (Mount Gambier). The flagship installation is a solar-powered Charge & Change Station at the Moorebank Intermodal Precinct in western Sydney, opened December 2024 [@nsw-moorebank-2024].

The 170-tonne triple road train conversion --- a Volvo FH16 8x6 hauling three trailers of copper concentrate from BHP's Carrapateena mine to Whyalla port (165 km) --- is the heaviest battery-electric truck operating in Australia [@janus-chargedevs-2023].

## Financial Position

Janus is pre-revenue in any meaningful sense. The May 2025 capital raise of A\$8.8 million was largely consumed by H1 2025 (~\$4.8 million spent on inventory, battery packs, station builds, R&D, and working capital). Operating cash flow was negative \$3.3 million in FY2024. Market capitalisation is approximately A\$20 million [@janus-asx-2025]. The company lost its CEO (Ian Campbell) and CFO (Greg Watson) within four months of listing [@janus-bna-2025].

A partnership with Canadian battery manufacturer Electrovaya will supply next-generation "JB650" lithium-ion packs with up to 14,000 cycle life (versus ~5,000 currently), potentially extending pack life from ~8 years to ~20 years [@janus-electrovaya-2025].

## Retrofit vs New-Build: Assessment

The Janus model addresses a real gap. Australia has ~80,000 articulated trucks, with an average age of ~11 years. Even if new-build electric trucks (Windrose, Volvo FH Electric) scale rapidly, they can only replace trucks at the rate of new purchases (~4,000--5,000 per year). Converting the existing fleet is the only way to accelerate the transition beyond the natural replacement cycle.

However, several factors limit the retrofit model's scalability:

1. **Donor vehicle quality.** A conversion makes economic sense on a 3--8 year old prime mover with significant remaining chassis life. Older vehicles have higher maintenance costs and shorter payback windows. The pool of suitable donors shrinks as the fleet ages.

2. **Performance gap.** The Windrose E1400 delivers 1,044 kW from four motors on an 800V platform purpose-designed for electric operation. A Janus conversion delivers 540 kW through an adapted diesel gearbox. The performance difference matters for loaded hill climbs and B-double operations.

3. **Charging infrastructure.** Janus's forklift-based swap is simple but labour-intensive and site-specific. It cannot use the MCS charging network that Windrose, Volvo, and Scania are building towards. This creates a parallel, proprietary infrastructure that must be funded from Janus's small balance sheet.

4. **Scale economics.** CATL's swap model works in China because CATL can spread station costs across hundreds of thousands of trucks using a single battery standard. Janus has 23 trucks and 9 stations. The station utilisation rate is very low --- 3,500 swaps across 9 stations over the company's lifetime is ~390 swaps per station, or roughly one per day.

5. **Financial viability.** A \$20 million market cap company with negative cash flow and executive turnover faces significant execution risk. The 142 contracted orders represent future revenue, but converting them requires capital that the company may struggle to raise.

**The retrofit model is most compelling as a transitional solution** --- electrifying trucks that would otherwise run on diesel for another 5--10 years while new-build electric trucks scale up. It is unlikely to compete with purpose-built electric trucks in the long run, because the performance, efficiency, and total cost of ownership advantages of a ground-up electric design (integrated battery thermal management, optimised weight distribution, 800V architecture, MCS compatibility) will widen as the technology matures. But for the next 5--7 years, while the new-build pipeline is thin and charging infrastructure is absent, Janus-style conversions could displace meaningful diesel volumes if the company can survive financially and scale its station network.

# China's Charging Infrastructure Scale

China is the clear global leader in deployed heavy truck charging infrastructure. As of late 2025, China has more than **9,000 public charging stations** dedicated to heavy-duty electric trucks, covering major logistics corridors, industrial clusters, ports, and mining zones [@china-9000-stations-2025]. This is an order of magnitude ahead of either the US or Europe.

The most impressive single facility is the Huawei "Sichuan Yuanqi Xingguang" megawatt supercharging station in Beichuan, Sichuan Province, which commenced operations in August 2025 [@huawei-100mw-2025].

| Parameter | Value |
|:----------|:------|
| Total designed capacity | 100 MW |
| Supercharging bays | 18 at 1.44 MW each |
| Fast charging bays | 108 at 600 kW each |
| Site area | 11.5 acres (4.7 hectares) |
| Construction cost | US\$20.9 million |
| Daily throughput | 700 trucks / 300,000+ kWh |
| Charge speed (3.5C trucks) | ~100 km range in 5 minutes |

At US\$20.9 million for a 126-bay, 100 MW facility, the cost per charging point is approximately US\$166,000 --- substantially below Western equivalents. Milence's European network implies ~EUR 294,000 per point; the Kettleman City project in California budgeted US\$58 million for 56 chargers (~US\$1 million per point including solar and battery) [@kettleman-city-2024; @milence-network-2025].

# Head-to-Head Comparison

: Battery Swap vs Megawatt Charging vs Retrofit Swap: Key Dimensions {#tbl-swap-vs-mcs}

| Dimension | CATL swap (China) | MCS fast charging (global) | Janus retrofit swap (Australia) |
|:----------|:------------------|:---------------------------|:-------------------------------|
| Turnaround time | ~5 min | 20--45 min (improving) | ~4 min (forklift) |
| Upfront truck cost | Lower (battery leased) | Higher (battery included) | Lowest (\$150--200k conversion) |
| Infrastructure cost per site | Very high (24 packs x 171 kWh) | Lower, but grid upgrades needed | Moderate (solar + forklift + packs) |
| Grid impact | Lower (off-peak charging) | Higher (MW-scale spikes) | Lower (solar + off-peak) |
| OEM buy-in | Chinese domestic only | All major global OEMs | OEM-agnostic (retrofit) |
| Standardisation | Single standard (CATL) | CharIN MCS (open); Tesla proprietary | Proprietary (Janus only) |
| Geographic reach | China (305+ stations) | Europe, N. America, Australia | Australia only (9 stations) |
| Battery management | Centralised (CATL) | Decentralised (fleet's risk) | Centralised (Janus owns packs) |
| Technology lock-in | High (CATL ecosystem) | Low (open standard) | High (Janus ecosystem) |
| Scale (trucks, 2026) | ~200,000+ on road | ~10,000 in Europe | 23 converted |

## The Charging Speed Gap Is Narrowing

The swap model's strongest advantage is speed: 5 minutes versus 20--45 minutes for conductive charging. But this gap is closing rapidly. BYD's 1.5 MW "Flash Charging" technology --- demonstrated for passenger vehicles but applicable to trucks --- achieves 10--97% charge in 9 minutes [@byd-megawatt-2025]. Huawei's 1.44 MW chargers with 3.5C-rate truck batteries deliver ~100 km of range in 5 minutes.

At these power levels, the time penalty of conductive charging versus swap becomes marginal when including time to enter and exit a swap station, and to verify pack integrity. By the late 2020s, a 5--10 minute megawatt charge may deliver sufficient range to match the convenience of a swap stop.

## The Swap Model's Structural Advantages

Speed aside, battery swap has two structural advantages that conductive charging cannot replicate:

1. **Upfront cost reduction.** Separating the battery from the vehicle cuts the truck's purchase price by 30--40%. For a fleet operator buying 50 trucks, this is a \$5--10 million capital saving at point of purchase. Conductive charging requires the full battery cost to be embedded in the vehicle price.

2. **Grid flexibility.** A swap station's 24 battery packs (~4 MWh of storage) can charge slowly during off-peak hours and swap quickly during peak truck traffic. This decouples the timing of grid demand from the timing of truck refuelling. A conductive charger, by contrast, creates a MW-scale demand spike exactly when trucks arrive --- typically during morning and evening freight peaks.

Both advantages may erode over time: battery prices are falling (reducing the capital premium argument), and smart depot charging with on-site storage can mitigate grid peak impacts.

# Which Approach Is Winning?

**Megawatt conductive charging is the emerging global standard.** Every major Western truck OEM (Daimler, Volvo, Traton/Scania/MAN) has aligned behind MCS. Tesla is at comparable power levels with a proprietary connector. Windrose supports both CCS2 and MCS.

Battery swap is a viable and rapidly scaling solution **within China** --- where CATL can enforce standardisation across domestic OEMs, government policy supports the model, and 305+ stations already operate. But outside China, no commercial battery-swap network for heavy trucks exists, and no major non-Chinese OEM has committed to the model.

The critical question is whether Chinese truck manufacturers bring battery swap with them as they expand internationally. If XCMG, SANY, and Sinotruk enter the Australian market (as they are entering Southeast Asia and the Middle East), they may bring the swap ecosystem as a bundled offering. But the Western OEMs that dominate Australian trucking --- Volvo, Scania, Daimler, PACCAR --- are all committed to MCS.

Janus Electric's retrofit swap occupies a different niche: it is not competing with new-build trucks for new sales, but rather offering a way to electrify the existing fleet while the new-build pipeline matures. If Janus can survive its current financial constraints and scale its station network, it could serve as a transitional bridge --- particularly for fleet operators who cannot justify the capital cost of a new Windrose or Volvo FH Electric but have serviceable 3--8 year old prime movers. The model's long-term viability depends on whether the cost and performance gap between retrofit and purpose-built narrows or widens as the technology matures.

## Implications for Australia

For Australia, the relevant technology pathway is MCS conductive charging. The critical gap is not vehicle availability but **charging infrastructure on key freight corridors**. As of March 2026, Australia has no publicly accessible heavy-vehicle megawatt charging station. NET's Wilton depot will be the first significant installation.

The priority actions are:

1. **Corridor charging on the Hume, Pacific, and Newell highways** --- Australia's three highest-volume freight routes, analogous to Europe's TEN-T corridors
2. **Grid connection pre-investment** at major logistics hubs (Moorebank, Somerton, Acacia Ridge) where 10--20 MW connections will be needed
3. **Standards alignment** --- ensuring Australian regulations recognise and accommodate MCS connectors and 1,250V DC systems

## References
