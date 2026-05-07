"""Wind and solar FID rolling 12-month — small multiples by state.

Tufte-style 2×3 grid, shared y-axis for cross-state comparison.
"""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

PAPER = "#FFFCF0"
INK = "#100F0F"
TEXT = "#403E3C"
MUTED = "#6F6E69"
UI = "#E6E4D9"
WIND = "#66800B"     # green 600
SOLAR = "#AD8301"    # yellow 600

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Inter", "-apple-system", "BlinkMacSystemFont",
    "Segoe UI", "system-ui", "Helvetica Neue", "Arial",
]

CSV = Path("/Users/davidleitch/Downloads/renewmap-project-irNtyNzzfjd7pCsSdv3r7G1e3CL2-1778115165587.csv")
OUT = Path("/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/AEMO_spot/pngs/renewmap_fid_rolling12_by_state.png")

df = pd.read_csv(CSV)
df["FID"] = pd.to_datetime(df["Financial Investment Decision"], format="%d/%m/%Y", errors="coerce")
df = df.dropna(subset=["FID", "Project Size (MW)"])
df = df[df["Technology"].isin(["Onshore Wind", "Solar PV"])]

# Common monthly index so zero-activity months propagate through the rolling window
common_idx = pd.date_range(df["FID"].min(), df["FID"].max(), freq="MS")

def rolling12(state: str, tech: str) -> pd.Series:
    monthly = (
        df[(df["State"] == state) & (df["Technology"] == tech)]
        .set_index("FID")["Project Size (MW)"]
        .resample("MS").sum()
        .reindex(common_idx, fill_value=0)
    )
    return monthly.rolling(12, min_periods=1).sum()

# Order panels by total wind + solar MW (largest first). Mainland NEM only.
state_order = ["NSW", "VIC", "QLD", "SA"]
plot_start = pd.Timestamp("2018-01-01")

fig, axes = plt.subplots(2, 2, figsize=(10.5, 6.4), sharex=True, sharey=True)
fig.patch.set_facecolor(PAPER)

for ax, state in zip(axes.flat, state_order):
    ax.set_facecolor(PAPER)
    wind = rolling12(state, "Onshore Wind")
    solar = rolling12(state, "Solar PV")
    wind = wind[wind.index >= plot_start]
    solar = solar[solar.index >= plot_start]

    ax.plot(wind.index, wind.values, color=WIND, linewidth=2.0)
    ax.plot(solar.index, solar.values, color=SOLAR, linewidth=2.0)

    # Panel title (state name, top-left, no box)
    ax.text(0.02, 0.93, state, transform=ax.transAxes,
            fontsize=12, fontweight="bold", color=INK, va="top")

    # Strip spines
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    ax.tick_params(colors=MUTED, length=0, labelsize=9)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_color(TEXT)

    # X-axis ticks every 2 years to keep panels uncluttered
    ax.xaxis.set_major_locator(mdates.YearLocator(base=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    # Light reference baseline at 0
    ax.axhline(0, color=UI, linewidth=0.8, zorder=0)

# Y-axis label only on left-column panels
for ax in axes[:, 0]:
    ax.set_ylabel("Rolling 12-mo MW", color=TEXT, fontsize=10)

# Y-axis formatter
for ax in axes.flat:
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))

# Single legend across the top
from matplotlib.lines import Line2D
legend_handles = [
    Line2D([0], [0], color=WIND, linewidth=2.5, label="Onshore wind"),
    Line2D([0], [0], color=SOLAR, linewidth=2.5, label="Solar PV"),
]
fig.legend(handles=legend_handles, loc="upper right", bbox_to_anchor=(0.99, 0.965),
           facecolor=PAPER, edgecolor="none", labelcolor=INK, fontsize=10,
           framealpha=0.0, ncol=2)

# Title
fig.text(0.04, 0.96, "Wind and solar FID by mainland state — rolling 12-month MW",
         color=INK, fontsize=14, fontweight="bold", ha="left")

# Source attribution
fig.text(0.99, 0.01,
         "Source: renewmap.com.au, ITK May 2026. Shared y-axis to enable cross-state comparison.",
         ha="right", va="bottom", color=MUTED, fontsize=9, style="italic")

plt.subplots_adjust(left=0.07, right=0.97, top=0.91, bottom=0.07,
                    wspace=0.15, hspace=0.22)

plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor="none", bbox_inches="tight")
print(f"Saved {OUT.name}")
