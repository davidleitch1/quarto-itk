---
title: "Data centre backup diesel gensets: technical specs and unit economics"
author: "David Leitch"
date: 2026-05-13
draft: true
---

# Why this matters

The diesel set behind a hyperscale data centre is, for most of its life, an unloved capital asset that runs 50–100 hours a year. But the kit is unusually concentrated, expensive and increasingly capacity-constrained. Caterpillar, Cummins and Rolls-Royce Power Systems (mtu) lead the global market; lead times for 2.5–3 MW class standby sets have stretched to 18–24 months [1]; and the installed fleet of standby capacity attached to data centres globally rose from around 20 GW in 2018 to 55 GW in 2024 [2]. Virginia alone permits more than 27 GW of diesel capacity behind data centres [2].

This note builds up the engineering and the unit economics from the OEM datasheet, through the 96-hour fuel inventory required for ANSI/TIA-942 Rated-4 and NFPA 110 Level 1 design intent, up to the total backup-power capex for a 100 MW IT-load hyperscale build, and then prices the annual operating cost.

The headline result for the 100 MW worked example: the diesel backup system — sets, switchgear, paralleling controls, fuel storage, polishing and ATSs — runs to roughly US\$1.0–1.5 million per MW of IT load installed, or US\$100–150 million for the facility. That sits inside an overall hyperscale build cost of US\$10–13 million per MW IT (US\$20m+ per MW for liquid-cooled AI training) [3, 4]. Backup-power kit is therefore 8–12% of total air-cooled hyperscale capex, and a smaller share of an AI build, but it is the longest-lead and most regulated component on the site.

# 1. The reference machines

Two anchors. The Caterpillar 3516E HD is the workhorse of US hyperscale builds in the 2.5–2.75 MW class. The mtu 20V4000 sits at 2.8–3.25 MW and is the European and APAC reference. Cummins QSK60 is the third option, particularly in markets where Cummins dealer coverage is strong (parts of APAC, the Middle East and Latin America). All three are V-configuration heavy-duty diesels at 1500 rpm (50 Hz) or 1800 rpm (60 Hz).

**Table 1 — Reference standby gensets, 2.5–3 MW class**

| Parameter | Caterpillar 3516E (60 Hz) | mtu 20V4000 DS3000 | Cummins QSK60-G23 |
|:----------|--------------------------:|-------------------:|------------------:|
| Standby rating (ekW) | 2,750 | 3,000 | 2,500 |
| Standby rating (kVA) | 3,438 | 3,750 | 3,125 |
| Prime / continuous (ekW) | 2,500 | 2,500 | 2,250 |
| Engine configuration | V16, 4-stroke | V20, 4-stroke | V16, 4-stroke |
| Bore × stroke (mm) | 170 × 215 | 170 × 210 | 159 × 190 |
| Displacement (L) | 78.1 | 95.4 | 60.2 |
| Compression ratio | 14.7:1 | 15.5:1 | 14.5:1 |
| Engine speed (rpm) | 1,800 | 1,800 | 1,800 |
| Specific power (kW/L disp.) | 35.2 | 31.4 | 41.5 |
| Dry weight, set + radiator (t) | ~19.8 | ~21.5 | ~23.0 |
| Footprint L×W×H (m) | 7.5 × 2.2 × 3.4 | 7.7 × 2.3 × 3.6 | 8.0 × 2.3 × 3.7 |
| EPA standby tier | Tier 2 (stationary emergency) | Tier 2 | Tier 2 |
| Aftertreatment (Tier 2 standby) | None standard | None standard | None standard |
| Tier 4 Final option | Yes, w/ SCR + DPF + DEF | Yes, w/ SCR + DPF + DEF | Yes, w/ SCR + DPF + DEF |

*Source: Caterpillar 3516E (60 Hz) datasheet LEHE1351-09 [5]; mtu Onsite Energy 20V4000 DS3000 G04 spec [6]; Cummins QSK60-G23 standby spec sheet, 2250–2500 kVA, Rev-03, May 2023 [7]. Cummins V16 has the highest specific power but the smallest displacement; the mtu V20 has the largest swept volume but lowest BMEP, reflecting an emphasis on overhaul interval over peak rating.*

The key point: standby-rated emergency gensets in the United States operate under a regulatory exemption that lets them stay at EPA Tier 2 emissions, avoiding the cost and complexity of SCR + DPF + AdBlue/DEF aftertreatment that Tier 4 Final demands [8]. Most hyperscale builds today specify Tier 2 standby gensets where local air permits allow; Virginia data, however, suggests that more than half of newly permitted capacity is now being installed at Tier 4 standards because of local non-attainment area limits and to preserve the option of running the kit in grid services or peak shaving [2, 9]. The Tier 4 adder runs to roughly US\$100–200/kW, plus DEF storage and a substantial increase in footprint and weight.

