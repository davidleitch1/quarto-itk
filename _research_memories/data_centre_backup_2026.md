---
title: "Research memory — data centre backup architecture (2026-05)"
draft: true
---

# Data centre backup architecture — research memory, May 2026

Worked through this thread over multiple sessions ending 2026-05-14. The work started from the data centre backup angle, expanded into battery economics, then into the transmission cost-allocation question. Outputs span an article, three background research drafts, two synthesis notes, and seven PNG charts.

## Outputs

### Published article

- `posts/data_centre_backup.md` — "The devil's in the detail but godliness is in the top down view"
  - Six-point executive summary at top + ~3,600 word body
  - Six embedded figures with Quarto cross-references
  - Published 2026-05-14

### Synthesis notes

- `background/backup_power_market.md` — synthesis of the three research drafts (market structure, economics, alternatives)
- `background/dc_more_backup_notes.md` — battery revenue, hybrid architectures, transmission socialisation
- `background/Transgrid_upgrade.md` — specific reform proposal for the Sydney West cluster

### Research drafts (in `background/_research_drafts/`)

- `backup_gensets_incumbents.md` — OEM market structure (Cat / Cummins / mtu / Kohler / Generac), lead times, capacity expansions, AU market specifics
- `backup_gensets_economics.md` — technical specs (Cat 3516E, mtu 20V4000, Cummins QSK60), fuel curves, 96-hour sizing, opex build-up, AS 1940 thresholds
- `backup_gensets_alternatives.md` — gas reciprocating, gas turbines, fuel cells, BESS, HVO, hydrogen, microgrid integrators, entry-play analysis

### Charts (in `aemo_spot/pngs/`)

| File | What it shows |
|:-----|:-------------|
| `dc_genset_market_2026.png` | Multi-panel infographic: price trajectory, demand pressure, supply response |
| `dc_genset_hours_us_vs_au_gt.png` | US vs Australia annual genset runtime by category (Great Tables) |
| `dc_backup_configurations.png` | Five backup configurations for a 100 MW site (Great Tables) |
| `sydney_west_backup_costs.png` | Annualised cost vs backup duration, no revenue |
| `sydney_west_backup_costs_with_revenue.png` | Same, with BESS revenue contribution shaded |
| Earlier work: `dc_genset_hours_us_vs_au.png` (plottable version, superseded by Great Tables version) |

Generation scripts saved at `aemo_spot/pngs/scripts/` per the persist-png-scripts convention.

## Headline numbers (verified during this work)

### Capex and opex (per GW of data centre IT load, Australia 2026 prices)

- **Diesel backup capex**: ~A\$2.0-2.9 bn per GW IT (midpoint A\$2.5 bn). Australian-installed at upper end of global range due to transport, fabrication content, AS 1940 compliance.
- **Annual opex**: ~A\$75M/yr per GW IT (~3.2% of installed capex)
- **Diesel inventory held**: ~40 ML per GW IT (96-hour Rated-4 spec)
- **Diesel consumed in routine testing**: ~16 ML/yr per GW IT
- **Diesel consumed in 96-hour tail event**: ~99 ML per event per GW IT

### Sydney West cluster (~800 MW IT, the anchor case)

- ~1,040 MW backed-up load (PUE 1.3)
- Diesel-only capex A\$1.6-2.3 bn, opex A\$60M/yr
- ~32 ML diesel inventory across the cluster
- ~775 standby gensets at 2N+1 redundancy

### Battery (BESS) — Tomago calibration

- **AGL Tomago benchmark (FID July 2025, COD late 2027)**: 500 MW / 2,000 MWh / A\$800M = **A\$0.4M/MWh at 4-hour duration**
- **Power-energy decomposition**: A\$240/kWh (energy: cells, packs, thermal) + A\$640/kW (power: PCS, transformer, switchgear, grid connection)
- **Per-MWh cost by duration** (Australia, 2026): A\$880/kWh @ 1hr; A\$400/kWh @ 4hr; A\$320/kWh @ 8hr; A\$247/kWh @ 96hr
- **Asset life for DC backup duty**: 10-12 years (vs 20-yr grid-scale due to calendar aging at high SOC)
- **Annual opex**: 2-3% of capex

### BESS revenue stack (1,040 MW cluster scale, Mode 2 = 25% reserved for backup, 75% traded)

- **Spot trading**: A\$100/MWh × 250 cycles/yr × tradeable MWh = ~A\$78M/yr (caps at 4-hour duration due to NEM peak-trough window)
- **FCAS**: ~A\$100M/yr (scales with MW power capacity)
- **RERT availability**: ~A\$70M/yr
- **Capacity payments / LTESA-style**: ~A\$30M/yr
- **Total revenue**: A\$240-380M/yr for a 4-hour 1,040 MW BESS at the cluster

