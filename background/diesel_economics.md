---
title: "Diesel Segment Economics: Total Cost of Ownership and Electrification Payback"
author: "David Leitch"
date: 2026-03-31
categories: ["EVs", "Investment"]
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

This document estimates the total cost of ownership (TCO) for each of the 13 diesel segments identified in the electrification prioritisation scorecard. It establishes the fuel share of total operating costs — the metric that determines how much electrification transforms the cost structure of each segment — and traces the logic from TCO through to the economic score used in the bubble chart and policy scorecard.

The headline finding: **fuel as a share of total operating cost ranges from 2% (passenger diesel) to 62% (mining haul trucks)**. When driver/operator wages are excluded, fuel's share of the controllable vehicle cost stack ranges from 13% (passenger) to 74% (agriculture). Off-road sectors — mining, construction, and agriculture — are the segments where fuel most dominates the cost structure, and where electrification most transforms the economics.

However, fuel share alone does not determine electrification economics. The critical metric is **simple payback**: the BEV capital premium divided by annual fuel saving. Segments with short payback (under 6 years) score highest regardless of fuel share. Passenger diesel vehicles have the lowest fuel share (2% of total including imputed driver) but score 5/5 on economics because the BEV premium has collapsed to zero.

---

# Methodology

## Cost components

For each segment we estimate five cost components:

1. **Fuel** — diesel consumption × price. Retail diesel at \$1.80/L for on-road vehicles. Fuel Tax Credit rebate (\$0.48/L) shown separately for eligible off-road sectors (mining, agriculture, construction).
2. **Driver/operator** — **fully loaded employer cost** including base salary, superannuation (11.5%), workers' compensation insurance (~6–7% for road transport), payroll tax (~5%), leave loading (17.5%), long service leave accrual, away-from-base allowances (where applicable), and relief/leave cover. This is the true cost to the fleet operator, not take-home pay. For owner-operated vehicles (utes, passenger cars, cab-chassis), an **imputed loaded cost of \$110,000/yr** is applied to enable like-for-like comparison across all segments. This figure approximates the fully loaded opportunity cost of a skilled operator.
3. **Depreciation** — purchase price divided by economic life. No financing costs (interest varies too much by operator).
4. **Maintenance + tyres** — scheduled and unscheduled maintenance, including tyre replacement for heavy vehicles.
5. **Insurance + registration + other** — comprehensive insurance, CTP, NHVR registration, and road user charges where applicable.

## Price assumptions

| Input | Value | Source |
|:------|------:|:-------|
| Retail diesel | \$2.00/L | B-doubles (real-world, incl AdBlue); \$1.80/L for other on-road |
| Fuel Tax Credit | \$0.48/L | Off-road diesel rebate (mining, agriculture, construction) |
| Electricity — high-volume fleet | \$0.15/kWh | B-doubles and mining; dedicated depot/site charging at off-peak or PPA rates |
| Electricity — standard commercial | \$0.25/kWh | All other segments; commercial depot charging tariffs |
| B-double driver (loaded) | \$200,000/yr | MC licence long-haul; base ~\$120k + on-costs ~\$80k |
| Mining operators (loaded, 2.3 FTE) | \$320,000/yr | Two-shift FIFO; base ~\$130k/FTE + on-costs |
| Bus driver (loaded) | \$115,000/yr | Metro transit; base ~\$75–85k + on-costs |
| Imputed driver (loaded) | \$110,000/yr | Applied to owner-operated segments for comparability |

**Labour cost sources:** Fair Work Road Transport (Long Distance Operations) Award MA000039 (52.85 c/km minimum, Oct 2025); NatRoad wage rate guidance (July 2024); Indeed, SEEK, Glassdoor salary data (2025–26); NET financial modelling (\$2.1M/10yr = \$210k/yr for B-double driver, consistent with loaded cost). On-cost loading of ~60–70% on base salary is standard for Australian road transport (super 11.5% + workers comp ~6.5% + payroll tax ~5% + leave loading 17.5% + LSL ~2% + relief cover ~12% + allowances).

