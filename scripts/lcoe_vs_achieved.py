"""LCOE/LCOS vs achieved YTD 2026 for new-build NSW economics.

Two Flexoki-styled PNG tables:
  1. Fuel economics — capex, CF, LCOE, YTD achieved VWAP/spread
  2. WACC build-up — CAPM components and conversion to real
"""

import matplotlib.pyplot as plt
import pandas as pd
from plottable import ColumnDefinition, Table

PAPER = "#FFFCF0"
INK = "#100F0F"
TEXT = "#403E3C"
MUTED = "#6F6E69"
UI = "#E6E4D9"
UI_BORDER = "#B7B5AC"
GREEN = "#66800B"
RED = "#AF3029"

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Inter", "-apple-system", "BlinkMacSystemFont",
    "Segoe UI", "system-ui", "Helvetica Neue", "Arial",
]


# ─────────────────────────────────────────────────────────────────
# Table 1 — Fuel economics
# ─────────────────────────────────────────────────────────────────

TITLE_1 = "New-build economics vs YTD 2026 achieved (NEM-wide)"
HEADERS_1 = ("Fuel", "Capex\n($m/MW)", "CF\n(%)", "LCOE / LCOS\n($/MWh)", "Achieved YTD\n($/MWh)")

fuel_rows = [
    ("Wind",        "3.8",  "32",                       "99",                            "VWAP 51"),
    ("Solar PV",    "1.5",  "25",                       "50",                            "VWAP 39"),
    ("Battery 4h",  "1.6",  "1 cyc/day\n× 85% RTE",     "LCOS 137\n(discharge only)",    "Spread 115"),
]

rows_1 = [(TITLE_1, "", "", "", ""), HEADERS_1] + fuel_rows
df1 = pd.DataFrame(rows_1, columns=list(HEADERS_1))


def render_fuel_table():
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    col_defs = [
        ColumnDefinition(name="Fuel", title="", width=0.85,
                         textprops={"ha": "left", "fontsize": 11, "fontweight": "bold", "color": INK}),
        ColumnDefinition(name="Capex\n($m/MW)", title="", width=0.55,
                         textprops={"ha": "right", "fontsize": 11, "color": INK}),
        ColumnDefinition(name="CF\n(%)", title="", width=0.85,
                         textprops={"ha": "right", "fontsize": 11, "color": INK}),
        ColumnDefinition(name="LCOE / LCOS\n($/MWh)", title="", width=1.00,
                         textprops={"ha": "right", "fontsize": 11, "color": INK}),
        ColumnDefinition(name="Achieved YTD\n($/MWh)", title="", width=0.85,
                         textprops={"ha": "right", "fontsize": 11, "color": INK}),
    ]

    tab = Table(
        df1, column_definitions=col_defs, index_col="Fuel",
        textprops={"fontsize": 11, "color": INK},
        row_dividers=True, row_divider_kw={"color": UI, "linewidth": 0.5},
        col_label_divider=False,
        column_border_kw={"color": UI, "linewidth": 0.5},
        cell_kw={"facecolor": PAPER, "edgecolor": PAPER},
        col_label_cell_kw={"facecolor": PAPER},
        ax=ax,
    )

    title_cell = tab.rows[0].cells[0]
    title_cell.text.set_fontsize(14)
    title_cell.text.set_fontweight("bold")
    title_cell.text.set_color(INK)

    for cell in tab.rows[1].cells:
        cell.text.set_fontweight("bold")
        cell.text.set_color(INK)
    # Right-align numeric headers (Fuel column stays left)
    for header_idx in (1, 2, 3, 4):
        tab.rows[1].cells[header_idx].text.set_ha("right")

    # Colour-code achieved column: red for under-recovery
    for r in (2, 3, 4):
        tab.rows[r].cells[4].text.set_color(RED)

    # Find the right edge of the last column in fig coords for footnote alignment
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    last_cell_patch = tab.rows[1].cells[-1].rectangle_patch
    bbox_disp = last_cell_patch.get_window_extent(renderer)
    bbox_fig = bbox_disp.transformed(fig.transFigure.inverted())
    footnote_x = bbox_fig.x1

    fig.text(
        footnote_x, 0.01,
        "LCOE: 5% real WACC, 30y wind/solar, 15y battery; FOM $29k/$12k/$12.5k per MW.yr.\n"
        "Battery spread excludes FCAS (~$24/MWh equiv. at $30k/MW.yr) — adding it lifts battery to ~$139/MWh.\n"
        "Achieved: Jan 1 – May 6 2026, NEM-wide, AEMO duckdb. Source: ITK May 2026.",
        ha="right", va="bottom", color=MUTED, fontsize=8.5, style="italic",
    )

    plt.savefig(
        "/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/itk_articles/media/lcoe_vs_achieved_2026.png",
        dpi=300, facecolor=PAPER, edgecolor="none", bbox_inches="tight",
    )
    plt.close(fig)
    print("Saved lcoe_vs_achieved_2026.png")


