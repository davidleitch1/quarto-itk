---
title: "Data centre backup architecture: revenue, hybrid designs and the transmission cost question"
author: "David Leitch"
date: 2026-05-13
categories: ["Demand", "Markets", "Networks"]
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

## Why this note exists

This note continues from `backup_power_market.md` and the three underlying research drafts (`backup_gensets_incumbents.md`, `backup_gensets_economics.md`, `backup_gensets_alternatives.md`). Those documents established the baseline market structure, unit economics and alternative technologies for data centre backup power. This note covers the subsequent analysis: how the picture changes when battery storage is allowed to earn revenue from grid services, how hybrid backup architectures perform, what a centralised single-DC alternative would look like, and how the existing Australian transmission cost-allocation framework affects all of this.

The anchor case throughout is the **~800 MW IT load cluster behind TransGrid's Sydney West Bulk Supply Point** in western Sydney — CDC Eastern Creek EC1-EC6, AirTrunk SYD3 nearby at Huntingwood, Stockland/EdgeConneX Davis Road at Wetherill Park, and adjacencies. Cluster total IT load 800 MW; backed-up load at PUE 1.3 = 1,040 MW.

Two charts produced during this analysis sit at `aemo_spot/pngs/`:

- `sydney_west_backup_costs.png` — cost-only crossover (diesel vs battery, no revenue)
- `sydney_west_backup_costs_with_revenue.png` — with BESS revenue (spot trading + FCAS + RERT + capacity)

---

## 1. Battery revenue opportunities under the IESS framework

The Australian regulatory framework changed materially on 3 June 2024 when the AEMC's Integrating Energy Storage Systems (IESS) rule took effect. Before IESS, bi-directional resources had to register as both a generator and a customer, with separate market interfaces, separate metering, and separate ancillary-services registrations. The IESS rule created the **Integrated Resource Provider (IRP)** category — a single registration for a facility that both generates and consumes electricity, with one bidding interface and one dispatch process.

A data centre with on-site BESS + diesel + load (and potentially solar PV) is technically a hybrid bi-directional facility. Under the IESS framework, the operator can register as an IRP and participate in:

- Spot energy market (charging the BESS when prices are low, discharging when high)
- Frequency Control Ancillary Services (FCAS) — both contingency and regulation services
- Reliability and Emergency Reserve Trader (RERT) availability payments
- Capacity payments where state schemes apply (NSW Long Term Energy Service Agreements)

The administrative cost of multi-revenue-stream participation is now low enough that it warrants serious consideration as a design choice.

### Revenue building blocks for a 1,040 MW BESS

For an 800 MW IT cluster with a 1,040 MW × 4-hour BESS (4,160 MWh of storage), the revenue stack:

**Table 1. BESS revenue components — 800 MW Sydney West cluster, 2026 prices**

| Revenue stream | Annual revenue (A\$M) | Mechanism |
|:---------------|---------------------:|:----------|
| Spot trading | 78-104 | A\$100/MWh margin × 250 cycles/yr × tradeable MWh |
| FCAS (contingency + regulation) | 80-150 | A\$80-150k per MW of PCS power capacity |
| RERT availability | 50-100 | A\$50-100k per MW of PCS power capacity |
| Capacity / LTESA-style payments | 30-50 | A\$30-50k per MW |
| **Combined annual revenue** | **240-400** | |

*Source: AGL Tomago FID 2025 capex (A\$0.4M/MWh installed); Enel X NSW VPP rates (95 MW contracted 2025); AEMO RERT quarterly reports; NSW Government LTESA published rates.*

The spot trading figure rests on two assumptions: A\$100/MWh average margin per cycle, and 250 cycle-days per year. The Hornsdale Power Reserve and Wallgrove Battery published returns suggest both numbers are defensible. The NEM peak-trough window typically accommodates one 4-hour cycle per day, so trading revenue caps at 4 hours of duration — additional MWh beyond 4 hours add no further trading revenue.

FCAS, RERT and capacity payments scale with the BESS's MW of power capacity (the inverter, transformer, switchgear) rather than its MWh of storage. So these revenue streams are fixed at ~A\$160-300M/yr regardless of whether the BESS is sized at 1 hour or 8 hours of duration.

### Modes of operation

Three operating-mode choices, each with different revenue/backup tradeoffs:

**Mode 1 — Pure backup.** BESS held at ~90% SOC continuously, never traded. Revenue: A\$160-300M/yr (FCAS + RERT + capacity, no trading). Backup integrity: 100% — full 4-hour ride-through guaranteed at any moment.

**Mode 2 — Partial trading with reserved backup.** Reserve 25% of MWh capacity at 90% SOC for guaranteed backup; trade the remaining 75%. Revenue: A\$240-380M/yr. Backup integrity: 1-hour guaranteed BESS ride-through + diesel/OCGT for remainder — no degradation of TIA-942 Rated-4 intent.

**Mode 3 — Aggressive trading.** BESS cycles freely 20-80% SOC. If empty at moment of outage, either fire diesel immediately (existing capacity) or accept temporary 20% load drop. Revenue: A\$260-400M/yr. Backup integrity depends on fallback. The economic upside is small (~A\$20-30M/yr above Mode 2) and the SLA risk is large (a single SLA breach can cost A\$50-150M).

**Mode 2 is the realistic default** for any serious operator running customer SLAs. The 25% reservation gives guaranteed 1-hour ride-through while leaving 75% of capacity available for trading.

### The cell-life argument

Lithium-iron-phosphate cells degrade faster under **continuous high-SOC calendar aging** than under **moderate-DoD daily cycling**. Published benchmarks from NREL's BLAST tool and Tesla's Megapack warranty data:

- Mode 1 (90% SOC continuous): ~3-4% capacity fade per year from calendar aging alone
- Mode 3 (20-80% daily cycling): ~1.5-2% combined cycle + calendar fade per year
- Mode 2 (partial cycling, 60-80% SOC bias): intermediate at ~2-2.5% per year

The conclusion is counter-intuitive but solid: **active trading actually extends BESS cell life relative to pure backup mode**. A trading-active BESS has both higher revenue *and* longer useful life. The augmentation reserve component in BESS opex (typically 0.5-1.5% of capex per year) can be tightened under Mode 2 / Mode 3 operation.

---

## 2. The cost-crossover analysis

Under the simplest assumption (battery cost flat at A\$0.4M/MWh × duration, no revenue), the crossover between battery and diesel sits at ~2.7 hours of backup duration. Two refinements substantially change this picture.

### Refinement 1 — battery costs decompose into power + energy

Battery system economics split into:

- **Power-related cost** (inverter, transformer, switchgear, grid connection) — scales with MW of power capacity
- **Energy-related cost** (cells, packs, thermal management, containerisation) — scales with MWh of storage

So the all-in A\$/MWh declines with duration. Calibrated to the AGL Tomago project (500 MW / 2,000 MWh / A\$800M / 4-hour duration / FID July 2025):

- Energy component: ~A\$240/kWh
- Power component: ~A\$640/kW
- Combined per-kWh: A\$240 + A\$640/D where D is duration in hours

For the 1,040 MW cluster BESS this gives a capex of A\$666M + A\$250M × hours, and an annualised cost of **A\$72M + A\$27M × hours per year**. The flat-cost model materially overstated battery economics at long durations and understated them at short durations.

### Refinement 2 — diesel opex scales with backup duration

Inventory-dependent operating costs (fuel polishing, fuel rotation, dangerous-goods compliance overhead) scale with the size of the diesel inventory, which scales with backup duration. Properly decomposed for the 800 MW cluster:

- Fixed opex (inventory-independent): A\$48M/yr
- Variable opex (inventory-scaling): A\$0.125M per hour of backup per year
- Plus expected event-burn fuel (probabilistic, at 1 tail event per 10 years): A\$0.046M per hour of backup per year
- Fixed capex annualised: A\$62M/yr
- Variable capex annualised: A\$0.10M per hour of backup per year

So total diesel annualised cost: **A\$110M + A\$0.27M × hours per year**.

### Crossover without revenue

Setting battery = diesel: 72 + 27h = 110 + 0.27h → **h ≈ 1.4 hours**.

Below 1.4 hours of backup duration, battery is cheaper. Above 1.4 hours, diesel is cheaper. At 96 hours (TIA-942 Rated-4 spec), battery is ~20× diesel.

### Crossover with BESS revenue included

Subtracting Mode 2 revenue (A\$200M/yr power-based + A\$19.5M per tradeable hour, capped at 4 hours):

