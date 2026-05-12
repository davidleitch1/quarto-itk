# Australian data centre industry — flexibility, demand response, BTM batteries and grid-cost positioning

**Date prepared:** 11 May 2026
**Prepared for:** ITK research note on Australian data centre industry response
**Scope:** Operating fleet, industry positions on grid services and demand flexibility, AEMO/AEMC engagement, behind-the-meter assets, federal and state policy, and how Australia's debate diverges from the US.

---

## 1. Headline picture

Australia's data centre fleet is small in absolute terms — about **1.35 GW operating IT load at end-2025** [Source: https://www.cefc.com.au/insights/market-reports/data-centre-growth-and-the-energy-transition/] versus roughly **50 GW** in the United States [Source: https://www.utilitydive.com/news/data-centers-miso-ferc-market-report/815831/] — but the pipeline is the political story. AEMO received **44 GW of data centre connection requests** from network service providers in the 2025 IASR process, against only ~6 GW required to meet Step Change demand [Source: https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2024/2025-iasr-scenarios/final-docs/oxford-economics-australia-data-centre-energy-consumption-report.pdf]. The CEFC/Baringa central forecast has Australian data centre capacity reaching **4.7-7.4 GW by 2035**, with electricity consumption rising from ~2% of NEM-supplied energy today to as much as **11% of national consumption** [Source: https://www.cefc.com.au/media/media-release/data-centre-boom-to-reshape-australia-s-energy-future-cefc-baringa-report/].

Three things make the Australian conversation different from the US one:

- **An organised industry voice has only just formed.** Data Centres Australia (DCA) was launched on 28 November 2025 by AirTrunk, AWS, CDC, Microsoft and NEXTDC, with NEXTDC CEO Craig Scroggie as inaugural chair and former Microsoft government affairs head Belinda Dennett as CEO. STACK, Equinix, Goodman, Schneider Electric and TikTok joined at launch [Source: https://www.cyberdaily.au/security/12953-thinking-machines-data-centre-giants-launch-new-aussie-peak-body-data-centres-australia ; Source: https://thetechcapital.com/data-centres-australia-names-nextdc-ceo-chair-of-new-peak-industry-body/]. There is no Australian equivalent of Tyler Norris's Duke/EPRI DCFlex line of work.

- **The political coalition has converged remarkably fast around "data centres should pay their own way."** A February 2026 statement by the Clean Energy Council, Electrical Trades Union, ACF, WWF-Australia, Smart Energy Council, RE-Alliance, Climate Energy Finance, Nature Conservation Council NSW, Environment Victoria, Queensland Conservation Council, Sunrise Project Australia and Carbon Zero Initiative — an unusual industry/union/environment alliance — demanded operators "build the renewables and water recycling to power" their facilities [Source: https://cleanenergycouncil.org.au/news-resources/data-centre-rush-must-power-itself-says-industry,-unions-and-environment-groups]. The Albanese Government's December 2025 *National AI Plan* and accompanying *expectations of data centres and AI infrastructure developers* explicitly require operators to "underwrite new renewable power supply, pay their full share of new grid connectivity so costs are not passed to consumers or businesses, and support Australia's energy transition through demand flexibility mechanisms" [Source: https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/ ; Source: https://www.industry.gov.au/news/australia-launches-national-ai-plan-capture-opportunities-share-benefits-and-keep-australians-safe].

- **Behind-the-meter response patterns are different.** There is no Australian equivalent of the US BTM gas turbine surge (Voltagrid, Bloom, Enchanted Rock, Solar Group at Memphis). NSW/VIC pipeline gas economics, the lack of cheap stranded gas in the urban load centres, and Australia's planning culture all point operators towards **on-site BESS plus utility-scale solar/wind PPAs**, not on-site reciprocating gas. Diesel remains the only sanctioned BTM generation, and the Mamre Road 1.2 GW proposal — with **852 diesel back-up generators** and 7,488 lithium-ion battery cabinets — gives a sense of the scale [Source: https://urbandigest.com.au/ssd-92743706-mamre-road-data-centre-campus/].

The thinness of Australian published material on data centre flexibility, particularly compared to the US DCFlex / EPRI / PJM literature, is itself a finding and is flagged throughout.

---

## 2. The operating fleet

### Headline numbers

**Table 1: Australian data centre operating IT load — end-2025 best estimates**

| Source | Operating IT load | Notes |
|:-------|------------------:|:------|
| CEFC/Baringa (Dec 2025) | ~1,350 MW | "Today" baseline against 4.7-7.4 GW 2035 forecast |
| US Studies Centre (Mar 2026) | ~1,400 MW across ~250 facilities | NSW 80%, VIC ~15% |
| Oxford Economics for AEMO (Jul 2025) | 3.9 TWh consumption FY25; ~98% in NEM; ~2% of NEM-supplied | Implies ~600-800 MW average load — consistent with 1.3-1.4 GW peak |
| M3 Property (Nov 2025) | "1.3 GW live; 0.7-1.7 GW supply gap by 2028" | Forecast 1.8 GW live by 2028 |

*Source: ITK compilation. CEFC: https://www.cefc.com.au/media/hs5ner3s/getting-the-balance-right-data-centres-and-the-energy-transition-full-report.pdf ; USSC: https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid ; Oxford Economics: https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2024/2025-iasr-scenarios/final-docs/oxford-economics-australia-data-centre-energy-consumption-report.pdf ; M3 Property: https://m3property.com.au/static/88f0d39061ca9072f2bf0a5b61dc5c3f/M3-Property-Report-Data-Centre-Growth-in-Australia-November-25.pdf*

The 1.3-1.4 GW figure should be treated as the **best single point estimate for operating IT load**. The often-quoted "2 GW" headline appears to confuse operating IT load with gross site MW or with announced/contracted but not commissioned capacity.

### Operators

**Table 2: Major Australian data centre operators — operating IT capacity (best estimates, end-2025/early 2026)**

| Operator | Ownership | Operating IT load (Australia) | Notable campuses |
|:---------|:----------|------------------------------:|:-----------------|
| AirTrunk | Blackstone + CPP Investments (acquired Sep 2024 for A$24 bn) | >1,200 MW across 5 campuses | SYD1 (121+ MW), SYD2 (158+ MW), SYD3 (330+ MW), MEL1 (276+ MW), MEL2 (354+ MW; opening 2H27) |
| NEXTDC | ASX-listed | ~316 MW contracted utilisation as of Sep 2025; pro-forma 416.6 MW after 1H26 wins | M1-M4 Melbourne, S1-S6 Sydney, P1-P2 Perth, B1-B2 Brisbane, C1 Canberra, A1 Adelaide, plus PH1 Pilbara |
| CDC Data Centres | Infratil 48% / Future Fund | ~281 MW operating Eastern Creek campus + Canberra campuses | Marsden Park 504 MW campus approved Nov 2025 (under construction) |
| Microsoft | Microsoft | "29 sites" announced; from ~3 operating in late 2025 with three more in build | Sydney + Melbourne + Canberra |
| AWS | Amazon | Asia Pacific (Sydney) + Asia Pacific (Melbourne) Regions; specific MW not disclosed | Multiple sites Sydney + Melbourne |
| Equinix | Equinix | Multiple smaller IBX facilities | SY-series Sydney, ME-series Melbourne |
| Macquarie Data Centres | ASX-listed Macquarie Technology Group | IC3 Super West Macquarie Park + Canberra | ~80 MW announced expansion |
| DCI | Brookfield (via 2024 acquisition from Northern Data) | Multiple cities | Eastern Creek, Adelaide, Darwin |
| Global Switch | CK Hutchison Holdings | SYD-1 Pyrmont + SYD-2 Ultimo | ~110 MW |
| Quinbrook (Supernode) | Quinbrook Infrastructure | New build at Brendale QLD | Co-located with 780 MW / 3,074 MWh BESS |

*Source: ITK compilation from operator websites, ASX disclosures, ResearchAndMarkets/Arizton portfolio reports. AirTrunk: https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/ ; NEXTDC: https://announcements.asx.com.au/asxpdf/20251201/pdf/06sr3ff6f4q4vv.pdf ; CDC: https://www.nsw.gov.au/ministerial-releases/data-centre-investment-sustainable-development ; AirTrunk Blackstone: https://airtrunk.com/completion-of-airtrunk-acquisition-by-blackstone-marking-new-era-of-growth/ ; Quinbrook: https://www.quinbrook.com/news-insights/quinbrooks-supernode-battery-completes-construction/*

### Geographic concentration

NSW hosts roughly 80% of Australian data centre capacity, Victoria most of the remainder, with Canberra (mainly federal-government colocation), Brisbane, Perth and Adelaide accounting for the residual [Source: https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid]. Western Sydney (Eastern Creek, Marsden Park, Kemps Creek/Mamre Road) and Macquarie Park are the two NSW clusters; Melbourne capacity concentrates in the western and northern suburbs. Per the existing background note `datacentre_locationfactors.md`, Australia's pattern is markedly more capital-city-clustered than the US, driven by cable landings, fibre exchanges, the colocation-heavy customer mix and the absence of cheap stranded power equivalent to PJM/ERCOT-adjacent rural sites.

**Regional / power-anchored projects** are a small but real category:

- **NEXTDC Pilbara edge:** PH1 (Port Hedland, operating) and NE1 (Newman, in construction). These are small modular edge facilities for mining customers — no hyperscale build [Source: https://www.nextdc.com/data-centres/port-hedland-data-centre-colocation].
- **Quinbrook Supernode (Brendale, QLD):** US$2.5 bn data centre adjacent to the South Pine substation, co-located with a 780 MW/3,074 MWh BESS contracted to Origin (stages 1-2) and Stanwell (stage 3). Stage 1 BESS energised September 2025 [Source: https://www.quinbrook.com/news-insights/quinbrooks-supernode-battery-completes-construction/ ; Source: https://www.datacenterdynamics.com/en/news/quinbrook-to-build-17-billion-data-center-2gwh-battery-storage-in-queensland-australia/].
- **Hunter Valley / coal-region speculation:** AGL has confirmed it is in discussions with data centre operators for "integrated energy hubs" on its Hunter sites; nothing publicly committed [Source: https://www.gloucesteradvocate.com.au/story/9168623/how-data-centres-could-impact-the-upper-hunters-post-mining-era/]. **No Macquarie Mortlake hyperscale data centre has been publicly announced** — the Mortlake activity is the existing 566 MW Origin gas plant plus the Origin 650 MWh BESS expected online late 2025. The Macquarie name in the brief appears to confuse the unrelated Macquarie Data Centres operator.
- **Tasmania:** Mostly small enterprise/colocation (DC3, TasmaNet). Firmus has approval for a 90 MW St Leonards facility near Launceston; Viridis has planning approval for a 1 MW Tasmanian site [Source: https://www.datacenterdynamics.com/en/news/australias-viridis-gets-approval-for-1mw-tasmania-data-center/]. Hydropower-anchored hyperscale remains a concept rather than a project.

---

## 3. Pipeline projects worth flagging

**Table 3: Major announced Australian projects — capex / capacity / status**

| Project | Operator | Location | Capacity | Status |
|:--------|:---------|:---------|:---------|:-------|
| Mamre Road / SYD4 | AirTrunk (site IFM) | Kemps Creek, NSW | 1.2 GW; 6 buildings; 852 diesel gensets | SSDA on public exhibition; SEARs issued 30 Sep 2025; construction targeted early 2026 |
| Marsden Park | CDC | Marsden Park, NSW | 504 MW (scalable to 1 GW) | NSW approval 28 Nov 2025; A$3.1 bn |
| S7 Eastern Creek | NEXTDC + OpenAI | Eastern Creek, NSW | 550 MW; A$7 bn | MoU Dec 2025; first phase target 2H 2027 |
| MEL2 | AirTrunk | Melbourne, VIC | 354+ MW; A$5 bn | Multi-phase; target 2H 2027 |
| Microsoft Australia A$25 bn | Microsoft | Sydney + Melbourne + Canberra | 29 total sites announced (vs 20 in 2023); 3 operating + 3 in build as of Oct 2025 | A$5 bn 2023 → A$25 bn (US$18 bn) by 2029 announced Apr 2026; MoU with federal government on the National AI Plan expectations |
| AWS A$20 bn | AWS | Sydney + Melbourne; new sites SW Sydney + outside Melbourne | Specific MW not disclosed | Apr 2025 announcement; supersedes earlier A$13.2 bn 2023-27 plan |
| Supernode | Quinbrook | Brendale, QLD | Stage 1 BESS energised Sep 2025; data hall to follow | A$2.5 bn total |
| Macquarie Park multi-site | Macquarie Data Centres + others | Macquarie Park, NSW | 4 new data centres seeking Ausgrid connection; new substation being built | Third Macquarie Park transformer commissioned Dec 2025; new Wallumatta STS contingent project filed Oct 2025 |

*Source: ITK compilation. AirTrunk Mamre: https://urbandigest.com.au/ssd-92743706-mamre-road-data-centre-campus/ and https://ia.acs.org.au/article/2026/concern-over-australia-s-most-power-hungry-data-centre.html ; CDC Marsden: https://www.nsw.gov.au/ministerial-releases/southern-hemispheres-biggest-data-centre-gets-green-light ; NEXTDC S7: https://www.theurbandeveloper.com/articles/eastern-creek-data-centre-550mw-openai-nextdc and https://www.nextdc.com/news/building-the-next-generation-of-sovereign-ai-infrastructure-in-australia ; AirTrunk MEL2: https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/ ; Microsoft A$25 bn: https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/ ; AWS A$20 bn: https://www.aboutamazon.com/news/aws/amazon-data-center-investment-in-australia ; Macquarie Park substation: https://www.aer.gov.au/system/files/2025-11/Ausgrid%20-%20Contingent%20Project%20Application%20-%20New%20Wallumatta%20STS%20-%2031%20October%202025.pdf*

The gap between **announced** capex and **delivered** MW is large and matters. Microsoft's 2023 A$5 bn commitment was upgraded to A$25 bn by April 2026 [Source: https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/], but as of October 2025 Microsoft itself acknowledged only three operating Australian sites with three more under construction. AWS's earlier A$13.2 bn (2023-27) commitment has been superseded by an A$20 bn (US$13.3 bn) 2025-2029 announcement [Source: https://www.aboutamazon.com/news/aws/amazon-data-center-investment-in-australia]. Treat hyperscaler dollar pledges as forward intent, not as in-service load.

---

## 4. Industry positions on flexibility, demand response and BTM batteries

### Data Centres Australia (the new peak body)

DCA's first major substantive output is the November 2025 Mandala Partners report **"Data Centres as Enabling Infrastructure"**, commissioned by AirTrunk, AWS, CDC and NEXTDC [Source: https://datacentres.org.au/wp-content/uploads/2025/11/2025-11_DCA-Mandala-Data-Centres-as-Enabling-Infrastructure.pdf ; Source: https://datacentres.org.au/data-centres-as-enabling-infrastructure/]. The framing is that data centres:

- Have invested A$3.1 bn in grid infrastructure since 2020 with another A$7.2 bn forecast by 2030, "including A$1.1 bn of excess capacity for communities and other industries";
- Underwrite renewable PPAs sufficient to power "over 200,000 homes a year";
- Have "around 70 per cent of energy consumption offset by renewables";
- Will invest A$500 m to A$1.1 bn in recycled water infrastructure by 2030.

The DCA framing is **explicitly positive-spillover**: data centres as catalysts for grid and renewables investment. There is no published DCA position paper specifically endorsing demand response or load flexibility commitments. The submission to the NSW Legislative Council inquiry (Submission No 30) reiterates the enabling-infrastructure framing rather than offering specific flexibility commitments [Source: https://www.parliament.nsw.gov.au/lcdocs/submissions/94922/0030%20Data%20Centres%20Australia.pdf]. DCA's response to the federal *expectations* document accepts the demand-flexibility expectation in principle [Source: https://datacentres.org.au/response-to-the-australian-governments-expectations-for-data-centres-and-ai-infrastructure-developers/], but operationalisation is left vague.

### Operator-specific positions

- **AirTrunk** publishes annual sustainability reports; signed the OX2 Riverina solar PPA (~25 MW into Australian grid via OX2) jointly with Google [Source: https://airtrunk.com/google-airtrunk-and-ox2-to-add-renewable-energy-capacity-in-australia/ ; Source: https://airtrunk.com/wp-content/uploads/2024/10/FY24-Sustainability-Report-by-AirTrunk.pdf]. The brief's reference to **"AirTrunk WA Akaysha BESS"** could not be verified — searches for an AirTrunk-Akaysha WA project returned no result. Operating co-located BESS at AirTrunk SYD/MEL campuses is part of the standard cooling/UPS design but is not configured as a grid-export resource.
- **NEXTDC** focuses sustainability messaging on PUE, NABERS 5-star, the M1 solar array (700 t CO2/yr offset) and the "NEXTneutral" carbon-offset add-on rather than on demand flexibility or grid services [Source: https://www.nextdc.com/about-us/environmental-sustainability]. Does not appear in the Energy Charter signatory list as of the December 2025 disclosure.
- **CDC** emphasises Marsden Park's "99% renewable energy by 2030" target and a 27 MW on-site solar component in announcements, with no demand-response commitment [Source: https://cdc.com/resources/news/cdc-data-centres-breaks-ground-on-new-state-of-the-art-data-centre-development-in-marsden-park-industrial-precinct/].
- **Microsoft Australia** signed a 15-year PPA for 100% offtake of FRV's 300 MW Walla Walla Solar Farm (NSW), commissioned October 2025 — its largest Australian renewable PPA [Source: https://www.pv-tech.org/frv-australia-brings-300mw-solar-pv-power-plant-with-microsoft-ppa-to-full-operation/ ; Source: https://reneweconomy.com.au/nsw-solar-farm-to-supply-microsoft-data-centres-now-fully-operational/]. The April 2026 A$25 bn announcement reaffirms 100% renewable matching by 2030 but does not commit to demand response.
- **AWS** announced **9 new Australian PPAs in April 2026 totalling 430 MW** (1 wind: Golden Plains 2 201.8 MW; 3 utility-scale solar+storage; 4 distributed solar+storage; 1 standalone battery) — eight of nine include co-located BESS. This is the most material Australian co-location of BESS by a hyperscaler customer to date [Source: https://www.energy-storage.news/amazon-australia-puts-battery-storage-centre-stage-as-it-inks-nine-ppas-for-data-centre-expansion/].
- **Anthropic** signed a non-binding government MoU on 1 April 2026 (the first under the National AI Plan) committing to renewable energy investment and alignment with the *expectations* — and met separately with NEXTDC, AirTrunk and CDC. A US$4.5 bn Sydney NEXTDC offtake has been reported [Source: https://www.anthropic.com/news/australia-MOU ; Source: https://certifiedstrategic.com/insights/anthropic-australia-mou-data-centre-operators].

### The "data centres can support the grid" argument in the Australian context

The Australian iteration of this argument is being made primarily by **battery vendors and renewable developers**, not by the hyperscalers themselves. Fluence's Jeff Monday (April 2026) is the clearest articulation: BESS allows data centres to "present a predictable, grid-compliant electrical profile", provide power-quality support, accelerate energisation versus waiting for transmission upgrades, and shift roles between load-management and grid participation over time [Source: https://www.energy-storage.news/how-australia-can-turn-the-data-centre-boom-into-a-grid-growth-story/]. This is closer to the US "site-level firming" framing than to actual workload-flexibility demand response.

### What the operators are not saying

There is no Australian operator equivalent of Microsoft's Tyler Norris-style commitment to AI workload time-shifting; no Australian publication of the EPRI DCFlex playbook; no hyperscaler offer of inference-shedding or training-pause grid services. The Property Council and DCA framing is consistently that data centres should be treated as critical infrastructure whose load is **not** materially flexible, with site-level batteries as the firming mechanism. This matches the US Studies Centre's March 2026 read that Australian data centres "operate continuously and cannot easily reduce or interrupt demand without disrupting critical services" [Source: https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid].

---

## 5. AEMO and AEMC engagement

### AEMO

The 2024 ESOO was the first to break out data centres as a discrete category. Central case: ~3 TWh at 2024 → 5 TWh by 2033-34; accelerated growth sensitivity ~10 TWh by 2033-34 (~5% of NEM consumption) [Source: https://wattclarity.com.au/articles/2024/08/29aug-esoo-datacentre/].

The **2025 ESOO** (published August 2025) and the underlying **Oxford Economics Australia data centre demand report** prepared for AEMO (July 2025) are the current authoritative numbers:

- FY25 actual: ~3.9 TWh (98% in NEM), ~2% of NEM-supplied energy.
- Step Change: 25.1% CAGR to 12.0 TWh by FY30, 34.5 TWh by FY50 [Source: https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2024/2025-iasr-scenarios/final-docs/oxford-economics-australia-data-centre-energy-consumption-report.pdf].
- 44 GW of NSP-reported connection requests received against the 6 GW required under Step Change — the explicit "phantom demand" finding.
- AEMO assumes data centres exhibit "relatively stable demand shape" not materially temperature-sensitive; flexibility from cooling load (~40% of total) is acknowledged as a possible mitigant for peak demand, but **is not relied on quantitatively** [Source: https://flowpower.com.au/aemo-2025-esoo-recap/ ; Source: https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2025/2025-electricity-statement-of-opportunities.pdf].

The 2026 ISP IASR (currently in consultation) will use the standalone data centre forecast methodology for the first time [Source: https://www.aemo.com.au/newsroom/news-updates/aemos-updated-forecasting-methodology-targets-rapidly-growing-electricity-loads]. AEMO submitted to the AEMC's package 2 consultation on access standards (June 2025).

### AEMC

The most active AEMC workstream is the **"Improving the NEM access standards — Package 2"** rule change. The draft determination (12 March 2026) responds to three consolidated rule change requests with five proposals [Source: https://www.aemc.gov.au/rule-changes/improving-nem-access-standards-package-2 ; Source: https://wattclarity.com.au/articles/2026/04/05april-aemc-draft-datacentre/ ; Source: https://www.aemc.gov.au/news-centre/media-releases/aemc-modernises-grid-connection-rules-accelerate-energy-transition-manage-ai-boom]:

1. **Raise the large-load threshold from 5 MW to 30 MW** for inverter-based loads on distribution networks, codified in the National Electricity Rules.
2. **Disturbance ride-through** requirements: data centres must remain connected during defined voltage and frequency events and recover within set timeframes.
3. **International alignment** with Texas (PUCT), Ireland (EirGrid) and Finland (Fingrid) standards.
4. **Visibility** for AEMO and NSPs into data centre disturbance response.
5. **Compliance via connection agreements** for non-registered data centres.

The draft was prompted in part by a US incident in which 60 data centres totalling ~1,500 MW disconnected simultaneously during a system disturbance (the July 2024 ERCOT/Houston event). Submissions closed 7 May 2026; final rule expected mid-2026.

The other substantive workstream is the **"Improving consideration of demand-side factors in the ISP"** rule change, which broadens AEMO's ISP demand-side analysis [Source: https://www.aemc.gov.au/rule-changes/improving-consideration-demand-side-factors-isp]. The **Integrating Price-Responsive Resources (IPRR)** rule change, scheduled for May 2027 implementation, will allow CER and flexible loads to participate in energy and FCAS markets through dispatch mode — relevant to any future data centre demand response participation [Source: https://flowpower.com.au/aemo-2025-esoo-recap/].

### Energy Charter and ECMC

The Energy Charter's December 2025 disclosure runs to 70+ Customer Code signatories; **no major data centre operator** appears as a signatory [Source: https://www.theenergycharter.com.au/]. The Energy and Climate Change Ministerial Council has committed to "developing a framework to facilitate demand flexibility" for new data centre loads and "ensuring new firmed generation enters the market as data centre demand increases", and is reviewing cost-recovery arrangements to ensure data centres cover network upgrades [Source: https://cleanenergycouncil.org.au/news-resources/energy-market-reforms-on-the-horizon-from-ministers-final-meeting-for-2025]. The framework itself has not yet been published as of May 2026.

---

## 6. Behind-the-meter batteries and on-site generation

### What Australian operators are doing

The pattern is **on-site UPS/cooling-grade BESS plus utility-scale renewable PPAs** (often co-located with grid-scale BESS off-site), not BTM gas turbines. Specific examples:

- **AirTrunk Mamre Road (proposed):** 7,488 lithium-ion battery cabinets on the SSDA documents, 936 cooling units, 852 diesel back-up generators [Source: https://urbandigest.com.au/ssd-92743706-mamre-road-data-centre-campus/]. The lithium battery cabinets are UPS-grade rather than configured for grid-export firming.
- **Quinbrook Supernode (Brendale, QLD):** the only Australian project where a meaningful grid-scale BESS is **explicitly co-located with a hyperscale data centre site**. 780 MW / 3,074 MWh total, with offtake to Origin (stages 1-2: 520 MW / 1,856 MWh) and Stanwell (stage 3: 250 MW / 1,010 MWh). Stage 1 backfeed-energised September 2025 [Source: https://www.quinbrook.com/news-insights/quinbrook-closes-first-250mw-stage-of-the-supernode-storage-project-at-south-pine-substation-signs-offtake-with-origin-energy/ ; Source: https://www.pv-magazine-australia.com/2024/09/23/quinbrook-picks-ge-vernona-for-1-gwh-supernode-battery-stage/]. The BESS is third-party owned/operated under a tolling model, making it more of a **co-located grid asset** than true BTM firming for the data centre.
- **AWS:** 8 of 9 April 2026 PPAs include co-located BESS at the renewable site (off-site relative to the data centre, on-site relative to the renewables) — the first Australian solar-plus-storage PPAs by AWS and the first outside the US [Source: https://www.energy-storage.news/amazon-australia-puts-battery-storage-centre-stage-as-it-inks-nine-ppas-for-data-centre-expansion/].
- **NEXTDC:** has on-site solar arrays at M1 (Melbourne) and small rooftop installations elsewhere but has not announced site-scale BESS or BTM gas.

### Why no BTM gas

Three structural reasons:

1. **Pipeline gas economics.** Wholesale gas in NSW/VIC has been A$10-18/GJ for most of 2024-25, well above the US Henry Hub equivalent. Cogen and reciprocating-engine LCOE are uncompetitive against grid + PPA, even with current grid congestion [implicit from AEMO gas market reports — not separately cited here].
2. **No stranded gas in load centres.** US BTM gas thrives on Permian flare gas and PJM-area Marcellus tailgate. Australia has no equivalent in the Sydney/Melbourne basins.
3. **Planning culture.** Diesel back-up generation is sanctioned through standard EPA/EIS processes and tightly capped on operating hours; new reciprocating gas would face a much harder approval path. Loudoun-County-style permit creep is unlikely.

The result is that Australian data centres rely on **diesel for back-up only** (and Mamre Road's 852 gensets is the headline number for what that means at scale), and look to **utility-scale BESS** rather than on-site gas for firming.

---

## 7. Government and political context

### Federal — National AI Plan and *Expectations*

The Albanese Government's **National AI Plan** was released 11 December 2025 [Source: https://www.industry.gov.au/news/australia-launches-national-ai-plan-capture-opportunities-share-benefits-and-keep-australians-safe]. The accompanying *Australian Government's expectations of data centres and AI infrastructure developers* sets five expectations [Source: https://www.minister.industry.gov.au/ministers/timayres/media-releases/australian-approach-ai-expectations-data-centres-deliver-australians ; Source: https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-australian-approach-ai-expectations-data-centres-deliver-australians]:

1. Prioritise Australia's national interest;
2. **Support Australia's energy transition** — including underwriting new renewable supply, paying full grid-connection costs, and supporting demand flexibility;
3. Use water sustainably and responsibly;
4. Invest in Australian skills and jobs;
5. Strengthen research, innovation and local capability.

This is an **expectations** framework, not binding rules. Microsoft (April 2026, A$25 bn) and Anthropic (April 2026, MoU) have publicly bound themselves to it. The MoU mechanism is the political enforcement device.

The **Treasury** extended the Clean Building Managed Investment Trust (MIT) withholding tax concession (10% rate) to data centres and warehouses in the 2025-26 Budget, conditional on meeting NABERS energy efficiency standards [Source: https://www.wfw.com/articles/data-centres-an-international-legal-and-regulatory-perspective-spotlight-on-australia/]. This is the principal tax-incentive tool. There is no Virginia-style sales-tax exemption.

The federal government also requires data centre service providers to government to achieve a 5-star NABERS rating [Source: https://www.energycouncil.com.au/analysis/data-centres-and-energy-demand-what-s-needed/].

### State

- **NSW:** Released a Data Centre Strategy consultation paper in March 2026 [Source: https://www.infrastructure.nsw.gov.au/media/qwwpt03m/nsw-data-centre-consultation-paper_wcag.pdf]. The NSW Investment Delivery Authority has received 23 data-centre/technology proposals worth a portion of A$136 bn in declared investment [Source: https://ia.acs.org.au/article/2025/nsw-approves-southern-hemisphere-s-largest-data-centre.html]. The NSW Legislative Council Public Accountability and Works Committee opened an inquiry on 29 January 2026 (Chair: Abigail Boyd / Greens), with submissions closing 27 March 2026, hearings 1, 8 and 22 May 2026, and a report due 30 September 2026 [Source: https://www.parliament.nsw.gov.au/committees/inquiries/Pages/inquiry-details.aspx?pk=3169]. Macquarie Park substation congestion is being addressed through a contingent project (third transformer commissioned Dec 2025; new Wallumatta STS application Oct 2025), with cost-reflective tariffs charged to the four data centre developers seeking connection [Source: https://www.aer.gov.au/system/files/2025-11/Ausgrid%20-%20Contingent%20Project%20Application%20-%20New%20Wallumatta%20STS%20-%2031%20October%202025.pdf]. Individual data-centre parcels are capped at 10 hectares in Macquarie Park and Eastern Creek to preserve industrial-precinct manufacturing land [Source: https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid].
- **Victoria:** No standalone data centre strategy as of May 2026; sector engages through Department of Energy, Environment and Climate Action and the Victorian Planning Authority. SEC's role is on retail and storage rather than data centres.
- **Queensland:** Energy and Jobs Plan 2022/2024 envisages large-load growth but does not specifically address data centres; Quinbrook's Supernode has been the highest-profile QLD project.
- **Western Australia:** The September 2025 WA transmission plan unlocks 2.6 GW of renewables but data centres are a small share of large-load demand at this point; Pilbara edge facilities are mining-customer driven.
- **Tasmania:** Hydropower-anchored hyperscale remains a concept (Firmus 90 MW St Leonards has approval; Viridis 1 MW), no major operator has committed.

### AEMO 2024 ISP and 2026 Draft

- The 2024 ISP did **not** treat data centres as a separate category; they were folded into commercial loads.
- The 2026 ISP IASR (consultation 2025-26) introduces standalone data centre forecasting using the Oxford Economics methodology described above. AEMO's flexibility assumption remains **conservative**: operating-load flexibility is acknowledged but not relied on for system-adequacy purposes.

---

## 8. Australia vs the US — synthesis points

| Dimension | United States (May 2026) | Australia (May 2026) |
|:----------|:-------------------------|:---------------------|
| Operating IT load | ~50 GW (FERC); ~580 hyperscale facilities | ~1.35 GW; ~250 facilities |
| Largest single campus operating | ~1,400 MW (Meta Altoona, multi-building) | ~330 MW (AirTrunk SYD3) |
| Pipeline | Trillions in announced AI capex; 35 GW "energy gap" by 2030 | A$85-135 bn investment to 2035; up to 7.4 GW by 2035 |
| Largest BTM trend | Gas turbines (Stargate Abilene 360 MW; xAI Memphis 35+ turbines) | None equivalent — diesel back-up only |
| Co-located BESS at hyperscale site | Switch Tahoe Reno 179 MW BTM solar; modest | Quinbrook Supernode 780 MW / 3 GWh — stand-out single project |
| Industry voice on grid services | EPRI DCFlex; Microsoft (Tyler Norris); AEP/PJM data centre tariffs | Data Centres Australia (Nov 2025 launch); no operator demand-response commitments |
| Political driver | PJM capacity auction 833% spike; ratepayer-protection PSC actions; bipartisan rate-shift backlash | National AI Plan / *Expectations* — government-led; no voter rate-shift backlash yet |
| Cross-cutting opposition coalition | Republican + Democrat, county-level, 142 activist groups | Industry + ETU + ACF + WWF + Smart Energy Council "must power itself" letter (Feb 2026) |
| Connection standards | FERC + state PUCs + ad-hoc tariffs | AEMC Package 2 draft 30 MW threshold + ride-through (March 2026) |
| Tax / incentive | Virginia-style sales-tax exemptions running A$1.6-3.2 bn/yr | Clean Building MIT extension; NABERS-conditional; small absolute scale |
| Workload time-shifting offer | Microsoft, Google have begun publishing | None |

The **biggest single divergence** is the political economy. In the US, the politics of data centres has crystallised around **residential bills going up because of capacity-auction stress and rate cases**, with cross-cutting Republican-Democrat coalitions at the state PSC level. In Australia the politics has crystallised around **the National AI Plan / energy-transition framing**: data centres should pay their own way and underwrite renewables, but as enabling infrastructure for AI sovereignty rather than as parasites on retail customers. Australian residential bills are rising independently of data centres (state-set network charges, wholesale tightness), and there is no equivalent of the PJM capacity-auction shock pinned on data centres.

Two more secondary divergences worth noting:

- **Australia has comparatively abundant residential VPP and battery resources per capita** (CER deployment is among the highest in the world); the demand-flexibility supply curve is not the binding constraint that it is in PJM. This may explain why data centre flexibility has attracted less policy attention.
- **Australia's planning culture is much less permissive of BTM gas generation** than US states like Texas or Tennessee. The Loudoun-County-style relaxation of emergency-engine running hours that US Virginia DEQ began consulting on in late 2025 has no Australian analogue, and the Mamre Road EIS process will be a critical test.

---

## 9. Caveats, gaps and pitfalls

1. **The "~2 GW operating" headline is not supported by the most recent published data.** CEFC, USSC and Oxford Economics all converge on ~1.3-1.4 GW operating IT load at end-2025. Higher figures appear to confuse operating with announced/committed, or IT load with gross site MW.
2. **Hyperscaler capex announcements are political instruments, not engineering schedules.** Microsoft's A$5 bn → A$25 bn escalation, AWS's A$13.2 bn → A$20 bn escalation, and the NEXTDC/OpenAI A$7 bn MoU are all **non-binding intent**. Operating MW lags by years.
3. **Australian operator positions on demand response are underspecified.** Neither DCA nor any major operator has published a quantitative demand-flexibility commitment. The Mandala report is positive-spillover advocacy, not a flexibility manifesto. ARENA and CSIRO have not published material on data centre demand flexibility comparable to the US EPRI DCFlex programme — this is a real gap.
4. **The Mortlake Macquarie data centre referenced in the brief could not be verified.** Mortlake (VIC) hosts Origin's 566 MW gas plant and a 650 MWh BESS but no announced Macquarie hyperscale data centre. The wording in the brief may conflate Macquarie Asset Management (former AirTrunk owner, now ex), Macquarie Data Centres (separate ASX entity, no Mortlake site), and the Origin Mortlake assets.
5. **The "AirTrunk WA Akaysha BESS" claim could not be verified.** AirTrunk's published Australian PPAs (with Google/OX2 in NSW) and Akaysha's published projects (Waratah NSW, Orana NSW, Brinkworth SA, Wurdong QLD, Elaine VIC) do not overlap in WA based on public sources to May 2026.
6. **The flexibility literature is thin.** Australian academic and consultant work on data centre demand flexibility is materially less developed than US equivalents. The 2024 Climate Council, 2025 CEFC/Baringa, 2025 Mandala/DCA and 2025 Oxford Economics reports are the principal Australian sources; none provides a quantitative flexibility decomposition equivalent to Norris's Duke work.
7. **NSW Legislative Council inquiry is mid-flight.** The inquiry report is due 30 September 2026 and could materially shift the political settlement on cost recovery, rezoning and demand-flexibility expectations.
8. **AEMC final rule on access standards is pending.** The 30 MW threshold and ride-through requirements are draft; final rule expected mid-2026.
9. **Energy Charter participation by data centre operators is absent.** This is a notable gap given DCA's positive-spillover positioning — and may evolve in 2026.

---

## 10. Bibliography

### Tier 1 — Government, regulator, AEMO

- Australian Energy Market Operator, *2025 Electricity Statement of Opportunities* (August 2025). https://www.aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2025/2025-electricity-statement-of-opportunities.pdf
- AEMO, "AEMO's updated forecasting methodology targets rapidly growing electricity loads" (2025). https://www.aemo.com.au/newsroom/news-updates/aemos-updated-forecasting-methodology-targets-rapidly-growing-electricity-loads
- AEMO, *2025-26 Inputs, Assumptions and Scenarios consultation*. https://www.aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp/2026-integrated-system-plan-isp/2025-26-inputs-assumptions-and-scenarios
- Oxford Economics Australia, *Data Centre Energy Demand — Final Report* prepared for AEMO (July 2025). https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2024/2025-iasr-scenarios/final-docs/oxford-economics-australia-data-centre-energy-consumption-report.pdf
- Australian Energy Market Commission, "AEMC modernises grid connection rules to accelerate energy transition, manage AI boom" (March 2026). https://www.aemc.gov.au/news-centre/media-releases/aemc-modernises-grid-connection-rules-accelerate-energy-transition-manage-ai-boom
- AEMC, *Improving the NEM access standards — Package 2: Draft determination* (12 March 2026). https://www.aemc.gov.au/sites/default/files/2026-03/Draft%20determination%20-%20Package%202.pdf
- AEMC, *Improving consideration of demand-side factors in the ISP*. https://www.aemc.gov.au/rule-changes/improving-consideration-demand-side-factors-isp
- Energy Charter, 2025 Disclosure (December 2025). https://www.theenergycharter.com.au/
- Department of Industry, Science and Resources, "Australia launches National AI Plan…" (December 2025). https://www.industry.gov.au/news/australia-launches-national-ai-plan-capture-opportunities-share-benefits-and-keep-australians-safe
- Joint media release, Bowen / Ayres / Charlton, "An Australian approach to AI: Expectations for data centres that deliver for Australians" (December 2025). https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-australian-approach-ai-expectations-data-centres-deliver-australians ; https://www.minister.industry.gov.au/ministers/timayres/media-releases/australian-approach-ai-expectations-data-centres-deliver-australians
- DISR, "Memorandum of understanding between the Australian Government and Anthropic on collaboration on AI opportunities" (April 2026). https://www.industry.gov.au/publications/memorandum-understanding-between-australian-government-and-anthropic-collaboration-ai-opportunities
- Infrastructure NSW, *Data Centre Consultation Paper* (March 2026). https://www.infrastructure.nsw.gov.au/media/qwwpt03m/nsw-data-centre-consultation-paper_wcag.pdf
- NSW Government, "Southern Hemisphere's biggest data centre gets the green light" (28 November 2025). https://www.nsw.gov.au/ministerial-releases/southern-hemispheres-biggest-data-centre-gets-green-light
- NSW Legislative Council Public Accountability and Works Committee, *Inquiry into data centres*. https://www.parliament.nsw.gov.au/committees/inquiries/Pages/inquiry-details.aspx?pk=3169
- AER, *Ausgrid Contingent Project Application — New Wallumatta STS* (31 October 2025). https://www.aer.gov.au/system/files/2025-11/Ausgrid%20-%20Contingent%20Project%20Application%20-%20New%20Wallumatta%20STS%20-%2031%20October%202025.pdf
- Energy Ministers, "Energy and Climate Change Ministerial Council" decisions December 2025, summarised by Clean Energy Council. https://cleanenergycouncil.org.au/news-resources/energy-market-reforms-on-the-horizon-from-ministers-final-meeting-for-2025

### Tier 2 — Industry, advisory, associations

- Clean Energy Finance Corporation / Baringa, *Getting the balance right: Data centre growth and the energy transition* (December 2025). https://www.cefc.com.au/insights/market-reports/data-centre-growth-and-the-energy-transition/ ; full report: https://www.cefc.com.au/media/hs5ner3s/getting-the-balance-right-data-centres-and-the-energy-transition-full-report.pdf ; investment insight: https://www.cefc.com.au/media/4qffpz0x/getting-the-balance-right-data-centres-and-the-energy-transition-investment-insight.pdf ; press release: https://www.cefc.com.au/media/media-release/data-centre-boom-to-reshape-australia-s-energy-future-cefc-baringa-report/
- Mandala Partners for Data Centres Australia, *Data Centres as Enabling Infrastructure* (November 2025). https://datacentres.org.au/wp-content/uploads/2025/11/2025-11_DCA-Mandala-Data-Centres-as-Enabling-Infrastructure.pdf ; landing: https://datacentres.org.au/data-centres-as-enabling-infrastructure/
- Data Centres Australia, "Response to the Australian Government's expectations for data centres and AI infrastructure developers" (December 2025). https://datacentres.org.au/response-to-the-australian-governments-expectations-for-data-centres-and-ai-infrastructure-developers/
- Data Centres Australia, "Introducing Data Centres Australia" (November 2025). https://datacentres.org.au/introducing-data-centres-australia/
- Data Centres Australia, Submission No 30 to NSW Legislative Council Inquiry. https://www.parliament.nsw.gov.au/lcdocs/submissions/94922/0030%20Data%20Centres%20Australia.pdf
- Mandala Partners for AirTrunk, *Empowering Australia's Digital Future* (October 2024). https://mandalapartners.com/uploads/Empowering-Australia%27s-Digital-Future---Report_October-2024.pdf
- Australian Energy Council, "Data Centres and Energy Demand — What's Needed?" (June 2024). https://www.energycouncil.com.au/analysis/data-centres-and-energy-demand-what-s-needed/
- Australian Energy Council, "Data centres: A 24hr power source?". https://www.energycouncil.com.au/analysis/data-centres-a-24hr-power-source/
- Australian Energy Council, "The GHG Protocol: make or break for green data centres?". https://www.energycouncil.com.au/analysis/the-ghg-protocol-make-or-break-for-green-data-centres/
- Climate Council, "Submission: NSW Inquiry into Data Centres" (2026). https://www.climatecouncil.org.au/resources/submission-nsw-inquiry-into-data-centres/
- Climate Council, "Submission: Infrastructure NSW Data Centres Consultation". https://www.climatecouncil.org.au/resources/submission-infrastructure-nsw-data-centres-consultation/
- Climate Council, "Seizing the opportunity to do data centres right". https://www.climatecouncil.org.au/what-does-the-data-centre-boom-mean-for-australias-switch-to-renewables/
- Clean Energy Council (with ETU, ACF, WWF, Smart Energy Council, RE-Alliance, CEF, NCC NSW, EnvVic, QCC, Sunrise Project, Carbon Zero Initiative), "Data centre rush must power itself" joint statement (February 2026). https://cleanenergycouncil.org.au/news-resources/data-centre-rush-must-power-itself-says-industry,-unions-and-environment-groups
- WWF-Australia, joint statement (February 2026). https://wwf.org.au/news/2026/data-centre-rush-must-power-itself-says-industry-unions-and-environment/
- United States Studies Centre, "Powering the cloud: Data centres and the future of Australia's grid" (March 2026). https://www.ussc.edu.au/powering-the-cloud-data-centres-and-the-future-of-australias-grid
- M3 Property, *Specialist Independent Valuation — Data Centre Growth in Australia* (November 2025). https://m3property.com.au/static/88f0d39061ca9072f2bf0a5b61dc5c3f/M3-Property-Report-Data-Centre-Growth-in-Australia-November-25.pdf
- Property Council of Australia, "The Data Centres Outlook: Policy, Power & Opportunity" event series. https://www.propertycouncil.com.au/event/the-data-centres-outlook-policy-power-opportunity
- Energy Consumers Australia, *Request for EOI — Consumer Impacts of Data Centres* (October 2025). https://energyconsumersaustralia.com.au/sites/default/files/2025-10/website-doc-eoi-request-consumer-impacts-data-centres.pdf
- Clayton Utz, "Co-locating batteries with data centres in Australia's National Electricity Market" (April 2025). https://www.claytonutz.com/insights/2025/april/co-locating-batteries-with-data-centres-in-australias-national-electricity-market
- Clayton Utz, "Wide-ranging inquiry into data centres in NSW…" (February 2026). https://www.claytonutz.com/insights/2026/february/wide-ranging-inquiry-into-data-centres-in-nsw-covers-energy-water-needs-and-much-more
- Ashurst, "NSW Legislative Council inquiry into data centres: submissions close 27 March 2026". https://www.ashurst.com/en/insights/nsw-legislative-council-inquiry-into-data-centres-submissions-close-27-march-2026/
- HSF Kramer, "National Expectations for the development of data centres and AI infrastructure" (March 2026). https://www.hsfkramer.com/insights/2026-03/national-expectations-for-the-development-of-data-centres-and-ai-infrastructure-have-been-released-what-you-need-to-know
- Dentons, "Powering Australia's data centre boom: Navigating energy compliance and opportunity" (July 2025). https://www.dentons.com/en/insights/articles/2025/july/3/powering-australias-data-centre-boom
- Watson Farley & Williams, "Data Centres: An International Legal and Regulatory Perspective — Spotlight on Australia". https://www.wfw.com/articles/data-centres-an-international-legal-and-regulatory-perspective-spotlight-on-australia/

### Tier 3 — Trade press, project-level, operators

- Cyber Daily, "Data centre giants launch new Aussie peak body, Data Centres Australia" (November 2025). https://www.cyberdaily.au/security/12953-thinking-machines-data-centre-giants-launch-new-aussie-peak-body-data-centres-australia
- The Tech Capital, "Data Centres Australia names NEXTDC CEO chair of new peak industry body". https://thetechcapital.com/data-centres-australia-names-nextdc-ceo-chair-of-new-peak-industry-body/
- AirTrunk, "Completion of AirTrunk Acquisition by Blackstone…" (Sep 2024). https://airtrunk.com/completion-of-airtrunk-acquisition-by-blackstone-marking-new-era-of-growth/
- AirTrunk, "AirTrunk expands Australian platform with a second hyperscale data centre campus in Melbourne" (December 2025). https://airtrunk.com/airtrunk-expands-australian-platform-with-a-second-hyperscale-data-centre-campus-in-melbourne/
- AirTrunk, "Google, AirTrunk and OX2 to add Renewable Energy Capacity in Australia". https://airtrunk.com/google-airtrunk-and-ox2-to-add-renewable-energy-capacity-in-australia/
- AirTrunk, *FY24 Sustainability Report*. https://airtrunk.com/wp-content/uploads/2024/10/FY24-Sustainability-Report-by-AirTrunk.pdf
- NEXTDC, ASX release "Contracted Utilisation and Capex Guidance Update" (1 December 2025). https://announcements.asx.com.au/asxpdf/20251201/pdf/06sr3ff6f4q4vv.pdf
- NEXTDC, "Building the next generation of sovereign AI infrastructure in Australia" (December 2025). https://www.nextdc.com/news/building-the-next-generation-of-sovereign-ai-infrastructure-in-australia
- The Urban Developer, "NEXTDC plans $7bn AI campus at Western Sydney site". https://www.theurbandeveloper.com/articles/eastern-creek-data-centre-550mw-openai-nextdc
- CDC Data Centres, "CDC Data Centres breaks ground on new state-of-the-art data centre development in Marsden Park industrial precinct". https://cdc.com/resources/news/cdc-data-centres-breaks-ground-on-new-state-of-the-art-data-centre-development-in-marsden-park-industrial-precinct/
- CDC, "CDC welcomes the launch of Data Centres Australia". https://cdc.com/resources/news/cdc-welcomes-the-launch-of-data-centres-australia-leading-the-way-in-digital-infrastructure/
- Microsoft Australia News Centre, "Microsoft deepens commitment to Australia with A$25 billion investment in AI infrastructure, security, and skills" (April 2026). https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/
- Microsoft Australia News Centre, "Microsoft and FRV Australia team up to add renewable energy to the grid". https://news.microsoft.com/en-au/features/microsoft-and-frv-australia-team-up-to-add-renewable-energy-to-the-grid/
- About Amazon, "Amazon will invest AU$20 billion in data center infrastructure in Australia" (2025). https://www.aboutamazon.com/news/aws/amazon-data-center-investment-in-australia
- Energy-Storage.News, "Amazon Australia puts battery storage centre stage as it inks nine PPAs for data centre expansion" (April 2026). https://www.energy-storage.news/amazon-australia-puts-battery-storage-centre-stage-as-it-inks-nine-ppas-for-data-centre-expansion/
- Energy-Storage.News, "How Australia can turn the data centre boom into a grid growth story" (Fluence/Jeff Monday, 2026). https://www.energy-storage.news/how-australia-can-turn-the-data-centre-boom-into-a-grid-growth-story/
- Quinbrook, "Quinbrook closes first 250MW stage of the Supernode storage project at South Pine substation, signs offtake with Origin Energy". https://www.quinbrook.com/news-insights/quinbrook-closes-first-250mw-stage-of-the-supernode-storage-project-at-south-pine-substation-signs-offtake-with-origin-energy/
- Quinbrook, "Supernode battery completes construction of first stage". https://www.quinbrook.com/news-insights/quinbrooks-supernode-battery-completes-construction/
- Data Center Dynamics, "Quinbrook to build $1.7 billion data center, 2GWh battery storage in Queensland". https://www.datacenterdynamics.com/en/news/quinbrook-to-build-17-billion-data-center-2gwh-battery-storage-in-queensland-australia/
- Data Center Dynamics, "Australian energy market operator creates standalone forecast category for data centers". https://www.datacenterdynamics.com/en/news/australian-energy-market-operator-creates-standalone-forecast-category-for-data-centers/
- Data Center Dynamics, "AirTrunk set to buy planned 1GW data center site in Western Sydney". https://www.datacenterdynamics.com/en/news/airtrunk-set-to-buy-planned-1gw-data-center-site-in-western-sydney-australia/
- Information Age (ACS), "Concern over Australia's most power-hungry data centre" (2026). https://ia.acs.org.au/article/2026/concern-over-australia-s-most-power-hungry-data-centre.html
- Information Age, "NSW approves southern hemisphere's largest data centre" (Nov 2025). https://ia.acs.org.au/article/2025/nsw-approves-southern-hemisphere-s-largest-data-centre.html
- Information Age, "OpenAI, NextDC ink $7b Australian data centre deal" (Dec 2025). https://ia.acs.org.au/article/2025/openai--nextdc-ink--7b-australian-data-centre-deal.html
- Information Age, "Microsoft to invest $25b in Australia by 2029" (April 2026). https://ia.acs.org.au/article/2026/microsoft-to-invest-25b-in-australia-by-2029.html
- Renew Economy, "NSW solar farm to supply Microsoft data centres now fully operational" (October 2025). https://reneweconomy.com.au/nsw-solar-farm-to-supply-microsoft-data-centres-now-fully-operational/
- Renew Economy, "Quinbrook seals record finance deal to build huge Supernode data centre battery". https://reneweconomy.com.au/quinbrook-seals-record-finance-deal-to-build-huge-supernode-data-centre-battery/
- pv magazine Australia, "Quinbrook closes first stage of 2 GWh Supernode battery project". https://www.pv-magazine-australia.com/2024/04/12/quinbrook-closes-first-stage-of-2-gwh-supernode-battery-project/
- pv magazine Australia, "Akaysha progresses plans for 1.6 GWh battery in Queensland". https://www.pv-magazine-australia.com/2024/07/18/akaysha-progresses-plans-for-1-6-gwh-battery-in-queensland/
- PV-Tech, "FRV Australia brings 300MW solar PV power plant with Microsoft PPA to full operation" (October 2025). https://www.pv-tech.org/frv-australia-brings-300mw-solar-pv-power-plant-with-microsoft-ppa-to-full-operation/
- PV-Tech, "Australia industry demands data centres fund own clean power" (February 2026). https://www.pv-tech.org/social-backlash-inevitable-industry-demands-data-centres-stop-freeloading-on-australias-clean-energy/
- WattClarity, "What's the 2024 ESOO say about Data Centres?" (29 August 2024). https://wattclarity.com.au/articles/2024/08/29aug-esoo-datacentre/
- WattClarity, "AEMC proposed new grid standards for Data Centre connections" (5 April 2026). https://wattclarity.com.au/articles/2026/04/05april-aemc-draft-datacentre/
- Anthropic, "Australian government and Anthropic sign MOU for AI safety and research". https://www.anthropic.com/news/australia-MOU
- CertifiedStrategic, "Anthropic Australia MOU and the data centre operators". https://certifiedstrategic.com/insights/anthropic-australia-mou-data-centre-operators
- Urban Digest, "$9B Hyperscale Data Centre Campus Proposed for Kemps Creek" (Mamre Road SSDA detail). https://urbandigest.com.au/ssd-92743706-mamre-road-data-centre-campus/
- Flow Power, "AEMO's 2025 ESOO recap". https://flowpower.com.au/aemo-2025-esoo-recap/
- ARN, "Federal government sets AI and data centre standards" (December 2025). https://www.arnnet.com.au/article/4148382/federal-government-sets-ai-and-data-centre-standards.html
- The Energy, "Shielding energy consumers from data centre whiplash". https://theenergy.co/article/shielding-mums-and-dads-from-data-centre-whiplash
- The Energy, "AEMO doubles data centre demand forecast". https://theenergy.co/article/aemo-doubles-data-centre-demand-forecast
- BeBeez International, "AirTrunk set to buy planned 1GW data centre site in Western Sydney" (November 2025). https://bebeez.eu/2025/11/11/airtrunk-set-to-buy-planned-1gw-data-center-site-in-western-sydney-australia/

---

*End of research note. The Mamre Road SSDA EIS, the AEMC Package 2 final rule, and the NSW Legislative Council inquiry report (due 30 September 2026) should be obtained directly for any figures or positions intended for publication, since secondary summaries differ in detail. Two specific brief items — the Mortlake Macquarie data centre and the AirTrunk WA Akaysha BESS — could not be verified against public sources to May 2026 and are flagged as such.*
