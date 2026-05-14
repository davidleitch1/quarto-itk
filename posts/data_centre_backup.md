---
title: "The devil's in the detail but godliness is in the top down view"
author: "David Leitch"
date: 2026-05-14
categories: ["Demand", "Networks"]
image: "../media/sydney_west_backup_costs_with_revenue.png"
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

# The devil's in the detail but godliness is in the top down view

Continuing my look at the data centre industry this note observes:

1. Data centre uptime standards for Tier IV / Rated-4 are 99.995% — about 26 minutes of permitted downtime per year. This requires every data centre to have diesel backups MW for MW. So if Australia builds 5 GW of data centres in 100 MW blocks, which is what we are currently doing, we will end up with 5 GW of diesel gensets, mostly spread around Eastern Creek in Sydney and Deer Park in Melbourne.  

   For every GW of data centre roughly \$2.5 bn is spent on diesel gensets with annual opex (mostly testing) of \$75 m. Around 40 ML of diesel has to be stored! It has to be turned over too. Untreated stored diesel only keeps for ~12 months; with active fuel polishing the inventory typically rotates every 18-24 months. Testing and actual outages (averaging less than 5 hours in Australia) consume 16 ML of diesel a year.

   When data centres are a relatively small business from an Australian energy context 99.9% uptime sounds terrific. When data centres are 10-20% of Australian electricity consumption that uptime requirement is a significant societal cost burden.

   In my opinion the industry and its customers and insurers should think about the uptime standard and work on how to build some flexibility into it. We would all be a lot happier.

2. By building the data centres bit by bit the industry is escaping the transmission related costs that facilities like Tomago have to incur. Specifically the 800 MW of data centre either in operation or being constructed around TransGrid's Sydney West terminal station has eaten up all the transmission capacity from the 330 kV "input line" and this requires the Sydney Southern Ring reinforcement to be built, but the data centres won't be paying for that. 

     If the cluster's aggregate 800-1,000 MW load were treated as a single industrial customer under the existing Australian framework, it would have:

     - Connected at 330 kV directly to Sydney West (like Tomago)
     - Paid the full connection asset cost (~A$120-240M cluster-wide rather than ~A$15-25M per operator at 132 kV)
     - Gone through a single connection-approval process with TransGrid
     - Negotiated a single TUOS arrangement
     - Been visible in TransGrid's TAPR as a named industrial customer with a specific contracted MW

     Aggregating to a single 330 kV connection is, in any case, probably cheaper than eight separate 132 kV connections.. The fact that the cluster is instead structured as eight separate operator connections each at 132 kV via Endeavour Energy is partly an artefact of how the DC industry grew (one operator at a time, each independent commercial decision) and partly an artefact of the regulatory framework not anticipating cluster-scale DC growth. 

3. Batteries can do everything the diesel gensets do, plus earn revenue from spot trading and grid services. The catch is that they're not economic beyond about 10 hours of backup — for the 96-hour tail event, you still need diesel. Or at least you do the way the industry is structured today: piecemeal, one operator at a time.

4. What if you took all the data centres at Sydney West and rebuilt them at Tomago? Then you could have one main connection point — no different from Sydney West today — but with a single behind-the-meter battery and a single "reserve", probably an open-cycle gas plant or whatever the most economic option turned out to be. On my numbers, a larger centre with centralised backup is lower cost than smaller centres each with their own backup. Of course that's not happening. Cold shower time.

5. Every aluminium smelter in Australia gets a subsidy of one sort or another. Boyne Island gets a sweet deal from CS Energy. Tomago has a low-cost contract and will move to a subsidised contract under the NSW Electricity Infrastructure Roadmap. Portland gets a subsidised electricity cost. Bell Bay, at 71 years old, gets a sweetheart deal from Hydro Tasmania — although I don't know the detail. Other than the implicit subsidy from transmission, data centres pay their way. But the implicit transmission subsidy and the negatives associated with such a large amount of diesel shouldn't be overlooked. Data centres don't provide as many direct jobs but, in my opinion, they facilitate downstream jobs..