## Fuel consumption — the Caterpillar 3516E datasheet

This is the load-curve number that matters most for sizing fuel storage and for operating-cost calculations. Caterpillar publishes the following for the 3516E at 2,750 ekW standby (60 Hz, low-fuel-consumption rating, with engine-mounted fan) [5]:

**Table 2 — Caterpillar 3516E HD fuel consumption (2,750 ekW standby, 60 Hz)**

| Load | Fuel rate (L/hr) | Fuel rate (US gph) | Specific fuel consumption (g/kWh) |
|:-----|-----------------:|-------------------:|----------------------------------:|
| 25% (687 kW) | 184.4 | 48.7 | 225 |
| 50% (1,375 kW) | 309.0 | 81.6 | 188 |
| 75% (2,063 kW) | 431.8 | 114.1 | 175 |
| 100% (2,750 kW) | 563.8 | 148.9 | 172 |

*Source: Caterpillar 3516E specification sheet LEHE1351-09 [5]. Note: the 3,000 ekW variant lifts 100% consumption to 645.8 L/hr (170.6 gph). Values are at sea level, 25 °C, ISO 3046 reference.*

The picture sharpens around 0.20 L/kWh at full load and slightly above 0.22 L/kWh at 25% — diesel becomes thermodynamically less efficient at low load, and this is the practical reason for the wet-stacking problem. The Cummins QSK60 at full standby load consumes around 535 L/hr (141 gph) for 2,500 ekW [7]; the mtu 20V4000 DS3000 sits at around 690–720 L/hr at 3,000 ekW from manufacturer data [6]. All three converge to roughly 200–215 g/kWh at full load — better-than-utility-scale diesel reciprocating performance but materially worse than CCGT.

For sizing purposes, the **rule of thumb of 0.22 L/kWh standby at full load is conservative and safe** across the three OEMs. For a 3 MW unit, that is 660 L/hr at full standby load — and that is the number I will use to size the 100 MW facility's fuel inventory below.

# 2. Fuel system for 96-hour autonomy

## The 96-hour requirement

ANSI/TIA-942-C, the data-centre infrastructure standard, sets descending fault-tolerance criteria from Rated-1 to Rated-4. Rated-4 (fault-tolerant) implicitly requires that the site survive any single failure including loss of utility power for an extended period. The standard is paywalled, but design-practice commentary consistently aligns Rated-4 with **96 hours of on-site fuel** at full critical load [10, 11].

NFPA 110, the US emergency power supply standard, expresses the same idea differently: Level 1 systems where loss of power could cause death or serious injury must be designed for 96 hours of operation, though the standard allows an authority having jurisdiction to accept a documented fuel-supply contract instead of full on-site inventory [12]. In practice, hyperscale operators don't rely on contracts during a 96-hour outage — they build the tanks.

By contrast, the Uptime Institute's Tier Standard sets only a 12-hour on-site fuel storage minimum for all Tiers including Tier IV [13]. The 96-hour number is therefore a TIA-942/NFPA design choice rather than a Tier number; most US and Australian hyperscale specifications use 72 or 96 hours.

## Tank sizing for a 3 MW set

At 660 L/hr (full standby load with margin), one 3 MW class set running for 96 hours needs:

660 L/hr × 96 hr = **63,360 L of usable fuel per genset**.

NFPA 110 requires the main fuel tank to carry 133% of the calculated requirement to allow for unusable volume, expansion ullage and pump cut-out [12]. Applied here:

63,360 × 1.33 = **~84,300 L (22,300 US gal) of nameplate tank capacity per 3 MW set**.

Most builds settle this in a two-tier architecture:

- A **belly tank or skid sub-base tank** on each genset providing 4–12 hours of run-time autonomy. Cat 3516E factory sub-base tanks are typically 7,000–12,000 L. mtu integrated tanks are typically 4,000 L at the standard package.
- A **bulk tank farm** sized for the remaining hours, feeding **day tanks** at each genset via duplex transfer pumps. Day tanks accept the engine-driven return-fuel loop and provide a thermally buffered local supply.

## Fuel polishing — the silent reliability risk

Diesel fuel begins to degrade within 28 days of delivery. Standby fuel that sits for months accumulates water (condensation, atmospheric moisture), microbial growth at the fuel/water interface, asphaltene precipitation as the fuel oxidises, and particulate sediment. The ASTM D975 specification covers grade-2 diesel quality at delivery but does not address stored-fuel ageing; that is left to ASTM D6217 (particulate), D2709 (water and sediment), D6469 (microbial) and similar [14].

