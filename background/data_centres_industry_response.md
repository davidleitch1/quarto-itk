---
title: "Can data centres lower electricity costs? US and Australian industry positions on flexibility, demand response and behind-the-meter batteries"
author: "David Leitch"
date: 2026-05-11
format: html
draft: false
category: "datacentres"
lightbox: true
---

# Can data centres lower electricity costs? US and Australian industry positions on flexibility, demand response and behind-the-meter batteries

## Headline answer

The starting question — does the data centre industry argue that large new loads can be added without raising prices for other customers, and can they actually contribute to lowering them — splits very differently in the United States and Australia.

In the **United States**, a substantial industry-friendly literature has emerged in 2024-2026 making three connected claims: (1) **flexible** large loads could absorb 76 GW of headroom on existing US grids if they accept 0.25% annual curtailment (the Norris-Duke "Rethinking Load Growth" paper); (2) **behind-the-meter batteries** already installed for ride-through can be re-purposed for grid services; and (3) **hyperscaler PPAs are net additive** to clean generation rather than diverting existing capacity. The counter-narrative — codified by LBNL/Brattle (Jan 2025) and amplified by EEI and the Data Center Coalition — is that grid spending, not load growth, is the dominant driver of recent rate increases, and that data centres are net positive for ratepayers via fixed-cost spreading. Microsoft is reported to be reconsidering its 24/7 carbon-free energy pledge as AI demand outruns renewable build, and McKinsey's projection that *inference* (the inflexible workload) will be the larger 2030 cohort is the industry's quietest concession.

In **Australia**, the picture is different by an order of magnitude. The fleet is small (~1.35 GW operating at end-2025 against ~50 GW in the US), the industry's peak body (Data Centres Australia) only formed on 28 November 2025, and **no Australian operator has published a quantitative demand-flexibility commitment**. The political coalition has converged remarkably fast around "data centres should pay their own way" — including a February 2026 industry/union/environment joint statement and the federal *National AI Plan* (December 2025) with binding-like *expectations* on demand flexibility, full grid-cost recovery and renewables underwriting. There is no Australian equivalent of the US behind-the-meter gas turbine surge, but there is one stand-out co-located BESS project (Quinbrook Supernode, 780 MW / 3,074 MWh in Brendale QLD) and AWS made its first Australian solar-plus-storage PPAs in April 2026 (430 MW across 9 PPAs, 8 with co-located BESS).

The biggest single divergence is the political economy. In the US the politics has crystallised around residential bills going up because of capacity-auction stress; in Australia it has crystallised around the National AI Plan / energy-transition framing. There is no Australian equivalent of the US bipartisan rate-shift backlash — yet.

This note draws on two parallel research drafts kept under `background/_research_drafts/industry_response_us.md` and `background/_research_drafts/industry_response_australia.md` for traceability.

---

## 1. The US industry case: what the literature, the hyperscalers and the trade groups actually say

### 1.1 The "flexible load" headroom argument

The single most-cited industry-friendly study in the past 18 months is Tyler Norris, Tim Profeta, Dalia Patino-Echeverri and Adam Cowie-Haskell, *Rethinking Load Growth*, Duke Nicholas Institute (February 2025) [@norris-duke-2025]. Headline finding across the 22 largest US balancing authorities (~95% of national peak load): the existing system could absorb **76 GW of new load if those loads accept 0.25% annual curtailment** (about 85 hours/year), rising to **98 GW at 0.5% curtailment** and **126 GW at 1.0%**. PJM headroom is ≈18 GW at the 0.5% threshold; MISO 15 GW; ERCOT 10 GW; SPP 10 GW; Southern Company 8 GW. In ~88-90% of curtailed hours at least half the load would still be served [@ud-norris-summary].

Two qualifiers that industry briefings frequently strip out are explicit in the paper: the analysis **does not model intra-zone transmission constraints** and uses **historical peak demand without an additional reserve margin** [@ud-norris-summary]. Norris's own ISO-NE briefing (March 2025) presents the headroom as an upper bound contingent on those assumptions [@iso-ne-norris]. The 76 GW number is now ubiquitous in EPRI materials, Data Center Coalition speaking points and policy-maker testimony, almost always without those qualifiers.

EPRI launched its **Data Center Flexible Load Initiative (DCFlex)** in March 2025 with about 15 founding members (Google, Meta, NVIDIA, Constellation, Duke Energy, NRG, PG&E, PGE, Southern Company, Vistra and others); membership had grown to ~40 organisations by early 2026 [@ud-dcflex; @latitude-dcflex-global]. The stated programme is to deploy 5-10 "flexibility hubs" by 2027 testing computational scheduling, backup-generator dispatch and on-site solar/storage, with nine active demonstration sites as of mid-2026 and a "Flex MOSAIC" performance framework intended to standardise flexibility measurement [@dcflex-epri]. EPRI is utility-funded research, not strictly advocacy, but hyperscaler co-funding makes the framing interest worth flagging.

The **MIT Center for Energy and Environmental Policy Research** working paper *Flexible Data Centers and the Grid: Lower Costs, Higher Emissions?* (Knittel, Senga and Wang, July 2025) modelled three regional grids (Texas, mid-Atlantic, WECC) and found total system-cost savings from data-centre flexibility of about **2% in WECC rising to 5% in ERCOT** — material, but not transformational [@mit-ceepr-2025; @mit-sloan-summary]. The emissions result is more contingent: in Texas, flexibility cut emissions by up to 40%; in coal-heavier regions flexibility *raised* emissions by up to 3% because the cheapest available shifted hours dispatched fossil baseload. The breakeven for emissions reductions is roughly 50% renewable penetration.

The most physical (as opposed to model-based) recent demonstration is **Emerald AI's March 2026 trial with National Grid Partners and Nebius** in London, using a 96-GPU NVIDIA Blackwell Ultra cluster. The platform responded to 22 live dispatch events and reduced power draw by up to **40% in under 40 seconds**, including a simulated UK "TV pickup" event, while keeping latency-sensitive inference workloads running and rescheduling training around natural checkpoint intervals [@register-emerald; @dcd-emerald]. Emerald has subsequently announced an integration with NVIDIA DSX Flex that the company claims could "unlock up to 100 GW of grid capacity" [@emerald-nvidia] — a vendor figure that should be treated as marketing until validated.

### 1.2 What the hyperscalers themselves have committed

Operationally, the hyperscalers' demand-response footprint is much smaller than the headline literature suggests:

- **Google** has the most operationally specific public claim. An October 2024 blog post announced new demand-response agreements with Indiana Michigan Power and TVA, layered on top of an earlier proof-of-concept with Omaha Public Power District where non-urgent ML workloads were curtailed across three grid events [@google-flex-2024]. Comparable arrangements exist with Centrica/Elia in Belgium and Taiwan Power. **No MW or MWh figures were disclosed.** Google's 2025 Environmental Report claims 66% carbon-free energy on an hourly basis (up from 64%); group-level emissions still rose 11% YoY and are 51% above the 2019 baseline [@google-env-2025; @esgdive-google].
- **Microsoft** reports about 40 GW of contracted renewable capacity across 26 countries (≈400 contracts, of which 19 GW operational), and 100% annual matching of 2025 global electricity consumption [@msft-blog-2025; @dcd-msft-40gw]. On flexibility: a Dublin grid-interactive UPS programme with Enel X and EirGrid bidding lithium-ion batteries (already installed for backup) into the Irish DS3 ancillary services market [@msft-ireland-ups]; a 1.5 MW hydrogen fuel-cell + battery hybrid at Cheyenne WY demonstrated with Caterpillar [@msft-h2-2024]; and an ESB green-hydrogen pilot for Dublin announced 2024.
- **AWS** positions its flexibility contribution primarily through *generation build-out* rather than load-shifting: 1.92 GW from Talen-Susquehanna (after FERC restructuring); the "Cascade" 12-unit X-energy SMR project (~960 MW by early 2030s); and a Dominion partnership for ≥300 MW SMR near North Anna [@powermag-talen; @powermag-amazon-cascade]. AWS reports a 2024 fleet PUE of 1.15 vs 1.25 cloud average and 1.63 on-premises [@aws-sustainability]. **No quantified MW of dispatchable flexibility has been disclosed.**
- **Meta**'s public flexibility footprint is the smallest. It joined DCFlex as a founding member but as of mid-2026 has no published MW commitment or operational DR programme. Meta's contribution to the lowering-costs narrative is procurement: 10.24 GW of clean energy contracted in 2025, narrowly leading Amazon (10.22 GW) [@esgtoday-2025].

According to BloombergNEF, the four hyperscalers together accounted for roughly **49% of global corporate clean PPA volume in 2025**, even as global volumes contracted 10% to 55.9 GW. Microsoft is now the largest cumulative corporate clean-energy buyer at 34.7 GW contracted [@bnef-2025; @sp-corporate-leaderboard].

### 1.3 Behind-the-meter batteries

The industry argument is that BTM batteries already installed for ride-through and UPS can be re-purposed for grid services. The most-cited US deployments:

- **Switch Citadel / Tahoe Reno** — co-developed with Capital Dynamics, a 127 MW behind-the-meter solar plant with a 240 MWh Tesla Megapack battery dedicated to the data centre campus; "Gigawatt 1 Nevada" pipeline aims at >800 MWh of total Megapack capacity across Switch's Las Vegas and Reno facilities [@dcf-switch-megapack; @switch-megapack-pr].
- **xAI Colossus (Memphis)** — 168 Tesla Megapacks deployed on site (each ≥3.9 MWh), combined order value reported at about \$375 million [@dcd-xai-megapacks; @teslanorth-xai]. Stated functions are peak-shaving, power-quality and outage ride-through. *Important caveat: industry coverage does not confirm enrolment in any TVA grid-services product.*
- **Equinix-Bloom Energy programme** — >100 MW of solid-oxide fuel cells across 19 IBX data centres in six US states (75 MW operational, 30 MW under construction at Feb 2025 expansion) [@bloom-equinix].
- **AEP-Bloom Energy** — gigawatt-scale procurement framework signed October 2024 to supply Bloom fuel cells as BTM generation to AEP's data-centre customers [@bloom-aep].

Outside Microsoft Dublin's DS3 participation, **publicly verifiable enrolment of US data-centre BTM batteries in ISO ancillary-service markets is limited** — claims of grid-services capability typically describe technical potential, not contracted MW.

### 1.4 ISO demand response programmes

- **ERCOT** reports about **5,302 MW of large load classified as "controllable"** as of 2025, ~2% of the total large-load portfolio [@ercot-large-load]. Texas SB 6 (June 2025) codifies a two-track curtailment framework: mandatory protocols for post-2025 interconnections during firm load shed, and a voluntary PUCT-procured reliability service for >75 MW loads with ≥24 hours' notice [@bakerbotts-sb6]. Industry response has been **mixed but mostly accepting** — DCC and individual operators have argued for clarity rather than challenging the authority itself. Some Capstone analysts have characterised SB 6 as providing "regulatory certainty" for IPPs and colocation deals.
- **PJM**'s December 2025 auction for 2027/28 fell 6,625 MW short of reliability targets and cleared at a record \$333.44/MW-day. PJM reports that "large data center operators began enrolling backup generation and curtailable load to participate" and that the DR availability window was widened to 24 hours for 2027/28, raising capacity value [@pjm-2025-review]. Aggregate quantification of cleared **data-centre-specific DR MW is not published**.
- **CAISO** forecasts data-centre load rising 1.8 GW by 2030 and 4.9 GW by 2040 in the CAISO footprint, with 4.5 GW already in study in 2025-26 transmission planning [@caiso-large-load]. **No California data-centre cohort with material registered DR participation has been publicly identified.**

### 1.5 The counter-argument on rate attribution

The most consequential 2025 publication for the industry's affirmative case is the joint **Lawrence Berkeley National Laboratory / Brattle Group** study (January 2025). It finds that grid-infrastructure spending — adaptation/hardening (28% of distribution spend), expansion (28% of distribution; 42% of transmission) and equipment-cost inflation in transformers and switchgear — is the dominant driver of recent rate increases, **not new load per se**. Rates in North Dakota actually fell about 1c/kWh between 2019 and 2024, partly attributed to data-centre and other large-load additions diluting fixed costs across more kWh [@lbnl-brattle-2025; @pbs-lbnl]. Brattle's December 2025 GridConnext extension estimates that better grid utilisation and load-following anchor effects could save consumers **>\$100 billion over the next decade** [@brattle-gridconnext; @latitude-brattle].

This LBNL/Brattle work is now the single most important non-advocacy citation industry uses to argue that data-centre load growth is not the cause of rising bills.

The contrary evidence the industry rarely confronts: PJM's Independent Market Monitor attributes **63% of the 2025/26 capacity price increase** — about \$9.3 billion that customers will pay through higher rates — directly to data-centre demand, and 40% of total auction cost (\$6.5 billion of \$16.4 billion) to data-centre load [@ud-imm-2025]. Industry response has been to challenge methodology and to counter-cite the LBNL/Brattle work; it has not been to dispute that capacity prices have risen.

### 1.6 Industry counter-positions: EEI, DCC, ICF

**Edison Electric Institute** (utility-side advocacy) reported in a March 2026 FERC filing that investor-owned utilities are working to interconnect at least **39 GW of large customer load**, with more than 80 large projects in development; 20 states have approved at least one large-load tariff and 9 have pending proposals [@ud-eei-39gw]. EEI president Drew Maloney's framing is careful: "We are committed to ensuring the timely interconnection of large loads while also ensuring benefits and protection for all customers and the grid." Projected 2025-29 utility capex is roughly \$1.1 trillion, nearly matching the \$1.3 trillion spent over the prior decade.

The **Data Center Coalition** (DCC, members include Google, Microsoft, Meta, Amazon and ~40 other operators) has pursued three rhetorical moves in 2025 filings:

1. *Cost-of-service compliance.* DCC director of energy policy Lucas Fykes is on the record that "the data center industry is committed to paying its full cost of service", routinely citing the December 2024 JLARC Virginia report as evidence [@latitude-dcc].
2. *Bring-your-own-power.* DCC, with PJM-state governors and utilities Exelon and PPL, has called for expedited grid entry for data centres bringing dedicated generation [@ud-dcc-byop].
3. *Voluntary, not mandatory, curtailment.* DCC opposes prescriptive curtailment regimes and prefers programmes that "encourage, but not force" data centres to seek their own capacity or curtail [@ud-dcc-voluntary].

DCC commended the Pennsylvania PUC's November 2025 large-load framework as preferable to "waiting for disputes to play out utility by utility", but stated public dissatisfaction with the AEP Ohio July 2025 ruling requiring data centres to pay a larger up-front share of system costs.

