---
title: "Community attitudes to US data centres: local fights, generalised politics and the 2024-2026 backlash"
author: "David Leitch"
date: 2026-05-10
format: html
draft: false
category: "datacentres"
lightbox: true
---

# Community attitudes to US data centres: local fights, generalised politics and the 2024-2026 backlash

## Headline answer

Until late 2024 opposition to US data centres was overwhelmingly local — county-level zoning fights about noise, water, traffic, viewshed and lost farmland. By mid-2026 it is also a generalised national political story, driven by three converging shocks: PJM capacity-auction prices clearing 833% above the prior auction in July 2024 and re-clearing at the new administrative cap a year later; a sequence of FERC orders culminating in the December 2025 PJM co-location order; and a wave of state legislation in 2025-26 (more than 300 bills tracked by MultiState) seeking to make hyperscalers pay their own grid costs. The clearest single piece of evidence that opposition has broadened is the Washington Post-Schar School Virginia poll: voter "comfort with a new data centre in your community" fell from 69% in 2023 to 35% in March 2026.

Two structural features of the new politics are notable:

- **The coalition is cross-cutting.** Republican legislators in Texas, Georgia and Ohio have advanced cost-allocation rules at least as aggressive as those proposed by Democrats in Virginia, New Jersey and Maryland. Data Center Watch finds elected-official opposition is split 55% Republican / 45% Democrat. Trade press has begun reporting GOP electoral exposure in Pennsylvania over the issue.
- **Federal and state are pulling in opposite directions.** The Trump administration is the most pro-data-centre actor in the system — Stargate was unveiled at the White House on the second day of the second Trump term, followed by Executive Order 14148 accelerating federal permitting and four nuclear executive orders in May 2025. State public service commissions across the partisan spectrum are pushing back through new rate classes, minimum-bill provisions and stranded-cost protections.

The local issues have not gone away — if anything they have intensified, with the xAI Colossus Memphis air-quality case becoming a national environmental-justice flashpoint, and the Prince William Digital Gateway court loss demonstrating that procedural land-use challenges can defeat \$17 GW of approved development. But the generalised cost-shifting and AI-environmental-impact frames have now overtaken purely local quality-of-life concerns as the political driver.

This note draws on two parallel research drafts kept under `background/_research_drafts/community_local.md` and `background/_research_drafts/community_political.md` for traceability.

---

## 1. The local opposition layer

Local opposition has accelerated through 2024-2026. Data Center Watch (industry-funded; figures should be treated as directional rather than precise) has tallied roughly \$156 billion in projects "blocked or delayed" by local opposition by the end of 2025, up from a \$64 billion running total in early 2025, with at least 142 organised activist groups across 24 states [@datacenterwatch-2025; @hill-bipartisan-2025].

### The recurring issues

**Noise.** The constant low-frequency hum from chillers and cooling fans is the most-cited grievance in densely-developed clusters. Loudoun County's industrial noise cap is 55 dB at residential property lines; one CloudHQ measurement reached 90 dB at the boundary, with at least a dozen 2024 complaints against Vantage [@wusa9-loudoun-noise]. Setback responses now include 400 ft (Calvert MD), 1,000 ft (Linn IA, New Castle DE) and 1,500 ft from sensitive receptors (LaGrange/Troup GA).

**Water.** The single most-cited concern in arid-state and drought-stressed locations. Of 25 projects cancelled in 2025, water use was raised in over 40% of cases [@commobs-2026]. In Tucson, Project Blue would have used about 2,000 acre-feet of city water per year, becoming Tucson's largest single water customer; the City Council rejected it 7-0 in August 2025, Pima County subsequently approved a closed-loop redesign on county land, and Amazon withdrew as anchor in December 2025 [@azlum-projectblue]. Chandler AZ rejected a similar proposal 7-0 in December 2025. Beaver Dam Wisconsin residents have reported wells running dry near the Meta construction site [@pbswi-secrecy].

**Air emissions.** xAI's Colossus campus in Memphis is the headline case. University of Tennessee aerial-imagery analysis documented at least 35 gas turbines on site (xAI's previously-disclosed count was lower); Earthjustice and SELC have argued the site became the largest single industrial NOx source in the 11-county Memphis area, with documented capacity to emit more than 1,700 tonnes of NOx, 180 tonnes of particulate matter, 500 tonnes of carbon monoxide and 19 tonnes of formaldehyde per year. The Shelby County Health Department issued an air permit for 15 turbines in July 2025; xAI subsequently moved 27 turbines across the state line to Southaven Mississippi to avoid Tennessee permitting; the NAACP, SELC and Earthjustice filed a federal Clean Air Act lawsuit in April 2026. American Lung Association graded both Shelby and DeSoto Counties "F" for ozone [@earthjustice-xai; @capitalbnews-musk; @cnbc-musk-memphis-2026].

In Loudoun County alone, approximately 4,700 diesel backup generators are now permitted with about 12 GW of nameplate capacity. Virginia DEQ began consulting in late 2025 on relaxing the 500-hour annual cap on emergency-engine running, narrowed in early 2026 to a Loudoun-only variance opposed by the Piedmont Environmental Council [@vamerc-diesel].

**Visual / viewshed / heritage.** The Manassas Battlefield case is the clearest viewshed flashpoint. The Pageland Lane parcels QTS and Compass sought to develop sit immediately west of the battlefield boundary on land long zoned agricultural specifically to provide a buffer; the National Park Service superintendent publicly described the proposal as risking "wholesale destruction" of associated historic context. The American Battlefield Trust and Piedmont Environmental Council were lead organisers [@pwt-superintendent; @abt-digital-gateway].

**Farmland and rural character.** Saline Township Michigan is the case-study reference point. The township board voted 4-1 in March 2025 to deny rezoning for the 1.4 GW Stargate (Related Digital / Oracle / OpenAI) project. Two days later the developer sued under Michigan's exclusionary-zoning doctrine, arguing that because Saline Township had no industrially-zoned land at all, a "necessary" use could not be excluded altogether. The township settled within weeks; construction began; the Michigan PSC approved the DTE supply contract in December 2025 with conditions; Fortune's May 2026 reporting confirms the facility is operational on a path to 1.4 GW. Residents secured roughly \$14 million in community benefits including fire-department funding and farmland preservation [@fortune-saline; @mipublic-saline].

**Fiscal trade-offs.** The job-density argument is now well-documented. JLARC estimates Virginia's data-centre sector supports 74,000 jobs across the economy, mostly in construction; the operational footprint per facility is much smaller, with industry analyses citing 1-2 permanent staff per MW for the most automated hyperscale campuses [@jlarc-2024; @latitude-jobs]. Meanwhile the sales-tax exemption costs are now substantial:

| State | Annual tax-break cost | Year | Note |
|:------|----------------------:|-----:|:-----|
| Virginia | \$1.6-3.2 bn | FY24-25 | 118% YoY increase; original 2008 estimate \$1.54m/yr — now exceeds it by 100,000% |
| Texas | ~\$1.8 bn projected | FY30 | Comptroller estimate, up from prior \$1.3 bn |
| Georgia | ~\$2.5 bn projected | FY26 | 664% above prior official \$327m estimate |

A University of Georgia audit found roughly **70% of Georgia's data-centre construction would have occurred without the exemption**, implying the marginal incentive value is well below the headline foregone revenue [@csgsouth-data]. Virginia's University of Virginia analyst Terance Rephann (cited in VPM coverage) estimates the exemption is the marginal driver in roughly 50% of cases and falling [@vpm-tax-2026].

### The leading local case studies

**Table 1: Major US data centre community-opposition cases, 2024-early 2026**