Best-practice data-centre fuel-quality programs run [14, 15, 16]:

- **Monthly** visual inspections and basic water-detection on day tanks.
- **Quarterly** microbial monitoring and water-bottom sampling on bulk tanks.
- **Annual** full ASTM D975 specification testing on each tank.
- **Continuous or scheduled fuel polishing** — pump fuel through filter/water-separator/coalescer skids — typically rotating the bulk inventory every 4–8 weeks. A 1–2 m³/hr polishing skid handles a 100,000 L tank in 2–4 days; permanent skids cost US\$15,000–40,000 each; mobile services cost roughly US\$0.05–0.15 per litre per pass [16].

Annual testing and polishing service contracts run US\$875–1,475 per tank in the US per Bell Performance benchmarks [15]; a hyperscale site with 30–50 bulk and day tanks therefore spends US\$30,000–75,000 a year on testing alone, plus polishing skid capex and consumables. Across a hyperscale fleet the total fuel-quality program can run into six figures annually [16].

## Australian dangerous-goods thresholds

AS 1940:2017 — *The storage and handling of flammable and combustible liquids* — is the technical standard that state and territory dangerous-goods regulations adopt by reference. Diesel is **Class C1 combustible liquid** (flash point >60 °C and ≤93 °C, or relabelled under recent GHS revisions). The key Australian thresholds [17, 18, 19]:

**Table 3 — Australian regulatory thresholds for above-ground diesel storage**

| Threshold | Quantity (diesel, C1 combustible) | Trigger |
|:----------|----------------------------------:|:--------|
| AS 1940 "minor storage" upper limit | 10,000 L (in any one location) | Above this, full AS 1940 fire-protection, bunding, separation distance rules apply |
| High-level alarm required | 25,000 L (above-ground combustible tank) | AS 1940:2017 update |
| Placard quantity (dangerous-goods placarding) | ~10,000 L for C1 combustible; varies by jurisdiction | Notify dangerous-goods regulator; placards on tanks |
| Manifest quantity (full notification) | 100,000 L (C1 combustible, model WHS) | Manifest filed with state regulator and fire brigade |
| Major hazard facility threshold | Schedule 15 quantity tests; for C1 combustibles, generally 5,000 t (~6,000,000 L) | Triggers MHF licensing under model WHS regulations |

*Source: AS 1940:2017 [17]; Bulk Fuel Australia 2019 Guide [18]; Safe Work Australia Schedule 15 to model WHS regulations [19]; Viva Energy AS 1940 compliance guide [20].*

For a hyperscale site with 4–8 million litres of diesel on hand, the placard and manifest quantities are crossed comfortably but the major hazard facility threshold for diesel alone is not. The MHF designation typically only triggers if the site also stores significant LPG, hydrogen or other Schedule 15 chemicals, or if multiple data centres on a single site aggregate above ~6 million litres. Hyperscale operators are therefore well inside heavy dangerous-goods regulatory territory but generally below MHF — they need licensed dangerous-goods premises, full bunding to AS 1940, fire-water capacity sized to NFPA 30, hot-work permits, and full firefighter pre-incident plans, but not the full safety-case regime of an oil terminal.

## Tank cost benchmarks (Australia)

Self-bunded above-ground steel tanks dominate the Australian data-centre fuel-storage market. Pricing from suppliers like Fes Tanks, Fuelfix and Durotank, plus several private quotes for hyperscale projects, give the following indicative ranges:

- 30,000 L self-bunded tank: AU\$35,000–55,000 (~AU\$1.20–1.80 per litre)
- 68,000 L tank: AU\$70,000–95,000 (~AU\$1.10–1.40 per litre)
- 110,000 L tank: AU\$110,000–140,000 (~AU\$1.00–1.30 per litre)

Civils, foundations, bunding upgrades, fire protection, level instrumentation, transfer pumps, day tank skids, polishing skids and 2.4 km equivalent of fuel-oil pipework typically multiply the bare-tank cost by 2.5–3.5×. **All-in installed bulk fuel storage** for hyperscale builds therefore lands at roughly AU\$3–5 per litre of capacity (US\$2–3.5/L) [21]. For a 100 MW facility that is approximately US\$10–17 million on fuel storage alone before fuel inventory itself.

## Refuelling logistics

Australian fuel road tankers are typically B-double 50,000–60,000 L payload. Delivering 4 million litres into a hyperscale tank farm during a sustained outage therefore requires roughly 70–80 tanker movements. The standing rate at which a fleet of 5–8 dedicated tankers can resupply a site is around 200,000–400,000 L per day per dedicated route — meaning a fully drained 96-hour inventory takes 10–20 days to refill at a single site. In practice, hyperscale fuel-supply contracts specify a minimum response time (typically 6 hours to first delivery, with priority access during emergencies) and a dedicated routing pool [22]. The Houston flood in 2017 and the Texas grid event in 2021 both saw data centres burn through 24–48 hours of fuel before resupply caught up — leaving the 72–96 hour inventory as the relevant design margin.