### 1.7 The "we'll bring new generation" argument

The headline claim is that hyperscaler procurement is *additional* — PPAs for nuclear restarts, SMRs, new wind, solar and storage rather than diverting existing capacity. The strongest exhibits are the Microsoft-Constellation Three Mile Island restart (835 MW, 20-year PPA, accelerated to 2027); Amazon-Talen Susquehanna (\$18 billion, 1.92 GW front-of-meter PPA); Amazon-X-energy/Energy Northwest "Cascade" (12 Xe-100 SMRs, ~960 MW by early 2030s); Amazon-Dominion ≥300 MW SMR near North Anna; and the BNEF 49% global PPA share figure cited above [@constellation-tmi; @powermag-talen; @powermag-cascade; @dominion-amazon-smr].

Critics' counterpoint — that PPAs for *existing* nuclear redirect already-committed clean MWh away from grid customers and force replacement with marginal gas — is what underlies the FERC Talen-AWS rejections. The industry has not directly rebutted that critique; instead it has restructured deals (the AWS front-of-meter pivot) or pursued *new* generation build (the SMR programme).

### 1.8 Where the industry concedes

The clearest concession is **Microsoft's reported reconsideration of its "100/100/0" target** — matching 100% of electricity, 100% of the time, with carbon-free energy on the same regional grid by 2030. Reporting in early May 2026 (Bloomberg, TechCrunch, Geekwire, DCD) cites internal deliberations on whether to delay or scale back the hourly-matching component as AI training capex outpaces renewable build [@bloomberg-msft; @geekwire-msft]. Azure infrastructure head Alistair Speirs has publicly conceded that "renewable energy on the grid did not yet exist in the volumes Microsoft expects to need as AI demand grows" [@kuow-msft]. *This is reported, not finalised, as of May 2026.*

The industry also implicitly concedes the **training-vs-inference flexibility split**: training workloads can tolerate ~100 ms of geographic latency, support remote siting and natural checkpoint pauses, and are the workload class Emerald AI / EPRI / Google demonstrations have actually flexed. Inference workloads tolerate as little as ~5 ms, must run near end-users and are *not* materially flexible without service-level degradation [@mck-workloads]. McKinsey expects inference to grow at a 35% CAGR to >90 GW by 2030 versus training at 22% CAGR to >60 GW — meaning **the inflexible cohort will be the larger one** within the forecast horizon. Training also runs at very high duty cycle (≥80% utilisation while a model is in flight), which limits the practical share of energy that can be shifted without lengthening training timelines that have themselves become a competitive variable.

---

## 2. Australia: smaller scale, different politics, very different industry voice

### 2.1 The fleet and the pipeline

Australia's operating IT load is ~1.35 GW at end-2025 [@cefc-baringa] versus ~50 GW in the United States. The often-quoted "2 GW" headline appears to confuse operating IT load with gross site MW or with announced/committed but not commissioned capacity; CEFC, USSC and Oxford Economics all converge on the 1.3-1.4 GW figure. The largest single operating campus is roughly **AirTrunk SYD3 at ~330 MW** — about a quarter of the size of Meta Altoona's master-plan envelope.

The pipeline is the political story. **AEMO received 44 GW of data centre connection requests** from network service providers in the 2025 IASR process, against only ~6 GW required to meet Step Change demand [@oxford-economics-aemo]. The CEFC/Baringa central forecast has Australian data centre capacity reaching 4.7-7.4 GW by 2035, with electricity consumption rising from ~2% of NEM-supplied energy today to as much as 11% of national consumption [@cefc-baringa].

Headline projects: AirTrunk Mamre Road / SYD4 (1.2 GW, 6 buildings, 852 diesel gensets, SSDA on exhibition); CDC Marsden Park (504 MW, scalable to 1 GW, NSW approval Nov 2025, A\$3.1 bn); NEXTDC + OpenAI S7 Eastern Creek (550 MW, A\$7 bn, MoU Dec 2025, target 2H 2027); AirTrunk MEL2 (354+ MW, A\$5 bn); Microsoft Australia A\$25 bn (April 2026, escalated from A\$5 bn in 2023, 29 sites announced); AWS A\$20 bn (April 2025, escalated from A\$13.2 bn 2023-27); Quinbrook Supernode at Brendale QLD; multi-site Macquarie Park substation upgrades [@airtrunk-mamre; @nsw-cdc-marsden; @nextdc-openai; @airtrunk-mel2; @msft-au-25bn; @aws-au-20bn].

### 2.2 The new peak body

Australia's data centre industry voice has just formed. **Data Centres Australia (DCA)** was launched on 28 November 2025 by AirTrunk, AWS, CDC, Microsoft and NEXTDC, with NEXTDC CEO Craig Scroggie as inaugural chair and former Microsoft government affairs head Belinda Dennett as CEO. STACK, Equinix, Goodman, Schneider Electric and TikTok joined at launch [@cyberdaily-dca; @techcap-dca].

DCA's first major substantive output is the November 2025 Mandala Partners report **"Data Centres as Enabling Infrastructure"**, commissioned by the four founding hyperscalers [@mandala-dca]. The framing is that data centres:

- Have invested A\$3.1 billion in grid infrastructure since 2020 with another A\$7.2 billion forecast by 2030 (including A\$1.1 billion of "excess capacity for communities and other industries")
- Underwrite renewable PPAs sufficient to power "over 200,000 homes a year"
- Have "around 70% of energy consumption offset by renewables"
- Will invest A\$500 million to A\$1.1 billion in recycled water infrastructure by 2030

The DCA framing is **explicitly positive-spillover**: data centres as catalysts for grid and renewables investment. **There is no published DCA position paper specifically endorsing demand response or load flexibility commitments**, and DCA's submission to the NSW Legislative Council inquiry (Submission No 30) reiterates the enabling-infrastructure framing rather than offering specific flexibility commitments [@dca-nsw-sub]. There is no Australian equivalent of Tyler Norris's Duke work or EPRI DCFlex.

### 2.3 What individual operators are doing on flexibility, BTM batteries and PPAs

- **AirTrunk**: signed the OX2 Riverina solar PPA jointly with Google; publishes annual sustainability reports. The brief's reference to an "AirTrunk WA Akaysha BESS" could not be verified — searches returned no result. Operating co-located BESS at AirTrunk SYD/MEL campuses is part of standard cooling/UPS design, not configured as a grid-export resource.
- **NEXTDC** focuses sustainability messaging on PUE, NABERS 5-star and the "NEXTneutral" carbon-offset add-on rather than on demand flexibility or grid services. Does not appear in Energy Charter signatories.
- **CDC** emphasises Marsden Park's "99% renewable energy by 2030" target and a 27 MW on-site solar component; no demand-response commitment.
- **Microsoft Australia** signed a 15-year PPA for 100% offtake of FRV's 300 MW Walla Walla Solar Farm (NSW), commissioned October 2025 — its largest Australian renewable PPA [@pvtech-walla-walla; @reneweconomy-walla-walla]. The April 2026 A\$25 bn announcement reaffirms 100% renewable matching by 2030 but does not commit to demand response.
- **AWS** announced **9 new Australian PPAs in April 2026 totalling 430 MW** (1 wind: Golden Plains 2 201.8 MW; 3 utility-scale solar+storage; 4 distributed solar+storage; 1 standalone battery) — **eight of nine include co-located BESS**. This is the most material Australian co-location of BESS by a hyperscaler customer to date, and AWS's first solar-plus-storage PPAs outside the US [@energy-storage-news-aws].
- **Anthropic** signed a non-binding government MoU on 1 April 2026 (the first under the National AI Plan) committing to renewable energy investment and alignment with the *expectations* — and met separately with NEXTDC, AirTrunk and CDC. A US\$4.5 billion Sydney NEXTDC offtake has been reported [@anthropic-au-mou; @certified-anthropic].

