"""
Australia's major trade flows — net positions, trailing 12 months (A$bn).

Flexoki Light stacked/diverging bar of net GOODS trade flows, comparing the big
export earners (iron ore, coal, gas, gold, meat) against the oil import bill, for
the diesel/oil-imports research thread.

Bars:
  Iron ore — net export, single segment (SITC 281)
  Coal     — net export, single segment (SITC 32)
  Gas (LNG)— net export, single segment (SITC 34)
  Gold     — net export, single segment (SITC 97; partly pass-through, see note)
  Meat     — net export, single segment (SITC 01)
  Oil      — stacked: diesel / petrol / other, each net of related exports (SITC 33)

Data source
-----------
ABS "Merchandise Imports/Exports by Commodity (SITC), Country and State"
(dataflows ABS:MERCH_IMP / MERCH_EXP, v1.0.0), SDMX-CSV pull, Australia total
(STATE=TOT, COUNTRY=TOT), monthly, May 2025 - Apr 2026. Values are OBS_VALUE in
thousands of AUD (UNIT_MULT=3). Saved in scripts/data/.
    SITC 281 = iron ore & concentrates
    SITC 32  = coal, coke & briquettes
    SITC 33  = petroleum (oil):  333 crude, 334 refined products, 335 other
    SITC 34  = gas (343 LNG, 342 LPG)
    SITC 97  = gold, non-monetary;  SITC 01 = meat

Diesel/petrol/jet split of refined products (334): the ABS open data and DFAT
pivot tables stop at 3-digit SITC (refined products as one lump), so the within-
refined split is estimated by applying the import-VOLUME shares from the US EIA
Australia Country Analysis Brief (Dec 2025, 2024 data) to the ABS refined-import
VALUE: diesel/gasoil 57%, gasoline (petrol) 25%, jet 13%, other ~5%. "Other" in
the oil bar is the residual so the bar sums to the exact ABS net of -45.0.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ---------------------------------------------------------------- Flexoki theme
PAPER, INK, TEXT, MUTED = '#FFFCF0', '#100F0F', '#403E3C', '#6F6E69'
UI_BORDER = '#B7B5AC'
ORANGE, MAGENTA = '#BC5215', '#A02F6F'
RED, GREEN, BLUE, CYAN, PURPLE, YELLOW = (
    '#AF3029', '#66800B', '#205EA6', '#24837B', '#5E409D', '#AD8301')

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui',
    'Helvetica Neue', 'Arial']

# --------------------------------------------------------------- load ABS goods
HERE = Path(__file__).resolve().parent
DATA = HERE / 'data'


def sitc_totals(path):
    """Sum OBS_VALUE (->A$bn) by SITC code for the Australia total (STATE=TOT)."""
    by = {}
    with open(path) as fh:
        rdr = csv.reader(fh)
        next(rdr)
        for row in rdr:
            sitc, state, val = row[1], row[3], row[6]
            if state != 'TOT':
                continue
            by[sitc] = by.get(sitc, 0.0) + float(val) / 1e6  # thousands -> $bn
    return by


imp = sitc_totals(DATA / 'abs_merch_imp_may25_apr26.csv')
exp = sitc_totals(DATA / 'abs_merch_exp_may25_apr26.csv')

iron_ore_net = exp.get('281', 0) - imp.get('281', 0)    # ~ +119.4
gold_net = exp.get('97', 0) - imp.get('97', 0)          # ~ +42.5 (partly pass-through)
meat_net = exp.get('01', 0) - imp.get('01', 0)          # ~ +27.4
coal_net = exp.get('32', 0) - imp.get('32', 0)          # ~ +64.2
gas_net = exp.get('34', 0) - imp.get('34', 0)           # ~ +58.1
oil_net = exp.get('33', 0) - imp.get('33', 0)           # ~ -45.0
refined_imp = imp.get('334', 0)                          # ~ 50.1

# diesel/petrol via EIA 2024 volume shares applied to refined-import value
diesel_net = -0.57 * refined_imp                         # ~ -28.5
petrol_net = -0.25 * refined_imp                         # ~ -12.5
oil_other_net = oil_net - diesel_net - petrol_net        # residual ~ -4.0

# ------------------------------------------------------------------- plot data
# (label, list of (segment_label, value, colour))
GRAY = '#B7B5AC'  # residual "other" fill
bars = [
    ('Iron ore', [('Iron ore', iron_ore_net, ORANGE)]),
    ('Coal', [('Coal', coal_net, INK)]),
    ('Gas (LNG)', [('Gas', gas_net, MAGENTA)]),
    ('Gold', [('Gold*', gold_net, YELLOW)]),
    ('Meat', [('Meat', meat_net, RED)]),
    ('Oil', [('Diesel', diesel_net, BLUE),
             ('Petrol', petrol_net, CYAN),
             ('Other\n(crude, jet, etc.)', oil_other_net, GRAY)]),
]

# segments with light fills need dark text labels
LIGHT_FILLS = {YELLOW, GRAY}

fig, ax = plt.subplots(figsize=(13, 8.5))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

x = range(len(bars))
WIDTH = 0.62


def label_seg(xc, lo, hi, txt, val, fill):
    """Place a segment label; value inside if tall enough, else to the side."""
    mid = (lo + hi) / 2
    if abs(hi - lo) >= 6:
        tc = INK if fill in LIGHT_FILLS else 'white'
        ax.text(xc, mid, f'{txt}\n{val:+.1f}', ha='center', va='center',
                color=tc, fontsize=10, fontweight='bold', linespacing=1.1)
    else:
        ax.text(xc + WIDTH / 2 + 0.04, mid, f'{txt} {val:+.1f}',
                ha='left', va='center', color=TEXT, fontsize=9)


for xc, (cat, segs) in zip(x, bars):
    pos = neg = 0.0
    for txt, val, col in segs:
        if val >= 0:
            ax.bar(xc, val, WIDTH, bottom=pos, color=col,
                   edgecolor=PAPER, linewidth=1.2)
            label_seg(xc, pos, pos + val, txt, val, col)
            pos += val
        else:
            ax.bar(xc, val, WIDTH, bottom=neg, color=col,
                   edgecolor=PAPER, linewidth=1.2)
            label_seg(xc, neg + val, neg, txt, val, col)
            neg += val
    # net marker + label for multi-segment bars
    net = sum(v for _, v, _ in segs)
    if len(segs) > 1:
        ax.plot([xc - WIDTH / 2 - 0.05, xc + WIDTH / 2 + 0.05], [net, net],
                color=INK, linewidth=1.8, zorder=5)
        va = 'bottom' if net >= 0 else 'top'
        off = 1.5 if net >= 0 else -1.5
        ax.text(xc, net + off, f'net {net:+.0f}', ha='center', va=va,
                color=INK, fontsize=11, fontweight='bold')
    else:
        ax.text(xc, net + 1.5, f'{net:+.0f}', ha='center', va='bottom',
                color=INK, fontsize=12, fontweight='bold')

# zero line
ax.axhline(0, color=UI_BORDER, linewidth=1.2)

# axes cosmetics
ax.set_xticks(list(x))
ax.set_xticklabels([c for c, _ in bars], fontsize=13, color=INK,
                   fontweight='bold')
ax.set_ylim(-62, 138)
ax.set_yticks(range(-40, 141, 20))
ax.set_yticklabels([f'{v:+d}' if v else '0' for v in range(-40, 141, 20)])
ax.tick_params(colors=MUTED, length=0)
for lab in ax.get_yticklabels():
    lab.set_color(TEXT)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_ylabel('Net goods balance, A$bn (trailing 12 months)',
              color=TEXT, fontsize=11)

# headline annotation
ax.text(0, 134, 'Export earners', ha='center', va='top', color=MUTED,
        fontsize=10, style='italic')
ax.text(5, -58, 'Import bill', ha='center', va='bottom', color=MUTED,
        fontsize=10, style='italic')

fig.text(0.125, 0.955, "Australia's big earners vs the oil import bill",
         ha='left', va='bottom', color=INK, fontsize=17, fontweight='bold')
fig.text(0.125, 0.918,
         'Net goods flows, 12 months to Apr 2026, A$bn',
         ha='left', va='bottom', color=MUTED, fontsize=11)

fig.text(0.125, 0.012,
         r"* Gold shown net: ~\$25bn doré imports refined and re-exported; "
         r"gross gold exports ~\$68bn.",
         ha='left', va='bottom', color=MUTED, fontsize=8, style='italic')
fig.text(0.99, 0.012,
         "Data: ABS Merchandise Trade by Commodity (SITC); "
         "diesel/petrol split est. from US EIA import-volume shares",
         ha='right', va='bottom', color=MUTED, fontsize=8, style='italic')

plt.tight_layout(rect=(0, 0.03, 1, 0.90))
OUT = HERE.parent / 'media' / 'trade_flows_net.png'
plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'saved {OUT}')

# echo the numbers used
print(f'coal_net   {coal_net:+.1f}')
print(f'gas_net    {gas_net:+.1f}')
print(f'oil_net    {oil_net:+.1f}  (refined_imp {refined_imp:.1f})')
print(f'  diesel   {diesel_net:+.1f}')
print(f'  petrol   {petrol_net:+.1f}')
print(f'  other    {oil_other_net:+.1f}')
print(f'gold_net   {gold_net:+.1f}')
print(f'meat_net   {meat_net:+.1f}')
