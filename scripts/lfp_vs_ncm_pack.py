"""
LFP vs NCM — 100 kWh pack: weight, volume AND cost (pack level, cell-to-pack).
Flexoki Light. Three bar panels + notes on cost driver, energy-in-use, cold weather.

Data (pack level, same 100 kWh nameplate):
  Weight:  LFP ~670-770 kg (~720) | NCM ~500-590 kg (~560)   [gravimetric 130-150 / 170-200 Wh/kg]
  Volume:  LFP ~330-400 L (~360)  | NCM ~210-250 L (~230)     [volumetric 250-300 / 400-480 Wh/L]
  Cost:    LFP $81/kWh -> ~$8,100 | NMC $128/kWh -> ~$12,800  [BNEF Li-ion price survey, Dec 2025,
           volume-weighted, all segments]. LFP ~37% cheaper, ~$4,700/100 kWh.
  Context: all-chem avg $108/kWh (-8% yoy); China ~$84/kWh, NA/Europe +44%/+56%.
  Driver: cathode active material — LFP ~$10-15/kWh vs NMC ~$40-60/kWh of cell capacity.
"""

import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import gridspec

# ---------------------------------------------------------------- Flexoki theme
PAPER, INK, TEXT, MUTED = '#FFFCF0', '#100F0F', '#403E3C', '#6F6E69'
TINT = '#F2EEDC'
LFP_C, NCM_C = '#205EA6', '#BC5215'      # blue / orange
BLUE, GREEN, RED = '#205EA6', '#66800B', '#AF3029'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'system-ui',
    'Helvetica Neue', 'Arial']

# ---------------------------------------------------------------------- data
# (mid, lo, hi)  — lo/hi None -> no whisker
weight = {'LFP': (720, 670, 770), 'NCM': (560, 500, 590)}
volume = {'LFP': (360, 330, 400), 'NCM': (230, 210, 250)}
cost = {'LFP': (8100, None, None), 'NCM': (12800, None, None)}

fig = plt.figure(figsize=(15, 8.6))
fig.patch.set_facecolor(PAPER)
gs = gridspec.GridSpec(2, 3, height_ratios=[1, 0.5], hspace=0.5, wspace=0.26,
                       left=0.06, right=0.97, top=0.83, bottom=0.04)


def panel(ax, data, ylim, ystep, ylab, title, sub, delta_txt, delta_col,
          money=False):
    ax.set_facecolor(PAPER)
    for i, c in enumerate(['LFP', 'NCM']):
        mid, lo, hi = data[c]
        col = LFP_C if c == 'LFP' else NCM_C
        ax.bar(i, mid, 0.56, color=col, edgecolor=PAPER, linewidth=1)
        if lo is not None:
            ax.errorbar(i, mid, yerr=[[mid - lo], [hi - mid]], fmt='none',
                        ecolor=INK, elinewidth=1.6, capsize=7, capthick=1.6)
            ax.text(i, hi + ylim * 0.04, f'{lo:,}–{hi:,}', ha='center',
                    va='bottom', color=TEXT, fontsize=10)
        lbl = f'~${mid:,}' if money else f'~{mid:,}'
        ax.text(i, mid / 2, lbl, ha='center', va='center', color='white',
                fontsize=18 if money else 20, fontweight='bold')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['LFP', 'NCM (NMC)'], fontsize=13, color=INK,
                       fontweight='bold')
    ax.set_ylim(0, ylim)
    ax.set_yticks(range(0, ylim + 1, ystep))
    ax.set_ylabel(ylab, color=TEXT, fontsize=11)
    ax.tick_params(colors=MUTED, length=0)
    for lab in ax.get_yticklabels():
        lab.set_color(TEXT)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(title, color=INK, fontsize=14, fontweight='bold', loc='left',
                 pad=24)
    ax.text(0, 1.05, sub, transform=ax.transAxes, color=MUTED, fontsize=9.3)
    ax.text(0.5, ylim * 0.93, delta_txt, ha='center', va='top', color=delta_col,
            fontsize=12, fontweight='bold')


panel(fig.add_subplot(gs[0, 0]), weight, 900, 300, 'kg', 'Pack weight (kg)',
      'Gravimetric density: LFP ~130–150  vs  NCM ~170–200 Wh/kg',
      'LFP +~160 kg\n(+~29%)', RED)
panel(fig.add_subplot(gs[0, 1]), volume, 460, 100, 'Litres', 'Pack volume (L)',
      'Volumetric density: LFP ~250–300  vs  NCM ~400–480 Wh/L',
      'LFP +~130 L\n(+~57%)', RED)
panel(fig.add_subplot(gs[0, 2]), cost, 16000, 4000, 'US$', 'Pack cost (US$)',
      'BNEF Dec 2025: LFP $81  vs  NMC $128 per kWh (volume-weighted)',
      'LFP −~$4,700\n(−~37%)', GREEN, money=True)

# ------------------------------------------------------------------ notes strip
axn = fig.add_subplot(gs[1, :])
axn.axis('off')
axn.set_xlim(0, 100)
axn.set_ylim(0, 100)

notes = [
    ('Cathode drives cost difference', BLUE,
     "Mostly cathode active material: iron-phosphate ~$10–15/kWh of cell "
     "capacity vs NMC ~$40–60/kWh."),
    ('Energy in use', GREEN,
     "The extra ~150 kg adds only ~0.5–1.0 kWh/100 km — a few % on a "
     "~16–18 base. LFP also charges to 100% daily without NMC's degradation, so "
     "usable kWh sits closer to nameplate."),
    ('Cold weather', RED,
     "The bigger real-world differentiator: LFP's higher internal resistance at "
     "low temp cuts power, raises consumption and weakens regen. Marginal in "
     "Sydney; material in a Xinjiang winter."),
]
for i, (head, col, body) in enumerate(notes):
    x = 0.5 + i * 33.3
    axn.add_patch(plt.Rectangle((x, 10), 31.5, 80, facecolor=TINT,
                                edgecolor='none'))
    axn.text(x + 1.6, 84, head, ha='left', va='top', color=col, fontsize=11.5,
             fontweight='bold')
    axn.text(x + 1.6, 74, '\n'.join(textwrap.wrap(body, width=44)),
             ha='left', va='top', color=TEXT, fontsize=9.3, linespacing=1.4)

# titles + attribution
fig.text(0.06, 0.925, 'LFP vs NCM battery packs — same 100 kWh',
         ha='left', va='bottom', color=INK, fontsize=18, fontweight='bold')
fig.text(0.97, 0.008,
         "Prices: BNEF Lithium-Ion Battery Price Survey, Dec 2025 (volume-weighted "
         "global avg; China ~$84/kWh, N. America/Europe +44–56%). "
         "Weight/volume: pack-level estimates ~2026  ·  ITK",
         ha='right', va='bottom', color=MUTED, fontsize=8, style='italic')

OUT = Path(__file__).resolve().parent.parent / 'media' / 'lfp_vs_ncm_pack.png'
plt.savefig(OUT, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'saved {OUT}')