# 3. Backup power system for a 100 MW Rated-4 facility

## Load to back up

A modern air-cooled hyperscale facility carries an IT load with PUE around 1.3–1.4. For a 100 MW IT design:

- IT load: 100 MW
- Cooling, lighting, controls, transformers: 30–40 MW
- **Total backed-up load: ~130 MW**

Liquid-cooled AI training builds achieve PUE 1.1–1.2 and back up roughly 110–120 MW for the same IT load; below I take the 130 MW number as the binding case.

## Generator count and architecture

2N is the binding redundancy choice for Rated-4. Two completely independent A-side and B-side gen-busses, each fully capable of carrying 130 MW. The standard architecture uses standby-rated 2.5–3 MW sets paralleled on a common medium-voltage bus per side.

Taking 2.75 MW per genset (Cat 3516E mission-critical rating) [5]:

- N per side: 130 / 2.75 = 48 sets (rounding up)
- With N+1 redundancy on each side: 49 sets per side
- **Total facility genset count: 98 sets**, total nameplate 270 MW
- Many designs simplify to 50 sets per side at 2.75 MW = 100 sets, 275 MW nameplate

Alternative architectures use larger 4 MW class sets (Caterpillar C175-20 or mtu 20V4000 DS4000) to reduce set count, switchgear complexity and footprint. A 4 MW per set 2N+1 design lands at roughly 34 sets per side (68 sets total, 272 MW nameplate). Hyperscale operators have moved toward larger 3–4 MW sets in the past five years for exactly this reason.

## Switchgear and paralleling

Each side of a 2N system needs medium-voltage paralleling switchgear capable of synchronising 30–50 sets to a common bus, plus generator breakers, bus-tie breakers, ATSs, distribution switchgear and protective relays. Indicative pricing from contractor quotes and industry benchmarks [1, 23]:

- Generator breakers and metering per set: US\$60,000–120,000
- Medium-voltage paralleling switchgear (per side, 50–60 MW bus): US\$3–8 million
- Automatic transfer switches (one per critical load block, typically 16–32 ATSs per side): US\$3–8 million total
- Paralleling control system (PLC, EMCP, synchroniser, load-share controls): US\$1.5–3 million

A complete 100 MW IT facility therefore lands at roughly **US\$25–45 million on switchgear and controls alone**.

## Fuel inventory

At 660 L/hr per 3 MW set running at full load, all 50 paralleled sets on one side at full load burn:

50 × 660 L/hr = 33,000 L/hr → 33 m³/hr → **3,168 m³ over 96 hours = ~3.17 million litres per side**.

A 2N design must store enough fuel for the binding scenario. The common interpretation is to size for one side at full load for 96 hours (because if the utility fails, one side is enough to carry the IT load — the other is parallel insurance). Some operators are more conservative and size each side independently for 96 hours.

**Practical specification: 4 million litres of total bulk fuel storage**, distributed across 30–50 tanks ranging 50,000–150,000 L each, with day tanks at each genset (typically 2,500–5,000 L) totalling another 200,000 L of distributed inventory. A handful of operators specify 6 million litres for genuine 2N × 96-hour redundancy.

## Capex build-up — 100 MW IT, Rated-4, air-cooled

**Table 4 — Backup power system capex, 100 MW IT facility (Rated-4, 2N)**

| Component | Quantity | Unit cost (US\$) | Total (US\$ million) |
|:----------|---------:|-----------------:|---------------------:|
| Gensets (2.75 MW, Tier 2, sound enclosure, sub-base tank) | 100 | 1.0–1.4 m each | 100–140 |
| Medium-voltage switchgear, paralleling | 2 sides | 5–8 m per side | 10–16 |
| Automatic transfer switches and distribution | ~40 ATSs | 150–250 k each | 6–10 |
| Paralleling controls, EMCP, synchronisers | facility | 2–4 m | 2–4 |
| Bulk fuel tanks (4 ML capacity, self-bunded steel) | 30–40 tanks | 2.5–3.5 \$/L installed | 10–14 |
| Day tanks, transfer pumps, fuel polishing | facility | 2–4 m | 2–4 |
| Fuel-oil piping, valves, leak detection | facility | 2–4 m | 2–4 |
| Civils, foundations, enclosures, exhaust stacks | facility | 8–14 m | 8–14 |
| Engineering, commissioning, witness testing | facility | 5–10% of above | 7–14 |
| **Total backup power system** | | | **147–220** |
| **Per MW IT (US\$M/MW)** | | | **1.5–2.2** |