| Project | Location | Lead developer / tenant | Primary issues | Outcome to May 2026 |
|:--------|:---------|:------------------------|:---------------|:--------------------|
| PW Digital Gateway | Prince William Co., VA | QTS (Blackstone), Compass | Heritage (Manassas buffer), rural character, scale | Rezoning voided by Circuit Court Aug 2025; upheld by VA Court of Appeals 31 Mar 2026; Compass dropped appeal; PWC withdrew from defence 15 Apr 2026; QTS appeal to VA Supreme Court 30 Apr 2026 — project effectively dead |
| Stargate Saline Township | Saline Township, MI | Related Digital / Oracle / OpenAI | Farmland, scale (1.4 GW) | Township denied 4-1 March 2025; developer sued under exclusionary-zoning doctrine; township settled; construction proceeded; PSC approved DTE contract Dec 2025 |
| xAI Colossus 1+2 | Memphis TN / Southaven MS | xAI | Air pollution from 35+ unpermitted gas turbines; environmental justice (Boxtown majority-Black) | NAACP/SELC/Earthjustice federal Clean Air Act suit April 2026; preliminary-injunction motion pending |
| Project Blue | Tucson / Pima Co., AZ | Beale Infrastructure (originally AWS) | Water (~2,000 ac-ft/yr) | Tucson Council rejected 7-0 Aug 2025; Pima Co. approved closed-loop redesign; Amazon withdrew Dec 2025 |
| Chandler proposal | Chandler, AZ | Confidential (\$2.5 bn) | Water (>100m gal/yr), noise | City Council rejected 7-0 Dec 2025 |
| Tract West Valley | Buckeye / Goodyear, AZ | Tract | Heights, noise, water | Original \$14 bn proposal withdrawn May 2024; smaller revision proceeded |
| Meta El Paso | El Paso, TX | Meta / El Paso Electric | Air emissions from 813 modular gensets (~366 MW); tax breaks | El Paso City Council voted unanimously Jan 2026 to intervene at Texas PUC |
| Microsoft Palmetto | South Fulton / Coweta Co., GA | Microsoft | Rural-fringe character, water | Approved 2024; mayor of Palmetto publicly opposed |
| DeKalb County moratorium | DeKalb Co., GA | n/a | Health, costs, density | Moratorium extended to 23 June 2026 |
| Microsoft Caledonia | Caledonia, WI | Microsoft | Energy demand, scale | Microsoft withdrew rezoning Sep 2025 after opposition |
| Vantage "Lighthouse" Stargate | Port Washington, WI | Vantage / Oracle / OpenAI | Construction nuisance, energy costs | Ground broken Dec 2025; mayoral recall petition Feb 2026 fell short |
| Meta Beaver Dam | Beaver Dam, WI | Meta (via Alliant) | Wells running dry; rate impact | Alliant ICR rate filing modified by PSC May 2026 to require data centre to bear full cost |
| Project Delta | Stokes Co., NC | Engineered Land Solutions | Dan River corridor, scale (1,800 ac) | County rezoning approved Jan 2026 voided March 2026 over defective public notice; community lawsuit pending |
| Microsoft LaPorte | LaPorte Co., IN | Microsoft | Farmland (~1,000 ac annexation) | County advanced restrictions late 2025; LaPorte city annexed ~1,000 acres April 2026 |
| University of Delaware | Newark, DE | The Data Centers LLC (2014 vintage) | Cogen power, residential proximity | Killed June 2024; New Castle Co. ordinance Sept 2025 imposed 1,000 ft setback |

*Source: ITK compilation from court filings, county/township meeting minutes, state PSC dockets and trade press. Outcomes current to early May 2026; several cases (PWDG VA Supreme Court appeal, xAI preliminary injunction, Stokes County re-do) are still moving and will need refresh before any further publication.*

### A procedural pattern worth noting

In two of the highest-profile defeats for developers — PWDG and Project Delta — the legal hook was inadequate public notice rather than substantive land-use or environmental law. This is a replicable cause of action in any jurisdiction with rigorous notice statutes. The Saline Township case shows the opposite: where state law incorporates an exclusionary-zoning doctrine, a township that has *never* zoned land industrially has accidentally given the developer the lever to override local opposition.

---

## 2. The political and generalised dimensions

The shift from local to generalised opposition runs through residential electricity bills, environmental-justice litigation, federal regulatory action and state legislation. The political coalition is cross-cutting; the regulatory consequence is a structural rate-design pivot that will outlast the news cycle.

### Residential electricity bills as the political driver

The PJM Interconnection 2025/26 Base Residual Auction, held in July 2024, cleared at \$269.92/MW-day across most of the RTO — an **833% jump** from \$28.92/MW-day in the prior auction. The Dominion zone cleared at \$444.26/MW-day; Baltimore Gas and Electric at \$466.35/MW-day. The 2026/27 auction, held July 2025, cleared at the new \$329.17/MW-day administrative price cap across the entire RTO, with cleared volumes only 139 MW above the reliability requirement [@pjm-2025-26; @pjm-2026-27; @ud-pjm-record].

The PJM Independent Market Monitor (Monitoring Analytics) attributed the 2025/26 increase principally to data centre demand: in a November 2025 filing, it estimated that data centres accounted for **63% of the 2025/26 auction price increase**, equivalent to \$9.3 billion of the \$14.7 billion total capacity bill. Across the most recent three auctions, data centre forecasts contributed 45% of \$47.2 billion in cumulative capacity costs [@imm-imm-complaint; @ud-imm-attribution].

**Table 2: PJM capacity cost translation to residential bills (IEEFA estimates)**

| Utility / area | Estimated monthly increase | Notes |
|:---------------|---------------------------:|:------|
| Pepco (Washington DC) | ~\$21/month | From June 2025; about half attributable to capacity-price spike |
| Western Maryland | ~\$18/month | PJM capacity-driven |
| Ohio (general) | ~\$16/month | PJM capacity-driven |
| Columbus, Ohio | ~\$27/month | Highest specific-market estimate |
| PJM aggregate | +\$1.4 bn/year from June 2026 | On top of 2025/26 increase |

*Source: IEEFA and Introl analysis [@ieefa-factor10; @introl-rateshock].*

The countervailing point on attribution: PJM capacity prices reflect retiring coal, lagging interconnection-queue throughput and rising gas prices in addition to data centre demand. JLARC's December 2024 study reached the more nuanced conclusion that historical cost-shifts from data centres to other Virginia ratepayers had been "minimal" because rate design correctly assigned incurred costs, but warned that going forward a large amount of new generation and transmission would have to be built that "would not otherwise be built", creating fixed costs all customers ultimately recover. JLARC projected Dominion residential bills could rise by **\$444 per year by 2040** due to data centre growth [@jlarc-2024]. NRDC has projected \$163 billion in cumulative PJM capacity-market costs through 2033 if data centre forecasts are realised — a contingent advocacy estimate [@cub-nrdc-163bn].

### State rate cases and the PSC pivot

Public service commissions across the partisan spectrum moved through 2025-26 to put data centres into separate rate classes with minimum-bill provisions and stranded-cost protection. The structural shift is the most consequential element of the entire backlash because rate-design changes operate for decades.

