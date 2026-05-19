"""Stacked-bar chart of equity (market cap) + gross debt by AI sub-sector.

Sub-sectors are aggregated from the finer `sub_segment` field in companies.csv.
Sovereign wealth excluded (no public equity/debt as fund types).

Run: python3 make_capital_structure.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

HERE = Path(__file__).parent

# Flexoki Light
PAPER = '#FFFCF0'
INK = '#100F0F'
TEXT = '#403E3C'
MUTED = '#6F6E69'
BLUE = '#205EA6'      # equity
ORANGE = '#BC5215'    # GAAP debt
RED = '#AF3029'       # off-balance-sheet leases
MAGENTA = '#A02F6F'   # forward vendor commits
UI_BORDER = '#B7B5AC'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', '-apple-system', 'Helvetica Neue', 'Arial']
plt.rcParams['text.parse_math'] = False

# Sub-segment → sub-sector aggregation
SUB_SECTOR_MAP = {
    'GPU_accelerator':           'GPU & accelerators',
    'custom_silicon':            'Custom silicon + networking',
    'networking_silicon':        'Custom silicon + networking',
    'foundry':                   'Foundry',
    'HBM_memory':                'HBM memory',
    'HBM_memory_foundry':        'HBM memory',
    'hyperscaler':               'Hyperscalers',
    'neocloud':                  'Neoclouds',
    'dc_reit':                   'DC REITs / developers',
    'dc_developer':              'DC REITs / developers',
    'ai_server_oem':             'AI server OEMs',
    'frontier_lab':              'Frontier AI labs',
    'frontier_lab_parent':       'Frontier AI labs',
    'enterprise_saas':           'Incumbent SaaS',
    'data_ai_platform':          'AI-native SaaS',
    'ai_native_dev':             'AI-native SaaS',
    'ai_native_enterprise_search': 'AI-native SaaS',
    'ai_native_legal':           'AI-native SaaS',
    'ai_native_cs':              'AI-native SaaS',
    'ai_native_research':        'AI-native SaaS',
    'ai_native_search':          'AI-native SaaS',
    'alt_asset_mgr':             'Private credit / alt mgrs',
    'sovereign_wealth':          'Sovereign wealth (excluded)',
}

df = pd.read_csv(HERE / 'companies.csv')
df['sub_sector'] = df['sub_segment'].map(SUB_SECTOR_MAP)

# Vendor compute commitments — derive from contracts.csv (operating compute flows)
contracts = pd.read_csv(HERE / 'contracts.csv')
compute = contracts[(contracts['flow_type'] == 'compute')
                   & contracts['amount_usd_bn'].notna()].copy()

# Map contract-payer names to chart sub_sectors
PAYER_TO_SUBSECTOR = {
    'OpenAI':         'Frontier AI labs',
    'Anthropic':      'Frontier AI labs',
    'xAI':            'Frontier AI labs',
    'SpaceX':         'Frontier AI labs',
    'SpaceX/xAI':     'Frontier AI labs',
    'xAI+Humain JV':  'Frontier AI labs',
    'Microsoft':      'Hyperscalers',
    'Alphabet':       'Hyperscalers',
    'Amazon':         'Hyperscalers',
    'Meta':           'Hyperscalers',
    'Meta Platforms': 'Hyperscalers',
    'Oracle':         'Hyperscalers',
}
compute['sub_sector'] = compute['payer'].map(PAYER_TO_SUBSECTOR)
vendor_commits_by_sub = compute.dropna(subset=['sub_sector']).groupby('sub_sector')['amount_usd_bn'].sum()
print("Vendor compute commitments by sub-sector (from contracts.csv):")
for sub, val in vendor_commits_by_sub.items():
    print(f"  {sub:25s}  ${val:>7,.0f}bn")

# Aggregate by sub_sector — NaN treated as 0 in sum
agg = df.groupby('sub_sector', dropna=False).agg(
    equity=('mkt_cap_usd_bn', 'sum'),
    debt=('debt_usd_bn', 'sum'),
    leased=('leased_usd_bn', 'sum'),
    n_companies=('company', 'count'),
).reset_index()
agg['vendor_commits'] = agg['sub_sector'].map(vendor_commits_by_sub).fillna(0)
agg['total'] = agg['equity'] + agg['debt'] + agg['leased'] + agg['vendor_commits']
agg = agg[agg['sub_sector'] != 'Sovereign wealth (excluded)']
agg = agg[agg['total'] > 0]
agg = agg.sort_values('total', ascending=False).reset_index(drop=True)

print("\nSub-sector aggregates (sorted by total capital + obligations):")
for _, r in agg.iterrows():
    print(f"  {r['sub_sector']:32s}  n={r['n_companies']:>2}  equity ${r['equity']:>7,.0f}bn  debt ${r['debt']:>6,.0f}bn  OBS-lease ${r['leased']:>5,.0f}bn  vendor-commits ${r['vendor_commits']:>6,.0f}bn  total ${r['total']:>7,.0f}bn")

# Plot
fig, ax = plt.subplots(figsize=(13.5, 7.5))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

y = range(len(agg))
ax.barh(y, agg['equity'], color=BLUE,
        label='Equity (market cap)', edgecolor='none', height=0.7)
ax.barh(y, agg['debt'], left=agg['equity'], color=ORANGE,
        label='Debt (gross, GAAP)', edgecolor='none', height=0.7)
ax.barh(y, agg['leased'], left=agg['equity'] + agg['debt'], color=RED,
        label='OBS leases (ITK est, Big-5)', edgecolor='none', height=0.7)
ax.barh(y, agg['vendor_commits'],
        left=agg['equity'] + agg['debt'] + agg['leased'], color=MAGENTA,
        label='Forward vendor commits', edgecolor='none', height=0.7)

ax.set_yticks(y)
ax.set_yticklabels(agg['sub_sector'], color=TEXT, fontsize=11)
ax.invert_yaxis()

x_max = agg['total'].max()
label_pad = x_max * 0.012

for i, row in agg.iterrows():
    eq, dt, ls, vc, tot = row['equity'], row['debt'], row['leased'], row['vendor_commits'], row['total']
    if eq > x_max * 0.04:
        ax.text(eq / 2, i, f"{eq:,.0f}",
                ha='center', va='center', color=PAPER, fontsize=10, fontweight='bold')
    if dt > x_max * 0.03:
        ax.text(eq + dt / 2, i, f"{dt:,.0f}",
                ha='center', va='center', color=PAPER, fontsize=10, fontweight='bold')
    if ls > x_max * 0.03:
        ax.text(eq + dt + ls / 2, i, f"{ls:,.0f}",
                ha='center', va='center', color=PAPER, fontsize=10, fontweight='bold')
    if vc > x_max * 0.03:
        ax.text(eq + dt + ls + vc / 2, i, f"{vc:,.0f}",
                ha='center', va='center', color=PAPER, fontsize=10, fontweight='bold')
    # Total at right end + company count
    ax.text(tot + label_pad, i, f"{tot:,.0f}  ({int(row['n_companies'])})",
            ha='left', va='center', color=INK, fontsize=10, fontweight='bold')

ax.set_xlim(0, x_max * 1.18)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)
ax.xaxis.set_visible(False)
ax.grid(False)

# Legend bottom-right
ax.legend(loc='lower right', facecolor=PAPER, edgecolor='none', fontsize=10,
          labelcolor=INK, framealpha=0.9)

# Title block
fig.text(0.02, 0.96, 'AI sector capital structure by sub-sector',
         ha='left', va='top', color=INK, fontsize=16, fontweight='bold')
fig.text(0.02, 0.92,
         'Equity (market cap) + GAAP debt + OBS leases + forward vendor commits, $bn  ·  '
         'sorted by total obligation  ·  (N) = company count  ·  May 2026',
         ha='left', va='top', color=MUTED, fontsize=11)

# Footnotes / source
fig.text(0.02, 0.06,
         'Equity: listed = Yahoo market cap; unlisted = SpaceX $1,500bn, Anthropic $350bn, Databricks $62bn (research).  Debt: Yahoo GAAP totalDebt.',
         ha='left', va='bottom', color=MUTED, fontsize=9, fontstyle='italic')
fig.text(0.02, 0.04,
         "OBS leases: ITK estimate splitting Moody's Feb 2026 Big-5 aggregate $662bn proportionally by 2026 capex; pending 10-K disclosure mining (task #10).",
         ha='left', va='bottom', color=MUTED, fontsize=9, fontstyle='italic')
fig.text(0.02, 0.02,
         'Vendor commits: aggregated forward compute-purchase obligations from contracts.csv (OpenAI $1.16trn, Anthropic $120bn, Meta-CoreWeave $35bn, etc.). Same dollars appear as forward revenue at the recipient sub-sector.',
         ha='left', va='bottom', color=MUTED, fontsize=9, fontstyle='italic')
fig.text(0.99, 0.02, 'Source: ITK Research',
         ha='right', va='bottom', color=MUTED, fontsize=9, fontstyle='italic')

plt.tight_layout(rect=[0, 0.10, 1, 0.90])

out = HERE / 'capital_structure_2026-05-17.png'
plt.savefig(out, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f"\nWrote {out}")
