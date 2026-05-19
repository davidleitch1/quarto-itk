"""Horizontal bar chart of OpenAI's seven-vendor commitment stack.

Source: Tomasz Tunguz, "OpenAI's $1.15 Trillion Infrastructure Commitments
(2025-2035)", 3 November 2025, https://tomtunguz.com/openai-hardware-spending-2025-2035

Amazon AWS and CoreWeave figures updated to May 2026 per Q1 2026 disclosures
(see contracts.csv notes).

Run: python3 make_openai_vendors.py
"""
from pathlib import Path
import matplotlib.pyplot as plt

# Flexoki Light
PAPER = '#FFFCF0'
BLACK = '#100F0F'
TEXT = '#403E3C'
MUTED = '#6F6E69'
UI_BORDER = '#B7B5AC'
BLUE = '#205EA6'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', '-apple-system', 'Helvetica Neue', 'Arial']
plt.rcParams['text.parse_math'] = False  # treat $ as a literal character

HERE = Path(__file__).parent

# (vendor, amount_usd_bn, contract description, source_flag)
# source_flag 'tunguz' = Tunguz Nov 2025 figure verbatim
# source_flag 'updated' = post-Tunguz update from Q1 2026 disclosure
data = [
    ('Broadcom',  350, 'Custom accelerator chips, 7y (2026-2032)',     'tunguz'),
    ('Oracle',    300, 'Stargate cloud infrastructure, 6y (2027-2032)', 'tunguz'),
    ('Microsoft', 250, 'Azure cloud services, 7y (2025-2031)',          'tunguz'),
    ('Amazon AWS', 138, 'Compute capacity; $38bn Tunguz + $100bn Q1 2026 expansion', 'updated'),
    ('Nvidia',    100, 'Equity investment + chip purchase commitment',  'tunguz'),
    ('AMD',        90, '6 GW GPU hardware with equity warrants',        'tunguz'),
    ('CoreWeave',  29, 'DC usage rights; $22.4bn Tunguz + $6.5bn expansion', 'updated'),
]
data.sort(key=lambda x: -x[1])

names = [d[0] for d in data]
values = [d[1] for d in data]
flags = [d[3] for d in data]
total = sum(values)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)

ypos = range(len(names))
ax.barh(ypos, values, color=BLUE, edgecolor='none', height=0.62)

ax.set_yticks(ypos)
ax.set_yticklabels(names, color=TEXT, fontsize=12)
ax.invert_yaxis()

# Value labels at the end of each bar
for i, (v, flag) in enumerate(zip(values, flags)):
    label = f'${v:,.0f}bn'
    if flag == 'updated':
        label += '*'
    ax.text(v + 6, i, label, ha='left', va='center',
            color=TEXT, fontsize=11, fontweight='bold')

ax.set_xlim(0, max(values) * 1.18)

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False, length=0)
ax.xaxis.set_visible(False)

# Title block
fig.text(0.02, 0.96, 'OpenAI infrastructure commitments by vendor',
         ha='left', va='top', color=BLACK, fontsize=15, fontweight='bold')
fig.text(0.02, 0.915,
         f'$bn committed 2025-2035  •  total ${total:,.0f}bn across seven vendors  •  as at May 2026',
         ha='left', va='top', color=MUTED, fontsize=11)

# Footnote on the asterisked rows
fig.text(0.02, 0.075,
         '* Amazon AWS and CoreWeave values updated to Q1 2026 disclosures; Tunguz Nov 2025 '
         'baselines were $38bn and $22bn respectively.',
         ha='left', va='top', color=MUTED, fontsize=9, fontstyle='italic')

# Source attribution
fig.text(0.99, 0.01,
         'Source: T. Tunguz, "OpenAI\'s $1.15 Trillion Infrastructure Commitments", 3 Nov 2025; tomtunguz.com',
         ha='right', va='bottom', color=MUTED, fontsize=9, fontstyle='italic')

plt.tight_layout(rect=[0, 0.10, 1, 0.88])

out = HERE / 'openai_vendors_2026-05-16.png'
plt.savefig(out, dpi=150, facecolor=PAPER, edgecolor='none', bbox_inches='tight')
print(f'Wrote {out}')
print(f'Total: ${total}bn across {len(data)} vendors')