## Confidence ratings

Each segment is rated for data confidence:

- **High** — fuel consumption from ABS SMVU or fleet telemetry; vehicle prices from public dealer data; payback calculable from known BEV pricing.
- **Medium** — fuel consumption from OEM specifications or ATAP models; vehicle prices from dealer data; some cost components estimated.
- **Low** — fuel consumption from OEM midpoint of a wide range; maintenance and BEV premium data unavailable; payback uncertain.

---

# Total Cost of Ownership by Segment

## 1. Mining — 240t haul truck (Cat 793F), 6,000 hrs/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 2,970,000 | 300 L/hr × 6,000 hr × \$1.65/L |
| FTC rebate | –864,000 | \$0.48/L × 1.8M litres |
| **Fuel (net of FTC)** | **2,106,000** | |
| Operators (2.3 FTE, loaded) | 320,000 | Two-shift FIFO; base ~\$130–140k/FTE + super, workers comp, FIFO allowances, leave cover |
| Depreciation | 750,000 | \$10M purchase ÷ ~13 yr economic life |
| Maintenance + rebuilds | 480,000 | ~\$80/operating hour |
| Tyres | 240,000 | 6 × ~\$50k, ~5,000 hr average life |
| Overhead/insurance | 100,000 | Site-allocated |
| **Total (pre-FTC)** | **4,860,000** | |
| **Total (post-FTC)** | **3,996,000** | |

**Fuel share:** 61% of total (pre-FTC); 53% post-FTC. Excluding labour: 65%.

**Electrification economics:** Assuming a modest BEV premium of 20–30% over the \$10M diesel purchase price (\$2–3M), the annual fuel saving of \$2.97M (pre-FTC) implies payback **under 1.5 years**. Even at a 50% premium (\$5M), payback is under 2 years. The Fortescue order for 360 Liebherr T 264 BEV trucks at an implied ~US\$7.8M per unit (~A\$12M) suggests a premium of ~\$2M over diesel, consistent with this estimate. Mining haul trucks have arguably the strongest electrification economics of any segment in absolute dollar terms, limited only by the early stage of fleet-scale deployment outside China.

**Sources:** IEEFA mining diesel report (fuel consumption, diesel volumes); Cat 793F OEM specifications; Fortescue deal value (implied per-unit pricing); Australia Institute FTC analysis; industry estimates for maintenance (\$80/hr) and tyres. **Confidence: Medium** — fuel data is high confidence (IEEFA), but maintenance, depreciation, and BEV premium are industry estimates.

---

## 2. Articulated trucks >40t — B-double, 180,000 km/yr

The ABS SMVU 2020 (Table 29) identifies **20,862 B-doubles** in Australia — all >40t GCM — carrying 79,448 million tonne-km at an average of 3.81 million tonne-km per vehicle. This is the highest work intensity of any truck configuration. Dividing by the fleet-average load across all km (~21t, including empty running), the implied average distance is **~180,000 km/yr** — far higher than the 78,300 km/yr average for all articulated trucks (which includes lighter semis doing shorter routes). This figure is consistent with NET's financial modelling at 200,000 km/yr for dedicated corridor B-doubles. BITRE Road Vehicles Australia (January 2025, Table 10) records 69,039 artics in the 60–100t GCM band — the weight class that includes most B-doubles — confirming the fleet has grown since the 2020 SMVU.

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 180,000 | 50 L/100km × 180,000 km × \$2.00/L |
| Driver (loaded) | 200,000 | MC licence long-haul; base ~\$120k + super, workers comp, payroll tax, allowances, leave cover |
| Depreciation | 46,000 | PM \$330k/10yr + B-double trailer set \$200k/15yr |
| Maintenance + tyres | 36,000 | ~\$0.20/km |
| Insurance | 18,000 | Comprehensive + CTP + cargo |
| Rego + road user charges | 22,000 | NHVR registration + RUC ~7c/km interstate |
| **Total** | **502,000** | |

