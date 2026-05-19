"""Populate companies.csv with two new columns:

  total_revenue_2026e_usd_bn  — analyst consensus next-FY revenue for listed
                                cos via yfinance; press/research for unlisted
  ai_revenue_2026e_usd_bn     — AI-attributable portion; sourced cell-by-cell
                                from `layer_revenue_2026e.md` (agent research)

Convention notes:
- Total revenue is FY-as-reported. Microsoft FYE Jun → FY26 ≈ CY2026 H1+H2.
  Nvidia FYE Jan → FY27 ≈ CY2026. Most others are calendar FY.
- AI revenue values are from the per-company table in layer_revenue_2026e.md.
  Where the agent's data is a range, midpoint is used.
- For labs and pure-play neoclouds, AI = total (~100% AI exposure).
- For diversified companies (chip, hyperscaler, SaaS incumbent),
  AI < total — the gap is the non-AI segment.

Run: python3 fetch_revenue.py
"""
import pandas as pd
import yfinance as yf
from pathlib import Path

HERE = Path(__file__).parent
CSV = HERE / 'companies.csv'

FX = {'USD': 1.0, 'KRW': 0.00072, 'HKD': 0.128, 'TWD': 0.0309,
      'EUR': 1.08, 'GBP': 1.27, 'JPY': 0.0065}


def ticker_to_symbol(t):
    if pd.isna(t) or not t:
        return None
    if ':' not in t:
        return t
    exch, code = t.split(':', 1)
    suffix = {'NASDAQ': '', 'NYSE': '',
              'KRX': '.KS', 'HKEX': '.HK', 'TWSE': '.TW',
              'LSE': '.L'}.get(exch, '')
    return code + suffix


def fetch_total_revenue_2026e(symbol):
    """Try +1y consensus first; fall back to TTM × growth."""
    try:
        t = yf.Ticker(symbol)
        info = t.info or {}
        currency = info.get('financialCurrency') or info.get('currency') or 'USD'
        fx = FX.get(currency.upper(), 1.0)

        # Attempt: forward revenue estimate
        try:
            re = t.revenue_estimate
            if re is not None and not re.empty:
                # yfinance returns rows indexed by period: '0q', '+1q', '0y', '+1y'
                for key in ('+1y', '0y'):
                    if key in re.index:
                        avg = re.loc[key, 'avg']
                        if pd.notna(avg):
                            return round(avg * fx / 1e9, 1), f"yf.revenue_estimate {key}"
        except Exception:
            pass

        # Fallback: TTM × revenueGrowth
        ttm = info.get('totalRevenue')
        if ttm:
            growth = info.get('revenueGrowth') or 0.10
            est = ttm * (1 + growth)
            return round(est * fx / 1e9, 1), f"TTM × ({1+growth:.2f}) fallback"
    except Exception as e:
        return None, f"error: {e}"
    return None, "no data"


# ── AI revenue per company (sourced from layer_revenue_2026e.md) ─────────
# Where the source quotes a range, midpoint is used. Cell-by-cell rationale
# in comments. Companies missing from this dict → blank in CSV.
AI_REV_2026E = {
    # Layer 1 — Chip / silicon
    'Nvidia':                     285,    # DC FY27 (~CY2026); Q1 FY27 guide $78bn × 91% DC
    'AMD':                        11,     # Instinct $10-12bn (TweakTown analyst)
    'Broadcom':                   40,     # Mizuho FY26 forecast $40.4bn
    'TSMC':                       60,     # HPC = 61% of FY26 rev ~$100bn (foundry; excluded from layer total but is TSMC's own AI revenue)
    'SK Hynix':                   17,     # HBM ~50% of $35bn AI HBM market
    'Samsung Electronics':        10,     # HBM ~28% share
    'Micron Technology':          7,      # HBM ~20% share
    'Marvell Technology':         5,      # AI portion of $7-8bn DC
    'Astera Labs':                1.4,    # ~100% AI
    'Intel':                      1,      # Small Gaudi line
    # Layer 2 — Infrastructure
    'Microsoft':                  50,     # $37bn Q3 run-rate → ~$50 YE
    'Alphabet':                   38,     # GCP AI-attributable midpoint $35-40
    'Amazon':                     28,     # AWS AI-attributable midpoint $25-30
    'Meta Platforms':             0,      # No external AI revenue (captive)
    'Oracle':                     18,     # OCI FY26 guide $18bn (~all AI-driven)
    'CoreWeave':                  12.5,   # FY26 guide $12-13bn (~100% AI)
    'Nebius Group':               3,      # Neocloud aggregate split
    'Equinix':                    5,      # AI-colocation share ~50% of $10.1bn
    'Digital Realty':             3,      # AI share ~45% of $6.7bn
    'Dell Technologies':          50,     # AI-server FY27 guide
    'Super Micro Computer':       40,     # FY26 guide $40bn+
    'Hewlett Packard Enterprise': 5,      # AI server line (smaller share)
    'Lenovo Group':               6,      # Estimate (China + global)
    # Layer 3 — Labs (~100% AI = total)
    'OpenAI':                     55,     # YE ARR midpoint $50-60
    'Anthropic':                  60,     # YE ARR midpoint $50-70
    'Mistral AI':                 1,      # €1bn target = ~$1.1bn
    'Cohere':                     0.3,    # $150m → $300m YE estimate
    'DeepSeek':                   0.1,    # Mostly open-weight; minimal commercial rev
    'Stability AI':               0.1,    # Distressed
    'Black Forest Labs':          0.1,    # Small, recent
    'SpaceX':                     2,      # xAI ARR portion (Sacra, SQ Magazine)
    'Databricks':                 7,      # Most of ARR is AI-related
    # Layer 4 — Products
    'Salesforce':                 2.5,    # Agentforce + Data Cloud $1.8bn → grow to YE
    'ServiceNow':                 1.5,    # Now Assist ACV YE target
    'Adobe':                      7,      # AI-first ARR per Q1 FY26
    'Workday':                    1.5,    # Estimate (small AI add-ons)
    'Anysphere (Cursor)':         2.5,    # $2bn Feb 2026, conservative YE
    'Glean':                      0.2,    # $200m ARR
    'Harvey':                     0.1,    # Estimate from $8bn valuation Nov 2025
    'Cresta':                     0.1,    # Estimate
    'Sierra':                     0.15,   # $150m Jan 2026
    'Decagon':                    0.05,   # Long-tail
    'Hebbia':                     0.05,   # Long-tail
    'Perplexity':                 0.15,   # ~$150m
    # Financiers: blank (not AI revenue per se)
}