Battery net cost (Mode 2):
- For h ≤ 4: −128 + 7.5h M/yr
- For h > 4: −206 + 27h M/yr

This is **negative below ~7.6 hours** — meaning the BESS is a net revenue generator. The new crossover with diesel sits at **~11.8 hours of backup duration**.

**Table 2. Annualised cost by backup duration — 800 MW Sydney West cluster**

| Duration | Diesel | Battery gross | Battery net (Mode 2) |
|:---------|-------:|--------------:|---------------------:|
| 1 hr | A\$110M | A\$99M | **−A\$121M** (net revenue) |
| 4 hr | A\$112M | A\$180M | **−A\$98M** (net revenue) |
| 7.6 hr | A\$112M | A\$278M | **A\$0** (zero crossing) |
| 11.8 hr | A\$113M | A\$391M | A\$113M (net crossover) |
| 24 hr | A\$116M | A\$720M | A\$442M |
| 96 hr | A\$136M | A\$2,664M | A\$2,390M |

*Source: Author build-up. AGL Tomago capex; OEM datasheets for diesel; Mode 2 revenue assumptions per Section 1.*

### Sensitivity

- If trading margin is A\$80/MWh (low end of NEM 2024-25 range): crossover shifts to ~10 hours
- If trading margin is A\$150/MWh (high end): crossover shifts to ~15 hours
- If power-based revenue is at the low end (A\$135M instead of A\$200M): crossover shifts to ~9 hours
- If power-based revenue is at the high end (A\$260M): crossover shifts to ~14 hours

The crossover range under reasonable parameter variation: **8-15 hours**. In all cases, the BESS is a net revenue generator below ~7-8 hours, and diesel wins decisively above ~15 hours.

---

## 3. Hybrid backup architectures

The crossover analysis points to a clear architectural conclusion: neither pure-battery nor pure-diesel is optimal. The hybrid that emerges:

- **0 to ~4 hours**: BESS handles ride-through (covers >95% of credible outage events)
- **4 to ~24 hours**: Diesel or gas tail (for events beyond BESS depletion)
- **>24 hours**: Eliminated by a stronger upstream transmission connection (see Section 4)

### Hybrid cost build-up for 800 MW Sydney West cluster

**Table 3. Hybrid architecture capex and revenue — 800 MW Sydney West cluster, 2026 prices**

| Component | Capex (A\$ bn) | Annualised (A\$M/yr) | Revenue (A\$M/yr) |
|:----------|-------------:|--------------------:|------------------:|
| BESS (4-hour, 1,040 MW × 4 hr) | 1.0-1.5 | 108-160 | 240-380 (Mode 2) |
| Diesel (sized to 24-hr tail, vs current 96-hr) | 1.3-1.8 | 95-115 | 0 |
| TransGrid BSP / 330 kV connection upgrade | 0.12-0.27 | 8-18 | 0 |
| **Total hybrid system** | **2.4-3.6** | **211-293** | **240-380** |
| **Net cluster cost (or surplus)** | | | **+A\$50-170M/yr net surplus** |

*Source: Author build-up. BESS per AGL Tomago benchmark; diesel sized to 24 hours rather than 96 hours; transmission upgrade per Section 4.*

Compared to current decentralised diesel-only at A\$120-150M/yr opex with no revenue, the hybrid architecture is **financially better by ~A\$170-300M/yr** while also delivering:

- 75% reduction in metropolitan diesel inventory (32 ML → 8 ML)
- 75% reduction in Scope 1 emissions during tail events
- Lower NOx and particulate exposure for adjacent communities during events
- ~A\$44M of working capital released (vs current diesel inventory)
- Better cell life for the BESS (cycling vs static high-SOC)
- Diversified revenue dependency on grid services markets (FCAS, RERT, spot)

The catch is that the architecture requires coordinated investment by multiple operators or a single centralised facility — which is not how the cluster is structured today.

---

## 4. The centralised single-DC alternative

A useful thought experiment: instead of eight separate operators with eight separate backup fleets, imagine one consolidated 800 MW data centre rented to multiple tenants. The architectural options open up materially.

### The OCGT alternative for tail-event backup

At scale, **open-cycle gas turbines (OCGT) are meaningfully cheaper than distributed diesel** for the tail-event backup role:

- Capex per MW: A\$1,200-1,500/kW (OCGT) vs A\$2,000-2,500/kW (diesel)
- Fuel cost per MWh delivered: ~A\$100/MWh (pipeline gas through 35%-efficient OCGT) vs ~A\$365/MWh (diesel through standby genset)
- Asset life: 30-40 years (OCGT) vs 25 years (diesel)
- Footprint: substantially smaller per MW for one large OCGT than for hundreds of distributed diesels

Trade-offs:

- **Start time**: Industrial heavy-duty OCGT cold start 15-30 minutes; hot standby 5-10 minutes. Fine for a 4-6 hour BESS bridge but inadequate for direct UPS-replacement role.
- **Gas supply risk**: A single 800 MW OCGT depends on continuous gas supply. East coast gas-pipeline pressure events (Black Summer 2019-20, winter cold snaps) could starve the unit. Mitigation: on-site LNG storage as a 24-48 hour backup.
- **Air permits**: NOx and SOx emissions during operation. SCR aftertreatment required. Tier 4-equivalent compliance.
- **Single point of failure**: An 800 MW OCGT undergoing major overhaul leaves a large gap. Better redundancy: 2 × 600 MW units in N+1 (one runner, one full standby) or 3 × 400 MW in 2N.

### Centralised cluster capex build-up

**Table 4. Centralised single-DC backup architecture — 800 MW IT, 2026 prices**

| Component | Capex (A\$M) | Annualised (A\$M/yr) |
|:----------|-------------:|---------------------:|
| BESS (4-6 hour, 1,040 MW PCS) | 1,000-1,500 | 108-160 |
| OCGT tail-event (2 × 600 MW industrial heavy-duty, N+1) | 1,000-1,400 | 30-45 |
| Gas pipeline connection + LNG backup storage | 140-350 | 7-20 |
| 330 kV direct transmission connection to Sydney West | 120-240 | 6-12 |
| Site civils, switchgear, control room, integration | 200-350 | 10-15 |
| **Total centralised facility** | **2,460-3,840** | **161-252** |

*Source: Author build-up using SemiAnalysis "Onsite Gas Deep Dive" Oct 2025 for OCGT pricing; TransGrid TAPR 2023 for connection cost benchmarks; gas-supply contract terms typical of Australian peaker projects.*

Compared to the current decentralised cluster (current diesel + hypothetical BESS retrofit) at ~A\$3.2-4.6 bn capex and A\$290-400M/yr opex, the centralised architecture saves **A\$0.5-1.0 bn capex and A\$130-200M/yr opex**, plus BESS revenue of A\$240-380M/yr.

### Commercial barrier

The technical and economic case is strong. The structural barrier is that the eight (or so) different operators occupying the Sydney West cluster — CDC, AirTrunk, Stockland/EdgeConneX, NEXTDC, Stack and others — do not share infrastructure. They compete with each other and have no commercial mechanism for jointly funding shared backup.

The AEMC IESS framework can technically accommodate a shared facility (it would register as a single IRP serving multiple offtakers). But the operator-level negotiation framework doesn't exist. No precedent for cluster-scale shared backup at GW scale exists in Australia.

The cleanest path to the centralised model: a single operator (or two in close partnership) builds the centralised facility as part of a new ground-up DC campus, with the BESS and OCGT as integrated components rather than separately-procured backup. The Crusoe Abilene + GE Vernova model and the AWS-Talen Susquehanna model in the US are the precedents. **Australia has no equivalent project announced.**

---

## 5. Transmission capacity and the 132 kV constraint

An 800 MW DC load at one site **cannot** be served at 132 kV. The arithmetic: 1,040 MW backed-up load at 0.95 power factor = 1,095 MVA. Typical 132 kV cable circuit rating is 250-400 MVA, so 1,095 MVA needs 3-4 parallel circuits plus N-1 redundancy = 4-5 circuits total. Impractical.

### What Sydney West has today

Sydney West BSP at 200 Old Wallgrove Road, Eastern Creek:

- 330 kV substation (NOT 500 kV)
- Step-out to 132 kV at **600 MVA** of transformer capacity
- Seven incoming 330 kV transmission lines (3 from north — Bayswater area; 3 from west — Mt Piper area; 1 from south — Bannaby/Yass)
- 500 kV transmission runs to Bayswater (the bulk-network hub) but does not terminate at Sydney West today