The Australian iteration of the "data centres can support the grid" argument is being made primarily by **battery vendors and renewable developers**, not by the hyperscalers themselves. Fluence's Jeff Monday (April 2026) is the clearest articulation: BESS allows data centres to "present a predictable, grid-compliant electrical profile", provide power-quality support, accelerate energisation versus waiting for transmission upgrades, and shift roles between load-management and grid participation over time [@energy-storage-news-fluence]. This is closer to the US "site-level firming" framing than to actual workload-flexibility demand response.

### 2.4 No Australian BTM gas — the structural reasons

Three reasons there is no Australian equivalent of Voltagrid, Bloom-Enchanted Rock or the xAI Memphis turbines:

1. **Pipeline gas economics.** Wholesale gas in NSW/VIC has been A\$10-18/GJ for most of 2024-25, well above the US Henry Hub equivalent. Cogen and reciprocating-engine LCOE are uncompetitive against grid + PPA, even with current grid congestion.
2. **No stranded gas in load centres.** US BTM gas thrives on Permian flare gas and PJM-area Marcellus tailgate. Australia has no equivalent in the Sydney/Melbourne basins.
3. **Planning culture.** Diesel back-up generation is sanctioned through standard EPA/EIS processes and tightly capped on operating hours; new reciprocating gas would face a much harder approval path. Loudoun-County-style permit creep (Virginia DEQ began consulting on relaxing the 500-hour annual cap in late 2025) has no Australian analogue.

The result is that Australian data centres rely on **diesel for back-up only** — Mamre Road's 852 gensets is the headline number for what that means at scale — and look to **utility-scale BESS** rather than on-site gas for firming.

The clear Australian standout is **Quinbrook Supernode** at Brendale QLD: a US\$2.5 billion data centre adjacent to the South Pine substation, co-located with a 780 MW / 3,074 MWh BESS contracted to Origin (stages 1-2: 520 MW / 1,856 MWh) and Stanwell (stage 3: 250 MW / 1,010 MWh). Stage 1 backfeed-energised September 2025 [@quinbrook-supernode; @pvmag-supernode]. The BESS is third-party owned/operated under a tolling model, making it more of a **co-located grid asset** than true BTM firming for the data centre — but it is the closest Australian analogue to the US Switch-Tahoe Reno BTM solar/storage model.

### 2.5 AEMO and AEMC engagement

The 2024 ESOO was the first to break out data centres as a discrete category. The **2025 ESOO** (published August 2025) and the underlying Oxford Economics report for AEMO (July 2025) are the current authoritative numbers: FY25 actual ~3.9 TWh (98% in NEM, ~2% of NEM-supplied energy); Step Change forecast 25.1% CAGR to 12.0 TWh by FY30 and 34.5 TWh by FY50; **44 GW of NSP-reported connection requests against 6 GW required** under Step Change — the explicit "phantom demand" finding [@aemo-esoo-2025; @oxford-economics-aemo]. AEMO assumes data centres exhibit "relatively stable demand shape" not materially temperature-sensitive; flexibility from cooling load (~40% of total) is acknowledged as a possible mitigant for peak demand but **not relied on quantitatively**.

The most active AEMC workstream is **"Improving the NEM access standards — Package 2"**. The draft determination (12 March 2026) responds to three consolidated rule change requests with five proposals [@aemc-package2; @wattclarity-aemc; @aemc-media-march26]:

1. **Raise the large-load threshold from 5 MW to 30 MW** for inverter-based loads on distribution networks.
2. **Disturbance ride-through requirements** — data centres must remain connected during defined voltage and frequency events and recover within set timeframes.
3. **International alignment** with Texas (PUCT), Ireland (EirGrid) and Finland (Fingrid) standards.
4. **Visibility** for AEMO and NSPs into data centre disturbance response.
5. **Compliance via connection agreements** for non-registered data centres.

The draft was prompted in part by a US incident in which 60 data centres totalling ~1,500 MW disconnected simultaneously during a system disturbance (the July 2024 ERCOT/Houston event). Submissions closed 7 May 2026; final rule expected mid-2026.

The Energy and Climate Change Ministerial Council has committed to "developing a framework to facilitate demand flexibility" for new data centre loads and "ensuring new firmed generation enters the market as data centre demand increases", and is reviewing cost-recovery arrangements to ensure data centres cover network upgrades [@cec-ecmc-2025]. The framework itself has not yet been published.

### 2.6 The "must power itself" coalition and the *National AI Plan*

The political coalition has converged unusually fast around "data centres should pay their own way". A **February 2026 joint statement** from the Clean Energy Council, Electrical Trades Union, ACF, WWF-Australia, Smart Energy Council, RE-Alliance, Climate Energy Finance, Nature Conservation Council NSW, Environment Victoria, Queensland Conservation Council, Sunrise Project Australia and Carbon Zero Initiative — an unusual industry/union/environment alliance — demanded operators "build the renewables and water recycling to power" their facilities [@cec-must-power-itself; @wwf-must-power-itself].

The Albanese Government's **National AI Plan** was released 11 December 2025 [@disr-ai-plan]. The accompanying *Australian Government's expectations of data centres and AI infrastructure developers* sets five expectations [@minister-ai-expectations]:

1. Prioritise Australia's national interest;
2. **Support Australia's energy transition** — including underwriting new renewable supply, paying full grid-connection costs, and supporting demand flexibility;
3. Use water sustainably and responsibly;
4. Invest in Australian skills and jobs;
5. Strengthen research, innovation and local capability.

This is an **expectations** framework, not binding rules. Microsoft (April 2026, A\$25 bn) and Anthropic (April 2026, MoU) have publicly bound themselves to it. The MoU mechanism is the political enforcement device. The Treasury extended the Clean Building MIT withholding tax concession (10% rate) to data centres in the 2025-26 Budget, conditional on meeting NABERS energy efficiency standards [@wfw-au]. There is no Virginia-style sales-tax exemption.

The NSW Legislative Council Public Accountability and Works Committee opened an inquiry on 29 January 2026 (Chair: Abigail Boyd / Greens), with hearings 1, 8 and 22 May 2026 and a report due 30 September 2026 [@nsw-leg-council-inquiry]. The Energy Charter's December 2025 disclosure shows **no major Australian data centre operator as a signatory** [@energy-charter] — a notable gap given DCA's positive-spillover positioning.

---

## 3. United States vs Australia — head-to-head

**Table 1: US vs Australian data centre industry positioning, May 2026**

