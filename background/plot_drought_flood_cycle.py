"""
Queensland's Drought-Flood Cycle in Numbers
Infographic-style callout for Quarto article on QLD disaster costs.

Flexoki Light theme, 2x2 card grid, hero numbers with context text.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── Flexoki Light palette ──────────────────────────────────────────────
BG       = "#FFFCF0"   # warm cream
TEXT_PRI = "#100F0F"    # primary text
TEXT_LBL = "#403E3C"    # label text
TEXT_MUT = "#6F6E69"    # muted text
UI_BG    = "#E6E4D9"    # card background
UI_BDR   = "#B7B5AC"    # card border

# Sector accent colours
C_ROADS  = "#205EA6"    # blue
C_CATTLE = "#BC5215"    # orange
C_FENCE  = "#24837B"    # cyan
C_WATER  = "#A02F6F"    # magenta

# ── Font setup ─────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Inter", "Helvetica Neue", "Arial", "sans-serif"],
    "text.color": TEXT_PRI,
    "text.usetex": False,
    "text.parse_math": False,    # prevent $ being treated as LaTeX math
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
})

# ── Figure ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 8), dpi=300)

# ── Title block ────────────────────────────────────────────────────────
fig.text(
    0.50, 0.960,
    "Queensland's Drought\u2013Flood Cycle in Numbers",
    ha="center", va="top",
    fontsize=22, fontweight="bold", color=TEXT_PRI,
)
fig.text(
    0.50, 0.924,
    "Drought pre-conditions the damage. Floods deliver it.",
    ha="center", va="top",
    fontsize=12, fontstyle="italic", color=TEXT_MUT,
)

# ── Attribution ────────────────────────────────────────────────────────
fig.text(
    0.97, 0.013,
    "Data: QRA, Deloitte, ABARES, QLD Government",
    ha="right", va="bottom",
    fontsize=7.5, color=UI_BDR,
)

# ── Card definitions ───────────────────────────────────────────────────
# NOTE: all text uses only ASCII or safe Unicode (en-dash \u2013, multiply \u00d7)
# Arrows use plain text to avoid missing-glyph warnings.
cards = [
    {
        "label": "ROADS",
        "accent": C_ROADS,
        "hero_lines": [
            ("70,000 km", "on black clay soils"),
            ("40%", "of all QLD roads affected"),
        ],
        "context": (
            "Drought shrinks reactive clay; flood swells it\n"
            "back again -- accelerated pavement failure.\n"
            "Drought pre-conditions the damage floods inflict."
        ),
    },
    {
        "label": "CATTLE",
        "accent": C_CATTLE,
        "hero_lines": [
            ("20\u201325\u00d7", "price swing: $68 to $1,500+/hd"),
            ("457,000", "cattle killed, Feb 2019 monsoon"),
        ],
        "context": (
            "Animals weakened by 6 years of preceding drought.\n"
            "Destocking at ~$68/head; restocking at $1,500+."
        ),
    },
    {
        "label": "FENCING",
        "accent": C_FENCE,
        "hero_lines": [
            ("20,500 km", "destroyed in 2025 floods"),
            ("$150\u2013250M", "estimated rebuild cost"),
        ],
        "context": (
            "8,500 km exclusion + 12,000 km internal fencing.\n"
            "Costs tripled in a decade: $5\u20137k/km to $15\u201320k/km.\n"
            "Govt committed $105M for exclusion fencing alone."
        ),
    },
    {
        "label": "WATER",
        "accent": C_WATER,
        "hero_lines": [
            ("$6.9B", "emergency infrastructure (drought)"),
            ("$4\u20138B", "new desal plant planned, 2035"),
        ],
        "context": (
            "Millennium Drought drove emergency spending.\n"
            "Floods then damage what was built.\n"
            "The cycle repeats at ever-higher cost."
        ),
    },
]

# ── Card layout geometry ───────────────────────────────────────────────
margin_x = 0.045
margin_top = 0.115
margin_bot = 0.050
gap_x = 0.030
gap_y = 0.035

card_w = (1.0 - 2 * margin_x - gap_x) / 2
card_h = (1.0 - margin_top - margin_bot - gap_y) / 2

positions = [
    (margin_x,                   1.0 - margin_top - card_h),
    (margin_x + card_w + gap_x,  1.0 - margin_top - card_h),
    (margin_x,                   1.0 - margin_top - 2 * card_h - gap_y),
    (margin_x + card_w + gap_x,  1.0 - margin_top - 2 * card_h - gap_y),
]


def draw_card(fig, x0, y0, w, h, card):
    """Draw a single infographic card on the figure."""
    accent = card["accent"]

    # ── Card axes ──────────────────────────────────────────────────
    ax = fig.add_axes([x0, y0, w, h])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # ── Card background (rounded rectangle) ────────────────────────
    rr = FancyBboxPatch(
        (0.015, 0.015), 0.97, 0.97,
        boxstyle="round,pad=0.025",
        facecolor=UI_BG,
        edgecolor=UI_BDR,
        linewidth=1.2,
        transform=ax.transAxes,
        zorder=0,
    )
    ax.add_patch(rr)

    # ── Accent stripe (left edge) ──────────────────────────────────
    stripe = FancyBboxPatch(
        (0.015, 0.015), 0.020, 0.97,
        boxstyle="round,pad=0.005",
        facecolor=accent,
        edgecolor="none",
        transform=ax.transAxes,
        zorder=1,
    )
    ax.add_patch(stripe)

    # ── Sector label ───────────────────────────────────────────────
    ax.text(
        0.085, 0.91,
        card["label"],
        transform=ax.transAxes,
        fontsize=15, fontweight="bold", color=accent,
        va="top", ha="left",
        zorder=2,
    )

    # ── Thin separator under label ─────────────────────────────────
    ax.plot(
        [0.085, 0.94], [0.835, 0.835],
        transform=ax.transAxes,
        color=UI_BDR, linewidth=0.7, zorder=2,
    )

    # ── Hero numbers + descriptors ─────────────────────────────────
    y_pos = 0.78
    for hero_num, hero_desc in card["hero_lines"]:
        # Large hero number
        ax.text(
            0.085, y_pos,
            hero_num,
            transform=ax.transAxes,
            fontsize=32, fontweight="bold", color=accent,
            va="top", ha="left",
            zorder=2,
        )
        # Descriptor right-aligned on the same baseline
        ax.text(
            0.94, y_pos - 0.01,
            hero_desc,
            transform=ax.transAxes,
            fontsize=11, color=TEXT_LBL,
            va="top", ha="right",
            zorder=2,
        )
        y_pos -= 0.275

    # ── Context text ───────────────────────────────────────────────
    ax.text(
        0.085, y_pos + 0.015,
        card["context"],
        transform=ax.transAxes,
        fontsize=9.0, color=TEXT_MUT,
        va="top", ha="left",
        linespacing=1.50,
        zorder=2,
    )


# ── Draw all cards ─────────────────────────────────────────────────────
for (x0, y0), card_data in zip(positions, cards):
    draw_card(fig, x0, y0, card_w, card_h, card_data)

# ── Save ───────────────────────────────────────────────────────────────
out = (
    "/Users/davidleitch/Library/Mobile Documents/"
    "com~apple~CloudDocs/snakeplay/itk_articles/background/"
    "qld_drought_flood_cycle.png"
)
fig.savefig(out, dpi=300, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print(f"Saved: {out}")