- **Dominion Virginia (November 2025)**: SCC approved a new GS-5 rate class for customers ≥25 MW (effective January 2027), under which large-load customers must pay for at least 85% of contracted distribution and transmission demand and 60% of generation demand. Average residential bills rise \$11.24/month in January 2026 plus \$2.36 in January 2027 [@vamerc-scc-class; @scc-dev-2025; @loudounnow-scc].
- **Georgia Power (December 2025)**: PSC unanimously approved a stipulated agreement adding 9,885 MW of new capacity (5 new gas units), with promised "downward pressure" of at least \$8.50/month on residential rates and a three-year base-rate freeze from July 2025. Sierra Club (advocacy) sought delay arguing Georgia Power had not produced underlying math [@georgia-recorder; @sierraclub-ga-irp; @gpc-fact-sheet].
- **Entergy Louisiana (August 2025 and April 2026)**: PSC voted 4-1 to approve three new gas plants for Meta's Hyperion campus and 4-1 again to fast-track seven more for "Project Everest" — totalling **10 gas plants for Meta in Louisiana**. Commissioner Davante Lewis was the sole dissent in both votes, arguing Meta is contractually committed for only 15-20 years (about half a gas turbine's lifespan), exposing ratepayers to potential stranded costs he placed at "about a 25% risk" [@lail-entergy-meta; @fortune-meta-10-gas; @krvs-lewis].
- **AEP Ohio (July 2025; PUCO denied appeal November 2025)**: tariff requires large new data centre customers (load >25 MW) to pay for a minimum of 85% of subscribed electricity for up to 12 years. AEP Ohio's data centre load grew from ~100 MW in 2020 to 600 MW in 2024, with a forecast 5 GW by 2030 and >30,000 MW in queue. Amazon, Google, Meta, Microsoft and the Ohio Manufacturers' Association challenged unsuccessfully [@aepohio-tariff; @kjk-aep-ohio; @dcf-ohio-precedent].
- **PPL Pennsylvania (settlement subject to PUC approval, 2026)**: new large-load rate class for data centres above 50 MW peak, requires minimum 10-year service agreements with stranded-cost protection, and \$11 million for low-income rate relief [@ud-ppl-settlement; @whyy-ppl; @wpsu-ppl].
- **Wisconsin PSC (May 2026)**: ruled that large data centres served by We Energies must pick up the entire cost of new generation needed to serve them. The Alliant Beaver Dam ICR was modified on the same principle. Commissioner Kristy Nieto called this potentially "fundamentally reshaping the utility system". The Sierra Club Wisconsin chapter's tally of public comments in the dockets (a self-conducted advocacy count) found 98.5% of 2,209 written comments in the WEC tariff docket disapproved of the proposed structure, and 93% of verbal / 85% of written comments in the Alliant docket said data centres should pay 100% of their costs [@wpr-pscwi; @sierra-wi-data].

### State legislation surge

Legislators across both parties introduced more than 238 data centre bills across all 50 states in 2025; over 40 were enacted in 21 states. MultiState tracked over 300 bills across 2025, rising further in 2026. The three dominant categories are rate-structure reform, tax-incentive rollback, and construction moratoriums [@powerpolicy-makebreak; @multistate-2026].

Selected bills:

- **Virginia 2026**: SB 253 (Sen. Lucas) and HB 1393 would direct the SCC to allocate the cost of new generating capacity to customers with ≥25 MW demand. SCC estimates SB 253 would cut typical residential rates by 3.4% (~\$5.52/month) while raising data centre rates by 15.8%. Governor Spanberger amended the bills 16 April 2026 weakening the cost-shift mechanism; the General Assembly rejected most of the amendments 22 April 2026. The data-centre tax-break debate held up the state budget [@vamerc-spanberger-amend; @vamerc-ga-rejects; @introl-sb253].
- **Texas SB 6 (June 2025)**: applies to customers >75 MW. Imposes site-control documentation, financial commitment and a \$100,000 minimum fee for transmission-screening applications — explicitly framed as a defence against "phantom load" inflating ERCOT planning. ERCOT gains narrow authority to remotely curtail large loads during grid emergencies. (The original brief referred to "SB 2627"; this companion bill does not appear in standard legal summaries — SB 6 is the operative bill) [@bakerbotts-sb6; @ud-texas-sb6; @mcguire-sb6].
- **Oregon POWER Act (June 2025)**: bipartisan; first state to create a dedicated data-centre electricity rate class [@ud-ferc-pjm].
- **Maryland**: Prince George's County 180-day moratorium September 2025; state legislation under consideration in 2026 would require new data centres to be paired with new gas or nuclear generation [@conduit-md-pg; @toms-md-2bn].

### The federal regulatory arc

The most consequential federal regulatory event was FERC's **1 November 2024 order** rejecting PJM's amended Interconnection Service Agreement that would have raised the Talen-Susquehanna nuclear-Amazon co-located load from 300 MW to 480 MW. The 2-1 vote (Christie and See in favour, Phillips dissenting) found PJM had failed to justify deviations from the pro-forma ISA, and that the proposed structure would have allowed Amazon to take services from the PJM transmission system without paying for them — improperly shifting costs to other ratepayers [@ud-ferc-talen; @powermag-ferc-blocks; @ans-ferc-rejects].

Constellation Energy filed a complaint at FERC on 22 November 2024 alleging the PJM tariff was unjust because it lacked clear rules for "Fully Isolated Co-Located Load". On 20 February 2025 FERC voted unanimously to launch a Section 206 show-cause proceeding [@ferc-show-cause-feb25; @stoel-ferc-show-cause].

On **18 December 2025** FERC issued its order disposing of the show-cause proceeding. The Commission found the PJM tariff unjust and unreasonable for failing to address co-location with sufficient clarity, and directed PJM to create three new transmission services for co-located load willing to limit grid withdrawals: Interim Non-Firm Transmission Service, Firm Contract Demand and Non-Firm Contract Demand. PJM was ordered to file tariff revisions by 20 January 2026. The substantive effect is to require co-located large loads either to take fully grid-integrated transmission service (and pay for it) or to accept enforceable contractual limits on grid withdrawals — an attempt to keep AI investment economically viable while preventing large loads from free-riding on transmission paid for by other ratepayers [@ferc-pjm-colo-2025; @baker-ferc-dec25; @daypitney-ferc; @morganlewis-ferc].

### The Trump administration: pulling the other way

The Trump administration is the most consistent pro-data-centre actor in US politics. Stargate (OpenAI, Oracle, SoftBank, MGX) was unveiled at the White House on 21 January 2025, with announced commitments of \$100 billion immediately and up to \$500 billion over four years [@cnn-stargate; @time-stargate]. On 23 July 2025 the President issued **Executive Order 14148** ("Accelerating Federal Permitting of Data Center Infrastructure") covering AI-dedicated facilities of more than 100 MW, alongside the "Winning the Race: America's AI Action Plan" [@whitehouse-eo14148; @hunton-ai-action].

On 23 May 2025 Trump signed four nuclear-energy executive orders directing reform of the NRC and tasking DOE with siting and approving advanced reactors to power data centres, designating AI data centres as critical defence facilities. On 24 July 2025 DOE selected four federal sites (Idaho National Laboratory, Oak Ridge, Paducah, Savannah River) to solicit data-centre development [@doe-nuclear-eos; @pillsbury-doe-sites].

In March 2026 the White House released a "Ratepayer Protection Pledge" aimed at PJM-state governors. It was at least nominally responsive to the rate backlash, though Maryland subsequently complained to FERC that additional grid-cost allocations to its ratepayers for out-of-state data centres breach those pledges [@whitehouse-pledge; @toms-md-2bn].

### Industry response and lobbying

The Data Center Coalition (members include Amazon, Google, Microsoft, Meta, Oracle, Stack Infrastructure and major colocation operators) spent **\$978,000 on federal lobbying in 2025** — \$123k Q1, \$125k Q2, \$360k Q3, \$500k+ Q4. The fourth-quarter figure represents a fourfold increase over Q1 [@opensecrets-dcc; @opensecrets-2025-news]. State-level lobbying via the Virginia Public Access Project shows similar acceleration in Richmond [@vpap-dcc].

