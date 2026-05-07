"""Rolling 12-month FID totals (MW) by technology, from renewmap.com.au export.

Wind and solar lines, Flexoki light theme.
"""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

# ── Flexoki ──
PAPER = "#FFFCF0"
INK = "#100F0F"
TEXT = "#403E3C"
MUTED = "#6F6E69"
UI = "#E6E4D9"
WIND = "#66800B"     # green 600 — primary
SOLAR = "#AD8301"    # yellow 600 — primary
BATTERY = "#92BFDB"  # blue 300 — secondary, deliberately faint

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Inter", "-apple-system", "BlinkMacSystemFont",
    "Segoe UI", "system-ui", "Helvetica Neue", "Arial",
]

CSV = Path("/Users/davidleitch/Downloads/renewmap-project-irNtyNzzfjd7pCsSdv3r7G1e3CL2-1778115165587.csv")
OUT = Path("/Users/davidleitch/Library/Mobile Documents/com~apple~CloudDocs/snakeplay/AEMO_spot/pngs/renewmap_fid_rolling12_wind_solar.png")

df = pd.read_csv(CSV)
df["FID"] = pd.to_datetime(df["Financial Investment Decision"], format="%d/%m/%Y", errors="coerce")
df = df.dropna(subset=["FID", "Project Size (MW)"])
df = df[df["Technology"].isin(["Onshore Wind", "Solar PV", "Battery"])]
df = df.sort_values("FID")

# Common monthly index across all techs, so months with zero FIDs propagate
# correctly through the 12-month rolling window (rather than being dropped).
common_idx = pd.date_range(df["FID"].min(), df["FID"].max(), freq="MS")

def rolling12(tech: str) -> pd.Series:
    monthly = (
        df[df["Technology"] == tech]
        .set_index("FID")["Project Size (MW)"]
        .resample("MS").sum()
        .reindex(common_idx, fill_value=0)
    )
    return monthly.rolling(12, min_periods=1).sum()

wind = rolling12("Onshore Wind")
solar = rolling12("Solar PV")
battery = rolling12("Battery")

# Trim before 2018 — earlier years suffer from sparse FID-date backfill
plot_start = pd.Timestamp("2018-01-01")
wind = wind[wind.index >= plot_start]
solar = solar[solar.index >= plot_start]
battery = battery[battery.index >= plot_start]

fig, ax = plt.subplots(figsize=(11, 5.6))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

# Battery first so wind/solar overplot it where they cross
ax.plot(battery.index, battery.values, color=BATTERY, linewidth=1.8, label="Battery (MW)")
ax.plot(wind.index, wind.values, color=WIND, linewidth=2.5, label="Onshore wind")
ax.plot(solar.index, solar.values, color=SOLAR, linewidth=2.5, label="Solar PV")

# Latest values annotation
last_x = wind.index[-1]
for series, colour in ((wind, WIND), (solar, SOLAR), (battery, BATTERY)):
    ax.scatter([last_x], [series.iloc[-1]], color=colour, s=60, zorder=5,
               edgecolors="white", linewidths=1.5)
    ax.annotate(f"{series.iloc[-1]:,.0f} MW", (last_x, series.iloc[-1]),
                xytext=(8, 0), textcoords="offset points",
                color=colour, fontsize=10, fontweight="bold", va="center")

# Spines & ticks
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(False)
ax.tick_params(colors=MUTED, length=0)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_color(TEXT)

# Y-axis formatting
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.set_ylabel("Rolling 12-month MW reaching FID", color=TEXT, fontsize=11)
ax.set_ylim(bottom=0)

# X-axis: yearly major ticks
ax.xaxis.set_major_locator(mdates.YearLocator(base=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

# Legend
ax.legend(loc="upper left", facecolor=PAPER, edgecolor="none",
          labelcolor=INK, fontsize=10, framealpha=0.8)

# Title
fig.text(0.04, 0.94, "Australian wind, solar and batteries — MW reaching FID (rolling 12 months)",
         color=INK, fontsize=14, fontweight="bold", ha="left")

# Source attribution
fig.text(0.99, 0.02,
         "Source: renewmap.com.au, ITK May 2026",
         ha="right", va="bottom", color=MUTED, fontsize=9, style="italic")

plt.subplots_adjust(left=0.08, right=0.94, top=0.88, bottom=0.10)

plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor="none", bbox_inches="tight")
print(f"Saved {OUT.name}")
print(f"Wind latest 12mo: {wind.iloc[-1]:,.0f} MW; peak: {wind.max():,.0f} MW ({wind.idxmax():%Y-%m})")
print(f"Solar latest 12mo: {solar.iloc[-1]:,.0f} MW; peak: {solar.max():,.0f} MW ({solar.idxmax():%Y-%m})")
print(f"Battery latest 12mo: {battery.iloc[-1]:,.0f} MW; peak: {battery.max():,.0f} MW ({battery.idxmax():%Y-%m})")
