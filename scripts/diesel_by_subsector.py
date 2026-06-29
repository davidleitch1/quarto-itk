"""
Where Australia's diesel goes — simple stacked-bar by sub-sector (A billion L/yr).

Reconciled to David Leitch's AES activity-basis reconciliation, agreed with
IEEFA's Andrew Gorringe (email thread "Finding source for a chart", 16 Apr 2026).

Four bars, each stacked (AES Table F FY2023-24 except road = ABS SMVU FY2019-20):
  Mining            — coal / iron ore / other mining (7.8 BL; split 48/26/26)
  Road transport    — B-doubles & heavy artic (>40t) / all other road
  Construction & ag — construction / agriculture
  Rail & other      — rail / utilities, commercial & manufacturing

THE KEY RECONCILIATION (why mining = 7.8, not IEEFA's 9.6):
  IEEFA's 9.6 BL is the INDUSTRY / Energy-Accounts basis (ABS Energy Accounts
  mining diesel & fuel oil = 452 PJ FY23-24) — it counts everything a mining
  COMPANY burns, including diesel for transport between sites, on-site power
  generation, and construction of mine infrastructure.
  AES Table F is the ACTIVITY basis: that same diesel is reallocated — transport
  -> Transport, generation -> Electricity, mine construction -> Construction.
  Only core extraction/processing stays in Mining = 299.6 PJ = 7.8 BL.
  Combining 9.6 BL with the SMVU road split would DOUBLE-COUNT mining transport
  and generation. So this chart uses 7.8 BL.

Data (BL/yr):
  Mining 7.8 (AES 299.6 PJ); coal/iron/other = IEEFA 48/26/26 -> 3.7/2.0/2.0
  Road 16.0 (SMVU 2020): B-doubles 4.0; all other road 12.0
    (other trucks 3.4 + LCV 5.0 + passenger 3.1 + buses 0.5)
  Construction 2.5 (kept; AES 26.5 PJ=0.7, +equipment-hire firms per D.L.)
  Agriculture 2.3 (AES 88.8 PJ)
  Rail 1.3 (AES 52.0 PJ); Utilities/commercial/mfg 2.3 (AES 89.8 PJ)
  TOTAL ~32.2 BL (AES basis). cf. APS diesel sales 33.5 BL 2025 (different measure
  + vintage): the ~1.3 BL gap is sales-vs-consumption and FY23-24 vs CY2025.
"""

import matplotlib.pyplot as plt

# ---------------------------------------------------------------- Flexoki theme
PAPER, INK, TEXT, MUTED = '#FFFCF0', '#100F0F', '#403E3C', '#6F6E69'
UI_BORDER = '#B7B5AC'
RED, ORANGE, YELLOW, GREEN = '#AF3029', '#BC5215', '#AD8301', '#66800B'
CYAN, BLUE, PURPLE, MAGENTA = '#24837B', '#205EA6', '#5E409D', '#A02F6F'
GRAY = '#B7B5AC'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui',
    'Helvetica Neue', 'Arial']

LIGHT_FILLS = {YELLOW, GRAY}

# ------------------------------------------------------------------- plot data
# Reconciled to David Leitch's AES activity-basis reconciliation (email to
# J. Oh / A. Gorringe, IEEFA, 16 Apr 2026). All from AES Table F 2023-24 except
# road (ABS SMVU FY2019-20). Mining is the AES "core mining" figure (7.8 BL),
# NOT the IEEFA 9.6 BL industry/Energy-Accounts figure — the latter also counts
# mining transport, on-site generation and mine construction, which the activity
# basis reallocates to Road, Rail/Other and Construction respectively.
artic_40 = 4.0                # B-doubles & heavy artic >40t (SMVU)
road_other = 12.0            # other trucks 3.4 + LCV 5.0 + passenger 3.1 + buses 0.5
road_total = artic_40 + road_other   # 16.0 (AES road transport ~16.1)
mining_total = 7.8           # AES Table F 2023-24, 299.6 PJ (core extraction/processing)
# commodity split: IEEFA emission shares (48/26/26) applied to AES core figure
coal, iron, other_min = (mining_total * 0.48, mining_total * 0.26,
                         mining_total * 0.26)
construction = 2.5           # kept (AES 0.7 PJ-basis; +hire firms per D.L.)
agriculture = 2.3            # AES 88.8 PJ
rail = 1.3                   # AES 52.0 PJ
util_other = 2.3             # AES elec/gas/water + commercial + manufacturing, 89.8 PJ
TOTAL = (mining_total + road_total + construction + agriculture
         + rail + util_other)  # ~32.2 BL (AES basis); cf. APS sales 33.5 BL

# bars ordered largest -> smallest (road transport on the left)
bars = [
    ('Road\ntransport', [('B-doubles &\nheavy artic (>40t)', artic_40, BLUE),
                         ('All other road', road_other, CYAN)]),
    ('Mining', [('Coal', coal, ORANGE),
                ('Iron ore', iron, RED),
                ('Other mining', other_min, YELLOW)]),
    ('Construction\n& agriculture', [('Construction', construction, PURPLE),
                                     ('Agriculture', agriculture, GREEN)]),
    ('Rail &\nother', [('Rail', rail, MAGENTA),
                       ('Utilities,\ncommercial, mfg', util_other, GRAY)]),
]

fig, ax = plt.subplots(figsize=(11.5, 8))
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
OUT = __import__('pathlib').Path(__file__).resolve().parent.parent / 'media' / 'diesel_by_subsector.png'
plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'saved {OUT}')
for cat, segs in bars:
    print(f'{cat.replace(chr(10), " "):<28}{sum(v for _, v, _ in segs):.1f}')
print(f'{"TOTAL":<28}{sum(v for _, segs in bars for _, v, _ in segs):.1f}')