Microsoft committed in 2024 to "next-generation" zero-water-cooling data centre designs and matched 100% of its global electricity consumption with renewables in 2025 [@msft-sustainability]. However, Microsoft is reported to be reconsidering its 24/7 carbon-free energy matching pledge in light of AI demand growth [@geekwire-msft-cfe; @dcd-msft-cfe]. Google maintains its 24/7 CFE moonshot for 2030 but its operational emissions have risen sharply with AI [@google-sustainability]. The political read is that voluntary corporate commitments are losing credibility with regulators because the underlying load-growth trajectory is making them harder to deliver on.

---

## 3. Environmental justice as the bridge between local and political

Environmental justice is the dimension where local quality-of-life concerns and generalised political symbolism most clearly fuse. xAI's Memphis Colossus is the flagship case.

xAI began operating the Colossus 1 data centre in South Memphis in June 2024 and installed approximately 35 methane gas turbines without an air-quality permit. The Shelby County Health Department issued an air permit on 2 July 2025 covering only 15 of the turbines. The NAACP, represented by the Southern Environmental Law Center and Earthjustice, appealed the permits in July 2025 [@actionnews5-permit; @tnlookout-naacp].

In **April 2026** the NAACP filed a federal Clean Air Act lawsuit against xAI and its subsidiary MZX Tech alleging illegal operation of 27 unpermitted gas turbines for a Colossus 2 facility located across the state line in Southaven Mississippi. SELC and Earthjustice characterise the Southaven plant as potentially the largest industrial NOx source in the greater Memphis area [@naacp-xai-suit; @cnbc-musk-memphis-2026; @earthjustice-xai].

Three facts anchor the environmental-justice frame: South Memphis is majority-Black; Shelby and DeSoto Counties both received "F" ratings for ozone from the American Lung Association; and tens of thousands of people live within close range of the turbines [@earthjustice-xai].

Equity concerns have surfaced in adjacent cases. Louisiana Commissioner Lewis has framed his Meta Hyperion dissent partly in environmental-justice terms (Richland Parish has relatively low household incomes). PWDG opposition in Virginia fused historic-site protection with concerns about disproportionate siting in lower-income parts of Prince William County. The available reporting does not surface an active EPA Title VI complaint targeting a data centre as of mid-2026 — the xAI litigation is being pursued under Clean Air Act citizen-suit provisions instead. There is also a clear gap in the published academic literature on data centre siting equity at large.

---

## 4. The unusual political coalition

The political colouration of opposition is unusual in two respects.

**First, opposition is bipartisan.** Data Center Watch (industry-funded; figures directional) finds elected-official opposition between 2023 and Q2 2025 split 55% Republican / 45% Democrat. Republican objections more often centred on tax incentives and grid reliability; Democratic objections more often centred on environmental impact and equity. NPR characterised the politics as "rare bipartisan agreement" cutting across the usual lines. CNBC reported in April 2026 that Pennsylvania GOP incumbents were facing real electoral threats over the issue. Texas Public Radio headlined "Texas Republicans Have a Data Center Problem" in May 2026 [@datacenterwatch-2025; @npr-bipartisan; @nbc-bipartisan; @cnbc-pa-gop; @tpr-tx-rep].

The intra-party splits are equally interesting. In Oregon, Democratic Governor Tina Kotek proposed expanding data-centre tax breaks while Democratic legislators passed a temporary tax-break suspension. In Georgia, Republicans have split on whether to constrain data-centre development [@opb-bipartisan].

**Second, federal and state are pulling against each other.** The Trump administration is pro-data-centre via Stargate, EO 14148, the four nuclear EOs and federal-land siting. State public service commissions across the partisan spectrum are simultaneously moving in the opposite direction through new rate classes, minimum-bill provisions and stranded-cost protections. The Energy Dominance Council and 13 PJM-state governors (a politically mixed group) issued a joint statement of principles committing to use state authorities to allocate costs to data centres and protect residential customers — that is, to do exactly what the administration's permit acceleration is intended to encourage in spite of [@powerpolicy-makebreak].

The frames in play are not aligned along the usual partisan axes:

- The **consumer-protection / rate-shift** frame (centred on residential bills) appeals across the spectrum.
- The **environmental-justice / climate** frame is left-coded.
- The **property-rights / farmland / NIMBY** frame is right-coded.
- The **fiscal-conservatism / tax-break** frame is right-coded.

Where opposition has prevailed politically — Powhatan VA, Warrenton VA, Saline Township MI (initially), Prince William County VA — it has typically combined two or more of these frames into local coalitions of unusual makeup.

---

## 5. What polling shows

### National

- **Pew Research (September 2025; updated March 2026)**: 50% of US adults are more concerned than excited about AI in daily life; 10% more excited than concerned. 25% expect AI to have a negative environmental impact; 20% positive [@pew-ai-2025; @pew-ai-2026].
- **Pew Research (October 2025) on data centres specifically**: Americans hold positive views of local employment and tax-revenue benefits but more strongly negative views of energy use and environmental cost [@pew-dc-energy].
- **Morning Consult (October 2025)**: 37% of voters support a ban on AI data centre construction in their communities; 39% oppose; 24% unsure. After being primed on energy-cost impacts, support for a ban rose six points to 43% [@morning-consult-oct25].
- **University of Chicago (2025)**: 72% of Americans are at least somewhat concerned about AI's environmental impact; 41% at least very concerned [@uchicago-ai].
- **AP-NORC (October 2025)**: electricity bills are a "major" source of stress for 36% of US adults [@apnorc-bills].

### Virginia (the most-polled state)

- **Washington Post-Schar School (March 26-31, 2026, n=1,101)**: 35% of Virginia voters comfortable with new data centres in their community, **down from 69% in 2023**. 57% believe data centres are negatively affecting home energy bills; 14% positive. 59% say negative impact on local environment; 14% positive. Support for tax breaks fell from 61% to 37%. **67% want to end the sales-tax exemption; 26% want to continue it** [@wapo-poll-2026; @wapo-tablet-2026].
- **Wason Center (CNU, January 2026)**: 86% support requiring site assessments before approval covering water, grid, carbon and agricultural impact. 81% support a noise study for sites near homes or schools. 69% support prohibiting data centres within a mile of a national park, state park or historic site. 63% support requiring renewable or nuclear power for new data centres [@wason-jan26].
- **Global Strategy Group (CCAN-commissioned, 2025)** — Democratic polling firm; advocacy commission, flag accordingly: 92% of likely Virginia voters say lawmakers are failing to properly manage data centre growth [@ccan-poll-2025].

### Other states

A Texas-specific published data-centre poll number was not located. The University of Houston / Texas Southern Texas Trends Survey (October 2025) documented widespread concern about rising energy costs and grid strain but did not isolate data centres on a numerical basis [@uh-tsu-trends].

---

## 6. Are attitudes changing?

Yes. The evidence is consistent across three independent measures:

1. **Polling.** The Virginia 35% comfort number (down from 69% in two years) is the most striking single data point. National Pew, Morning Consult and University of Chicago surveys all show clear majorities (a) more concerned than excited about AI overall and (b) negative on the environmental and energy footprint of data centres specifically. The energy-bill prime increases anti-data-centre sentiment by six points in the only experiment we have.

2. **Political behaviour.** Data Center Watch's \$98 billion of blocked or delayed projects by mid-2025; the Warrenton Virginia council being voted out and replaced by a council unanimously opposed to Amazon's local data centre; Virginia's flagship cost-shift bills passing the General Assembly twice in 2026; state legislatures passing more than 40 substantive bills in 21 states in 2025; the AEP Ohio tariff and PPL settlement creating new precedents for separate large-load rate classes.