### What's coming

The **Sydney Southern Ring project** under construction includes a new South Creek substation with 2 × 1,500 MVA 500/330/33 kV transformers and 330 kV connections to Sydney West. This brings 500 kV capacity into the Sydney West area but via South Creek, not directly at the existing Sydney West site.

### The right connection for 800 MW

**Direct 330 kV connection** to Sydney West's 330 kV bus, bypassing the 330/132 step-down entirely:

**Table 5. Connection voltage options for 800 MW DC load**

| Voltage | Per-circuit rating (MVA) | Circuits needed (incl N-1) | Comment |
|:--------|-------------------------:|--------------------------:|:--------|
| 132 kV | 250-400 | 4-5 | Impractical at this scale |
| 220-275 kV | 600-800 | 2-3 | No standard NSW interface |
| **330 kV** | **1,100-1,500** | **2** | Clean N-1; existing TransGrid standard |
| 500 kV | 2,000-3,000 | 1+1 | Oversized for this load |

Connection capex (additional to centralised facility): **A\$120-240M** for two 330 kV cable circuits to the Sydney West bus, on-site 330/22 kV transformers, switchyard, control building, and connection-process costs.

The current decentralised arrangement works because each operator's 100-400 MW connection is small enough for 132 kV via Endeavour Energy's distribution network. **At cluster aggregate level the load is already approaching Sydney West's 600 MVA transformer capacity** — meaning further DC growth in the cluster will require either Sydney Southern Ring completion (planned), additional transformer capacity at Sydney West, or some operators connecting directly at 330 kV.

---

## 6. The transmission cost socialisation question

This is the load-bearing regulatory issue. **Australian data centres are not paying the causal cost of the transmission capacity they consume.** The current framework socialises that cost to all NSW electricity customers.

### How TUOS cost allocation actually works

The cluster's electrical hierarchy clarifies what is shared:

```
330 kV transmission (7 incoming lines, ~5-7 GW aggregate)
     ↓
330 kV bus at Sydney West
     ↓
330/132 kV step-down transformer fleet (600 MVA total — binding constraint)
     ↓
132 kV bus at Sydney West
     ↓
132 kV feeders (Sydney West → Blacktown; Eastern Creek 2; Sydney West → Wetherill Park; Sydney West → Guilford; Regentville)
     ↓
Endeavour Energy / Ausgrid distribution
     ↓
DC customer connection point
```

Every MW the DCs draw flows through every link upward. Although each DC formally connects at 132 kV via Endeavour Energy's network, **they are consuming 330 kV transmission capacity, the 330/132 transformer fleet, and the upstream Bayswater / Mt Piper 330 kV corridors** in proportion to their load.

The 600 MVA transformer fleet is the practical binding constraint. Aggregate cluster load on a backed-up MW basis (800 MW IT × 1.3 PUE = ~1,040 MW) **already exceeds the transformer fleet's nameplate**, which is why TransGrid's Sydney Southern Ring (with South Creek 500/330 kV substation) is partly driven by this growth.

The NEM has two layers of transmission cost recovery:

**1. Connection assets.** Specific kit that physically connects a customer to the network. Paid directly by the customer via a connection contract negotiated with the TNSP. So when CDC at Eastern Creek takes a 132 kV connection via Endeavour Energy, they pay for the Endeavour distribution-side cables and substation.

**2. Shared transmission.** The bulk 330 kV lines, the 600 MVA transformer fleet at Sydney West, the broader regional grid. Costs sit in TransGrid's Regulatory Asset Base (RAB). The AER approves a regulated revenue recovery, and that revenue is collected via Transmission Use of System (TUOS) charges, allocated to customers by a regulatory formula.

The TUOS allocation formula has a locational component (Sydney West has a particular rate), a demand-related component based on coincident peak, and an energy-related component based on MWh consumption. None of these adjust dynamically to causal cost. A data centre that grows to 100 MW continuous load adds to the rate base, but pays TUOS at AER-approved rates that backward-look at RAB rather than forward-look at the marginal cost they are imposing.

### The cross-subsidy in specific terms

For a 100 MW continuous DC load behind Sydney West:

**Table 6. Transmission cost components — who pays vs who causes**

