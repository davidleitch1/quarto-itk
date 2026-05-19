"""Build matrix heatmap of AI sector financing flows.

Companion to make_heatmap.py (operating flows). This matrix filters to
financing flow types (equity, debt, lease, vendor_financing) and shows
where external capital is plugging into the operating web.

Excludes:
- compute / vendor commitments (operating; shown in main matrix)
- The xAI ↔ X all-stock acquisition (corporate combination, not financing)
- The SpaceX ↔ xAI all-stock acquisition (corporate combination, not financing)

Consolidates the four xAI VC equity rounds (Series C, D, Sept 2025, Series E)
into a single 'xAI VC pool' entity. Disaggregated detail remains in
contracts.csv.

Run: python3 make_financing_matrix.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

PAPER = '#FFFCF0'
BLACK = '#100F0F'
TEXT = '#403E3C'
MUTED = '#6F6E69'
UI_BORDER = '#B7B5AC'
BLUE = '#205EA6'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', '-apple-system', 'Helvetica Neue', 'Arial']
plt.rcParams['text.parse_math'] = False

HERE = Path(__file__).parent
df = pd.read_csv(HERE / 'contracts.csv')

# Filter to financing flow types
FINANCING_TYPES = {'equity', 'debt', 'lease', 'vendor_financing'}
fin = df[df['flow_type'].isin(FINANCING_TYPES)].copy()

# Drop all-stock acquisitions — corporate combinations, not fresh capital
def is_all_stock_acquisition(row):
    notes = str(row.get('notes', '')).lower()
    return 'all-stock' in notes and 'acquisition' in notes
fin = fin[~fin.apply(is_all_stock_acquisition, axis=1)].copy()

# Consolidate the four xAI VC rounds into a single 'xAI VC pool' label
VC_ROUNDS = {'Series C investors', 'Series D investors',
             'Sept 2025 investors', 'Series E investors'}
fin.loc[fin['payer'].isin(VC_ROUNDS), 'payer'] = 'xAI VC pool'

matrix = fin.pivot_table(
    values='amount_usd_bn', index='payer', columns='recipient',
    aggfunc='sum', fill_value=0,
)

# Order: capital providers top, financing vehicles middle, op recipients bottom
order = [
    # Capital providers
    'Bond market', 'Apollo+Blackstone', 'Apollo', 'Humain', 'xAI VC pool',
    'SpaceX', 'Tesla', 'Nvidia', 'Microsoft', 'Amazon', 'Alphabet', 'Meta',
    # Financing vehicles
    'Valor Compute Infra LP', 'Meta Hyperion SPV',
    # Operating recipients
    'Oracle', 'Broadcom', 'OpenAI', 'Anthropic', 'xAI',
]
order = [e for e in order if e in matrix.index or e in matrix.columns]
matrix = matrix.reindex(index=order, columns=order, fill_value=0)

n = matrix.shape[0]
fig, ax = plt.subplots(figsize=(15, 13))
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
                    color=text_color, fontsize=9, fontweight='bold')

# Marginal totals
row_totals = matrix.sum(axis=1)
col_totals = matrix.sum(axis=0)
grand_total = float(matrix.values.sum())

ax.set_xticks(range(n))
ax.set_xticklabels(matrix.columns, rotation=45, ha='left', color=TEXT, fontsize=9)
ax.xaxis.tick_top()
ax.set_yticks(range(n))
ax.set_yticklabels(matrix.index, color=TEXT, fontsize=9)

ax.set_xlim(-0.7, n + 1.4)
ax.set_ylim(n + 1.4, -0.7)

# Dividers between matrix and totals area
ax.plot([n, n], [-0.5, n + 0.9], color=UI_BORDER, linewidth=0.6, clip_on=False)
ax.plot([-0.5, n + 0.9], [n, n], color=UI_BORDER, linewidth=0.6, clip_on=False)

# Section dividers separating capital providers / vehicles / op recipients
section_breaks = []
if 'Valor Compute Infra LP' in order:
    section_breaks.append(order.index('Valor Compute Infra LP') - 0.5)
if 'Oracle' in order:
    section_breaks.append(order.index('Oracle') - 0.5)
for b in section_breaks:
    ax.plot([-0.5, n - 0.5], [b, b], color=UI_BORDER, linewidth=0.4,
            linestyle='--', clip_on=False)
    ax.plot([b, b], [-0.5, n - 0.5], color=UI_BORDER, linewidth=0.4,
            linestyle='--', clip_on=False)

# Row totals
for i, v in enumerate(row_totals):
    if v > 0:
        ax.text(n + 0.5, i, f'{v:,.0f}', ha='center', va='center',
                color=BLACK, fontsize=10, fontweight='bold')

# Column totals
for j, v in enumerate(col_totals):
    if v > 0:
        ax.text(j, n + 0.5, f'{v:,.0f}', ha='center', va='center',
                color=BLACK, fontsize=10, fontweight='bold')

# Grand total
ax.text(n + 0.5, n + 0.5, f'{grand_total:,.0f}', ha='center', va='center',
        color=BLACK, fontsize=12, fontweight='bold')

ax.text(n + 0.5, -0.95, 'Contracted\noutflows',
        ha='center', va='bottom', color=MUTED, fontsize=8,
        fontweight='bold', fontstyle='italic')
ax.text(-0.95, n + 0.5, 'Contracted\ninflows',
        ha='right', va='center', color=MUTED, fontsize=8,
        fontweight='bold', fontstyle='italic')

# Minor-tick gridlines
ax.set_xticks(np.arange(n + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(n + 1) - 0.5, minor=True)
ax.grid(which='minor', color=UI_BORDER, linewidth=0.4)
ax.tick_params(which='minor', length=0)
ax.tick_params(length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(0.02, 0.97, 'AI sector — financing flows',
         ha='left', va='top', color=BLACK, fontsize=15, fontweight='bold')
fig.text(0.02, 0.94,
         'External capital plugging into the operating web (equity, debt, lease)  •  '
         'excludes operating compute commitments and all-stock acquisitions  •  $bn  •  16 May 2026',
         ha='left', va='top', color=MUTED, fontsize=10)

fig.text(0.99, 0.01,
         'Source: see ai_finance/sources.md  •  '
         'xAI VC pool aggregates Series C/D/E + Sept 2025 rounds ($41bn)  •  '
         'dashed lines separate capital providers / vehicles / op recipients',
         ha='right', va='bottom', color=MUTED, fontsize=8, fontstyle='italic')

plt.tight_layout(rect=[0, 0.03, 1, 0.93])

out = HERE / 'financing_matrix_2026-05-16.png'
plt.savefig(out, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'Wrote {out}')
print(f'Matrix shape: {matrix.shape}')
print(f'Top row totals (outflows): {matrix.sum(axis=1).sort_values(ascending=False).head(8).to_dict()}')
print(f'Top col totals (inflows): {matrix.sum(axis=0).sort_values(ascending=False).head(8).to_dict()}')
