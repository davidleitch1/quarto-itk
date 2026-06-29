---
title: "Research memory: Australian diesel use & oil imports (Mar–Apr 2026)"
author: "David Leitch"
date: 2026-06-28
draft: true
---

# Diesel use & oil imports — research thread

**Period:** March–April 2026. **Theme:** Australia's diesel dependence as (1) an energy-security and balance-of-trade problem that electrification can fix, and (2) a diagnostic signal — rising diesel intensity in coal mining as evidence coal has passed peak.

This memory exists mainly to record the **input data sources**, since the analysis hangs off a handful of official statistics and report extracts. All of these can be re-downloaded if lost; the value is knowing which series, which table, and the headline number each one supplied.

---

## Input data — the series that drive everything

| # | Source | What it gives | Key figure(s) | Where to get it again |
|:--|:-------|:--------------|:--------------|:----------------------|
| 1 | **DCCEEW — Australian Petroleum Statistics** | National diesel sales (the top-line consumption number) | Total diesel sales **33,508 ML in 2025** (up from ~30,000 ML in 2022) | energy.gov.au/publications/australian-petroleum-statistics — monthly extract; used Jan 2026 extract |
| 2 | **ABS — Survey of Motor Vehicle Use (Cat. 9208.0)**, yr ended 30 Jun 2020 | On-road diesel split by vehicle type (the *only* authoritative on-road breakdown — survey since **discontinued**) | Road transport fuel 33,019 ML (49.0% petrol / 49.1% diesel). Diesel: trucks 7,465 ML, LCV 5,014 ML, passenger 3,128 ML, buses 530 ML. Data file `92080DO001_202006.xls` | abs.gov.au — Survey of Motor Vehicle Use, latest release. **Note: final edition, not updated since 2020** |
| 3 | **IEEFA — "Cutting Australian mining's diesel emissions"** (Andrew Gorringe, Jan 2026) | Mining (off-road) diesel + the coal-intensity trend | Mining **9.6 BL FY2023-24**, 22 Mt CO₂-e. Coal 48%, iron ore 26%, other 26%. **Coal diesel intensity +50%** FY2010-11→FY2023-24 (iron ore +6%). Built on NGER data | ieefa.org/resources/cutting-australian-minings-diesel-emissions |
| 4 | **DCCEEW — Australian Energy Statistics 2025, Table F** (Energy Consumption by Industry & Fuel) | Cross-check on mining/agriculture diesel in PJ | FY2023-24 mining diesel **299.6 PJ** (coal 151.4, oil&gas 2.8, other 145.4). Agriculture diesel 88.8 PJ | energy.gov.au/energy-data/australian-energy-statistics/energy-consumption |
| 5 | **The Australia Institute — Fuel Tax Credit & fossil fuel subsidies** (R. Campbell, 2024) | FTC rebate by sector → off-road diesel allocation + the "kill the rebate" policy lever | FY2022-23 FTC **$7.8 bn total**; mining **$3.5 bn (45%)**; agriculture/forestry/fishing $1.3 bn | australiainstitute.org.au (P1481) |
| 6 | **Climate Change Authority — Sector Pathways Review: Transport** (2024) | Transport emissions split (the 90 Mt framing) | Transport **90 Mt CO₂-e (21% of national)** 2022. Cars 38 Mt (42%), LCV 17 Mt, heavy trucks+buses 22 Mt (rigid 8.7 / artic 11.7 / bus 1.6). 23% of trucks >21 yrs; 90% of operators small business | climatechangeauthority.gov.au/publications/sector-pathways-review |
| 7 | **ACAPMA / ATSE** | Qualitative framing — ~60% of liquid fuel is diesel, ~40% of diesel is non-transport; key diesel sectors | — | acapmag.com.au; atse.org.au decarbonising-diesel-industries |
| 8 | **renewables.ninja** (Pfenninger & Staffell) | Pilbara wind profile for the Fortescue model | Port Hedland Vestas V162 6MW @120m, annual CF **36.1%** (Jun 50% / Feb 29%) | renewables.ninja — MERRA-2 reanalysis |

