---
title: "Incumbent data centre backup generator market: a briefing for would-be entrants"
author: "David Leitch"
date: 2026-05-13
draft: true
categories: ["Demand", "Generation"]
lightbox: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

## Why this note

The AI capex cycle has dragged diesel reciprocating gensets — a sleepy, oligopolised corner of heavy industrial equipment — into a structural growth story. Caterpillar's Power & Energy "sales to users" grew 37% in 2025, with power generation alone up 44% and exceeding \$10 billion in revenue [@cat-q4-2025]. Cummins Power Systems, the segment that houses standby gensets, posted full-year 2025 revenue of \$7.5 billion (+16%) at an EBITDA margin of 22.7% (+430 bp); the Q1 2026 margin print was 29.5% [@cummins-q4-2025; @cummins-q1-2026]. Rolls-Royce mtu's power generation orders into data centres grew almost 50% in 2024 and the Mankato, Minnesota plant is being more than doubled in output [@rr-mankato-2025].

The combination of (a) supply-constrained incumbents earning Power-Systems-segment EBITDA margins approaching 30%, (b) lead times that have stretched well into 2028, and (c) a customer base that is desperate, well-capitalised and willing to pre-pay, naturally invites the question of entry. This note maps the incumbents, their product, their geography, their lead times, indicative pricing and where new entrants might or might not have a chance.

A reminder on units. "kVA" is apparent power. "kW" is real power. At the data centre power factor assumption of 0.8, 1,000 kVA = 800 kW. Throughout, where an OEM quotes kVA, I have converted to kW. All generator ratings here are ISO 8528-1 ESP (Emergency Standby Power) unless flagged otherwise. ESP allows variable load up to 70% average load factor over 200 hr/yr; PRP (Prime) sits ~10% lower in continuous output; data centre operators frequently buy ESP and rely on EPA emergency-engine exemptions that keep them out of Tier 4 Final aftertreatment [@cummins-iso-8528; @epa-tier4-guide].

## The product landscape: who sells what to data centres at 1 MW+

The market above 2 MW has effectively three serious vendors — Caterpillar, Cummins, Rolls-Royce mtu — plus Kohler/Rehlko at the upper end of the second tier, Mitsubishi (MHI) and Generac as price-positioned alternatives, and a long tail (FG Wilson/Perkins, Doosan, Hyundai Power Systems, Volvo Penta, John Deere) that essentially does not play above 2 MW for hyperscale standby. Wärtsilä occupies a different box — large gas reciprocating engines sold as prime power, not standby — and is included for context.

**Table 1. Data centre standby genset model lineup at 1 MW+**

| Supplier | Lead model(s) | Engine family | Standby kW (60 Hz) | Standby kW (50 Hz) | Notes |
|:---------|:---------------|:--------------|-------------------:|-------------------:|:------|
| Caterpillar | 3516E | 78-litre V16 | 2,500–3,000 | 2,500–2,750 | Workhorse; >50% of new US DC builds. |
| Caterpillar | C175-16 | 85-litre V16 quad-turbo | 2,500–3,100 | 2,200–2,800 | Higher power density, newer architecture. |
| Caterpillar | C175-20 | 106-litre V20 | up to 3,500 | up to 3,250 | Top of the diesel range. |
| Cummins | QSK60 | 60-litre V16 | 1,500–2,000 | 1,400–1,825 | Mid-DC workhorse. |
| Cummins | QSK78 | 78-litre V18 | 2,500 | 2,500 | Direct 3516E competitor. |
| Cummins | QSK95 / C3500 D6e | 95-litre V16 | 2,750–3,500 | 2,500–3,250 | "Centum" series; capacity doubled in 2025. |
| Cummins | S17 (new) | 17-litre V8 | up to 1,000 | ~900 | Launched 2025; clean-sheet small-footprint unit. |
| Rolls-Royce mtu | 16V/20V 4000 DS series | 76/95-litre | 2,250–3,250 | 2,000–3,200 | Series 4000 is the DC mainstay; 20V4000 DS4000 hits 3,200 kW / 4,000 kVA. |
| Kohler / Rehlko | KD3000, KD3500, KD4000 | 78-95-litre | 2,800, 3,500, 4,000 | comparable | Engines sourced from Liebherr / Rolls-Royce / MTU collaboration. |
| Generac | SDMD2250–SDMD3250 | 65/87.5-litre Baudouin | 2,250–3,250 | 2,000–3,000 | Launched April 2025; Baudouin M55 engine. |
| Mitsubishi MHI | MGS-R series | 50-60-litre S12/S16/S20 | up to 2,000 | up to 2,750 (kVA basis ~2,200 kW) | Built in Singapore; strong in APAC. |
| FG Wilson / Perkins | P-series | Perkins 4006/4012 | up to ~1,650 | up to ~1,500 | Sub-2 MW; not a serious DC hyperscale supplier. |
| HD Hyundai Infracore (ex-Doosan) | DP/DX | Up to 30-litre | ~625–900 | ~600–870 | Edge/enterprise; not above 1 MW for DC standby. |