**Fuel share:** 36% of total. Excluding labour: 60%.

**Electrification economics:** At 180,000 km/yr and real-world 50 L/100km, the annual fuel bill is \$180k. At \$0.30/km electric running cost (\$54k/yr), the annual saving is ~\$126,000. At an estimated BEV premium of ~\$250,000, simple payback is **~2 years**. For triaxle semi-trailers (the largest artic sub-fleet at ~50,000 vehicles, averaging ~50,000 km/yr), the saving is smaller but still material. The B-double is the single most compelling on-road electrification target: 20,862 vehicles consuming an estimated ~1,600 ML of diesel per year (39% of all artic >40t fuel).

**Sources:** ABS SMVU 2020 Table 29 (B-double tonne-km and vehicle count, derived); Table 4 (total artic vehicles and km); BITRE Road Vehicles Australia January 2025 Table 10 (current fleet by GCM); ATAP Appendix E (B-double L/100km); TruckSales.com.au (new vehicle pricing); NTC Heavy Vehicle Operating Cost Model (indicative maintenance); Fair Work Road Transport Award (driver wages); NHVR (registration and RUC schedules). **Confidence: High** — vehicle count and km/yr now derived from ABS primary data.

---

## 3. Passenger diesel — large SUV (Prado/Everest class), 15,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 2,295 | 8.5 L/100km × 15,000 km × \$1.80/L |
| Imputed driver (loaded) | 110,000 | Standardised loaded opportunity cost |
| Depreciation | 10,500 | ~\$70k vehicle, ~15% avg annual |
| Insurance | 2,200 | Comprehensive |
| Maintenance | 1,500 | Scheduled servicing |
| Rego + CTP | 1,200 | State average |
| **Total** | **127,695** | |

**Fuel share:** 2% of total (incl imputed driver). Excluding labour: 13%.

**Electrification economics:** BEV alternatives (BYD Atto 3 at \$40k, MG4 at \$31k) are at or below the price of equivalent diesel SUVs. The capital premium is **zero or negative**. A 70% fuel cost saving (\$0.15/km → \$0.05/km) delivers ~\$1,320/yr. Payback: **0–3 years**. This market is largely self-correcting — no policy intervention required beyond maintaining the NVES.

**Sources:** CarsGuide (real-world fuel consumption); ABS SMVU 2020 (annual km, adjusted for pre-COVID); RedBook (depreciation); manufacturer websites (BEV pricing); RACV/NRMA (insurance, rego). **Confidence: High.**

---

## 4. Buses — 12m metro transit, 60,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 41,580 | 42 L/100km × 60,000 km × \$1.65/L |
| Driver (loaded) | 115,000 | Metro transit; base ~\$80k + super, workers comp, penalties, leave cover |
| Depreciation | 30,000 | \$450k ÷ 15 yr asset life |
| Maintenance | 18,000 | ~\$0.30/km for diesel bus |
| Insurance + rego | 8,000 | State fleet |
| **Total** | **212,580** | |

**Fuel share:** 20% of total. Excluding labour: 43%.

**Electrification economics:** A 64% fuel cost saving (\$0.69/km → \$0.25/km) delivers ~\$26,600/yr. The BEV premium is \$300–400k (BYD K9 ~\$800k vs diesel at ~\$450k), giving payback of **4–6 years** against a 15–20 year asset life. When maintenance savings are included (diesel bus maintenance is 30–50% higher than electric), effective payback drops to 3–4 years. Every state transit authority in Australia now has zero-emission bus procurement targets.

**Sources:** Transit authority fleet data (fuel consumption, annual km); Sustainable Bus (electric bus energy consumption benchmarks); Transport Workers' Union EBA (driver wages); transit authority procurement data (vehicle pricing, asset life). **Confidence: High.**

---

