---
title: "Data centre space cadets"
author: "David Leitch"
date: 2026-05-12
categories: ["Demand", "Markets"]
bibliography: data_centre_space_cadets.bib
link-citations: true
reference-section-title: "Sources"
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# Deus ex machina  

Opposition to data centres in the USA has increased, spreading out from specific community level concerns to a broader argument about the impact on electricity prices. These concerns could harden into a widespread movement opposing AI and data centres, matched by a counter-movement insisting "AI and data centres are wonderful".

Demand for data centres in Australia is growing strongly. Renewmap identifies close to 1800 MW under construction [@renewmap-2026]. Despite limited disclosure, what is being built in Australia is nothing like what Amazon, OpenAI and Meta are building in the USA.

Although data centre size is typically expressed in MW, in reality the power cost and power supply is at most the second most important cost item. USA AI data centre costs are dominated by depreciation on the GPUs and the associated "racks" and clusters.

As far as power goes, in the USA new data centres are dominated by gas; renewables rarely get a mention. Whether in the USA or Australia backup is done with diesel gensets. The USA industry argues, to the extent they have any interest, that gas is the only technology available near-term. I'd argue that renewables can be built far more quickly than gas generation. And that using gas actually undermines the industry's ability to earn society's trust.

However the more general concern is the idea that data centres have to bring their own generation. Since when? Does every house have to bring its own generation, does every shop, where do we draw the line?

Higher prices provide the signal to build new supply. If data centres increase demand, but also provide firming, then new supply gets built anyway. That's how the market is supposed to work.

Requiring data centres to bring their own supply also ignores the benefits of a portfolio. Properly designed, the grid provides the lowest-cost supply on average. Self-supply works when things are going well, but the insurance value of large diversified supply and demand shows up when there is scarcity. We see this insurance value at the regional level, let alone with aluminium smelters or data centres trying to do it all on their own. I return to this point at the end of the note.

Is Australia a good place to build data centres? It doesn't matter for a few years: chips are so hard to get you couldn't fit one out with the latest Vera Rubin or Trainium chips for three or four years. We are a long way from the consumers, but other than that we have the land, we have cheap labour, cheap renewable electricity that will provide sustainable power for decades and lots of software skills. We also have property developers that can compete with the best. So possibly we could be a data centre destination of choice. You can't rule it out.




## Enhar BESS conference had some great data centre presentations

For some time now data centres have been the talk of the town, even more so than batteries. Even at the Smart Energy conference, I'm told, solar panels were barely worth a mention and wind energy might as well not exist for all the interest the conference showed in it.

But at Enhar the role of data centres and where batteries fit in was well discussed with two strong presentations from Keith Middleton from Fyfe and Damien Sanford from Celero Infrastructure in a session chaired by Muneeb Anwar from Enhar. The Enhar conference had that nice vibe of the "in crowd" talking to each other.

Why would Amazon, Anthropic or OpenAI choose Australia — 26 million people, thousands of km from the real market?

Surely data centres were just the next hydrogen thought bubble, egged on by policy makers desperate to prove Australia was an attractive investment destination.

If there aren't going to be any data centres, then the angst about whether they are good or bad is less of an issue.

What I noticed from the presentations is that the presenters focussed, quite correctly because that was their brief, on the technical side of things, and the contribution that batteries can make. However this struck a note of discord with me because I'd just been in a prior session where the entire discussion from the battle-hardened renewable energy developers was all about "social licence". Social licence is a convenient term to reach for, but it is itself value-laden.

As I show in this note, in the USA the data centre industry is already deep into a social licence minefield it hardly knows it's in. AI labs — this generation's "masters of the universe" — and the creators of social media don't seem to understand that they are just as subject to its laws and mores as anyone else.

Even the best of them, Anthropic in my book, has just done a deal to rent the most polluting data centre recently built in the USA and the one with the least "social licence".

In this note therefore I've tried to piece together the state of play in the USA. This may offer some clues — first, why Australia might be an alternative to Virginia, and second, how Australia can avoid the same naivety.

## The USA industry: 17 GW under construction

Gonna let these tables speak for themselves.

