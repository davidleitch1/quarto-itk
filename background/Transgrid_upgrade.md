---
title: "TransGrid upgrade for the Sydney West data centre cluster: what 'needs grid upgrade' means specifically"
author: "David Leitch"
date: 2026-05-14
categories: ["Networks", "Demand"]
lightbox: true
draft: true
format:
  html:
    include-after-body:
      - "../comment_load.html"
  docx: default
---

The Config C architecture from `dc_more_backup_notes.md` — 4-hour BESS plus 24-hour diesel instead of the current 96-hour diesel — relies on the upstream grid being reliable enough that no credible outage exceeds 24 hours. Three specific things must be in place for an operator to credibly drop the diesel spec from 96 hours to 24 hours under TIA-942 Rated-4 audit.

## 1. Physical infrastructure — N-2 at Sydney West

The current N-1 configuration at Sydney West tolerates any single contingency (one transformer, one line, one breaker) without losing load. The credible failure modes that drive longer-than-24-hour restoration today — busbar faults, multi-tower collapse, two-line loss during planned outage — are not N-1 protected.

**Specific kit needed**

| Component | Indicative AU\$M |
|:----------|----------------:|
| Third 330/132 kV transformer at Sydney West (so the 600 MVA fleet becomes N-2 capable) | 30-60 |
| Third 132 kV cable circuit corridor to the cluster (separates Eastern Creek and Huntingwood feeds from a common single-corridor risk) | 50-150 |
| Pre-positioned spare 330/132 kV transformer at TransGrid depot, plus transport and rapid-install infrastructure | 30-50 |
| Busbar protection upgrades (duplicate protection systems for the 330 kV bus at Sydney West) | 10-20 |
| Sydney Southern Ring completion (South Creek 500/330 kV substation already under construction — provides upstream redundancy) | already in TransGrid 2023-2028 RAB |
| **Total cluster-specific physical investment** | **120-280** |

*Source: TransGrid Transmission Annual Planning Report 2023; Sydney Southern Ring project documentation; ITK analysis of cluster-specific reliability augmentation requirements.*

Most of this can be retrofitted to the existing Sydney West site over a 3-5 year program. It's not a greenfield project — it's incremental capacity and redundancy on top of existing infrastructure.

## 2. Contractual SLA from TransGrid

Without a binding SLA, the physical infrastructure doesn't change the DC operator's audit obligation. The Rated-4 auditor needs a documented commitment that any credible failure will be restored within 24 hours. **This is not currently a product TransGrid offers.**

What it would look like:

- TransGrid (and ultimately AEMO as system operator) contractually commits to a 24-hour maximum restoration window for any credible failure within the contracted reliability footprint
- Includes specified pre-positioned spares, response-team SLAs, and is backed by insurance or AER-approved bonding
- Penalties payable to the customer if breached
- Tied to specific connection points (Sydney West cluster customers in this case)

The closest existing analogue in Australia: **the Reliability and Emergency Reserve Trader (RERT)**, where AEMO contracts in advance for emergency response capacity, with payments for availability plus payments for activation. The Sydney West reliability SLA would be a customer-side version of the same idea — TransGrid pre-contracting for guaranteed restoration time, with payments coming from the contracted customers.

## 3. AEMC regulatory framework — the "negotiated reliability tier"

The AEMC's National Electricity Rules don't currently recognise customer-side negotiation of TNSP reliability levels. TransGrid's reliability obligations are set by the AER revenue determination process and the AEMC's reliability standards, not by customer contract. A new rule category would be needed:

- A "negotiated reliability tier" framework allowing a cluster of high-reliability customers to contract directly for enhanced TNSP reliability in exchange for a defined customer-side backup obligation
- Cost-allocation tied to the avoided incremental investment (Wallumatta STS contingent project precedent)
- Independent audit and SLA enforcement
- Interface with TIA-942 / Uptime Institute tier audits so the AEMC-recognised reliability counts toward Rated-4 / Tier IV compliance

The AEMC Package 2 transmission cost-allocation work (final mid-2026) is the natural vehicle for introducing this. It's not currently on the consultation agenda but would be a logical extension. **Until it lands, Config C is theoretical — operators can't legally accept the 24-hour spec under Rated-4 audit even if all the physical infrastructure existed.**

## Cost-allocation summary

If all three pieces were in place, who pays for what:

**Cost allocation across the three components**

| Component | Who pays |
|:----------|:---------|
| Sydney West physical upgrade (A\$120-280M) | DC cluster customers via cost-reflective tariff (Wallumatta model) |
| TransGrid SLA pre-positioning and emergency-response capability | DC cluster customers via reliability service fee (~A\$5-15M/yr cluster-wide) |
| AEMC rule change drafting | AEMC operating budget (standard process) |
| Customer-side audit and verification | DC operators (their own audit cost) |

*Source: AER Contingent Project framework (Wallumatta STS Macquarie Park precedent, Feb-Oct 2025); AEMC Package 2 consultation materials; ITK analysis.*

Cluster-wide annualised cost: ~A\$8-22M/yr (capex annualised plus SLA payments). Cluster-wide saving from spec reduction: ~A\$17M/yr in diesel opex plus ~A\$60M of one-off diesel infrastructure capex avoided. **Net cluster-wide benefit roughly neutral to positive on direct dollars — but the social and environmental benefits (75% reduction in metropolitan diesel inventory) are the larger gain.**

---

*See also: `dc_more_backup_notes.md` for the full backup-architecture analysis the Config C reference connects to; `backup_power_market.md` for the underlying genset market structure; `data_centres_australia_top10_construction.md` for the cluster composition.*

*Charts referenced: `aemo_spot/pngs/sydney_west_backup_costs_with_revenue.png` (where Config C sits on the cost curve); `aemo_spot/pngs/dc_backup_configurations.png` (the configuration comparison table that flags Config C as cost-optimal).*
