"""Hierarchical treemap of company enterprise value within sub-sector.

Each tile is a company, sized by EV (or market cap for unlisted as proxy),
coloured by sub-sector container. Flexoki Light pastels.

Output: ev_treemap_2026-05-17.png

Run: python3 make_ev_treemap.py
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import yfinance as yf

HERE = Path(__file__).parent

# Flexoki Light pastels — one per sub-sector
SUB_SECTOR_COLORS = {
    'Hyperscalers':                '#BFCFE7',  # blue 200
    'GPU & accelerators':          '#BFD8D5',  # cyan 200
    'HBM memory':                  '#C2D3B5',  # cyan-green
    'Custom silicon + networking': '#D8E0AB',  # green 200
    'Foundry':                     '#D8E2C5',  # sage
    'Frontier AI labs':            '#E5C0D5',  # magenta 200
    'AI server OEMs':              '#DAE0EE',  # pale blue
    'DC REITs / developers':       '#C5D5E0',  # blue-grey
    'Neoclouds':                   '#B5C8DA',  # blue darker
    'Incumbent SaaS':              '#DDE2B2',  # green 200
    'AI-native SaaS':              '#C7D4A0',  # darker green
    'Private credit / alt mgrs':   '#F0E5B0',  # yellow 200
    'Semi equipment':              '#DACCEB',  # purple 200 — chip-adjacent
}

SUB_SECTOR_MAP = {
    'GPU_accelerator': 'GPU & accelerators',
    'custom_silicon': 'Custom silicon + networking',
    'networking_silicon': 'Custom silicon + networking',
    'foundry': 'Foundry',
    'HBM_memory': 'HBM memory',
    'HBM_memory_foundry': 'HBM memory',
    'hyperscaler': 'Hyperscalers',
    'neocloud': 'Neoclouds',
    'dc_reit': 'DC REITs / developers',
    'dc_developer': 'DC REITs / developers',
    'ai_server_oem': 'AI server OEMs',
    'frontier_lab': 'Frontier AI labs',
    'frontier_lab_parent': 'Frontier AI labs',
    'enterprise_saas': 'Incumbent SaaS',
    'data_ai_platform': 'AI-native SaaS',
    'ai_native_dev': 'AI-native SaaS',
    'ai_native_enterprise_search': 'AI-native SaaS',
    'ai_native_legal': 'AI-native SaaS',
    'ai_native_cs': 'AI-native SaaS',
    'ai_native_research': 'AI-native SaaS',
    'ai_native_search': 'AI-native SaaS',
    'alt_asset_mgr': 'Private credit / alt mgrs',
    'sovereign_wealth': 'Sovereign wealth',
}

df = pd.read_csv(HERE / 'companies.csv')
df['sub_sector'] = df['sub_segment'].map(SUB_SECTOR_MAP)

# EV proxy: ev_usd_bn (Yahoo) for listed; mkt_cap_usd_bn for unlisted/pending
df['ev_proxy_bn'] = df['ev_usd_bn'].fillna(df['mkt_cap_usd_bn'])
df = df[df['ev_proxy_bn'].notna() & (df['ev_proxy_bn'] > 0)]

# Sovereigns excluded (PIF/QIA/MGX — no public EV)
df = df[df['sub_sector'] != 'Sovereign wealth']

# ── For this plot only: add OpenAI + Cerebras + semi equipment ───────────
# OpenAI is in the CSV but with no valuation populated — patch inline.
openai_idx = df[df['company'] == 'OpenAI'].index
if len(openai_idx) == 0:
    df = pd.concat([df, pd.DataFrame([{
        'company': 'OpenAI', 'sub_sector': 'Frontier AI labs',
        'ev_proxy_bn': 500.0,
    }])], ignore_index=True)
else:
    df.loc[openai_idx[0], 'ev_proxy_bn'] = 500.0
    df.loc[openai_idx[0], 'sub_sector'] = 'Frontier AI labs'

# Fetch semi-equipment + Cerebras market data from yfinance
EXTRA_SYMBOLS = {
    'ASML':  ('ASML',                       'Semi equipment'),
    'AMAT':  ('Applied Materials',          'Semi equipment'),
    'KLAC':  ('KLA Corp',                   'Semi equipment'),
    'LRCX':  ('Lam Research',               'Semi equipment'),
    'CBRS':  ('Cerebras Systems',           'GPU & accelerators'),
}
print("\nFetching extra symbols from Yahoo Finance...")
extras = []
for sym, (name, sub) in EXTRA_SYMBOLS.items():
    # Cerebras: override with Day-1 close ($67bn). Yfinance data lags for 3-day-old listings.
    if sym == 'CBRS':
        extras.append({'company': name, 'sub_sector': sub, 'ev_proxy_bn': 67.0})
        print(f"  {sym:6s}  {name:25s}  $67.0bn  (override — Day-1 close 14 May 2026)")
        continue
    try:
        info = yf.Ticker(sym).info or {}
        mc = info.get('marketCap')
        ev = info.get('enterpriseValue')
        val = ev if ev else mc
        if val:
            val_bn = round(val / 1e9, 1)
            extras.append({'company': name, 'sub_sector': sub, 'ev_proxy_bn': val_bn})
            print(f"  {sym:6s}  {name:25s}  ${val_bn}bn")
        else:
            print(f"  {sym:6s}  {name:25s}  no data")
    except Exception as e:
        print(f"  {sym:6s}  ERR {e}")

df = pd.concat([df, pd.DataFrame(extras)], ignore_index=True)

print(f"Companies in treemap: {len(df)}\n")
summary = df.groupby('sub_sector').agg(
    ev=('ev_proxy_bn', 'sum'),
    n=('company', 'count'),
).reset_index().sort_values('ev', ascending=False)
print(summary.to_string(index=False))

# Display label: company name + EV (formatted)
def fmt(v):
    if v >= 1000:
        return f"${v/1000:.2f}T"
    if v >= 10:
        return f"${v:.0f}B"
    return f"${v:.1f}B"

df['leaf_label'] = df.apply(lambda r: f"{r['company']}<br>{fmt(r['ev_proxy_bn'])}", axis=1)

fig = px.treemap(
    df,
    path=[px.Constant('AI sector'), 'sub_sector', 'leaf_label'],
    values='ev_proxy_bn',
    color='sub_sector',
    color_discrete_map=SUB_SECTOR_COLORS,
)

fig.update_traces(
    root_color='#FFFCF0',
    textfont=dict(family='Inter, sans-serif', color='#100F0F', size=13),
    marker=dict(line=dict(color='#FFFCF0', width=2)),
    textposition='middle center',
    hovertemplate='<b>%{label}</b><br>EV: $%{value:,.1f}bn<extra></extra>',
)

fig.update_layout(
    paper_bgcolor='#FFFCF0',
    plot_bgcolor='#FFFCF0',
    margin=dict(t=110, l=20, r=20, b=70),
    title=dict(
        text='AI sector — enterprise value by sub-sector and company',
        font=dict(family='Inter, sans-serif', color='#100F0F', size=20),
        x=0.02, xanchor='left', y=0.96,
    ),
    annotations=[
        dict(
            text=("EV from Yahoo Finance for listed; market cap proxy for unlisted/pending "
                  "(Anthropic $350bn, SpaceX $1,500bn, Databricks $62bn). "
                  "TSMC corrected via Taipei listing. Sovereigns excluded."),
            xref='paper', yref='paper',
            x=0.02, y=0.99,
            xanchor='left', yanchor='top',
            showarrow=False,
            font=dict(family='Inter, sans-serif', color='#6F6E69', size=11),
            align='left',
        ),
        dict(
            text='Source: ITK Research  ·  May 2026',
            xref='paper', yref='paper',
            x=0.98, y=-0.04,
            xanchor='right', yanchor='top',
            showarrow=False,
            font=dict(family='Inter, sans-serif', color='#6F6E69', size=10),
        ),
    ],
)

out = HERE / 'ev_treemap_2026-05-17.png'
fig.write_image(str(out), width=1600, height=1000, scale=2)
print(f"\nWrote {out}")