## 5. Utes — HiLux/Ranger dual-cab 4x4, 20,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 3,240 | 9 L/100km × 20,000 km × \$1.80/L |
| Imputed driver (loaded) | 110,000 | Standardised loaded opportunity cost |
| Depreciation | 8,000 | ~\$55k vehicle, ~15% avg annual |
| Insurance | 1,800 | Comprehensive |
| Maintenance | 1,200 | Scheduled servicing |
| Rego + CTP | 900 | State average |
| **Total** | **125,140** | |

**Fuel share:** 3% of total (incl imputed driver). Excluding labour: 21%.

**Electrification economics:** The KGM Musso EV at \$60,000 commands a premium of only ~\$5,000 over a diesel ute. A 53% fuel cost saving (\$0.16/km → \$0.08/km) delivers ~\$1,700/yr, giving payback of **~3 years**. However, the realistic pathway is PHEV, not full BEV — the BYD Shark 6 (\$57,900, 80 km electric range) is already the 4th best-selling 4x4 ute in Australia. PHEVs displace only 50–70% of diesel, reducing the effective diesel prize from 3.2 BL to ~2 BL.

**Sources:** CarsGuide (real-world consumption); ABS SMVU 2020 (annual km); FCAI VFACTS (pricing); manufacturer websites (BEV pricing). **Confidence: High.**

---

## 6. Construction — 20t excavator (Cat 320), 4,000 hrs/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 132,000 | 20 L/hr × 4,000 hr × \$1.65/L |
| FTC rebate | –38,400 | \$0.48/L × 80,000 litres |
| **Fuel (net of FTC)** | **93,600** | |
| Operator (loaded) | 110,000 | Earthmoving operator; base ~\$80k + on-costs |
| Depreciation | 25,000 | \$250k ÷ 10 yr |
| Maintenance | 20,000 | ~\$5/hr |
| Insurance/mobilisation | 5,000 | Site-allocated |
| **Total (pre-FTC)** | **292,000** | |

**Fuel share:** 45% of total (pre-FTC). Excluding labour: 72%.

**Electrification economics:** Electric excavators are emerging — Caterpillar's 320F Z-Line and Volvo's ECR25 Electric are in production or late trials — but most construction equipment categories (dozers, cranes, compactors) have no electric alternative at Australian-relevant sizes. No BEV premium data is publicly available for medium excavators. The FTC rebate further weakens the incentive. Score reflects uncertainty, not poor underlying economics.

**Sources:** Cat 320 OEM specifications (fuel consumption range 15–25 L/hr, midpoint used); ConstructionSales (vehicle pricing); Australia Institute (FTC); Fair Work construction EBA (operator). **Confidence: Low** — fuel consumption is midpoint of a wide OEM range; maintenance data limited; no BEV pricing available.

---

## 7. Agriculture — 200hp tractor (John Deere 6R), 1,500 hrs/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 74,250 | 30 L/hr × 1,500 hr × \$1.65/L |
| FTC rebate | –21,600 | \$0.48/L × 45,000 litres |
| **Fuel (net of FTC)** | **52,650** | |
| Imputed operator (loaded) | 110,000 | Standardised loaded opportunity cost |
| Depreciation | 15,000 | \$200k ÷ 13 yr (slow turnover, avg age ~15 yr) |
| Maintenance | 8,000 | ~\$5/hr |
| Insurance | 3,000 | Farm equipment |
| **Total (pre-FTC)** | **210,250** | |

**Fuel share:** 35% of total (pre-FTC). Excluding labour: 74%.

**Electrification economics:** Electric tractors are embryonic. The Monarch MK-V is in limited US production; John Deere has demonstrated a prototype but has no production timeline. Solar-plus-battery systems for irrigation pumps and sheds are commercially proven and already deployed on Australian farms, but they address stationary loads, not mobile equipment. The agricultural fleet turns over very slowly and operates far from grid infrastructure. No BEV pricing data exists for broadacre tractors.

**Sources:** John Deere 6R OEM specifications (fuel consumption range 20–40 L/hr, midpoint used); Farm Machinery Sales (vehicle pricing); Australia Institute (FTC). **Confidence: Low** — fuel consumption is midpoint of a wide range; hours are seasonal (1,000–2,000); maintenance is an author estimate.

