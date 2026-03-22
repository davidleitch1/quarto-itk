---
title: "Diesel Vehicle Economics: Consumption, Costs, and Electrification"
date: 2026-03-21
draft: true
bibliography: diesel_electrification_references.bib
---

# Diesel Vehicle Economics by Sub-Sector

This document estimates diesel fuel consumption per km, annual kilometres, and the electricity equivalent for each vehicle sub-sector. The purpose is to establish the underlying economics that determine which diesel segments are most amenable to electrification.

## Methodology

For each vehicle class we estimate:

1. **Diesel consumption** (L/100km) — real-world fleet averages, not manufacturer claims
2. **Annual kilometres** — from ABS Survey of Motor Vehicle Use (Cat. 9208.0, June 2020)
3. **Electric equivalent** (kWh/100km) — from OEM specifications and fleet operator data
4. **Diesel-to-electricity ratio** — empirical kWh of electricity per litre of diesel displaced
5. **Operating cost comparison** — diesel \$/km vs electric \$/km at current Australian prices

### Key price assumptions

| Input | Value | Source |
|-------|------:|--------|
| Retail diesel | \$1.80/L | Australian avg, early 2026 |
| Fleet/bulk diesel | \$1.65/L | Typical fleet discount 8-10% |
| Depot charging (commercial) | \$0.25–0.30/kWh | Commercial electricity rates |
| DC fast charging (public) | \$0.55–0.80/kWh | Various networks |

**Note on diesel prices:** Fleet operators purchasing in bulk typically pay 8–10% below retail pump prices. We use \$1.65/L for fleet calculations and \$1.80/L for retail (owner-operator) calculations.

### The diesel-to-electricity conversion

Diesel fuel contains 10.7 kWh of chemical energy per litre. A diesel engine converts roughly 35–40% of this to useful work at the wheels; an electric drivetrain converts roughly 85–90%. The theoretical electricity required to displace one litre of diesel is therefore:

$$\frac{10.7 \times 0.38}{0.88} \approx 4.6 \text{ kWh/L}$$

In practice, the empirical ratio observed in real-world fleet data is lower — typically **2–4 kWh of electricity per litre of diesel displaced** — because electric vehicles benefit from regenerative braking, no idling losses, and more efficient auxiliary systems. The ratio varies by vehicle class and duty cycle.

---

## 1. Articulated Trucks >40t (B-doubles, road trains)

**Diesel budget share:** ~8.7 BL/yr (largest single segment)

### Diesel consumption

| Configuration | L/100km | Source |
|--------------|--------:|--------|
| Semi-trailer (6 axle) | 33–34 | H2-Hybrid Australia, ATAP |
| B-double (9 axle) | 41–42 | ATAP Appendix E (free-flow rural) |
| B-triple (road train) | 50 | H2-Hybrid Australia |
| A-triple | 59 | H2-Hybrid Australia |
| **Fleet average (all artics)** | **53.1** | ABS SMVU 2020 |

The gap between the B-double model estimate (41–42 L/100km) and the fleet average (53.1 L/100km) reflects real-world conditions: varying loads, terrain, traffic, and the inclusion of heavier configurations (B-triples, road trains) in the fleet average.

### Annual kilometres

Articulated trucks: **78,300 km/year** (ABS SMVU 2020). This is the highest of any vehicle class, reflecting their long-haul role. Trucksales.com.au cites 79,400 km/year from the same dataset.

### Electric equivalent

| Vehicle | kWh/100km | Payload | Range | Source |
|---------|----------:|--------:|------:|--------|
| Mercedes eActros 600 | 96–120 | 22 t | 500 km | Vandijck real-world test |
| Volvo FH Electric | ~110 | 20 t | 300 km | Volvo specifications |
| Tesla Semi | 96–108 | 37 t (US) | 500+ mi | CARB testing; PepsiCo fleet data |
| Windrose E1400 | ~150 (est.) | 68 t GCW | 400 km | Windrose preliminary specs |

**Implied ratio:** Taking a B-double at 42 L/100km diesel and an eActros 600 at 110 kWh/100km:

$$\frac{110}{42} = 2.6 \text{ kWh per litre diesel displaced}$$

### Operating cost calculation

For a **semi-trailer at 35 L/100km** (lighter end of artic spectrum):

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 35 L/100km | 110 kWh/100km |
| Unit cost | \$1.65/L | \$0.28/kWh |
| **Cost per km** | **\$0.58/km** | **\$0.31/km** |
| Annual fuel cost (78k km) | \$45,000 | \$24,000 |
| **Annual saving** | | **\$21,000** |

