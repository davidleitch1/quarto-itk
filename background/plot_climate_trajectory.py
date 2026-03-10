"""
Render the QLD climate projections table as a styled PNG using plottable.
Flexoki Light theme, Tufte-style minimal lines, colour-coded confidence column.
"""

import matplotlib.pyplot as plt
import pandas as pd
from plottable import Table, ColumnDefinition

# ── Flexoki Light theme ──
BG        = '#FFFCF0'
FG        = '#100F0F'
TEXT      = '#403E3C'
MUTED     = '#6F6E69'
UI        = '#E6E4D9'
UI_BORDER = '#B7B5AC'
RED       = '#AF3029'
ORANGE    = '#BC5215'
BLUE      = '#205EA6'
CYAN      = '#24837B'
GREEN     = '#66800B'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica Neue', 'Helvetica', 'Arial']
plt.rcParams['text.color'] = TEXT

# ── Confidence colour map ──
CONFIDENCE_COLORS = {
    'Very high': RED,
    'High': ORANGE,
    'Medium': BLUE,
}

# ── Data ──
data = {
    'Aspect': [
        'Extreme rainfall intensity',
        'Drought severity',
        'Cyclone intensity',
        'Cyclone tracks',
        'Marine heatwaves',
        'Dry season rainfall',
        'Sea level',
    ],
    'Direction': [
        '+15%/\u00b0C',
        '+40% from warming',
        'Increasing (Cat 4\u20135 share)',
        'Moving south',
        'More frequent, longer',
        'Decreasing',
        'Rising, accelerating (4 cm/decade)',
    ],
    'Confidence': [
        'High',
        'High',
        'Medium',
        'Medium',
        'High',
        'Medium',
        'Very high',
    ],
    'Implication for Costs': [
        'Worse flooding per event',
        'Greater agricultural losses',
        'Higher per-event damage',
        'New exposure for SEQ',
        'Accelerating GBR decline',
        'Extended fire seasons, water stress',
        'Compound coastal flooding',
    ],
}

df = pd.DataFrame(data)

# ── Figure ──
fig, ax = plt.subplots(figsize=(14, 5.2))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# ── Title ──
fig.text(
    0.5, 0.95,
    "Queensland\u2019s Climate Trajectory",
    ha='center', va='top',
    fontsize=20, fontweight='bold', color=FG,
)

# ── Column definitions ──
# 'Aspect' will be used as index_col, so its ColumnDefinition uses that name
col_defs = [
    ColumnDefinition(
        name='Aspect',
        title='Aspect',
        width=1.5,
        textprops={'ha': 'left', 'fontsize': 11, 'color': FG, 'fontweight': 'bold'},
    ),
    ColumnDefinition(
        name='Direction',
        title='Direction',
        width=2.0,
        textprops={'ha': 'left', 'fontsize': 11, 'color': TEXT},
    ),
    ColumnDefinition(
        name='Confidence',
        title='Confidence',
        width=0.8,
        textprops={'ha': 'left', 'fontsize': 11, 'fontweight': 'bold'},
    ),
    ColumnDefinition(
        name='Implication for Costs',
        title='Implication for Costs',
        width=1.8,
        textprops={'ha': 'left', 'fontsize': 11, 'color': TEXT, 'style': 'italic'},
    ),
]

# ── Build table ──
tab = Table(
    df,
    ax=ax,
    index_col='Aspect',
    column_definitions=col_defs,
    textprops={'fontsize': 11, 'color': TEXT, 'ha': 'left'},
    col_label_cell_kw={'facecolor': BG, 'edgecolor': BG},
    cell_kw={'facecolor': BG, 'edgecolor': BG},
    col_label_divider=True,
    col_label_divider_kw={'color': FG, 'linewidth': 1.5},
    row_dividers=True,
    row_divider_kw={'color': UI_BORDER, 'linewidth': 0.4},
    footer_divider=True,
    footer_divider_kw={'color': FG, 'linewidth': 1.0},
    even_row_color=None,
    odd_row_color=None,
)

# ── Colour-code the Confidence column ──
conf_col = tab.get_column('Confidence')
for cell in conf_col.cells:
    text_val = cell.content
    colour = CONFIDENCE_COLORS.get(text_val, TEXT)
    cell.text.set_color(colour)

# ── Style column headers ──
for cell in tab.col_label_row.cells:
    cell.text.set_fontweight('bold')
    cell.text.set_fontsize(12)
    cell.text.set_color(MUTED)

# ── Attribution ──
fig.text(
    0.97, 0.03,
    'Source: CSIRO/BoM State of the Climate 2024, IPCC AR6, QLD Future Climate Science Program.',
    ha='right', va='bottom',
    fontsize=8.5, color=MUTED, style='italic',
)

# ── Save ──
outpath = (
    '/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/'
    'snakeplay/itk_articles/background/qld_climate_trajectory.png'
)
plt.savefig(outpath, dpi=300, facecolor=BG, edgecolor='none', bbox_inches='tight',
            pad_inches=0.4)
plt.close()
print(f'Saved to {outpath}')
