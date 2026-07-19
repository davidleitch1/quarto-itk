---
title: "How the four banks valued SpaceX's AI business"
author: "David Leitch"
date: 2026-07-19
categories: ["Investment", "Demand"]
lightbox: true
draft: false
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

Reference note, July 2026. Companion to the main orbital data-centres note; this records the starting point — what each initiating bank actually did — so the back-out analysis can be followed. Banks are anonymised as A–D, consistent with the charts. All four reports were published on 7 July 2026.

**Table: the four approaches at a glance**

| | Bank A | Bank B | Bank C | Bank D |
|:--|:--|:--|:--|:--|
| Price target | $210 | $205 | $225 | $200 |
| AI segment value | ~$1.7tn | ~$2.28tn | ~$2.37tn | not separated |
| AI share of company value | ~63% | ~68% | ~77% | n/a |
| Profit year used | 2028 forecast | 2029 forecast | 2028 forecast | 2027 and 2030 forecasts |
| Multiple applied | 28× EBITDA | 28× operating income | 50× operating income | averages of three methods |
| Where orbital sits | In the multiple ("optionality") | In the earnings (~half of 2029 capacity) | In the multiple (stated) | Inside an undivided AI segment |

*Source: ITK summary of the four initiation reports, 7 July 2026.*

## Bank A — a premium multiple justified by orbital "optionality"

Bank A values SpaceX as three businesses — launch, satellite broadband, and AI — and adds them. The AI segment gets **28 times its forecast 2028 EBITDA of about $61bn, giving roughly $1.7tn**, about 63% of the company's total value.

Where does 28× come from? The big cloud-computing companies trade at about 11× EBITDA while growing about 23% a year. Bank A argues SpaceX's AI profits will grow about 60% a year, and scales the multiple up proportionately. The AI *earnings* in the model are terrestrial — the bank states its base case is "anchored by GW-scale terrestrial footprint" — but the *multiple* is defended, in the bank's own words, because the framework "attempts to capture the optionality associated with initiatives such as Orbital AI Compute and Terafab, neither of which are reflected in the business models of traditional hyperscalers."

In short: orbital appears nowhere in the numbers and everywhere in the multiple. The growth rate that justifies 28× is itself largely a forecast of orbital scaling after 2028.

## Bank B — orbital capitalised inside the base-case earnings

Bank B also sums the parts, but anchors on **2029** forecasts: AI operating income of $81.4bn at 28×, giving **~$2.28tn**, about 68% of company value, which is then discounted back two years to produce the $205 target.

The distinctive feature: Bank B's 2029 anchor year already contains **8.5 GW of orbital computing out of ~17.5 GW total** — roughly half the capacity generating the anchor-year profit is satellites that, at publication, had never flown. Orbital is not an option here; it is in the base case, capitalised in the price target. The bank does not split terrestrial from orbital revenue anywhere in the report. Its AI revenue path runs from $15.6bn (2026) to $589bn (2031), roughly doubling every year.

## Bank C — orbital excluded from the target, priced in the multiple anyway

Bank C's $225 target is built differently: **41 times forecast 2028 earnings per share**, with the 2028 anchor chosen deliberately because orbital is still negligible that year (0.4 GW, internal use only) — so the bank can describe orbital as an unpriced option rather than a forecast.

But its supporting sum-of-the-parts tells the fuller story: the AI segment at **50 times 2028 operating income, ~$2.37tn, 77% of company value** — and the bank states directly that the 50× multiple "reflects the long-duration optionality of orbital compute." Alongside the $225 target it publishes a $436 "illustration" (20× forecast 2031 earnings, discounted back), which it describes as the lens that captures orbital. The gap between the two numbers — over $200 per share — is orbital option value, displayed but not formally priced.

## Bank D — three methods averaged, orbital inseparable

Bank D's $200 target is the average of three approaches: growth-adjusted multiples on 2027 forecasts ($191), a sum of the parts ($187), and multiples on 2030 forecasts ($222). Its sum of the parts divides AI only into "advertising" and "infrastructure" sub-segments, with orbital folded inside infrastructure and never disaggregated — which is why no terrestrial value can be backed out of Bank D and it is absent from the ITK decomposition charts.

Bank D is also the most conditional in language, describing orbital economics as "economically fragile once real-world losses materialize" — and the most expansive in aspiration, publishing a long-term illustrative value of "$900+" per share predicated on roughly $1tn of revenue by 2031 if every milestone lands.

## What the four have in common

- **None publishes a standalone orbital valuation, profit forecast, or per-satellite return model** (Bank A partially excepted — it has a one-page unit economics table). Orbital is carried inside an AI segment worth 63–77% of company value.
- Across ~390 pages and 21 named analysts, roughly **20 pages discuss orbital computing** — the business that carries most of each model's growth beyond 2028.
- All four assume orbital capacity, when it arrives, earns **$9–15 per watt-year — the same rates as terrestrial data centres** — with no discount for slower service, ageing chips, or unrepairable failures.
- All four describe essentially the same satellite (SpaceX's disclosed AI1 design) and the same launch-cost trajectory; the consensus is one company's guidance restated four ways.

## How ITK uses this

The decomposition in the main note reverses each bank's own construction: where orbital sits in the multiple (Banks A and C), the terrestrial business is re-valued at ordinary comparator multiples and the residual is orbital; where orbital sits in the earnings (Bank B), the earnings are split by capacity share. That produces the implicit orbital value of roughly $1.0–1.4tn per bank, and — after also pricing the data-centre leasing business at listed-comparator (CoreWeave) levels — the residual implied value of the Grok model business. The supporting detail is in `model_assumptions.md` and `spacex_2026_revenue.md`.

*Source: ITK research, July 2026, from the four initiation reports of 7 July 2026. Quotations are from the reports; page-level extracts are held in the research file.*
