"""
China heavy-truck electrification policy — Flexoki info-box (callout card).

Left: the 2030 targets (joint plan from 11 government bodies, 13 Jun 2026).
Right: where China is now (2025 actuals).

Sources: Bloomberg, CnEVPost, CarNewsChina, Automotive World (June 2026).
Output: itk_articles/media/china_etruck_policy_box.png
"""

import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------- Flexoki theme
PAPER, INK, TEXT, MUTED = '#FFFCF0', '#100F0F', '#403E3C', '#6F6E69'
UI, UI_BORDER, TINT = '#E6E4D9', '#B7B5AC', '#F2EEDC'
RED, ORANGE, BLUE, GREEN = '#AF3029', '#BC5215', '#205EA6', '#66800B'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui',
    'Helvetica Neue', 'Arial']

fig, ax = plt.subplots(figsize=(12, 7.4))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# --- header band ---
ax.add_patch(Rectangle((2, 85), 96, 13, facecolor=RED, edgecolor='none'))
ax.text(5, 92.6, "China mandates 40% electric heavy trucks by 2030",
        ha='left', va='center', color='white', fontsize=20, fontweight='bold')
ax.text(5, 87.6,
        "Joint implementation plan — 11 government bodies (Ministry of "
        "Transport lead)  ·  announced 13 June 2026",
        ha='left', va='center', color='white', fontsize=10.5, alpha=0.92)

# --- bottom comparison strip ---
ax.add_patch(Rectangle((2, 2), 96, 11, facecolor=TINT, edgecolor='none'))
ax.text(5, 9.2, 'For comparison', ha='left', va='center', color=ORANGE,
        fontsize=10, fontweight='bold')
ax.text(5, 5.6,
        "Australia has no CO₂ emissions standard for road vehicles over "
        "4.5 tonnes — no mandate or pricing signal on truck diesel.",
        ha='left', va='center', color=TEXT, fontsize=11)

# --- outer border + column divider ---
ax.add_patch(Rectangle((2, 2), 96, 96, facecolor='none',
                       edgecolor=UI_BORDER, linewidth=1.5))
ax.plot([51, 51], [16, 81], color=UI_BORDER, linewidth=1)

# ============================================================ LEFT: the targets
ax.text(5, 79, 'THE 2030 TARGETS', ha='left', va='top', color=RED,
        fontsize=12.5, fontweight='bold')

bullets = [
    "40% of new heavy-truck sales to be new-energy (battery or fuel-cell)",
    "Fleet of >1.6 million NEV heavy trucks — about 20% of the heavy-truck "
    "fleet, carrying ~18% of highway freight",
    ">80% electrification of fixed short-haul routes in priority regions "
    "(Beijing–Tianjin–Hebei, Fenwei Plain)",
    "30,000 km of “zero-carbon freight corridors”; ~3,000 heavy-truck "
    "charging & battery-swap stations",
]

y = 73
for b in bullets:
    ax.text(6.5, y, '•', ha='left', va='top', color=ORANGE, fontsize=15,
            fontweight='bold')
    lines = textwrap.wrap(b, width=46)
    ax.text(9.5, y, '\n'.join(lines), ha='left', va='top', color=TEXT,
            fontsize=11.5, linespacing=1.35)
    y -= 4.0 + 3.6 * (len(lines) - 1)

# ===================================================== RIGHT: where China is now
ax.text(55, 79, 'WHERE CHINA IS NOW (2025)', ha='left', va='top', color=RED,
        fontsize=12.5, fontweight='bold')

stats = [
    ('~29%', BLUE, 'full-year new-energy share of heavy-truck sales in 2025'),
    ('~231,000', ORANGE, 'NEV heavy trucks sold in 2025  (+182% on 2024)'),
]

y = 66
for num, col, desc in stats:
    ax.text(55, y, num, ha='left', va='top', color=col, fontsize=33,
            fontweight='bold')
    ax.text(55, y - 9.0, '\n'.join(textwrap.wrap(desc, width=40)),
            ha='left', va='top', color=TEXT, fontsize=11, linespacing=1.3)
    y -= 22

# --- attribution ---
fig.text(0.985, 0.012,
         "Sources: Bloomberg; CnEVPost; CarNewsChina; Automotive World, "
         "June 2026  ·  ITK",
         ha='right', va='bottom', color=MUTED, fontsize=8, style='italic')

plt.tight_layout()
OUT = Path(__file__).resolve().parent.parent / 'media' / 'china_etruck_policy_box.png'
plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'saved {OUT}')