For a **B-double at 42 L/100km** (user's article data [@leitch-longhaul-2025]):

| | Diesel | Electric |
|---|------:|--------:|
| Cost per km | \$1.03/km | \$0.30/km |
| Annual fuel cost (100k km) | \$103,000 | \$30,000 |
| **Annual saving** | | **\$73,000** |
| Capital premium | | ~\$250,000 |
| **Simple payback** | | **~3.4 years** |

**Verdict:** Excellent economics. The fuel cost saving alone drives payback in 2–4 years. As the user's article puts it: "an absolute no brainer" [@leitch-longhaul-2025].

### Vehicle availability

Excellent for semi-trailers up to ~44t GCW. The eActros 600, Volvo FH Electric, and Scania R 450e are all in production. **Gap:** no electric B-double or road train exists in production — only the Windrose E1400 targets 68t GCW, and it is pre-production.

---

## 2. Articulated Trucks 30–40t (lighter semi-trailers)

### Diesel consumption

Lighter articulated trucks with 4–5 axles: **27–30 L/100km** (H2-Hybrid Australia, ATAP). These are typically distribution-focused semi-trailers operating shorter routes.

### Annual kilometres

The ABS SMVU groups all articulated trucks together at 78,300 km/year. Lighter artics likely average somewhat less — estimated **50,000–65,000 km/year** based on their shorter distribution routes.

### Electric equivalent

The same vehicles (eActros 600, Volvo FH) serve this segment. At lighter loads, consumption drops:

| Scenario | kWh/100km (est.) |
|----------|--------:|
| Light artic, distribution | 85–100 |

**Implied ratio:** 28 L/100km diesel, 90 kWh/100km electric → **3.2 kWh/L**

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 28 L/100km | 90 kWh/100km |
| Unit cost | \$1.65/L | \$0.28/kWh |
| **Cost per km** | **\$0.46/km** | **\$0.25/km** |
| Annual saving (60k km) | | **\$12,600** |

**Verdict:** Good economics. Lower annual km reduces absolute savings, but the cost-per-km advantage is clear.

---

## 3. Rigid Trucks >20t GVM

### Diesel consumption

Heavy rigids (3+ axle, >20t GVM) are used for construction, waste collection, and short-haul freight. Fuel consumption varies widely:

| Application | L/100km |
|------------|--------:|
| Heavy rigid (3 axle, highway) | 25–30 |
| Tipper/concrete agitator (urban) | 35–45 |
| **Typical estimate** | **30–35** |

Sources: ATAP vehicle operating cost models; NTC Heavy Vehicle Operating Cost Model; fleet operator reports.

### Annual kilometres

Rigid trucks: **21,100 km/year** (ABS SMVU 2020). Heavy rigids likely average 25,000–30,000 km/year (more than the fleet average which includes small rigids).

### Electric equivalent

| Vehicle | kWh/100km | GVM | Range | Source |
|---------|----------:|----:|------:|--------|
| Volvo FE Electric (27t) | 100–130 | 27t | 200 km | Volvo fleet data |
| Volvo FM Electric | 110–140 | 44t | 300 km | Volvo specifications |
| eActros 300 (now superseded) | 120–150 | 27t | 300 km | Mercedes data |

**Implied ratio:** 32 L/100km diesel, 120 kWh/100km electric → **3.75 kWh/L**

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 32 L/100km | 120 kWh/100km |
| Unit cost | \$1.65/L | \$0.28/kWh |
| **Cost per km** | **\$0.53/km** | **\$0.34/km** |
| Annual saving (25k km) | | **\$4,800** |

**Verdict:** Moderate economics. The fuel saving is clear per-km but low annual km limits the absolute saving. Better suited to high-utilisation fleets (waste, concrete) that operate return-to-base cycles compatible with depot charging.

---

## 4. Rigid Trucks 8–20t GVM

### Diesel consumption

Medium rigids are the workhorse of urban delivery — furniture, beverages, parcels. This is the segment where electric trucks first became commercially viable.

| Application | L/100km |
|------------|--------:|
| Medium rigid (2 axle, urban) | 20–25 |
| Medium rigid (suburban delivery) | 18–22 |
| **Typical estimate** | **20–25** |

Source: The Conversation (Mar 2026) cites 35 L/100km for a "medium-duty truck" but this appears to be at the heavy end of the range or inclusive of larger rigids. Fleet data from Designwerk (Swiss operator) shows 95–148 kWh/100km for electric equivalents, suggesting diesel benchmarks of 25–40 L/100km.

### Annual kilometres

Estimated **20,000–25,000 km/year** (within the rigid truck average of 21,100 km/year from ABS SMVU).

### Electric equivalent

| Vehicle | kWh/100km | GVM | Range | Source |
|---------|----------:|----:|------:|--------|
| Fuso eCanter (2nd gen) | 59–83 | 4.5–8.5t | up to 300 km | Fuso specs (82.8 kWh battery) |
| Volvo FE Electric (16t) | 95–120 | 16t | 200 km | Volvo fleet data |
| Designwerk fleet average | 95–148 | varies | varies | Swiss fleet telemetry |
| JAC N-series electric | 80–120 | 8–14t | 200+ km | JAC Australia |

**Implied ratio:** 22 L/100km diesel, 100 kWh/100km electric → **4.5 kWh/L** (this is the highest ratio, reflecting urban stop-start where regenerative braking has maximum benefit)

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 22 L/100km | 100 kWh/100km |
| Unit cost | \$1.65/L | \$0.28/kWh |
| **Cost per km** | **\$0.36/km** | **\$0.28/km** |
| Annual saving (22k km) | | **\$1,800** |

**Verdict:** Marginal on fuel savings alone for low-km operators, but these vehicles operate return-to-base cycles ideal for depot charging. Maintenance savings (fewer brake replacements, no DPF regeneration) add approximately \$0.05–0.08/km, improving the case substantially. Fleet operators like DHL, DB Schenker, and Australia Post have found the TCO case compelling at scale.

---

## 5. Rigid Trucks ≤8t GVM (Light rigids / cab-over)

### Diesel consumption

Small rigids overlap with large vans. Used for last-mile delivery, tradesperson applications.

| Application | L/100km |
|------------|--------:|
| Small rigid (urban delivery) | 15–20 |
| Cab-over (furniture, parcels) | 12–18 |
| **Typical estimate** | **15–18** |

### Annual kilometres

Estimated **15,000–20,000 km/year** based on ABS SMVU rigid average adjusted for lighter duty cycles.

### Electric equivalent

| Vehicle | kWh/100km | GVM | Range | Source |
|---------|----------:|----:|------:|--------|
| Fuso eCanter (4.5t) | 45–60 | 4.5t | 200+ km | Fuso specs |
| SEA Electric (various) | 50–80 | 4.5–8.5t | 150–250 km | SEA Electric |

**Implied ratio:** 16 L/100km diesel, 55 kWh/100km electric → **3.4 kWh/L**

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 16 L/100km | 55 kWh/100km |
| Unit cost | \$1.65/L | \$0.28/kWh |
| **Cost per km** | **\$0.26/km** | **\$0.15/km** |
| Annual saving (18k km) | | **\$2,000** |

**Verdict:** Moderate economics. The Fuso eCanter 2nd gen (from 4.5t GVM, car-licence driveable) is available and practical for urban delivery. Return-to-base depot charging is straightforward. 14 models in the eCanter range give good coverage.

---

## 6. Buses

**Diesel budget share:** ~1.5 BL/yr (all buses)

### Diesel consumption

Bus fuel consumption varies enormously by type:

| Type | L/100km | Source |
|------|--------:|--------|
| Standard metro (12m) | 40–50 | Sustainable Bus, fleet data |
| Articulated metro (18m) | 55–70 | European fleet data |
| Coach (long distance) | 20–25 | Lower due to highway operation |
| Minibus | 15–20 | Smaller size |
| **Typical metro bus** | **40–45** | Australian transit fleets |

### Annual kilometres

Buses: **24,600 km/year** (ABS SMVU 2020). Metro buses in service typically run **60,000–80,000 km/year** — the lower ABS average includes school buses and chartered coaches with lower utilisation.

### Electric equivalent

| Vehicle | kWh/km | Battery | Range | Source |
|---------|-------:|--------:|------:|--------|
| BYD K9 (12m) | 1.0 | 324 kWh | 250+ km | Santiago fleet data |
| Yutong E12 (12m) | 0.8–1.1 | 281 kWh | 250 km | Australian fleet operators |
| Ebusco 2.2 (12m) | 0.8–1.0 | 350 kWh | 300+ km | Ebusco specification |
| **Typical metro bus** | **0.9–1.2** | | | Range depends on climate |

**Note:** Seasonal variation is significant. In Australian conditions (mild winters, hot summers with A/C), typical consumption is 0.9–1.2 kWh/km. European winter data (heating loads) can reach 2.0+ kWh/km.

**Implied ratio:** 42 L/100km diesel, 100 kWh/100km electric → **2.4 kWh/L**

### Operating cost

For a **metro bus at 60,000 km/year**:

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 42 L/100km | 100 kWh/100km (1.0 kWh/km) |
| Unit cost | \$1.65/L | \$0.25/kWh (depot, off-peak) |
| **Cost per km** | **\$0.69/km** | **\$0.25/km** |
| Annual fuel cost | \$41,600 | \$15,000 |
| **Annual saving** | | **\$26,600** |

**Verdict:** Excellent economics. Buses are perhaps the strongest electrification case of all: high utilisation, fixed routes, return-to-base operation (depot charging), and large fuel consumption. Every state transit authority in Australia is now ordering electric buses. Electric buses currently cost \$700–900k vs \$400–500k for diesel equivalents — a premium of ~\$300–400k — but this is recovered in fuel and maintenance savings within 5–7 years given the high utilisation rates, with a 15–20 year asset life. Government procurement mandates are accelerating the transition; NSW, Victoria, and Queensland all have zero-emission bus targets.

---

## 7. Utes (Light commercial, ≤3.5t GVM)

**Diesel budget share:** ~3.2 BL/yr

### Diesel consumption

| Vehicle | L/100km (real world) | Source |
|---------|---------------------:|--------|
| Toyota HiLux diesel | 8–10 | Owner reports, CarsGuide |
| Ford Ranger diesel | 8–10 | Owner reports |
| Isuzu D-Max diesel | 7–9 | CarsGuide |
| **Typical diesel ute** | **8.5–10** | |

### Annual kilometres

Light commercial vehicles: **15,300 km/year** (ABS SMVU 2020). Utes used for trade work likely average higher — estimated **18,000–22,000 km/year**.

### Electric equivalent

| Vehicle | kWh/100km | Battery | Range (WLTP) | Price (AUD) | Source |
|---------|----------:|--------:|-------------:|------------:|--------|
| LDV eT60 | ~27 | 88.6 kWh | 330 km | \$92,990 | LDV Australia |
| KGM Musso EV (FWD) | ~19 | 80.6 kWh | 420 km | \$60,000 d/a | KGM Australia |
| KGM Musso EV (AWD) | 26 | 80.6 kWh | 380 km | \$64,000 d/a | KGM Australia |
| Toyota HiLux BEV | ~25 (est.) | 59.2 kWh | 240 km (est.) | TBA (late 2025/2026) | Toyota announcement |

**Implied ratio:** 9 L/100km diesel, 25 kWh/100km electric → **2.8 kWh/L**

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 9 L/100km | 25 kWh/100km |
| Unit cost | \$1.80/L (retail) | \$0.30/kWh (home/depot) |
| **Cost per km** | **\$0.16/km** | **\$0.08/km** |
| Annual saving (20k km) | | **\$1,700** |

### Capital premium

| Comparison | Diesel | Electric | Premium |
|-----------|-------:|---------:|--------:|
| HiLux vs KGM Musso EV | ~\$55,000 | ~\$60,000 | ~\$5,000 |
| Ranger vs LDV eT60 | ~\$55,000 | ~\$93,000 | ~\$38,000 |

The KGM Musso EV at \$60,000 drive-away has changed the economics dramatically — the premium over a diesel ute is now only ~\$5,000, recoverable in fuel savings within **3 years**.

**Verdict:** Economics now favourable for the KGM Musso EV. The LDV eT60 remains expensive. The Toyota HiLux BEV (when it arrives) could be decisive given Toyota's dominant market share in Australian utes. **Key limitation:** electric utes currently have lower towing capacity and shorter range when towing, which matters for tradies and rural users. The Musso EV is based on a monocoque SUV platform rather than a ladder-frame chassis, limiting heavy-duty applications.

---

## 8. Vans

### Diesel consumption

| Vehicle | L/100km (real world) | Source |
|---------|---------------------:|--------|
| Mercedes Sprinter diesel | 10–13 | Fleet operator data |
| Ford Transit diesel | 9–12 | Fleet operator data |
| Toyota HiAce diesel | 8–10 | Owner reports |
| Renault Master diesel | 10–12 | Fleet data |
| **Typical diesel van** | **9–12** | |

### Annual kilometres

Vans used for delivery and trade: estimated **20,000–30,000 km/year**. High-utilisation fleets (parcel delivery, trades) may exceed 40,000 km/year.

### Electric equivalent

| Vehicle | kWh/100km | Battery | Range (WLTP) | Price (AUD) | Source |
|---------|----------:|--------:|-------------:|------------:|--------|
| Mercedes eSprinter (mid) | 27–30 | 81 kWh | 311 km | \$104,313 | Mercedes Australia |
| Mercedes eSprinter (long) | 30–35 | 113 kWh | 437 km | ~\$115,000 | Mercedes Australia |
| Ford E-Transit | 30–38 | 68 kWh | 317 km | \$69,990^c^ | Ford Australia (promotional) |
| Ford E-Transit Custom | ~25 | 64 kWh | 317 km | ~\$75,000 | Ford Australia (2025) |

**Implied ratio:** 11 L/100km diesel, 30 kWh/100km electric → **2.7 kWh/L**

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 11 L/100km | 30 kWh/100km |
| Unit cost | \$1.65/L (fleet) | \$0.28/kWh |
| **Cost per km** | **\$0.18/km** | **\$0.08/km** |
| Annual saving (25k km) | | **\$2,500** |

### Capital premium

| Comparison | Diesel | Electric | Premium |
|-----------|-------:|---------:|--------:|
| Sprinter vs eSprinter | ~\$65,000 | ~\$104,000 | ~\$39,000 |
| Transit vs E-Transit | ~\$55,000 | ~\$70,000^c^ | ~\$15,000 |
| Transit vs E-Transit Custom | ~\$55,000 | ~\$75,000 | ~\$20,000 |

At \$2,500/year fuel saving and a \$39k premium, the eSprinter's simple payback is **~16 years** — unattractive. The Ford E-Transit at \$69,990 drive-away reduces the premium to ~\$15,000 and payback to **~6 years**.^[The E-Transit list price was originally \$104,990; Ford has since reduced to \$69,990. The E-Transit Custom at ~\$75,000 offers a smaller form factor at similar economics.] High-utilisation fleets (40k+ km/year) with depot charging can achieve **4–5 years**.

The core problem for vans remains the **low fuel-bill-to-premium ratio**. A van consuming 11 L/100km generates only \$2,500/year in fuel savings — the absolute size of the fuel bill is simply too small to overcome a premium measured in tens of thousands of dollars. By contrast, a B-double consuming 42 L/100km generates \$73,000/year in savings, easily absorbing a \$250,000 premium.

**Verdict:** Improving but still challenging. The Ford E-Transit price reduction has moved vans from "very marginal" to "viable for high-utilisation fleets with depot charging." The eSprinter remains uneconomic for most operators. Public DC fast charging (55–73c/kWh) destroys the operating cost advantage entirely — depot charging at 25–28c/kWh is essential. Fleet operators running 40k+ km/year from a depot are the natural early adopters; owner-operators and low-km users should wait for further price reductions.

---

## 9. Cab-chassis (light commercial)

Cab-chassis vehicles are utes or light trucks with custom bodies fitted — tray-backs, service bodies, tippers. They overlap significantly with utes (Section 7) and small rigids (Section 5).

### Diesel consumption

Similar to utes: **9–12 L/100km** depending on body weight and application.

### Electric equivalent

The electric cab-chassis market is thin. The Fuso eCanter at 4.5t GVM is the closest equivalent. SEA Electric offers electric conversions of Hino and other cab-chassis platforms, but availability and pricing are case-by-case.

**Verdict:** Limited vehicle availability. The Fuso eCanter 4.5t (car-licence) partially addresses this segment. Purpose-built electric cab-chassis are not yet widely available in Australia. This is a gap in the market.

---

## 10. Passenger vehicles (diesel)

**Diesel budget share:** ~2.9 BL/yr

### Diesel consumption

| Vehicle | L/100km (real world) | Source |
|---------|---------------------:|--------|
| Toyota Prado diesel | 10–11 | CarsGuide, owner reports |
| Ford Everest diesel | 7.5–8.5 | CarsGuide |
| Isuzu MU-X diesel | 7–9 | CarsGuide |
| Diesel sedan (Mazda CX-5 etc.) | 6–7 | Green Vehicle Guide |
| **Typical diesel passenger** | **7–10** | |

### Annual kilometres

Passenger vehicles: **11,100 km/year** (ABS SMVU 2020). However, the SMVU 2020 figure is depressed by COVID lockdowns. Pre-COVID (2018): **13,400 km/year**.

### Electric equivalent

| Vehicle | kWh/100km | Battery | Range | Price (AUD) |
|---------|----------:|--------:|------:|------------:|
| BYD Atto 3 | 15–16 | 60 kWh | 420 km | from \$39,990 |
| Tesla Model Y (RWD) | 13–14 | 60 kWh | 455 km | from \$58,900 |
| MG4 (base) | 14–16 | 51 kWh | 350 km | from \$30,990 (promo) |
| BYD Seal | 14–15 | 82 kWh | 570 km | from \$47,888 |

**Implied ratio:** 8 L/100km diesel, 15 kWh/100km electric → **1.9 kWh/L** (lowest ratio — passenger cars have the smallest efficiency gain from electrification because diesel passenger cars are already relatively efficient, and BEVs carry proportionally heavy batteries for their size)

### Operating cost

| | Diesel | Electric |
|---|------:|--------:|
| Consumption | 8.5 L/100km | 15 kWh/100km |
| Unit cost | \$1.80/L (retail) | \$0.30/kWh (home) |
| **Cost per km** | **\$0.15/km** | **\$0.05/km** |
| Annual saving (12k km) | | **\$1,320** |

### Capital premium

The capital premium for passenger BEVs has collapsed. A BYD Atto 3 at \$40k competes directly with a diesel Mazda CX-5 at \$42k. An MG4 at \$31k is **cheaper** than many diesel alternatives.

**Verdict:** Strong economics. The capital premium is now negligible or negative. The main barrier to diesel-to-electric switching in this segment is not economics but consumer preferences: towing needs, range anxiety for rural drivers, and the dominance of diesel in the large SUV/4WD segment (Prado, LandCruiser, Patrol) where electric alternatives with genuine off-road capability and towing capacity don't yet exist.

---

## 11. Mining (off-road)

**Diesel budget share:** ~9.6 BL/yr — the single largest diesel-consuming sector in Australia

### Where the diesel goes

Mining consumed **9.6 billion litres of diesel** in 2023–24, representing 35% of Australia's total diesel consumption and producing 22 Mt CO2e [@ieefa-mining-diesel-2026]. This figure has been rising — diesel emissions in mining have **doubled since 2011**, increasing at roughly 6% per year, even as government projections assume a 4.5% annual decline.

By commodity, **coal mining accounts for 48%** and **iron ore for 26%** of mining diesel emissions — three-quarters of the total. The remaining 26% is spread across gold, copper, lithium, bauxite, and other minerals.

By equipment type, published data is surprisingly sparse. The best available estimates:

| Equipment category | Share of mine diesel | Source |
|-------------------|--------------------:|--------|
| Haul trucks | ~30–40% | Academic studies; Scope 1 emissions data |
| Excavators and loaders | ~15–20% | Estimated from energy audits |
| Ancillary (dozers, water trucks, graders, drills) | ~40% | Worley analysis |
| Generators and other | ~5–10% | Residual |

Haul trucks are the single largest diesel consumer on a mine site. A Cat 793F (240-tonne class) burns approximately **200–450 L/hour** depending on grade and load, with fuel consumption roughly **4× higher on inclines** than on flat haul roads. BHP and Rio Tinto together operate approximately **1,500 haul trucks** in Australia.

### Why diesel intensity is rising

Coal mining diesel intensity has increased **50% since FY2010-11**, driven by:

- **Rising strip ratios** — deeper pits require moving more overburden per tonne of coal (typical 20:1 material-to-coal)
- **Shift to open-cut** — proportion of coal from open-cut mines grew 30% during 2011–2024
- **Longer haul distances** — as pits deepen, ramp distances lengthen

Between 2018 and 2024, mining diesel consumption rose 23% while extraction volumes grew only 16% [@ieefa-mining-diesel-2026].

### Electric alternatives — surface mining

Surface mine electrification is advancing rapidly but is not yet at fleet scale outside China:

**Battery-electric haul trucks:**

| OEM | Model | Payload | Battery | Status (early 2026) |
|-----|-------|--------:|--------:|-----|
| Liebherr | T 264 BEV | 240 t | 3.2 MWh | Validation at Fortescue Pilbara; 360-unit order (US\$2.8B) |
| Caterpillar | 793 XE | 240 t | Undisclosed | 7 Early Learner units; arrived BHP Jimblebar Dec 2025 |
| Komatsu | 930E Power Agnostic | 290 t | TBD | Diesel-trolley trial at Boliden Aitik (Sweden) Jul 2025 |
| Hitachi | EH4000AC-3 | ~200 t | LTO (ABB) | Single prototype at FQM Kansanshi (Zambia) since Jun 2024 |
| XCMG | ZNK95 | ~95 t | Battery-swap | **100 units operating** at Huaneng Yimin mine (China); 50,000 swaps by Nov 2025 |

The Liebherr T 264 BEV is the most commercially advanced for the Australian market, with Fortescue's order for 360 autonomous battery-electric trucks, 55 electric excavators (R 9400 E), and 60 battery-powered dozers (PR 776), all for delivery by 2030. The battery pack (developed by Fortescue Zero) weighs ~15 tonnes and charges via an automated 6 MW charger in 30 minutes.

**China is ahead on fleet-scale deployment.** Over 2,000 electric mining trucks were projected to be sold in China in 2025, and the China National Coal Association projects over 10,000 autonomous mining trucks by 2026. XCMG has also secured an order to supply up to 400 electric 240-tonne trucks to Fortescue (delivery 2028–2030).

**Trolley-assist** offers a bridging pathway. Overhead DC catenary lines on haul ramps power truck wheel motors directly (diesel engine idles), reducing diesel consumption by **~90% on the ramp** and doubling loaded speed on grade. BHP has submitted an EIS for trolley infrastructure at Escondida (Chile) — US\$250M investment targeting 30% mine-wide diesel reduction by 2028, with full battery-trolley (zero diesel) post-2030.

**Electric excavators** are more advanced than trucks. Electric rope shovels have always been electrically powered (cable-connected) and are standard equipment in large open-pit mines. Liebherr's R 9400 E cable-electric hydraulic excavator has been **operational at Fortescue's Cloudbreak** since December 2023 — Australia's first, and reported to outperform its diesel counterpart.

### Electric alternatives — underground mining

Underground electrification is **significantly further advanced** than surface mining. The drivers are different: eliminating diesel exhaust reduces ventilation costs (30–40% of an underground mine's energy budget), cuts heat load, and improves air quality.

All three major underground equipment OEMs now offer production battery-electric models:

| OEM | Model | Type | Payload | Battery | Status |
|-----|-------|------|--------:|--------:|--------|
| Sandvik | TH665B | Truck | 65 t | 354 kWh LFP | Trial at Sunrise Dam (WA) since Sep 2023; record fleet order from South32 |
| Sandvik | LH621iE | Loader | 21 t | LFP | In production |
| Epiroc | MT42 SG | Truck | 42 t | ~500+ kWh | In production; deployed at multiple sites |
| Epiroc | ST18 SG | Loader | 18 t | 540 kWh LFP | In production |
| Caterpillar | R1700 XE | Loader | 15 t | 213 kWh Li-ion | In production; <20 min charge at 840 kW |

South32's Hermosa mine (Arizona) placed Sandvik's largest-ever BEV fleet order (~SEK 750M) in 2025, covering trucks, loaders, bolters, and drills. Underground BEV technology is no longer experimental — it is entering mainstream commercial adoption.

### Australian deployments

Australia — specifically the **Pilbara iron ore province** — is the global epicentre for mining electrification:

- **Fortescue**: US\$2.8B Liebherr deal (360 BEV trucks + 55 electric excavators + 60 BEV dozers); US\$400M XCMG deal (electric loaders, dozers, water trucks); US\$220M Epiroc deal (~50 autonomous electric drill rigs); R 9400 E electric excavator at Cloudbreak since Dec 2023; 60 MW solar farm displacing ~100 ML diesel/yr; **target zero diesel by 2030**
- **BHP**: Cat 793 XE arrived at Jimblebar Dec 2025 (joint trial with Rio Tinto); strategic XCMG partnership for BEV fleet development; committed to 30% operational emissions reduction by 2030; 200+ electric light vehicles already deployed across WA iron ore
- **Rio Tinto**: Joint Cat 793 XE trial at Jimblebar; Komatsu BEV trials planned for Pilbara from 2026; US\$7.5B decarbonisation investment through 2030
- **AngloGold Ashanti**: Sandvik TH665B trial at Sunrise Dam gold mine (WA) since Sep 2023

### Economics

Mining economics differ fundamentally from on-road transport. A single 240-tonne haul truck consuming 300 L/hr for 6,000 operating hours/year burns approximately **1.8 million litres of diesel per year** — a fuel bill of ~\$3 million at \$1.65/L. Even modest fuel savings per truck are enormous in absolute terms.

The capital cost of a diesel Cat 793F is approximately A\$10 million. Battery-electric premiums are not yet publicly disclosed, but the Fortescue fleet order (at ~US\$7.8M per truck implied by the deal value) suggests premiums may be modest relative to the fuel saving.

**Verdict:** Mining is the largest single diesel sector and electrification is advancing faster than commonly understood. Underground is already commercial. Surface haul trucks are in late-stage trials in the West and fleet-scale deployment in China. The 2025–2030 window is critical. The Fuel Tax Credits Scheme (\$0.48/L rebate on off-road diesel) remains a significant countervailing subsidy — its reform would accelerate the transition.

---

## Summary Table

: Diesel Electrification Economics by Vehicle Class {#tbl-economics-summary}

| Vehicle class | Diesel L/100km | Electric kWh/100km | kWh/L ratio | Diesel \$/km | Electric \$/km | Saving % | Annual km | Annual saving | Payback^a^ |
|--------------|---------------:|-------------------:|------------:|-------------:|---------------:|---------:|----------:|--------------:|--------:|
| Artic >40t (B-double) | 42 | 110 | 2.6 | 1.03 | 0.30 | 71% | 100,000 | \$73,000 | 3–4 yr |
| Artic >40t (semi) | 35 | 110 | 3.1 | 0.58 | 0.31 | 47% | 78,000 | \$21,000 | ~10 yr |
| Artic 30–40t | 28 | 90 | 3.2 | 0.46 | 0.25 | 46% | 60,000 | \$12,600 | ~15 yr |
| Rigid >20t | 32 | 120 | 3.8 | 0.53 | 0.34 | 36% | 25,000 | \$4,800 | >15 yr |
| Rigid 8–20t | 22 | 100 | 4.5 | 0.36 | 0.28 | 22% | 22,000 | \$1,800 | >15 yr |
| Rigid ≤8t | 16 | 55 | 3.4 | 0.26 | 0.15 | 42% | 18,000 | \$2,000 | ~10 yr |
| Buses (metro) | 42 | 100 | 2.4 | 0.69 | 0.25 | 64% | 60,000 | \$26,600 | 4–6 yr |
| Utes | 9 | 25 | 2.8 | 0.16 | 0.08 | 53% | 20,000 | \$1,700 | 3 yr^b^ |
| Vans | 11 | 30 | 2.7 | 0.18 | 0.08 | 54% | 25,000 | \$2,500 | 6–16 yr^c^ |
| Cab-chassis | 10 | ~50 | ~3 | 0.17 | 0.14 | 18% | 18,000 | \$500 | >20 yr |
| Passenger diesel | 8.5 | 15 | 1.9 | 0.15 | 0.05 | 70% | 12,000 | \$1,320 | 0–3 yr |

: Source: Author calculations based on ABS SMVU 2020, OEM specifications, fleet operator data, and the sources cited in each section.

^a^ Simple payback = capital premium / annual fuel saving. Does not include maintenance savings (typically 30–50% lower for BEVs).
^b^ Based on KGM Musso EV at ~\$5k premium over diesel ute. LDV eT60 payback is much longer (~22 yr).
^c^ 6 yr at Ford E-Transit \$69,990; 16 yr at eSprinter \$104,000.

---

## The Diesel-to-Electricity Ratio by Vehicle Class

The empirical kWh-per-litre ratio varies systematically:

| Vehicle class | kWh per litre diesel displaced | Why |
|--------------|------:|-----|
| Passenger cars | 1.9 | Diesel cars already quite efficient; BEV battery weight penalty proportionally large |
| Buses | 2.4 | Large vehicles, good diesel thermal efficiency, but stop-start gives BEV regeneration advantage |
| Artic trucks (heavy) | 2.6 | Excellent diesel thermal efficiency at cruise; limited regeneration on highway |
| Vans | 2.7 | Mixed use; some urban regeneration benefit |
| Utes | 2.8 | Mixed use, moderate regeneration |
| Light rigids | 3.4 | Urban stop-start maximises regeneration |
| Rigid >20t | 3.8 | Urban/suburban cycles, heavy braking loads |
| Rigid 8–20t | 4.5 | Delivery cycles with constant stop-start — maximum BEV advantage |

The pattern is clear: **urban stop-start duty cycles produce the highest kWh/L ratios** (i.e., electric vehicles gain the most advantage), while **highway cruise operation produces the lowest ratios** (diesel engines are already relatively efficient at steady state).

---

## Policy Prioritisation Scorecard

This scorecard ranks each diesel sub-sector on three dimensions to identify where policy intervention would have the greatest impact. Each dimension is scored 1–5 (5 = strongest case for policy action). Budget is **double-weighted** because we want to prioritise sectors where electrification displaces the most diesel. Total = Budget×2 + Economics + Availability (out of 20).

### Scoring criteria

1. **Diesel budget** — annual consumption in billion litres. Larger budgets mean more emissions displaced per percentage point of electrification.
2. **Fuel cost economics** — combination of per-km saving percentage and simple payback period. Better economics mean the private sector will move faster with lighter policy nudges.
3. **Vehicle availability** — whether fit-for-purpose electric alternatives exist in production, at scale, at competitive prices.

### Scorecard

: Policy Prioritisation Scorecard — Diesel Electrification by Sector {#tbl-policy-scorecard}

| Sector | Diesel (BL/yr) | Budget | Econ | Avail | **Total (/20)** | **Priority** |
|--------|---------------:|:---:|:---:|:---:|:---:|:---|
| **Artic >40t** | 4.0 | 5 | 5 | 3 | **18** | Highest |
| **Passenger diesel** | 3.1 | 4 | 5 | 5 | **18** | Highest^d^ |
| **Mining** | 9.6 | 5 | 3 | 3 | **16** | Highest |
| Utes | 3.2 | 3 | 4 | 2 | **12** | Medium |
| Buses | 0.5 | 1 | 5 | 5 | **12** | Medium |
| Construction | 2.5 | 4 | 2 | 2 | **12** | Medium |
| Agriculture | 2.5 | 4 | 2 | 1 | **11** | Medium |
| Vans | 1.8 | 3 | 2 | 3 | **11** | Medium |
| Rigid >20t | 1.6 | 3 | 2 | 3 | **11** | Medium |
| Rigid ≤8t | 0.7 | 2 | 3 | 3 | **10** | Medium |
| Rigid 8–20t | 0.8 | 2 | 1 | 3 | **8** | Low |
| Artic 30–40t | 0.3 | 1 | 2 | 4 | **8** | Low |
| Cab-chassis | ~0.5 | 1 | 2 | 1 | **5** | Low |

: Source: Author calculations based on ABS SMVU 2020 diesel budgets (Table 2.6) and the economics analysis in this document. Budget is double-weighted: Total = Budget×2 + Econ + Avail.

^d^ Passenger diesel scores highest but the market is largely self-correcting — BEV prices are at or below diesel equivalents and sales are growing without significant policy support. Policy effort is better directed at segments where market failures or structural barriers impede the transition.

### Interpretation by priority tier

**Highest priority — Artic >40t (score 18)**
The single largest on-road diesel consumer at 4.0 BL/yr. Economics are compelling (71% fuel saving, 3–4 year payback for B-doubles) and multiple production trucks exist for semi-trailers up to 44t GCW. The Windrose E1400 has demonstrated 68-tonne B-double operation in Australia (hauling steel up Mount Ousley for Toll/BlueScope), and established OEMs (Volvo, Scania) are production-ready for semi-trailers. Policy should focus on:

- Charging infrastructure on major freight corridors (Megawatt Charging System deployment)
- Support for Windrose and established OEM electric prime movers at B-double weights
- Purchase subsidies or accelerated depreciation for first-mover fleets

**Highest priority — Passenger diesel (score 18)**
Scores jointly highest but the market is largely self-correcting — BEV prices are at or below diesel equivalents and sales are growing without significant policy support. Policy effort is better directed at segments where market failures or structural barriers impede the transition.

**Highest priority — Mining (score 16)**
The largest single diesel consumer at 9.6 BL/yr and advancing faster than widely understood. Underground BEV equipment is already in commercial production (Sandvik, Epiroc, Caterpillar). Surface haul trucks are in late-stage trials in Australia (Cat 793 XE at BHP Jimblebar, Liebherr T 264 BEV at Fortescue) and fleet-scale deployment in China (100 XCMG trucks at Yimin mine). Fortescue has ordered 360 BEV trucks for delivery by 2030. The Fuel Tax Credits Scheme (\$0.48/L rebate) remains the largest policy lever — its reform or phase-out would sharply tilt mining economics toward electrification. Trolley-assist offers a bridging pathway (30% mine-wide diesel reduction) while full BEV fleets scale up.

**Medium priority — Utes (score 12)**
At 3.2 BL/yr, utes are the second-largest on-road diesel segment — but the realistic electrification pathway is PHEV, not BEV. The BYD Shark 6 (\$57,900, 80 km EV range, 2,500 kg towing) is already the 4th best-selling 4x4 ute in Australia, and the GWM Cannon Alpha PHEV and Ford Ranger PHEV offer full 3,500 kg towing at near-diesel prices. Full BEV utes remain compromised: the Toyota HiLux BEV (due H1 2026) offers only 240 km range and ~1,600 kg towing at an estimated \$90–100k — far weaker than the KGM Musso EV (\$60,000, 420 km) but still limited. Because PHEVs displace only 50–70% of diesel (drivers revert to petrol/diesel for long trips and heavy towing), the effective diesel prize is ~2 BL rather than 3.2 BL. Budget and availability scores are reduced accordingly. The market is partially self-correcting via PHEVs; policy should focus on ensuring charging infrastructure reaches regional centres and workplaces.

**Medium priority — Buses (score 12)**
Despite excellent economics and vehicle availability (both scored 5), buses rank only Medium because the diesel budget is small (0.5 BL). Government controls procurement (transit authorities), so this is the segment where government can move fastest — all states should mandate 100% zero-emission bus purchases for new fleet. But the total diesel displacement prize is modest.

**Medium priority — Construction, Agriculture, Vans, Rigids (scores 10–12)**
Construction and agriculture have sizeable diesel budgets (2.5 BL each) but electric alternatives are embryonic. Vans suffer from a structural problem: the fuel bill is too small relative to the vehicle premium. At 11 L/100km and 25,000 km/year, annual fuel cost is only ~\$4,500 — even a 54% saving (\$2,500/yr) takes 6–16 years to recover the capital premium. Heavy rigids (>20t) have moderate diesel budgets but low annual km limits the fuel saving. The Fuso eCanter addresses the light rigid (≤8t) segment. Policy should support demonstration projects and fleet purchase subsidies but should not divert resources from higher-priority sectors.

**Low priority — Rigid 8–20t, Artic 30–40t, Cab-chassis (scores 5–8)**
Medium rigids (8–20t) are the weakest on-road segment: 22% fuel saving and >15 year payback. Artic 30–40t vehicles exist but the tiny diesel budget (0.3 BL) limits the prize. Cab-chassis have no purpose-built electric models in Australia. Economics will improve naturally as vehicle prices fall — no near-term policy action warranted.

### China as validation

China is the world's largest commercial vehicle market and accounts for over 80% of global electric truck sales. Its deployment data provides an independent check on our scorecard: if the economics are right, the sectors we rank highest should be the ones where China has moved furthest. Total new energy commercial vehicle sales reached **871,000 units in 2025** (up 64% YoY), with an overall penetration rate of 26.9%.

: China NE Commercial Vehicle Penetration vs Australian Scorecard {#tbl-china-validation}

| Sector | Our score | Our priority | China NE penetration (2025) | China validates? |
|--------|:---------:|:-------------|----------------------------:|:-----------------|
| Heavy trucks (>16t) | 18 | Highest | 28.9% (231,100 units) | Yes — explosive growth |
| Passenger BEVs | 18 | Highest | ~50% of all new car sales | Yes — self-correcting market |
| Mining haul trucks | 16 | Highest | 100+ BEV trucks at Yimin; 10,000 target by 2026 | Yes — fleet-scale |
| Utes/pickups | 12 | Medium | ~10% (niche; 15,000 units) | N/A — pickups are a niche category in China |
| Buses | 12 | Medium | ~95% (Shenzhen 100% since 2018) | Yes — strongest case globally |
| Vans/LCVs (<3.5t) | 11 | Medium | **45–59%** (urban logistics) | **No** — China far ahead^e^ |
| Light/medium trucks | 8–10 | Low–Medium | ~27% (~300,000 units) | **No** — China far ahead^e^ |

: Source: ICCT, IEA Global EV Outlook 2025, CAAM via CnEVPost and Electrive. Full 2025 figures include subsidy front-loading in December.

^e^ China's van and light truck penetration (45–59% and 27% respectively) is far higher than our scorecard's "Medium" and "Low" ratings would suggest. Three factors explain the divergence: (1) Chinese EV prices are 40–60% lower than in Australia (e.g., electric vans from ~\$15,000); (2) Chinese cities restrict diesel vehicle access to urban centres, creating a regulatory push absent in Australia; (3) Chinese fleet utilisation rates are higher (more km/year), improving payback. **Our Australian scorecard ratings remain valid for Australian conditions** — the economics genuinely are marginal for vans and medium rigids at Australian vehicle prices. But the China data shows that if vehicle prices fall (as they did for passenger BEVs), these segments could shift rapidly.

**Key insight from China data:** In December 2025, electric heavy trucks outsold diesel for the first time in a single month (54% share), though this was distorted by front-loading ahead of a 2026 subsidy expiry. The full-year penetration rate of 28.9% is more representative but still remarkable — it was just 9.9% in 2024.^[Source: Electrive, "Year-end surge: electric trucks outsell diesel for first time in China," January 2026.]

The top Chinese NE heavy truck manufacturers are XCMG, SANY, FAW Jiefang, Shacman, and Yutong — none of which currently sell electric trucks in Australia. BYD, which dominates the Australian electric bus market, is not a top-10 NE heavy truck maker in China but is growing fast (+711% in H1 2025 for non-bus commercial vehicles).

---

## Problem Websites (for manual download)

The following sources contain data tables needed for this analysis but could not be accessed by automated research agents:

1. **ABS SMVU 2020 Excel workbook** — `abs.gov.au/statistics/.../92080DO001_202006.xls` (binary Excel, JavaScript-heavy ABS pages)
2. **BITRE Road Vehicles Australia January 2024** — `bitre.gov.au/.../bitre-road-vehicles-australia--january2024.pdf` (PDF parsing issues)
3. **ATAP Appendix E fuel consumption coefficients** — `atap.gov.au/.../appendix-e-detailed-fuel-consumption-coefficients-uninterrupted-flow` (the page loaded but detailed coefficient tables may need manual extraction)
4. **NTC Heavy Vehicle Operating Cost Model** — operator cost reports not freely available online
5. **Australia Institute "Slow Lane" electric bus report** — `australiainstitute.org.au/wp-content/uploads/2023/04/P1321-Slow-lane-electric-buses-Web.pdf` (PDF parsing failed)

---

## Sources

Key sources consulted:

- ABS Survey of Motor Vehicle Use, Australia, Cat. 9208.0, 12 months ended 30 June 2020
- H2-Hybrid Australia — truck fuel consumption database
- ATAP (Australian Transport Assessment and Planning) — vehicle operating cost models
- The Conversation, "Electric trucks are finally ready for prime time" (Mar 2026) — citing David Leitch analysis
- Trucksales.com.au — 2025 electric truck guide
- Sustainable-bus.com — electric bus energy consumption data
- CarExpert, CarsGuide, Zecar — Australian vehicle pricing and specifications
- ICCT working papers on HDV total cost of ownership
- NREL electric vehicle efficiency ratios

See `diesel_electrification_references.bib` for full bibliography.