*Source: OEM technical datasheets — Caterpillar [@cat-c175-spec; @cat-3516e-spec], Cummins [@cummins-qsk95; @cummins-qsk60-pc3; @cummins-s17], Rolls-Royce mtu [@mtu-4000-spec; @mtu-20v4000-spec], Kohler/Rehlko [@kohler-kd3500], Generac [@generac-sdmd3250], MHI [@mhi-mgs-r]. Where the OEM only publishes kVA, kW is at PF = 0.8.*

A point Australian readers usually miss: published 50 Hz ratings are typically lower than 60 Hz ratings for the same engine. This is largely a function of running speed (1,500 vs 1,800 rpm) and the resulting thermal limits. For a given engine family, expect roughly 10-15% less output at 50 Hz. That is one reason Australian sites with the same nameplate MW capacity tend to need ~10% more units than US equivalents.

## Market share: roughly knowable, never precise

There is no public source that surveys actual data centre genset deliveries by brand. Market-research firms (Mordor, Arizton, Fortune Business Insights, Research and Markets) publish numbers, but the methodology is opaque and the ranges differ enough that they should be treated as directional rather than authoritative. Frost & Sullivan figures show Caterpillar with the largest data-centre standby share, Cummins second, Rolls-Royce mtu third — with one widely-cited but un-sourced trade-press claim of 42% / 24% / 21% [@mordor-dc-gen]. I would not bet on those specific decimals; the directional ranking is reliable.

**Table 2. Indicative incumbent share of global data-centre standby genset shipments (>1 MW)**

| Supplier | Indicative share | Geographic strength | Channel structure |
|:---------|----------------:|:--------------------|:------------------|
| Caterpillar | 35-45% | US (dominant), AU/NZ, ME, India | Dealer (WesTrac/EPSA, Foley, Boyd, Toromont) |
| Cummins | 20-30% | US, India, China, UK | Mixed direct + dealer |
| Rolls-Royce mtu | 15-25% | Germany, EU, growing US, AU via Penske | Distributor (AVK in EU, Penske in AU) |
| Kohler / Rehlko | 5-10% | US, EU | Distributor + direct |
| Generac | 2-5% | US sub-1 MW; growing in 2-3 MW | Direct + dealer |
| MHI (Mitsubishi) | 2-5% | Japan, SE Asia, ME | Direct |
| Others (FG Wilson, Doosan, INNIO, HITEC) | residual | Sub-1 MW or niche flywheel | Various |

*Source: Triangulated from Mordor Intelligence [@mordor-dc-gen], Research and Markets / ABI Research [@rm-2025-2030], and OEM-reported segment revenues. Treat as directional.*

The combined share of the top five is consistently estimated at 60-75% globally; the rest is fragmented among regional packagers (FG Wilson, Himoinsa, Pramac, INNIO/Jenbacher in gas) and aftermarket repackagers (AVK, ClarkePower, Curtis Power, Pacific Power Group).

A useful frame is that there is one tier of supplier that builds the engine and packages the genset (Caterpillar, Cummins, Rolls-Royce mtu, MHI, increasingly Generac via Baudouin), and another tier that buys engines and packages them (FG Wilson with Perkins, AVK with mtu, Himoinsa with various). The packaged sub-segment has lower margins, less product differentiation and is the channel through which Chinese and Indian volume could plausibly attack the market.

## Emissions: Tier 4 Final is barely a constraint

For data-centre backup specifically, EPA's "emergency engine" provisions under 40 CFR Part 60 Subpart IIII allow Tier 2 engines to be installed and operated under the 100-hours-per-year non-emergency cap, plus unlimited emergency hours [@epa-tier4-guide; @kirkland-epa-2025]. Almost every US data-centre standby unit is therefore Tier 2 or Tier 3, not Tier 4 Final. The cost premium to install Tier 4 Final (selective catalytic reduction, diesel particulate filter, urea/DEF dosing, additional 1-3 m of exhaust train, higher fuel burn) is meaningful — industry estimates put the kit alone at 15-25% of genset cost — but for the moment is mostly avoided.