I'm still in the early stages of thinking about this stuff, but time and tide wait for no person so I'm putting these thought bubbles out there. Feel free to pop them. It's also worth noting that in my UBS and JP Morgan days I'd have gone out and interviewed industry participants, attended management briefings, gone on site tours.  The sort of research I do now relies on my analyst trading and experience, the internet and AI, specifically Claude's ability to supercharge internet research. At the end of the day because this is a relatively new industry to me, even though I recognised NEXTDC as an attractive investment about 8 years ago, and have been programming since the 1970s, and because of the lack of "recalibration" that discussion with industry participants provides, it's quite likely this research is wrong in significant respects and readers should bear that in mind.

## Diesel gensets are killing it in the data centre boom

Once an analyst always an analyst. When I do a sector fact finding overview as I did to freshen up on data centres one of the semi autonomous process in my mind derived from 33 years of investment banking research is scanning for money making ideas. My skills are in industry analysis, supply, demand, growth, competitive structure, winners and losers. And where to invest. But you need the detail. Got to hang with the devil. But the devil has flaws — often the detail is where the insights, such as they are, come from.

As every Australian knows most of the people making money in gold mining were shop keepers and equipment suppliers rather than the average panhandler. And so it is with industries today.

And right now one of the segments flowing rivers of gold from the data centre boom is backup diesel gensets.

For a Tier IV / Rated-4 certified data centre 96 hours of backup capacity, MW for MW is required. So if 17 GW are being built in the USA that's roughly 17 GW of diesel generators, or possibly gas reciprocating engines. Partly reduced by onsite effectively self insurance generation. In Australia where 1.8 GW are under construction that's almost certainly going to be 1.8 GW of diesel generators, possibly the leading supplier Kerry Stokes' Caterpillar franchise.

### Prices up 50% over the past 3-4 years

Cushman & Wakefield's 2025 cost guide records data centre generator capital costs up 45% from Q3 2021 to mid-2024. Other electrical infrastructure has moved the same way — transformers +44%, UPS +48%, switchgear +31%. The drivers are copper, specialty steel, power electronics, specialist labour and pure OEM pricing power. None has reversed.

