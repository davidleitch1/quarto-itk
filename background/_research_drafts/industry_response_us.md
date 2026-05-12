# What the US data centre industry says about lowering electricity costs

*Research draft — May 2026*

This note compiles the principal arguments the US data centre industry, its
academic allies, hyperscaler sustainability teams and consultant economists
have advanced to claim that large new loads can be integrated *without*
raising prices for other customers — and, in some framings, can lower them.
It privileges sources from 2024–2026 and flags advocacy bodies explicitly.
The companion question of whether utility regulators or independent market
monitors accept those arguments is dealt with elsewhere; the focus here is
on the industry's own affirmative case.

---

## 1. The "flexible load" argument

### 1.1 Norris et al. (Duke Nicholas Institute), February 2025

The single most-cited industry-friendly study published in the last 18
months is Tyler H. Norris, Tim Profeta, Dalia Patino-Echeverri and Adam
Cowie-Haskell, *Rethinking Load Growth: Assessing the Potential for
Integration of Large Flexible Loads in US Power Systems*, Duke University
Nicholas Institute for Energy, Environment & Sustainability, 11–13 February
2025 [Source: https://nicholasinstitute.duke.edu/events/rethinking-load-growth-assessing-potential-integration-large-flexible-loads-us-power-systems].

Headline finding: across the 22 largest US balancing authorities, which
serve roughly 95 % of national peak load, the existing system could absorb
about **76 GW of new load if those loads are willing to curtail an average
of 0.25 % of their annual energy**, **98 GW** at 0.5 % and **126 GW** at
1.0 % [Source: https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/]. Average curtailment hours scale
correspondingly — about 85 hours per year at the 0.25 % level, 177 hours at
0.5 % and 366 hours at 1.0 %. In roughly 88–90 % of the curtailed hours at
least half of the new load would still be served [Source: https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/].
Largest balancing-authority headrooms at the 0.5 % curtailment threshold
are PJM (≈18 GW), MISO (≈15 GW), ERCOT (≈10 GW), SPP (≈10 GW) and Southern
Company (≈8 GW) [Source: https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/].

Two qualifiers that industry briefings frequently omit are explicit in the
paper: the analysis **does not model intra-zone transmission constraints**
and uses **historical peak demand without an additional reserve margin**
[Source: https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/]. Norris's own ISO-NE briefing on
27 March 2025 frames the headroom as an upper bound contingent on those
assumptions [Source: https://www.iso-ne.com/static-assets/documents/100021/march_clg_meeting_speaker_norris_03_27_25.pdf].

The 76 GW number is now ubiquitous in industry advocacy — it appears in EPRI
materials, Data Center Coalition speaking points and policy-maker
testimony — and is rarely accompanied by the transmission/reserve-margin
caveats.

### 1.2 EPRI DCFlex initiative

EPRI announced its Data Center Flexible Load Initiative (DCFlex) on 5 March
2025, with founding membership of about 15 utilities, IPPs and hyperscalers
including Google, Meta, NVIDIA, Constellation, Duke Energy, NRG, PG&E,
Portland General Electric, Southern Company and Vistra [Source: https://www.utilitydive.com/news/epri-launches-data-center-flexibility-initiative-with-NVIDIA-google-meta/731490/].
By early 2026 membership had grown to about 40 organisations including
Dominion Energy, ERCOT, PJM, Microsoft, the New York Power Authority,
RTE (France), PPC (Greece) and Schneider Electric [Source: https://www.latitudemedia.com/news/epri-takes-its-data-center-flexibility-project-global/].

DCFlex's stated programme is to deploy **five to ten "flexibility hubs"**
between 2025 and 2027 that will field-test computational scheduling,
backup-generator dispatch, on-site solar/storage and other flexibility
options. EPRI's public site reports nine active demonstration sites as of
mid-2026 and has introduced what it calls the "Flex MOSAIC" performance
framework intended to standardise flexibility measurement across
sites [Source: https://dcflex.epri.com/]. EPRI's underlying claim is that
data centres could rise from roughly 4 % of US electricity in 2024 to
9–17 % by 2030, making the integration question urgent [Source: https://dcflex.epri.com/].
*(Note: EPRI is a utility-funded research body, not strictly advocacy, but
hyperscaler co-funding of DCFlex makes it appropriate to flag the framing
interest.)*

### 1.3 MIT, Microsoft Research and Emerald AI demonstrations

The MIT Center for Energy and Environmental Policy Research working paper
WP-2025-14, *Flexible Data Centers and the Grid: Lower Costs, Higher
Emissions?* by Christopher R. Knittel, Juan Ramon L. Senga and Shen Wang
(July 2025) [Source: https://ceepr.mit.edu/workingpaper/flexible-data-centers-and-the-grid-lower-costs-higher-emissions/]
modelled three regional grids — Texas, the mid-Atlantic and WECC — that
together expect to host more than 80 % of US data-centre demand by 2030.
It found total system-cost savings from data-centre flexibility of roughly
**2 % in the Western Interconnection rising to about 5 % in
ERCOT** [Source: https://mitsloan.mit.edu/ideas-made-to-matter/flexible-data-centers-can-reduce-costs-if-not-emissions]. The emissions
result is more contingent: in Texas, where renewables are about half the
mix, flexibility cut emissions by up to 40 %; in coal-heavier regions
flexibility raised emissions by up to 3 %, because the cheapest available
shifted hours dispatched fossil baseload. Roughly 50 % renewable
penetration is the breakeven for emissions reductions [Source: https://mitsloan.mit.edu/ideas-made-to-matter/flexible-data-centers-can-reduce-costs-if-not-emissions].

The most physical — as opposed to model-based — recent demonstration is
Emerald AI's March 2026 trial with National Grid Partners and Nebius in
London using a 96-GPU NVIDIA Blackwell Ultra cluster. The platform
responded to 22 live dispatch events and reduced power draw by up to **40 %
in under 40 seconds**, including a simulated UK "TV pickup" event, while
keeping latency-sensitive inference workloads running and rescheduling
training/fine-tuning around natural checkpoint intervals [Source: https://www.theregister.com/2026/03/04/demo_shows_datacenters_can_reduce/] [Source: https://www.datacenterdynamics.com/en/news/emerald-ai-releases-results-of-uk-demonstration-project-in-partnership-with-national-grid/].
Emerald has subsequently announced an integration with NVIDIA DSX Flex that
the company claims could "unlock up to 100 GW of grid capacity"
[Source: https://www.emeraldai.co/blog/emerald-ai-nvidia-dsx-flex-ai-factories]
— a vendor figure that should be treated as marketing until validated.

Microsoft Research's Carbon-Aware Computing programme and Google's
Carbon-Intelligent Compute Management work, both originally published
2020–2022, are the academic bedrock of the workload-shifting argument and
remain the most widely cited justifications by hyperscaler sustainability
teams [Source: https://cloud.google.com/blog/topics/sustainability/googles-approach-to-carbon-aware-data-center].

---

## 2. Hyperscaler-published positions

### 2.1 Google

Google has the most operationally specific public claim. In an October 2024
blog post, *How we're making data centers more flexible to benefit power
grids* [Source: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/],
the company announced new demand-response agreements with Indiana Michigan
Power (Fort Wayne data centre) and Tennessee Valley Authority, layered on
top of an earlier proof-of-concept with Omaha Public Power District in
which non-urgent ML workloads were curtailed across three grid events.
Comparable arrangements exist with Centrica/Elia in Belgium and Taiwan
Power. Google explicitly notes the limitations: demand response is "in
the early stages and will only be available at certain locations" because
core services such as Search, Maps and certain Cloud customers cannot
tolerate degradation [Source: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/].
**No MW or MWh figures were disclosed.**

Google's 2025 Environmental Report claims **66 % carbon-free energy on an
hourly basis** across owned and operated data centres (up from 64 %), with
nine of 20 grid regions above 80 % CFE; data-centre energy emissions fell
12 % despite a 27 % increase in electricity demand, attributed to more than
25 clean-energy projects (≈2.5 GW added in 2024) reaching commercial
operation [Source: https://blog.google/outreach-initiatives/sustainability/environmental-report-2025/].
Group-level emissions still rose 11 % year-on-year and are now 51 % above
the 2019 baseline [Source: https://www.esgdive.com/news/googles-emissions-rise-despite-data-center-decarbonization-ppas-environmental-report-2025/752236/].

### 2.2 Microsoft

Microsoft's 2025 Environmental Sustainability Report, published 29 May
2025, reports **about 40 GW of contracted renewable capacity** across
26 countries (≈400 contracts, of which 19 GW operational), and that the
company matched 100 % of 2025 global electricity consumption with
renewables on an annual basis [Source: https://blogs.microsoft.com/on-the-issues/2025/05/29/environmental-sustainability-report/] [Source: https://www.datacenterdynamics.com/en/news/microsoft-matches-100-of-2025-power-use-with-renewables-with-more-than-40gw-of-contracted-capacity/].
Group emissions remained roughly 23 % above the 2020 baseline.

On flexibility and grid services Microsoft's published evidence is thinner
than Google's. The most-cited deployments are:

- The Dublin grid-interactive UPS programme with Enel X and EirGrid, which
  uses lithium-ion batteries already installed for backup to bid into the
  Irish DS3 ancillary services market [Source: https://news.microsoft.com/source/features/sustainability/ireland-wind-farm-datacenter-ups/].
- A 1.5 MW hydrogen fuel-cell + battery hybrid at the Cheyenne, Wyoming
  data centre, demonstrated with Caterpillar in 2022–2024 to run a 48-hour
  backup event [Source: https://news.microsoft.com/source/features/sustainability/hydrogen-datacenters/] [Source: https://www.caterpillar.com/en/news/corporate-press-releases/h/caterpillar-microsoft-collaboration.html].
- The ESB green-hydrogen pilot announced for Dublin in 2024 [Source: https://news.microsoft.com/source/emea/2024/09/microsoft-announces-pioneering-green-hydrogen-pilot-project-with-esb/].

(The user's note refers to a Microsoft "12 MW Bloom Energy fuel-cell +
battery deployment trial". I could not verify a deployment of that exact
size and configuration in publicly available sources as of May 2026; press
coverage confirms a ≈100 MW Bloom-Equinix programme [Source: https://www.bloomenergy.com/news/bloom-energy-expands-data-center-power-agreement-with-equinix-surpassing-100mw/]
and a 1 GW AEP-Bloom procurement framework [Source: https://www.bloomenergy.com/news/bloom-energy-announces-gigawatt-fuel-cell-procurement-agreement-with-aep-to-power-ai-data-centers/], but no
12 MW Microsoft–Bloom-specific announcement.)

The Microsoft "Community-First AI Infrastructure" framework published
13 January 2026 is the company's most explicit commitment to *bear* the
cost of new transmission and generation rather than externalise it onto
existing ratepayers [Source: https://blogs.microsoft.com/on-the-issues/2026/01/13/community-first-ai-infrastructure/].
It is, however, a policy statement, not a contracted instrument.

### 2.3 Amazon Web Services

AWS positions its flexibility contribution primarily through generation
build-out rather than load-shifting. Its public summary highlights nuclear
investments (1.92 GW from Talen's Susquehanna plant under a restructured
front-of-the-meter PPA after FERC twice rejected the original behind-the-
meter interconnection amendment in November 2024 and April 2025) [Source: https://www.powermag.com/talen-amazon-launch-18b-nuclear-ppa-a-grid-connected-ipp-model-for-the-data-center-era/] [Source: https://www.ans.org/news/2025-04-16/article-6937/];
the "Cascade" 12-unit X-energy SMR project with Energy Northwest in
Washington (≈960 MW by the early 2030s) and a Dominion partnership for at
least 300 MW of SMR capacity near North Anna in Virginia [Source: https://www.utilitydive.com/news/amazon-small-modular-reactor-deals-nuclear-dominion-x-energy-energy-northwest/730022/] [Source: https://www.powermag.com/amazon-unveils-cascade-energy-northwests-xe-100-smr-project-targeting-construction-by-2030/].
AWS asserts a 2024 fleet PUE of 1.15 versus a 1.25 cloud average and a 1.63
on-premises average and claims it remained the world's largest corporate
purchaser of renewables in 2025 [Source: https://aws.amazon.com/sustainability/data-centers/].

AWS's own published material on demand response and grid services is
limited to high-level partnership references (Duke Energy, GE Vernova) and
advocacy for Grid Enhancing Technologies; **no quantified MW of dispatchable
flexibility has been disclosed** [Source: https://aws.amazon.com/sustainability/data-centers/].

### 2.4 Meta

Meta's public flexibility footprint is the smallest of the four
hyperscalers. It joined DCFlex as a founding member [Source: https://www.utilitydive.com/news/epri-launches-data-center-flexibility-initiative-with-NVIDIA-google-meta/731490/]
but, as of mid-2026, has no published MW commitment or operational
demand-response programme. Meta's contribution to the lowering-costs
narrative is procurement: Meta contracted 10.24 GW of clean energy in 2025,
narrowly leading Amazon (10.22 GW), with combined 4.7 GW of nuclear
[Source: https://www.esgtoday.com/amazon-meta-google-microsoft-account-for-half-of-global-clean-energy-purchase-deals-in-2025-report/].

### 2.5 Combined hyperscaler procurement

According to BloombergNEF, Meta, Amazon, Google and Microsoft together
accounted for roughly **49 % of global corporate clean PPA volume in 2025**,
even as global volumes contracted 10 % to 55.9 GW
[Source: https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/].
On a cumulative basis, Microsoft is now the largest corporate clean-energy
buyer at 34.7 GW contracted (end-September 2025) [Source: https://www.spglobal.com/market-intelligence/en/news-insights/research/corporate-ppa-leaderboard-microsoft-leap-cuts-into-amazon-lead].

---

## 3. Behind-the-meter batteries as a flexibility resource

The industry argument is that BTM batteries already installed for
ride-through and UPS purposes can be re-purposed for grid services
(frequency response, fast-frequency response, voltage support, capacity)
without requiring incremental utility investment.

Specific deployments routinely cited:

- **Switch Citadel Campus / Tahoe Reno** — co-developed by Switch and
  Capital Dynamics, integrating a 127 MW behind-the-meter solar plant with
  a **240 MWh Tesla Megapack battery** dedicated to the data-centre
  campus [Source: https://www.datacenterfrontier.com/energy/article/11428858/switch-will-use-tesla-megapacks-for-hyperscale-energy-storage]
  [Source: https://www.switch.com/switch-and-capital-dynamics-break-ground-on-massive-solar-and-battery-storage-developments-advancing-rob-roys-gigawatt-nevada/].
  The "Gigawatt 1 Nevada" pipeline aims at >800 MWh of total Megapack
  capacity across Switch's Las Vegas and Reno facilities.
- **xAI Colossus (Memphis, TN)** — 168 Tesla Megapacks deployed on site,
  each ≥3.9 MWh, for combined order value reported at about US$375 m
  [Source: https://www.datacenterdynamics.com/en/news/xai-deploys-168-tesla-megapacks-to-power-its-colossus-supercomputer-in-memphis/]
  [Source: https://teslanorth.com/2025/11/19/xai-taps-375m-in-tesla-megapacks-to-power-colossus-ii/]. xAI's
  stated functions are peak-shaving, power-quality and outage ride-through
  for the supercomputer connected to Memphis Light, Gas and Water and TVA
  via a 150 MW substation. *(Caveat: industry coverage does not confirm
  enrolment in any TVA grid-services product.)*
- **Equinix–Bloom Energy programme** — >100 MW of solid-oxide fuel cells
  across 19 IBX data centres in six US states, with about 75 MW operational
  and 30 MW under construction at the February 2025 expansion announcement
  [Source: https://www.bloomenergy.com/news/bloom-energy-expands-data-center-power-agreement-with-equinix-surpassing-100mw/].
- **AEP–Bloom Energy** — gigawatt-scale procurement framework signed
  October 2024 to supply Bloom fuel cells as behind-the-meter generation to
  AEP's data-centre customers [Source: https://www.bloomenergy.com/news/bloom-energy-announces-gigawatt-fuel-cell-procurement-agreement-with-aep-to-power-ai-data-centers/].
- **Microsoft-Caterpillar Cheyenne hydrogen fuel cell/battery hybrid**
  (1.5 MW + Cat PGS 1260 batteries) demonstrated for 48-hour backup
  [Source: https://www.caterpillar.com/en/news/corporate-press-releases/h/caterpillar-microsoft-collaboration.html].

The general industry positioning, articulated by Schneider Electric,
FlexGen, NextG and others, is that grid-forming BTM BESS can deliver
"virtual spinning reserve" during AI-training power swings and can in
principle be enrolled in capacity, frequency-regulation and voltage-support
markets [Source: https://www.flexgen.com/resources/blog/solving-data-center-power-needs-battery-energy-storage]
[Source: https://nextgpower.com/data-center-battery-storage-why-ai-is-driving-explosive-growth-in-utility-scale-and-btm-systems/].
Outside Microsoft's Dublin DS3 participation, **publicly verifiable enrolment
of US data-centre BTM batteries in ISO ancillary-service markets is
limited** — claims of grid-services capability typically describe technical
potential, not contracted MW.

---

## 4. Demand-response participation in ISO programmes

### 4.1 ERCOT

ERCOT's Large Load Working Group reports about **5,302 MW of large load
classified as "controllable"** as of 2025, equivalent to roughly 2 % of the
total large-load portfolio in ERCOT [Source: https://www.ercot.com/services/rq/large-load-integration].
The Controllable Load Resource (CLR) framework allows qualified loads to
participate in Security-Constrained Economic Dispatch and to provide
ancillary services. ERCOT staff describe data centres as "the most
controllable large loads in history" — a forward-looking characterisation
used in Large Flexible Load Task Force materials, including a March 2025
presentation by Emerald AI [Source: https://www.ercot.com/files/docs/2025/03/27/Emerald-AI-LFLTF-Background-for-Circulation-March-28-2025.pdf].

Texas Senate Bill 6, signed 21 June 2025, codifies a two-track curtailment
framework for new ERCOT large loads: mandatory curtailment protocols for
post-2025 interconnections during firm load shed, and a voluntary
PUCT-procured reliability service for >75 MW loads with ≥24 hours' notice
[Source: https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation].
Industry response has been **mixed but mostly accepting** rather than
contested: the Data Center Coalition and individual operators have argued
for clarity and proportional implementation rather than challenging the
authority itself. Capstone analysts have characterised SB 6 as providing
"regulatory certainty" for IPPs and colocation deals
[Source: https://www.utilitydive.com/news/texas-law-gives-grid-operator-power-to-disconnect-data-centers-during-crisi/751587/];
some operators have publicly indicated openness to voluntary curtailment or
back-up generation switching, while others remain resistant on
service-level grounds [Source: https://www.datacenterfrontier.com/energy/article/55298872/texas-senate-bill-6-a-bellwether-on-how-states-may-approach-data-center-energy-use].

### 4.2 PJM

PJM's 2027/28 Base Residual Auction (held 2025) cleared at the
$329.17/MW-day system-wide cap, a 22 % rise on the prior auction; the
2025/26 delivery year had cleared at $269.92/MW-day system-wide and at
zonal caps of $466.35/MW-day in BGE and $444.26/MW-day in Dominion
[Source: https://insidelines.pjm.com/2025-in-review-pjm-market-rules-support-efficiency-resource-adequacy/].
PJM's December 2025 auction for 2027/28 fell 6,625 MW short of reliability
targets and cleared at a record $333.44/MW-day [Source: https://introl.com/blog/pjm-grid-crisis-2027-data-center-capacity-shortfall].

PJM's own commentary attributes some new demand-response (DR) enrolment to
this price signal: "large data center operators began enrolling backup
generation and curtailable load to participate"; for the 2027/28 delivery
year DR resources' availability window was widened to 24 hours, raising
their capacity value and increasing cleared DR MW [Source: https://insidelines.pjm.com/2025-in-review-pjm-market-rules-support-efficiency-resource-adequacy/].
Aggregate quantification of cleared *data-centre-specific* DR MW is not
published.

### 4.3 CAISO

The California Energy Commission forecasts data-centre load in the CAISO
footprint rising 1.8 GW by 2030 and 4.9 GW by 2040, with about 4.5 GW
already in study in the 2025–26 transmission planning cycle
[Source: https://www.caiso.com/documents/issue-paper-large-load-consideration-jan-20-2026.pdf].
CAISO's annual Flexible Capacity Needs Assessment governs procurement, but
**no California data-centre cohort with material registered DR participation
has been publicly identified**; integration is being addressed through the
Demand & Distributed Energy Market Integration (DDEMI) initiative.

---

## 5. Industry counter-arguments to rate-impact attribution

### 5.1 Lawrence Berkeley / Brattle, "Factors Influencing Electricity Prices"

The most consequential 2025 publication for the industry's affirmative
case is the joint Lawrence Berkeley National Laboratory / Brattle Group
study released January 2025 [Source: https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/].
The study finds that grid-infrastructure spending — adaptation/hardening
(28 % of distribution spend), expansion (28 % of distribution; 42 % of
transmission) and equipment-cost inflation in transformers, switchgear and
conductors — is the dominant driver of recent rate increases, **not new
load per se**. Rates in North Dakota actually fell about 1 ¢/kWh between
2019 and 2024, partly attributed to data-centre and other large-load
additions diluting fixed costs across more kWh
[Source: https://www.pbs.org/newshour/show/how-data-center-power-demand-could-help-lower-electricity-prices].
Brattle's December 2025 GridConnext presentation extended the analysis,
estimating that better grid utilisation and load-following anchor effects
could save consumers >US$100 bn over the next decade
[Source: https://www.brattle.com/wp-content/uploads/2025/12/Electric-Rates-and-Affordability-Observations-on-the-LBNL-Brattle-Study-and-Future-Trends.pdf]
[Source: https://www.latitudemedia.com/news/grid-efficiency-could-save-utility-customers-more-than-110-billion/].

This is now the single most important non-advocacy citation industry uses
to argue that data-centre load growth is not the cause of rising bills.

### 5.2 Edison Electric Institute (advocacy body — utility-side)

In a March 2026 FERC filing, EEI reported that investor-owned utilities
are working to interconnect at least **39 GW of large customer load** —
data-centre, manufacturing and other industrial — with more than 80 large
projects in development; 20 states have approved at least one large-load
tariff and 9 have pending proposals [Source: https://www.utilitydive.com/news/ious-edison-electric-interconnect-data-center-ferc/814688/].
Drew Maloney, EEI president and CEO, framed the position carefully:
*"We are committed to ensuring the timely interconnection of large loads
while also ensuring benefits and protection for all customers and the
grid"* [Source: https://www.utilitydive.com/news/ious-edison-electric-interconnect-data-center-ferc/814688/].
EEI's projected 2025–29 utility capex is roughly US$1.1 trn, nearly
matching the US$1.3 trn spent over the prior decade
[Source: https://www.utilitydive.com/news/electric-utilities-will-invest-more-than-11t-by-2030-to-meet-demand-growt/753783/].

### 5.3 Data Center Coalition (advocacy body)

The Data Center Coalition (DCC), whose membership includes Google,
Microsoft, Meta, Amazon and ≈40 other operators, has pursued three rhetorical
moves in 2025 filings and statements:

1. **Cost-of-service compliance**. DCC director of energy policy Lucas
   Fykes is on the record that "the data center industry is committed to
   paying its full cost of service" [Source: https://www.latitudemedia.com/news/state-lawmakers-stand-between-ratepayers-and-data-center-costs/].
   The coalition routinely cites the December 2024 JLARC Virginia report
   [Source: https://jlarc.virginia.gov/pdfs/reports/Rpt598-2.pdf] as
   evidence that data centres in Virginia *are* paying their cost of
   service — though the same report concedes that incremental demand will
   raise system costs for non-data-centre customers.
2. **Bring-your-own-power**. In response to PJM capacity-market reforms,
   DCC, with the governors of MD, NJ, PA and VA and utilities Exelon and
   PPL, called for expedited grid entry for data centres bringing dedicated
   generation [Source: https://www.utilitydive.com/news/solving-pjms-data-center-problem/805600/].
3. **Voluntary, not mandatory, curtailment**. DCC opposes prescriptive
   curtailment regimes and prefers programmes that "encourage, but not
   force, data centers to seek out their own capacity or curtail power use
   during grid emergencies" [Source: https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/].

In Pennsylvania, DCC commended the PUC's 6 November 2025 large-load
framework as preferable to "waiting for disputes to play out utility by
utility", with vice-president for state policy Dan Diorio saying the key
test will be whether utility filings "stay grounded in cost causation,
remain end-use neutral, and apply these tools in a way that is proportional
to actual risk" [Source: https://www.puc.pa.gov/press-release/2025/puc-advances-plan-to-balance-data-center-growth-and-consumer-protection-11062025]
[Source: https://www.latitudemedia.com/news/state-lawmakers-stand-between-ratepayers-and-data-center-costs/].
By contrast, DCC stated public dissatisfaction with the Public Utilities
Commission of Ohio's July 2025 ruling requiring data centres to pay a
larger up-front share of system costs.

### 5.4 ICF, Brattle CONE work and consultant economics

- ICF has published siting analyses arguing that data centres can be added
  *quickly* in regions with existing transmission headroom and surplus
  generation — implicitly supporting the headroom-utilisation narrative
  [Source: https://www.rtoinsider.com/121784-icf-paper-data-center-siting/].
- Brattle's Sixth Quadrennial Review CONE work for PJM (April–August 2025)
  provides the technical basis for capacity-price formation and is itself
  cited by both industry advocates *and* market monitors in opposite
  directions [Source: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mic/2025/20250411-special/item-1-02-revised-cone-report-final.pdf].

It is worth flagging the contrary evidence the industry rarely confronts.
PJM's Independent Market Monitor attributes 63 % of the 2025/26 capacity
price increase — about US$9.3 bn that customers will pay through higher
rates — directly to data-centre demand, and 40 % of total auction cost
($6.5 bn of $16.4 bn) to data-centre load [Source: https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/]
[Source: https://www.utilitydive.com/news/data-centers-pjm-capacity-auction-market-monitor/801780/].
Industry response to this finding has been to challenge methodology and to
counter-cite the LBNL/Brattle work; it has not been to dispute that
capacity prices have risen.

---

## 6. The "we'll bring new generation" argument

The headline claim is that hyperscaler procurement is *additional* — i.e.
PPAs for nuclear restarts, SMRs, new wind, solar and storage — rather than
diverting existing capacity from the grid. The strongest exhibits are:

- **Microsoft–Constellation Three Mile Island (Crane Clean Energy
  Center)**: 20-year, 835 MW PPA announced 20 September 2024 to restart
  Unit 1, with target return-to-service brought forward from 2028 to 2027
  and a US$1 bn DOE loan to Constellation announced November 2025
  [Source: https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html]
  [Source: https://www.utilitydive.com/news/constellation-three-mile-island-nuclear-power-plant-microsoft-data-center-ppa/727652/]
  [Source: https://www.utilitydive.com/news/doe-loan-constellation-crane-nuclear-restart/805923/].
- **Amazon–Talen Susquehanna**: 17-year, $18 bn PPA for up to 1,920 MW
  delivered front-of-the-meter after FERC's 1 November 2024 (2-1) and
  April 2025 rejections of the original behind-the-meter interconnection
  amendment [Source: https://www.powermag.com/talen-amazon-launch-18b-nuclear-ppa-a-grid-connected-ipp-model-for-the-data-center-era/].
- **Amazon–X-energy / Energy Northwest "Cascade"**: 12-unit Xe-100 SMR
  project for ≈960 MW by the early 2030s, plus US$500 m Series C-1
  investment in X-energy [Source: https://www.powermag.com/amazon-backs-massive-nuclear-smr-deployment-5-gw-with-x-energy-agreements-with-energy-northwest-dominion/].
- **Amazon–Dominion Energy** SMR exploration near North Anna for at least
  300 MW [Source: https://investors.dominionenergy.com/news/press-release-details/2024/Dominion-Energy-and-Amazon-to-explore-advancement-of-Small-Modular-Reactor-SMR-nuclear-development-in-Virginia/default.aspx].
- **Hyperscaler renewable build**: ≈49 % of 2025 global corporate clean PPA
  volume of 55.9 GW (BNEF), with Meta and Amazon each at ≈10.2 GW
  contracted in 2025 alone and Microsoft cumulative at 34.7 GW [Source: https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/].

The industry argument is that without these PPAs, neither the TMI restart
nor most of the SMR pipeline would proceed, and that incremental procured
renewable capacity *adds* to the system rather than substituting for it.
Critics' counterpoint — that PPAs for existing nuclear redirect
already-committed clean MWh away from grid customers and force replacement
with marginal gas — is what underlies the FERC Talen/AWS rejections. The
industry has not directly rebutted that critique; instead it has
restructured deals (as in the AWS front-of-the-meter pivot) or pursued
*new* generation build (the SMR programme).

---

## 7. Where industry concedes

The clearest concession is Microsoft's reported reconsideration of its
"100/100/0" target — matching 100 % of electricity, 100 % of the time,
with carbon-free energy on the same regional grid by 2030. Reporting in
early May 2026 (Bloomberg, TechCrunch, Geekwire, DCD) cites internal
deliberations on whether to delay or scale back the hourly-matching
component as AI training capex outpaces renewable build [Source: https://www.bloomberg.com/news/articles/2026-05-06/microsoft-clean-power-target-on-chopping-block-over-data-center-boom]
[Source: https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/]
[Source: https://www.geekwire.com/2026/report-as-ai-electricity-demands-soar-microsoft-weighs-retreat-from-ambitious-carbon-free-energy-pledge/]
[Source: https://www.datacenterdynamics.com/en/news/microsoft-considering-scrapping-247-renewable-energy-matching-target-report/].
Azure infrastructure head Alistair Speirs has publicly conceded that
"renewable energy on the grid did not yet exist in the volumes Microsoft
expects to need as AI demand grows" and described the original 2020 pledge
as a "moonshot" whose enabling capabilities did not yet exist [Source: https://www.kuow.org/stories/are-microsoft-s-ai-and-environmental-goals-compatible].
*This is a reported, not yet finalised, retreat as of May 2026.*

The industry also implicitly concedes the **training-versus-inference
flexibility split**:

- Training workloads can tolerate ~100 ms of geographic latency, support
  remote siting and natural checkpoint pauses, and are the workload class
  Emerald AI/EPRI/Google demonstrations have actually flexed [Source: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-next-big-shifts-in-ai-workloads-and-hyperscaler-strategies].
- Inference workloads tolerate as little as ~5 ms of latency, must run
  near end-users and are *not* materially flexible without service-level
  degradation [Source: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-next-big-shifts-in-ai-workloads-and-hyperscaler-strategies].
- McKinsey expects inference to grow at a 35 % CAGR to >90 GW by 2030
  versus training at 22 % CAGR to >60 GW, meaning the inflexible cohort
  will be the *larger* one within the forecast horizon.

Training also runs at very high duty cycle (≥80 % utilisation while a model
is in flight), which limits the practical share of energy that can be
shifted without lengthening training timelines that have become a
competitive variable for the model-builders themselves.

---

## 8. Caveats

- **Headline 76 GW number**. Cite Norris always with the curtailment rate
  (0.25 %), the absence of intra-zone transmission modelling and the use of
  historical peak without an additional reserve margin. The 98 GW (0.5 %)
  and 126 GW (1.0 %) sensitivities are equally valid and arguably more
  realistic.
- **Corporate "matched" capacity vs. delivered MW**. Hyperscaler PPA
  totals (Microsoft 40 GW contracted, Meta 10.24 GW added in 2025, etc.)
  are *contractual* not *operating*; Microsoft's report notes 19 of 40 GW
  is online. Annual matching is not the same as 24/7/365 same-grid
  matching.
- **BTM battery enrolment**. Most US data-centre BTM batteries discussed
  in industry materials are described as having *capability* for grid
  services, not as having *registered MW* in an ISO ancillary product.
  Microsoft Dublin–Enel X DS3 and a small number of utility-side pilots
  (Google/I&M, Google/TVA) are the clear instrument-backed exceptions.
- **Microsoft 24/7 CFE retreat is reported, not finalised**. As of
  10 May 2026 there is no published Microsoft sustainability report
  document withdrawing or modifying the 2030 hourly-matching target.
  Reporting is sourced to Bloomberg interviews and second-hand summaries.
- **The 12 MW Microsoft-Bloom fuel-cell + battery deployment** referenced
  in the prompt could not be independently verified at that exact
  configuration in publicly available sources reviewed. The closest
  verifiable Microsoft fuel-cell deployment is the 1.5 MW Caterpillar
  hybrid at Cheyenne, WY.
- **Emerald AI / NVIDIA "100 GW" claim** is vendor marketing and should
  not be treated as an independent estimate; it implicitly extrapolates
  from the 96-GPU London demonstration.

---

## Bibliography (full URLs)

### Tier 1 — Academic, national-lab, ISO/RTO, FERC, hyperscaler primary

- Norris, T. H., Profeta, T., Patino-Echeverri, D. & Cowie-Haskell, A.
  (2025). *Rethinking Load Growth: Assessing the Potential for Integration
  of Large Flexible Loads in US Power Systems*. Duke Nicholas Institute,
  February 2025. https://nicholasinstitute.duke.edu/events/rethinking-load-growth-assessing-potential-integration-large-flexible-loads-us-power-systems
- Norris, T. H. (2025). ISO-NE Consumer Liaison Group presentation,
  27 March 2025. https://www.iso-ne.com/static-assets/documents/100021/march_clg_meeting_speaker_norris_03_27_25.pdf
- Knittel, C. R., Senga, J. R. L. & Wang, S. (2025). *Flexible Data
  Centers and the Grid: Lower Costs, Higher Emissions?* MIT CEEPR
  WP-2025-14, July 2025. https://ceepr.mit.edu/workingpaper/flexible-data-centers-and-the-grid-lower-costs-higher-emissions/
- MIT Sloan summary of CEEPR WP-2025-14. https://mitsloan.mit.edu/ideas-made-to-matter/flexible-data-centers-can-reduce-costs-if-not-emissions
- Lawrence Berkeley National Laboratory (2025). Press release on data-
  centre electricity demand, 15 January 2025. https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- LBNL (2024). *2024 United States Data Center Energy Usage Report*.
  https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- Google (2024). *How we're making data centers more flexible to benefit
  power grids*. https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/
- Google (2025). *2025 Environmental Report*. https://sustainability.google/reports/google-2025-environmental-report/ and https://blog.google/outreach-initiatives/sustainability/environmental-report-2025/
- Google Cloud Sustainability blog: *Google's approach to carbon-aware data
  center*. https://cloud.google.com/blog/topics/sustainability/googles-approach-to-carbon-aware-data-center
- Microsoft (2025). *2025 Environmental Sustainability Report*.
  https://blogs.microsoft.com/on-the-issues/2025/05/29/environmental-sustainability-report/
  PDF: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report.pdf
- Microsoft (2026). *Building Community-First AI Infrastructure*,
  13 January 2026. https://blogs.microsoft.com/on-the-issues/2026/01/13/community-first-ai-infrastructure/
- Microsoft Source: *Microsoft tests hydrogen fuel cells for backup power
  at datacenters*. https://news.microsoft.com/source/features/sustainability/hydrogen-datacenters/
- Microsoft Source: *Microsoft datacenter batteries to support growth of
  renewables on the power grid* (Ireland Enel X DS3). https://news.microsoft.com/source/features/sustainability/ireland-wind-farm-datacenter-ups/
- Microsoft Source EMEA (2024). *Pioneering green hydrogen pilot project
  with ESB*. https://news.microsoft.com/source/emea/2024/09/microsoft-announces-pioneering-green-hydrogen-pilot-project-with-esb/
- Caterpillar press release: *Caterpillar Demonstrates Viability of Using
  Hydrogen Fuel Cell Technology for Backup Power at Microsoft Data Center*.
  https://www.caterpillar.com/en/news/corporate-press-releases/h/caterpillar-microsoft-collaboration.html
- AWS Sustainability — Data Centers. https://aws.amazon.com/sustainability/data-centers/
- Constellation Energy (2024). *Constellation to Launch Crane Clean Energy
  Center, Restoring Jobs and Carbon-Free Power to the Grid*.
  https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html
- Talen Energy statement on FERC rejection (Nov 2024).
  https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-statement-ferc-order-rejecting-susquehanna-isa
- Dominion Energy / Amazon SMR exploration release.
  https://investors.dominionenergy.com/news/press-release-details/2024/Dominion-Energy-and-Amazon-to-explore-advancement-of-Small-Modular-Reactor-SMR-nuclear-development-in-Virginia/default.aspx
- ERCOT — Large Load Integration. https://www.ercot.com/services/rq/large-load-integration
- ERCOT — Large Load Interconnection Process Q&A (Dec 2025).
  https://www.ercot.com/files/docs/2025/12/24/Large-Load-Interconnection-Process-Q-A.pdf
- Emerald AI / ERCOT Large Flexible Load Task Force background
  (March 2025). https://www.ercot.com/files/docs/2025/03/27/Emerald-AI-LFLTF-Background-for-Circulation-March-28-2025.pdf
- PJM (Dec 2025). 2027/28 BRA Auction press release.
  https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf
- PJM Inside Lines (2026). *2025 in Review: PJM Market Rules Support
  Efficiency, Resource Adequacy*. https://insidelines.pjm.com/2025-in-review-pjm-market-rules-support-efficiency-resource-adequacy/
- CAISO (2026). *Large Load Considerations Issue Paper*, 30 January 2026.
  https://www.caiso.com/documents/issue-paper-large-load-consideration-jan-20-2026.pdf
- CAISO Demand Response page. https://www.caiso.com/generation-transmission/load/demand-response
- JLARC (Virginia) (2024). *Data Centers in Virginia*. https://jlarc.virginia.gov/pdfs/reports/Rpt598-2.pdf

### Tier 2 — Brattle, ICF, EPRI, McKinsey

- Brattle (April 2025). *Cost of New Entry Study for PJM* (Sixth Quadrennial
  Review). https://www.pjm.com/-/media/DotCom/committees-groups/committees/mic/2025/20250411-special/item-1-02-revised-cone-report-final.pdf
- Brattle (December 2025). *Electric Rates and Affordability — Observations
  on the LBNL/Brattle Study and Future Trends* (GridConnext presentation).
  https://www.brattle.com/wp-content/uploads/2025/12/Electric-Rates-and-Affordability-Observations-on-the-LBNL-Brattle-Study-and-Future-Trends.pdf
- Brattle (May 2025). *Clean Capital Efficiency*. https://www.brattle.com/wp-content/uploads/2025/05/Clean-Capital-Efficiency_Brattle_May-2025.pdf
- ICF / RTO Insider (2025). Where data centres can be sited quickly.
  https://www.rtoinsider.com/121784-icf-paper-data-center-siting/
- EPRI DCFlex programme site. https://dcflex.epri.com/
- EPRI press release on DCFlex.
  https://www.epri.com/about/media-resources/press-release/yimzjv2xnv9cqiztau1zxbedletwyqk1
- EPRI DCFlex product page (technical brief).
  https://www.epri.com/research/products/000000003002031004
- McKinsey (2026). *The next big shifts in AI workloads and hyperscaler
  strategies*. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-next-big-shifts-in-ai-workloads-and-hyperscaler-strategies
- BloombergNEF (Jan 2026). *Corporate Clean Energy Buying Fell in 2025*.
  https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/
- S&P Global Sustainable1: *Hyperscaler procurement to shape US power
  investment*. https://www.spglobal.com/sustainable1/en/insights/special-editorial/hyperscaler-procurement-to-shape-us-power-investment

### Tier 3 — Trade press, advocacy bodies (FLAGGED)

*Edison Electric Institute and Data Center Coalition are advocacy bodies.*

- EEI: Drew Maloney quote and 39 GW interconnection figure. https://www.utilitydive.com/news/ious-edison-electric-interconnect-data-center-ferc/814688/
- EEI 2030 capex projection. https://www.utilitydive.com/news/electric-utilities-will-invest-more-than-11t-by-2030-to-meet-demand-growt/753783/
- DCC reaction to PA PUC framework. https://www.puc.pa.gov/press-release/2025/puc-advances-plan-to-balance-data-center-growth-and-consumer-protection-11062025
- DCC framing of voluntary curtailment in PJM. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/
- DCC alternative to PJM data-centre constraints. https://www.utilitydive.com/news/solving-pjms-data-center-problem/805600/
- DCC cost-of-service quote (Latitude). https://www.latitudemedia.com/news/state-lawmakers-stand-between-ratepayers-and-data-center-costs/
- Utility Dive (2025). *Existing US grid can handle "significant" new
  flexible load: report*. https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/
- Power Magazine. *Duke Researchers: Grid Flexibility Key to Accommodate
  Load Growth*. https://www.powermag.com/duke-researchers-grid-flexibility-key-to-accommodate-load-growth/
- Latitude Media. *EPRI takes its data center flexibility project global*.
  https://www.latitudemedia.com/news/epri-takes-its-data-center-flexibility-project-global/
- Utility Dive (2025). EPRI launches DCFlex with NVIDIA, Google, Meta.
  https://www.utilitydive.com/news/epri-launches-data-center-flexibility-initiative-with-NVIDIA-google-meta/731490/
- Data Center Dynamics. xAI 168 Tesla Megapacks at Colossus.
  https://www.datacenterdynamics.com/en/news/xai-deploys-168-tesla-megapacks-to-power-its-colossus-supercomputer-in-memphis/
- Tesla North. Colossus II $375m Megapack order.
  https://teslanorth.com/2025/11/19/xai-taps-375m-in-tesla-megapacks-to-power-colossus-ii/
- Switch press release. Switch & Capital Dynamics break ground on Gigawatt
  Nevada solar + storage. https://www.switch.com/switch-and-capital-dynamics-break-ground-on-massive-solar-and-battery-storage-developments-advancing-rob-roys-gigawatt-nevada/
- Data Center Frontier. Switch — Tesla Megapacks for hyperscale storage.
  https://www.datacenterfrontier.com/energy/article/11428858/switch-will-use-tesla-megapacks-for-hyperscale-energy-storage
- Bloom Energy. Equinix expansion >100 MW (Feb 2025).
  https://www.bloomenergy.com/news/bloom-energy-expands-data-center-power-agreement-with-equinix-surpassing-100mw/
- Bloom Energy. AEP gigawatt fuel-cell agreement (Oct 2024).
  https://www.bloomenergy.com/news/bloom-energy-announces-gigawatt-fuel-cell-procurement-agreement-with-aep-to-power-ai-data-centers/
- Baker Botts. *Texas SB 6 — Understanding the Impacts to Large Loads and
  Co-located Generation*. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation
- Data Center Frontier. *Texas SB 6: A Bellwether on How States May
  Approach Data Center Energy Use*. https://www.datacenterfrontier.com/energy/article/55298872/texas-senate-bill-6-a-bellwether-on-how-states-may-approach-data-center-energy-use
- Utility Dive. *Texas law gives grid operator power to disconnect data
  centers during crisis*. https://www.utilitydive.com/news/texas-law-gives-grid-operator-power-to-disconnect-data-centers-during-crisi/751587/
- Utility Dive. Talen-AWS Susquehanna 1.92 GW PPA.
  https://www.utilitydive.com/news/talen-amazon-aws-susquehanna-nuclear-data-centert/750440/
- Power Magazine. *Talen, Amazon Launch $18B Nuclear PPA*.
  https://www.powermag.com/talen-amazon-launch-18b-nuclear-ppa-a-grid-connected-ipp-model-for-the-data-center-era/
- Data Center Dynamics. Three Mile Island 20-year 835 MW Microsoft PPA.
  https://www.datacenterdynamics.com/en/news/three-mile-island-nuclear-power-plant-to-return-as-microsoft-signs-20-year-835mw-ai-data-center-ppa/
- Power Magazine. Amazon X-energy 5 GW SMR plan with Energy Northwest and
  Dominion. https://www.powermag.com/amazon-backs-massive-nuclear-smr-deployment-5-gw-with-x-energy-agreements-with-energy-northwest-dominion/
- Utility Dive. Amazon SMR deals with Dominion, X-energy, Energy
  Northwest. https://www.utilitydive.com/news/amazon-small-modular-reactor-deals-nuclear-dominion-x-energy-energy-northwest/730022/
- Utility Dive. *Data centers were 40% of PJM capacity costs in last
  auction: market monitor*. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/
- Utility Dive. *Data centers "primary reason" for high PJM capacity
  prices: market monitor*. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction-market-monitor/801780/
- Utility Dive. EEI 39 GW interconnection filing.
  https://www.utilitydive.com/news/ious-edison-electric-interconnect-data-center-ferc/814688/
- The Register. *UK datacenter cuts AI power draw 40 % on command*
  (Emerald AI / Nebius / National Grid). https://www.theregister.com/2026/03/04/demo_shows_datacenters_can_reduce/
- Data Center Dynamics. Emerald AI UK demo results.
  https://www.datacenterdynamics.com/en/news/emerald-ai-releases-results-of-uk-demonstration-project-in-partnership-with-national-grid/
- Emerald AI / NVIDIA DSX Flex announcement. https://www.emeraldai.co/blog/emerald-ai-nvidia-dsx-flex-ai-factories
- PBS NewsHour interview on LBNL/Brattle findings.
  https://www.pbs.org/newshour/show/how-data-center-power-demand-could-help-lower-electricity-prices
- Latitude Media (2026). Grid efficiency could save customers >US$110 bn.
  https://www.latitudemedia.com/news/grid-efficiency-could-save-utility-customers-more-than-110-billion/
- Bloomberg (May 2026). Microsoft 24/7 CFE target on chopping block.
  https://www.bloomberg.com/news/articles/2026-05-06/microsoft-clean-power-target-on-chopping-block-over-data-center-boom
- TechCrunch (May 2026). Microsoft AI data centre push collides with
  clean-power goals. https://techcrunch.com/2026/05/06/microsofts-ai-data-center-push-is-colliding-with-its-clean-power-goals/
- GeekWire (May 2026). Microsoft weighs retreat from carbon-free pledge.
  https://www.geekwire.com/2026/report-as-ai-electricity-demands-soar-microsoft-weighs-retreat-from-ambitious-carbon-free-energy-pledge/
- Data Center Dynamics. Microsoft considering scrapping 24/7 renewable
  matching. https://www.datacenterdynamics.com/en/news/microsoft-considering-scrapping-247-renewable-energy-matching-target-report/
- KUOW interview with Alistair Speirs.
  https://www.kuow.org/stories/are-microsoft-s-ai-and-environmental-goals-compatible
- ESG Dive. Google emissions still rising in 2025 report.
  https://www.esgdive.com/news/googles-emissions-rise-despite-data-center-decarbonization-ppas-environmental-report-2025/752236/
- ESG Today. Big-tech 49 % of clean PPA volume in 2025.
  https://www.esgtoday.com/amazon-meta-google-microsoft-account-for-half-of-global-clean-energy-purchase-deals-in-2025-report/
- S&P Global. Corporate PPA leaderboard — Microsoft cumulative 34.7 GW.
  https://www.spglobal.com/market-intelligence/en/news-insights/research/corporate-ppa-leaderboard-microsoft-leap-cuts-into-amazon-lead
- ANS. FERC denies Talen-Amazon agreement again (April 2025).
  https://www.ans.org/news/2025-04-16/article-6937/
- Utility Dive. DOE loan to Constellation for TMI restart.
  https://www.utilitydive.com/news/doe-loan-constellation-crane-nuclear-restart/805923/
- Utility Dive. Constellation 2028 → 2027 restart with Microsoft PPA.
  https://www.utilitydive.com/news/constellation-three-mile-island-nuclear-power-plant-microsoft-data-center-ppa/727652/
- Power Magazine. Amazon "Cascade" Energy Northwest SMR project.
  https://www.powermag.com/amazon-unveils-cascade-energy-northwests-xe-100-smr-project-targeting-construction-by-2030/
- Introl. PJM 6 GW capacity shortfall analysis.
  https://introl.com/blog/pjm-grid-crisis-2027-data-center-capacity-shortfall
- FlexGen. *Solving for Data Center Power Needs with Battery Energy
  Storage*. https://www.flexgen.com/resources/blog/solving-data-center-power-needs-battery-energy-storage
- NextG Power. *Data Center Battery Storage: Why AI Is Driving Explosive
  Growth*. https://nextgpower.com/data-center-battery-storage-why-ai-is-driving-explosive-growth-in-utility-scale-and-btm-systems/
- PA PUC press release on large-load framework (Nov 2025).
  https://www.puc.pa.gov/press-release/2025/puc-advances-plan-to-balance-data-center-growth-and-consumer-protection-11062025
- Utility Dive. *Solving PJM's data center problem* (DCC + governors plan).
  https://www.utilitydive.com/news/solving-pjms-data-center-problem/805600/
