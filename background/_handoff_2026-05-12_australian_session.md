# Handoff: data centres research thread, end of session 2026-05-12

For the next session focused on Australian data centres specifically. Read this first.

---

## What's already built

Six published background notes in `background/`:

| File | What it covers | Headline numbers |
|:-----|:---------------|:-----------------|
| `data_centres_usa.md` | Operating fleet, construction pipeline, demand, fuel sources | ~50 GW operating IT load (FERC 2025); 22-26 GW physically under construction; 17 GW in named mega-campuses; 500-700 TWh by 2030 (12-17% of US electricity); ~74% gas in effective fuel mix |
| `data_centres_community.md` | Local opposition cases, political dimensions | VA voter comfort fell 69% → 35% (WaPo-Schar School Mar 2026); PJM 833% capacity-auction jump; FERC PJM co-location order Dec 2025; "must power itself" coalition Feb 2026 in Australia |
| `data_centres_industry_response.md` | Flexibility, DR, BTM batteries, US vs AU | Norris/Duke 76 GW headroom @ 0.25% curtailment; AWS Apr 2026 9 PPAs in AU (8 with co-located BESS); AEMC Package 2 draft 30 MW threshold; Quinbrook Supernode 780 MW / 3 GWh BESS |
| `training_v_inference.md` | Hardware lineage, utilisation, lifecycle | Llama 3 16K-H100 cluster: 90% effective time, 38-43% MFU; Meta H100 cluster TCO: 71% CapEx / 29% OpEx; depreciation life debate (5-yr central) |
| `token_memory.md` | Decode bandwidth math | tokens/sec ≈ HBM bandwidth ÷ bytes per token; B200 at 8 TB/s on 70B FP8 → ~115 tok/sec/stream; the memory wall explained |
| `datacentre_opex.md` | OpEx structures, US-vs-AU competitiveness | Energy share rises 46% → 73% as utilisation goes 30% → 90%; AU PPA + BESS at US$115/MWh-IT competitive with ERCOT West, cheaper than PJM Dominion (US$178); fixed costs sub-linear at scale (~3.5× for 5× MW); water + depreciation context added |

Underlying research drafts (10+) in `background/_research_drafts/`. Five summary PNGs in `aemo_spot/pngs/`.

## The user's evolving framework (what they care about)

David has been building toward an article (or set of articles) on the **competitiveness of Australian data centres** for AI build-out. The framework that's emerged:

1. **At AI training utilisation (~90%), energy is the dominant cash OpEx** — 73% at 100 MW US, 80%+ at hyperscale.
2. **The right structural play in Australia is renewable PPA + facility-contracted BESS** — not firmed retail. Delivers ~A$95-110/MWh effective vs A$140 for firmed retail. The BESS does double duty: PPA firming + FCAS revenue + facility ride-through.
3. **Australia is competitive against PJM Dominion** (where most US construction is concentrated) and roughly even with ERCOT West Texas. Only beaten by Quincy WA hydro.
4. **The competitive Australian site needs**:
   - Transmission interconnection (the AEMC Package 2 final rule, due mid-2026, matters)
   - PPA + BESS structure (AWS doing this; smaller operators not yet)
   - Avoidance of any future PJM-style capacity-cost socialisation
5. **Limits on the thesis**: GPU depreciation dwarfs OpEx at ~5× cash OpEx, so AU advantage on energy is material for operating margin but small against TCO; talent pool and scale are real constraints; and Australia can't match Quincy hydro economics.

## What's explicitly open / pending

The user has flagged these as future work — pick up in priority order:

1. **Transmission and network charges in detail** — David said "I will get to the transmission and other bits later" when reviewing the per-region electricity price work. The AEMC Package 2 rule (final mid-2026), TUOS/DUOS structures, connection charges, contingent project applications (Wallumatta STS, Macquarie Park substation transformer), AER decisions on incremental connection. This is the next chunk to research.
2. **The economics piece on training v inference** — repeatedly flagged in the Caveats and closing pointers of `training_v_inference.md`, `token_memory.md`, `datacentre_opex.md`. Will combine: the energy share trajectory, the bandwidth math, the workload split, the reasoning compute share, and the per-region pricing into a unified per-token economics analysis. The OpEx work has set up most of the inputs.
3. **Australian regional / state breakdown** — currently treats NEM as one. NSW vs VIC vs QLD vs WA(SWIS) have different price profiles, different network charges, different state policy. Worth disaggregating.
4. **Macquarie Park substation upgrade story** — Wallumatta STS contingent project (AER application Oct 2025), third Macquarie Park transformer commissioned Dec 2025. Could be a useful illustrative case for "what does it cost to add a GW of data centre capacity to existing transmission".
5. **NextDC + OpenAI S7 deep dive** — A$7bn, 550 MW Eastern Creek, Stargate Australia. Major recent commit, partly disclosed; could use a focused project-level note.
6. **AirTrunk competitive position post-Blackstone** — AirTrunk is the largest AU operator (~1.2 GW + when SYD3/MEL2 fully built), now Blackstone-owned, no longer publicly listed. Their PPA portfolio and competitive positioning is partly opaque.

## Workflow patterns that have worked

Captured in `feedback_research_workflow.md` (memory) but worth restating for project continuity:

- **Delegate research to 2-3 parallel general-purpose agents**, each with one slice of the topic. Brief them with explicit Tier 1 / Tier 2 / Tier 3 source-quality requirements, what NOT to do, and what to flag as advocacy vs primary.
- **Drafts land in `background/_research_drafts/<slug>.md`**, then synthesise into `background/<topic>.md`.
- **For contested questions**, two independent methodologies via two parallel agents, then reconcile (the reasoning compute share work is the model — bottom-up 84% vs top-down 60% reconciled to 70-75%).
- **Push back on weak figures** before synthesising — Meta Altoona "1,400 MW IT load" was the canonical case where I pushed back and it turned out to be a master-plan envelope, not energised IT.
- **House conventions**: Australian English in body prose ("centre", "behaviour"); proper-noun terms keep US spelling ("Crane Clean Energy Center"); never use the word "genuine"/"genuinely"; escape standalone $ outside tables (`\$`); table style is bold title above, plain markdown table, italic source below.

## PNG charts produced

In `aemo_spot/pngs/`:

- `dc_fleet_at_a_glance.png` — operating fleet headline numbers (300 DPI)
- `dc_power_source.png` — financing 4-bucket split (47% generic grid)
- `dc_power_fuel.png` — effective fuel mix (74% gas)
- `dc_top_projects.png` — project × tenant matrix + state bar (with stacked Named/Incremental for state breakdown)
- `dc_capex_per_gw.png` — waterfall of cost build-up
- `reasoning_models_lineage.png` — six-lab table of reasoning architecture
- `reasoning_compute_share.png` — bottom-up vs top-down vs reconciled estimates
- `us_opex_by_utilisation.png` — variable energy vs fixed costs at 30/60/90% utilisation, with depreciation memo

If user asks for charts, generation scripts in `/tmp/` (don't survive — reconstruct in chat from existing chart code conventions).

## Things to flag at start of next session

- Confirm with David which of the open items above is the priority (transmission/network is most-explicitly-flagged but the per-token economics piece is also pending and largely set up).
- Check whether the SemiAnalysis Gmail email he mentioned has been imported (we discussed AppleScript or MCP Gmail; he was going to "manage that separately"). Could be substantial source material if so.
- The Wisconsin PSC May 2026 ruling (data centres bear full cost of new generation) is a precedent worth tracking — Australia equivalent would be major.
- The user is a Claude Code Max subscriber and a heavy user of extended thinking; that informed his observation that "the industry is heavily shifting toward inference [reasoning] models". The reasoning-share research started from his lived experience as a power user.

## Calibration notes for the next session

- David has deep NEM expertise; do not over-explain NEM mechanics. Do explain US/global where unfamiliar.
- He pushes back well on weak numbers and methodological shortcuts (he caught the FX-flat conversion of fixed OpEx; the PJM-vs-NEM electricity price discussion). Lean toward exposing methodology rather than presenting numbers as black-box.
- He prefers fewer, sharper tables and bullet lists over long prose. Two-column comparison tables work well.
- He's tolerant of length when the work justifies it but allergic to padding.
- He likes the parallel-agents-then-reconcile pattern when the question is genuinely contested.

---

*End of handoff. Read this, then read `data_centres_usa.md` for the operating-fleet picture if context is needed, then `datacentre_opex.md` §6 for the competitiveness frame the user is building toward.*