![Data centre backup genset market 2026](../media/dc_genset_market_2026.png){#fig-genset-market}

### Order books extend to 2028

Cummins CEO Jennifer Rumsey told the Q4 2025 call that "we're taking orders now well into 2028". Generac, in deliberate market-entry positioning, quotes 50-60 weeks (12-14 months) — half the incumbent lead time.

**Table 1. Data centre genset lead times — 2-3 MW class**

| Period     | Typical lead time | Comment                                         |
| :--------- | :---------------- | :---------------------------------------------- |
| Pre-2022   | 10–14 months      | Competitive bidding; stable.                    |
| 2023       | 14–18 months      | First AI orders begin queueing.                 |
| Q4 2024    | 18–22 months      | Hyperscalers buying multi-year forward.         |
| Q4 2025    | 22–30 months      | Cummins QSK95 cited at 18 months pre-expansion. |
| Q1–Q2 2026 | 24–30 months      | Generac at 12–14 months for new lineup.         |

*Source: OEM earnings transcripts (Cummins, Caterpillar), Mordor Intelligence, Generac press releases.*

Capacity expansions announced 2024-2026 — Caterpillar US\$725 million at Lafayette, Indiana; Cummins US\$150 million at Fridley, Minnesota; mtu US\$24 million at Mankato lifting Series 4000 output by 120%+ — do not close the gap inside the planning horizon. Caterpillar's ~125% nominal capacity lift over two years has been overrun by order intake more than doubling.

### Supply side response

Diesel gensets are essentially a commodity, so a supply-side response is already coming through three channels:

**First**, existing OEMs are expanding capacity and new entrants from India, China and South Korea are pushing up-market.

**Second**, "self-insurance" — some hyperscale data centres are going behind-the-meter on gas supply rather than relying on diesel.

**Third**, gas reciprocating engines such as smaller versions of those used at the Barker Inlet power station in South Australia are starting to replace diesel for the prime+standby role.

### Backup opex for a 100 MW site

**Annual operating cost, backup power system — 100 MW Rated-4 facility**

| Cost item                                              | US\$m/year | US\$/MW IT/yr |
| :----------------------------------------------------- | ---------: | ------------: |
| Parts, scheduled testing & operator labour             |       2.25 |        22,500 |
| Fuel, oil, polishing, quality control & rotation       |       1.10 |        11,000 |
| OEM 24/7 service contract                              |       1.50 |        15,000 |
| Insurance, dangerous-goods compliance & spill response |       0.40 |         4,000 |
| **Total annual opex**                                  |   **5.25** |    **52,500** |

  *Source: Author build-up. Maintenance and testing from Cummins and Caterpillar service literature; fuel polishing and rotation from Bell Performance and Mojo Fuel benchmarks; diesel pricing from Australian Institute of Petroleum terminal-gate data. Total opex is ~3.2% of installed capex.*



### Outages in Australia have historically been short but with extreme tails

![Data centre backup genset hours US vs Australia](../media/dc_genset_hours_us_vs_au_gt-8645887.png){#fig-hours-us-au}

Australian hyperscale sites typically clock 10-25 genset hours per year, mostly from scheduled testing rather than actual grid-driven runs, against ~35 hours for US sites (@fig-hours-us-au). The tail-event scenarios — Hurricane Sandy 4-7 days, Hurricane Ida 9 days, Texas Uri 18-72 hours, the SA black system 6-48 hours, the Victorian February 2024 storms — each sit at 24-200+ hours per event but only once every 5-20 years.

### The geography of backup at Sydney West

As I mentioned in my last note data centres in Sydney are concentrated around TransGrid's Sydney West terminal and in Melbourne around Deer Park. It's excellent that Renewmap shows this in a map together with the transmission connections — a fantastic piece of software (@fig-sydney-west-map). You can ride your pushbike on a loop in the area and never know the data centres are there. Just off screen is the Sydney Southern Ring exit corridor.

![Sydney West data centre cluster map. , Source:Renewmap.com.au](../media/image-20260513143207590.png){#fig-sydney-west-map}

By and large the data centres are spread out around the 132 kV lines that come out of the Sydney West terminal station. Naturally the terminal station has N-1 redundancy but just as clearly if the centre itself went offline it would be a problem and 800 MW of diesel would start running. Initially the on-site UPS battery picks up the load. The diesel gensets start within about 10 seconds, but the UPS battery is sized for 5-10 minutes to allow for re-tries, load transfer and any genset that fails to fire on first attempt.

To me, as a space cadet learning about the specifics of this, there are questions about all the diesel that will be stored in the area and who really wants 800 MW of diesel generators running next door. However I have zero doubt that this has all been carefully considered.

## Now the big question: could batteries replace the diesel backups

Since I know little about either data centres or diesel generators and only a little bit more about batteries clearly I am supremely well qualified to have an opinion about this. It's a bit like climate change, the less you know the more confident you are in your opinion.

The outage data appears to support a view that a say 4-8 hour battery could handle the vast majority of the outages and could also earn revenue from the grid via frequency control, and with more risk tolerance even trading revenue.

But batteries can't cover the tail risk. Batteries are cheaper for most outages a Sydney data centre is likely to experience (@fig-sw-costs). After all an extended complete outage at Sydney West would cause a few eyebrows to be raised.



![Sydney West data centres backup costs (no revenue. Source:ITK)](../media/sydney_west_backup_costs.png){#fig-sw-costs}

### Revenue

So far as I can find out, even with 1800 MW of existing data centres — the vast majority of which must have diesel gensets — the industry does not participate in RERT. From January 2019 to December 2023, the RERT mechanism paid out A$172.5 million in reserve contracts (peak A$131.7M in 2022). The typical participants are:

- Industrial loads that can be curtailed (smelters, refineries, cold storage)
- Aggregated commercial loads via demand-response service providers
- Standby generation at industrial sites (mining, food processing, hospitals)
- Mothballed power plants being temporarily reactivated (SA's Snuggery and Port Lincoln diesel stations is the live 2024-25 example)

**Because:..**

 The DC's whole value proposition is uptime. Tier IV / Rated-4 facilities have multi-million-dollar SLA penalties for any unplanned downtime. Voluntarily transferring load to backup creates a non-zero risk of failed transfer — and the asymmetric upside (a few hundred thousand dollars of RERT revenue) is dwarfed by the downside (multi-million-dollar customer compensation if a  transfer fails).

Insurance underwriters don't love it. Property and business-interruption insurance for critical power systems treats standby gensets as emergency-only. Operating them in a paid-grid-service capacity could be construed as primary power usage and trigger insurance reclassification.

The Australian RERT framework wasn't designed for DCs. The 2024-25 IRR contracts (85 MW in NSW, 605 MW short-notice reserves during November 2024 heat-stress event) are sized for industrial-scale single resources. The DC fleet is structurally different — many small distributed generators behind one cluster — and would need an aggregator-level participation framework.

**What's changing in the framework:**

1. IESS rule (Integrating Energy Storage Systems, in force 3 June 2024). Creates the Integrated Resource Provider (IRP) category that accommodates bi-directional resources — grid-scale storage, hybrid facilities, aggregators of small generation and storage. A DC operator with on-site BESS + diesel + load could in principle register as an IRP and participate in spot energy, FCAS and RERT through one framework. The transition period for bidirectional units extended to 3 March 2025 — so the framework is now fully live.

2. AEMC consultation on extending VPP rules to backup generators. Mentioned in the May 2025 AEMC media materials. If adopted, would explicitly let backup gensets compete in VPP energy and ancillary services markets.


Batteries can earn FCAS, RERT, trading and capacity revenue streams. In this first pass I was just interested to see how that improved the battery competitiveness, and the answer is: a lot (@fig-sw-costs-revenue).

![Sydney West data centres backup costs with BESS revenue, Source:ITK](../media/sydney_west_backup_costs_with_revenue.png){#fig-sw-costs-revenue}

But the batteries still can't deliver 96 hours of Rated-4 backup. 96 hours is 4 days and nights. It seems to me that if we are in that territory it's a bit of a lottery whether it's 3 days or 6 days. The events are going to be so infrequent as to be impossible to attach any reasonable probability.

What this analysis shows is that, using my revenue assumptions, batteries could cover everything but tail events at a lower cost than diesel gensets.

### Guessing at configurations that might work

The table compares five backup configurations for a single 100 MW IT site (@fig-configurations). Config A is the current decentralised default. Config B keeps the full 96-hour diesel but adds a 4-hour battery for revenue. Config C goes further — shorter diesel reserve, relying on the public grid to restore service within 24 hours of any credible failure.

![Backup configurations for a single 100 MW data centre. Source:ITK](../media/dc_backup_configurations.png){#fig-configurations}

### Grid upgrade - shift the beyond 24 hour risk to TransGrid

The following was suggested by Claude as required to shift from the 96-hour diesel standard to a 24-hour standard. The cost saving is relatively small but the community benefit via lower levels of diesel storage is arguably significant.

#### 1. Physical infrastructure — N-2 at Sydney West

The current N-1 configuration at Sydney West tolerates any single contingency (one transformer, one line, one breaker) without losing load. The credible failure modes that drive longer-than-24-hour restoration today — busbar faults, multi-tower collapse, two-line loss during planned outage — are not N-1 protected.

**Specific kit needed**

| Component                                                    |                   Indicative AU\$M |
| :----------------------------------------------------------- | ---------------------------------: |
| Third 330/132 kV transformer at Sydney West (so the 600 MVA fleet becomes N-2 capable) |                              30-60 |
| Third 132 kV cable circuit corridor to the cluster (separates Eastern Creek and Huntingwood feeds from a common single-corridor risk) |                             50-150 |
| Pre-positioned spare 330/132 kV transformer at TransGrid depot, plus transport and rapid-install infrastructure |                              30-50 |
| Busbar protection upgrades (duplicate protection systems for the 330 kV bus at Sydney West) |                              10-20 |
| Sydney Southern Ring completion (South Creek 500/330 kV substation already under construction — provides upstream redundancy) | already in TransGrid 2023-2028 RAB |
| **Total cluster-specific physical investment**               |                        **120-280** |

*Source: TransGrid Transmission Annual Planning Report 2023; Sydney Southern Ring project documentation*

Most of this can be retrofitted to the existing Sydney West site over a 3-5 year program. It's not a greenfield project — it's incremental capacity and redundancy on top of existing infrastructure.

#### 2. Contractual SLA from TransGrid

Without a binding SLA, the physical infrastructure doesn't change the DC operator's audit obligation. The Rated-4 auditor needs a documented commitment that any credible failure will be restored within 24 hours. **This is not currently a product TransGrid offers.**

What it would look like:

- TransGrid (and ultimately AEMO as system operator) contractually commits to a 24-hour maximum restoration window for any credible failure within the contracted reliability footprint
- Specified pre-positioned spares, response-team SLAs, backed by insurance or AER-approved bonding
- Penalties payable to the customer if breached
- Tied to specific connection points (Sydney West cluster customers in this case)

The closest existing analogue in Australia: **the Reliability and Emergency Reserve Trader (RERT)**, where AEMO contracts in advance for emergency response capacity, with payments for availability plus payments for activation. The Sydney West reliability SLA would be a customer-side version of the same idea — TransGrid pre-contracting for guaranteed restoration time, with payments coming from the contracted customers.

#### 3. AEMC regulatory framework — the "negotiated reliability tier"

The AEMC's National Electricity Rules don't currently recognise customer-side negotiation of TNSP reliability levels. TransGrid's reliability obligations are set by the AER revenue determination process and the AEMC's reliability standards, not by customer contract. A new rule category would be needed:

- A "negotiated reliability tier" framework allowing a cluster of high-reliability customers to contract directly for enhanced TNSP reliability in exchange for a defined customer-side backup obligation
- Cost-allocation tied to the avoided incremental investment (Wallumatta STS contingent project precedent)
- Independent audit and SLA enforcement
- Interface with TIA-942 / Uptime Institute tier audits so the AEMC-recognised reliability counts toward Rated-4 / Tier IV compliance

The AEMC Package 2 transmission cost-allocation work (final mid-2026) is the natural vehicle for introducing this.

#### Cost-allocation summary

If all three pieces were in place, who pays for what:

**Cost allocation across the three components**

| Component                                                    | Who pays                                                     |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Sydney West physical upgrade (A\$120-280M)                   | DC cluster customers via cost-reflective tariff (Wallumatta model) |
| TransGrid SLA pre-positioning and emergency-response capability | DC cluster customers via reliability service fee (~A\$5-15M/yr cluster-wide) |

*Source: AER Contingent Project framework (Wallumatta STS Macquarie Park precedent, Feb-Oct 2025); AEMC Package 2 consultation materials; ITK analysis.*

Cluster-wide annualised cost: ~A\$8-22M/yr (capex annualised plus SLA payments). Cluster-wide saving from spec reduction: ~A\$17M/yr in diesel opex plus ~A\$60M of one-off diesel infrastructure capex avoided. **Net cluster-wide benefit roughly neutral to positive on direct dollars — but the social and environmental benefits (75% reduction in metropolitan diesel inventory) are the larger gain.**