The exceptions are non-attainment zones (notably parts of California, the New York/New Jersey corridor, Northern Virginia after recent local rule changes) and any unit that participates in grid demand-response. EPA guidance issued in May 2025 clarified that emergency-use generators may dispatch to support local grid stress without losing their emergency status, provided certain conditions are met; this materially eases the regulatory worry that hyperscalers' "behind-the-meter" arrangements might trigger Tier 4 obligations [@sidley-epa-2025; @kirkland-epa-2025].

European Stage V is stricter: in practice all new gensets sold for permanent installation in the EU now require SCR + DPF aftertreatment. This has lifted European data-centre genset prices roughly 10-15% above US equivalents and has lengthened design cycles for OEMs. Rolls-Royce mtu, with its German engineering base, is relatively well-positioned; Caterpillar and Cummins have invested heavily but their Stage V product mix is narrower than the US Tier 2 mix.

Note also: HVO (hydrogenated vegetable oil) is increasingly specified by hyperscalers as a "drop-in" diesel substitute. All major OEMs — Caterpillar, Cummins, mtu, Kohler, Generac — now warranty HVO operation on most current engines [@rr-mankato-2025; @cummins-s17].

## Lead times: 18-30 months and not easing materially

The single most telling fact about this market in 2026 is that order books extend into 2028. Cummins CEO Jennifer Rumsey said on the Q4 2025 call that "we're taking orders now well into 2028; the demand remains very strong for diesel backup power" [@cummins-q4-2025]. Caterpillar's reported order backlog hit \$51 billion at year-end 2025 (+71% YoY) and \$63 billion at Q1 2026 (+79% YoY); Power & Energy is the segment most exposed [@cat-q4-2025; @cat-backlog-q1-2026].

**Table 3. Data centre genset lead times — 2 MW class units**

| Period | Typical lead time | Comment |
|:-------|:------------------|:--------|
| Pre-2022 | 10-14 months | Stable; competitive bidding common. |
| 2023 | 14-18 months | First AI orders begin lengthening queues. |
| Q4 2024 | 18-22 months | Hyperscalers buying multi-year forward. |
| Q4 2025 | 22-30 months | Cummins QSK95 specifically cited at 18 months pre-expansion. |
| Q1-Q2 2026 | 24-30 months | Generac quotes 50-60 weeks (12-14 months) for its new lineup — a deliberate market-entry play. |

*Source: OEM earnings transcripts [@cummins-q4-2025; @cat-q4-2025], Mordor Intelligence [@mordor-dc-gen], Generac press release [@generac-dc-launch].*

Capacity expansions announced 2024-2026:

- **Caterpillar:** \$725 million expansion of the Lafayette, Indiana large-engine plant (the 3500/C175 line) — the largest single capex commitment at the site since 1982. \$3.5 billion total capex planned for 2026, up 25% YoY [@cat-q4-2025; @cat-axios-2026].
- **Cummins:** doubled 95-litre engine output in 2025; \$150 million further expansion of the Fridley, Minnesota high-horsepower plant announced February 2026, lifting QSK95 capacity an additional 30%; full Centum S17 product family launched [@cummins-q4-2025; @cummins-s17].
- **Rolls-Royce mtu:** \$24 million investment in Mankato, Minnesota will lift production of Series 4000 generators by more than 120% by end-2026 versus 2024 base [@rr-mankato-2025; @rr-dcd-mankato].
- **Kohler/Rehlko:** carved out of Kohler in May 2024, now Platinum Equity-controlled; KD-series being scaled but no explicit MW-of-capacity disclosure [@rehlko-platinum].
- **Generac:** new SDMD2250-SDMD3250 product family launched April 2025; differentiated on lead time (50-60 weeks) more than performance [@generac-dc-launch].

The thing to notice is that even with all of this capex, supply does not catch demand inside the planning horizon. Caterpillar's 125% capacity expansion over two years (per company commentary [@cat-axios-2026]) does not close the gap because order intake has more than doubled. New entrants making a credible 2027-2028 delivery offer would find buyers — the question is whether they can be credible.

## Pricing: \$1,000/kW for the box, \$1,500-2,500/kW installed

The numbers below are indicative. Real pricing varies with enclosure (sub-arctic vs tropical), sound attenuation (Singapore 65 dBA boundary limit drives \$50-200k of acoustic kit per unit), fuel system (sub-base tank vs day-tank-plus-bulk), switchgear voltage (480 V vs 13.8 kV medium-voltage) and aftermarket bundling.

**Table 4. Indicative installed cost — 3 MW data-centre standby genset, US/AU**