| Dimension | United States | Australia |
|:----------|:--------------|:----------|
| Operating IT load | ~50 GW; ~580 hyperscale facilities | ~1.35 GW; ~250 facilities |
| Largest single operating campus | ~1,400 MW (Meta Altoona master-plan envelope) | ~330 MW (AirTrunk SYD3) |
| Pipeline | 22-26 GW physically under construction; ~26 GW more in contracted full-envelope; aspirational 35-40 GW | A\$85-135 bn investment to 2035; up to 7.4 GW by 2035; AEMO sees 44 GW in connection queue against 6 GW required |
| Industry peak body | Data Center Coalition (mature, ~\$978k 2025 federal lobby spend) | Data Centres Australia (formed 28 Nov 2025) |
| Flexibility literature | Norris/Duke 76 GW; EPRI DCFlex; MIT CEEPR; Emerald AI National Grid demo | Largely absent — no domestic equivalent of Norris or DCFlex |
| Hyperscaler DR commitments | Google has DR agreements with I&M and TVA (no MW disclosed); Microsoft Dublin DS3 only; AWS and Meta have none | **None disclosed by any operator** |
| ISO DR participation | ERCOT 5,302 MW "controllable" large load (~2% of total); PJM ELRP enrolment growing but data-centre-specific MW not published | None tracked specifically; AEMC IPRR rule change scheduled May 2027 |
| BTM gas turbines | 6 GW in the US construction pipeline (Voltagrid, Bloom, Enchanted Rock, on-site at xAI/Stargate) | **None** — structural reasons (gas price, no stranded gas, planning culture) |
| Co-located BESS at hyperscale site | Switch Tahoe Reno 127 MW solar / 240 MWh BESS; xAI 168 Megapacks (\$375m); Equinix-Bloom 100+ MW; AEP-Bloom GW framework | Quinbrook Supernode 780 MW / 3,074 MWh BESS (third-party tolling, not pure BTM); AWS April 2026 9 PPAs with 8 incl. co-located BESS |
| Counter-argument on rates | LBNL/Brattle Jan 2025; Brattle GridConnext Dec 2025 (>\$100bn savings claim); EEI 39 GW filing; DCC "we pay full cost of service" | Mandala for DCA "Enabling Infrastructure" (Nov 2025); positive-spillover framing |
| Generation-build argument | Strong: TMI restart, AWS-Talen 1.92 GW PPA, Cascade SMR, Dominion SMR, 49% of global PPA volume | Smaller scale: Microsoft FRV 300 MW; AWS 430 MW Apr 2026; Anthropic-NEXTDC reported \$4.5bn |
| Microsoft 24/7 CFE pledge status | Reported reconsideration May 2026 (Bloomberg, TechCrunch) | Reaffirmed in April 2026 A\$25bn announcement |
| Workload time-shifting offer | Google + Microsoft have begun publishing | None |
| Political driver | PJM capacity auction 833% spike; ratepayer-protection PSC actions; bipartisan rate-shift backlash | National AI Plan / *Expectations* — government-led; no voter rate-shift backlash yet |
| Cross-cutting opposition coalition | R + D, county-level, 142 activist groups (Data Center Watch) | Industry + ETU + ACF + WWF + Smart Energy Council "must power itself" letter (Feb 2026) |
| Connection standards | FERC + state PUCs + ad-hoc tariffs; FERC PJM co-location order Dec 2025 | AEMC Package 2 draft 30 MW threshold + ride-through (March 2026, final mid-2026) |
| Tax / incentive regime | Virginia-style sales-tax exemptions running US\$1.6-3.2 bn/yr (under attack) | Clean Building MIT extension; NABERS-conditional; small absolute scale; no Virginia-style fight |

*Source: ITK compilation. See `_research_drafts/industry_response_us.md` and `_research_drafts/industry_response_australia.md` for full citations.*

## 4. What the divergence means

**1. The US flexibility literature is well ahead of US flexibility practice.** The Norris-Duke 76 GW headroom number is the most-cited piece of work in the industry's affirmative case, but the actual operational footprint of hyperscaler demand response in the US is small: Google has unspecified DR agreements with I&M and TVA, Microsoft has Dublin DS3 (Ireland), AWS and Meta have nothing public. ERCOT's 5,302 MW of "controllable" large load is real but only 2% of the total. The industry is making a theoretical case for flexibility that has not yet been validated in dispatched MW at scale. The Emerald AI / Nebius / National Grid March 2026 trial is the most advanced physical demonstration to date — 40% reduction in 40 seconds on a 96-GPU cluster — but that is one cluster, not one gigawatt.

**2. The training-vs-inference split is the industry's quietest concession.** McKinsey's projection that inference (the inflexible workload) will reach 90+ GW by 2030 versus training at 60+ GW means the inflexible cohort will be the larger one within the forecast horizon. Norris-style headroom claims based on training flexibility do not generalise. Industry arguments about workload time-shifting are real for training but largely irrelevant for the inference build-out that will dominate by the end of the decade.

**3. The "we'll bring new generation" argument is genuinely additive in the US but contested by FERC.** The Microsoft-Constellation TMI restart, AWS-Cascade SMR programme and AWS-Dominion SMR exploration represent material new firm low-carbon build that almost certainly would not exist without hyperscaler offtake. But the underlying dispute — whether PPAs against *existing* nuclear (Susquehanna) divert clean MWh from grid customers and force replacement with marginal gas — is what FERC's November 2024 rejection of the Talen-AWS ISA was about, and the industry has not directly rebutted that critique. It has restructured deals (AWS front-of-meter pivot) and pursued new build (SMRs) instead.

**4. Australia is where the politics is right but the projects are too small to test the theory.** The federal *National AI Plan* and *Expectations* explicitly require data centres to underwrite renewables, pay full grid costs and support demand flexibility — a more demanding framework than any single US state has imposed. AEMC's Package 2 draft adopts US/Texas/Ireland/Finland-aligned ride-through standards. The Energy and Climate Change Ministerial Council has committed to a demand-flexibility framework. But Australia has only 1.35 GW operating IT load and no operator has published a quantitative flexibility commitment. The instruments are in place; what is being tested is small.

**5. The Australian peak body has just formed and is in defence mode.** DCA's Mandala "Enabling Infrastructure" framing is positive-spillover (data centres as grid investment catalysts) rather than flexibility-led. The submission to the NSW Legislative Council inquiry is a defensive posture against the cost-recovery and zoning questions, not an affirmative case for data-centre grid contribution. By contrast, the US Data Center Coalition has spent a decade building "we pay our cost of service" and "voluntary not mandatory curtailment" lines that DCA has not yet developed.

**6. The Australian residential battery and VPP fleet is structurally different.** Australia has the world's highest residential battery deployment per capita; the Federal Solar Sharer / NSW PDRS / VIC orchestration / SA VPP programmes are mature. The demand-flexibility *supply* side in Australia is therefore not the binding constraint that it is in PJM — which may explain why data centre flexibility specifically has attracted less policy attention than in the US. The Australian flexibility resource is consumer-side; the US flexibility resource has to be the data centres themselves because the residential supply is much thinner.

**7. The bipartisan US backlash hasn't crossed to Australia yet.** PJM's 833% capacity-auction spike is what made data centre rate impacts a state-level voter issue. Australia's residential bill increases are driven by state-set network charges, wholesale tightness and Snowy 2.0 / transmission cost flow-through — none of which are pinned on data centres. AEMO's 44 GW phantom-demand finding could change that if it were re-framed as "data centres are about to push your bill up", but as of May 2026 the political framing is energy-transition / AI sovereignty rather than ratepayer-protection.

## 5. Implications

For an Australian observer of NEM dynamics, three things are worth watching:

- **The AEMC Package 2 final rule (mid-2026)** will set the legal frame for new data centre connections and is the closest Australian analogue to the FERC PJM co-location order. Any large hyperscale connection from H2 2026 will be governed by the 30 MW threshold and ride-through standards.
- **The NSW Legislative Council inquiry (report due 30 September 2026)** is the political centre of gravity. If it recommends Virginia-style cost-recovery reforms or DR mandates, the National AI Plan *Expectations* framework would gain the enforcement mechanism it currently lacks.
- **AWS's April 2026 9 PPAs with 8 co-located BESS** is the most operationally significant Australian data-centre flexibility instrument to date. If AWS goes on to register the BESS in NEM ancillary services through the Integrating Price-Responsive Resources (IPRR) framework (scheduled May 2027), it would be the first hyperscaler to do so.

For the US, the central question is whether the Norris-Duke headroom argument can survive contact with the **inference-dominated 2030 fleet**. The case for 76 GW of flexible-load headroom assumes data centres are willing to curtail. AI training accepts curtailment in principle (long checkpoint intervals); inference does not (millisecond latency). The McKinsey forecast that inference will exceed training in 2030 is the structural challenge to the flexibility case — and one the industry has not yet engaged with.

---

## 6. Caveats

1. **The Norris-Duke 76 GW headline.** Always cite with the 0.25% curtailment assumption, the absence of intra-zone transmission modelling, and the use of historical peak without an additional reserve margin. The 98 GW (0.5%) and 126 GW (1.0%) sensitivities are arguably more realistic.
2. **Hyperscaler PPA totals are contractual, not operating.** Microsoft 40 GW contracted vs 19 GW operating; Meta 10.24 GW added in 2025. Annual matching is not the same as 24/7 same-grid matching.
3. **BTM battery enrolment.** Most US data-centre BTM batteries discussed in industry materials are described as having *capability* for grid services, not as having *registered MW* in an ISO ancillary product. Microsoft Dublin DS3 and a small number of utility-side pilots are the clear instrument-backed exceptions.
4. **Microsoft 24/7 CFE retreat is reported, not finalised.** As of 11 May 2026 there is no published Microsoft sustainability report withdrawing or modifying the 2030 hourly-matching target.
5. **Emerald AI / NVIDIA "100 GW" claim** is vendor marketing and should not be treated as an independent estimate.
6. **Australian operating IT load** is best estimated at ~1.35 GW. Higher figures appear to confuse operating with announced/committed, or IT load with gross site MW.
7. **Hyperscaler capex announcements are political instruments, not engineering schedules.** Microsoft's A\$5 bn → A\$25 bn escalation, AWS's A\$13.2 bn → A\$20 bn escalation, and the NEXTDC/OpenAI A\$7 bn MoU are all non-binding intent. Operating MW lags by years.
8. **Australian operator positions on demand response are underspecified.** Neither DCA nor any major operator has published a quantitative demand-flexibility commitment. The Mandala report is positive-spillover advocacy, not a flexibility manifesto. ARENA and CSIRO have not published material on data centre demand flexibility comparable to EPRI DCFlex.
9. **The AirTrunk WA Akaysha BESS reference and the Macquarie Mortlake hyperscale data centre** referenced in scoping could not be verified in publicly available sources to May 2026. Mortlake hosts an Origin gas plant + 650 MWh BESS but no Macquarie hyperscale build is announced.
10. **NSW Legislative Council inquiry is mid-flight.** Findings due September 2026 could materially shift the political settlement on cost recovery and demand-flexibility expectations.
11. **AEMC Package 2 final rule is pending.** The 30 MW threshold and ride-through requirements are draft only; final rule expected mid-2026.

---

## 7. References

The full bibliography is below. URLs are listed in plain markdown and would convert to BibTeX entries (`@org-topic-year`) for any subsequent published article. The two underlying research drafts are kept under `background/_research_drafts/industry_response_us.md` and `background/_research_drafts/industry_response_australia.md` for full source-level traceability.

### United States — academic, government and lab sources

- Norris, T., Profeta, T., Patino-Echeverri, D., Cowie-Haskell, A., *Rethinking Load Growth: Assessing the Potential for Integration of Large Flexible Loads in US Power Systems*, Duke Nicholas Institute (Feb 2025). https://nicholasinstitute.duke.edu/events/rethinking-load-growth-assessing-potential-integration-large-flexible-loads-us-power-systems
- Utility Dive summary of Norris findings. https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/
- Norris, ISO-NE Consumer Liaison Group presentation (March 2025). https://www.iso-ne.com/static-assets/documents/100021/march_clg_meeting_speaker_norris_03_27_25.pdf
- EPRI DCFlex landing page. https://dcflex.epri.com/
- Knittel, C.R., Senga, J.R.L., Wang, S., *Flexible Data Centers and the Grid: Lower Costs, Higher Emissions?* MIT CEEPR WP-2025-14 (July 2025). https://ceepr.mit.edu/workingpaper/flexible-data-centers-and-the-grid-lower-costs-higher-emissions/
- MIT Sloan summary of CEEPR finding. https://mitsloan.mit.edu/ideas-made-to-matter/flexible-data-centers-can-reduce-costs-if-not-emissions
- Lawrence Berkeley National Laboratory news release on DOE 2024 data centre energy report (Jan 2025). https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- Brattle, "Electric Rates and Affordability: Observations on the LBNL/Brattle Study and Future Trends" (Dec 2025). https://www.brattle.com/wp-content/uploads/2025/12/Electric-Rates-and-Affordability-Observations-on-the-LBNL-Brattle-Study-and-Future-Trends.pdf
- ERCOT, Large Load Integration page. https://www.ercot.com/services/rq/large-load-integration
- ERCOT, Emerald AI LFLTF presentation (March 2025). https://www.ercot.com/files/docs/2025/03/27/Emerald-AI-LFLTF-Background-for-Circulation-March-28-2025.pdf
- PJM Inside Lines, "2025 in Review" (Dec 2025). https://insidelines.pjm.com/2025-in-review-pjm-market-rules-support-efficiency-resource-adequacy/
- CAISO, Issue Paper Large Load Consideration (Jan 2026). https://www.caiso.com/documents/issue-paper-large-load-consideration-jan-20-2026.pdf

### United States — hyperscaler and project sources