*Source: Author build-up using OEM list prices [1, 5, 6, 7], Cushman & Wakefield Data Center Development Cost Guide 2025 commentary [3], Generator Source benchmarks [23] and Australian self-bunded tank pricing [21].*

The Cushman & Wakefield 2025 guide notes that generator capital costs alone rose 45% from Q3 2021 to mid-2024, and that data-centre electrical equipment costs across all categories (transformers +44%, UPS +48%, switchgear +31%) have all moved in lockstep [3]. The build-up above reflects 2025 pricing; pre-Covid pricing for the same system would have been roughly 30–35% lower in nominal terms.

**The gensets themselves are 65–70% of the backup-power system cost.** Switchgear and paralleling are 10–15%. Fuel storage and distribution is 12–15%. Civils, engineering and commissioning soak up the balance.

# 4. Operating costs

## Routine maintenance

Standby gensets at hyperscale data centres run a heavily proceduralised maintenance cycle [24, 25]:

- **Monthly:** No-load black-start test, visual inspection, battery and charger check, day-tank water draining, control-system function check.
- **Quarterly:** Load-bank test at minimum 30% load for 30 minutes (NFPA 110 wet-stacking prevention), oil and fuel sample analysis, fuel polishing if needed.
- **Annual:** Stepped 2-hour load-bank test (30% → 50% → 75% for 30/30/60 minutes), oil and filter change, coolant test/change, air filter change, complete control-system inspection, fuel polishing all bulk tanks.
- **Top-end overhaul at 12,000–18,000 hours** (often never reached on a true standby genset that runs <100 hr/yr — would take 120+ years), or by calendar at 10–15 years for valve adjustment and injector replacement.
- **Major overhaul at 36,000–60,000 hours** — almost never reached on pure standby duty.

## Annual cost per MW

Building it up [24, 25, 26, 16]:

**Table 5 — Annual operating cost per MW IT, backup power system (100 MW Rated-4 facility)**

| Cost item | US\$/year (100 MW IT) | US\$/MW IT/yr |
|:----------|---------------------:|--------------:|
| Routine maintenance (monthly + quarterly + annual PMs, parts) | 1,200,000 | 12,000 |
| Annual stepped load-bank testing (rented load banks, labour) | 250,000 | 2,500 |
| Diesel consumed in load-bank tests (estimate 50 hr × 660 L/hr × 100 sets × AU\$1.50/L) | 500,000 | 5,000 |
| Fuel polishing and quality testing | 200,000 | 2,000 |
| Fuel inventory turnover (every 18–24 months, ~AU\$0.30/L loss to mixing, blending, replacement) | 600,000 | 6,000 |
| Lube oil, coolant, filters | 200,000 | 2,000 |
| Major service contract (OEM, 24/7 response) | 1,500,000 | 15,000 |
| Insurance, dangerous-goods compliance, spill response | 400,000 | 4,000 |
| Operator labour allocation (DC ops team prorata) | 800,000 | 8,000 |
| **Total annual opex, backup power** | **5,650,000** | **56,500** |
| As % of installed capex | ~3.4% | |

*Source: Author build-up. Routine maintenance benchmarks from Cummins data-centre genset specification guide [24] and Caterpillar service literature [25]. Fuel polishing pricing from Bell Performance [15] and Mojo Fuel [16]. Diesel pricing per Australian Institute of Petroleum terminal-gate data [27].*

Two observations. First, **the working-capital cost of holding 4 million litres of diesel** is itself material. At AU\$1.80/L wholesale (close to the May 2026 terminal-gate price [27]), the fuel inventory alone represents AU\$7.2 million of working capital, or roughly AU\$430,000/year at a 6% pre-tax cost of funds — not large, but real. Second, **fuel inventory turnover is a substantive cost**: standby fuel cannot sit for ever. Operators rotate inventory every 18–24 months, either by burning it in extended load-bank tests, blending into commercial diesel supply, or paying for tanker removal and replacement. Each tank-flush event costs around AU\$0.20–0.40/L of capacity.

Diesel consumed during the quarterly load-bank tests is the largest single fuel cost. A typical site burns approximately 50 hours × 660 L/hr × 50 sets per year on testing = 1.65 million litres, costing AU\$2.5–3 million in fuel alone at 2026 prices.

# 5. Backup power as a fraction of total hyperscale capex

## Total hyperscale capex per MW IT

Multiple independent benchmarks converge on US\$10–13 million per MW IT for a current-generation air-cooled hyperscale build [3, 4, 28, 29]:

- JLL Global Data Center Outlook 2026: US\$11.3 million per MW projected average, up from US\$10.7m in 2025 and US\$7.7m in 2020 [4]
- Turner & Townsend Data Centre Construction Cost Index 2025: Tokyo US\$15.2/W, Singapore US\$14.5/W, Zurich US\$14.2/W, Dublin/Madrid US\$10.0/W [29]
- Cushman & Wakefield 2025 Cost Guide: US Tier-1 markets US\$10–13M/MW IT for air-cooled hyperscale [3]
- AI/liquid-cooled builds: US\$20–25M/MW IT for facility only; US\$30–40M/MW including GPU fit-out [4, 28]

**Anchor: US\$11M/MW IT for an air-cooled hyperscale build; US\$22M/MW IT for AI-optimised.**

## Capex breakdown

Drawing on the Cushman & Wakefield 2025 guide, JLL 2026 and Alpha Matica deconstruction [3, 4, 28, 30]:

**Table 6 — Capex breakdown, 100 MW IT hyperscale (US\$11M/MW IT baseline)**

| Category | Share of total | US\$M for 100 MW IT | US\$M/MW IT |
|:---------|---------------:|--------------------:|------------:|
| Building shell and core | 10–15% | 110–165 | 1.1–1.6 |
| Land and site works | 4–7% | 44–77 | 0.4–0.8 |
| Mechanical / cooling | 15–20% | 165–220 | 1.6–2.2 |
| Electrical distribution, transformers, MV gear | 15–20% | 165–220 | 1.6–2.2 |
| UPS systems (with batteries) | 8–12% | 88–132 | 0.9–1.3 |
| **Backup power (generators + switchgear + fuel)** | **8–12%** | **88–132** | **0.9–1.3** |
| Fire suppression, security, BMS | 2–4% | 22–44 | 0.2–0.4 |
| Interior fit-out, white space | 10–15% | 110–165 | 1.1–1.6 |
| Engineering, commissioning, contingency | 8–12% | 88–132 | 0.9–1.3 |
| **Total** | 100% | 1,100 | 11.0 |

*Source: Cushman & Wakefield Data Center Development Cost Guide 2025 [3]; JLL 2026 Global Data Center Outlook [4]; Alpha Matica deconstruction [28]; author build-up for backup-power line item from Table 4.*

The backup-power slice — 8–12% of facility capex, roughly US\$1.0–1.3 million per MW IT — is the third or fourth largest line item, behind shell, cooling and primary electrical distribution. It is roughly the same size as the UPS-and-battery system. Both are typically built and operated by the same electrical contractor pool, and both have suffered similar 40–50% price rises since 2021 because of identical demand-side pressure on switchgear, transformer and large-format battery supply chains [3].

For an AI-optimised liquid-cooled build at US\$22M/MW IT, the backup-power slice is smaller proportionally (4–6%) because cooling and primary electrical kit scale faster. But the absolute size — US\$1.0–1.5M/MW — is roughly the same, because what is backed up is roughly the same number of joules.

## How the backup-power slice compares

To anchor: a 100 MW IT facility's backup-power system, at US\$1.0–1.5M/MW IT installed, is in the same range as:

- A modern combined-cycle gas turbine plant (US\$1.0–1.5M/MW installed), although a GT delivers continuous power and the genset delivers standby insurance.
- The site's primary HV transformer and switchyard (typically US\$0.8–1.2M/MW for a 132/33 kV connection).
- The cost of three large lithium-iron-phosphate utility batteries that could in principle replace 5–10 minutes of UPS function but not 96 hours.

The reason hyperscalers continue to pay this premium is straightforward: diesel is the only practical technology that delivers 96 hours of guaranteed energy storage at the densities — 35–40 MJ/kg — that a 130 MW load demands. A lithium battery alternative for the same energy stored (130 MW × 96 hr = 12,480 MWh) would cost roughly US\$3.5–5 billion at current battery prices, before any consideration of cycling life, footprint or fire risk. The diesel set is, in this narrow sense, irreplaceable.

# 6. Implications for entry

For an analyst evaluating the diesel-backup-services market the relevant takeaways:

1. **The kit market is concentrated.** Caterpillar, mtu (Rolls-Royce Power Systems) and Cummins together hold roughly 80% of the >1 MW data-centre standby market globally. Generac is pushing aggressively into the 2.25–3.25 MW range [1] and Kohler/Rehlko are credible challengers. Entry as an OEM is implausible.

2. **The integration and service market is fragmented.** A single hyperscale build with 100 sets needs dozens of skids, hundreds of valves, kilometres of fuel-oil pipework, paralleling switchgear, ATSs and a 30–50 tank fuel farm. Generator-package integrators, fuel-system specialists, switchgear builders, polishing-service operators and tank fabricators all compete for fragmented slices. This is where service revenue and capital-light entry sit.