### Cost crossover battery vs diesel (cluster scale)

- **Without revenue**: ~1.4 hours (battery cheaper below this duration)
- **With BESS revenue (Mode 2)**: ~11.8 hours
- **Battery is a NET revenue generator** below ~7.6 hours of duration

### Cell-life finding

- **Calendar aging at 90% SOC**: ~3-4%/year capacity fade
- **Cycling 20-80% SOC daily**: ~1.5-2%/year combined fade
- **Counter-intuitive**: active trading actually extends BESS cell life vs pure-backup standby duty

### TIA-942 fuel-storage spec by tier (verified against multiple sources)

| Rated | On-site fuel storage |
|:------|:--------------------|
| Rated-1 | Tank ≥ 80% full |
| Rated-2 | 24 hours |
| Rated-3 | 72 hours |
| Rated-4 | 96 hours |

Uptime Institute Tier IV requires only 12 hours minimum, less prescriptive than TIA-942.

### Uptime targets (corrected during this work)

| Tier | Uptime | Annual downtime |
|:-----|-------:|----------------:|
| Tier III / Rated-3 | 99.982% | ~96 minutes |
| Tier IV / Rated-4 | 99.995% | ~26 minutes |

NOT 99.4% (a number that came up as a mistaken recollection). NOT 99.9+% in the loose sense (the actual spec is 99.995%).

### Sydney West cluster transmission infrastructure (verified)

- TransGrid Sydney West BSP: **330/132 kV** (NOT 500 kV)
- 7 × 330 kV incoming lines (3 from north Bayswater area; 3 from west Mt Piper; 1 from south Bannaby/Yass)
- 600 MVA of 330/132 kV step-down transformer capacity (binding constraint for the cluster)
- 132 kV outgoing feeders: Sydney West → Blacktown; Eastern Creek 2; Sydney West → Wetherill Park; Sydney West → Guilford; Regentville → Sydney West
- 500 kV coming via Sydney Southern Ring → South Creek 500/330/33 kV substation (under construction, in TransGrid RAB)
- DNSP serving the western Sydney DC cluster: **Endeavour Energy** (NOT Ausgrid — Ausgrid covers the Macquarie Park cluster which is separate at ~150-200 MW)

### Australian large-customer connection voltage benchmarks

- Tomago aluminium smelter (~950 MW): 330 kV direct
- Portland aluminium smelter (~535 MW): 500 kV + 220 kV
- Bell Bay aluminium smelter (~190 MW): 220 kV (Tasmanian backbone)
- **Industry convention**: anything ≥ ~150 MW connects at 220 kV or above, NOT 132 kV
- Sydney West cluster (~800 MW aggregate) is an outlier — connected at 132 kV via DNSP rather than direct 330 kV like Tomago

### AU regulatory framework — key dates

- **IESS rule** (Integrating Energy Storage Systems): in force 3 June 2024; bidirectional transition ended 3 March 2025. Creates IRP (Integrated Resource Provider) category for hybrid DC+BESS+diesel facilities to register and bid in markets.
- **AEMC Package 2** (transmission cost-allocation methodology for DC-driven augmentations): final rule due mid-2026.
- **Wallumatta STS contingent project** (Ausgrid, Macquarie Park): A\$162M recovered from four DC customers via cost-reflective tariff; A\$1/yr residential bill impact. The precedent for causal cost-allocation but applies only at DNSP-level augmentation.

## Methodology notes — what was contested / calibrated during the work