---

## 8. Vans — Sprinter/Transit, 25,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 4,538 | 11 L/100km × 25,000 km × \$1.65/L |
| Driver (loaded) | 110,000 | Urban courier/delivery; base ~\$70k + on-costs |
| Depreciation | 9,300 | \$65k ÷ 7 yr |
| Insurance | 3,000 | Commercial fleet |
| Maintenance | 2,000 | Scheduled servicing |
| Rego + CTP | 1,000 | |
| **Total** | **129,838** | |

**Fuel share:** 3% of total. Excluding labour: 23%.

**Electrification economics:** The core problem for vans is the low fuel-bill-to-premium ratio. Annual fuel spend is only ~\$4,500 — even a 54% saving (\$2,500/yr) takes 6–16 years to recover the BEV premium (\$15k for Ford E-Transit; \$39k for Mercedes eSprinter). Public DC fast charging (55–73c/kWh) eliminates the operating cost advantage entirely — depot charging at 25–28c/kWh is essential. High-utilisation fleets (40k+ km/yr) with depot charging can achieve 4–5 year payback; most operators cannot.

**Sources:** Fleet operator data (fuel consumption); Mercedes/Ford Australia (BEV pricing); Transport Workers' Union EBA (driver wages); manufacturer websites (diesel pricing). **Confidence: High.**

---

## 9. Rigid trucks >20t — heavy rigid (waste/tipper), 25,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 13,200 | 32 L/100km × 25,000 km × \$1.65/L |
| Driver (loaded) | 110,000 | Urban heavy vehicle; base ~\$75k + on-costs |
| Depreciation | 25,000 | \$300k ÷ 12 yr |
| Maintenance + tyres | 8,000 | ~\$0.32/km |
| Insurance | 8,000 | Commercial heavy vehicle |
| Rego | 5,000 | NHVR |
| **Total** | **169,200** | |

**Fuel share:** 8% of total. Excluding labour: 22%.

**Electrification economics:** At 32 L/100km and only 25,000 km/yr, the annual fuel bill is modest (\$13k). A 36% fuel saving yields ~\$4,800/yr, but with BEV premiums of \$70–100k (estimated from Volvo FE Electric and Mercedes eActros 300 pricing), payback exceeds **15 years**. The exception is waste collection: stop-start urban routes maximise regenerative braking, and several Australian councils have found TCO competitive when maintenance savings (30–50% lower) are included.

**Sources:** ATAP (fuel consumption); ABS SMVU 2020 (annual km); Hino/Isuzu dealer pricing; NTC Heavy Vehicle model (indicative maintenance); NHVR (registration). **Confidence: Medium.**

---

## 10. Rigid trucks 8–20t — medium rigid (Hino 500), 22,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 7,986 | 22 L/100km × 22,000 km × \$1.65/L |
| Driver (loaded) | 110,000 | Urban delivery; base ~\$70k + on-costs |
| Depreciation | 17,000 | \$200k ÷ 12 yr |
| Maintenance | 5,000 | ~\$0.23/km |
| Insurance | 5,000 | |
| Rego | 3,000 | NHVR |
| **Total** | **147,986** | |

**Fuel share:** 5% of total. Excluding labour: 21%.

**Electrification economics:** This is the weakest on-road segment. At 22 L/100km and 22,000 km/yr, annual fuel spend is only \$8,000. A 22% fuel saving (\$1,800/yr) — the lowest of any segment — cannot justify a BEV premium of \$50–80k. Payback exceeds **15 years**. The Volvo FL Electric addresses this segment and DHL has reported positive TCO at high utilisation, but only when maintenance savings are included. No near-term policy action warranted; economics will improve as battery prices fall.

**Sources:** ATAP (fuel consumption); ABS SMVU 2020 (annual km); Hino/Isuzu dealer pricing; fleet operator data. **Confidence: Medium.**

---