| Cost component | \$/kW | Comment |
|:---------------|------:|:--------|
| Bare genset (engine + alternator + radiator + base controls) | 350–450 | Mid-volume hyperscale pricing 2022–2023. |
| Bare genset, 2026 spot | 550–700 | Post-AI demand surge; Caterpillar and Cummins lead. |
| Sound-attenuated weatherproof enclosure | 80–150 | Higher in Singapore/HK due to 65 dBA limit. |
| Day tank + sub-base belly tank (24-72 hr) | 60–100 | Excludes bulk farm and pipework. |
| Critical-grade exhaust + silencer + flex | 40–70 | Tier 2; Tier 4 Final would add 100-150. |
| Switchgear, paralleling, ATS, MV interface | 200–350 | Highly site-dependent. |
| Installation labour, foundation, integration | 150–300 | US union markets at top end. |
| Commissioning, load-bank acceptance test, freight | 60–120 | |
| **Total installed, Tier 2 emergency standby** | **~1,500–2,200** | A 3 MW unit lands at ~\$4.5–6.5 million installed. |
| Add for Tier 4 Final (SCR/DPF/DEF) | +200–350 | Where required (CA, parts of NY/NJ, EU Stage V). |
| Add for medium-voltage paralleling switchgear | +100–250 | Hyperscale 13.8/22 kV bus designs. |

*Source: Cummins technical brief "Diesel Generators in the Data Center" [@cummins-dc-bigger]; vendor pricing benchmarks reported by Latitude Media [@latitude-diesel-boom]; analyst commentary triangulated against EIA construction-cost data [@eia-gen-cost]. Treat the 2026 spot as a ±20% range; OEMs do not publish.*

Direction of travel since 2022: roughly +30-40% on the bare genset, more like +50% on enclosed and switchgear-integrated packages. Drivers: copper (alternator windings), electronics (engine controls, paralleling), specialist labour, and pure pricing power — incumbents are not visibly discounting.

For a sense of scale: a 100 MW data-centre campus typically installs 30-40 generators of 2.5-3 MW each (N+1 or 2N redundancy), so genset capex is in the order of \$150-250 million of a total \$1-1.5 billion build [@bluecap-dc; @kio-dc-costs]. The OEMs are capturing perhaps 10-20% of total facility capex.

## Aftermarket: where the real moat sits

The aftermarket — service contracts, parts, fuel polishing, load-bank testing, overhaul — is the structural moat. Industry surveys put aftermarket gross margins at 35-45% versus 15-25% on the box. Caterpillar's dealer network captures the bulk of this through multi-decade service agreements bundled at point of sale. The mechanism is that customers signing 20-year DC standby fleet agreements lock in OEM parts, OEM-trained technicians, and OEM-certified fuel testing, with switching costs that approach the residual value of the genset itself.

Service requirements for data-centre standby gensets typically include [@generator-source-maint; @csd-dc-maint]:

- Quarterly inspection (visual, fluid, controls)
- Semi-annual oil and filter change (even on low hours)
- Annual load-bank test at 100% rated load for 2-4 hours (NFPA 110 and many local codes are explicit on this)
- Annual fuel testing and triennial fuel polishing (diesel degrades from ~6 months; polishing extends usable life to 5+ years)
- 10-year major overhaul (depending on starts and run hours)

A typical service contract for a 3 MW unit runs \$25,000-50,000/yr for parts and labour, \$5,000-15,000/yr for fuel testing and polishing, plus load-bank costs (\$5,000-10,000 per event). Across a hyperscale fleet of 30-40 units that is \$1-2 million/yr in recurring revenue per site, almost all of which flows through the original OEM's authorised channel.

Caterpillar's competitive edge here is not the engine — it is the dealer footprint, which is larger by a factor of 3-5x versus Cummins or mtu in most regions. WesTrac/EPSA in Australia, Foley Industries in the US Northeast, Boyd Cat in the US Mid-Atlantic, Toromont in eastern Canada — these are billion-dollar businesses whose service technicians are within a 4-hour drive of essentially every Caterpillar standby genset they have ever sold. Cummins relies more on direct service plus a smaller distributor footprint. Rolls-Royce mtu is competitive in Germany and parts of the EU but materially thinner everywhere else; Penske in Australia is its strongest non-European territory.

A new entrant could plausibly compete on the box. Competing on the 20-year service relationship is the harder problem.

## Recent corporate activity worth flagging

