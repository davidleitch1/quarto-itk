"""Build matrix heatmap of AI sector contractual commitments.

Schema (contracts.csv):
  payer            string  — counterparty putting money/capacity in
  recipient        string  — counterparty receiving
  flow_type        string  — one of: equity, debt, lease, compute, license_royalty, vendor_financing
  amount_usd_bn    float   — point estimate, $bn
  amount_low_bn    float   — low end of range when value is a range
  amount_high_bn   float   — high end of range when value is a range
  term_years       float   — contract length in years; blank for one-off
  signed_date      ISO     — YYYY-MM-DD
  status           string  — signed | loi | announced | reported | disclosed_aggregate
  source_key       string  — short key into sources.md
  notes            string  — free text; commas need quoting

Run: python3 make_heatmap.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Flexoki Light palette
PAPER = '#FFFCF0'
BLACK = '#100F0F'
TEXT = '#403E3C'
MUTED = '#6F6E69'
UI_BORDER = '#B7B5AC'
BLUE = '#205EA6'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', '-apple-system', 'Helvetica Neue', 'Arial']

HERE = Path(__file__).parent
df = pd.read_csv(HERE / 'contracts.csv')

# Operating-entity heatmap: drop financing-only counterparties (bond market, private credit,
# internal SPVs, VC pools, acquisition targets, JVs, sovereign and Musk-empire equity vehicles)
# — they crowd the matrix without adding to the circular-flow narrative; their flows live in
# the financing matrix. Tesla's only operating tie is $0.43bn of Megapacks from xAI — too
# small to show against $300bn cells; documented in CSV.
EXCLUDE = {
    'Bond market', 'Apollo+Blackstone', 'Apollo', 'Humain',
    'Meta Hyperion SPV', 'Valor Compute Infra LP',
    'Series C investors', 'Series D investors',
    'Sept 2025 investors', 'Series E investors',
    'SpaceX', 'Tesla',
    'Solaris JV', 'xAI+Humain JV',
    'X (Twitter)',
}
op = df[~df['payer'].isin(EXCLUDE) & ~df['recipient'].isin(EXCLUDE)].copy()

# Normalise the Anthropic→SpaceX/xAI Colossus-1 lease so it lands in the xAI column
op.loc[op['recipient'] == 'SpaceX/xAI', 'recipient'] = 'xAI'

matrix = op.pivot_table(
    values='amount_usd_bn',
    index='payer',
    columns='recipient',
    aggfunc='sum',
    fill_value=0,
)

# Role-driven order — chipmaker / hyperscalers (cap providers) at top-left,
# AI labs and neocloud (cap recipients / compute sellers) at bottom-right.
order = ['Nvidia', 'AMD', 'Broadcom', 'Microsoft', 'Alphabet', 'Amazon', 'Meta',
         'Oracle', 'CoreWeave', 'Dell',
         'OpenAI', 'Anthropic', 'xAI']
order = [e for e in order if e in matrix.index or e in matrix.columns]
matrix = matrix.reindex(index=order, columns=order, fill_value=0)

n = matrix.shape[0]
fig, ax = plt.subplots(figsize=(12.5, 10.8))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

cmap = mcolors.LinearSegmentedColormap.from_list('flexoki_blue', [PAPER, BLUE])
vmax = matrix.values.max()
norm = mcolors.PowerNorm(gamma=0.45, vmin=0, vmax=vmax)
ax.imshow(matrix.values, cmap=cmap, norm=norm, aspect='equal')

# Cell annotations
for i in range(n):
    for j in range(n):
        v = matrix.iloc[i, j]
        if v > 0:
            text_color = PAPER if norm(v) > 0.55 else BLACK
            label = f'{v:,.0f}' if v >= 10 else f'{v:.1f}'
            ax.text(j, i, label, ha='center', va='center',
                    color=text_color, fontsize=11, fontweight='bold')

# Marginal totals — render OUTSIDE the colour-scaled imshow region so they
# don't get washed out by the colormap and don't dominate cell-level encoding.
row_totals = matrix.sum(axis=1)
col_totals = matrix.sum(axis=0)
grand_total = float(matrix.values.sum())

# Tick labels — column labels on top, x rotated 45° rising up-right
ax.set_xticks(range(n))
ax.set_xticklabels(matrix.columns, rotation=45, ha='left', color=TEXT, fontsize=10)
ax.xaxis.tick_top()
ax.set_yticks(range(n))
ax.set_yticklabels(matrix.index, color=TEXT, fontsize=10)

# Extend limits to make room for a marginal row + column (with a small gap)
ax.set_xlim(-0.7, n + 1.4)
ax.set_ylim(n + 1.4, -0.7)

# Thin divider lines separating the colour-scaled matrix from the totals area
ax.plot([n, n], [-0.5, n + 0.9], color=UI_BORDER, linewidth=0.6, clip_on=False)
ax.plot([-0.5, n + 0.9], [n, n], color=UI_BORDER, linewidth=0.6, clip_on=False)

# Row totals (right column = contracted outflows for each payer)
for i, v in enumerate(row_totals):
    if v > 0:
        ax.text(n + 0.5, i, f'{v:,.0f}', ha='center', va='center',
                color=BLACK, fontsize=11, fontweight='bold')

# Column totals (bottom row = contracted inflows for each recipient)
for j, v in enumerate(col_totals):
    if v > 0:
        ax.text(j, n + 0.5, f'{v:,.0f}', ha='center', va='center',
                color=BLACK, fontsize=11, fontweight='bold')

# Grand-total cell
ax.text(n + 0.5, n + 0.5, f'{grand_total:,.0f}', ha='center', va='center',
        color=BLACK, fontsize=12, fontweight='bold')

# Compact headers for the marginal axes
ax.text(n + 0.5, -0.95, 'Contracted\noutflows',
        ha='center', va='bottom', color=MUTED, fontsize=9,
        fontweight='bold', fontstyle='italic')
ax.text(-0.95, n + 0.5, 'Contracted\ninflows',
        ha='right', va='center', color=MUTED, fontsize=9,
        fontweight='bold', fontstyle='italic')

# Faint gridlines between cells (Flexoki ui_border)
ax.set_xticks(np.arange(n + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(n + 1) - 0.5, minor=True)
ax.grid(which='minor', color=UI_BORDER, linewidth=0.5)
ax.tick_params(which='minor', length=0)
ax.tick_params(length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

# Title block (figure-level)
fig.text(0.02, 0.97, 'AI sector — committed dollar flows between counterparties',
         ha='left', va='top', color=BLACK, fontsize=15, fontweight='bold')
fig.text(0.02, 0.935,
         'Forward contractual commitments, $bn  •  row pays column  •  16 May 2026',
         ha='left', va='top', color=MUTED, fontsize=11)

# Footer / attribution
fig.text(0.99, 0.01,
         "Source: see ai_finance/sources.md  •  blanks = no public dollar figure  •  "
         "xAI chip purchases via xAI+Humain JV (up to 600k Blackwell) excluded — no $ disclosed",
         ha='right', va='bottom', color=MUTED, fontsize=8, style='italic')

plt.tight_layout(rect=[0, 0.03, 1, 0.91])

out_path = HERE / 'contracts_matrix_2026-05-16.png'
plt.savefig(out_path, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'Wrote {out_path}')
print(f'Matrix shape: {matrix.shape}; row totals: {matrix.sum(axis=1).to_dict()}')
print(f'Column totals: {matrix.sum(axis=0).to_dict()}')