3. **Regulatory behaviour.** FERC's November 2024 rejection of the Talen-Amazon ISA, its February 2025 show-cause order, and its December 2025 PJM co-location order together represent the most consequential federal regulatory pivot on large-load arrangements in a generation. State PSCs (Virginia SCC, Louisiana PSC dissent, Ohio PUCO, Pennsylvania PUC, Wisconsin PSC) are all moving in the same direction.

The opposition is broadening from local to generalised. The political coalition is cross-cutting: GOP-led states (Texas, Ohio, Georgia) are at least as activist on rate allocation as Democratic-led states (Virginia, Maryland, New Jersey). The Trump administration is pulling in the opposite direction with permit acceleration, Stargate and federal-land siting; this creates a federal-vs-states tension that will likely sharpen through the 2026 midterms, especially in Pennsylvania where GOP incumbents face the most acute electoral exposure.

The case against treating this as a settled trend is twofold. Opposition has been building during a period of concentrated rate shocks — the PJM 2025/26 and 2026/27 auctions; supportive polling on jobs and tax revenue still exists. If capacity prices stabilise or fall — possible if announced gas builds materialise on time — public salience may decline. But the structural shift in PSC rate design, codified in tariff orders that operate for decades, will outlast the news cycle.

---

## 7. Caveats

1. **Data Center Watch numbers** (\$64-156 billion blocked/delayed) come from an industry-funded tracker that has not published audited definitions of "blocked" versus "delayed". They should be read as directional indicators rather than precise accounts.
2. **Advocacy sources** (Sierra Club, NAACP, SELC, Earthjustice, Piedmont Environmental Council, American Battlefield Trust, IEEFA, NRDC, Memphis Community Against Pollution, CCAN Action Fund) describe legitimate facts (turbine counts, court filings, ordinance language) that are independently verifiable, but their characterisations of public-health risk, motive or scale should be cross-checked against primary regulatory dockets where possible.
3. **"Moratorium" terminology** requires care. Most jurisdictional pauses are 6-12 month studies pending an ordinance, not permanent prohibitions.
4. **Rate-impact attribution** requires care. PJM capacity prices reflect retiring coal, lagging interconnection-queue throughput and rising gas prices in addition to data centre demand. Monitoring Analytics and IEEFA both publish methodology; their numbers attribute a marginal share to data centres, not all of the increase. JLARC's December 2024 finding that historical cost-shifts were "minimal" is included alongside the marginal-attribution figures.
5. **Polling commissioned by advocacy groups** has been flagged separately (Global Strategy Group / CCAN Action Fund). Pew, Wason Center, Washington Post-Schar School and Pew Research are non-advocacy.
6. **Distinguishing local from generalised concerns.** Wisconsin PSC dockets, Virginia rate cases and Texas comptroller fights involve electricity-customer interests across an entire utility footprint. They are politically related to local opposition (the same residents may oppose both) but are analytically distinct.
7. **Distinguishing site opposition from AI-ethics opposition.** Some opposition material conflates local quality-of-life concerns with national debates about AI safety, content moderation or labour displacement. The case studies in this note are all rooted in site-specific or rate-related impacts.
8. **Cases not verified.** A "Hanging Rock NC / Apex / xAI" project at the level of detail flagged in early scoping was not located; the Newark "Stargate" angle did not surface in 2025-26 reporting. The original brief's reference to "Texas SB 2627" does not appear in standard legal summaries — SB 6 is the operative bill.
9. **Outcome volatility.** Several of these cases are still moving as of May 2026 (PWDG VA Supreme Court appeal, xAI preliminary-injunction motion, Stokes County re-do, Virginia tax-break special session). Outcomes will need refresh before any further publication.

---

## 8. References

The full bibliography is below. URLs are listed in plain markdown and would convert to BibTeX entries (`@org-topic-year`) for any subsequent published article. The two underlying research drafts are kept under `background/_research_drafts/community_local.md` and `background/_research_drafts/community_political.md` for full source-level traceability.

### Primary regulatory and legislative documents

- PJM, "2025/2026 Base Residual Auction Report" (July 2024). https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf
- PJM, "2026/2027 Base Residual Auction Report" (July 2025). https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf
- Monitoring Analytics, "Complaint of the Independent Market Monitor for PJM" (Docket EL26-XX, 25 November 2025). https://www.monitoringanalytics.com/filings/2025/IMM_Complaint_re_Data_Center_Loads_Docket_No_EL26-XX_20251125.pdf
- FERC, "FERC Orders Action on Co-Location Issues Related to Data Centers Running AI" (20 February 2025). https://ferc.gov/news-events/news/ferc-orders-action-co-location-issues-related-data-centers-running-ai
- FERC, "FERC Directs Nation's Largest Grid Operator to Create New Rules" (18 December 2025). https://www.ferc.gov/news-events/news/ferc-directs-nations-largest-grid-operator-create-new-rules-embrace-innovation-and
- Virginia State Corporation Commission, "SCC Issues Order on DEV Biennial Review" (November 2025). https://www.scc.virginia.gov/about-the-scc/newsreleases/release/scc-issues-order-on-dev-biennial-review-2025/scc-rules-in-dev-biennial-review-case.html
- JLARC (Virginia), "Data Centers in Virginia" (December 2024). https://jlarc.virginia.gov/pdfs/reports/Rpt598-2.pdf
- JLARC presentation, "Virginia Data Center Study" (9 December 2024). https://jlarc.virginia.gov/pdfs/presentations/JLARC%20Virginia%20Data%20Center%20Study_FINAL_12-09-2024.pdf
- Virginia Department of Taxation, "Virginia Tax Exemptions for Data Centers" (2 January 2026). https://rga.lis.virginia.gov/Published/2026/RD40/PDF
- Senate Energy & Natural Resources Committee, hearing announcement (23 July 2025). https://www.energy.senate.gov/2025/7/chairman-lee-holds-hearing-to-address-urgent-challenges-facing-america-s-skyrocketing-energy-demands
- Senator Warren press release on hyperscaler investigation. https://www.warren.senate.gov/newsroom/press-releases/senator-warren-lawmakers-open-investigation-into-big-tech-data-centers-role-in-driving-up-families-utility-costs
- White House, Executive Order 14148 (23 July 2025). https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/
- White House, "Ratepayer Protection Pledge" fact sheet (March 2026). https://www.whitehouse.gov/fact-sheets/2026/03/fact-sheet-president-donald-j-trump-advances-energy-affordability-with-the-ratepayer-protection-pledge/
- US DOE, "9 Key Takeaways from President Trump's Executive Orders on Nuclear Energy" (May 2025). https://www.energy.gov/ne/articles/9-key-takeaways-president-trumps-executive-orders-nuclear-energy
- AEP Ohio, "Data Center Tariff" page. https://www.aepohio.com/company/about/rates/data-center-tariff/
- Georgia PSC, "Data Center Fact Sheet" (March 2026). https://psc.ga.gov/site/downloads/datacenterfactsheet.pdf
- Memphis & Shelby County Air Pollution Control Board, NAACP appeal filing (15 July 2025). https://cdn.arstechnica.net/wp-content/uploads/2025/07/NAACP-and-YGGs-xAI-Air-Permit-Appeal-7-15-2025.pdf
- Caroline County (VA) Planning Commission, SPEX-08-2025 packet. https://co.caroline.va.us/AgendaCenter/ViewFile/Item/7389?fileID=11579
- Congress.gov, S.4214 "Artificial Intelligence Data Center Moratorium Act". https://www.congress.gov/bill/119th-congress/senate-bill/4214/text

### Polling