3. **The opex line is small but sticky.** US\$50,000–75,000 per MW IT per year, across a 55 GW global standby fleet, is a US\$3–4 billion service-and-fuel market — and growing at 15–20% as the installed base catches up with the build pipeline. Australian hyperscale opex spends are 10–15% above US benchmarks because of higher labour rates and dangerous-goods compliance loads.

4. **Lead times are the binding constraint.** 18–24 months for a new 3 MW set from order to delivery [1] means that secondhand and refurbished diesel sets are now trading above replacement cost in some markets. Hyperscale buyers will lock in 3–5 year framework supply agreements with Caterpillar and Cummins; the spot market is for the merchant DC operator.

5. **Tier 4 transition is the regulatory tail risk.** Today, the standby exemption keeps emergency gensets at Tier 2 [8]. Two threats to this: tightening of state-level non-attainment area air permits (already happening in California, Virginia, Texas) and re-classification if the genset participates in demand-response or peak-shaving markets [9]. A Tier-4 retrofit costs roughly US\$200/kW and adds DEF storage, weight and footprint.

6. **The 96-hour fuel inventory is not optional and not cheap.** A 100 MW facility holds roughly 4 million litres of diesel — about the same physical inventory as a regional fuel terminal. The dangerous-goods, fire-protection and refuelling-logistics envelope around that inventory is a meaningful operational discipline and a credible barrier to entry for second-tier operators.

# References

