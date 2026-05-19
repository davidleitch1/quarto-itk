# AI sector — top-down findings, 2026-05-16

Synthesis of research published 16 February to 16 May 2026, organised around the value-chain framing in `README.md`. Citations point to entries in `sources.md`. Numbers cross-checked across at least two sources where possible; single-source claims are flagged.

## Executive summary

The AI sector in May 2026 sits at an inflection where the bull case (compute demand exceeds supply at every hyperscaler; model-lab revenue is compounding above 10× per year; chip ASPs are rising not falling) is fundamentally true, and the bear case (free cash flow has collapsed at four of five hyperscalers; ~$1trn of off-balance-sheet obligations sit outside GAAP debt; ~94% of operating cash flow now goes to capex; the model labs financing 60-90% of that revenue back to the cloud providers are themselves loss-making) is also fundamentally true. The reconciling fact — which both bulls and bears agree on — is that the system runs on contractual web rather than on cash. Microsoft, Alphabet, Amazon, Meta and Oracle's combined 2026 capex guidance now totals roughly $800bn ([Economist, 13 May]; [Morgan Stanley]) and analysts already extrapolate >$1trn in 2027 ([CNBC, 30 April]; [Morgan Stanley, 4 May]). The customer for that capex is, in cash terms, mostly other hyperscalers and their captive model labs. Whether this resolves as a productivity miracle or a credit event depends on enterprise willingness to pay for AI output — and the most concrete McKinsey survey work to date ([McKinsey 2026 State of AI]) says 94% of adopters report no significant value from gen-AI deployments. The next 12-24 months will resolve that gap one way or the other.

## The capex / cashflow picture

### Aggregate numbers (calendar 2026 guidance, post Q1 prints)

| Issuer | 2026 capex | YoY | Operating-cash-flow context |
|---|---:|---:|:---|
| Microsoft | ~$190bn | +24% | Q3 FY26 capex $31.9bn, GM 67.6% (narrowest since 2022) |
| Alphabet | $180-190bn (raised from $175-185bn) | low single digits | Q1 capex $35.7bn; CFO flags 2027 "significantly higher" |
| Amazon | ~$200bn | +1% | Q1 capex $44.2bn (+77%); FCF –95% to $1.2bn |
| Meta | $125-145bn (raised from $115-135bn) | +8% | Quarterly FCF still positive ~$12bn |
| Oracle | $50bn FY26 (2× original) | ~ +140% | TTM FCF –$24.7bn; net debt ~$90bn |
| **Total (US Big Five)** | **~$800bn** | **~80% YoY** | |

