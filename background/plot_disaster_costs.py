"""
Two-panel chart: Australian disaster costs — historical ICA data + QLD projections.
Left: National insured losses by financial year (ICA catastrophe declarations)
Right: Projected QLD total economic disaster costs at 6% growth to 2050
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Flexoki Light theme ──
BG       = '#FFFCF0'
FG       = '#100F0F'
TEXT     = '#403E3C'
MUTED    = '#6F6E69'
UI       = '#E6E4D9'
UI_BORDER = '#B7B5AC'
BLUE     = '#205EA6'
ORANGE   = '#BC5215'
CYAN     = '#24837B'
RED      = '#AF3029'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', '-apple-system', 'BlinkMacSystemFont',
                                    'Segoe UI', 'system-ui', 'Helvetica Neue', 'Arial']

# ── LEFT PANEL DATA ──
# National insured catastrophe losses by financial year (A$ billion)
# Sources: ICA catastrophe declarations, ICA annual reports, reinsurance media
# Confirmed data points: FY23-24 ($2.2B), FY24-25 ($1.97B), major events as noted
# Other years: author estimates from declared catastrophe event costs

fy_labels = [
    "FY11", "FY12", "FY13", "FY14", "FY15",
    "FY16", "FY17", "FY18", "FY19", "FY20",
    "FY21", "FY22", "FY23", "FY24", "FY25"
]

# Annual national insured catastrophe losses ($B)
losses = [
    4.8,   # FY10-11: QLD floods ($3.5B) + TC Yasi + Perth storms
    1.1,   # FY11-12
    1.3,   # FY12-13
    1.5,   # FY13-14: NSW bushfires
    1.8,   # FY14-15: Brisbane hail ($1.4B)
    1.2,   # FY15-16
    3.0,   # FY16-17: TC Debbie ($1.74B) + other
    1.3,   # FY17-18
    2.0,   # FY18-19: NQ Monsoon ($1.24B) + other
    4.5,   # FY19-20: Black Summer ($1.87B) + Melbourne hail
    1.5,   # FY20-21
    6.5,   # FY21-22: East Coast floods ($5.56B) + other
    2.5,   # FY22-23
    2.2,   # FY23-24: ICA confirmed
    2.0,   # FY24-25: ICA confirmed (~$1.97B)
]

# Event annotations (index, label, offset_y)
events = {
    0:  ('Floods +\nTC Yasi', 0.3),
    6:  ('TC\nDebbie', 0.3),
    9:  ('Black\nSummer', 0.3),
    11: ('East Coast\nFloods', 0.3),
}

# ── RIGHT PANEL DATA ──
years_proj = np.arange(2025, 2051)
baseline_cost = 5.0       # QLD total economic disaster costs, current ($B)
cost_growth = 0.06        # 6% nominal (ICA observed rate)
gsp_2025 = 531.0          # Nominal GSP ($B)
gsp_growth = 0.045        # 4.5% nominal (2.5% real + 2% inflation)

projected_cost = baseline_cost * (1 + cost_growth) ** (years_proj - 2025)
projected_gsp = gsp_2025 * (1 + gsp_growth) ** (years_proj - 2025)
pct_of_gsp = (projected_cost / projected_gsp) * 100

# ── BUILD FIGURE ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7.5),
                                gridspec_kw={'width_ratios': [1.1, 1]})
fig.patch.set_facecolor(BG)

# Suptitle
fig.suptitle('The Rising Cost of Disasters', fontsize=18, fontweight='bold',
             color=FG, y=0.97)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEFT PANEL: Historical ICA insured losses
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ax1.set_facecolor(BG)
for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.grid(False)

# Bars — highlight extreme years in orange
bar_colors = [ORANGE if v >= 4.0 else BLUE for v in losses]
bars = ax1.bar(range(len(fy_labels)), losses, color=bar_colors, width=0.7, alpha=0.9)

# 30-year average line
avg_30yr = 2.1
ax1.axhline(y=avg_30yr, color=MUTED, linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(14.3, avg_30yr + 0.15, '30-yr avg\n$2.1B', ha='right', va='bottom',
         color=MUTED, fontsize=8.5, style='italic', linespacing=1.2)

# 5-year average line (more recent)
avg_5yr = np.mean(losses[-5:])
ax1.axhline(y=avg_5yr, color=ORANGE, linestyle=':', linewidth=1.5, alpha=0.5)
ax1.text(14.3, avg_5yr + 0.15, f'5-yr avg\n${avg_5yr:.1f}B', ha='right', va='bottom',
         color=ORANGE, fontsize=8.5, style='italic', alpha=0.8, linespacing=1.2)

# Event labels
for idx, (label, offset) in events.items():
    ax1.text(idx, losses[idx] + offset, label,
             ha='center', va='bottom', color=TEXT, fontsize=7.5,
             fontweight='bold', linespacing=1.1)

# Axes
ax1.set_xticks(range(len(fy_labels)))
ax1.set_xticklabels(fy_labels, rotation=45, ha='right', fontsize=9)
ax1.tick_params(colors=MUTED, length=0)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_color(TEXT)

ax1.set_ylabel('Insured Catastrophe Losses ($B)', color=TEXT, fontsize=11, labelpad=10)
ax1.set_title('National Insured Catastrophe Losses (ICA)', color=FG, fontsize=13,
              fontweight='bold', pad=12)
ax1.set_ylim(0, 8.5)
ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0fB'))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RIGHT PANEL: QLD projected total economic costs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ax2.set_facecolor(BG)
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.grid(False)

# Area fill + line
ax2.fill_between(years_proj, projected_cost, alpha=0.12, color=ORANGE)
ax2.plot(years_proj, projected_cost, color=ORANGE, linewidth=2.5)

# Current level reference line
ax2.axhline(y=baseline_cost, color=MUTED, linestyle=':', linewidth=1.0, alpha=0.5)
ax2.text(2050.5, baseline_cost + 0.2, 'Current level', ha='right', va='bottom',
         color=MUTED, fontsize=8, style='italic')

# Key point annotations
key_points = [
    (2025, 0.94, (12, -15)),
    (2035, None, (12, 5)),
    (2050, None, (-80, 12)),
]

for yr, _, xytext in key_points:
    idx = yr - 2025
    cost = projected_cost[idx]
    pct = pct_of_gsp[idx]
    gsp_val = projected_gsp[idx]

    ax2.scatter([yr], [cost], color=ORANGE, s=80, zorder=5,
                edgecolors='white', linewidths=1.5)
    ax2.annotate(
        f'${cost:.0f}B\n{pct:.1f}% of GSP',
        (yr, cost),
        textcoords='offset points', xytext=xytext,
        color=ORANGE, fontsize=10, fontweight='bold',
        linespacing=1.3,
        arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.8)
            if yr == 2050 else None
    )

# Secondary y-axis for % of GSP
ax2_r = ax2.twinx()
ax2_r.set_facecolor(BG)
for spine in ax2_r.spines.values():
    spine.set_visible(False)
ax2_r.plot(years_proj, pct_of_gsp, color=CYAN, linewidth=1.8, linestyle='--', alpha=0.7)
ax2_r.set_ylabel('% of GSP', color=CYAN, fontsize=10, labelpad=10)
ax2_r.tick_params(colors=CYAN, length=0)
for label in ax2_r.get_yticklabels():
    label.set_color(CYAN)
    label.set_fontsize(9)
ax2_r.set_ylim(0.5, 2.0)

# Legend for right panel
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=ORANGE, linewidth=2.5, label='Total economic cost ($B)'),
    Line2D([0], [0], color=CYAN, linewidth=1.8, linestyle='--', alpha=0.7, label='% of GSP'),
]
ax2.legend(handles=legend_elements, loc='upper left', facecolor=BG,
           edgecolor='none', labelcolor=FG, fontsize=9, framealpha=0.8)

# Axes
ax2.tick_params(colors=MUTED, length=0)
for label in ax2.get_xticklabels() + ax2.get_yticklabels():
    label.set_color(TEXT)
    label.set_fontsize(9)

ax2.set_ylabel('Total Economic Cost ($B/yr)', color=TEXT, fontsize=11, labelpad=10)
ax2.set_title('Projected QLD Disaster Costs (6% growth)', color=FG, fontsize=13,
              fontweight='bold', pad=12)
ax2.set_ylim(0, 28)
ax2.set_xlim(2024, 2051)
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0fB'))
ax2.xaxis.set_major_locator(mticker.MultipleLocator(5))

# ── Attribution ──
fig.text(0.99, 0.01,
         "Data: ICA Declared Catastrophes (insured losses only; excludes sub-threshold events); Author projections at ICA observed growth rate. "
         "GSP at 4.5% nominal.",
         ha='right', va='bottom', color=MUTED, fontsize=8, style='italic')

fig.text(0.01, 0.01,
         "Note: FY annual totals are author estimates from ICA declared events. "
         "Total economic cost = insured × 2.5 (incl. uninsured, infrastructure, indirect).",
         ha='left', va='bottom', color=MUTED, fontsize=7.5, style='italic')

plt.tight_layout(rect=[0, 0.04, 1, 0.94])

outpath = '/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/itk_articles/background/disaster_costs_projection.png'
plt.savefig(outpath, dpi=150, facecolor=BG, edgecolor='none', bbox_inches='tight')
plt.close()
print(f"Saved to {outpath}")