- **Battery model started flat at A\$0.4M/MWh** (user pushed back). Corrected to A\$240/kWh + A\$640/kW power-energy decomposition. Crossover moved from 2.5 hr to 1.4 hr without revenue.
- **Diesel opex slope** was missing inventory-scaling components and event-burn fuel cost (user flagged). Corrected to A\$110M fixed + A\$0.27M per backup-hour.
- **Battery cycling extends cell life** (user's intuition, verified against NREL BLAST / Tesla Megapack warranty data). Pure-backup BESS at 90% SOC has 3-4%/yr fade; cycling reduces this to 1.5-2%/yr.
- **96-hour design intent vs actual usage** — Australian DC sites run gensets 10-25 hr/yr (mostly scheduled testing). The 96-hour spec is tail-event insurance, not modal-year sizing.
- **DC connection at 132 kV consumes 330 kV capacity** — even though the formal connection is at sub-transmission voltage, the 330/132 transformer fleet is the binding constraint and the 330 kV bulk transmission is where Sydney Southern Ring expansion sits.
- **TUOS does not allocate causal cost** — DCs pay their TUOS share (~A\$5-15M/yr per 100 MW), but the incremental causal cost of network expansion is in the order of A\$30-60M/yr per 100 MW. Cross-subsidy estimated at A\$200-400M/yr across the Sydney West cluster, paid by residential and small-business customers.

## User preferences expressed during the work

- **Voice**: informal, first-person, conversational; "thought bubbles" framing. Don't over-formalise.
- **AI disclosure**: user wants the "research assisted by Claude" framing kept visible, but disagreed with my proposal to move it out of the numbered list in the article (R5 declined).
- **Tomago contract softening (R3 declined)** — user left the stronger claim about subsidised contract as-is.
- **No conclusion section (R4 declined)** — user preferred the article to end on the cost-allocation summary.
- **Tables**: minimal-border style (top + bottom rules only), Great Tables for standalone research output, plottable for chart-embedded. Use the `save_gt_flexoki_png` helper from `~/.claude/skills/flexoki-plotting/examples/great_tables_minimal.py` to avoid the white-halo bug.
- **Charts**: Flexoki Light theme always. Save scripts to `aemo_spot/pngs/scripts/<name>.py`.
- **"Mode 2" jargon avoided** — user asked to drop the "Mode 2" label from chart footnotes; describe behaviour plainly.
- **Trading margin assumption**: A\$100/MWh × 250 cycles/yr per MWh of capacity (user-supplied).
- **Adjective discipline**: per global CLAUDE.md update during this work — avoid "genuine", "honest", "substantial", "significant", "meaningful", "considerable", "robust", "really", "truly", "clearly", "obviously", "frankly", "simply", "actually". Default to no adjective. Replace with numbers or examples.

## Open questions / pending work

1. **Detailed transmission and network charges piece** — the next research chunk flagged in the 2026-05-12 handoff. The cost-allocation analysis in this work touched on it but didn't go deep.
2. **Per-region (NSW/VIC/QLD/SA/WA) breakdown** — current analysis treats NEM as one. Deer Park (VIC) cluster has different size (~880 MW) and different DNSP (Powercor).
3. **NextDC S7 / OpenAI Stargate AU deep dive** — A\$7bn, 550 MW Eastern Creek, marketed as Tier IV. Pushes Sydney West cluster aggregate above 1 GW.
4. **AirTrunk post-Blackstone competitive position** — opaque since the September 2024 privatisation.
5. **Macquarie Park substation upgrade story** — Wallumatta STS contingent project + third transformer. Worth a separate note as the precedent for DC-driven causal cost allocation.
6. **Vic Feb 2024 storm impact on the Deer Park cluster** — six 500 kV towers fell on Moorabool-Sydenham; the western-Melbourne cluster mostly stayed up but reporting is thin.
7. **AEMO RERT participant list verification** — confirm whether any of the 2024-25 IRR contract holders are DC operators. The provisional finding was no, but worth verifying directly.
8. **TPG Sydney DC outage February 2025** — storm + genset failure. Failure-mode reconstruction could be a case study for the new-entrant service play.
9. **Sydney Southern Ring economics and timeline** — when does South Creek 500/330 energise? What's the bill-impact assessment? How does it interact with DC load growth?
10. **AEMC Package 2 draft determination** — watch for Q3 2026 release. The causal-cost framework proposal is the key.

## Skills and tooling updates during this work

- **`/flexoki-plotting` skill** restructured (lines 312 → 349). Added best-practice table principles (no vertical rules, top+bottom rules only), library-choice guidance (plottable vs Great Tables), and the `save_gt_flexoki_png` helper. Examples moved to `examples/` subdirectory.
- **`/edit` skill** Figure Labels section updated to require source attribution in figure captions (parallel to the table-source convention).
- **Global `~/.claude/CLAUDE.md`** updated with adjective-discipline rule.

## Cross-references

- Previous DC research: `background/data_centres_australia_top10_construction.md` (cluster composition), `background/data_centres_australia_community.md` (political dimensions), `background/datacentre_opex.md` (US vs AU competitiveness)
- Handoff note that this work continues from: `background/_handoff_2026-05-12_australian_session.md`
- Auto-memory MEMORY.md entries that reference this work: data centres research thread (2026-05-12); persist-png-scripts convention; deploy_workflow.md

---

*Cite this file as the entry point for any future work on data centre backup, transmission cost allocation, or BESS revenue stacking in the AU NEM context.*