# ─────────────────────────────────────────────────────────────────
# Table 2 — WACC build-up
# ─────────────────────────────────────────────────────────────────

TITLE_2 = "WACC build-up — ITK assumptions (May 2026)"
HEADERS_2 = ("Component", "Value", "Notes")

wacc_rows = [
    ("Risk-free rate (10y AGB)",     "5.0%",  "10-year Australian Government bond"),
    ("Debt margin",                  "1.5%",  "Project-finance margin over Rf"),
    ("Cost of debt — pre-tax",       "6.5%",  "Rf + margin"),
    ("Cost of debt — after-tax",     "4.5%",  "× (1 − 30% tax)"),
    ("Market risk premium",          "6.0%",  "Long-run Australian equity premium"),
    ("Equity beta",                  "0.8",   "Regulated infrastructure / merchant blend"),
    ("Cost of equity (CAPM)",        "9.8%",  "Rf + β × MRP"),
    ("Debt share",                   "65%",   ""),
    ("Equity share",                 "35%",   ""),
    ("WACC — nominal pre-tax",       "7.6%",  "wₑ × Rₑ + w_d × R_d"),
    ("WACC — nominal after-tax",     "6.4%",  "wₑ × Rₑ + w_d × R_d × (1 − t)"),
    ("Inflation",                    "2.5%",  "Long-run RBA midpoint"),
    ("WACC — real pre-tax",          "5.0%",  "Fisher: (1 + nom)/(1 + π) − 1"),
    ("WACC — real after-tax",        "3.8%",  "Fisher: (1 + nom)/(1 + π) − 1"),
]

rows_2 = [(TITLE_2, "", "")] + [HEADERS_2] + wacc_rows
df2 = pd.DataFrame(rows_2, columns=list(HEADERS_2))


def render_wacc_table():
    fig, ax = plt.subplots(figsize=(9.5, 6.4))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    col_defs = [
        ColumnDefinition(name="Component", title="", width=1.40,
                         textprops={"ha": "left", "fontsize": 11, "fontweight": "bold", "color": INK}),
        ColumnDefinition(name="Value", title="", width=0.55,
                         textprops={"ha": "right", "fontsize": 11, "color": INK}),
        ColumnDefinition(name="Notes", title="", width=2.10,
                         textprops={"ha": "left", "fontsize": 10.5, "color": TEXT}),
    ]

    tab = Table(
        df2, column_definitions=col_defs, index_col="Component",
        textprops={"fontsize": 11, "color": INK},
        row_dividers=True, row_divider_kw={"color": UI, "linewidth": 0.5},
        col_label_divider=False,
        column_border_kw={"color": UI, "linewidth": 0.5},
        cell_kw={"facecolor": PAPER, "edgecolor": PAPER},
        col_label_cell_kw={"facecolor": PAPER},
        ax=ax,
    )

    title_cell = tab.rows[0].cells[0]
    title_cell.text.set_fontsize(14)
    title_cell.text.set_fontweight("bold")
    title_cell.text.set_color(INK)

    for cell in tab.rows[1].cells:
        cell.text.set_fontweight("bold")
        cell.text.set_color(INK)
    tab.rows[1].cells[1].text.set_ha("right")

    # Bold the headline WACC outputs
    headline_rows = {
        "WACC — nominal pre-tax": 11,
        "WACC — nominal after-tax": 12,
        "WACC — real pre-tax": 14,
        "WACC — real after-tax": 15,
    }
    for r in headline_rows.values():
        for cell in tab.rows[r].cells:
            cell.text.set_fontweight("bold")
            cell.text.set_color(INK)

    fig.text(
        0.99, 0.01,
        "Source: ITK May 2026; CAPM convention",
        ha="right", va="bottom", color=MUTED, fontsize=9, style="italic",
    )

    plt.savefig(
        "/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/itk_articles/media/wacc_buildup_2026.png",
        dpi=300, facecolor=PAPER, edgecolor="none", bbox_inches="tight",
    )
    plt.close(fig)
    print("Saved wacc_buildup_2026.png")


if __name__ == "__main__":
    render_fuel_table()
    render_wacc_table()
