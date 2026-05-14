---
title: "Alternatives to diesel backup at data centres: a competitive entry landscape"
author: "David Leitch"
date: 2026-05-13
draft: true
---

## 1. The incumbent and why it's under pressure

Diesel reciprocating gensets remain the dominant standby technology at hyperscale and colocation data centres. AirTrunk's Kemps Creek Western Sydney master plan illustrates the scale of the incumbent build: 846 emergency diesel generators, more than 18,000 kilolitres of on-site diesel storage to back 1.2 GW of IT capacity [1]. Loudoun County, Virginia alone has approximately 4,700 generators across data centre campuses, with around 8,000 across the state, the vast majority Tier II [2]. Most diesel gensets in 60Hz markets sit in the 2-3 MW class (Cat 3516, Cummins QSK60/95, mtu Series 4000, Kohler/Rolls-Royce equivalents), packaged as N+1 or 2N redundancy at \$700-1,200/kW installed (the prime mover alone is roughly half that; switchgear, fuel, tanks and integration the balance).

Three pressures are reshaping the genset market in 2025-2026:

1. **Lead-time stretch.** Cummins flagged 18-month lead times for QSK95 high-horsepower units and expanded its Fridley, Minnesota facility by USD 150 million in February 2026 to add 30% capacity; the backlog now extends "well into 2028" [3]. Caterpillar increased manufacturing capacity for data centre engines by ~125% over two years. Both OEMs have effectively been on allocation since mid-2024.
2. **Permitting friction.** Virginia DEQ moved presumptive BACT for new data-centre gen-sets to Tier 4-equivalent (SCR + DOC + DPF) from July 2026 onward [4]. NSW EPA technical noise and air-quality scrutiny on Project Mars (Lane Cove West) flagged that diesel assumptions in environmental assessments may be under-reporting NOx and SOx [5]. California already requires CARB DG certification for distributed engines.
3. **Hyperscaler decarbonisation accounting.** Scope 1 emissions from on-site combustion sit awkwardly with Microsoft/Google/AWS net-zero pledges. Even if utilisation is low (10-50 hours/year for true backup), the fuel inventory and lifecycle disclosure are now material.

The result: even where diesel remains the default for true emergency standby, operators are diversifying into adjacent technologies that handle longer-duration roles (prime power, grid bridging, ride-through) and present better emissions optics. Each section below sizes a category and identifies where it has reached commercial scale versus where it remains pilot-stage.

## 2. Natural-gas reciprocating engines

This is the category where the largest behind-the-meter dollars are currently moving. The economics are simple: pipeline gas at a Henry Hub-linked basin price plus delivery (typically USD 3-6/MMBtu in the US Gulf and Marcellus regions) yields fuel costs of roughly USD 25-50/MWh through a 42-44% efficient engine, comfortably below grid retail in stressed PJM/ERCOT pockets, and the engines can be containerised and stood up in 12-18 months versus 4-7 years for transmission.

### Key OEM offerings

**Cat G3520** (1.75-2.5 MW, spark ignition): the first EPA-certified gas genset rated to NFPA 110 Level 1 Type 10, UL 2200 listed. Quick-start (10-second loading) variant launched 2020 [6]. Typical install \$1,400-1,800/kW depending on packaging.

**Cat G3516 / G3612 / G3616** (1-4 MW class): the larger 16-cylinder G3616 is rated to ~3.2 MW continuous at 900 rpm.

**Wärtsilä 34SG and 50SG** (5-12 MW class, spark-ignition gas, fuel-flex roadmap to hydrogen blends): Wärtsilä had sold over 1.6 GW into the US data centre market by Q2 2026, including:
- 412 MW (40 × 34SG) for an Ohio hyperscale project, the 34SG's data-centre debut [7]
- 790 MW (42 × 50SG) for a Texas data centre, fifth US data-centre order [8]
- 507 MW (27 × 50SG) earlier US order [9]
- Engines explicitly marketed as convertible to sustainable fuels.

**INNIO Jenbacher J624 and J920**: The J624 (4.5 MW, turbocharged, containerisable) is the workhorse of VoltaGrid's behind-the-meter fleet. The J920 FleXtra is the most powerful Jenbacher engine at 9.5-10.6 MW with 48.7% electrical efficiency, two-minute cold start, and CHP-mode efficiency over 90% [10][11]. VoltaGrid placed an order with INNIO for 300 J624 and J620 engines integrated into its proprietary QPac platform in January 2025 [12].

**Cummins HSK78G** (up to 2 MW per engine, 44% efficient, tolerant of pipeline gas to 70MN methane number) [13].

**Rolls-Royce mtu Series 4000** gas gensets: 20V4000 L64 platform delivering 2.8 MW with 45-second fast-start (60Hz, from 2026); 120-second variant already shipping globally; 84,000-hour overhaul life [14]. Hydrogen certification roadmap on the same engine block.

### Hyperscale gas-genset deployments (commercial, not pilot)

**Table 1**

**Selected behind-the-meter gas-engine deployments to data centres, 2024-2026**

| Operator | Site | Capacity | Equipment | Status |
|:---------|:-----|--------:|:----------|:------|
| Wärtsilä / hyperscaler | Ohio | 412 MW | 40 × 34SG | Q2 2026 order; COD early 2028 |
| Wärtsilä / hyperscaler | Texas | 790 MW | 42 × 50SG | Q2 2026 order |
| Wärtsilä / hyperscaler | Undisclosed US | 507 MW | 27 × 50SG | Booked 2025 |
| VoltaGrid / Vantage | North America (multiple) | >1 GW | Jenbacher J624 microgrids | 2025 deployment |
| VoltaGrid / Oracle | Texas | 2.3 GW | Jenbacher in QPac | 2025-2026 |
| xAI Colossus 1 | Memphis | ~155 MW + (34 × J624) | INNIO J624 + GE turbines | Operating |
| ExxonMobil / hyperscaler | Permian basin region | >1,500 MW | Gas-fired plus 90% CCS | FID late 2026 (announced Dec 2024) |
| Meta / Entergy | Richland Parish, Louisiana | 2,250 MW | 3 × heavy-duty gas turbines | LPSC approved Aug 2025 |

