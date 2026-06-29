"""
Where Australia's diesel goes — stacked bar by sub-sector, with the ROAD bar
broken into its vehicle classes (blue family). Variant of diesel_by_subsector.py.

Reconciled to David Leitch's AES activity-basis reconciliation, agreed with
IEEFA's Andrew Gorringe (email "Finding source for a chart", 16 Apr 2026).
See diesel_by_subsector.py docstring for the full mining 7.8-vs-9.6 reconciliation.

Road transport 16.0 BL (ABS SMVU FY2019-20) now split:
  B-doubles & heavy artic (>40t) 4.0 · Other trucks 3.4 · Light commercial 5.0
  · Passenger diesel 3.1 · Buses 0.5
Other bars unchanged: Mining 7.8 (coal/iron/other 48/26/26), Construction 2.5 +
Agriculture 2.3, Rail 1.3 + Utilities/commercial/mfg 2.3. Total ~32.2 BL (AES).
"""

import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------------------- Flexoki theme
PAPER, INK, TEXT, MUTED = '#FFFCF0', '#100F0F', '#403E3C', '#6F6E69'
UI_BORDER = '#B7B5AC'
RED, ORANGE, YELLOW, GREEN = '#AF3029', '#BC5215', '#AD8301', '#66800B'
CYAN, BLUE, PURPLE, MAGENTA = '#24837B', '#205EA6', '#5E409D', '#A02F6F'
GRAY = '#B7B5AC'
# blue family for the road bar (dark -> light, bottom -> top)
B_HEAVY, B_TRUCK, B_LCV, B_PASS, B_BUS = (
    '#1B4D8A', '#205EA6', '#2E6DB8', '#4A8AD4', '#6BA3E0')

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui',
    'Helvetica Neue', 'Arial']

LIGHT_FILLS = {YELLOW, GRAY, B_PASS, B_BUS}

# ------------------------------------------------------------------- plot data
mining_total = 7.8
coal, iron, other_min = (mining_total * 0.48, mining_total * 0.26,
                         mining_total * 0.26)
construction, agriculture = 2.5, 2.3
rail, util_other = 1.3, 2.3

# bars ordered largest -> smallest (road transport on the left)
bars = [
    ('Road\ntransport', [('B-doubles &\nheavy artic (>40t)', 4.0, B_HEAVY),
                         ('Other trucks', 3.4, B_TRUCK),
                         ('Light commercial', 5.0, B_LCV),
                         ('Passenger diesel', 3.1, B_PASS),
                         ('Buses', 0.5, B_BUS)]),
    ('Mining', [('Coal', coal, ORANGE),
                ('Iron ore', iron, RED),
                ('Other mining', other_min, YELLOW)]),
    ('Construction\n& agriculture', [('Construction', construction, PURPLE),
                                     ('Agriculture', agriculture, GREEN)]),
    ('Rail &\nother', [('Rail', rail, MAGENTA),
                       ('Utilities,\ncommercial, mfg', util_other, GRAY)]),
]

fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

x = range(len(bars))
WIDTH = 0.62


def seg_label(xc, lo, hi, txt, val, fill):
    mid = (lo + hi) / 2
    if (hi - lo) >= 1.2:
        tc = INK if fill in LIGHT_FILLS else 'white'
        ax.text(xc, mid, f'{txt}\n{val:.1f}', ha='center', va='center',
                color=tc, fontsize=9.5, fontweight='bold', linespacing=1.1)
    else:
        ax.text(xc + WIDTH / 2 + 0.05, mid, f'{txt}  {val:.1f}',
                ha='left', va='center', color=TEXT, fontsize=8.5)


for xc, (cat, segs) in zip(x, bars):
    bottom = 0.0
    for txt, val, col in segs:
        ax.bar(xc, val, WIDTH, bottom=bottom, color=col,
               edgecolor=PAPER, linewidth=1.2)
        seg_label(xc, bottom, bottom + val, txt, val, col)
        bottom += val
    ax.text(xc, bottom + 0.4, f'{bottom:.1f}', ha='center', va='bottom',
            color=INK, fontsize=13, fontweight='bold')

# axes cosmetics
ax.set_xticks(list(x))
ax.set_xticklabels([c for c, _ in bars], fontsize=12, color=INK)
ax.set_ylim(0, 19)
ax.set_yticks(range(0, 19, 4))
ax.tick_params(colors=MUTED, length=0)
for lab in ax.get_yticklabels():
    lab.set_color(TEXT)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_ylabel('Diesel consumption, billion litres per year',
              color=TEXT, fontsize=11)

fig.text(0.125, 0.955, "Where Australia's diesel goes",
         ha='left', va='bottom', color=INK, fontsize=17, fontweight='bold')
fig.text(0.125, 0.918,
         'By sub-sector, billion litres per year. AES activity basis (FY2023-24); '
         'road from ABS SMVU (FY2019-20). Sums to ~32 BL',
         ha='left', va='bottom', color=MUTED, fontsize=10.5)

fig.text(0.125, 0.024,
         "Mining = AES 'core mining' (7.8 BL). IEEFA's 9.6 BL is the industry basis, "
         "which also counts mining's own transport, generation & mine construction "
         "(here in Road, Rail/other, Construction). Coal/iron/other = IEEFA 48/26/26 "
         "applied to 7.8.",
         ha='left', va='bottom', color=MUTED, fontsize=8, style='italic')
fig.text(0.125, 0.010,
         "Data: ABS AES Table F 2023-24; ABS SMVU 2020; IEEFA Mining Diesel 2026. "
         "Reconciliation per D. Leitch / IEEFA correspondence, Apr 2026.",
         ha='left', va='bottom', color=MUTED, fontsize=8, style='italic')

plt.tight_layout(rect=(0, 0.03, 1, 0.90))
OUT = Path(__file__).resolve().parent.parent / 'media' / 'diesel_by_subsector_road_detail.png'
plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'saved {OUT}')
for cat, segs in bars:
    print(f'{cat.replace(chr(10), " "):<28}{sum(v for _, v, _ in segs):.1f}')
print(f'{"TOTAL":<28}{sum(v for _, segs in bars for _, v, _ in segs):.1f}')