- Washington Post, "Poll finds Virginia voters have turned against data centers" (15 April 2026). https://www.washingtonpost.com/business/2026/04/15/data-centers-poll-virginia/
- Washington Post-Schar School Virginia poll cross-tabs (March 2026). https://www.washingtonpost.com/tablet/2026/04/03/march-26-31-2026-washington-post-schar-school-virginia-poll/
- Washington Post-Schar School poll documents PDF. https://www.washingtonpost.com/documents/0eee4c34-9746-492b-babe-116e433209d1.pdf
- Pew Research, "How Americans View AI" (September 2025). https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
- Pew Research, "Key findings about how Americans view artificial intelligence" (March 2026). https://www.pewresearch.org/short-reads/2026/03/12/key-findings-about-how-americans-view-artificial-intelligence/
- Pew Research, "What we know about energy use at U.S. data centers" (24 October 2025). https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/
- Morning Consult, "Voters Divided Over Banning AI Data Center Construction" (October 2025). https://pro.morningconsult.com/analysis/ai-data-center-construction-voter-polling-october-2025
- University of Chicago Institute for Climate, "2025 Poll: Americans' Views on the Environmental Impact of AI". https://climate.uchicago.edu/insights/2025-poll-americans-views-on-the-environmental-impact-of-ai
- Wason Center for Civic Leadership poll, January 2026, via WDBJ7. https://www.wdbj7.com/2026/01/29/wason-center-releases-results-new-poll-various-virginia-issues/
- Mason-Dixon Polling & Strategy, "December 2024 Virginia poll" (commissioned by VHHA). https://vhha.com/wp-content/uploads/2025/01/Mason-Dixon-Poll-December-2024.pdf
- Cardinal News, "CNU poll: Spanberger up, data centers down" (January 2025). https://cardinalnews.org/2025/01/16/cnu-poll-spanberger-up-data-centers-down-except-maybe-in-southwest-virginia/
- AP-NORC, via ABC News, "Voters anger over high electricity bills" (October 2025). https://abcnews.go.com/US/wireStory/voters-anger-high-electricity-bills-data-centers-loom-127325979
- CCAN Action Fund (Global Strategy Group, 2025) — advocacy. https://ccanactionfund.org/92-of-virginians-say-lawmakers-must-do-more-to-control-data-center-impacts/
- University of Houston / Texas Southern Texas Trends Survey (October 2025). https://www.uh.edu/news-events/stories/2025/october/10272025-texas-trends-survey-energy-2025.php

### Major newspapers and academic / industry analysts

- Bisnow, "Developer Backs Out Of 17-GW Virginia Data Center Plan". https://www.bisnow.com/national/news/data-center-development/developer-backs-out-of-17-gw-virginia-data-center-plan-134341
- Bloomberg, "Loudoun County Data Center Growth Strains Residents Seeking AI Regulation" (29 July 2025). https://www.bloomberg.com/news/features/2025-07-29/loudon-county-data-center-growth-strains-residents-seeking-ai-regulation
- Capital B News, "A Historic Black Community Takes On the World's Richest Man Over Environmental Racism". https://capitalbnews.org/musk-xai-memphis-black-neighborhood-pollution/
- CNBC, "Microsoft data center rejected in Wisconsin village, AI boom hits snag" (25 November 2025). https://www.cnbc.com/2025/11/25/microsoft-ai-data-center-rejection-vs-support.html
- CNBC, "Microsoft's plans for 15 more data centers win approval" (26 January 2026). https://www.cnbc.com/2026/01/26/microsoft-wins-approval-for-15-data-centers-at-wisconsin-foxconn-site.html
- CNBC, on xAI Memphis lawsuit (April 2026). https://www.cnbc.com/2026/04/14/elon-musk-xai-memphis-data-centers.html
- CNBC, "AI data center backlash threatens Pennsylvania GOP incumbents" (24 April 2026). https://www.cnbc.com/2026/04/24/ai-data-centers-pennsylvania-republicans-2026-election.html
- CNN, on Stargate (21 January 2025). https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment
- Fortune, "A Michigan farm town voted down plans for a giant OpenAI-Oracle data center" (6 May 2026). https://fortune.com/2026/05/06/ai-data-center-michigan-saline-politics-farmland/
- Fortune, "Meta orders 10 gas-fired power plants for its Hyperion AI campus" (March 2026). https://fortune.com/2026/03/27/meta-hyperion-10-gas-power-plants-louisiana-entergy/
- NPR, "These major issues have brought together Democrats and Republicans" (February 2026). https://www.npr.org/2026/02/26/nx-s1-5726431/data-centers-ai-trump-housing-states
- NBC News, "Reining in data centers sparks rare bipartisanship in statehouses". https://www.nbcnews.com/politics/politics-news/reining-data-centers-sparks-rare-bipartisanship-statehouses-rcna262990
- TIME, "What to Know About Stargate". https://time.com/7209167/stargate-openai-donald-trump/
- Texas Public Radio, "Texas Republicans Have a Data Center Problem" (May 2026). https://www.tpr.org/news/2026-05-07/texas-republicans-have-a-data-center-problem
- Texas Tribune, "Plan to run El Paso data center on natural gas" (26 January 2026). https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/
- Texas Tribune, "Texas losing a billion dollars a year on data center tax break" (8 April 2026). https://www.texastribune.org/2026/04/08/texas-data-centers-sales-tax-break-billion-dollars/
- Tom's Hardware, "Virginia voter support for new data centers collapses to 35%". https://www.tomshardware.com/tech-industry/virginia-voter-support-for-new-data-centers-collapses-to-35-percent
- Tom's Hardware, on Maryland $2bn FERC complaint. https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises
- The Hill, "Bipartisan local backlash to data centers halts $64B" (2025). https://thehill.com/policy/technology/5605667-data-center-criticism-study/
- The Hill, "Anti-data center measures gain traction at state, local level". https://thehill.com/policy/technology/5843665-data-center-backlash-grows/
- Virginia Mercury (multiple): https://virginiamercury.com/2026/04/16/lawmakers-dominion-say-spanbergers-amendments-weaken-bill-to-shift-costs-onto-data-centers/ ; https://virginiamercury.com/2026/04/23/va-lawmakers-ok-governors-tweaks-to-major-energy-bills-reject-health-and-labor-bill-amendments/ ; https://virginiamercury.com/2026/04/27/data-center-tax-exemption-changes-still-holding-up-virginia-budget/ ; https://virginiamercury.com/2025/11/25/scc-approves-chesterfield-gas-plant-and-dominion-rate-hike-creates-new-rate-class-for-data-centers/ ; https://virginiamercury.com/2025/12/16/virginia-regulators-weigh-expanded-use-of-data-centers-polluting-generators/
- VPM, "$2B data center tax break fight pushes Virginia budget negotiations" (12 March 2026). https://www.vpm.org/generalassembly/2026-03-12/budget-data-center-tax-break-scott-lucas-spanberger-torian-rephann
- WPR (Wisconsin Public Radio), on PSC May 2026 ruling. https://www.wpr.org/news/state-regulators-change-we-energies-data-center-rate-proposal-to-protect-customers
- Power Magazine, "FERC Blocks PJM Proposal to Expand Amazon Data Center Load" (November 2024). https://www.powermag.com/ferc-blocks-pjm-proposal-to-expand-amazon-data-center-load-at-susquehanna-nuclear-plant/
- ANS, "FERC rejects interconnection deal for Talen-Amazon data centers". https://www.ans.org/news/article-6534/ferc-rejects-interconnection-deal-for-talenamazon-data-centers/
- Open Secrets, Data Center Coalition lobbying profile. https://www.opensecrets.org/federal-lobbying/clients/summary?cycle=2025&id=D000118063
- Open Secrets, "Data centers are fueling the lobbying industry" (November 2025). https://www.opensecrets.org/news/2025/11/data-centers-are-fueling-the-lobbying-industry-not-just-the-growth-of-ai/
- VPAP, Data Center Coalition Virginia lobbying. https://www.vpap.org/lobbying/client/352969-data-center-coalition/