## 11. Rigid trucks ≤8t — light rigid (Fuso Canter), 18,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 4,752 | 16 L/100km × 18,000 km × \$1.65/L |
| Driver (loaded) | 110,000 | Light delivery (car licence); base ~\$65k + on-costs |
| Depreciation | 8,000 | \$80k ÷ 10 yr |
| Maintenance | 3,000 | |
| Insurance | 4,000 | |
| Rego | 2,000 | |
| **Total** | **131,752** | |

**Fuel share:** 4% of total. Excluding labour: 22%.

**Electrification economics:** The Fuso eCanter 2nd generation (from \$68,900, 14 variants, up to 300 km range) commands a premium of ~\$14–30k over diesel equivalents. A 42% fuel saving yields ~\$2,000/yr, giving payback of ~10 years on fuel alone. When maintenance savings are included (electric drivetrains have 30–50% lower servicing costs), payback drops to 6–8 years. Small batteries charge overnight from a standard 15A depot outlet. This is the most accessible electric truck segment.

**Sources:** Fuso dealer pricing (eCanter and diesel Canter); fleet operator data (fuel consumption); ABS SMVU 2020 (annual km). **Confidence: Medium.**

---

## 12. Articulated trucks 30–40t — distribution semi, 60,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 27,720 | 28 L/100km × 60,000 km × \$1.65/L |
| Driver (loaded) | 110,000 | Regional distribution; base ~\$80k + on-costs |
| Depreciation | 18,000 | \$215k ÷ 12 yr |
| Maintenance + tyres | 12,000 | ~\$0.20/km |
| Insurance | 12,000 | |
| Rego + RUC | 10,000 | |
| **Total** | **189,720** | |

**Fuel share:** 15% of total. Excluding labour: 35%.

**Electrification economics:** At 28 L/100km and 60,000 km/yr, annual fuel spend is ~\$28k. A 46% fuel saving yields ~\$12,600/yr, but with a BEV premium of ~\$200k (estimated from eActros 600, Volvo FH Electric), payback is **~15 years**. Multiple production vehicles exist (Scania BEV, Volvo FH Electric, Mercedes eActros 600), so vehicle availability is not the constraint. The tiny diesel budget (0.3 BL total) means complete electrification of this segment would displace less diesel than a single large mine site.

**Sources:** ATAP (fuel consumption); author estimate for annual km (lighter artics serve shorter distribution routes than heavy artics); TruckSales (vehicle pricing). **Confidence: Medium.**

---

## 13. Cab-chassis — tray-back (trade), 18,000 km/yr

| Cost item | \$/yr | Basis |
|:----------|------:|:------|
| Fuel | 3,240 | 10 L/100km × 18,000 km × \$1.80/L |
| Imputed driver (loaded) | 110,000 | Standardised loaded opportunity cost |
| Depreciation | 6,000 | ~\$50k ÷ 8 yr |
| Insurance | 1,500 | |
| Maintenance | 1,000 | |
| Rego + CTP | 800 | |
| **Total** | **122,540** | |

**Fuel share:** 3% of total (incl imputed driver). Excluding labour: 26%.

**Electrification economics:** No purpose-built electric cab-chassis models are available in Australia. The Fuso eCanter at 4.5t GVM partially addresses this segment. SEA Electric offers electric conversions of existing platforms, but availability and pricing are case-by-case. With annual fuel spend of only \$3,200 and no clear BEV alternative to price, payback is incalculable. Economics will improve as electric light trucks proliferate.

**Sources:** CarsGuide (fuel consumption, estimated); author estimate for annual km. **Confidence: Low.**

---

# Summary Table

**Table: Total Cost of Ownership and Electrification Economics by Diesel Segment**