- **Caterpillar / American Intelligence & Power alliance (March 2026):** 2 GW of dedicated AI infrastructure committed via a strategic alliance with Caterpillar and Boyd CAT, with engines for a West Virginia campus tied to Microsoft and NVIDIA-class workloads [@cat-aip-alliance; @power-eng-wv].
- **Caterpillar / Weichai Baudouin distribution (Nov 2025):** \$85 million acquisition of Weichai's European distribution network for Baudouin engines — odd because Baudouin is the engine Generac is using in the new SDMD product. Reads as a defensive move against Baudouin volume in Europe.
- **Cummins S17 launch (Sep 2025):** clean-sheet 17-litre platform delivering 1,000 kW from a notably small footprint. Targeted at urban edge sites where the 95-litre is physically too large. Not a direct hyperscale play but expands Cummins' addressable market downward into the 1 MW segment that had been Kohler/Generac territory [@cummins-s17].
- **Kohler → Rehlko separation (May 2024 → Sept 2024 rebrand):** Platinum Equity took majority control of the former Kohler Energy business, which then rebranded as Rehlko. Now operating Power Systems (KD-series), Kohler UPS, Clarke Energy (gas engines), Heila Technologies (microgrid controls) and Curtis Instruments as a more focused energy platform [@rehlko-platinum; @rehlko-dcd]. Private-equity ownership likely means more aggressive pricing and faster product cycles.
- **Generac DC entry (April 2025):** Generac was a sub-2 MW player. The SDMD2250-SDMD3250 lineup with Baudouin M55 engines and a 50-60 week quoted lead time is a clear shot at the underserved segment of buyers who can't wait for Caterpillar [@generac-dc-launch].
- **Rolls-Royce mtu Mankato (March 2025):** \$24 million spend to lift US Series 4000 output more than 120%; aimed squarely at the US data-centre opportunity it cannot serve from Friedrichshafen [@rr-mankato-2025].
- **Wärtsilä gas reciprocating prime-power orders (2025):** 507 MW (27 × Wärtsilä 50SG) for a US data-centre developer in November 2025; 429 MW separately reported earlier in the year. Wärtsilä is selling not standby but on-site prime power as a workaround for grid connection lead times. This is a different product than diesel standby but is increasingly a substitute purchase for hyperscalers who cannot get a grid connection [@wartsila-507mw; @wartsila-429mw].

New entrants to watch but not yet credible at 1 MW+:

- **Chinese OEMs (Weichai Baudouin, Yuchai, Wuxi Power):** real engineering capability at the engine level, but no Western data-centre certification track record, weak global service. The Generac/Baudouin partnership is the most credible Western channel to a Chinese engine to date.
- **Indian (Mahindra, Kirloskar):** sub-1 MW competence, expanding upward, structurally challenged in the largest markets.
- **HD Hyundai Infracore (formerly Doosan):** Korean, technically credible, has not yet committed serious capital to 2 MW+ DC standby.
- **PowerSecure (a Southern Company subsidiary):** packagers and developers, not engine OEM. Compete on integration and microgrid services rather than the box.

## Australian market specifics

The Australian data-centre market has a structure that mirrors the global incumbent oligopoly with two clear local twists. First, the Caterpillar dealer network — WesTrac in WA/NSW/ACT and Energy Power Systems Australia (EPSA) elsewhere — is unusually strong, a function of the long-standing mining customer base which created technician depth and parts inventory. Second, Penske Power Systems holds the exclusive distributorship for Rolls-Royce mtu, and has used that to become the dominant supplier to NEXTDC.

**Table 5. Australian data-centre operator generator alignment (publicly disclosed)**

| Operator | Lead genset supplier | Channel | Evidence |
|:---------|:---------------------|:--------|:---------|
| NEXTDC | Rolls-Royce mtu (20V4000 series) | Penske Power Systems | Penske publicly disclosed 40+ units shipped to NEXTDC sites, with M3 Melbourne taking 3× 20V4000 at ~3 MW each [@penske-mtu]. NEXTDC M3 alone is 150 MW critical load. |
| AirTrunk | Mixed, leaning mtu | Penske + others | Penske discloses AirTrunk as a customer; specific mix not public. Now Blackstone-owned post the A\$24 billion acquisition (Sept 2024). |
| CDC | Predominantly Caterpillar | WesTrac/EPSA | Public-domain commentary suggests Cat-aligned, particularly for Canberra defence-grade sites; no comprehensive disclosure. |
| Equinix | Mixed Caterpillar / Cummins / mtu | Multi-vendor by design | Equinix specifies multiple OEMs globally for supply resilience. |
| Macquarie Data Centres | Caterpillar (historic), unconfirmed for IC3 East | WesTrac/EPSA | Defence-aligned Canberra/Sydney workloads; specific brand for IC3 East not in the public domain. |
| DCI Data Centers | Caterpillar (Sydney, Adelaide) | WesTrac/EPSA | Publicly visible Cat-branded enclosures at Sydney sites. |
| Global Switch | Cummins (Sydney) | Cummins direct | Long-standing Cummins reference; Cummins case study material on the Sydney West site has referenced their installation. |