*Sources: company press releases; [Tom's Hardware, 30 April]; [Economist, 13 May]; [Om Malik, 30 April]; [Fortune, 10 March on Oracle].*

If you add the major Chinese platforms — Alibaba $53bn (3-year), ByteDance $30bn 2026 (+25% YoY), Tencent/Baidu/Huawei plus the China-state-fund DeepSeek participation — TrendForce's nine-issuer aggregate sits around $830bn ([Morgan Stanley Institute, 2026]; [Recode China AI]). Note the China numbers are smaller than US in $ terms but rising faster off a lower base.

### The cashflow gap

The compelling Q1 2026 datapoint: Amazon's free cash flow fell 95% to $1.2bn while AWS revenue grew 28% to $37.6bn ([Amazon Q1]; [Next Web, 29 April]). Microsoft's gross margin slipped to 67.6%, the narrowest since 2022, on data-centre depreciation; Bank of America calculates hyperscaler capex now consumes ~94% of operating cash flow after dividends and buybacks ([cited via Fortune], [TheStreet]). Oracle is the visible extreme: trailing-12-month FCF –$24.7bn. The Economist's chart ([Kamikaze capex, 13 May]) shows the cashflow gap opening in 2024 and widening through 2025 and Q1 2026 — at the same time as operating profits keep rising. Two firms — Amazon and Alphabet — also booked unusually large non-cash gains from marking up their stakes in Anthropic ($16.8bn for Amazon, ~$36.8bn for Alphabet); without those marks, reported NI growth in Q1 looks meaningfully weaker ([Om Malik]).

### Buybacks and dividends

The Economist's observation that "buybacks collapsed" in Q1 ([Kamikaze capex]) is testable: aggregate Big-Five share buybacks fell sharply quarter-on-quarter while debt issuance accelerated. The reading: capital allocation has shifted from returning cash to capex and to maintaining cash buffers ahead of further debt raises.

## Revenue — what the model-makers and product-sellers actually pull in

### Frontier-lab revenue

- **OpenAI**: ~$25bn ARR as of April 2026 ([The Information via Morningstar]). Internal forecast: $14bn loss in 2026 on ~$13bn revenue; cash burn ~$27bn in 2026 and ~$63bn in 2027 ([Yahoo Finance reporting on internal projections]; [Ed Zitron]). Own forecast does not see positive cash flow until 2030. Revenue mix ~50% ChatGPT, ~20% API, ~20% other.
- **Anthropic**: $30bn ARR in April 2026 (from $14bn in February — implying 2.1× in two months) ([The Information]; [SaaStr]; [Epoch AI]). SemiAnalysis puts a higher number — $44bn — in its May piece ([SemiAnalysis, AI Value Capture]), which may be a later definitional run-rate or simply mid-May acceleration; flagged for follow-up. Anthropic's customer mix is ~80% enterprise vs OpenAI's ~50% consumer ([SaaStr]). SemiAnalysis claims inference-stack gross margins moved from 38% to 70%+ over the period; if true, that's a structural shift in the unit economics of model-as-a-product.
- **Contested**: OpenAI's CRO Denise Dresser in an internal 13 April memo claimed Anthropic's $30bn figure is overstated by ~$8bn under net-revenue conventions ([leaked memo via The Information]). Both companies' numbers are unaudited.

### Hyperscaler AI revenue

Microsoft disclosed $37bn annualised AI revenue at its Q3 FY26 print (+123% YoY); Azure constant-currency growth 40% above Street ~37-39% ([Microsoft FY26 Q3]). Google Cloud grew 63% to $20.0bn with backlog of $460bn; Pichai stated they were "compute-constrained in the near term — cloud revenue would have been higher if we could meet demand" ([Alphabet Q1]; [Tunguz, 29 April]). AWS grew 28% with RPO of $364bn excluding a fresh $100bn OpenAI commitment ([Amazon Q1]).

A pattern visible in Q1: cloud growth rates inversely correlate with operating scale, but the smallest of the three (Google Cloud) is now adding revenue at the fastest absolute rate per dollar of capex. The Tunguz framing ([29 April]) is that the hyperscaler owning the model layer (Google with Gemini) is growing fastest, which would suggest vertical-integration premium. Microsoft's looser hold on OpenAI post-April-27 restructure (see below) tests that hypothesis.

### Chip-tier revenue

Nvidia Q1 FY26 (calendar Q1 2025) revenue $44.1bn (+69%), Data Center $39.1bn (+73%) ([Nvidia 8-K]). At GTC March 2026, Huang lifted the combined Blackwell + Rubin commercial pipeline forecast to $1trn through 2027; Blackwell systems are sold out through mid-2026 ([Stratechery, TSMC Risk]; [Phemex]). ASP per Blackwell Ultra system: ~$40k. TSMC 2026 revenue guidance: +30% YoY in USD; HPC (incl. AI) is 61% of revenue; 2026 capex $52-56bn (top of range) with 70-80% on advanced nodes ([TSMC Q1 print, 16 April]; [Tom's Hardware]).

The Economist's observation that Broadcom + Micron + Nvidia + Sandisk account for ~25% of forecast S&P 500 profit growth in 2026 ([Kamikaze capex]) is the cleanest single statistic for "the hyperscalers' capex is someone else's free cash flow." Of those four, only TSMC's capex actually expands the productive capacity of the system in physical terms — the rest are operational profits flowing to chip designers and memory suppliers.

### Enterprise demand reality check

McKinsey's State of AI 2026 finds ~89% of enterprises have at least one AI deployment but 94% report no significant value yet ([McKinsey, Where AI will create value]). Only 1% describe their AI rollout as "mature." Gartner: 88% of agent pilots fail to graduate to production; 40%+ of agentic projects at risk of cancellation by 2027 ([Gartner, 26 Aug 2025 release; 15 Jan 2026 spend release]). 72% of enterprises have at least one AI workload in production; only 31% have an agent in production. These numbers describe a market that is buying, but only a sliver of which has built repeatable ROI. Gartner pegs 2026 worldwide AI spending at $2.5trn — but the bulk of that is hardware and IT services rather than software ARR flowing to model-makers.

## The contractual web — deals to know

| Counterparties | Value | Term | Date | Significance |
|:--|:--|:--|:--|:--|
| Microsoft ↔ OpenAI (restructure) | Revenue share capped; IP license to 2032 (non-exclusive); revenue share to 2030 | through 2032 | 27 Apr 2026 | AGI clause removed; OpenAI free to sell via any cloud; Microsoft retains royalty stream |
| OpenAI ↔ Oracle (Stargate) | $300bn / 5 years (begins 2027); 4.5GW; 2m+ Blackwell | 2027-2032 | confirmed 2026 | Doubles prior $30bn/yr to $60bn/yr; central to Oracle thesis |
| Anthropic ↔ Amazon | $25bn AWS invest; $100bn Anthropic spend on AWS over 10y; 5GW Trainium | 10y | 20 Apr 2026 | Trainium 2/3 capacity; Anthropic compute diversification leg 1 |
| Anthropic ↔ Google | $10bn upfront + up to $30bn milestone; 5GW TPU; $350bn post-money | multi-year | 24 Apr 2026 | Anthropic compute diversification leg 2; total pledged equity ~$65bn, 10GW reserved capacity |
| Nvidia → OpenAI | $30bn equity | one-off | Feb 2026 | Largest single Nvidia equity bet in AI; total Nvidia AI equity deployment $40bn YTD |
| Meta ↔ CoreWeave | $14.2bn original + $21bn expansion (through 2032) | to 2032 | 2026 | Largest neocloud single-customer concentration |
| OpenAI ↔ CoreWeave | $22.4bn cumulative | multi-year | 2026 | Plus $6.5bn expansion announced |
| Amazon → OpenAI | $100bn fresh commitment + $38bn existing | multi-year | Q1 2026 | Disclosed alongside AWS Q1 |
| Meta + Blue Owl (Hyperion SPV) | $27.3bn 144A bonds (A+, T+225, 2049 maturity) | 2049 | Oct 2025 | Template for off-balance-sheet AI DC financing |

OpenAI's total disclosed/leaked vendor commitments 2025-2035 aggregate ~$1.15trn across seven vendors ([Tunguz]). For context, that's roughly the entire 2026 hyperscaler capex from one customer's commitment stack, spread over a decade. The model labs are sitting at the centre of contracts that, in aggregate, exceed their own foreseeable cash generation by an order of magnitude. The hyperscalers funding them are then borrowing in the bond market to fulfil their side of those contracts. This is what the Economist labels "Kamikaze capex."

## Financing structures coming under scrutiny

### Bond issuance

Big Five raised $260bn from bond markets since start-2025, ~25% of all listed US non-financial issuance ([Economist, 13 May]). Nearly a third of 2026 issuance is in non-USD currencies; Alphabet will soon issue its first yen-denominated bonds. Headline single deals: Oracle $18bn (Sept 2025), Meta $30bn (Oct 2025 — largest non-M&A high-grade single deal in IG history), Alphabet $17.5bn (Nov 2025), Amazon $15bn, Alphabet 100-year bond (Feb 2026 — first tech century bond in decades) ([Fortune, 7 March]). BofA forecast: $175bn in hyperscaler bond issuance in 2026, >6× the $28bn historical average ([Tunguz, 29 April]). Reuters / underwriter consensus: total US IG corporate supply $2.46trn 2026 (+11.8%). Aa2/Aa3 issuers paid 10-15bp premium over existing curves; Oracle (Baa2) is two notches above junk and pays a larger spread.

### Off-balance-sheet leases (the Moody's piece)

Top-five US hyperscalers carry $662bn in not-yet-commenced data-centre lease commitments off-balance-sheet under GAAP ([Moody's, Feb 2026]; [Fortune, 25 Feb]; [Bisnow]; [DCD]). Total undiscounted future lease obligations $969bn. The $662bn is 113% of these firms' adjusted reported debt. The Economist's $820bn figure ([Kamikaze capex]) appears to be the higher uncommenced figure plus inflation through May, which is consistent. The structural reason for the off-balance-sheet treatment: equipment with 4-6 year useful life forces short initial lease terms, which fall below GAAP's threshold for liability recognition, with hyperscalers absorbing residual-value risk via RVGs ([DCD]; [Bisnow]). Investors looking only at GAAP debt see roughly half the actual contractual obligation.

### SPV financing — the Meta Louisiana template

Meta's Hyperion campus financed via Beignet Investor SPV: Blue Owl owns 80% and controls the board, Meta 20%. $27.3bn of 144A bonds issued October 2025, A+ rated by S&P, priced at T+225bp, 2049 maturity, fully amortising. Buyers include PIMCO and BlackRock ([Global Data Center Hub]; [DCD, Oct 2025]; [Vinod Kothari Consultants]). The structure achieves what Oracle's CFO called "uncoupling capex from cashflow" — Meta gets a data centre, Blue Owl and bondholders carry the financing risk, Meta's GAAP balance sheet shows none of the debt. The Economist explicitly cites this deal as the largest single corporate bond in history and flags Oracle's intention to do similar engineering ([Kamikaze capex]).

### Private-credit involvement

Apollo, Blackstone and KKR are the structural counterparties to most of these off-balance-sheet deals. Bloomberg flagged a forming $35bn Apollo+Blackstone financing for Broadcom on 8 May. Apollo's house view (per its public commentary): $5trn+ of expected data centre capex would need $1.5-2trn of annual AI revenue by 2030 vs $40-60bn today — i.e. they are aware of the gap and pricing for it. Blackstone is committed to $150bn of digital infrastructure investment over coming years.

### Circular financing critique

Bloomberg's "AI Circular Deals" graphic ([Bloomberg, 2026]) traces the flows: Microsoft invests $13bn in OpenAI → OpenAI spends most of that on Azure; Nvidia invests $30bn in OpenAI → OpenAI commits to buy Nvidia chips via Oracle's Stargate; Amazon invests $25bn in Anthropic → Anthropic commits $100bn to AWS; Google invests up to $40bn in Anthropic → Anthropic commits 5GW of TPU. EU competition staff flagged this in March 2026. Dario Amodei's defence ([cited via Yahoo Finance]): "One player has capital and has an interest, because they're selling the chips, and the other player is pretty confident they'll have the revenue at the right time, but they don't have $50bn at hand." Bull-case framing: this is just how you finance a capital-intensive infrastructure transition before the demand-side cashflows arrive. Bear-case framing: it mirrors the vendor-financing patterns of telecom equipment makers in 1999-2000, where Lucent and Nortel booked revenue from CLECs they were simultaneously lending money to, and the contract chain collapsed when one link defaulted.

### Margin / cost trends in the model layer

Token prices have been declining ~200× per year by some measures in 2024-26 (GPT-4-equivalent inference from $20/Mt in late 2022 to ~$0.40/Mt today). Anthropic cut Opus pricing 67% from $15/$75 (Opus 4.1) to $5/$25 (Opus 4.6) in Feb 2026. SemiAnalysis claims effective blended cost at Opus 4.7 is $0.99/Mt due to high cache hit rates, with inference gross margins for Anthropic rising from 38% to >70% over the period. If those two facts are simultaneously true, the model layer is on a Moore's-law-like cost-down curve while also expanding margins — which means the unit economics are improving fast enough that the customer-side demand growth (10-30× over 15 months at Anthropic) is being met without proportional capex growth at the model lab itself. The capex sits with the cloud provider. That's why hyperscaler vertical integration in the model layer (Microsoft, Google) is so contested.

## Where consensus is — and where it's cracking

### Consensus

- Demand for AI compute exceeds supply at every hyperscaler. All four Q1 callers said it explicitly ([Stratechery, Agents Over Bubbles]; [Tunguz, 29 April]). This is not in dispute.
- Token consumption and frontier-lab ARR are growing 10×+ per year. Anthropic's $1bn → $30bn in 15 months is the cleanest single datapoint ([Epoch AI]).
- TSMC is the binding physical constraint on the overall buildout pace. N3 utilisation >100% expected H2 2026; N2 fully booked ([SemiAnalysis]; [Stratechery, TSMC Risk]).
- Power/grid is the binding physical constraint on the data-centre side. Hyperscalers are moving from PPAs to direct generation investment to bypass interconnect queues ([Fortune, 18 March]; [IEA]).
- Big Five hyperscalers will dominate IG corporate bond issuance in 2026, on a scale comparable to the Big Six banks ([Reuters]).

### Where consensus is cracking

- **Returns on capex.** Goldman: maintaining historical RoIC needs >$1trn annual profit run-rate vs $450bn consensus ([Goldman, Tracking Trillions]). Sequoia: $600bn revenue gap (vs $200bn 12 months ago) ([Sequoia, $600B Question, updated 2026]). Bears (Howard Marks, Ed Zitron, Sequoia) argue this is unsustainable; bulls (a16z's Appenzeller, Jefferies, Wells Fargo) argue $5trn IT spend amortises this easily.
- **Quality of revenue.** Is the AI revenue real (distributed productive enterprise demand) or circular (hyperscalers funding labs that buy back compute)? OM Malik: "a meaningful portion of the AI revenue and AI investment gains are flowing in a circle." EU competition staff has flagged ([March 2026]). Goldman acknowledges this ([Tracking Trillions]).
- **Whether to trust GAAP.** Moody's $662bn off-balance-sheet figure plus the rising tide of SPV bonds means the visible debt understates the obligation by ~50%. The Economist makes this central to its critique ([Kamikaze capex]). Credit analysts (CreditSights, Janus Henderson) increasingly adjust for it. Equity analysts often don't.
- **Whether the labs reach cashflow positive.** OpenAI's own forecast: 2030 (which assumes flat capex commitments after 2028 — unlikely given Stargate ramp). Anthropic's improving inference margins are the clearest counter-evidence that the math can work — but its compute spend is committed via Amazon/Google not on its own balance sheet, so the question reduces to whether those clouds make their money back from Anthropic's growth.
- **Microsoft vs Google for the integration premium.** Post-27 April restructure, OpenAI is no longer exclusive to Azure. Google's Cloud growth at 63% (with own model Gemini) outpaces Azure's 40% (with hosted OpenAI). If the integration premium thesis is right, Google should keep widening that gap.

### Bull-case framing (synthesised)

Demand for compute exceeds supply at every hyperscaler. Token-per-minute throughput at Gemini grew 60% QoQ in Q1. Agents (Claude 4.5/Opus 4.7, GPT-5.4, Gemini-2.5-Pro) multiply compute demand because one human supervises many agent runs ([Stratechery]). Enterprise willingness to pay is rising even if value capture is uneven. Frontier-lab gross margins are expanding even as headline token prices fall. Capex looks vertiginous but $5trn of global IT spend can amortise it. Mag-7 trade at ~23× forward earnings — not stretched on metrics that ignore capex, stretched if you penalise the unrecognised obligations. ([a16z]; [Bernstein]; [Wells Fargo]; [Jefferies]; [Stratechery].)

### Bear-case framing (synthesised)

Free cash flow has collapsed at four of five hyperscalers. Capex is 94% of operating cash flow. Goldman's math says reaching ~$1trn aggregate profit run-rate is needed to justify the deployed capital; consensus has $450bn. $662bn of lease obligations sit off the balance sheet; SPV bonds are extending that further. The model labs being funded by the hyperscalers are not cash-positive and don't expect to be for years; OpenAI's own forecast says 2030. Token prices are falling 200× per year while ASPs of training/inference hardware are rising. Nvidia's $40bn YTD equity into customers is vendor financing in another costume. The enterprise demand surveys (McKinsey 94% no-value, Gartner 88% pilot-failure) do not support the scale of the build. Telecom 1999-2000 had all the same features and ended with $300bn+ of impairments. ([Goldman]; [Sequoia]; [Morgan Stanley bubble note]; [Howard Marks via TheStreet]; [Ed Zitron]; [Economist].)

## Open questions for follow-up research

1. **Anthropic ARR reconciliation.** SemiAnalysis says $44bn in mid-May; The Information/Epoch say $30bn in April. Definitional? Or May acceleration? Drives the whole model-lab valuation question.
2. **What share of hyperscaler AI revenue is circular?** A first-principles estimate would tag revenue from OpenAI, Anthropic, xAI, Cohere, Mistral and partner-equity stakes as circular, vs revenue from non-stake'd third-party enterprises. The Bloomberg graphic gestures at this but doesn't quantify it.
3. **The Oracle balance sheet.** $50bn FY26 capex, –$25bn TTM FCF, ~$90bn net debt, Baa2 rating, $300bn OpenAI contract anchoring the FY28+ revenue line. What's the credit rating sensitivity? When does Stargate revenue actually start being recognised?
4. **Moody's $662bn breakdown by issuer.** The aggregate is in the public report. Per-firm is less clear. Where does each of Microsoft/Alphabet/Amazon/Meta/Oracle sit in the $662bn?
5. **What's the asset life mark-down risk?** Microsoft disclosed $37.5bn of one quarter's capex went to "short-lived" assets (GPUs, 5y depreciation) — well below traditional DC infra (30y). If Blackwell-class GPUs are obsoleted faster than the 5y schedule (because Rubin or AMD MI400X is better), there's an impairment risk that doesn't show in the bond covenants.
6. **Where does the bond-market debt actually sit on issuance dates vs SPV-bond commitments?** Need to triangulate the $260bn Big-Five 2025-26 IG issuance with the $662bn off-balance-sheet plus the Hyperion-style $27bn private-credit deals — the totality is the real "AI debt stack."
7. **China-side capex with US dollar comparability.** ByteDance $30bn, Alibaba $53bn over 3y — is this comparable in compute-output terms to US hyperscaler capex, or is it inflated by US export-control workarounds raising effective per-chip cost?
8. **Enterprise per-seat economics.** Microsoft 365 Copilot, Google Workspace Gemini, Anthropic Claude Enterprise — what are the actual adoption / churn / pricing trends inside large enterprises? McKinsey's 94%-no-value survey suggests something is broken; Gartner's $2.5trn TAM suggests revenue is somewhere. Where?
9. **Power-side bottleneck cost.** IEA says +15% p.a. data-centre power. What's the all-in $/MWh that hyperscalers actually pay in 2026 vs 2024, accounting for direct-investment-in-generation now happening? This connects directly to the user's existing electricity-market expertise.
10. **The 2027-28 capex trajectory.** Alphabet CFO said 2027 capex "significantly higher" than 2026. Microsoft hasn't given 2027 numbers. Morgan Stanley's $1.1trn 2027 forecast: how is that distributed across the Big Five, and at what point do the credit ratings start moving?