| Cost component | Who pays |
|:---------------|:---------|
| Their own connection cables and substation | DC operator (full causal cost) |
| Their share of TUOS on existing transmission | DC operator (~A\$5-15M/yr at typical AU TUOS × 100 MW × capacity factor × hours) |
| New transformer at Sydney West driven by their connection | Cost-shared with all customers unless flagged as contingent project |
| Reinforcement of upstream 330 kV transmission triggered by aggregate DC load | All NSW load customers via RAB-based revenue |
| Sydney Southern Ring upgrade (500 kV, South Creek substation) | All NSW load customers via RAB-based revenue |
| N-2 redundancy investment driven by DC reliability requirements | All NSW load customers unless explicitly negotiated |

*Source: AER 2023 Electricity Network Performance Report; TransGrid TAPR 2023; AEMC Contingent Project framework documentation.*

The DC operator pays A\$5-15M/yr in TUOS for their 100 MW load. But the marginal cost they impose on the broader system — saturating the 132 kV transformer capacity, driving Sydney Southern Ring investment, requiring redundancy increases at Sydney West — is materially higher. The incremental causal cost might be A\$30-60M/yr per 100 MW of DC load if allocated cleanly.

**Across the 800 MW Sydney West cluster, the cross-subsidy is in the range of A\$200-400M/yr — paid by NSW residential and small-business customers rather than the DC operators.**

### The two existing fixes

**Wallumatta STS contingent project** (Ausgrid, AER application 7 February 2025, updated 31 October 2025). Ausgrid identified that four data centre connection applications at Macquarie Park required a new sub-transmission substation costing A\$162M. Under the AER Contingent Project framework, that A\$162M is being recovered via **cost-reflective tariffs charged to those four DC customers**, not the broader Ausgrid rate base. Residential bill impact: ~A\$1/year. DC customer bill impact: substantial, but specific to those four operators.

This is the model that *would* solve the causal-cost problem at Sydney West if applied broadly. But it's contingent project — has to be triggered by specific named customer connections and their specific augmentation. It doesn't cover broader transmission upgrades driven by aggregate growth. It doesn't cover the existing-capacity utilisation gap.

**The "embedded customer" framework** (used by Tomago Aluminium, large pulp mills) lets a customer connect directly at 330 kV and pay only for their own connection assets plus TUOS. They benefit from the shared network without paying its incremental expansion cost. This works for individual industrial loads but doesn't scale cleanly to clustered DC growth.

### AEMC Package 2 — the policy vehicle

The AEMC's Package 2 transmission cost-allocation work (final rule due mid-2026, per the 2026-05-12 handoff) is the regulatory vehicle for addressing the cross-subsidy. The early consultation papers flagged:

1. The existing demand-allocated framework doesn't reflect rapid-growth concentrated load
2. DC connection applications are saturating regional capacity in ways the framework didn't anticipate
3. A more causation-based allocation methodology is needed

Three plausible landing points for the final rule:

- **Minimal**: extend the contingent-project framework to capture broader regional upgrades. Incremental fix.
- **Moderate**: introduce a "high-growth customer" tariff class that pays a premium on TUOS proportional to incremental causal cost.
- **Comprehensive**: full causal-cost framework where new DC connections pay the marginal expansion cost over their first 10-15 years.

My read is that the AEMC will go moderate-incremental. The comprehensive option faces resistance from DC operators arguing it would deter investment in Australia at a time when global DC capital is flowing into competing markets.

### International comparison

Australia is lagging.

- **PJM's 2024 capacity auction prices jumped 833%** because the demand curve shifted from data centre load growth. Costs are being allocated to all PJM load customers as capacity charges. Residential bills are up US\$200-400/year in Virginia.
- **Wisconsin PSC ruling (May 2026)** explicitly required data centres to bear full cost of new generation triggered by their load. Precedent for Texas, Indiana, Ohio, Georgia.
- **Virginia's "must power itself" coalition** (February 2026) is lobbying for a rule that requires data centres above a threshold to bring their own dedicated generation rather than rely on shared grid capacity.
- **JLARC review of Loudoun County data centre permits** found data centres at 7% of permitted backup capacity on average — suggesting the cross-subsidy issue extends to backup architecture choices, not just transmission.

Australia has no equivalent debate yet. The Boyd inquiry into NSW electricity reliability has touched on it; AEMC Package 2 is moving but slowly.

---

