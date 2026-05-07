"""NSW major transmission projects — Flexoki-styled summary table."""

import matplotlib.pyplot as plt
import pandas as pd
from plottable import ColumnDefinition, Table

PAPER = "#FFFCF0"
INK = "#100F0F"
TEXT = "#403E3C"
MUTED = "#6F6E69"
UI = "#E6E4D9"
UI_BORDER = "#B7B5AC"

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Inter", "-apple-system", "BlinkMacSystemFont",
    "Segoe UI", "system-ui", "Helvetica Neue", "Arial",
]

TITLE = "Major NSW transmission projects — status May 2026"
HEADERS = (
    "Project",
    "Cost\n($bn)",
    "Scope",
    "Target\ncompletion",
    "Latest news (2026)",
)

rows_data = [
    (
        "Project EnergyConnect (NSW)",
        "3.6",
        "900 km,\nNSW–SA–VIC",
        "Sep 2026",
        "Western section energised Apr 2025;\n1,508 towers up; commissioning H2 2026",
    ),
    (
        "HumeLink",
        "4.9",
        "360 km, Wagga to\nBannaby/Maragle",
        "Late 2027",
        "Under construction; East/West JVs let;\nAER capex $3.96 bn (Aug 2024)",
    ),
    (
        "Central-West Orana REZ\n(ACEREZ)",
        "5.5",
        "90 km × 500 kV +\n150 km × 330 kV",
        "2028",
        "Financial close Apr 2025; construction\nstarted Jun 2025; unlocks 4.5 GW",
    ),
    (
        "Waratah Super Battery (SIPS)",
        "1.0",
        "850 MW /\n1,680 MWh",
        "End 2026",
        "350 MW online; transformer fault Nov 2025;\nreplacement due Q3 2026",
    ),
    (
        "VNI West (KerangLink)",
        "~4.0",
        "475 km × 500 kV,\nDinawan to Bulgana",
        "Nov 2030",
        "Transgrid committed $700m for early works;\nEIS public exhibition Aug 2025",
    ),
    (
        "Hunter Transmission Project",
        "TBC",
        "110 km × 500 kV,\nBayswater–Olney",
        "2029",
        "EIS lodged; Transgrid preferred operator;\nIDA-fast-tracked Mar 2026",
    ),
    (
        "New England REZ\nTransmission",
        "TBC",
        "290 km × 500 kV +\n25 km × 330 kV",
        "Stage 1: 2032\nStage 2: 2034",
        "Federal EPBC approval sought;\nnetwork-operator procurement underway",
    ),
]

df = pd.DataFrame(
    [(TITLE, "", "", "", ""), HEADERS] + rows_data,
    columns=list(HEADERS),
)

fig, ax = plt.subplots(figsize=(11.5, 7.4))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

col_defs = [
    ColumnDefinition(name="Project", title="", width=1.45,
                     textprops={"ha": "left", "fontsize": 11, "fontweight": "bold", "color": INK}),
    ColumnDefinition(name="Cost\n($bn)", title="", width=0.45,
                     textprops={"ha": "right", "fontsize": 11, "color": INK}),
    ColumnDefinition(name="Scope", title="", width=1.20,
                     textprops={"ha": "left", "fontsize": 10.5, "color": TEXT}),
    ColumnDefinition(name="Target\ncompletion", title="", width=0.85,
                     textprops={"ha": "left", "fontsize": 10.5, "color": INK}),
    ColumnDefinition(name="Latest news (2026)", title="", width=2.00,
                     textprops={"ha": "left", "fontsize": 10, "color": INK}),
]

tab = Table(
    df, column_definitions=col_defs, index_col="Project",
    textprops={"fontsize": 11, "color": INK},
    row_dividers=True, row_divider_kw={"color": UI, "linewidth": 0.5},
    col_label_divider=False,
    column_border_kw={"color": UI, "linewidth": 0.5},
    cell_kw={"facecolor": PAPER, "edgecolor": PAPER},
    col_label_cell_kw={"facecolor": PAPER},
    ax=ax,
)

# Title row
title_cell = tab.rows[0].cells[0]
title_cell.text.set_fontsize(14)
title_cell.text.set_fontweight("bold")
title_cell.text.set_color(INK)

# Header row
for cell in tab.rows[1].cells:
    cell.text.set_fontweight("bold")
    cell.text.set_color(INK)
tab.rows[1].cells[1].text.set_ha("right")

# Footnote right-aligned with last column
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
last_cell_patch = tab.rows[1].cells[-1].rectangle_patch
bbox_disp = last_cell_patch.get_window_extent(renderer)
bbox_fig = bbox_disp.transformed(fig.transFigure.inverted())
footnote_x = bbox_fig.x1

fig.text(
    footnote_x, 0.01,
    "Costs: developer / AER capex where determined; New England + Hunter pending AER. SIPS = System Integrity Protection Scheme.\n"
    "Source: Transgrid, EnergyCo, AER, ITK web research May 2026.",
    ha="right", va="bottom", color=MUTED, fontsize=8.5, style="italic",
)

plt.savefig(
    "/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/itk_articles/media/nsw_transmission_2026.png",
    dpi=300, facecolor=PAPER, edgecolor="none", bbox_inches="tight",
)
print("Saved nsw_transmission_2026.png")