*Source: Penske Power Systems disclosures [@penske-mtu], NEXTDC public M3 commissioning video [@nextdc-m3-video], operator project announcements, and Cummins reference customer materials [@cummins-digital-realty]. Where the genset brand is not publicly disclosed, this table flags rather than guesses.*

Pricing for Australian-installed Tier 2 standby gensets sits at the upper end of the global range — typically \$2,000-2,500/kW installed for a 3 MW class unit, a function of higher transport, lower local fabrication content, and the cost of Australian compliance (acoustic and bushfire-zone considerations in Sydney and Melbourne; cyclone ratings in Brisbane and the Pilbara industrial market). Lead times reported by Penske and EPSA in 2026 are broadly consistent with the US figures: 22-30 months for new orders into 2028 windows.

The structural point about the Australian market is that it is a price-taker on equipment but a meaningful service-revenue market. Penske and WesTrac/EPSA each operate \$100m+ annual service businesses tied directly to the data-centre standby installed base. A new entrant in Australia faces not only the Caterpillar dealer moat but also the practical reality that Penske is the only credible mtu service alternative, and Cummins direct is a smaller team than its global parent suggests.

## What this means for an entrant

The market today rewards capacity. Incumbents are not under price pressure. Aftermarket margins are protected by long-tail dealer networks. Lead times are quoted on a multi-year basis and customers are pre-paying.

That said, the structural risk to the incumbents over a 5-7 year horizon is concentrated. Three things would need to be true for a new entrant to make material inroads:

1. **A credible engine.** Either licensed from a tier-1 OEM (the Generac/Baudouin route), or imported from a Chinese/Korean OEM that has accumulated DC standby references. The engine is necessary but not sufficient.
2. **A service network.** The hard part. Either acquire an existing independent service business (US: there are perhaps 15-20 of these of meaningful scale), or build through a captive subsidiary as Rolls-Royce mtu effectively did through AVK in Europe.
3. **A first hyperscale anchor.** All majors will sole-source from established OEMs unless there is a specific demand-shock event. The Wärtsilä prime-power example shows that a niche product can break in if it solves an acute customer pain (grid connection delay).

A more realistic entry is not as an OEM but as a capacity arbitrageur — buying genset capacity from a tier-2 OEM (Baudouin, Yuchai, HD Hyundai) and packaging it with switchgear, controls and service for hyperscalers willing to take 6-12 months of lead time off the incumbent quote. Generac's SDMD strategy is exactly this. The mtu/AVK channel is exactly this. The margin in the box is unspectacular; the margin in the service relationship is the whole game.

## Open questions where this synthesis is weakest

- Precise market shares — public sources differ by 5-15 percentage points per OEM and none discloses underlying methodology.
- Tier 4 Final cost premium as a percentage of box price — I have triangulated from sub-component costs rather than from OEM disclosure; the 15-25% range should be taken as indicative.
- Australian operator brand alignment for AirTrunk, CDC and Macquarie — partial public disclosure only; the table flags where the data is uncertain.
- Aftermarket margins — drawn from heavy-equipment industry analogues rather than DC-specific disclosure; segment reporting is too coarse to isolate DC standby service revenue from broader power systems aftermarket.
- 2026 spot pricing per kW — OEMs do not publish; the \$550-700/kW bare-genset range is based on RFP-level chatter reported in trade press and analyst notes rather than verifiable transactions.

---

## References