## 7. Putting it together: three architectural options for Sydney West

The analysis converges on three plausible architectures for the cluster, each with different cost / risk / regulatory profiles.

**Table 7. Sydney West cluster — architectural options compared**

| Option | Description | Capex (A\$ bn) | Annual cost (net of revenue) | Diesel inventory (ML) | Status |
|:-------|:------------|-------------:|----------------------------:|--------------------:|:-------|
| **A. Current decentralised diesel** | 8 operators each with 96-hr diesel at 132 kV | 1.6-2.3 | 120-150 (no revenue) | 32 | Status quo |
| **B. Decentralised hybrid (each site BESS + 96-hr diesel)** | 8 operators each with 4-hr BESS + 96-hr diesel | 3.2-4.6 | 290-400 cost, 240-380 revenue → 50-160 net | 32 | Possible per-operator decision; no shared framework needed |
| **C. Centralised facility (one DC, BESS + OCGT)** | Single 800 MW DC with 4-hr BESS + 2 × 600 MW OCGT, 330 kV connection | 2.4-3.8 | 160-250 cost, 240-380 revenue → −20 to +100 net | 0 (gas instead) | Commercially blocked; no shared-operator framework |
| **D. Decentralised hybrid + stronger TransGrid (24-hr spec)** | 8 operators with 4-hr BESS + 24-hr diesel; TransGrid invests in N-2 BSP for 24-hr restoration SLA | 2.7-3.7 | 220-310 cost, 240-380 revenue → −20 to +90 net | 8 | Requires AEMC negotiated-reliability-tier rule |

*Source: Author build-up combining the earlier economics tables.*

The net-cost ranking (after revenue):

1. **Option C (centralised)**: −A\$20M/yr to +A\$100M/yr — best economics, plus zero diesel inventory
2. **Option D (hybrid + stronger BSP)**: −A\$20M/yr to +A\$90M/yr — almost as good as C, requires AEMC framework
3. **Option B (per-operator hybrid)**: +A\$50-160M/yr net — meaningful improvement on status quo, achievable without coordination
4. **Option A (status quo)**: +A\$120-150M/yr net — worst economics, highest diesel inventory

The gap between Option A and Option C / D is **~A\$100-200M/yr of foregone benefit, plus 100% of metropolitan diesel inventory unnecessarily held**. That foregone benefit accumulates over the 25-year facility life to ~A\$3-5 billion of foregone economic value, plus the environmental externalities.

---

## 8. Publishable theses

Three angles that could anchor an article.

### Thesis 1: The IESS rule (June 2024) made BESS-based DC backup revenue accessible — but no Australian operator has acted

The structural enabler (IESS rule, in force since 3 June 2024) is in place. The revenue pool (~A\$240-400M/yr per GW of DC load) is real and accessible. The technology (4-hour LFP BESS at A\$0.4M/MWh) is procurement-ready. The hyperscale operators are aware: AWS Australia's eight-of-nine PPAs with co-located BESS demonstrate the structural awareness. But no Australian DC operator has built a behind-the-meter BESS sized for grid-services revenue. The gap is not technical or regulatory — it's a procurement and corporate-strategy delay.

### Thesis 2: The transmission cost socialisation is a quiet but real cross-subsidy from residential to DC customers

Australian DCs are using ~A\$200-400M/yr of incremental transmission capacity at the Sydney West cluster that is not being charged back to them. The Wallumatta STS contingent project demonstrates that the AER framework *can* do causal allocation; it just hasn't been applied broadly. PJM and Wisconsin have moved more aggressively; Australia is lagging. The AEMC Package 2 work (final rule mid-2026) is the regulatory vehicle but is unlikely to land a comprehensive fix on its current trajectory.

### Thesis 3: The architectural future is centralised BESS + OCGT + stronger transmission, not distributed diesel — but the regulatory framework doesn't allow it

The centralised single-DC architecture (Option C above) is materially cheaper per MW of IT load than the current decentralised model. The technical components (industrial OCGT, 4-hour BESS, 330 kV direct connection) are all proven. The barrier is that the existing eight-operator cluster cannot coordinate a shared infrastructure facility, and the AEMC framework has no mechanism for negotiating a shared-reliability tier. The policy reform required is modest: a "negotiated reliability tier" rule that lets a metropolitan cluster of high-reliability customers buy enhanced TNSP reliability in exchange for a reduced on-site backup obligation, with cost-allocation tied to the avoided incremental investment.