*Source: SemiAnalysis "Onsite Gas Deep Dive" Oct 2025 [15]; Wärtsilä press releases [7][8][9]; VoltaGrid/INNIO press releases [12]; Microgrid Knowledge [16]; PowerMag [17]; Louisiana Public Service Commission filings [18]. Meta's Entergy contract is utility-built rather than behind-the-meter strictly, but functionally captive to the load.*

### Pricing benchmarks

Drawing on SemiAnalysis's detailed October 2025 build-up [15]:

- Gas reciprocating (high-speed Jenbacher J624 class): USD 1,700-2,000/kW all-in, 15-24 month lead time including ~10 months commissioning, 10-minute cold-to-full-output ramp.
- Medium-speed (Wärtsilä 34SG/50SG, Bergen, Everllence): USD 1,700-2,000/kW, similar lead times, better part-load heat-rate, lower maintenance hours.
- Diesel reference: USD 700-1,100/kW for the genset alone (Cat 3516 class 2-2.5 MW), 18-24 month lead time at major OEMs.

The fuel-cost advantage of gas over diesel is roughly 60-70% per MWh at 2025 commodity prices (gas \$30-40/MWh fuel cost vs diesel \$140-180/MWh in standby diesel use). The trade-off: gas requires a firm pipeline connection (an additional infrastructure constraint, but cheaper than waiting for transmission); diesel ships and stores anywhere with tanks.

### Where this displaces diesel

Pipeline-gas-available sites where the operator can size the gas plant for either prime+standby (microgrid-style, with grid as backup) or for extended-runtime standby with diesel as last-resort. The VoltaGrid model — gas microgrid as primary, grid as supplementary, diesel for prolonged gas outage only — is becoming standard in ERCOT and Marcellus regions. In Australia, behind-the-meter gas reciprocating at hyperscale data-centre scale has not yet emerged commercially: AEMO gas supply tightness, the AEMC's gas-statement-of-opportunities consistently flagging east-coast supply shortfalls from 2027, and the lack of established BTM gas-plus-DC precedent are the binding constraints rather than equipment availability.

## 3. Aeroderivative and industrial gas turbines

Where gas reciprocating engines top out around 12 MW per unit and need many units for hyperscale loads, gas turbines bring 30-50 MW per box in the aero class and 100+ MW per box in the heavy-duty class. This is the technology now powering the most-publicised hyperscale on-site builds.

### Key OEM products

**GE Vernova LM2500XPRESS** (34 MW) and **LM6000** (~57 MW): aeroderivatives derived from CF6 jet engines. Crusoe ordered 29 LM2500XPRESS units totalling ~1 GW for Abilene; GE Vernova has subsequently been delivering them through 2025 [19][20]. SemiAnalysis estimates installed cost at USD 1,700-2,000/kW.

**GE Vernova heavy-duty 7HA/9HA** (300+ MW class): the technology Entergy is deploying for Meta's Louisiana Hyperion campus (3 × ~750 MW units). Backlog into 2030. GE Vernova booked 18 GW of turbine orders in Q4 2025 alone; 80 GW backlog at year-end 2025; CEO Strazik expects sold-out through 2030 by end-2026 [21][22].

**Solar Turbines** (Cat subsidiary) — Mercury 50 (4.6 MW, 38.5% efficient, recuperated, single-digit NOx ppm), Centaur 40/50, Taurus 60/65/70, Mars 100, Titan 130/250: 5-50 MW range, USD 1,500-1,800/kW. Better hot-climate derating than aeros. Lead times 12-36 months new; <12 months for refurbished [15][23].

**Siemens SGT-A35/A45** (aeroderivatives, ex-Rolls-Royce Industrial Trent/RB211 lineage, 25-40 MW): comparable to GE LM2500/LM6000 class.

**Mitsubishi FT8 MOBILEPAC** (~30 MW): trailerable; APR Energy has been using these in rental fleet deployments to hyperscalers.

**Vericor PowerWorks** and similar small-aero specialists: 4-10 MW range for fast-start backup roles, more niche.

### The big shift in 2024-2026

The hyperscale shift to turbines as primary on-site generation has three drivers:
1. **Grid-connection queues** stretching 4-7 years in PJM Dominion and ERCOT-Houston make waiting for transmission untenable when GPU depreciation runs at 25% per year of TCO.
2. **Scope 1 vs Scope 2 emissions accounting:** owning a 90% CCS-equipped on-site plant looks better to some investors than buying brown grid power.
3. **Dispatchability + speed-to-energise:** turbines and reciprocating engines can both bridge to grid in 12-18 months from FID, where transmission upgrades take 4-7 years.

### Lead-time bottleneck

Heavy-duty turbine cores now have 24-30 month build/commission cycles; turbine blade and vane supply is choked by just four Western foundries (PCC, Howmet, CPP, Doncasters) [15]. GE Vernova target production: 20 GW/year mid-2026, stretching to 24 GW/year by mid-2028. Heavy-duty new orders quoting 2028+. Aeroderivative supply (LM2500XPRESS, FT8) somewhat better — Boom Supersonic is even retooling to ship 42 MW "Symphony-derived" turbines, with 29 units booked by Crusoe [24].

### Where this displaces diesel

