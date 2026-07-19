---
title: "SpaceX and the Emperor's new clothes"
author: "David Leitch"
date: 2026-07-17
categories: ["Demand", "Investment"]
image: "../media/bank_ai_value_vs_peers-4251337.png"
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

## SpaceX AI valuations - abundant optimism

In this note I build a first pass cashflow model of orbital data centres as proposed by SpaceX. It finds they are unlikely to have a positive NPV: even with generous discounts the model needs an achieved price of about US$11.30 per watt-year against roughly US$8.50 achievable. I tested a wide range of sensitivities in coming to that conclusion. The note includes an explainer and a glossary for this new business. It could be a winner, but it's one where demand for AI continues to grow incredibly fast, improvements in space technology happen at an unlikely pace, and the apparent revenue disadvantages of orbital data centres disappear. 

As part of the process I also considered the value of SpaceX's AI business in the context of [how four leading investment banks have valued it](https://itkservices3.com/background/bank_ai_valuation.html). I backed out an estimate of the value the banks assign to the terrestrial business to derive the implied value they attribute to the orbital business.

I also compare the investment bank business value of the terrestrial AI with valuations of Anthropic, OpenAI and CoreWeave. In 2026 SpaceX's AI revenue is essentially data centre rentals on three month cancellable leases. Clearly if that were all it was it would likely be less valuable than CoreWeave because although it gets higher prices, the 90 day cancellation clause is a value killer.

In order to form an opinion of how likely SpaceX's Grok model is to be a significant revenue earner I did some last-minute checking of how Grok is rated and how other competitors, particularly Chinese models, are doing. I find that the USA models are all losing significant market share at the low end and that trust (hallucination rate and confidence in developer) is the key at the high-revenue end of the market. Grok arguably will need to improve on the trust score if it is to seriously compete in the upper end. Competing with the Chinese models on price at the commodity end of the market doesn't generally end well for Western firms. 

## Methods

The design, ordering, overall responsibility and most of the drafting is by me. Identification of satellite technical issues , glossary drafting, building of the cashflow table is done by Claude (fable). What is in the note is essentially my ideas, the images were built by Claude to my specifications. As usual,  strong statements have been checked by me. Supporting and triangulation data and facts have been requested wherever they seem needed. Numbers have been disaggregated for my benefit but mostly collected by Claude. In short I am the researcher, Claude is the assistant and data gatherer. The process is little different to when I was head of Australian utilities and building materials research at UBS Australia, except that Claude works faster and pushes back less than the very able hard working teams I headed up. In my opinion the quality of the work is superior to what I used to do, except that, not marketing it, I don't have the benefit of fund managers or competing analysts offering alternative and often better "takes".

## Investment banking initiations on SpaceX

Claude and I reviewed the initiation reports on SpaceX by 4 leading global investment banks. The four reports between them totalled about 390 pages compiled by 21 named analysts.

Claude counted 20 pages out of the 390 that discussed orbital data centres. Not one report valued them explicitly. The terrestrial AI value implied by the banks' own models — their 2028/29 forecast operating income excluding orbital, valued at roughly a 20× comparator multiple — works out at about US\$0.7–1.0 trillion. Two market-based cross-checks land far lower: applying OpenAI's and Anthropic's own revenue multiples to the segment's current revenue gives roughly US\$270–420 billion, and the listed pure-play comparator (CoreWeave, at ~2.4× enterprise value to revenue) prices the actual hosting business near US\$70 billion. After all the vast majority of the revenue in the terrestrial AI businesses consists of leasing data centres, and those leases are cancellable on 90 days notice. Despite the cancellation, and despite the fact that Grok barely registers in the enterprise API market where the high-quality revenue is, I estimate the terrestrial business is valued by the investment banks at 67× 2026 revenue.

**Table: the pure-play comparator — CoreWeave vs SpaceX's hosting business**

|                | CoreWeave                                                    | SpaceX hosting business                                      |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Business       | Buys market-priced GPUs, houses them, rents the capacity to AI labs | The same                                                     |
| Revenue        | $31–35bn FY2026 guidance                                     | ~$28bn run-rate (mid-2026)                                   |
| Customers      | Microsoft, OpenAI, Meta-backed deals                         | Anthropic, Google, Reflection AI                             |
| Contracts      | Multi-year take-or-pay, ~4–5 yr weighted; Nvidia $6.3bn purchase backstop to 2032 | Cancellable by either party on 90 days' notice from January 2027 |
| Unit price     | ~$10–13/W-yr                                                 | ~$29–50/W-yr (scarcity rates)                                |
| Market pricing | ~$80bn enterprise value ≈ 2.4× revenue (incl. $35bn debt and leases) | At the same 2.4× → ~$68bn enterprise value                   |