Bibliographies holding full entries: `background/diesel_electrification_references.bib` (master, ~60 entries incl. all truck-OEM / charging-standard / mining-equipment sources) and `posts/diesel_to_electricity.bib` (subset for the flagship post).

---

## Published outputs

**Posts (`posts/`, published):**
- `Diesel_to_electricity.md` (2026-03-22) — flagship. Full fleet electrification redirects **~$22 bn/yr from petroleum imports to domestic electricity** (~1% of GDP import substitution), cuts **~90 Mt CO₂ (~15% of emissions)**, ~$15 bn welfare at AER $176/t. Priorities: long-haul trucking, mining (end diesel rebate), diesel passenger cars. Image: `media/diesel_policy_scorecard_table.png`.
- `Diesel_symptom.md` (2026-04-28) — "Diesel consumption reveals the malaise in coal." Diesel/tonne of coal +50% vs +6% iron ore ⇒ coal past peak, rising cost.
- `Longhaul.md` (2026-03-06) — Sydney–Melbourne road freight: 2–4 yr payback, ~$0.9 bn/yr fuel savings, ~$2.5 bn incremental capex. ~22 Mt freight, ~1.2 bn freight-km.
- `Twiggy.md` (2026-04-13) — Fortescue Pilbara electrification: ~16% pretax IRR, trucks carry it, battery-swap beats in-truck batteries.
- `Freight_forward.md` (2026-03-31) — Smart Energy/Boundless conference reportage.
- `tesla_semi.md` (2026-03-23) — Tesla Semi real-world performance/pricing.

**Background notes (`background/`, mostly `draft: true`):**
`diesel_electrification.md` (where diesel goes), `diesel_segment_profiles.md` (12-segment appendix), `diesel_economics.md` (TCO by segment — fuel share 2% passenger → 62% mining haul), `etruck_economics.md` (per-km consumption & diesel→kWh ratios), `diesel_in_mining.md`, `Fortescue_diesel_replacement.md` (~$1.1 bn/yr savings, 5–6 yr payback), plus FTC, swap-vs-CCS, iron-bridge-magnetite notes.

---

## Methodology notes