---

## 9. Open questions for further research

- **Specific per-site TNSP system minutes** for TransGrid (Sydney West BSP) and AusNet (Deer Park TS, the Victorian equivalent). AER publishes the annual TNSP performance dataset but the per-supply-point breakdown is in regulatory submissions rather than the headline report.
- **The Vic Feb 2024 storm's actual impact on the Deer Park cluster.** Six 500 kV towers collapsed on the Moorabool-Sydenham line; the western-Melbourne DC cluster (CDC Laverton + Stack Truganina) was at risk but largely stayed up. A fault geometry slightly different would have taken the cluster.
- **NEM RERT participation by data centres.** Worth confirming whether any of the 14 RERT contract holders for 2024-25 are DC operators. AEMO publishes the list. If yes, the cross-subsidy and revenue arguments need refining.
- **The TPG Sydney DC outage of February 2025** — the genset-failure mode in particular is worth a dedicated note. If a 2025 Australian DC genset failure can be properly reconstructed (OEM, failure mode, recovery time), that's exactly the case study the new-entrant service play needs.
- **The Sydney Southern Ring project economics and timeline.** When does the South Creek 500/330 kV substation actually energise? What's the bill-impact assessment? How does it interact with DC load growth?
- **AEMC Package 2 draft determination.** Watch for the draft (expected Q3 2026) and what causal-cost mechanism it proposes.

---

## References

- AGL Energy. *Final Investment Decision on the 500 MW Tomago Battery* (July 2025). [agl.com.au](https://www.agl.com.au/about-agl/news-centre/2025/july/final-investment-decision-on-the-500-mw-tomago-battery)
- AEMC. *Implementing Integrated Energy Storage Systems*. Final determination 2 December 2021. [aemc.gov.au](https://www.aemc.gov.au/rule-changes/implementing-integrated-energy-storage-systems)
- AEMO. *Reliability and Emergency Reserve Trader (RERT) Quarterly Report Q4 2024* (February 2025).
- AER. *Ausgrid Wallumatta STS Contingent Project Application* (7 February 2025; updated 31 October 2025). [aer.gov.au](https://www.aer.gov.au/industry/networks/contingent-projects/ausgrid-increased-customer-demand-requirements-macquarie-park-area-contingent-project)
- AER. *Electricity Network Performance Report 2023*.
- BNEF / Energy-Storage News. *Battery storage system prices continue to fall sharply* (2024).
- CEFC. *Getting the balance right: data centres and the energy transition* (December 2025).
- Enel X Australia. *NSW Virtual Power Plant launch under Electricity Infrastructure Roadmap* (June 2025).
- Energy Consumers Australia. *How data centres are reshaping Australia's energy landscape* (2026).
- Hamilton Locke. *IESS QUEEN! AEMC Clarifies the Implementation of Integrated Energy Storage Systems* (2024).
- JLARC (Joint Legislative Audit and Review Commission, Virginia). *Loudoun County data centre permit and utilisation review* (2025).
- NREL Annual Technology Baseline 2024. *Utility-scale battery storage cost projections*.
- Oxford Economics for AEMO. *Data Centre Energy Demand Final Report* (July 2025).
- SemiAnalysis. *Onsite Gas Deep Dive* (October 2025).
- TransGrid. *Transmission Annual Planning Report 2023*; *Sydney West 330 kV BESS Specifications Engineering Report*.
- Uptime Institute. *Annual Outage Analysis 2025*. [uptimeinstitute.com](https://uptimeinstitute.com/resources/research-and-reports/annual-outage-analysis-2025)

---

*See also: `backup_power_market.md` (synthesis), `_research_drafts/backup_gensets_incumbents.md`, `_research_drafts/backup_gensets_economics.md`, `_research_drafts/backup_gensets_alternatives.md`, `data_centres_australia_top10_construction.md`, `data_centres_australia_community.md`.*

*Charts referenced: `aemo_spot/pngs/sydney_west_backup_costs.png`, `aemo_spot/pngs/sydney_west_backup_costs_with_revenue.png`, `aemo_spot/pngs/dc_genset_hours_us_vs_au_gt.png`, `aemo_spot/pngs/dc_genset_market_2026.png`.*