![dc_fleet_at_a_glance](../media/dc_fleet_at_a_glance.png){#fig-dc-fleet-at-a-glance}

In the USA gas is the primary fuel.

![dc_power_fuel](../media/dc_power_fuel.png){#fig-dc-power-fuel}

So I think that's pretty dumb of the USA operators. The 13 GW of gas means more carbon emissions and more long-term reserve issues. Gas is relatively slow to ramp up and down. It's short-termism. After all, when your main focus is "where are the chips coming from?" and "who pays for them before my IPO this year?", long-term power supply issues can look after themselves. As we will see, community concerns are not really about fuel source — at least not right now. As I say, this is an industry with an ultra-short-term focus.

We can also look at the pipeline by tenant and geography.

![dc_top_projects](../media/dc_top_projects-8468989.png){#fig-dc-top-projects}

## Capex is driven by equipment cost

If I work off USD \$47bn/GW for the 17 GW actually under construction, that's about USD \$0.8 trillion.

![dc_capex_per_gw](../media/dc_capex_per_gw.png){#fig-dc-capex-per-gw}

## Equipment availability is the key constraint, not energy or transmission

The global rate at which new AI data centres can actually be energised is not ultimately set by transmission queues or local zoning fights — it is set by TSMC. AI accelerators^[**Accelerator** — umbrella term for AI-specialised chips (Nvidia GPUs, Google TPUs, Amazon Trainium); the workhorses inside an AI data centre.] consumed roughly 9% of TSMC's leading-edge N3 wafer^[**N3 wafer** — TSMC's 3-nanometre process node, the current leading edge for AI accelerators.] output in 2025; SemiAnalysis estimates that share reached 60% in 2026 and projects 90% by 2027 [@semianalysis-silicon-shortage-2026]. Nvidia alone accounts for around 80% of the accelerator-wafer share, with Broadcom — which fabricates Google's TPUs and Amazon's Trainium chips — the only meaningful second customer. The N3 wafer price has lifted from about US$20,000 to US$23,000 over two years, and HBM^[**HBM (High Bandwidth Memory)** — stacked memory paired with each accelerator.] is in structural deficit through at least 2027. The practical consequence is that headline hyperscaler capex announcements run well ahead of what TSMC and its memory partners can actually deliver, so the binding global constraint on AI data-centre capacity through 2027 is silicon, not megawatts.

## Energy demands of inference and training

A year ago the view was that inference^[**Inference** — using a trained model to answer queries; ongoing operational compute.] would have lower capacity utilisation than training^[**Training** — building a model by running optimisation across vast datasets; a discrete, finite compute job.]. So a 100 MW training load would use more energy than 100 MW devoted to inference (answering user queries). However reasoning models^[**Reasoning models** — newer class of models that produce extended internal "thinking" tokens before answering, multiplying inference compute per query.] make that assumption questionable.

![reasoning_models_lineage](../media/reasoning_models_lineage.png){#fig-reasoning-lineage}

To my way of thinking as far as model adoption goes the table shows just how far off the pace Meta is. However Meta's data centres might still be quite profitable, just not running Meta's models.

![reasoning_compute_share](../media/reasoning_compute_share.png){#fig-reasoning-compute-share}

Reasoning probably already represents the largest share of LLM compute, and that share is likely to keep increasing. The implication is that capacity utilisation in a data centre used for AI is likely to be high under any circumstances.

## Data centre opex — depreciation dominates

Energy becomes a bigger share of opex the larger the data centre and the higher the capacity utilisation. Fixed annual costs like labour don't scale with size. Water costs are regarded as minor but you have to have the water. As the table shows, depreciation is by far the largest cost. I worked off 5 years on the equipment, but currently, due to chip shortages, perhaps 6 years is economic. On the depreciation point, new chip generations can't simply be dropped in to replace old ones. Racks and cooling need to be replaced. Building shells may be reusable, and no doubt in Australia new data centres are designed from that point of view. Eventually the value of the revenue produced falls below the energy cost.

![us_opex_by_utilisation](../media/us_opex_by_utilisation.png){#fig-us-opex-utilisation}



## The social issues

You don't need to be an expert to know that the population at large generally has concerns about anything different or new.

Anything that increases productivity is immediately suspect because some jobs will disappear. The jobs that disappear will be much more obvious than the new jobs that are created. Throughout history, from at least the invention of the wheel, productivity has resulted in some jobs being lost but a greater number of new jobs being created. Unions will never, ever understand this and these days it's pretty hard to get the message through to the broader population. Still it must be true because the number of employed people tends to grow, and — except in Australia — productivity tends to increase. The invention of the car saw horse jobs decline but auto jobs increase far more. Etc.

Until late 2024, opposition to US data centres was overwhelmingly local — county-level zoning fights about noise, water, traffic, viewshed and lost farmland. By mid-2026 it is also a generalised national political story, driven by three converging shocks: PJM capacity-auction prices clearing 833% above the prior auction in July 2024 and re-clearing at the new administrative cap a year later; a sequence of FERC orders culminating in the December 2025 PJM co-location order; and a wave of state legislation in 2025-26 (more than 300 bills tracked by MultiState) seeking to make hyperscalers pay their own grid costs. The clearest single piece of evidence that opposition has broadened is the Washington Post-Schar School Virginia poll: voter "comfort with a new data centre in your community" fell from 69% in 2023 to 35% in March 2026.

The Trump administration is the most pro-data-centre actor in the system — Stargate was unveiled at the White House on the second day of the second Trump term, followed by Executive Order 14148 accelerating federal permitting and four nuclear executive orders in May 2025. State public service commissions across the partisan spectrum are pushing back through new rate classes, minimum-bill provisions and stranded-cost protections.

The local issues have not gone away — if anything they have intensified, with the xAI Colossus Memphis air-quality case becoming a national environmental-justice flashpoint, and the Prince William Digital Gateway court loss demonstrating that procedural land-use challenges can defeat 17 GW of approved development. But the generalised cost-shifting and AI-environmental-impact frames have now overtaken purely local quality-of-life concerns as the political driver.

### Recurring local issues

**Noise.** The constant low-frequency hum from chillers and cooling fans is the most-cited grievance in densely-developed clusters. Loudoun County's industrial noise cap is 55 dB at residential property lines; one CloudHQ measurement reached 90 dB at the boundary, with at least a dozen 2024 complaints against Vantage [@wusa9-loudoun-noise].

**Water.** The single most-cited concern in arid-state and drought-stressed locations. Of 25 projects cancelled in 2025, water use was raised in over 40% of cases [@commobs-2026].

**Air emissions.** xAI's Colossus campus in Memphis is the headline case. University of Tennessee aerial-imagery analysis documented at least 35 gas turbines on site (xAI's previously-disclosed count was lower); Earthjustice and SELC have argued the site became the largest single industrial NOx source in the 11-county Memphis area, with documented capacity to emit more than 1,700 tonnes of NOx, 180 tonnes of particulate matter, 500 tonnes of carbon monoxide and 19 tonnes of formaldehyde per year.

In Loudoun County alone, approximately **4,700 diesel backup generators are now permitted** with about 12 GW of nameplate capacity.

**Farmland and rural character.** Saline Township, Michigan, is the case-study reference point. The township board voted 4-1 in March 2025 to deny rezoning for the 1.4 GW Stargate (Related Digital / Oracle / OpenAI) project. Two days later the developer sued under Michigan's exclusionary-zoning doctrine, arguing that because Saline Township had no industrially-zoned land at all, a "necessary" use could not be excluded altogether. The township settled within weeks; construction began; the Michigan PSC approved the DTE supply contract in December 2025 with conditions; Fortune's May 2026 reporting confirms the facility is operational on a path to 1.4 GW. Residents secured roughly \$14 million in community benefits including fire-department funding and farmland preservation [@fortune-saline; @mipublic-saline].

## Emerging identity (for or against) uses community cost as the wedge

The shift from local to generalised opposition runs through residential electricity bills, environmental-justice litigation, federal regulatory action and state legislation. The political coalition is cross-cutting; the regulatory consequence is a structural rate-design pivot that will outlast the news cycle.

### Residential electricity bills as the political driver

The PJM Interconnection 2025/26 Base Residual Auction, held in July 2024, cleared at \$269.92/MW-day across most of the RTO — an **833% jump** from \$28.92/MW-day in the prior auction. The Dominion zone cleared at \$444.26/MW-day; Baltimore Gas and Electric at \$466.35/MW-day. The 2026/27 auction, held July 2025, cleared at the new \$329.17/MW-day administrative price cap across the entire RTO, with cleared volumes only 139 MW above the reliability requirement [@pjm-2025-26; @pjm-2026-27; @ud-pjm-record].

The PJM Independent Market Monitor (Monitoring Analytics) attributed the 2025/26 increase principally to data centre demand: in a November 2025 filing, it estimated that data centres accounted for **63% of the 2025/26 auction price increase**, equivalent to \$9.3 billion of the \$14.7 billion total capacity bill. Across the most recent three auctions, data centre forecasts contributed 45% of \$47.2 billion in cumulative capacity costs [@imm-imm-complaint; @ud-imm-attribution]. The industry counter-view, advanced by SemiAnalysis in March 2026, attributes the price step-change primarily to a 34.4 GW (20%) supply contraction — Capacity Performance accreditation reform after Winter Storm Elliott (-14 GW), coal closures (-10 GW) and renewable derating and other reductions (-10 GW) against only +4.5 GW of new build — with data-centre demand setting the auction's clearing level rather than causing the spike [@semianalysis-electric-bills-2026].

Public service commissions across the partisan spectrum moved through 2025-26 to put data centres into separate rate classes with minimum-bill provisions and stranded-cost protection. The structural shift is the most consequential element of the entire backlash because rate-design changes operate for decades.

Legislators across both parties introduced more than 238 data centre bills across all 50 states in 2025; over 40 were enacted in 21 states. 

Microsoft committed in 2024 to "next-generation" zero-water-cooling data centre designs and matched 100% of its global electricity consumption with renewables in 2025 [@msft-sustainability]. However, Microsoft is reported to be reconsidering its 24/7 carbon-free energy matching^[**24/7 CFE (Carbon-Free Energy matching)** — commitment to match every hour of consumption with carbon-free generation in real time, rather than just matching annual volumes; Google's 2030 moonshot.] pledge in light of AI demand growth [@geekwire-msft-cfe; @dcd-msft-cfe]. Google maintains its 24/7 CFE moonshot for 2030 but its operational emissions have risen sharply with AI [@google-sustainability]. 

## What polling shows

### USA National

- **Pew Research (September 2025; updated March 2026)**: 50% of US adults are more concerned than excited about AI in daily life; 10% more excited than concerned. 25% expect AI to have a negative environmental impact; 20% positive [@pew-ai-2025; @pew-ai-2026].
- **Pew Research (October 2025) on data centres specifically**: Americans hold positive views of local employment and tax-revenue benefits but more strongly negative views of energy use and environmental cost [@pew-dc-energy].
- **Morning Consult (October 2025)**: 37% of voters support a ban on AI data centre construction in their communities; 39% oppose; 24% unsure. After being primed on energy-cost impacts, support for a ban rose six points to 43% [@morning-consult-oct25].
- **University of Chicago (2025)**: 72% of Americans are at least somewhat concerned about AI's environmental impact; 41% at least very concerned [@uchicago-ai].
- **AP-NORC (October 2025)**: electricity bills are a "major" source of stress for 36% of US adults [@apnorc-bills].

### Virginia (the most-polled state)

- **Washington Post-Schar School (March 26-31, 2026, n=1,101)**: 35% of Virginia voters comfortable with new data centres in their community, **down from 69% in 2023**. 57% believe data centres are negatively affecting home energy bills; 14% positive. 59% say negative impact on local environment; 14% positive. Support for tax breaks fell from 61% to 37%. **67% want to end the sales-tax exemption; 26% want to continue it** [@wapo-poll-2026; @wapo-tablet-2026].
- **Wason Center (CNU, January 2026)**: 86% support requiring site assessments before approval covering water, grid, carbon and agricultural impact. 81% support a noise study for sites near homes or schools. 69% support prohibiting data centres within a mile of a national park, state park or historic site. 63% support requiring renewable or nuclear power for new data centres [@wason-jan26].
- **Global Strategy Group (CCAN-commissioned, 2025)** — Democratic polling firm; advocacy commission, flag accordingly: 92% of likely Virginia voters say lawmakers are failing to properly manage data centre growth [@ccan-poll-2025].

## Are attitudes changing?

Yes. The evidence is consistent across three independent measures:

1. **Polling.** The Virginia 35% comfort number (down from 69% in two years) is the most striking single data point. National Pew, Morning Consult and University of Chicago surveys all show clear majorities (a) more concerned than excited about AI overall and (b) negative on the environmental and energy footprint of data centres specifically. The energy-bill prime increases anti-data-centre sentiment by six points in the only experiment we have.

2. **Political behaviour.** Data Center Watch's \$98 billion of blocked or delayed projects by mid-2025; the Warrenton Virginia council being voted out and replaced by a council unanimously opposed to Amazon's local data centre; Virginia's flagship cost-shift bills passing the General Assembly twice in 2026; state legislatures passing more than 40 substantive bills in 21 states in 2025; the AEP Ohio tariff and PPL settlement creating new precedents for separate large-load rate classes.

3. **Regulatory behaviour.** FERC's November 2024 rejection of the Talen-Amazon ISA^[**Talen-Amazon ISA** — In March 2024 AWS bought Talen's Cumulus data centre campus next to Talen's 2.5 GW Susquehanna nuclear plant in Pennsylvania for US\$650 m, planning to draw power direct from the reactor "behind the meter" and bypass the PJM grid. PJM filed an amended Interconnection Service Agreement raising permitted co-located load from 300 MW to 480 MW. FERC rejected it 2-1 in November 2024, accepting Exelon and AEP's argument that the arrangement would shift transmission costs onto other ratepayers. The landmark precedent on whether hyperscalers can co-locate behind existing generation and bypass the grid.], its February 2025 show-cause order, and its December 2025 PJM co-location order together represent the most consequential federal regulatory pivot on large-load arrangements in a generation.


## Australia

At present Australia is structurally quite different to what is happening in the USA.



![dc_australia_overview](../media/dc_australia_overview-8535989.png){#fig-dc-au-overview}

1. Other than NextDC, disclosure of anything is very limited.

2. In general Australian data centres are a partnership between the operator who builds a site to a generic spec and the tenants who fit it out. Such designs cannot reasonably be used for training AI, although they could conceivably be used for inference work.

3. NextDC has disclosed its contracted load, but there is little or no disclosure for AirTrunk or CDC. CDC has made some tenant disclosures at its Brooklyn opening. Despite the lack of disclosure, the capital expenditure is unlikely to have been made without at least a significant degree of contracting. In that sense it's no different to any other property development.

4. The new data centres under construction are largely based around two terminal centres, Deer Park (Ausnet) in Melbourne and Sydney West (Blacktown Transgrid)

5. Each data centre does the required backup via diesel gensets (so someone is making a lot of money). AirTrunk claims to have 80% renewable PPAs across the fleet [@airtrunk-renewables] and NextDC has "Climate Active Carbon Neutral" certification^[**Climate Active** — Australian Government-administered carbon-neutral certification (formerly the National Carbon Offset Standard): organisations measure emissions, reduce where possible, and buy offsets for the remainder. It does not require renewable electricity. The scheme has been criticised for over-reliance on offsets, and several large corporates including Telstra have exited.] [@nextdc-climate-active].

   ![dc_australia_top10_matrix](../media/dc_australia_top10_matrix-8499063.png){#fig-dc-au-top10}

## Australian community and political attitudes

Australia has had no equivalent of the US political moment. Local opposition is real but small in scale, council-led, and procedurally weak — the State Significant Development pathway in NSW and ministerial call-in in Victoria have routinely overridden council objections. There is no Australian equivalent of the Data Center Watch \$160bn-blocked tally, no Title VI civil-rights litigation, no Washington Post-Schar School voter-comfort poll showing a 34-point drop, no PJM capacity-auction shock translating into residential bill politics, and no Talen-style co-location decision requiring AEMC to write new rules.

There is:

- A **NSW Legislative Council inquiry** (Greens-initiated, chair Abigail Boyd, submissions closed 27 March 2026, hearings May 2026, report due 30 September 2026) [@nsw-legco-dc-inquiry-2026] — the most likely vector for a generalised political moment
- A **"must power itself" coalition** statement (23 February 2026) signed by twelve industry, union and environmental groups demanding 100% additional renewables [@must-power-itself-coalition-2026] — pre-empted by the Albanese government's National AI Plan *Expectations* (11 December 2025) [@aus-gov-ai-plan-2025]
- Council-level objections (Lane Cove, Ryde, Penrith, Blacktown, Maribyrnong)
- An administrative cost-allocation settlement working through the **AER contingent-project mechanism** rather than through political rate cases

The Albanese government released the National AI Plan and accompanying *Australian Government's expectations of data centres and AI infrastructure developers* on 11 December 2025 [@aus-gov-ai-plan-2025]. The five expectations are: national interest, energy transition (with explicit "full share of new grid connectivity" and "underwrite new renewables" language), water sustainability, skills and jobs, and research/innovation. The instrument is not legally binding — the enforcement device is the bilateral Memorandum of Understanding. **Microsoft signed an A\$25bn MoU in April 2026 binding itself publicly to the Expectations** [@microsoft-aus-mou-2026]; Anthropic signed the first AI-developer MoU in April 2026 [@anthropic-aus-mou-2026].

### The "must power itself" coalition

The joint statement of 23 February 2026 is signed by twelve organisations: Clean Energy Council, Smart Energy Council, Electrical Trades Union, ACF, WWF-Australia, RE-Alliance, Climate Energy Finance, Nature Conservation Council NSW, Environment Victoria, Queensland Conservation Council, Sunrise Project Australia and Carbon Zero Initiative.

The four demands are: (1) all new data centres matched 100% with *additional* renewable generation from day one; (2) operators pay full grid-connection costs; (3) demand-flexibility mechanisms integrated; (4) workforce training contributions.

## "Must power itself" has some muddy thinking

An emerging trend in Australia and in the USA is that data centres have to bring their own power. In the USA the multi-billion-dollar data centres can do this — and are doing it — with facility-specific power, e.g. their own gas generators. Nevertheless each of them is then backed up with its own diesel sets.

In Australia there is a coalition of groups that want each data centre to provide its own power or perhaps to show it has caused sufficient renewable generation to be built.

In my opinion — and this stems from my background as a finance analyst and from a decade of work on aluminium smelters — this is basically a dumb idea, or at least should not be implemented the way it sounds.

The basic point is that it's no more sensible for a data centre to be stand-alone, disconnected from the grid, than it is for the individual house, even if the house has a battery.

The grid is in effect a giant insurance scheme that means every consumer can access the common supply when needed, even if the consuming unit is largely self-sufficient.

Imagine a data centre running from a wind farm and batteries. You need a lot of batteries. The same goes for a data centre running off solar and batteries. Same rules apply.

Now imagine a data centre in Melbourne and one in Sydney. It's raining in Sydney and sunny in Melbourne. If they are both powered by solar, and assuming away transmission (or assuming it's done in markets rather than physically), then fewer batteries are needed because the batteries at the centre still receiving sun can be used to help the centre where it's raining.

Equally, adding a wind farm would reduce portfolio volatility, meaning less firming and lower overall cost. To me this is so bloody obvious as to be embarrassing to write out. But it seems to be completely over the heads of the "must power itself" agitators.

One way forward might be an independent company — call it "Data Centre Power Supply" — to provide firmed power. Each data centre would buy shares in the company according to its share of the power required, and the company would build a portfolio of firmed power. Such portfolios already exist. Snowy Hydro for instance already has one, but the data centres can't buy a share of Snowy Hydro.

Snowy is not the only option: Tilt or Brookfield Renewable Australia (Neoen) could offer such a portfolio. Of course "co-ops" basically end up fighting with each other, but the point is there are vast savings to be made.

The most obvious example would be batteries at the Transgrid and Deer Park terminal stations that could supply services to all the data centres at those locations — at a minimum reducing diesel usage, but also being used to firm renewable power that the data centres might contract.

Equally, if the data centres contracted a diverse portfolio — even though they are close to co-located — the shared firming might lower their overall costs.

## Further reading

- **JLL, *2026 Global Data Center Outlook*** — for the broadest published estimate of US data centre capacity under construction (35 GW, 92% pre-committed, with more than 10 sites of 1 GW or larger). <https://www.jll.com/en-us/insights/market-outlook/data-center-outlook>
- **SemiAnalysis newsletter** — for the detailed analysis behind the "silicon, not megawatts" argument and the contrary view on what is actually driving PJM capacity prices. <https://newsletter.semianalysis.com/>NENEX