*CoreWeave owns no AI model — and neither does the hosting revenue being compared. Grok, the model business (~$4bn revenue), is valued separately at a model-owner multiple (~21×, Anthropic's own mark), adding ~$60–100bn. Sum of the parts ≈ US$130–170bn, against the banks' US$1.7–2.4tn AI segment. Note the asymmetry runs one way: CoreWeave's 2.4× is earned on committed multi-year revenue; SpaceX's book is 90-day paper at two to five times the unit price.*

However that egregious overstatement is as nothing compared to the implied valuation of the space data centres at around US\$1 trillion to US$1.4 trillion. Claude and I obtained those numbers by backing out a terrestrial valuation from the investment banks AI segment. It's easier to see in the associated figure. The figure shows three of the four banks: the fourth's sum-of-the-parts valuation does not separate its AI segment, so no terrestrial value can be backed out of it.

![Implied value of SpaceX orbital data centres backed out of investment-bank AI segment valuations, compared with terrestrial peers. Source: ITK analysis of bank initiation reports, Jul 26](../media/bank_ai_value_vs_peers-4251337.png){#fig-bank-ai-value}

So to put this starkly the investment banks implicitly valued at \$1 trillion a business that has never earned \$1 of revenue, which does not exist other than on SpaceX marketing documents and which has well defined technical hurdles and probable pricing issues. The valuation was not explicit, for what seems to me obvious reasons. Not only was the valuation hidden away within the overall AI segment, but only 20 pages out of 390 were devoted to discussing the concept even though the implied orbital valuation is something like 30–40% of the overall SpaceX enterprise values behind the banks' price targets.

And indeed the "greater fool than thou" theory of share trading is well proven in markets. Over time cash flow fundamentals inevitably come to the fore but there can be heaps of trading along the way. SpaceX traded up on IPO. Giddy up.



## Orbital data centre concept

Since I know nothing about trading, and apparently very little about SpaceX, the remainder of this note is devoted to building a cash flow model of orbital data centres. 

This table uses only one set of ground equipment so it ignores all the hype around the SpaceX 75 GW deployed. In fact I look at a 10 GW model, and the usable number is less due to breakage.

As we get into the discussion the key points are these. The focus is on how much computing power a satellite can hold (specific power per tonne). The limiting factor right now is the heat radiator. There is a pathway to more than 71 kW/t, but it doesn't do much for the cash flow, because chips make up the bulk of the capex and have to be replaced every five years — broadly how long a satellite lasts. As compared with a terrestrial data centre there is no market for old chips because the satellite is destroyed (with its environmental consequences).

![Cashflow model of a 10 GW orbital data-centre fleet. Source: ITK model, Jul 26](../media/orbital_model_table.png){#fig-orbital-model}

An orbital data centre is not a building in space. It is a fleet of satellites, each one roughly a single server rack: SpaceX's disclosed "AI1" design is a 2.1-tonne satellite drawing 120 kW average (150 kW peak) of compute power — about one Nvidia GB300 rack — with a 600 m² solar array, a 110 m² pumped-liquid radiator, and laser links tying hundreds of thousands of such satellites into one distributed cluster. The end-to-end process runs: buy chips, build satellites, launch, operate for about five years, burn up, replace. Each step has its own industrial chain, described below.

**Chips.** The process starts where a terrestrial data centre starts: buying Nvidia-class accelerators at market prices — the same GB300-class silicon, at roughly $31 of the ~$40 per watt an AI1 satellite costs. SpaceX has announced Terafab, a captive chip plant in Grimes County, Texas (a joint project with Tesla and xAI, using Intel's 14A process), intended eventually to supply its own accelerators below market price. The contracted commitment so far is $5bn of a $119bn announcement, exit-able on 90 days' notice, and first production silicon is unlikely before 2030–31 — so for planning purposes the chips are market-sourced for the rest of this decade.

**Satellites.** Chips, solar arrays, radiators and the satellite bus are assembled at plants built on the Starlink production model. Current Starlink output is roughly 3,000 satellites a year; the bank projections require of the order of 100,000 a year, so satellite manufacture is itself a major new industrial facility. Finished satellites are flat-packed 47–48 to a Starship — one launch carries ~7 MW of computing.

**Launch.** Starship is a two-stage vehicle. The booster flies back to the launch tower, is caught and reused many times; the "ship" (second stage) carries the satellites to orbit and is expected to fly about 17 times over its life — at the flight rates the projections require, that is a few months of service, so ships are consumables built at dedicated factories ("Gigabays", Texas and Florida, each planned for up to 1,000 ships a year). Each satellite flies once. Launch pads today are Starbase in South Texas and the Cape Canaveral/Kennedy complex in Florida, with regulatory approval currently capped at 145 launches a year across all sites; the dawn-dusk orbit the design depends on requires near-due-south launch corridors, traditionally flown from Vandenberg in California, so polar-capable pads are part of the build-out.

**Fuel.** Each launch burns ~5,250 tonnes of propellant: ~1,150 t of liquid methane (natural gas, liquefied at the pad) and ~4,100 t of liquid oxygen, separated from air at plants co-located with the launch sites. At a right-sized ~300 flights a year this is one large air-separation unit and a modest gas supply — a normal industrial project. At the banks' projected ~4,800 flights a year it becomes ~20% of world industrial oxygen production and the gas throughput of a mid-sized LNG train, with ~1.6 GW of continuous electric load for liquefaction.

**Operations.** In orbit each satellite unfolds to a ~70-metre wingspan — wider than a 747 — deploying the solar wing and the radiator, which stands as a vertical blade edge-on to the sun so both faces radiate to cold space. The satellites fly in dawn-dusk sun-synchronous orbit, riding the day/night boundary so the panels see sunlight more than 90% of the time. Laser links mesh the fleet into one distributed cluster; ground gateway stations connect it to the terrestrial internet; customers buy the computing the way they buy cloud capacity today.

**End of life.** There is no servicing — a failed satellite stays failed, and delivered capacity decays over each satellite's life. At the end of the ~5-year design life the satellite is steered down and burns up on re-entry, and a replacement cohort carrying that year's chips is launched. The fleet is therefore a rolling procurement programme, not a build-once asset: whatever the fleet costs, roughly a fifth of it is re-bought every year, forever.

## Energy is a red herring for orbital data centres

The pitch is that orbit deletes the things that make terrestrial data centres slow and contentious to build — land, permits, grid connections, cooling water, electricity bills — and replaces them with solar power that needs no planning approval. Roughly 47 satellites fit on one Starship, so one launch delivers ~7 MW of compute. 

But land and electricity are second-order problems with data centres. Today the problem with data centres is obtaining and financing the GPUs and associated memory. Orbital satellites increase capex costs, result in a slightly lower capability data centre due to slower communications between the satellites and provide no upside optionality. And that's assuming everything works the way SpaceX proposes. For SpaceX investors the questions are: Will it work? Will it be on time? What's its value?

The challenges fall into two main areas — technical and economic — and of course they interact. On the technical side the issue that gets the most attention is heat rejection. On the economics the issues are around lack of terminal value optionality, the need to replace failures, and the fact that orbital data centres will mostly deal with batch requests, e.g. deep research. Terrestrial data centre customers already pay discounted rates for batch work. Those economic issues go to long term profitability. If this were a note about SpaceX valuation I would simply point to the timeline. It's absurdly, in my opinion, unrealistic. . 

Among the many categories of things unlikely to be achieved is building Terafab on time and having it produce with the same quality as TSMC. Without Terafab just getting hold of the modelled GPUs will be difficult. Indeed at the grandiose scale SpaceX and its army of investment banking acolytes project. the RAM will be even more of a constraint than the GPUs.

The constraint ordering is: memory first, GPUs second, energy third. High-bandwidth memory (HBM) is DRAM, and DRAM is an industry whose wafer capacity has been roughly flat for fifteen years — all the growth came from shrinking the circuits, and a three-firm oligopoly has held factory discipline since 2012. HBM breaks that model: it uses roughly three times the wafer area per bit of ordinary memory, so it already consumes ~18% of the world's DRAM wafers while supplying only ~7% of the bits — which is why memory prices are rising now, at today's moderate rate of GPU growth. On my capacity modelling, the central AI growth path to 2031 requires the first doubling of the world DRAM wafer base since the 2000s, roughly US$150–250 billion of new memory fabs from incumbents whose combined capital spending is US$60–70 billion a year across all products. GPUs bind second: leading-edge AI wafer starts need to grow about 30% a year — the current crisis pace, sustained for another four years. Energy binds third and latest. Terafab is a logic plant and does not touch memory at all — if anything, cheaper logic chips would add to HBM demand; and orbital data centres make the silicon problem worse rather than better, because destroyed satellites support no second-hand chip market and unrepairable failures mean flying 20–40% more chips for the same delivered capacity.

There are many things to discuss but at the scale proposed 20 Mt of liquid oxygen a year is required. That itself requires 1.6 GW of power. Perhaps more important — and the issue has yet to gain visibility — is the damage to the environment. Satellites burn up after their five year life and that burn up creates alumina which then collects in the atmosphere. I have no view on the significance of this but I am not generally a fan of fiddling with the atmosphere.

The scale proposed is not incremental. The July 2026 bank initiations project 40–75GW of orbital compute by 2031 (175,000–390,000 satellites; the entire North American data-centre industry added ~12GW in 2025), requiring 5,600–9,400 Starship launches — a vehicle that has not yet re-flown a second stage.

**Table: the proposed fleet vs everything in orbit today**

| Measure               |                          Today, all purposes (mid-2026) | Proposed AI fleet (2030–31) |
| :-------------------- | ------------------------------------------------------: | --------------------------: |
| Active satellites     |                              ~15,000 (Starlink ~10,700) |    175,000–387,000 (12–26×) |
| Mass in orbit         | ~16,600 t — every human object since 1957, incl. debris |  370,000–810,000 t (22–49×) |
| Launched in peak year |                                 ~3,000 t (2025, record) |           ~480,000 t (2031) |

*Sources: ESA space environment statistics; SatFleet/Orbital Radar satellite counts; bank extracts; ITK arithmetic.*

Humanity has launched roughly 20,000–25,000 satellites in 68 years; the 2031 build year alone launches ~227,000 — about ten times all of history in twelve months, nearly all of it into one narrow orbital family (dawn-dusk sun-synchronous), where conjunction rates scale with the square of density. 



## What you have to believe

An orbital data centre does appear to be technically achievable. However, the economics are questionable. The following table compares assumptions that the investment banks appear to have made, with what's been achieved and what may be achievable.



![Assumption stack: bank assumptions vs achieved and achievable. Source: ITK analysis, Jul 26](../media/assumption_stack-4257681.png){#fig-assumption-stack}

The table doesn't cover some of the challenges. For instance the economics assume Starship's second stage (the "ship" that carries the satellites) returns to Earth, is caught at the launch tower, reloaded and relaunched about 17 times over its life. To date a ship has been caught once and has never been re-flown. Separately, regulatory approvals currently cap Starship at 145 launches a year across all sites, against the thousands per year the projections require.



The figure bridges from the banks' revenue assumption to what the observable market discounts imply.

![Bridge from bank assumptions to ITK base case. Source: ITK analysis, Jul 26](../media/orbital_bank_bridge.png){#fig-bank-bridge}



The concept is technically achievable: nothing in it breaches physics, a startup has already run an Nvidia H100 in orbit, and radiation testing has substantially cleared the chips. At the right-sized scale of my model — roughly 10 GW from one set of ground infrastructure — the supply-side objections largely dissolve: one or two launch pads, about 300 flights a year, one air-separation plant, and silicon demand within industry capability. SpaceX's execution record also deserves respect: Starlink went from nothing to ~10,700 working satellites and cut launch costs by ~85%, against near-universal scepticism at the outset. And there is a world in which the economics work: if terrestrial compute scarcity persists into the 2030s — because chips, memory and grid connections stay short — capacity prices hold near today's levels rather than normalising, and interactive-grade service can be proven from orbit then above WACC can be earned

That is the bet  not on physics, but on a decade of scarcity pricing plus near-flawless engineering delivery on a first-of-a-kind machine. On my capacity modelling the scarcity world is about one scenario in three.

## The problems, ranked

Orbital data centres face several constraints which are ranked here by my perceived order of significance. Two get expanded treatment because they are unfamiliar: getting rid of heat (#1, the most consequential for the engineering) and the environmental ledger (#6, the most exposed to accumulating science).

### 1. Heat rejection — the binding technical constraint

**Problem.** Essentially every watt of electricity a computer chip draws becomes heat, and the heat must go somewhere or the chip cooks. On Earth, data centres shed it with air and water — fans, chillers, cooling towers. In vacuum there is no air and no water: the only way heat leaves a satellite is by *radiating* it from a surface, the way a bar heater glows. The rate a panel can radiate therefore caps how much computing a satellite can carry, in the same way a grid connection caps a terrestrial data centre.

**The physics.** Radiated power rises steeply with the radiator's temperature (with its fourth power), so hot radiators can be small and cool radiators must be enormous. But heat only flows downhill — the radiator must stay cooler than the chips it serves — and the chips have a temperature ceiling. The designer is squeezed from both ends: run the radiator hot to keep it small, and you spend the operating headroom the chips need; run it cool, and the panel grows until it dominates the satellite.

**The spec versus the record.** SpaceX's disclosed AI1 satellite promises 150 kW of computing cooled by a 110 m² radiator — about 1,360 watts shed per square metre of panel. That is ~680 W/m² per face. Against that:

| Benchmark                                    |       W/m² | Status                                 |
| :------------------------------------------- | ---------: | :------------------------------------- |
| Simple passive panels (Redwire baseline)     |       ~250 | Engineered design, common materials    |
| Best published engineered design (heat-pipe) |       ~379 | Point design, unflown at this scale    |
| Theoretical limit at 20°C, both faces        |       ~633 | Arithmetic, net of sun and Earth glare |
| **AI1 spec**                                 | **~1,360** | **Disclosed spec, unbuilt**            |

*Sources: Redwire white paper May 2026; SpaceX AI1 disclosure; ITK arithmetic.*

The pattern is the point: engineered hardware historically delivers 40–60% of the theoretical figure, once the plumbing that moves heat to the panel, the armour against micrometeoroids, and the geometry of what the panel actually "sees" are included. Nothing built or published reaches half the AI1 number. The largest radiators ever flown — on the International Space Station — reject about 70 kW *for the whole station*, at several times the assumed weight per square metre. No test has yet been flown that settles the question; the first real datapoint arrives with the AI1 demonstration satellites expected 2027–28. Getting the required dissipation means running the radiator at close to the maximum temperature of the chips.

**Why it matters: the mass cascade.** A radiator shortfall does not stop the project — it makes everything heavier. More mass per satellite means fewer watts of computing per tonne launched; and that means more satellites, more rockets and more dollars for the same delivered capacity. Independent engineering estimates put achievable *specific power* (computing watts per tonne of satellite — the industry's key figure of merit) at 17–49 kW per tonne, against the 70–100 SpaceX assumes. One expert consulted in the bank research put radiators at up to ~80% of satellite mass.

### 2. Five year satellite life, no residual

A satellite cannot be serviced or is at least very unlikely to be serviced, so its chips are welded in for life, and the whole asset — bus, solar array, radiator, launch — is thrown away and re-bought every ~5 years. A terrestrial data centre re-buys only its chips (~60% of capex) inside a 25-year building. Every other cost on this list recurs through the treadmill: whatever a satellite costs, the fleet re-buys 100% of it every five years, forever.

### 3. The chip-cost logic trap

Chips are 70–83% of the cost of an orbital data centre on the banks' own numbers. "Free solar power and no building" therefore attacks the *small* end of the cost stack. The cheap orbital scenarios in the bank research require chips at roughly a third of market price from SpaceX's proposed "Terafab" — but cheap chips would lower terrestrial costs equally, so they cannot create an orbital advantage. Looking separately at Terafab provides zero confidence it will ever produce chips any cheaper than, say, TSMC. Yields are likely to be very low. I've ignored Terafab in this analysis.

### 4. Orbital satellites better suited to batch than on-demand use

Orbital capacity is latency-tolerant, batch-suited, and carries silicon up to five years old — yet every bank prices it near terrestrial rates. The market already prices those qualities: batch computing sells at ~50% below interactive rates, chip rental values fall ~25%/yr as generations land, and unserviceable failures compound. Applied to the banks' own unit model, these observable discounts take revenue from $13.3 to ~$4.9 per watt-year against a break-even near $10–11 — the central issue my model tests.

So two key sensitivities in valuation are the revenue discount for a current generation batch of chips because they aren't doing on demand inference and a separate discount for the fact that over their life the chips become out of date. This may not matter so much once chip development slows down. 

Just on the non-training use cases the current thinking is:

**Table: where the inference dollars are, and how orbital fits**

| Revenue pool                                                 | Computational fit                                           | The binding problem                                          |
| :----------------------------------------------------------- | :---------------------------------------------------------- | :----------------------------------------------------------- |
| Interactive coding (autocomplete, IDE chat) — the largest pool, >70% of OpenAI + Anthropic ARR is coding-related | Poor                                                        | Sub-second latency per keystroke, premium SLA, session state across satellite passes |
| Agentic coding (long autonomous runs, CI agents) — the fastest-growing segment | Moderate                                                    | Latency-tolerant per step, but every step executes code in a sandbox — CPU- and memory-heavy virtual machines that GPU-dense satellites don't carry; splitting model in orbit from sandbox on ground round-trips every tool call through scarce downlink |
| Consumer chat subscriptions (~$17bn of OpenAI's ~$25bn ARR)  | Conditional                                                 | Median latency is fine; p99 guarantees across satellite passes and weather-limited optical links unproven |
| Professional services (legal research, document analysis) — fastest-maturing enterprise segment | Best computational fit: batch, parallel, verification-heavy | Governance, not physics: privileged client documents processed on hardware that crosses every jurisdiction on Earth every 90 minutes; data-residency law has no orbital category; the buyers are the most compliance-bound in the economy |
| RL rollouts, synthetic data, evaluations                     | Clean fit                                                   | Priced at wholesale batch rates — the discount problem       |

*Source: ITK research, July 2026. Revenue mix: SemiAnalysis TokenBudgeting (30 Jun 2026), company disclosures; workload fit: ITK orbital workload analysis.*

It's not that exciting.

### 5. Attrition without repair

On the ground, a failed GPU is swapped the same day and capacity stays at nameplate. In orbit every failure is permanent, so delivered capacity decays monotonically over each satellite's life. Compounding a 10% early-failure rate with realistic wear implies fleets deliver ~72–83% of nameplate on average — meaning 20–40% more satellites and launches for the same delivered capacity. Only one bank applied any failure derate at all.

### 6. The environmental ledger: burning the fleet, and feeding the rockets

#### The alumina problem, in plain terms

**Step one: the disposal plan is incineration in the sky.** Satellites cannot be serviced or brought home, so every one of them ends its ~5-year life by being steered down to burn up, 50–80 km overhead. Because the whole fleet is replaced every five years, this is not a one-off: whatever the fleet weighs, that tonnage is burned into the upper atmosphere every five years, forever.

**Step two: burned aluminium doesn't go away.** A satellite is roughly 30–40% aluminium, and burning aluminium produces aluminium oxide — *alumina* — as nanoparticles. Injected that high, they are above the weather: nothing rains them out, and they take decades to settle down through the stratosphere. Annual burn-ups therefore *accumulate* into a growing particle layer sitting in and above the ozone layer.

**Step three: alumina is a catalyst for ozone destruction.** The stratosphere still holds decades' worth of chlorine from the CFC era. Most of it is locked in inactive forms that don't attack ozone — until it meets a particle surface, where it converts to the active form that does. This is the same surface chemistry that polar ice clouds perform over Antarctica each spring, which is what creates the ozone hole. Measured reaction probability on alumina is ~2% per collision, and because a catalyst is not consumed, every nanoparticle keeps reactivating chlorine for as long as it stays aloft. Burning tens of kilotonnes of aluminium a year into the upper atmosphere re-runs ozone-hole chemistry, continuously, on chlorine that is already up there.

**The scale, by fleet size:**

| Fleet                         | Re-entering per year | Of which aluminium |
| :---------------------------- | -------------------: | -----------------: |
| 10 GW (the Model tab's fleet) |               ~28 kt |           ~8–11 kt |
| 20–30 GW                      |            ~56–84 kt |          ~17–34 kt |
| 75 GW (the bank models, 2031) |              ~160 kt |          ~50–65 kt |

*Benchmarks: natural meteoroid influx is a few tens of kt/yr but only ~1% aluminium (well under 1 kt); the atmospheric-science literature treats ~10 kt/yr of re-entry aerosol as its problem scenario for 2040; measured aluminium from re-entries in 2022 already ran ~30% above natural background. ITK arithmetic at 2.8 kt of re-entry mass per GW per year.*

Two readings of that table. First, the effect scales with the fleet, so a 10–30 GW industry is a materially smaller problem than the banks' 75 GW — at the model's scale, mitigation (controlled re-entries, material substitution, disposal fees) is a bearable cost line rather than an existential one. Second, even the smallest fleet on the table exceeds the literature's problem scenario in total mass and roughly matches it in aluminium alone — so "smaller" means manageable-with-mitigation, not immaterial. The magnitudes carry real uncertainty in both directions: these are modelling studies, the first direct measurement of a re-entry plume was published only in February 2026, and particle sizes and residence times are contested.

#### The propellant chain, including the oxygen

Starship burns ~5,250 tonnes of propellant per flight — roughly 1,150 t of methane and 4,100 t of liquid oxygen. The oxygen itself is environmentally benign (it returns to the air it was separated from); the issue is industrial scale and energy:

- **At the Model tab's ~300 flights/yr:** ~1.8 Mt/yr of propellant — about 0.4 Mt of methane (combustion ~1.1 Mt CO₂/yr, comparable to a single mid-sized gas generator) and ~1.4 Mt of liquid oxygen, roughly one large air-separation plant. A normal industrial project.
- **At the banks' ~4,800 flights/yr:** ~5.5 Mt of methane (the output of a mid-sized LNG train) and ~20 Mt of liquid oxygen — about 20% of current world industrial oxygen production, requiring ~11 air-separation plants the size of the largest ever built, plus ~1.6 GW of continuous electric load for liquefaction. Combustion CO₂ ~15 Mt/yr — noticeable, though small against global emissions. A launch system premised on escaping grid constraints arrives needing a grid connection larger than most of the data centres it replaces.

The pattern matches the alumina table: at the model's scale the propellant chain is an engineering procurement; at the banks' scale it is a re-plumbing of world industrial gas markets.

## Appendix: AI models — where Grok sits, and the Chinese models

![grok_residual_table](../media/grok_residual_table.png){#fig-grok-value}

For me "trust" is the most important determinant. And the relevant catch cry is "Trust but verify". Trust has several dimensions. Technically it's about the hallucination rate. In turn the hallucination rate in practice is partly a function of the user prompts and "/skill" sets. The second dimension of trust goes to opinions about the model owner and its developers. I believe Musk can lean on Grok and will lean on it if it suits him. There are likely more subtle leans in Anthropic models but I find it works well for me. Chinese models are useful apparently at the low end. But I personally want models that are at the high end. 

Here is the Claude (talk the book) status summary:

"The popular perception that Grok is well behind the leading models is out of date, but only partly. On independent aggregate benchmarks Grok 4.5 now ranks fourth among frontier models, essentially level with the best models on agentic coding and at roughly one-fifth the per-task cost of the Claude leader. The gap that remains is reliability rather than raw capability: independent testing found Grok 4.5's hallucination rate more than doubled to 54% of unknown-answer questions, against the mid-30s for the best Claude models. That distinction shows up in the commercial data. xAI's revenue growth is largely consumer subscriptions and its X integration; in the enterprise API market — where Anthropic holds roughly a third and OpenAI a quarter — Grok barely registers, and Anthropic reportedly captures over 40% of AI coding spend despite a large price premium. Paying customers are demonstrably buying quality and reliability, not tokens.

The more consequential competitive story is Chinese open-weight models. The best of them (Kimi K2.6, DeepSeek V4, Qwen 3.6) now score level with Grok on independent capability indices, sit about six points behind the closed US frontier, and have largely closed the hallucination gap — at a fraction of the price. The result is a market that has visibly bifurcated: on OpenRouter, a reasonable proxy for developer token flows, Chinese labs now carry over 45% of traffic while the US share has collapsed from about 70% to about 30% in a year, yet quality-sensitive revenue remains concentrated in the US closed labs. Epoch AI's careful measurement puts the Chinese frontier a stable seven months behind the US frontier — not converging, but tracking it while reportedly spending an order of magnitude less and without access to Blackwell-class hardware, a constraint the Chinese labs have substantially offset through algorithmic efficiency (and, plausibly, some strategic subsidy in pricing).

For users, the practical question is whether cheap-and-nearly-as-good displaces best-in-class. The evidence suggests it does at the bottom of the market (high-volume, low-stakes, price-sensitive work) but not at the top, where reliability is the binding constraint because review costs swamp token savings. Lock-in cuts two ways: at the API layer it is weak — around 60% of enterprises now run two or more vendors and switching is technically trivial — but at the workflow layer it is real and growing, as accumulated context, personalisation and user fluency with a particular model become genuine switching costs, especially for small businesses without the resources to run formal evaluations. That familiarity moat protects incumbents against marginal improvements, though not against step changes, as OpenAI's halved enterprise share over three years attests."



## Glossary

Orbital compute sits at the junction of three industries — space, semiconductors and data centres — and borrows jargon from all three. 

### Units and money

**$/W — capex per watt.** Total capital divided by capacity. Terrestrial all-in runs ~$28–46/W; the banks' orbital estimates span $10–47/W.

**$/W-yr — revenue per watt-year.** The annual rent a watt of capacity earns. The banks assume $9–15/W-yr; scarcity deals today are signed at $25–50 but all four banks treat those as unsustainable. Against a 5-year disposable asset, $/W-yr must repay $/W quickly: at $40/W capex, break-even is ~$8–11/W-yr.

**Nameplate vs delivered capacity.** Advertised capacity versus what is actually sellable after failures. On the ground the gap is negligible because dead GPUs are swapped same-day; in orbit nothing is repaired, so delivered capacity decays every year of a satellite's life.

### The machine

**Satellite bus.** Everything except the payload: structure, solar arrays, power management, propulsion, thermal system.

**AI1.** SpaceX's disclosed orbital-compute satellite design: 2.1 tonnes, 120 kW average / 150 kW peak, 600 m² solar array, 110 m² radiator, ~5-year life, no servicing. All four bank models describe this same machine.

**GPU / accelerator / "GB300-class".** The Nvidia-designed chips that do the AI computation, named by generation (Hopper → Blackwell → Rubin). Generations land every 12–18 months and rental prices for old silicon fall 15–25% a year.

**Specific power (kW/tonne).** Compute watts per tonne of satellite. The banks assume 70–100; flown hardware implies ~49; independent estimates run 17–49. In my model this sets both cost per watt and the fleet's growth ceiling.

**Radiator / thermal (heat) rejection.** How the satellite sheds the heat its chips make — in vacuum, radiation from panels is the only exit. 

**PUE — power usage effectiveness.** Total facility power divided by power reaching the IT load; 1.0 is perfect. Terrestrial runs 1.2–1.5 (cooling overhead); orbital ~1.05 is credible because radiative cooling needs almost no power. 

**ISL — inter-satellite (laser) links.** The optical links that tie thousands of satellites into one cluster, replacing the data centre's internal network. Demonstrated ~1.6 Tbps; a training fabric wants ~10 Tbps per link, and intra-rack links on the ground are orders of magnitude faster still. 

### Orbit and launch

**LEO — low Earth orbit.** A few hundred kilometres up, one lap every ~90 minutes. Close enough that latency is small; low enough that dead satellites re-enter and burn up in years rather than centuries.

**Dawn-dusk sun-synchronous orbit (SSO).** A polar orbit that rides the day/night boundary so the solar panels see the sun >90% of the time: it needs polar launch corridors (traditionally Vandenberg, not Texas or Florida), and it concentrates the entire fleet into one narrow orbital family.

**Starship / booster / ship.** SpaceX's two-stage heavy-lift rocket: the booster (first stage, tower-catch demonstrated, has re-flown) and the ship (second stage, caught once, never re-flown). The economics need the ship to fly ~17 times each. ~100 tonnes to orbit per flight; 47–48 AI1 satellites per load. At a steady cadence the ships are consumables: a 17-flight life is a few months of service.

**$/kg to orbit.** The launch industry's unit price. History ~$18,500/kg; Falcon 9 today ~$2,700; the bank models need $137–300; Starcloud assumes $30. Below ~$500/kg launch stops being the binding cost — chips and thermal dominate.

### The compute market

**Batch vs interactive; SLA; p99.** Interactive work answers a waiting human; batch work runs whenever capacity is free — and the market prices the difference: posted batch tiers run ~50% below interactive rates. An SLA is the contractual service guarantee, and p99 latency (the slowest 1% of responses) is the usual metric. 

**Chip-age discount.** A satellite's GPUs are welded in for its whole life; a terrestrial data centre swaps them every ~2.5 years.

**RL rollouts.** Reinforcement-learning workloads where the model practises tasks in parallel across many independent copies — the fastest-growing slice of training compute, and the slice best suited to orbit because the copies barely need to talk to each other.

**Terafab.** The SpaceX/Tesla/xAI captive chip-fab project (Grimes County, Texas; Intel 14A process). The cheap ends of the bank capex ranges assume Terafab silicon at roughly a third of market price. Three problems: the binding commitment is $5bn with a 90-day no-cause exit against a $119bn announcement; the closest execution benchmark puts credible first silicon at ~2030–31 and competitive yields at ~2032–34; and cheap chips help terrestrial data centres equally.

### Failure and end of life

**COTS — commercial off-the-shelf.** Ordinary commercial hardware (Nvidia GPUs) rather than radiation-hardened space processors, which are decades behind in performance. The whole thesis rides on COTS chips surviving orbit well enough.

**TID — total ionising dose.** Cumulative radiation damage that eventually kills a part — Google's testing found 20× margin over a shielded 5-year mission.

**Infant mortality / attrition.** Infant mortality: satellites dead on arrival or soon after (~10% — the only failure number in ~390 pages of bank research). Attrition: the ongoing failure of chips and satellites that, unrepairable, compounds to 15–25% of delivered capacity over a 5-year life. 

**De-orbit / demise / alumina.** End-of-life satellites are steered down to burn up in the atmosphere. The burn converts the fleet's aluminium into aluminium-oxide (alumina) nanoparticles that persist for decades in the stratosphere and catalyse ozone destruction.

### The thermal terms

Three directions to hold onto: rejection flux **higher is better** (smaller radiators), areal density **lower is better** (lighter radiators), specific power **higher is better** (fewer launches). 

**Flux (W/m²).** Watts of heat shed per square metre of radiator. Higher is better: double the flux and the radiator halves. The SpaceX-vs-independent dispute is about whether ~680 W/m² per face is achievable in built hardware.

**Planform.** The footprint of a flat panel, counted once even when it radiates from both faces. A "1,360 W/m² planform" spec met by a two-sided panel means each face does ~680 — the fairer way to compare against single-surface benchmarks.

**Stefan–Boltzmann law.** Radiated power rises with the fourth power of the radiator's temperature, so hot radiators are small radiators. But heat only flows downhill: the radiator must stay cooler than the chips, and the chips have a ceiling. That squeeze is the central design tension.

**Thermal margin.** The gap between a chip's operating temperature and its maximum. Running the radiator hotter to shrink it consumes this margin: saving radiator mass by spending chip performance and reliability.

**MMOD armour.** Micrometeoroid and orbital debris shielding on radiator panels. A liquid-filled panel is puncturable, so real panels carry armour mass that theoretical radiator calculations omit — one reason built hardware delivers 40–60% of theory.

**Redwire.** A listed US space-infrastructure supplier (deployable solar arrays and radiators, ISS payload hardware) whose May 2026 white paper is the closest thing to a public engineering benchmark from a company that builds this class of hardware. Its "baseline" (~250 W/m²) is a simple passive panel; its "point design" (~379 W/m²) is a worked heat-pipe design for an 8 kW load.

**ISS-class.** Hardware with International Space Station heritage — the largest pumped-ammonia radiator systems ever flown, rejecting ~70 kW for the whole station. Shorthand for "proven in space, but an order of magnitude below what one AI1 satellite requires, at several times the assumed weight per square metre."