Turbines do not displace diesel in the strict NFPA 110 emergency-standby role (they're slow-starting and run inefficiently at light load). They do displace the *need* for a fully diesel-fed grid-tied campus: behind-the-meter gas turbines as primary power, with diesel reduced to a smaller true-emergency role behind UPS+BESS. This is the architecture at Crusoe Abilene and the OpenAI Stargate "986 MW from 29 × 34 MW" Texas campus [25].

## 4. Fuel cells

After more than a decade of niche use, fuel cells have entered hyperscale procurement in serious volume in 2025-2026, driven almost entirely by Bloom Energy's solid-oxide fuel cell (SOFC) platform.

### Bloom Energy SOFC

Bloom Energy Server modules (commercial 325 kW base unit, multiple-MW campuses): nominal heat rate 6,000-7,000 BTU/kWh on natural gas reformed on-site. Capex USD 3,000-4,000/kW installed [15]. Cell stack life 5-6 years (a non-trivial refurbishment expense).

Commercial deployments at scale through 2025-2026:
- **Equinix:** over 100 MW signed across 19 data centres; ~75 MW operational, 30 MW under construction [26]
- **Oracle:** 1.2 GW initial deployment of a master agreement up to 2.8 GW [27]
- **AEP / Indiana Michigan:** 1 GW agreement to power AI data centres off-grid [28]
- **Brookfield:** USD 5 billion partnership to deploy Bloom SOFCs globally [29]
- Total deployed to date: over 400 MW [26].

Bloom's stated 90-day deployment timeline is the major differentiator versus turbines — when grid interconnection is blocked but pipeline gas is available, fuel cells can bridge the gap. Their permit footprint is also lighter: "no material air pollution besides CO2" makes minor-source permitting feasible in jurisdictions where reciprocating engines need full Title V.

### Other fuel-cell technologies

**FuelCell Energy** (molten carbonate, MCFC): operates 58 MW single-site fuel-cell park in South Korea; signed MOU with Inuverse in July 2025 for up to 100 MW phased deployment from 2027 at AI Daegu Data Center [30]. MCFC tolerates internal reforming of natural gas at ~700°C, advantage for combined CHP roles but slower-ramping than SOFC.

**Doosan Fuel Cell** (Korea, phosphoric acid PAFC predominantly): focuses on data-centre supply solutions; emphasises PAFC's reliability rather than efficiency.

**Plug Power** (PEM hydrogen fuel cells): Microsoft's 3 MW Plug-built backup demo at Latham NY (2022) was the high-profile "moon landing moment" — but PEM-on-hydrogen at data centres is still pre-commercial at hyperscale [31]. Plug expects "deployments at some scale" by late 2025; the company is also financially stressed (going-concern doubts raised 2023). Amazon's 17,000+ Plug forklift fuel cells are commercial, but extrapolation to DC backup is not.

### Pricing reality

Fuel cells are still the most-expensive per-kW capex option for on-site power (3-4× diesel, ~2× gas reciprocating). They cannot peak-shave or function as true seconds-scale emergency backup. The 90-day deployment and minor-source permit advantages are what justify the premium for hyperscalers willing to pay for time.

### Status assessment

**Commercially mature:** Bloom SOFC on natural gas (clear hyperscale procurement at GW-scale, multiple operators).
**Approaching commercial:** FuelCell Energy MCFC, Doosan PAFC for South Korean and selected US sites.
**Still pilot:** PEM hydrogen fuel cells for primary DC power. Hydrogen supply, storage, and cost remain unresolved.

## 5. BESS as primary or first-line backup

Battery storage at data centres now spans three architecturally distinct roles, which is causing terminology confusion in trade press:

1. **UPS replacement** (seconds-minutes ride-through): lithium-ion replacing VRLA at the rack/row level. Mature and commercial.
2. **Behind-the-meter co-located BESS for PPA firming and grid services**: the AWS Australia model.
3. **Long-duration BESS as bridge to genset start or as substitute for some genset capacity**: 2-4 hours, behind-the-meter at campus scale.

Roles 2 and 3 are where the diesel-displacement story sits.

### Sizing and economics

A typical 100 MW IT-load campus might pair with 50-200 MWh of BESS (1-2 hours at full IT load, or 4 hours at half load). Tesla Megapack at ~USD 250-350/kWh installed (recent generation) plus power-conversion and balance-of-plant gives ~USD 400-500/kWh all-in for the 4-hour duration application. Fluence Gridstack, Wärtsilä Quantum, Sungrow, and CATL/Envision packages are roughly comparable.

Google's 2020 St. Ghislain (Belgium) 2.75 MW / 5.5 MWh battery retrofit was the first major hyperscaler proof-of-concept that BESS could carry the campus load in lieu of diesel for several minutes [32]. Tesla Megapack is the primary battery at xAI's Colossus in Memphis. Most large hyperscalers now spec at least some battery duration behind the UPS in new builds.

### The Australian case: AWS PPA portfolio

Of the 9 PPAs Amazon Web Services signed in Australia in 2026, 8 include co-located BESS. The structure is:
- 3 large-scale solar+BESS hybrids (Muswellbrook 94.5 MW PV / 70 MW BESS; Forest Glen 72/72; Anza Laceby 48/48)
- 4 distributed solar+BESS hybrids
- 1 wind farm
- 1 retrofit BESS at the previously announced Mokoan solar farm [33]

This is grid-side firming of the PPA portfolio rather than behind-the-meter campus backup. The BESS sits at the generator site, not the data-centre site. AWS's behind-the-meter backup at the data centres themselves remains a more conventional UPS+diesel architecture for now. The PPA-co-located BESS is doing PPA shape-firming, FCAS provision, and arbitrage for revenue — it's a renewable-firming play, not directly a backup-displacement play. AWS describes itself as "entirely focused on renewables firmed with batteries" in Australia [33].

### Limitations as backup

- **Sustained discharge:** even a 4-hour battery cannot ride through a multi-hour grid outage at full IT load without coupling to a generator. The architecture is BESS-for-ride-through + gas/diesel-for-runtime.
- **Capacity fade and round-trip:** 2-3% annual capacity loss; allowance for cycle losses degrades effective backup duration over the asset life.
- **Thermal management:** lithium-ion fire and runaway risk; NSW EPA and similar regulators are tightening separation and venting requirements.

### Status assessment

Mature for ride-through and PPA firming. The "fully BESS-backed data centre" (no diesel, no gas) remains aspirational at hyperscale outside microgrid-island contexts.

## 6. Renewable and drop-in liquid fuels (HVO)

Hydrotreated vegetable oil — known commercially as renewable diesel or HVO — meets EN 15940 and ASTM D975 and is a drop-in replacement for fossil diesel in unmodified engines. Lifecycle CO2 reduction is typically 70-90% depending on feedstock (waste oils, tallow, used cooking oil score highest). Critically, HVO does *not* significantly reduce NOx, particulates, or SOx — these are combustion products and depend on engine controls, not fuel carbon. So HVO buys carbon optics but does not solve local air-quality permits.

### Hyperscale adoption

- **Microsoft Sweden** uses Preem Evolution Diesel Plus (50% renewable diesel content); projects ~45% lifecycle CO2 reduction vs fossil [34].
- **Microsoft Denmark East** uses HVO where available.
- **Microsoft Clonee, Ireland** piloted HVO from 2024 (clear adoption trajectory in EU).
- **AWS** committed to converting all European data centres to HVO, starting Ireland and Sweden.
- **Equinix, Vantage, Digital Realty, STACK, Green Mountain** — all running HVO at selected European facilities.
- **Bridge Data Centres** (Bain-backed APAC operator) completed an HVO backup-fuel pilot across selected APAC facilities in 2026 with EcoCeres [35].

### Pricing premium

HVO sits at a typical 20-50% premium to fossil diesel in Europe (volatile, feedstock-dependent). In Australia, RD2Go and Delta Specialised Energy supply imported HVO; the Australian premium is wider — current market chatter suggests 30-60% premium versus pump diesel, depending on volume and delivery — because there is no domestic HVO production yet. Annual fuel-polishing savings (HVO is shelf-stable and doesn't separate or accumulate water) partially offset the premium for low-utilisation backup fleets, which can be six-figure savings per multi-site fleet [36].

### Australian supply

Viva Energy and Delta Spec import HVO today. BP's Kwinana biorefinery conversion (~A\$580m, WA government approved) is targeted to start operations in 2026-27, producing SAF and HVO from local and imported feedstocks (canola, etc.) [37][38]. BP's global biofuels target is ~50,000 bpd of SAF+HVO by 2030 across multiple sites.

### Status assessment

Commercially mature where supply is available. The barrier is fuel supply, not technology: every diesel generator is already HVO-ready.

## 7. Hydrogen-ready engines and hydrogen fuel cells

This is where the hyperscale press releases run furthest ahead of the underlying physics and economics. The honest assessment:

### Engines on hydrogen blends

- **Cummins QSK60** with hydrogen-blend roadmaps: pre-commercial.
- **mtu Series 4000**: Rolls-Royce certified hydrogen capability for the 4000 series engine block (announced 2024-2025); production conversion from natural gas is straightforward in principle, but no commercial hydrogen-fired DC installation has happened at scale [14][39].
- **Cat 100% hydrogen demo** (Microsoft, 2022): Cat ran a single-engine demo on 100% hydrogen at MS Quincy.
- **Jenbacher J920** is already certified to run on hydrogen blends; the J624 has a hydrogen roadmap.

### Hydrogen PEM fuel cells

Microsoft Plug Power 3 MW demo (Latham, 2022) was the high-water mark for proof-of-concept. National Grid Ventures is installing the first 100% hydrogen-fuelled commercial linear generator (Mainspring) at Northport Power Plant in NY. Plug Power expects scale data-centre deployments "late 2025" — these are still at the order-of-tens-of-MW level, not hundreds.

### The hydrogen cost-and-supply reality

Green hydrogen production cost in Australia today is roughly A\$8-15/kg, which at ~33.3 kWh/kg LHV translates to ~A\$240-450/MWh of fuel cost *before* conversion losses. Through a 55-60% efficient PEM fuel cell, that's A\$400-820/MWh of electricity. Compare to gas at ~A\$80-120/MWh fuel-cost-equivalent through a 45% engine, or diesel at A\$140-180/MWh through a Tier 4 standby genset, and the economics are not close.

The supply problem is worse: there is no large-volume green-hydrogen distribution network in Australia, the US, or most of Europe. Pipeline hydrogen blending is at single-digit-percent demonstration scale. Liquid hydrogen logistics is bespoke and expensive. Storage at data-centre quantities (hundreds of tonnes for multi-day backup) has not been engineered.

### Status assessment

**Pilot-stage in every dimension that matters at hyperscale.** Engines and fuel cells are technically ready; fuel supply, fuel storage, fuel cost, and lifecycle infrastructure are not. Treat 2025-2026 hydrogen DC announcements as marketing investments in optionality, not commercial procurement.

## 8. Microgrid integrators and packaging plays

The pure equipment OEMs (Wärtsilä, INNIO, Cat, Cummins, GE Vernova, Solar Turbines, Bloom) sell metal. The integrators wrap that metal in a turnkey deliverable — sizing, paralleling, controls, fuel management, permits, ride-through architecture, and often financing. Several have built defensible positions in 2024-2026:

**Enchanted Rock** (Houston-based): natural-gas reciprocating microgrids specifically designed for fast-start, dual-purpose backup and grid-support roles in ERCOT. CARB DG-certified engine. Marketed as a direct diesel replacement with diesel-like footprint and seconds-scale start. The "bridge-to-grid" model — own-and-operate a microgrid that powers the data centre until the utility connection energises, then transitions to grid-support role — has been a clear winner [40][41]. Partnered with US Energy to provide backup for at least one Microsoft Texas data centre.

**VoltaGrid** (Houston-based): factory-built QPac modules (20 MW per node, up to 200 MW under minor-source air permit) wrapping Jenbacher J624 and J620 engines. As covered in §2, has booked >3.3 GW with Vantage and Oracle through 2026, with delivery capacity of "up to 50 MW per month" of QPac units [12][42]. Closest thing to "buy a data-centre-grade microgrid off-the-shelf".

**Mainspring Energy**: the most-interesting equipment innovation in the category. The Linear Generator (LGen) is a small-format (single-unit ~250 kW; site-deployed in arrays) fuel-flexible power generator that uses linear reaction-control rather than rotating crankshaft. Runs on natural gas, biogas, propane, field gas, associated gas, or hydrogen without retrofit, switches between fuels without downtime [43]. Mainspring closed USD 258m Series F in April 2025 with Amazon Climate Pledge Fund participating; AEP has a utility pilot; National Grid Ventures is installing the first 100% hydrogen LGen at Northport NY [44]. AWS investment via Climate Pledge Fund is suggestive of behind-the-meter pilot interest at hyperscale, but no announced large DC commercial commitment yet. The 250-kW unit size is small for hyperscale; Mainspring's path is array-of-units.

**Cummins / Caterpillar microgrid integration**: in-house competitive offering wrapping their own engines plus BESS and switchgear; functionally competitive with VoltaGrid but with the OEM's installed-base relationship.

**Aggreko, APR Energy, United Rentals power division**: established rental/temporary power operators now selling 100 MW+ packages to hyperscalers on rental terms. APR deployed 100 MW mobile gas-turbine fleet for a single AI client in early 2025; Duos Technologies installed a 100 MW backup system in 10 days [45]. This is rental-as-bridge-power, distinct from owned microgrid integration. United Rentals and Atlas Copco buy-and-build consolidating the rental segment.

## 9. Where's the gap for a new entrant?

David, this is the strategic question. Six concrete entry plays, ranked by my read of credibility-versus-difficulty.

### 9.1 Lead-time arbitrage: refurbished gensets and fast-track new packaging

**The opening:** Cat 3516 and Cummins QSK60/95 lead times of 18-24+ months out of OEM new-build channels, with backlog into 2028. Used and refurbished generators in the 2-3 MW class trade actively (Woodstock Power, Central States, USP&E, Crusader, IMP). A reseller/refurbisher with rigorous data-centre-grade testing, warranty, and load-bank certification can sell into the 12-18 month gap.

**The reality check:** Many hyperscalers refuse refurbished kit on warranty/insurance grounds; the buyer pool is mid-tier colo and edge. Margin is real but capped. Capital intensity is moderate.

**Australian angle:** No domestic refurbisher of consequence exists at data-centre scale. With Australian data-centre build accelerating (AirTrunk Kemps Creek, NEXTDC S7 with OpenAI's 550 MW Stargate AU, Microsoft Sydney expansion), demand is real. A purpose-built Sydney/Melbourne refurbishment yard with OEM-parts supply agreements and 12-month delivery guarantees would have a defensible price/lead-time wedge in colo and tier-2 hyperscale.

### 9.2 Backup-as-a-service (BaaS) — own-and-operate the fleet

**The opening:** Most colo and mid-tier DC operators do not want to own, maintain, fuel-manage, run quarterly load tests, manage emissions reporting, or carry the capital line for their backup fleet. A BaaS operator owns the generators, BESS, controls, and fuel supply, and charges \$/MW/year for guaranteed availability under SLA (Tier III/Tier IV uptime guarantee, with insurance underwriting the SLA).

**Existing players who *partially* do this:** Aggreko (rental, short-term); Enchanted Rock (microgrid as primary, with the operator paying for energy not just availability); a few utility-affiliated providers. Nobody is doing "long-term availability-fee BaaS" as the headline product.

**The reality check:** This is a capital-heavy build (own the gensets means you fund \$700-1,200/kW yourself, then earn a multi-year availability fee). Underwriting the SLA depends on insurance/reinsurance comfort, which is achievable but slow. Counterparty credit is a real risk (you carry the asset; if the DC tenant exits, the gensets are stranded). Best path: anchor with one or two major colos as launch tenants, then add capacity.

**Why this might work in Australia specifically:** Australian colo operators (NEXTDC, CDC, DCI, Macquarie, Equinix) are mostly capital-constrained relative to US peers; a leasing/BaaS model relieves their balance sheet. The model fits a financial-sponsor profile (infra debt funds, super funds) needing long-duration availability-linked cash flows.

### 9.3 Service and aftermarket — the independent service company

**The opening:** Cat and Cummins make money in their service and parts businesses through 30+ year operating lives of installed gensets. Independent service operators (the third-party maintenance market is ~USD 1.2bn globally but extremely fragmented per Gartner [46]) can offer 30-40% pricing below OEM service contracts on out-of-warranty fleets. Genuine OEM parts can be sourced for most components; specialist parts (control boards, injection systems) are the chokepoint.

**The reality check:** Customer trust is hard to win against the OEMs in a critical-power application. The unique selling proposition is usually cost-saving on the older fleet plus willingness to support unusual configurations or older firmware.

**Australian angle:** Existing operators (Cirrus Power Systems in NSW does Jenbacher; multiple regional diesel-service operators) serve mining, hospitals, telecoms. None is publicly positioning specifically for the data-centre wave. A focused DC-grade independent service operator with NATA-accredited fuel quality testing, predictive-maintenance instrumentation, and a 24/7 emergency-response SLA could win mid-tier business, then progressively the hyperscalers as fleets age. Capital-light; high-margin; service annuities are valuable on a multiple.

### 9.4 HVO fuel supply and distribution

**The opening:** Australian HVO supply is currently entirely imported (RD2Go, Delta Spec, Viva). BP's Kwinana biorefinery is targeting 2026-27 start. Hyperscalers' decarbonisation commitments (AWS, Microsoft) are pulling demand. The price premium of 30-60% over fossil diesel is paid by customers willing to monetise Scope 1 reductions.

**The reality check:** This is a fuel-supply business, not a technology business. Margins are real but operational (storage, blending, delivery, certification). The path to a sustainable competitive position is either:
(a) anchor an Australian feedstock-sourced production facility (UCO collection logistics, tallow, etc.) and partner with a refiner, or
(b) own the data-centre-tailored distribution stack (on-site storage, fuel polishing, certification, blended-product delivery) at premium pricing.

**Why play (b) is interesting:** A premium DC-grade HVO logistics operator (think AdBlue but for renewable diesel) with ISO-tank delivery, NATA-certified fuel testing, certificate-of-origin chain-of-custody, and on-site polishing services bills at considerably higher unit margins than bulk fuel. The volume per site is modest (10-30 ML/year per major DC), but high-value.

### 9.5 Australian assembly and AHJ-compliance integration

**The opening:** Every gas reciprocating engine and aero turbine in Australian DCs today is imported as a packaged genset or as bare components requiring local switchgear, controls, paralleling, and AS-compliant enclosure work. The major OEMs are not focused on local content; the local engineering-procurement-construction (EPC) market is fragmented.

**The reality check:** Building genuine local assembly capacity for >2 MW units requires capital and skills that Australia largely lacks today. A more credible play is "AS 1940-compliant integrated systems": bringing in OEM cores and adding locally-fabricated enclosure, switchgear integration, paralleling, AS 3000-compliant controls, and AHJ-relations as a turnkey package. This already exists in fragmented form (Synertec, Energy Power Systems Australia, MTU Detroit Diesel Australia, etc.). The opportunity is consolidation and DC-specialisation.

### 9.6 Software and controls — the third-party platform

**The opening:** Cat (Cat Connect) and Cummins (PrevenTech) sell their own paralleling, sequencing, fuel monitoring, and predictive maintenance platforms locked to their own genset fleets. Hyperscale operators with mixed fleets (often deliberately split across vendors to manage supplier risk) want a vendor-agnostic supervisory platform.

**The reality check:** This is the most-speculative entry of the six. Building a third-party platform that wins against OEM tooling requires deep DCS/SCADA capability, integration certifications, and trust in critical-power applications. The closest precedents are FlexGen (BESS-side controls, broadening) and a few startups (Sapient Industries, Eaton's Brightlayer). The market exists; the moat is hard.

**Why this is less compelling for a 2-person ITK-style entry:** capital requirements are significant (you need a real software product with safety and cyber-security certifications); product cycle is long; the moat is technical-credibility, not first-to-market.

### What I'd discount

- **A "build a hydrogen ecosystem for DCs" play.** Pre-commercial fuel supply, unresolved storage, unappealing economics. Unlikely to commercialise at scale before 2030.
- **A "build a small modular reactor for DCs" play.** That's a different question, but every nuclear-DC press release through 2025-2026 is 2030-2035 horizon at the earliest.
- **A "compete head-on with VoltaGrid in microgrid packaging" play.** Too capital-intensive against entrenched ERCOT-region competition. An adjacent geographic strategy (e.g., NEM-region microgrid packaging) is more plausible.

## 10. Summary of where I'd put new entry capital

The four most-credible plays for a sophisticated new entrant (not in priority order — depends on capital scale and risk appetite):

**Capital-light, high-margin:** Independent data-centre-grade service and aftermarket operator in Australia (option 9.3). Annual recurring service revenue, multi-year contracts, valuable on exit.

**Capital-medium, attractive returns:** Backup-as-a-service availability-fee operator with one or two major colo anchor tenants (option 9.2). Best suited to a financial-sponsor partnership.

**Capital-medium, fuel-supply angle:** DC-specialised renewable-diesel distribution and on-site logistics (option 9.4(b)). Modest absolute volumes but premium pricing; fits hyperscaler decarbonisation procurement.

**Speculative but timing-aligned:** Lead-time arbitrage via refurbished/fast-track packaging for the Australian colo and tier-2 hyperscale wave (option 9.1). Limited duration of opportunity (3-5 years before OEM new-build supply catches up), but real margin window now.

The technology-by-technology maturity assessment is summarised below.

**Table 2**

**Commercial maturity of diesel-genset alternatives at hyperscale data centres, May 2026**

| Technology | Maturity | Lead time | Indicative capex (USD/kW) | Where displacing diesel |
|:-----------|:--------:|:---------|:--------------------------|:------------------------|
| Diesel reciprocating (incumbent) | Mature | 18-24 months | 700-1,100 | Reference |
| Gas reciprocating high-speed (J624 class) | Commercial | 15-24 months | 1,700-2,000 | Prime + standby microgrid |
| Gas reciprocating medium-speed (34SG/50SG, Bergen) | Commercial | 15-24 months | 1,700-2,000 | Hyperscale BTM prime |
| Aero gas turbine (LM2500XPRESS, FT8) | Commercial | 18-36 months | 1,700-2,000 | BTM prime, large hyperscale |
| Heavy-duty gas turbine (7HA/9HA) | Commercial but constrained | 36-60+ months | 800-1,200 | Utility-built behind contract |
| Industrial gas turbine (Solar, Siemens SGT-800) | Commercial | 12-36 months | 1,500-1,800 | Hot-climate hyperscale |
| Bloom SOFC fuel cell | Commercial | 90 days from order | 3,000-4,000 | Permit-constrained sites |
| FuelCell Energy MCFC | Approaching commercial | 18-24 months | ~3,000-4,000 | Korean DC market |
| BESS for ride-through (Megapack, Quantum) | Mature | 6-12 months | 400-500 per kWh | UPS extension; PPA firming |
| HVO drop-in fuel | Commercially supplied | n/a (fuel) | 30-60% fuel premium | Decarbonisation optics |
| Mainspring linear generator | Early-commercial | <12 months | n/d publicly | Niche, fuel-flexible |
| Hydrogen reciprocating (mtu, Cat) | Pilot | n/d for commercial | n/d | Demonstrations only |
| Hydrogen PEM fuel cell | Pilot | n/d | n/d | Demonstrations only |

*Source: Author analysis drawing on SemiAnalysis Oct 2025 [15]; OEM datasheets and press releases (Cat, Wärtsilä, INNIO, Cummins, Rolls-Royce, GE Vernova, Solar Turbines, Bloom Energy, Mainspring) [6][7][8][10][11][12][14][20][21][24]; Data Center Dynamics, Power Magazine, Microgrid Knowledge, Hartford Business reporting [16][17][26][27][29][30]; AWS Australia PPA disclosures [33]. n/d = not publicly disclosed at meaningful resolution.*

## References

1. ACS Information Age, "Concern over Australia's most power-hungry data centre", 2026: https://ia.acs.org.au/article/2026/concern-over-australia-s-most-power-hungry-data-centre.html
2. Virginia Mercury, "Virginia regulators weigh expanded use of data centres' polluting generators", 16 Dec 2025: https://virginiamercury.com/2025/12/16/virginia-regulators-weigh-expanded-use-of-data-centers-polluting-generators/
3. Tikr/Cummins investor disclosure, "Cummins Worst Truck Cycle in 20 Years…", 2026: https://www.tikr.com/blog/cummins-worst-truck-cycle-in-20-years-still-produced-record-earnings-heres-why
4. Trinity Consultants, "Virginia DEQ Releases Three Air Permitting Guidance Documents for Data Centers", 2025: https://trinityconsultants.com/resources/virginia-department-of-environmental-quality-releases-three-air-permitting-guidance-documents-for-data-centers/
5. NSW Planning Portal, Project Mars Data Centre — submissions and assessment documentation: https://www.planningportal.nsw.gov.au/major-projects/projects/project-mars-data-centre
6. PowerSystemsToday, "Caterpillar Launches Quick-Starting G3520 2- & 2.5-MW Natural Gas Generators", Jul 2020: https://www.powersystemstoday.com/blog/power-system-news/2020/07/caterpillar-launches-quick-starting-quick-loading-g3520-2-and-25-mw-natural-gas-generators
7. Wärtsilä press release, "Wärtsilä's 34SG engine makes its data center debut with new 412 MW U.S. project", 16 Apr 2026: https://www.wartsila.com/media/news/16-04-2026-wartsila-s-34sg-engine-makes-its-data-center-debut-with-new-412-mw-u-s-project-3740972
8. Wärtsilä press release, "Wärtsilä continues to expand its data center footprint with new 790 MW order in Texas", 23 Apr 2026: https://www.wartsila.com/media/news/23-04-2026-wartsila-continues-to-expand-its-data-center-footprint-with-new-790-mw-order-in-texas-the-next-data-center-alley-3744599
9. Wärtsilä press release, "507 MW order in the US", 20 Nov 2025: https://www.wartsila.com/media/news/20-11-2025-wartsila-continues-growth-in-the-data-center-segment-with-a-507-mw-order-in-the-us-offering-engines-as-a-reliable-power-solution-3686573
10. INNIO Jenbacher J920 FleXtra product page: https://www.jenbacher.com/en/gas-engines/type-9/j920-flextra/
11. Power Engineering International, "GE Jenbacher launches 9.5 MW, 48.7 per cent efficient J920 gas engine": https://www.powerengineeringint.com/world-regions/asia/ge-jenbacher-launches-9-5-mw-48-7-per-cent-efficient-j920-gas-engine-scheduled-for-installation-from-2012/
12. VoltaGrid press release, "VoltaGrid and INNIO-Jenbacher Partner to Revolutionize Data Center Power Solutions with QPac", 16 Jan 2025: https://voltagrid.com/voltagrid-and-innio-jenbacher-partner-to-revolutionize-data-center-power-solutions-with-qpac
13. Cummins HSK78G specification sheet: https://www.cummins.com/sites/default/files/2019-08/Spec-Sheet-HSK78G-50Hz_2.pdf
14. Rolls-Royce press release, "Rolls-Royce introduces fast-start mtu gas gensets for powering data centers", 10 Feb 2025: https://www.rolls-royce.com/media/press-releases/2025/02-10-2025-rr-introduces-fast-start-mtu-gas-gensets-for-powering-data-centers.aspx
15. SemiAnalysis, "How AI Labs Are Solving the Power Crisis: The Onsite Gas Deep Dive", Oct 2025: https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power
16. Microgrid Knowledge, "Gas-fired Microgrids to Power Data Centers at Heart of New VoltaGrid-Vantage Deal": https://www.microgridknowledge.com/data-center-microgrids/news/55267670/gas-fired-microgrids-to-power-data-centers-at-heart-of-new-voltagrid-vantage-deal
17. PowerMag, "Oracle Taps VoltaGrid for 2.3-GW Modular Gas Fleet to Power AI Data Centers Across Texas": https://www.powermag.com/oracle-taps-voltagrid-for-2-3-gw-modular-gas-fleet-to-power-ai-data-centers-across-texas/
18. TechCrunch, "Gas power plants approved for Meta's \$10B data center", 21 Aug 2025: https://techcrunch.com/2025/08/21/gas-power-plants-approved-for-metas-10b-data-center-and-not-everyone-is-happy/
19. Data Center Dynamics, "Crusoe orders 19 natural gas turbines from GE Vernova": https://www.datacenterdynamics.com/en/news/crusoe-orders-19-natural-gas-turbines-from-ge-vernova-to-power-data-centers/
20. GE Vernova press release, "29-unit aeroderivative gas turbine deal to deliver power to AI data centers": https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers
21. Utility Dive, "GE Vernova expects to end 2025 with an 80-GW gas turbine backlog that stretches into 2029": https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/
22. Power-Eng, "Data centers drive record surge in GE Vernova power equipment orders as turbine slots tighten through 2030": https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/
23. Solar Turbines product line page: https://www.solarturbines.com/en_US/products/power-generation-packages.html
24. TechCrunch, "Boom Supersonic raises \$300M to build natural gas turbines for Crusoe data centers", 9 Dec 2025: https://techcrunch.com/2025/12/09/boom-supersonic-raises-300m-to-build-natural-gas-turbines-for-crusoe-data-centers/
25. Tom's Hardware, "U.S. electricity grid stretches thin as data centers rush to turn on onsite generators": https://www.tomshardware.com/tech-industry/artificial-intelligence/u-s-electricity-grid-stretches-thin-as-data-centers-rush-to-turn-on-onsite-generators-meta-xai-and-other-tech-giants-race-to-solve-ais-insatiable-power-appetite
26. Bloom Energy, "Bloom Energy Expands Data Center Power Agreement with Equinix Surpassing 100MW": https://www.bloomenergy.com/news/bloom-energy-expands-data-center-power-agreement-with-equinix-surpassing-100mw/
27. Bloom Energy investor release, "Bloom Energy and Oracle Expand Strategic Partnership to Deploy up to 2.8 GW": https://investor.bloomenergy.com/press-releases/press-release-details/2026/Bloom-Energy-and-Oracle-Expand-Strategic-Partnership-to-Deploy-up-to-2-8-GW-to-Accelerate-AI-Infrastructure-Build-Out/default.aspx
28. EnkiAI summary, "Bloom Energy Fuel Cell Deals 2025, 1 GW AEP Agreement": https://enkiai.com/solid-oxide-fuel-cells/bloom-energy-data-center-projects/
29. Data Center Dynamics, "Bloom Energy signs \$5bn partnership with Brookfield": https://www.datacenterdynamics.com/en/news/bloom-energy-signs-5bn-partnership-with-brookfield-to-deploy-fuel-cell-tech-across-ai-data-centers/
30. FuelCell Energy investor release, "FuelCell Energy and Inuverse Sign MOU for Data Center Development in Korea": https://investor.fce.com/press-releases/press-release-details/2025/FuelCell-Energy-and-Inuverse-Sign-MOU-for-Data-Center-Development-in-Korea-Signaling-Growth-in-Hyperscale-and-AI-Markets/default.aspx
31. Data Center Dynamics, "Microsoft builds 3MW hydrogen fuel cell backup power plant": https://www.datacenterdynamics.com/en/news/microsoft-builds-3mw-hydrogen-fuel-cell-backup-power-plant/
32. Data Center Dynamics, "The quest to run data centers on battery power": https://www.datacenterdynamics.com/en/analysis/the-quest-to-run-data-centers-on-battery-power/
33. Energy-Storage.News, "Amazon Australia puts battery storage centre stage as it inks nine PPAs": https://www.energy-storage.news/amazon-australia-puts-battery-storage-centre-stage-as-it-inks-nine-ppas-for-data-centre-expansion/
34. Microsoft EMEA, "How Microsoft's new datacenter region in Sweden incorporates the company's sustainability commitments": https://news.microsoft.com/source/emea/features/how-microsofts-new-datacenter-region-in-sweden-incorporates-the-companys-sustainability-commitments/
35. The Bruneian, "Bridge Data Centres and EcoCeres Complete Inaugural HVO-Powered Backup Fuel Pilot for Data Centres in Asia Pacific", 12 May 2026: https://thebruneian.news/2026/05/12/bridge-data-centres-and-ecoceres-complete-inaugural-hvo-powered-backup-fuel-pilot-for-data-centres-in-asia-pacific/
36. DediRock, "HVO: A Case for Rethinking Fuel Choices in Data Center Generators": https://dedirock.com/blog/hvo-a-case-for-rethinking-fuel-choices-in-data-center-generators/
37. ACAPMA, "bp unveils biorefinery plans for Kwinana energy hub": https://acapmag.com.au/2023/02/bp-unveils-biorefinery-plans-for-kwinana-energy-hub/
38. S&P Global, "BP secures further approval for A\$580 mil Kwinana biorefinery conversion in Australia": https://www.spglobal.com/commodity-insights/en/news-research/latest-news/agriculture/103024-bp-secures-further-approval-for-a580-mil-kwinana-biorefinery-conversion-in-australia
39. MarketScreener, "Rolls-Royce: hydrogen certification for mtu 4000 series": https://www.marketscreener.com/quote/stock/ROLLS-ROYCE-HOLDINGS-PLC-4004084/news/Rolls-Royce-hydrogen-certification-for-mtu-4000-series-47363471/
40. Enchanted Rock, "Texas Data Center Surge: Fast, Flexible Power via Microgrids": https://enchantedrock.com/texas-data-center-surge-needs-a-fast-flexible-power-solution-natural-gas-microgrids-can-deliver/
41. Microgrid Knowledge, "Enchanted Rock's reciprocating engine secures CARB DG certification": https://www.microgridknowledge.com/google-news-feed/article/11427202/enchanted-rocks-reciprocating-engine-secures-carb-dg-certification
42. VoltaGrid, "VoltaGrid Orders 1.5 GW for Behind-the-Meter Power Generation from INNIO": https://voltagrid.com/voltagrid-orders1-5-gw-for-behind-the-meter-power-generation-from-innio
43. Mainspring Energy product page: https://www.mainspringenergy.com/product
44. Mainspring Energy, "Mainspring Secures \$258 Million in Financing to Scale Linear Generator Business": https://www.mainspringenergy.com/news/mainspring-secures-258-million-in-financing-to-scale-linear-generator-business-adds-energy-and-tech-leaders-to-board
45. Astute Analytica, "Global Power Rental Market Outlook 2025: AI, Trends & Regional Analysis": https://www.astuteanalytica.com/industry-report/power-rental-market
46. Smart 3rd Party / Gartner Market Guide, "Market Guide for Data Center and Network Third-Party Hardware Maintenance": https://smart3rdparty.com/wp-content/uploads/2019/11/Smart-3rd-Party-Gartner-Market-Guide.pdf