1. [Caterpillar Inc., Q4 and Full-Year 2025 Results, press release](https://www.caterpillar.com/en/news/corporate-press-releases/h/4q25-results-caterpillar-inc.html)
2. [Caterpillar Inc., Q1 2026 backlog and capex commentary, investor materials](https://investors.caterpillar.com/news/news-details/2026/Caterpillar-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
3. [Caterpillar Inc., American Intelligence & Power 2 GW Alliance press release](https://investors.caterpillar.com/news/news-details/2026/American-Intelligence--Power-Forms-Strategic-Alliance-with-Caterpillar-and-Boyd-CAT-to-Deploy-2-Gigawatts-of-Dedicated-Power-for-Hyperscale-AI-Infrastructure/default.aspx)
4. [Caterpillar C175-16 spec sheet, 60 Hz](https://www.cat.com/en_US/products/new/power-systems/electric-power/diesel-generator-sets/1000028916.html)
5. [Caterpillar 3516E spec sheet, 60 Hz](https://www.cat.com/en_US/products/new/power-systems/electric-power/diesel-generator-sets/1000033111.html)
6. [Caterpillar, EPA Tier 4 and the Electric Power Industry white paper](https://www.cat.com/en_US/by-industry/electric-power/Articles/White-papers/epa-tier-4-and-the-electric-power-industry.html)
7. [Axios, "Don't look now, but Caterpillar is becoming an AI darling" (Apr 2026)](https://www.axios.com/2026/04/30/caterpillar-ai-data-centers)
8. [Cummins Inc., Q4 and Full-Year 2025 Results press release](https://www.cummins.com/en-na/news/releases/2026/02/05/cummins-reports-strong-fourth-quarter-and-full-year-2025-results-records)
9. [Cummins Inc., Q1 2026 slides via Investing.com](https://ng.investing.com/news/company-news/cummins-q1-2026-slides-power-generation-surge-offsets-truck-weakness-93CH-2499275)
10. [Cummins Inc., S17 Centum Series press release (Jun 2025)](https://www.cummins.com/en-na/news/releases/2025/06/25/cummins-redefines-power-density-announcement-groundbreaking-17-liter)
11. [Cummins QSK95 product page](https://www.cummins.com/generators/qsk95)
12. [Cummins QSK60 2250-2500 kVA spec PDF](https://www.cummins.com/sites/default/files/2023-05/2250-2500kVA-QSK60_Rev-03.pdf)
13. [Cummins, Understanding ISO 8528 Generator Set Ratings (PowerHour white paper)](https://www.cummins.com/sites/default/files/2018-08/201707%20PowerHour_Understanding%20ISO%208528%20GeneratorSetRatings.pdf)
14. [Cummins, "Diesel Generators in the Data Center — When is the Bigger Generator the Better Generator?" technical brief](https://mart.cummins.com/imagelibrary/data/assetfiles/0056714.pdf)
15. [Cummins, Powering Growth: Data Center Backup Power (Nov 2025)](https://www.cummins.com/en-na/news/2025/11/12/powering-growth-cummins-solutions-data-center-backup-power)
16. [Cummins Power Generation case study, Digital Realty Sydney](https://www.cummins.com/case-studies/cummins-power-generation-delivers-critical-protection-power-digital-realty)
17. [Rolls-Royce, Mankato Minnesota investment press release (Mar 2025)](https://www.rolls-royce.com/media/press-releases/2025/03-06-2025-rr-powers-data-center-growth-with-increased-investment-in-us-manufacturing.aspx)
18. [Data Center Dynamics, "Rolls Royce to double production of backup diesel gen sets to supply US data center market"](https://www.datacenterdynamics.com/en/news/rolls-royce-to-double-production-of-backup-diesel-gen-sets-to-supply-us-data-center-market/)
19. [mtu Series 4000 generator sets product page](https://www.mtu-solutions.com/au/en/applications/power-generation/power-generation-applications/data-centers.html)
20. [mtu 20V4000 DS4000 4000 kVA 50 Hz spec sheet PDF](https://www.mtu-solutions.com/content/dam/mtu/products/power-generation/powergeneration-product-list-latest/32310781_PG_spec_20V4000DS4000_4000kVA_3D_FC_50Hz.pdf/_jcr_content/renditions/original./32310781_PG_spec_20V4000DS4000_4000kVA_3D_FC_50Hz.pdf)
21. [Curtis Power Solutions, MTU Onsite Energy rating definitions](https://www.curtispowersolutions.com/generator-set-ratings)
22. [Kohler / Rehlko KD3500 product page](https://www.powersystems.rehlko.com/product/kd3500)
23. [Kohler KD3500 specification sheet PDF](https://resources.kohler.com/power/kohler/industrial/pdf/g5591.pdf)
24. [Platinum Equity, Kohler Energy rebrand as Rehlko press release](https://www.platinumequity.com/news/kohler-energy-rebrands-as-rehlko/)
25. [Data Center Dynamics, "Kohler sells majority stake in energy unit to Platinum Equity"](https://www.datacenterdynamics.com/en/news/kohler-sells-majority-stake-in-energy-unit-to-platinum-equity/)
26. [Generac, "New Products Designed for the Data Center Market" (Apr 2025)](https://www.generac.com/about/news/new-products-designed-for-the-data-center-market/)
27. [Generac SDMD3250 product page](https://www.generac.com/industrial-products/stationary-generators/stationary-generator-3250kw-diesel-87.5l/)
28. [Data Center Frontier, "Generac Sharpens Focus on Data Center Power"](https://www.datacenterfrontier.com/energy/article/55281190/generac-sharpens-focus-on-data-center-power-with-scalable-diesel-and-natural-gas-generators)
29. [Mitsubishi Heavy Industries, MGS-R Series launch press release](https://www.mhi.com/news/22032401.html)
30. [Mitsubishi Heavy Industries MGS product page](https://www.mhi.com/products/energy/generation_generator_mgs.html)
31. [Wärtsilä, 507 MW data centre order press release (Nov 2025)](https://www.wartsila.com/media/news/20-11-2025-wartsila-continues-growth-in-the-data-center-segment-with-a-507-mw-order-in-the-us-offering-engines-as-a-reliable-power-solution-3686573)
32. [Wärtsilä, Ohio 429 MW data centre engine plant (Jul 2025)](https://www.wartsila.com/media/news/15-07-2025-wartsila-engines-selected-to-deliver-reliable-power-for-u-s-data-center-3632885)
33. [Penske Power Systems Australia energy solutions page](https://www.penskeanz.com/solutions/energy-solutions/)
34. [Energy Power Systems Australia (EPSA) home page](https://www.energypower.com.au/)
35. [Cat Australia, Data Centre Energy Solutions page](https://www.cat.com/en_AU/by-industry/electric-power/electric-power-industries/data-centers.html)
36. [Mordor Intelligence, Data Center Generator Market report](https://www.mordorintelligence.com/industry-reports/data-center-generator-market)
37. [Research and Markets / BusinessWire, Data Center Generator Market Landscape 2025-2030](https://www.businesswire.com/news/home/20250715362216/en/Data-Center-Generator-Market-Landscape-2025-2030-Featuring-Key-Providers---ABB-Caterpillar-Cummins-Generac-Power-Systems-HITEC-Power-Protection-Rehlko-Rolls-Royce-and-Himoinsa---ResearchAndMarkets.com)
38. [Latitude Media, "The data center boom is a diesel generator boom"](https://www.latitudemedia.com/news/the-data-center-boom-is-a-diesel-generator-boom/)
39. [Inside Climate News, "Data Centers' Use of Diesel Generators for Backup Power Is Commonplace—and Problematic"](https://insideclimatenews.org/news/12112025/data-center-diesel-generators-noise-pollution/)
40. [Kirkland & Ellis LLP, "New EPA Guidance Clarifies When Data Centers... May Utilize Emergency Backup Generators"](https://www.kirkland.com/publications/kirkland-alert/2025/05/new-epa-guidance-clarifies-when-data-centers-and-other-operators-may-utilize-emergency-backup)
41. [Sidley Austin LLP, "EPA Clarifies Rules for Backup Generator Use" (May 2025)](https://www.sidley.com/en/insights/newsupdates/2025/05/us-epa-issues-new-guidance-on-data-center-emergency-generator-operations)
42. [Generator Source, "The Facility Manager's Guide to EPA Tier 4 Final vs. Tier 2/3 Standby"](https://generatorsource.com/fuel/diesel/the-facility-managers-guide-to-epa-tier-4-final-vs-tier-2-3-standby/)
43. [Generator Source, "Data Center Generator Maintenance & Sizing"](https://generatorsource.com/industries/data-center-generator-maintenance/)
44. [Central States Diesel Generators, "Guide to Data Center Generator Maintenance"](https://csdieselgenerators.com/guide-to-data-center-generator-maintenance/)
45. [Power Engineering, "Caterpillar engines to support 2 GW of onsite power at West Virginia data center campus"](https://www.power-eng.com/onsite-power/caterpillar-engines-to-support-2-gw-of-onsite-power-at-west-virginia-data-center-campus-tied-to-microsoft-nvidia/)
46. [Power Magazine, "Data Centers Are Turning to Gas Generators for Prime Power"](https://www.powermag.com/data-centers-are-turning-to-gas-generators-for-prime-power-to-eliminate-long-lead-times-for-grid-connections/)
47. [U.S. Energy Information Administration, Construction cost data for electric generators](https://www.eia.gov/electricity/generatorcosts/)
48. [BlueCap Economic Advisors, "Cost Data Center"](https://www.bluecapeconomicadvisors.com/post/cost-data-center)
49. [Kio.tech, "Costs of a Data Center"](https://www.kio.tech/en-us/blog/data-center/costs-of-a-data-center)
50. [NEXTDC M3 Melbourne generator installation video](https://www.youtube.com/watch?v=DWsK4h-HVQE)
