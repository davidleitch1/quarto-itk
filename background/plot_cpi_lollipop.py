"""
Horizontal lollipop chart: Top 10 CPI sub-groups by cumulative change,
decade to Dec 2025. All Groups CPI as vertical reference line.

Data: ABS Cat 6401.0 CPI index numbers, weighted average of eight capital cities.
Period: Dec 2015 to Dec 2025 (10 years).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── Flexoki Light palette ─────────────────────────────────────────────
BG       = "#FFFCF0"
FG       = "#100F0F"
TEXT     = "#403E3C"
MUTED    = "#6F6E69"
UI       = "#E6E4D9"
UI_BDR   = "#B7B5AC"
BLUE     = "#205EA6"
ORANGE   = "#BC5215"
CYAN     = "#24837B"
RED      = "#AF3029"
MAGENTA  = "#A02F6F"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Inter", "Helvetica Neue", "Arial", "sans-serif"],
    "text.color": FG,
    "text.parse_math": False,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
})

# ── Data from ABS API (2015-Q4 to 2025-Q4) ───────────────────────────
# Curated top 10 + All Groups reference
# Using expenditure classes (not groups that double-count)
data = [
    ("Tobacco",              201.9),
    ("Insurance",             72.6),
    ("Gas & other fuels",     67.2),
    ("Automotive fuel",       48.4),
    ("Health",                43.8),
    ("Education",             42.1),
    ("Housing",               38.7),
    ("Food & beverages",      33.9),
    ("Transport",             31.7),
    ("Child care",            29.5),
]

all_groups_pct = 33.3  # All groups CPI reference

# Sort ascending for horizontal chart (top = highest)
data.sort(key=lambda x: x[1])
labels = [d[0] for d in data]
values = [d[1] for d in data]

# ── Colour: red for Insurance, orange if above All Groups, blue if below
def pick_color(label, val):
    if label == "Insurance":
        return MAGENTA
    return ORANGE if val > all_groups_pct else BLUE

colors = [pick_color(l, v) for l, v in zip(labels, values)]

# ── Build chart ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# Remove spines and grid
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(False)

y_pos = range(len(labels))

# Lollipop stems
ax.hlines(y_pos, 0, values, color=UI_BDR, linewidth=1.2, zorder=1)

# Lollipop dots
ax.scatter(values, y_pos, color=colors, s=120, zorder=3,
           edgecolors="white", linewidths=1.5)

# Value labels to the right of each dot
for i, (val, lbl) in enumerate(zip(values, labels)):
    ax.text(val + 2.5, i, f"+{val:.0f}%", va="center", ha="left",
            fontsize=11, fontweight="bold",
            color=pick_color(lbl, val))

# Y-axis labels — highlight Insurance
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12, color=TEXT)
for tick_label in ax.get_yticklabels():
    if tick_label.get_text() == "Insurance":
        tick_label.set_color(MAGENTA)
        tick_label.set_fontweight("bold")
ax.tick_params(axis="y", length=0, pad=8)
ax.tick_params(axis="x", colors=MUTED, length=0)

# X-axis
ax.set_xlim(-5, 225)
ax.xaxis.set_major_formatter(mticker.FormatStrFormatter("+%.0f%%"))
for label in ax.get_xticklabels():
    label.set_color(MUTED)
    label.set_fontsize(9)

# All Groups CPI reference line
ax.axvline(x=all_groups_pct, color=MUTED, linestyle="--", linewidth=1.5,
           alpha=0.6, zorder=2)
ax.text(all_groups_pct + 1.5, 0.3,
        f"All Groups CPI  +{all_groups_pct:.0f}%",
        va="center", ha="left", color=MUTED, fontsize=9,
        fontweight="bold")

# Title and subtitle via fig.text to avoid overlap
fig.text(0.06, 0.97,
         "CPI Growth by Category, Decade to December 2025",
         ha="left", va="top", fontsize=16, fontweight="bold", color=FG)
fig.text(0.06, 0.93,
         "Cumulative % change, weighted average of eight capital cities",
         ha="left", va="top", fontsize=11, color=MUTED)

# Attribution
fig.text(0.99, 0.01,
         "Data: ABS Cat 6401.0, CPI index numbers (Dec 2015 to Dec 2025)",
         ha="right", va="bottom", color=MUTED, fontsize=8, style="italic")

plt.tight_layout(rect=[0, 0.03, 1, 0.90])

outpath = (
    "/Users/davidleitch/Library/Mobile Documents/"
    "com~apple~CloudDocs/snakeplay/itk_articles/background/"
    "cpi_growth_by_category.png"
)
plt.savefig(outpath, dpi=200, facecolor=BG, edgecolor="none", bbox_inches="tight")
plt.close()
print(f"Saved: {outpath}")