- Google, "How we're making data centers more flexible" (October 2024). https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/
- Google, *2025 Environmental Report*. https://blog.google/outreach-initiatives/sustainability/environmental-report-2025/
- ESG Dive on Google emissions. https://www.esgdive.com/news/googles-emissions-rise-despite-data-center-decarbonization-ppas-environmental-report-2025/752236/
- Microsoft, *2025 Environmental Sustainability Report* announcement (May 2025). https://blogs.microsoft.com/on-the-issues/2025/05/29/environmental-sustainability-report/
- DCD on Microsoft 40 GW. https://www.datacenterdynamics.com/en/news/microsoft-matches-100-of-2025-power-use-with-renewables-with-more-than-40gw-of-contracted-capacity/
- Microsoft Source on Ireland UPS / DS3. https://news.microsoft.com/source/features/sustainability/ireland-wind-farm-datacenter-ups/
- Microsoft Source on hydrogen data centres. https://news.microsoft.com/source/features/sustainability/hydrogen-datacenters/
- Microsoft "Community-First AI Infrastructure" framework (Jan 2026). https://blogs.microsoft.com/on-the-issues/2026/01/13/community-first-ai-infrastructure/
- AWS Sustainability — Data Centers. https://aws.amazon.com/sustainability/data-centers/
- Power Magazine on AWS-Talen Susquehanna restructured PPA. https://www.powermag.com/talen-amazon-launch-18b-nuclear-ppa-a-grid-connected-ipp-model-for-the-data-center-era/
- Power Magazine on Amazon-Cascade SMR. https://www.powermag.com/amazon-unveils-cascade-energy-northwests-xe-100-smr-project-targeting-construction-by-2030/
- Bloom Energy on Equinix expansion. https://www.bloomenergy.com/news/bloom-energy-expands-data-center-power-agreement-with-equinix-surpassing-100mw/
- Bloom Energy on AEP framework. https://www.bloomenergy.com/news/bloom-energy-announces-gigawatt-fuel-cell-procurement-agreement-with-aep-to-power-ai-data-centers/
- Data Center Frontier on Switch-Tesla Megapacks. https://www.datacenterfrontier.com/energy/article/11428858/switch-will-use-tesla-megapacks-for-hyperscale-energy-storage
- Switch Tahoe Reno + Megapack press release. https://www.switch.com/switch-and-capital-dynamics-break-ground-on-massive-solar-and-battery-storage-developments-advancing-rob-roys-gigawatt-nevada/
- DCD on xAI 168 Megapacks. https://www.datacenterdynamics.com/en/news/xai-deploys-168-tesla-megapacks-to-power-its-colossus-supercomputer-in-memphis/
- Constellation on TMI Crane Clean Energy Center. https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html
- Power Magazine on Amazon backing X-energy. https://www.powermag.com/amazon-backs-massive-nuclear-smr-deployment-5-gw-with-x-energy-agreements-with-energy-northwest-dominion/
- Dominion-Amazon SMR press release. https://investors.dominionenergy.com/news/press-release-details/2024/Dominion-Energy-and-Amazon-to-explore-advancement-of-Small-Modular-Reactor-SMR-nuclear-development-in-Virginia/default.aspx
- McKinsey on AI workload shifts. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-next-big-shifts-in-ai-workloads-and-hyperscaler-strategies
- BloombergNEF on 2025 corporate clean PPA volume. https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/

### United States — analysts, advocacy and trade press

- Latitude Media on EPRI DCFlex global expansion. https://www.latitudemedia.com/news/epri-takes-its-data-center-flexibility-project-global/
- Utility Dive on EPRI DCFlex launch. https://www.utilitydive.com/news/epri-launches-data-center-flexibility-initiative-with-NVIDIA-google-meta/731490/
- The Register on Emerald AI demonstration. https://www.theregister.com/2026/03/04/demo_shows_datacenters_can_reduce/
- Data Center Dynamics on Emerald AI. https://www.datacenterdynamics.com/en/news/emerald-ai-releases-results-of-uk-demonstration-project-in-partnership-with-national-grid/
- Emerald AI / NVIDIA DSX Flex. https://www.emeraldai.co/blog/emerald-ai-nvidia-dsx-flex-ai-factories
- Latitude Media on Brattle GridConnext. https://www.latitudemedia.com/news/grid-efficiency-could-save-utility-customers-more-than-110-billion/
- PBS NewsHour on data centres lowering prices. https://www.pbs.org/newshour/show/how-data-center-power-demand-could-help-lower-electricity-prices
- Utility Dive on EEI 39 GW filing. https://www.utilitydive.com/news/ious-edison-electric-interconnect-data-center-ferc/814688/
- Utility Dive on PJM 2025/26 capacity attribution. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/
- Utility Dive on PJM IMM. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction-market-monitor/801780/
- Latitude Media on DCC and state-level rate fights. https://www.latitudemedia.com/news/state-lawmakers-stand-between-ratepayers-and-data-center-costs/
- Pennsylvania PUC press release on large-load framework. https://www.puc.pa.gov/press-release/2025/puc-advances-plan-to-balance-data-center-growth-and-consumer-protection-11062025
- Bloomberg on Microsoft CFE pledge reconsideration. https://www.bloomberg.com/news/articles/2026-05-06/microsoft-clean-power-target-on-chopping-block-over-data-center-boom
- TechCrunch on Microsoft CFE retreat. https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/
- GeekWire on Microsoft CFE retreat. https://www.geekwire.com/2026/report-as-ai-electricity-demands-soar-microsoft-weighs-retreat-from-ambitious-carbon-free-energy-pledge/
- KUOW on Speirs commentary. https://www.kuow.org/stories/are-microsoft-s-ai-and-environmental-goals-compatible
- Baker Botts on Texas SB 6. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation
- Utility Dive on Texas SB 6. https://www.utilitydive.com/news/texas-law-gives-grid-operator-power-to-disconnect-data-centers-during-crisi/751587/
- Utility Dive on bring-your-own-power. https://www.utilitydive.com/news/solving-pjms-data-center-problem/805600/

### Australia — government and regulator

- AEMO, *2025 Electricity Statement of Opportunities* (August 2025). https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2025/2025-electricity-statement-of-opportunities.pdf
- AEMO, "Updated forecasting methodology" (2025). https://www.aemo.com.au/newsroom/news-updates/aemos-updated-forecasting-methodology-targets-rapidly-growing-electricity-loads
- AEMO, 2025-26 Inputs, Assumptions and Scenarios consultation. https://www.aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp/2026-integrated-system-plan-isp/2025-26-inputs-assumptions-and-scenarios
- Oxford Economics Australia for AEMO, *Data Centre Energy Demand — Final Report* (July 2025). https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2024/2025-iasr-scenarios/final-docs/oxford-economics-australia-data-centre-energy-consumption-report.pdf
- AEMC, "AEMC modernises grid connection rules" (March 2026). https://www.aemc.gov.au/news-centre/media-releases/aemc-modernises-grid-connection-rules-accelerate-energy-transition-manage-ai-boom
- AEMC, *Improving the NEM access standards — Package 2: Draft determination* (March 2026). https://www.aemc.gov.au/sites/default/files/2026-03/Draft%20determination%20-%20Package%202.pdf
- AEMC, *Improving consideration of demand-side factors in the ISP*. https://www.aemc.gov.au/rule-changes/improving-consideration-demand-side-factors-isp
- Department of Industry, Science and Resources, "Australia launches National AI Plan" (Dec 2025). https://www.industry.gov.au/news/australia-launches-national-ai-plan-capture-opportunities-share-benefits-and-keep-australians-safe
- Joint media release Bowen / Ayres / Charlton, "Australian approach to AI: Expectations" (Dec 2025). https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-australian-approach-ai-expectations-data-centres-deliver-australians
- DISR, Anthropic MoU (April 2026). https://www.industry.gov.au/publications/memorandum-understanding-between-australian-government-and-anthropic-collaboration-ai-opportunities
- Infrastructure NSW, *Data Centre Consultation Paper* (March 2026). https://www.infrastructure.nsw.gov.au/media/qwwpt03m/nsw-data-centre-consultation-paper_wcag.pdf
- NSW Government, "Southern Hemisphere's biggest data centre gets the green light" (Nov 2025). https://www.nsw.gov.au/ministerial-releases/southern-hemispheres-biggest-data-centre-gets-green-light
- NSW Legislative Council Public Accountability and Works Committee inquiry. https://www.parliament.nsw.gov.au/committees/inquiries/Pages/inquiry-details.aspx?pk=3169
- AER, Ausgrid Wallumatta STS contingent project application (October 2025). https://www.aer.gov.au/system/files/2025-11/Ausgrid%20-%20Contingent%20Project%20Application%20-%20New%20Wallumatta%20STS%20-%2031%20October%202025.pdf