| Segment | Fuel \$/yr | Total opex | Fuel % | Fuel % excl labour | Saving % | Saving \$/yr | Premium | Payback | Econ | Confidence |
|:--------|----------:|-----------:|-------:|-------------------:|:--------:|-----------:|--------:|--------:|:----:|:-----------|
| Mining (haul truck) | 2,970,000 | 4,860,000 | 61% | 65% | ~70% | ~2,079,000 | ~\$2–3M | ~1 yr | 5 | Medium |
| Artic >40t (B-double) | 180,000 | 502,000 | 36% | 60% | 72% | 129,000 | ~\$250k | ~2 yr | 5 | High |
| Passenger diesel | 2,295 | 127,695 | 2% | 13% | 75% | 1,733 | \$0/neg | 0–3 yr | 5 | High |
| Buses (metro) | 41,580 | 212,580 | 20% | 43% | 64% | 26,580 | \$300–400k | 4–6 yr | 5 | High |
| Utes | 3,240 | 125,140 | 3% | 21% | 61% | 1,990 | ~\$5k | ~3 yr | 4 | High |
| Construction (excavator) | 132,000 | 292,000 | 45% | 72% | unclear | unclear | no data | no data | 2 | Low |
| Agriculture (tractor) | 74,250 | 210,250 | 35% | 74% | unclear | unclear | no data | no data | 2 | Low |
| Artic 30–40t | 27,720 | 189,720 | 15% | 35% | 51% | 14,220 | ~\$200k | ~14 yr | 2 | Medium |
| Vans | 4,538 | 129,838 | 3% | 23% | 59% | 2,662 | \$15–39k | 6–15 yr | 2 | High |
| Rigid >20t | 13,200 | 169,200 | 8% | 22% | 43% | 5,700 | \$70–100k | 12–18 yr | 2 | Medium |
| Rigid ≤8t | 4,752 | 131,752 | 4% | 22% | 48% | 2,277 | \$14–30k | 6–13 yr | 3 | Medium |
| Rigid 8–20t | 7,986 | 147,986 | 5% | 21% | 31% | 2,486 | \$50–80k | >20 yr | 1 | Medium |
| Cab-chassis | 3,240 | 122,540 | 3% | 26% | 31% | 990 | no data | >20 yr | 2 | Low |

*Notes: All labour costs are fully loaded employer costs (base salary + super 11.5% + workers comp + payroll tax + leave loading + relief cover). B-double driver loaded at \$200k/yr; mining operators 2.3 FTE loaded at \$320k/yr; bus driver loaded at \$115k/yr; all other segments loaded at \$110k/yr. Mining fuel is pre-FTC. Mining saving assumes ~70% fuel displacement (conservative; BEV premium 20–30% of \$10M diesel price per Fortescue/Liebherr implied pricing). B-double: 180,000 km/yr (ABS SMVU derived from 20,862 B-doubles × 3.81M tonne-km each), 50 L/100km real-world, diesel \$2.00/L; electric 190 kWh/100km at \$0.15/kWh. All other on-road segments use diesel \$1.80/L (except B-double \$2.00) and electricity \$0.25/kWh. Electric consumption (kWh/100km) from OEM fleet data: buses 100, artic 30–40t 90, rigid >20t 120, rigid 8–20t 100, rigid ≤8t 55, vans 30, utes 25, passenger 15, cab-chassis 50. Payback = BEV capital premium ÷ annual fuel saving (fuel only; maintenance savings not included). NET financial modelling at 200k km/yr confirms: \$220k/yr energy, \$210k/yr driver — consistent with our figures scaled for km.*

---

# How the Economic Score Is Determined

The economic score (1–5) used in the policy scorecard combines two metrics: the **per-km fuel cost saving percentage** and the **simple payback period** (BEV premium ÷ annual fuel saving). The scoring bands:

| Score | Criteria | Segments |
|:-----:|:---------|:---------|
| 5 | Payback ≤6 yr or zero premium; saving ≥47% | Mining, Artic >40t, Passenger, Buses |
| 4 | Payback ≤3 yr but small absolute saving | Utes |
| 3 | Decent saving % but payback ~10 yr; or large absolute saving with uncertain premium | Rigid ≤8t |
| 2 | Payback >15 yr, or no BEV alternative to price | Construction, Agriculture, Vans, Rigid >20t, Artic 30–40t, Cab-chassis |
| 1 | Worst economics: lowest saving % AND longest payback | Rigid 8–20t |