### Industry / trade press

- Utility Dive (multiple): https://www.utilitydive.com/news/pjm-interconnection-capacity-auction-data-center/808264/ ; https://www.utilitydive.com/news/data-centers-pjm-capacity-auction-market-monitor/801780/ ; https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/ ; https://www.utilitydive.com/news/ferc-pjm-colocation-data-center/808368/ ; https://www.utilitydive.com/news/texas-law-gives-grid-operator-power-to-disconnect-data-centers-during-crisi/751587/ ; https://www.utilitydive.com/news/ppl-electric-rate-case-settlement-data-center-tariff/814760/ ; https://www.utilitydive.com/news/ferc-interconnection-isa-talen-amazon-data-center-susquehanna-exelon/731841/
- Data Center Frontier, "Ohio Sets New Precedent: AEP's Power Rules Shift Data Center Cost Burden". https://www.datacenterfrontier.com/energy/article/55304787/ohio-sets-new-precedent-aeps-power-rules-shift-data-center-cost-burden
- Data Center Frontier on Texas SB 6. https://www.datacenterfrontier.com/energy/article/55298872/texas-senate-bill-6-a-bellwether-on-how-states-may-approach-data-center-energy-use
- Holland & Knight, "Loudoun County, Virginia, Eliminates By-Right Data Center Development" (April 2025). https://www.hklaw.com/en/insights/publications/2025/04/loudoun-county-virginia-eliminates-by-right-data-center-development
- Baker Botts on Texas SB 6. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation
- McGuireWoods on Texas SB 6. https://www.mcguirewoods.com/client-resources/alerts/2025/7/texas-senate-bill-6-significantly-expands-regulatory-oversight-over-large-loads-in-ercot/
- Baker Botts on FERC December 2025 order. https://www.bakerbotts.com/thought-leadership/publications/2025/december/ferc-issues-order-providing-guidance-for-co-locating-power-plants-with-data-centers-within-pjm
- Pillsbury Law, on DOE site selection. https://www.pillsburylaw.com/en/news-and-insights/AI-data-center-DOE-site-trump.html
- Stoel, FERC show-cause analysis. https://www.stoel.com/insights/publications/ferc-institutes-show-cause-proceeding-to-address-co-location-issues-related-to-data-centers-running-ai-in-pjm-and-requests-industry-comments
- KJK, on AEP Ohio tariff. https://kjk.com/2025/11/14/regulating-surge-legal-analysis-aep-ohios-data-center-tariff-and-pucos-approval/
- Power Policy, "Data Centers Could Make or Break". https://www.powerpolicy.net/p/data-centers-could-make-or-break
- MultiState, "State Data Center Legislation in 2026". https://www.multistate.us/insider/2026/2/20/state-data-center-legislation-in-2026-tackles-energy-and-tax-issues
- CSG South, "Take That for Data". https://csgsouth.org/policies/take-that-for-data-incentivizing-innovation-or-inefficiency/
- Conduit Street (Maryland Counties), on Prince George's moratorium. https://conduitstreet.mdcounties.org/2025/09/24/prince-georges-pauses-data-center-approvals-amid-policy-review/
- Latitude Media, "In Indiana, an anatomy of data center opposition". https://www.latitudemedia.com/news/in-indiana-an-anatomy-of-data-center-opposition/
- Latitude Media, "Data center jobs aren't at servers". https://www.latitudemedia.com/news/data-center-jobs-arent-at-servers-theyre-in-energy/
- Commercial Observer, "Data Center Opposition Has Scrambled the Calculations" (Feb 2026). https://commercialobserver.com/2026/02/opposition-data-centers-real-estate-reasons/
- Good Jobs First, "Virginia Tax Revenue Losses to Data Centers Soar to $1.6 Billion for FY25". https://goodjobsfirst.org/virginia-tax-revenue-losses-to-data-centers-soar-to-1-6-billion-for-fy25/
- Good Jobs First, "Data Center Moratorium Bills Are Spreading in 2026". https://goodjobsfirst.org/data-center-moratorium-bills-are-spreading-in-2026/
- Wisconsin Examiner, "Rural Wisconsin has become a hotspot for data centers" (January 2026). https://wisconsinexaminer.com/2026/01/22/rural-wisconsin-has-become-a-hotspot-for-data-centers-states-unique-tax-instrument-explains-why/

### Advocacy sources (clearly flagged)

- Earthjustice, "Illegal Pollution from Data Center Power Plants — We're Suing xAI". https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus
- Earthjustice press release, NAACP April 2026 emergency action. https://earthjustice.org/press/2026/naacp-asks-court-for-emergency-action-to-stop-illegal-air-pollution-from-xais-data-center-power-plant
- SELC, "xAI built an illegal power plant". https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/
- SELC, "A rural community steps up to stop data centers". https://www.selc.org/news/a-rural-community-steps-up-to-stop-data-centers/
- NAACP, "NAACP Sues xAI for Illegal Pollution". https://naacp.org/articles/naacp-sues-xai-illegal-pollution-data-center-power-plant
- Sierra Club Wisconsin, "The Data is In: Widespread Disproval for Data Center Costs in Wisconsin" (April 2026). https://www.sierraclub.org/wisconsin/blog/2026/04/data-widespread-disproval-data-center-costs-wisconsin
- Sierra Club, on Georgia PSC IRP. https://www.sierraclub.org/press-releases/2025/12/georgia-public-service-commission-issues-final-order-data-center-power-plan
- IEEFA, "Projected data center growth spurs PJM capacity prices by factor of 10". https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
- NRDC / Citizens Utility Board, "$163B in additional electricity capacity costs". https://www.citizensutilityboard.org/blog/2025/10/23/data-center-concerns-cub-nrdc-experts-warn-pjm-states-could-get-hit-with-forced-blackouts-163b-in-additional-electricity-capacity-costs/
- Piedmont Environmental Council, "Proposed Increase to Data Center Diesel Generator Use". https://www.pecva.org/work/energy-work/proposed-increase-to-data-center-diesel-generator-use/
- PEC, "Massive 'Digital Gateway' Data Center Project Has Been Halted". https://www.pecva.org/region/regional-state-national-region/prince-william/massive-digital-gateway-data-center-project-has-been-halted/
- American Battlefield Trust, "Digital Gateway Threatens to Overwhelm Manassas". https://www.battlefields.org/speak-out/digital-gateway-threatens-overwhelm-manassas-battlefield
- Data Center Watch (industry-funded), Report. https://www.datacenterwatch.org/report
- Data Center Watch Q2 2025 update. https://www.datacenterwatch.org/q22025
- Data Center Coalition (industry). https://datacentercoalition.org

### Project-level reporting