[1] [Kairui Power, "Generator Price Trends 2025–2030: Plan Smarter for Data Centers"](https://www.kairuipower.com/blog/generator-price-trends-implications-for-data-center-and-power-plant-planning), 2025.

[2] [Latitude Media, "The data center boom is a diesel generator boom"](https://www.latitudemedia.com/news/the-data-center-boom-is-a-diesel-generator-boom/), 2025.

[3] [Cushman & Wakefield, US Data Center Development Cost Guide 2025](https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide).

[4] [JLL, 2026 Global Data Center Outlook](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook).

[5] [Caterpillar 3516E (60 Hz) 2500–2750 kW Diesel Generator product page](https://www.cat.com/en_US/products/new/power-systems/electric-power/diesel-generator-sets/1000033111.html), specification sheet LEHE1351-09 referenced via Western States Cat and Cleveland Brothers dealer pages.

[6] [mtu Onsite Energy 20V4000 DS3000 60 Hz spec sheet](https://www.mtu-solutions.com/content/dam/mtu/products/power-generation/powergeneration-product-list-latest/231219_PG_Spec_20V4000DS3000G04_3000kW_3D_FC_60Hz_45C.pdf); supplementary [Curtis Power Solutions 60 Hz MTU 4000 series listings](https://www.curtispowersolutions.com/specs-mtu-4000-gensets).

[7] [Cummins QSK60 Series 2250–2500 kVA Standby spec sheet, Rev-03, May 2023](https://www.cummins.com/sites/default/files/2023-05/2250-2500kVA-QSK60_Rev-03.pdf).

[8] [Generator Source, "The Facility Manager's Guide to EPA Tier 4 Final vs. Tier 2/3 Standby"](https://generatorsource.com/fuel/diesel/the-facility-managers-guide-to-epa-tier-4-final-vs-tier-2-3-standby/).

[9] [Power Generation Enterprises, "Tier 4 Generator Requirements: Compliance Guide 2026"](https://powergenenterprises.com/tier-4-generator-requirements-compliance-guide-2026).

[10] [TIA Online, "ANSI/TIA-942 Standard"](https://tiaonline.org/products-and-services/tia942certification/ansi-tia-942-standard/).

[11] [Score Group, "Data Center Standards (ISO, ANSI/TIA-942 and Tiers) in 2026"](https://www.score-grp.com/en/post/data-center-standards-iso-ansi-tia-942-and-tiers-in-2026-how-to-design-classify-and-operate-re).

[12] [CK Power, "No-Nonsense Guide to NFPA 110 Compliance for Emergency Power Systems"](https://ckpower.com/wp-content/uploads/2018/04/NFPA-110-Final.pdf); also [Curtis Power Solutions "NFPA 110 Emergency Power Supply"](https://www.curtispowersolutions.com/nfpa-110-emergency-power-supply-eps).

[13] [Uptime Institute Journal, "Fuel system design and reliability"](https://journal.uptimeinstitute.com/fuel-system-design-reliability/).

[14] [FuelCare USA, "ASTM D975 Diesel Fuel Testing Guide"](https://fuelcareusa.com/critical-facilities-power-resilience/astm-d975-diesel-fuel-testing-guide/).

[15] [Bell Performance, "Data Center Generator Fuel Quality: Complete Guide"](https://www.bellperformance.com/bell-performs-blog/data-center-generator-fuel-quality-the-complete-guide-to-preventing-backup-power-failures).

[16] [Mojo Fuel Optimization, Commercial & Industrial Fuel Polishing service pricing](https://mojo-fuel.com/commercial-and-industrial); [Precision Filtration "How Fuel Polishing Prevents Data Center Downtime"](https://precisionfiltration.com/blog/how-fuel-polishing-prevents-data-center-downtime/).

[17] [Fes Tanks summary of AS 1940:2017 changes](https://www.festanks.com.au/blog/as1940-2017-storage-handling-flammable-combustible-liquids/).

[18] [Bulk Fuel Australia, "A guide to flammable and combustible liquids (2019 Edition)"](https://bulkfuel.com.au/index.php?id=106%3Aa-guide-to-flammable-and-combustible-liquids-part-one).

[19] [Safe Work Australia, model WHS Regulations Schedule 15 — Hazardous chemicals at major hazard facilities](https://classic.austlii.edu.au/au//legis/cth/consol_reg/whasr2011327/sch15.html); [Safe Work Australia, Major Hazard Facilities Notification and Determination Guide, 2012](https://www.safeworkaustralia.gov.au/system/files/documents/1702/notification_and_determination.pdf).

[20] [Viva Energy, "Complying with AS1940 — the safe storage and handling of fuel"](https://www.vivaenergy.com.au/blog/innovation/complying-with-as1940-the-safe-storage-and-handling-of-fuel).

[21] [Fes Tanks](https://www.festanks.com.au/grande-tanks/68000l-aboveground-fuel-tank/), [Fuelfix](https://www.fuelfix.com.au/product/30000l-self-bunded-fuel-tank/), [Durotank](https://durotank.com.au/product-category/self-bunded-fuel-tanks/), [Fuel Equipment Specialists](https://www.fuelequipmentspecialists.com.au/p/110-000-litre-self-bunded-tank) — Australian self-bunded tank pricing 2024–2026.

[22] [Earthsafe, "The New Logistics of Data Center Fuel Supply"](https://www.earthsafe.com/the-new-logistics-of-data-center-fuel-supply); [Mansfield Energy, "Powering Data Centers: The Ultimate Guide to a Fail-Safe Fueling Program"](https://mansfield.energy/2025/01/30/powering-data-centers-the-ultimate-guide-to-a-fail-safe-fueling-program/).

[23] [Generator Source, "Backup Power for Data Centers"](https://generatorsource.com/backup-power/backup-power-for-data-centers/); [Constructandcommission "Data Center Redundancy: N, N+1, N+2, 2N & 2N+1 Explained"](https://constructandcommission.com/data-center-redundancy-n-n1-n2-2n-2n1-2n1-explained/).

[24] [Cummins, "Specifying Standby Generator Set Requirements for Data Centers"](https://www.cummins.com/sites/default/files/2023-04/Specifying%20Standby%20Generator%20Set%20Requirements%20for%20Data%20Centers%202022-08-10.pdf).

[25] [Central States Diesel Generators, "Guide to Data Center Generator Maintenance"](https://csdieselgenerators.com/guide-to-data-center-generator-maintenance/); [Central States Diesel Generators, "NFPA 110 Generator Maintenance Requirements Simplified for 2025"](https://csdieselgenerators.com/nfpa-110-generator-maintenance-requirements-simplified-for-2025/).

[26] [Avtron Power Solutions, "How can load bank testing your genset reduce the cost of ownership?"](https://avtronpower.com/resources/articles/how-can-load-bank-testing-your-genset-reduce-the-cost-of-ownership/).

[27] [Australian Institute of Petroleum, Terminal Gate Prices](https://www.aip.com.au/pricing/terminal-gate-prices); [ACCC Weekly fuel price monitoring update 2 April 2026](https://www.accc.gov.au/system/files/weekly-fuel-price-monitoring-report-2-april-2026.pdf).

[28] [Alpha Matica, "Deconstructing the Data Center: A Look at the Cost Structure Igniting the AI Boom"](https://www.alpha-matica.com/post/deconstructing-the-data-center-a-look-at-the-cost-structure-1).

[29] [Turner & Townsend, Data Centre Construction Cost Index 2025-2026](https://www.turnerandtownsend.com/insights/data-centre-construction-cost-index-2025-2026/); [report site 2025](https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/).

[30] [IoT Analytics, "Data Center infrastructure market: AI-driven CapEx pushing IT and facility equipment spending toward \$1 trillion by 2030"](https://iot-analytics.com/data-center-infrastructure-market/).