**Revision note:** Mining has been upgraded from 3 to 5 in this analysis. The original score of 3 reflected genuinely unknown BEV premiums for ultra-class haul trucks at the time of the initial scorecard. The Fortescue/Liebherr order (360 BEV trucks at implied ~US\$7.8M per unit, suggesting a premium of ~\$2M over diesel) and fleet-scale Chinese deployment now provide sufficient pricing signal to calculate payback. At pre-FTC fuel costs, mining haul truck electrification pays back in approximately one year — the strongest absolute-dollar economics of any segment.

---

# Key Observations

**1. Fuel share varies enormously — and the relevant metric depends on the question.**

Including the imputed driver, fuel ranges from 2% (passenger) to 62% (mining). This is the true cost structure. But for the electrification decision, **fuel % excluding labour** is more relevant: it shows how much the controllable cost stack changes. Off-road sectors (mining 65%, agriculture 74%, construction 72%) are transformed by electrification; on-road vehicles cluster at 13–43%.

**2. Payback period, not fuel share, determines the economic score.**

Passenger diesel vehicles have the lowest fuel share of any segment (2% including imputed driver, 13% excluding) but score 5/5 on economics because the BEV premium has collapsed to zero. Conversely, agriculture has the highest fuel share (74% excl labour) but scores only 2/5 because no electric alternative exists to price. The score rewards segments where the private sector can act today.

**3. Mining is now clearly the highest-value electrification target.**

At \$2.97M/yr fuel cost per truck (pre-FTC), ~1 year payback, and 9.6 BL of national diesel, mining combines the largest fuel budget, the highest fuel share, and (with modest BEV premiums now observable) compelling payback. The Fuel Tax Credits Scheme (\$0.48/L, costing ~\$4.6B/yr for mining alone) is the single largest policy lever — its reform would accelerate a transition that is already economically rational.

**4. The driver cost dominates on-road vehicle economics.**

For every on-road segment, the imputed \$85k driver cost represents 50–87% of total opex. This has two implications: (a) fuel savings from electrification are a modest share of total fleet costs, and (b) any technology that reduces driver requirements (autonomous trucks, platooning) would transform the cost structure far more than electrification alone. The intersection of autonomy and electrification — as pursued by Fortescue and XCMG in mining — is where the largest economic disruption lies.

**5. Data gaps remain in construction and agriculture.**

Both sectors have large diesel budgets (2.5 BL each) and high fuel shares (49–74% including FTC), but the absence of BEV pricing data makes payback incalculable. These are scored conservatively at 2/5. If electric excavator and tractor pricing follows the trajectory of electric trucks (where premiums have fallen from >100% to 20–30% in five years), both sectors could rapidly become high-priority targets.

---

# Sources

Fuel consumption data: ABS Survey of Motor Vehicle Use, Cat. 9208.0, year ending June 2020 [@abs-smvu-2020]; ATAP vehicle operating cost models; OEM specifications (Cat, Komatsu, John Deere, Fuso, Hino); IEEFA mining diesel report [@ieefa-mining-diesel-2026].

Vehicle pricing: TruckSales.com.au; ConstructionSales.com.au; Farm Machinery Sales; CarsGuide; manufacturer websites (Toyota, Ford, BYD, Mercedes, Volvo, Fuso, KGM).

Operating costs: NTC Heavy Vehicle Operating Cost Model (indicative); Fair Work Award rates (Road Transport, Construction); Transport Workers' Union enterprise bargaining agreements; NHVR registration schedules; RACV/NRMA insurance comparison data.

Electrification economics: etruck_economics.md (this project); diesel_segment_profiles.md (this project); Fortescue Metals Group ASX announcements; ICCT working papers on HDV total cost of ownership.

Policy data: Australia Institute analysis of Fuel Tax Credit claims [@australia-institute-ftc-2024]; AIP terminal gate pricing; ACCC Petroleum Market Report.
