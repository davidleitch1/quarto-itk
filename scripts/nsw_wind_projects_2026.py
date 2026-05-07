"""NSW wind projects competing to reach FID — Flexoki-styled table with 2026 news."""

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

TITLE = "NSW wind projects competing to reach FID"
HEADERS = ("Project", "Size (MW)", "Cost ($B)", "Transmission", "Owner", "2026 news")

# Pre-format numbers as strings so we can mix a title row with the data.
def fnum(x):
    return f"{x:,.0f}"

def fcost(x):
    return f"{x:.1f}"

# News strings hand-wrapped to two lines so the column can stay narrow.
data_rows = [
    ("Yanco Delta",     fnum(1500), fcost(5.3),  "1,460 MW",   "Origin",     "$175m transmission paid; FID FY27 H1;\nIDA-endorsed Mar 2026"),
    ("Liverpool Range", fnum(1332), fcost(4.7),  "REZ rights", "Tilt",       ""),
    ("Pottinger",       fnum(1300), fcost(4.6),  "831 MW REZ", "AGL/Someva", "Endorsed by NSW Investment Delivery\nAuthority Mar 2026 (fast-track)"),
    ("Dinawan",         fnum(1300), fcost(4.6),  "1,007 MW",   "Spark/TNB",  "Solar+BESS approved Apr; IDA-endorsed\nMar 2026; wind FC late 2026"),
    ("Valley of Winds", fnum(943),  fcost(3.3),  "Approved",   "ACEN",       "Class 1 appeal (Baillieu) in\nconciliation; decision pending"),
    ("Winterbourne",    fnum(730),  fcost(2.6),  "New England", "Vestas",    "DPHI assessment due mid-2026;\namendment ~70% public support"),
    ("Spicers Creek",   fnum(700),  fcost(2.5),  "REZ access", "Squadron",   "CBoP/EBoP contractor tenders\nreceived Feb 2026"),
    ("Hills of Gold",   fnum(420),  fcost(1.5),  "Yes",        "Someva",     "Court-mediated settlement Mar 2026;\nproject cleared to proceed"),
    ("Coppabella",      fnum(289),  fcost(1.0),  "Yes",        "Goldwind",   "BESS modification on exhibition\nDec 2025; pivoting to wind+storage"),
    ("NSW Total",       fnum(8514), fcost(30.1), "",           "",           ""),
]

# Layout: title row, then column-header row, then data, then total.
rows = [
    (TITLE, "", "", "", "", ""),
    HEADERS,
] + data_rows

df = pd.DataFrame(rows, columns=["Project", "Size (MW)", "Cost ($B)", "Transmission", "Owner", "2026 news"])

fig, ax = plt.subplots(figsize=(11.5, 6.8))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

# Use empty column titles — the column-header row in the dataframe acts as the visible header.
col_defs = [
    ColumnDefinition(
        name="Project",
        title="",
        width=0.95,
        textprops={"ha": "left", "fontsize": 10.5, "fontweight": "bold", "color": INK},
    ),
    ColumnDefinition(
        name="Size (MW)",
        title="",
        width=0.55,
        textprops={"ha": "right", "fontsize": 10.5, "color": INK},
    ),
    ColumnDefinition(
        name="Cost ($B)",
        title="",
        width=0.55,
        textprops={"ha": "right", "fontsize": 10.5, "color": INK},
    ),
    ColumnDefinition(
        name="Transmission",
        title="",
        width=0.75,
        textprops={"ha": "left", "fontsize": 10.5, "color": TEXT},
    ),
    ColumnDefinition(
        name="Owner",
        title="",
        width=0.75,
        textprops={"ha": "left", "fontsize": 10.5, "color": TEXT},
    ),
    ColumnDefinition(
        name="2026 news",
        title="",
        width=2.0,
        textprops={"ha": "left", "fontsize": 9.5, "color": INK},
    ),
]

tab = Table(
    df,
    column_definitions=col_defs,
    index_col="Project",
    textprops={"fontsize": 10.5, "color": INK},
    row_dividers=True,
    row_divider_kw={"color": UI, "linewidth": 0.5},
    col_label_divider=False,
    footer_divider=True,
    footer_divider_kw={"color": UI_BORDER, "linewidth": 1.0},
    column_border_kw={"color": UI, "linewidth": 0.5},
    cell_kw={"facecolor": PAPER, "edgecolor": PAPER},
    col_label_cell_kw={"facecolor": PAPER},
    ax=ax,
)

# Title row = row 0. Large bold title in the first cell.
title_cell = tab.rows[0].cells[0]
title_cell.text.set_fontsize(14)
title_cell.text.set_fontweight("bold")
title_cell.text.set_color(INK)

# Header row = row 1. Bold all cells; right-align numeric headers.
for cell in tab.rows[1].cells:
    cell.text.set_fontweight("bold")
    cell.text.set_color(INK)
for header_idx in (1, 2):
    tab.rows[1].cells[header_idx].text.set_ha("right")

# NSW Total = last row; bold it.
last_idx = len(tab.rows) - 1
for cell in tab.rows[last_idx].cells:
    cell.text.set_fontweight("bold")
    cell.text.set_color(INK)

# Source attribution
fig.text(
    0.99, 0.01,
    "Source: renewmap.com.au, ITK; 2026 news compiled May 2026",
    ha="right", va="bottom", color=MUTED, fontsize=9, style="italic",
)

plt.savefig(
    "/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/itk_articles/media/nsw_wind_projects_2026_news.png",
    dpi=300, facecolor=PAPER, edgecolor="none", bbox_inches="tight",
)
print("Saved nsw_wind_projects_2026_news.png")
