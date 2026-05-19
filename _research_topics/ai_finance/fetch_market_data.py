"""Fetch market cap, debt, EV, and 12m performance from Yahoo Finance for
listed companies in companies.csv. For non-US listings, converts the local
currency to USD using approximate FX. For unlisted companies, manually
populates high-confidence valuations from our research.

Re-run periodically: python3 fetch_market_data.py

Caveats:
- Yahoo `totalDebt` is GAAP gross debt — does NOT include off-balance-sheet
  data-centre lease commitments (~$662bn Moody's for the Big-5 hyperscalers).
  The `source` column flags this with "Yahoo Finance YYYY-MM-DD".
- Yahoo `enterpriseValue` already nets out cash (EV = MktCap + TotalDebt
  + MinorityInterest + Preferred − Cash). Use this directly rather than
  recomputing.
- 12m performance is trailing-365-day price change ending today.
"""
import pandas as pd
import yfinance as yf
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
CSV = HERE / 'companies.csv'

# Approximate FX rates (May 2026) — refresh periodically
FX = {
    'USD': 1.0,
    'KRW': 0.00072,   # ~1390 KRW/USD
    'HKD': 0.128,     # ~7.81 HKD/USD
    'TWD': 0.0309,    # ~32.4 TWD/USD
    'EUR': 1.08,
    'GBP': 1.27,
    'JPY': 0.0065,
}


def ticker_to_symbol(ticker):
    """Convert 'NASDAQ:NVDA' to 'NVDA', 'KRX:000660' to '000660.KS', etc."""
    if pd.isna(ticker) or not ticker:
        return None
    if ':' not in ticker:
        return ticker
    exch, code = ticker.split(':', 1)
    suffix = {
        'NASDAQ': '', 'NYSE': '',
        'KRX': '.KS', 'HKEX': '.HK', 'TWSE': '.TW', 'LSE': '.L', 'TSE': '.T',
    }.get(exch, '')
    return code + suffix


def fetch_yahoo(symbol):
    """Return dict with mkt_cap, debt, ev (in USD bn), perf_12m_pct."""
    try:
        t = yf.Ticker(symbol)
        info = t.info or {}
        currency = info.get('currency', 'USD').upper()
        fx = FX.get(currency, 1.0)

        def to_bn(v):
            if v is None or v == 0:
                return None
            return round(v * fx / 1e9, 1)

        hist = t.history(period='1y')
        perf = None
        if not hist.empty and len(hist) > 1:
            first = hist['Close'].iloc[0]
            last = hist['Close'].iloc[-1]
            perf = round((last / first - 1) * 100, 1)

        return {
            'mkt_cap_usd_bn': to_bn(info.get('marketCap')),
            'debt_usd_bn': to_bn(info.get('totalDebt')),
            'ev_usd_bn': to_bn(info.get('enterpriseValue')),
            'performance_12m_pct': perf,
            'currency': currency,
        }
    except Exception as e:
        return {'error': str(e)}


def main():
    df = pd.read_csv(CSV)

    for c in ['symbol', 'mkt_cap_usd_bn', 'debt_usd_bn', 'ev_usd_bn',
              'performance_12m_pct', 'source']:
        if c not in df.columns:
            df[c] = None

    df['symbol'] = df['ticker'].apply(ticker_to_symbol)

    today = datetime.now().strftime('%Y-%m-%d')
    listed = df[df['listing_status'] == 'listed']
    print(f"Fetching {len(listed)} listed companies from Yahoo Finance...")

    for idx, row in listed.iterrows():
        sym = row['symbol']
        if not sym:
            print(f"  [{row['company']}] no symbol — skip")
            continue
        data = fetch_yahoo(sym)
        if 'error' in data:
            print(f"  {sym:12s} ERROR — {data['error'][:80]}")
            continue
        for k in ('mkt_cap_usd_bn', 'debt_usd_bn', 'ev_usd_bn', 'performance_12m_pct'):
            df.loc[idx, k] = data[k]
        df.loc[idx, 'source'] = f"Yahoo Finance {today}"
        mc = data.get('mkt_cap_usd_bn')
        perf = data.get('performance_12m_pct')
        print(f"  {sym:12s} ({data['currency']})  mc=${mc}bn  perf={perf}%")

    # High-confidence unlisted valuations from research files
    unlisted_estimates = {
        'Anthropic':  {'mkt_cap_usd_bn': 350.0,
                       'source': 'Apr 2026 Google round post-money (sources.md)'},
        'SpaceX':     {'mkt_cap_usd_bn': 1500.0,
                       'source': '2026 IPO target, pre-IPO (sources.md)'},
        'Databricks': {'mkt_cap_usd_bn': 62.0,
                       'source': 'Dec 2024 funding round'},
    }
    for company, data in unlisted_estimates.items():
        idx_match = df[df['company'] == company].index
        if len(idx_match) > 0:
            for k, v in data.items():
                df.loc[idx_match[0], k] = v

    col_order = ['company', 'layer', 'sub_segment', 'listing_status',
                 'symbol', 'ticker', 'country',
                 'mkt_cap_usd_bn', 'debt_usd_bn', 'ev_usd_bn',
                 'performance_12m_pct', 'source', 'notes']
    df = df[col_order]
    df.to_csv(CSV, index=False)

    n_priced = df['mkt_cap_usd_bn'].notna().sum()
    print(f"\nWrote {CSV}  ·  {n_priced} rows have mkt_cap populated")


if __name__ == '__main__':
    main()