- Action News 5 Memphis, "Health dept grants permit xAI turbines". https://www.actionnews5.com/2025/07/02/health-dept-grants-permit-xai-turbines/
- Tennessee Lookout, "NAACP others appeal xAI turbine permits". https://tennesseelookout.com/briefs/naacp-others-appeal-xai-turbine-permits-for-memphis-data-center/
- AZ Luminaria, "Tucson City Council rejects Project Blue" (6 August 2025). https://azluminaria.org/2025/08/06/tucson-city-council-rejects-project-blue-amid-intense-community-pressure/
- KJZZ, "Rejected by Tucson and abandoned by Amazon, Project Blue" (December 2025). https://www.kjzz.org/the-show/2025-12-09/rejected-by-tucson-and-abandoned-by-amazon-project-blue-data-center-moves-forward
- Phoenix New Times, "How much water will Chandler's data center project use?" https://www.phoenixnewtimes.com/news/how-much-water-will-chandlers-data-center-project-use-40627750/
- Fox 10 Phoenix, "Chandler City Council unanimously rejects". https://www.fox10phoenix.com/news/chandler-data-center-proposal-draws-heavy-opposition-council-meeting
- Bristow Beat, "NASA scientist brings attention to data center noise levels". https://bristowbeat.com/stories/nasa-scientist-brings-attention-to-data-center-noise-levels,11231
- WUSA9, "As data center noise concerns grow, Loudoun Co. officials discuss possible mitigation". https://www.wusa9.com/article/news/local/data/loudoun-county-officials-data-center-noise/65-45884219-750f-4d47-a660-71a20d8db001
- Prince William Times, "Park superintendent warns of data centers' 'wholesale destruction'". https://www.princewilliamtimes.com/news/park-superintendent-warns-of-data-centers-wholesale-destruction-of-historic-areas-around-the-manassas-battlefield/article_278caca0-37c3-11ee-9f99-abdeeaa89493.html
- WTOP, "Prince William Co. withdraws from Digital Gateway lawsuit" (April 2026). https://wtop.com/virginia/2026/04/prince-william-co-withdraws-from-digital-gateway-lawsuit-reversing-course-from-2023/
- Michigan Public, "Michigan regulators approve Saline Twp data center request" (December 2025). https://www.michiganpublic.org/environment-climate-change/2025-12-18/michigan-regulators-approve-saline-twp-data-center-request-with-conditions
- WPR, "Port Washington data center campus" (Lighthouse Stargate). https://www.wpr.org/news/port-washington-data-center-campus-openai-oracle-stargate-chatgpt
- PBS Wisconsin, "Wisconsin communities face scrutiny over data center secrecy". https://pbswisconsin.org/news-item/wisconsin-communities-face-scrutiny-over-data-center-secrecy-beyond-use-of-ndas/
- Reasons to Be Cheerful, "The Small Wisconsin City That Defeated a Giant Data Center". https://reasonstobecheerful.world/menomonie-wisconsin-data-center-toolkit/
- WSB-TV Atlanta, "Palmetto residents concerned over data center construction". https://www.wsbtv.com/news/local/atlanta/palmetto-residents-concerned-over-data-center-construction-neighboring-coweta-county/AKZ6W5ZB3JAOFEY7DOLVX7FUGY/
- AJC, on Microsoft Atlanta land grab. https://www.ajc.com/news/business/microsoft-continues-aggressive-metro-atlanta-land-grab-for-data-center-development/2OCAF752OFEUDNJTOJPVWLRDGI/
- CBS Atlanta, on DeKalb moratorium. https://www.cbsnews.com/atlanta/news/dekalb-leaders-extend-data-center-moratorium-to-june-as-residents-raise-health-cost-concerns/
- LaGrange News, on Troup County. https://www.lagrangenews.com/news/commissioners-approve-data-center-ordinance-lift-moratorium-2b6e15ed
- The Current GA, on Glynn County. https://thecurrentga.org/2026/04/15/glynn-county-to-vote-on-zoning-residents-ask-to-delay-data-center-rule/
- NC Health News, "NC communities push back on AI data centers" (March 2026). https://www.northcarolinahealthnews.org/2026/03/25/nc-communities-push-back-ai-data-centers-project-delta-lawsuit/
- NC Newsline, "Community groups sue over planned data center in Stokes County". https://ncnewsline.com/2026/03/13/community-groups-sue-over-planned-data-center-in-stokes-county/
- VPM, "Data center opposition is 'catching a fire' across North Carolina politics" (May 2026). https://www.vpm.org/news/2026-05-05/wunc-data-center-opposition-political-challenges-north-carolina
- Indiana Economic Digest, "LaPorte County backs limits on data centers". https://indianaeconomicdigest.net/Content/Most-Recent/Agriculture/Article/LaPorte-County-backs-limits-on-data-centers-amid-farmland-concerns/31/68/120326
- WNDU, "LaPorte moves forward with annexation of 1,000 acres" (April 2026). https://www.wndu.com/2026/04/14/city-laporte-votes-annex-roughly-1000-acres-farmland-near-microsoft-data-center-project/
- Inside Climate News, "Facing Its Third Data Center, an Iowa County Rolls Out Extensive Zoning Rules" (March 2026). https://insideclimatenews.org/news/01032026/iowa-county-data-center-ordinance/
- Spotlight Delaware, "Two New Castle County industrial projects may become data centers" (December 2025). https://spotlightdelaware.org/2025/12/16/two-new-castle-county-industrial-projects-may-become-data-centers/
- Data Center Knowledge, "University of Delaware Puts Nail in Coffin". https://www.datacenterknowledge.com/regulations/university-of-delaware-puts-nail-in-coffin-of-data-center-and-power-plant-project
- Bisnow, "Loudoun Approves Controversial Data Center After Initial Opposition". https://www.bisnow.com/washington-dc/news/data-center/loudoun-approves-controversial-data-center-after-initial-opposition-84151
- TIME, "Inside the Memphis Community Battling Elon Musk's xAI". https://time.com/7308925/elon-musk-memphis-ai-data-center/
- El Paso Matters, on Meta data centre gas plant. https://elpasomatters.org/2026/01/18/el-paso-electric-meta-data-center-new-473-million-natural-gas-power-plant/
- Heinrich Böll Stiftung, "How South Memphis Is Refusing AI's Big Lies" (January 2026). https://us.boell.org/en/2026/01/28/promise-peace-plenty-how-south-memphis-refusing-ais-big-lies
- Louisiana Illuminator, on Meta-Entergy. https://lailluminator.com/2025/08/20/entergy-meta/
- The Lens (NOLA), "Enforceable guarantees or pinky promises?" (April 2026). https://thelensnola.org/2026/04/14/meta-project-evest-louisiana-energy-expansion-costs-entergy/
- WBRZ, "PSC votes 4-1 to fast-track Entergy's proposal" (April 2026). https://www.wbrz.com/news/psc-votes-4-1-to-fast-track-entergy-s-proposal-for-billions-in-energy-investments-to-power-meta-data-center
- KRVS, "Entergy wants to fast-track $21B Meta deal" (April 2026). https://www.krvs.org/louisiana-news/2026-04-14/entergy-wants-to-fast-track-21b-meta-deal-as-psc-commissioner-advocates-sound-alarm
- Cardinal News, "General Assembly rejects more than a dozen of Spanberger amendments". https://cardinalnews.org/2026/04/22/general-assembly-rejects-more-than-a-dozen-of-spanbergers-amendments/
- Microsoft Sustainability page. https://datacenters.microsoft.com/sustainability/
- Microsoft 2025 Environmental Sustainability Report. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2025-Microsoft-Environmental-Sustainability-Report.pdf
- GeekWire, "Report: as AI electricity demands soar, Microsoft weighs retreat from CFE pledge". https://www.geekwire.com/2026/report-as-ai-electricity-demands-soar-microsoft-weighs-retreat-from-ambitious-carbon-free-energy-pledge/
- Google Data Centers sustainability page. https://datacenters.google/operating-sustainably/
- Stanford Law Review, "The Future of Environmental Justice Claims Under Title VI" (May 2025). https://law.stanford.edu/wp-content/uploads/2025/05/Sivas-FINAL.pdf

---

*End of background note. Two underlying research drafts are kept under `background/_research_drafts/community_local.md` and `background/_research_drafts/community_political.md` for traceability.*