# Total revenue for unlisted/pending — from research, not Yahoo
TOTAL_REV_UNLISTED = {
    'OpenAI':             55,     # = AI (lab is ~100% AI)
    'Anthropic':          60,
    'SpaceX':             25,     # xAI $2 + Starlink ~$15 + launches ~$5 + other (rough)
    'Databricks':         7,
    'Mistral AI':         1,
    'Cohere':             0.3,
    'DeepSeek':           0.1,
    'Stability AI':       0.1,
    'Black Forest Labs':  0.1,
    'Anysphere (Cursor)': 2.5,
    'Glean':              0.2,
    'Harvey':             0.1,
    'Cresta':             0.1,
    'Sierra':             0.15,
    'Decagon':            0.05,
    'Hebbia':             0.05,
    'Perplexity':         0.15,
}


def main():
    df = pd.read_csv(CSV)

    if 'total_revenue_2026e_usd_bn' not in df.columns:
        df['total_revenue_2026e_usd_bn'] = pd.NA
    if 'ai_revenue_2026e_usd_bn' not in df.columns:
        df['ai_revenue_2026e_usd_bn'] = pd.NA

    listed = df[df['listing_status'] == 'listed']
    print(f"Fetching total revenue 2026e for {len(listed)} listed companies...\n")
    for idx, row in listed.iterrows():
        sym = ticker_to_symbol(row['ticker'])
        if not sym:
            continue
        val, basis = fetch_total_revenue_2026e(sym)
        if val is not None:
            df.loc[idx, 'total_revenue_2026e_usd_bn'] = val
        print(f"  {sym:12s} {row['company']:32s} total ${val}bn  ({basis})")

    # TSMC: refetch via 2330.TW for clean FX (TSM ADR has the currency-mix issue)
    print("\nTSMC: override with 2330.TW × FX")
    tsmc_idx = df[df['company'] == 'TSMC'].index[0]
    val, basis = fetch_total_revenue_2026e('2330.TW')
    if val is not None:
        df.loc[tsmc_idx, 'total_revenue_2026e_usd_bn'] = val
        print(f"  TSMC total: ${val}bn ({basis})")

    # Unlisted/pending total revenue
    print("\nPopulating unlisted/pending total revenue from research:")
    for company, val in TOTAL_REV_UNLISTED.items():
        m = df[df['company'] == company].index
        if len(m) == 0:
            print(f"  WARN: {company} not found")
            continue
        df.loc[m[0], 'total_revenue_2026e_usd_bn'] = val
        print(f"  {company:32s} ${val}bn")

    # AI revenue cell-by-cell
    print("\nPopulating AI revenue from layer_revenue_2026e.md:")
    for company, val in AI_REV_2026E.items():
        m = df[df['company'] == company].index
        if len(m) == 0:
            print(f"  WARN: {company} not found")
            continue
        df.loc[m[0], 'ai_revenue_2026e_usd_bn'] = val
        print(f"  {company:32s} AI ${val}bn")

    # Reorder columns
    col_order = ['company', 'layer', 'sub_segment', 'listing_status',
                 'ticker', 'country',
                 'mkt_cap_usd_bn', 'debt_usd_bn', 'leased_usd_bn', 'ev_usd_bn',
                 'total_revenue_2026e_usd_bn', 'ai_revenue_2026e_usd_bn',
                 'performance_3m_pct', 'performance_12m_pct',
                 'source', 'notes']
    df = df[col_order]
    df.to_csv(CSV, index=False)

    # Sanity check: AI should never exceed total
    err = df[df['ai_revenue_2026e_usd_bn'].notna()
             & df['total_revenue_2026e_usd_bn'].notna()
             & (df['ai_revenue_2026e_usd_bn'] > df['total_revenue_2026e_usd_bn'])]
    if not err.empty:
        print("\n!! AI revenue exceeds total revenue for:")
        print(err[['company', 'total_revenue_2026e_usd_bn', 'ai_revenue_2026e_usd_bn']].to_string(index=False))
    else:
        print("\nSanity check passed: AI ≤ Total for all rows.")

    pop = df[df['total_revenue_2026e_usd_bn'].notna()].shape[0]
    ai_pop = df[df['ai_revenue_2026e_usd_bn'].notna()].shape[0]
    print(f"\nWrote {CSV}  ·  total_revenue populated for {pop}/{len(df)} rows  ·  ai_revenue for {ai_pop}/{len(df)} rows")


if __name__ == '__main__':
    main()