- **National total** comes from Petroleum Statistics (#1). **On-road split** from ABS SMVU (#2) — but that survey ended in 2020, so the split is scaled to the current national total rather than re-measured. **Off-road (mining/ag)** built from IEEFA (#3) + FTC claims (#5), cross-checked against Energy Statistics Table F (#4).
- **13/12-segment scorecard** is the analytical spine: each segment scored on diesel volume, economics (fuel share of TCO), and security/strategic value → bubble chart + policy scorecard.
- **$22 bn import-substitution** figure = full diesel volume × import price, framed as balance-of-trade. The oil-imports angle is woven through (import dependence, "crisis diesel price" scenarios sharply improve paybacks) rather than a standalone piece.
- Fortescue model uses two capex sets (aggressive Chinese-supplier pricing vs conservative); headline IRR uses conservative; Pilbara wind CF from renewables.ninja (#8).

---

## Open questions / follow-ups

- No dedicated oil-imports/energy-security standalone piece — the import-dependence and liquid-fuel-security argument could be developed further (IEA 90-day reserve obligation, refinery closures, single-source supply chains).
- ABS SMVU discontinuation (#2) leaves the on-road split increasingly stale — watch for any replacement series.
- Diesel passenger-car segment flagged as low-effort win (NVES + FBT levers already exist) but not deeply costed.

---

## Synthesis extension (June 2026): trade-flow comparison

Added a synthesis comparing Australia's big export earners against the oil import bill, framed as net trade balances. **Chart:** `media/trade_flows_net.png` — Flexoki diverging stacked bar. **Script:** `scripts/trade_flows_net.py`. **Raw data:** `scripts/data/abs_merch_{imp,exp}_may25_apr26.csv`.

### Headline net positions (A$bn, trailing 12 months)

| Flow | Net | Detail |
|:-----|----:|:-------|
| Coal | **+64.2** | SITC 32; imports ~0 |
| Gas (LNG) | **+58.1** | SITC 34 (343 LNG +56.4, 342 LPG +1.7); imports ~0 |
| Tourism — education | **+54.7** | credits 55.1, debits 0.4 |
| Tourism — personal ex-education | **−43.2** | credits 25.7, debits 68.8 (deficit; Australians out-spend inbound) |
| Oil (petroleum, SITC 33) | **−45.0** | imports 59.1, exports 14.1 |
| ↳ crude (333) | +0.9 | imp 7.8 / exp 8.8 — roughly net-neutral |
| ↳ refined products (334) | **−44.8** | imp 50.1 / exp 5.3 — the whole deficit |
| ↳ other petroleum (335) | −1.2 | |

**Key finding:** the entire oil deficit is **refined-product imports**; crude is net-neutral. Coal, gas and education are now within ~$10bn of each other ($64 / $58 / $55bn). Diesel alone (~−$28.5bn est.) is the single largest slice of the oil import bill.

### Data access — how to refresh (IMPORTANT, reproducible)

Goods (coal/gas/oil) by SITC come from the ABS SDMX API dataflows **`MERCH_IMP`** / **`MERCH_EXP`** (these go to 3-digit SITC; dimension order `COMMODITY_SITC.COUNTRY.STATE.FREQ`, `TOT`=total, `M`=monthly; OBS_VALUE in thousands AUD, UNIT_MULT=3). The `Accept` header is essential — without it you get XML:
```bash
curl -H "Accept: application/vnd.sdmx.data+csv" \
  "https://data.api.abs.gov.au/rest/data/ABS,MERCH_IMP,1.0.0/.TOT..M?startPeriod=2025-05&endPeriod=2026-04" -o merch_imp.csv
curl -H "Accept: application/vnd.sdmx.data+csv" \
  "https://data.api.abs.gov.au/rest/data/ABS,MERCH_EXP,1.0.0/.TOT..M?startPeriod=2025-05&endPeriod=2026-04" -o merch_exp.csv
```
Tourism (travel) is quarterly from ABS BoP cat. 5302.0 Tables 8/9 (see input-data table above).

**4-digit limitation:** neither the ABS open cube nor DFAT pivot tables publish diesel (SITC 3344) vs petrol (3342) in dollars — they stop at "refined products" (334) as one lump. The diesel/petrol split in the chart is **estimated** by applying US EIA Australia Country Analysis Brief (Dec 2025, 2024 data) import-VOLUME shares — diesel/gasoil 57%, petrol 25%, jet 13%, other 5% — to the ABS refined-import VALUE; "other" is the residual so the bar sums to the exact −45.0. To get exact 4-digit dollars would need a custom ABS data request or DCCEEW APS value data.

**Petroleum import spike:** Mar–Apr 2026 petroleum imports jumped (Apr ~$9.2bn vs ~$4.5bn run-rate) — this is the **Hormuz crisis** price/volume shock (real, not an artefact). It lifts the net oil deficit from a ~−$36bn run-rate to the reported −$45.0bn.

## Diesel sub-sector breakdown — mining reconciliation (settled Apr 2026)

Chart `media/diesel_by_subsector.png` (script `scripts/diesel_by_subsector.py`), trailing diesel by sub-sector.

**Key rule: mining diesel = 7.8 BL, NOT 9.6 BL.** IEEFA's 9.6 BL is the *industry / Energy-Accounts* basis (counts a mining company's own transport, on-site generation and mine construction). AES Table F *activity* basis reallocates those out → core extraction/processing = 299.6 PJ = **7.8 BL**. Combining 9.6 with the SMVU road split **double-counts** mining transport. Settled in email thread with IEEFA's Andrew Gorringe (Fastmail "Finding source for a chart", 16 Apr 2026).

Agreed segments (BL/yr): mining 7.8 (coal/iron/other = IEEFA 48/26/26 → 3.7/2.0/2.0); road 16.0 (B-doubles 4.0 + all other 12.0, SMVU FY19-20); construction 2.5 (kept vs AES 0.7 — gap is equipment-hire firms, not road trucks); agriculture 2.3; rail 1.3; utilities/commercial/mfg 2.3. Total ~32.2 BL (AES basis) vs APS sales 33.5 BL (sales-vs-consumption + vintage).

## Related
- See `_research_memories/data_centre_backup_2026.md` — overlaps on diesel gensets and Fortescue/battery-swap.