### Australia — industry, peak bodies, consultants

- CEFC / Baringa, *Getting the balance right: Data centre growth and the energy transition* (Dec 2025). https://www.cefc.com.au/insights/market-reports/data-centre-growth-and-the-energy-transition/
- CEFC / Baringa full report. https://www.cefc.com.au/media/hs5ner3s/getting-the-balance-right-data-centres-and-the-energy-transition-full-report.pdf
- Mandala for Data Centres Australia, *Data Centres as Enabling Infrastructure* (Nov 2025). https://datacentres.org.au/wp-content/uploads/2025/11/2025-11_DCA-Mandala-Data-Centres-as-Enabling-Infrastructure.pdf
- Data Centres Australia landing page. https://datacentres.org.au/data-centres-as-enabling-infrastructure/
- DCA, "Response to Australian Government's expectations" (Dec 2025). https://datacentres.org.au/response-to-the-australian-governments-expectations-for-data-centres-and-ai-infrastructure-developers/
- DCA Submission No 30 to NSW Legislative Council Inquiry. https://www.parliament.nsw.gov.au/lcdocs/submissions/94922/0030%20Data%20Centres%20Australia.pdf
- Mandala for AirTrunk, *Empowering Australia's Digital Future* (October 2024). https://mandalapartners.com/uploads/Empowering-Australia%27s-Digital-Future---Report_October-2024.pdf
- Australian Energy Council, "Data Centres and Energy Demand". https://www.energycouncil.com.au/analysis/data-centres-and-energy-demand-what-s-needed/
- Climate Council Submission to NSW Inquiry. https://www.climatecouncil.org.au/resources/submission-nsw-inquiry-into-data-centres/
- Clean Energy Council et al. "Data centre rush must power itself" joint statement (Feb 2026). https://cleanenergycouncil.org.au/news-resources/data-centre-rush-must-power-itself-says-industry,-unions-and-environment-groups
- US Studies Centre, "Powering the cloud: Data centres and the future of Australia's grid" (March 2026). https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid
- M3 Property, *Data Centre Growth in Australia* (November 2025). https://m3property.com.au/static/88f0d39061ca9072f2bf0a5b61dc5c3f/M3-Property-Report-Data-Centre-Growth-in-Australia-November-25.pdf
- Energy Consumers Australia, *Request for EOI — Consumer Impacts of Data Centres* (Oct 2025). https://energyconsumersaustralia.com.au/sites/default/files/2025-10/website-doc-eoi-request-consumer-impacts-data-centres.pdf
- Clayton Utz, "Co-locating batteries with data centres in Australia's NEM" (April 2025). https://www.claytonutz.com/insights/2025/april/co-locating-batteries-with-data-centres-in-australias-national-electricity-market
- HSF Kramer on National Expectations (March 2026). https://www.hsfkramer.com/insights/2026-03/national-expectations-for-the-development-of-data-centres-and-ai-infrastructure-have-been-released-what-you-need-to-know
- Energy Charter, 2025 Disclosure. https://www.theenergycharter.com.au/

### Australia — operators, projects, trade press

- Cyber Daily, "Data centre giants launch new Aussie peak body, Data Centres Australia" (Nov 2025). https://www.cyberdaily.au/security/12953-thinking-machines-data-centre-giants-launch-new-aussie-peak-body-data-centres-australia
- The Tech Capital, "Data Centres Australia names NEXTDC CEO chair". https://thetechcapital.com/data-centres-australia-names-nextdc-ceo-chair-of-new-peak-industry-body/
- AirTrunk, Blackstone acquisition completion (Sep 2024). https://airtrunk.com/completion-of-airtrunk-acquisition-by-blackstone-marking-new-era-of-growth/
- AirTrunk, MEL2 announcement (Dec 2025). https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/
- AirTrunk, Google-OX2-AirTrunk PPA. https://airtrunk.com/google-airtrunk-and-ox2-to-add-renewable-energy-capacity-in-australia/
- AirTrunk *FY24 Sustainability Report*. https://airtrunk.com/wp-content/uploads/2024/10/FY24-Sustainability-Report-by-AirTrunk.pdf
- NEXTDC ASX release on contracted utilisation (Dec 2025). https://announcements.asx.com.au/asxpdf/20251201/pdf/06sr3ff6f4q4vv.pdf
- NEXTDC, "Building the next generation of sovereign AI infrastructure" (Dec 2025). https://www.nextdc.com/news/building-the-next-generation-of-sovereign-ai-infrastructure-in-australia
- The Urban Developer on NEXTDC-OpenAI A\$7bn S7. https://www.theurbandeveloper.com/articles/eastern-creek-data-centre-550mw-openai-nextdc
- CDC Marsden Park groundbreaking. https://cdc.com/resources/news/cdc-data-centres-breaks-ground-on-new-state-of-the-art-data-centre-development-in-marsden-park-industrial-precinct/
- Microsoft Australia A\$25 bn announcement (April 2026). https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/
- Microsoft Australia FRV 300 MW PPA. https://news.microsoft.com/en-au/features/microsoft-and-frv-australia-team-up-to-add-renewable-energy-to-the-grid/
- PV-Tech on Walla Walla 300 MW commissioning. https://www.pv-tech.org/frv-australia-brings-300mw-solar-pv-power-plant-with-microsoft-ppa-to-full-operation/
- RenewEconomy on Walla Walla. https://reneweconomy.com.au/nsw-solar-farm-to-supply-microsoft-data-centres-now-fully-operational/
- AWS Australia A\$20 bn announcement. https://www.aboutamazon.com/news/aws/amazon-data-center-investment-in-australia
- Energy-Storage.News on AWS 9 Australian PPAs. https://www.energy-storage.news/amazon-australia-puts-battery-storage-centre-stage-as-it-inks-nine-ppas-for-data-centre-expansion/
- Energy-Storage.News, Fluence on data centre BESS in Australia. https://www.energy-storage.news/how-australia-can-turn-the-data-centre-boom-into-a-grid-growth-story/
- Anthropic Australia MoU. https://www.anthropic.com/news/australia-MOU
- Quinbrook Supernode press releases. https://www.quinbrook.com/news-insights/quinbrooks-supernode-battery-completes-construction/ ; https://www.quinbrook.com/news-insights/quinbrook-closes-first-250mw-stage-of-the-supernode-storage-project-at-south-pine-substation-signs-offtake-with-origin-energy/
- Mamre Road SSDA (Urban Digest). https://urbandigest.com.au/ssd-92743706-mamre-road-data-centre-campus/
- Information Age (ACS) on Mamre Road. https://ia.acs.org.au/article/2026/concern-over-australia-s-most-power-hungry-data-centre.html
- Watt Clarity on AEMO 2024 ESOO data-centre breakout. https://wattclarity.com.au/articles/2024/08/29aug-esoo-datacentre/
- Watt Clarity on AEMC Package 2 draft. https://wattclarity.com.au/articles/2026/04/05april-aemc-draft-datacentre/
- Flow Power on AEMO 2025 ESOO. https://flowpower.com.au/aemo-2025-esoo-recap/
- WWF Australia joint statement. https://wwf.org.au/news/2026/data-centre-rush-must-power-itself-says-industry-unions-and-environment/

---

*End of background note. Two underlying research drafts are kept under `background/_research_drafts/industry_response_us.md` and `background/_research_drafts/industry_response_australia.md` for traceability.*
