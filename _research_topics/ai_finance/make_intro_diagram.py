"""Generate an Excalidraw mud-map of the AI sector value chain.

Output: intro_diagram.excalidraw (open in Excalidraw web or desktop).

v4 — feedback loops moved to a dedicated callout panel below the customer
layer (replacing the broken visual loop arrows); cash-flow badges added to
the left of each layer (+/-/± for 2026e net FCF including inter-sector
equity stakes; current values are back-of-envelope, pending task #9).

Aesthetic — hybrid type:
- Virgil (fontFamily=1, hand-drawn) for titles, headlines, loop labels
- Helvetica (fontFamily=2, clean) for entity lists + body text
- roughness=1 on shapes for the mud-map feel

Run: python3 make_intro_diagram.py
"""
import json
import time
from pathlib import Path

HERE = Path(__file__).parent

# Flexoki Light pastel palette
PAPER = '#FFFCF0'
INK = '#100F0F'
TEXT = '#403E3C'
MUTED = '#6F6E69'
RED = '#AF3029'
GREEN = '#66800B'
AMBER = '#AD8301'

CHIP_FILL = '#BFD8D5'
INFRA_FILL = '#BFCFE7'
LAB_FILL = '#E5C0D5'
PRODUCT_FILL = '#D2D9B0'
CUSTOMER_FILL = '#ECD0B0'
CAPITAL_FILL = '#F0E5B0'

CHIP_STROKE = '#24837B'
INFRA_STROKE = '#205EA6'
LAB_STROKE = '#A02F6F'
PRODUCT_STROKE = '#66800B'
CUSTOMER_STROKE = '#BC5215'
CAPITAL_STROKE = '#AD8301'
LOOP_STROKE = '#AF3029'

now = int(time.time() * 1000)
_seed = [1000]
_id = [10**12]


def next_seed():
    _seed[0] += 1009
    return _seed[0]


def make_id():
    _id[0] += 17
    return str(_id[0])


def base(elem_type, x, y, w, h, **kw):
    e = {
        "id": make_id(),
        "type": elem_type,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": INK,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "seed": next_seed(),
        "version": 1,
        "versionNonce": next_seed(),
        "isDeleted": False,
        "boundElements": [],
        "updated": now,
        "link": None,
        "locked": False,
    }
    e.update(kw)
    return e


def rect(x, y, w, h, stroke=INK, fill='transparent', stroke_width=2, roundness=3):
    return base("rectangle", x, y, w, h,
                strokeColor=stroke,
                backgroundColor=fill,
                fillStyle="solid",
                strokeWidth=stroke_width,
                roundness={"type": roundness} if roundness else None)


def ellipse(x, y, w, h, stroke, fill, stroke_width=2):
    return base("ellipse", x, y, w, h,
                strokeColor=stroke,
                backgroundColor=fill,
                fillStyle="solid",
                strokeWidth=stroke_width,
                roundness=None)


def _text(x, y, txt, size, font, align, color):
    char_w = 0.55 if font == 1 else 0.52
    w = int(len(txt) * size * char_w) + 20
    h = int(size * 1.25)
    e = base("text", x, y, w, h,
             strokeColor=color,
             backgroundColor="transparent",
             roundness=None)
    e["text"] = txt
    e["originalText"] = txt
    e["fontSize"] = size
    e["fontFamily"] = font
    e["textAlign"] = align
    e["verticalAlign"] = "top"
    e["containerId"] = None
    e["lineHeight"] = 1.25
    e["baseline"] = int(size * 0.9)
    return e


def title(x, y, txt, size=22, color=INK):
    return _text(x, y, txt, size, font=1, align='left', color=color)


def body(x, y, txt, size=15, color=TEXT, bold=False):
    return _text(x, y, txt, size, font=2, align='left',
                 color=INK if bold else color)


def annot(x, y, txt, size=12, color=MUTED):
    return _text(x, y, txt, size, font=2, align='left', color=color)


def arrow(x1, y1, x2, y2, stroke=INK, width=2, points=None):
    dx = x2 - x1
    dy = y2 - y1
    bbox_w = max(1, abs(dx))
    bbox_h = max(1, abs(dy))
    e = base("arrow", x1, y1, bbox_w, bbox_h,
             strokeColor=stroke,
             strokeWidth=width,
             roundness={"type": 2})
    if points is None:
        e["points"] = [[0, 0], [dx, dy]]
    else:
        e["points"] = points
    e["startBinding"] = None
    e["endBinding"] = None
    e["startArrowhead"] = None
    e["endArrowhead"] = "arrow"
    e["lastCommittedPoint"] = None
    return e


def cf_badge(y_center, sign, color):
    """Cash-flow badge (filled ellipse with +/- sign) at the left of a layer."""
    size = 42
    bx = 20
    by = y_center - size // 2
    elems = [
        ellipse(bx, by, size, size, stroke=color, fill=color, stroke_width=2),
    ]
    # Centre the sign inside the ellipse via the text-element width hack.
    # Virgil at 28pt: "+" is ~16px wide, "-" similar. Centre by hand.
    sign_x = bx + 11 if sign == '+' else bx + 13
    sign_y = by + 4
    elems.append(_text(sign_x, sign_y, sign, size=28, font=1,
                       align='left', color=PAPER))
    return elems


elements = []

# ─── Title block ──────────────────────────────────────────────────────────
elements += [
    title(80, 30, "AI sector — value chain", size=30),
    body(80, 75, "Layers, contracts, and the loops that bind them  ·  16 May 2026",
         size=14, color=MUTED),
]

# ─── Cash-flow badges (left of each layer) ────────────────────────────────
# Current rough estimates — see task #9 for vetted numbers
# Layer y-centres: chip 195, infra 355, labs 515, products 675, customers 835
elements += cf_badge(195, '+', GREEN)   # Chip — net positive after AI equity outflows
elements += cf_badge(355, '-', RED)     # Infra — strongly negative (capex >> op cash)
elements += cf_badge(515, '-', RED)     # Labs — strongly negative (loss-making)
elements += cf_badge(675, '+', GREEN)   # Products — modestly positive (SaaS strength)
elements += cf_badge(835, '-', RED)     # Customers — negative on AI-specific spend

# ─── Layer 1: Chip / silicon ──────────────────────────────────────────────
y, h = 130, 130
elements += [
    rect(80, y, 1020, h, stroke=CHIP_STROKE, fill=CHIP_FILL),
    title(100, y + 12, "1. Chip / silicon  ·  ~$380bn AI merchant silicon (CY2026e)", size=20),
    body(100, y + 50, "Nvidia (Blackwell, Rubin)  ·  AMD (MI400)  ·  Broadcom (custom)  ·  HBM (SK Hynix, Samsung, Micron)"),
    body(100, y + 78, "+ captive hyperscaler silicon — Google TPU, Meta MTIA, MS Maia, AWS Trainium  (~$60–90bn shadow)",
         color=MUTED),
    annot(100, y + 104,
          "Nvidia DC ~$285bn  ·  Broadcom AI ~$40bn  ·  HBM ~$35bn  ·  AMD AI ~$11bn  ·  Marvell+Astera ~$9bn  ·  excludes TSMC foundry (input to all)"),
]
elements += [
    arrow(180, y + h + 4, 180, y + h + 28, stroke=CHIP_STROKE),
    annot(200, y + h + 6, "chip sales"),
]

# ─── Layer 2: Infrastructure ──────────────────────────────────────────────
y, h = 290, 130
elements += [
    rect(80, y, 1020, h, stroke=INFRA_STROKE, fill=INFRA_FILL),
    title(100, y + 12, "2. Infrastructure providers  ·  ~$310bn AI cloud + DC services (CY2026e)", size=20),
    body(100, y + 50, "Hyperscalers  ·  Azure  ·  GCP  ·  AWS  ·  Oracle (Stargate)  ·  Meta DCs"),
    body(100, y + 78, "Neoclouds  ·  CoreWeave, Crusoe, Lambda, Nebius  +  DC developers + AI-server OEMs (Dell, Supermicro)"),
    annot(100, y + 104,
          "Narrow: disclosed AI rev + neoclouds + OEM gross  ·  Broad (cloud × AI-share): ~$540bn  ·  2026 capex aggregate ~$800bn  ·  FCF collapsing 4 of 5 hyperscalers"),
]
elements += [
    arrow(180, y + h + 4, 180, y + h + 28, stroke=INFRA_STROKE),
    annot(200, y + h + 6, "compute capacity  (RPO contracts)"),
]

# ─── Layer 3: AI labs ─────────────────────────────────────────────────────
y, h = 450, 130
elements += [
    rect(80, y, 1020, h, stroke=LAB_STROKE, fill=LAB_FILL),
    title(100, y + 12, "3. AI model providers (labs)  ·  ~$130bn frontier ARR (YE 2026e)", size=20),
    body(100, y + 50, "Frontier  ·  OpenAI  ·  Anthropic  ·  xAI  ·  Google DeepMind  ·  Meta-AI"),
    body(100, y + 78, "Specialist + open  ·  Mistral  ·  Cohere  ·  DeepSeek  ·  Stability  ·  Black Forest"),
    annot(100, y + 104,
          "OpenAI YE ~$55bn  ·  Anthropic YE ~$60bn  ·  xAI ~$2bn  ·  tail ~$5bn  ·  YE run-rate, not CY revenue  ·  vendor commits $1.5trn+ across 5-10y"),
]
elements += [
    arrow(180, y + h + 4, 180, y + h + 28, stroke=LAB_STROKE),
    annot(200, y + h + 6, "IP / API licence"),
]

# ─── Layer 4: Products / Applications ─────────────────────────────────────
y, h = 610, 130
elements += [
    rect(80, y, 1020, h, stroke=PRODUCT_STROKE, fill=PRODUCT_FILL),
    title(100, y + 12, "4. AI products & applications  ·  ~$155bn AI-product ARR (YE 2026e)", size=20),
    body(100, y + 50, "Consumer  ·  ChatGPT  ·  Claude.ai  ·  Gemini app"),
    body(100, y + 78, "Enterprise  ·  Microsoft 365 Copilot  ·  Workspace AI  ·  Salesforce  ·  ServiceNow"),
    body(100, y + 104, "AI-native  ·  Cursor  ·  Glean  ·  Harvey  ·  Cresta  ·  Sierra  ·  Decagon",
         color=MUTED),
]
elements += [
    arrow(180, y + h + 4, 180, y + h + 28, stroke=PRODUCT_STROKE),
    annot(200, y + h + 6, "subscription / per-seat / per-token"),
]

# ─── Layer 5: Customers ───────────────────────────────────────────────────
y, h = 770, 130
elements += [
    rect(80, y, 1020, h, stroke=CUSTOMER_STROKE, fill=CUSTOMER_FILL),
    title(100, y + 12, "5. AI customers  ·  $2.5trn 2026 AI spend (Gartner, broad)", size=20),
    body(100, y + 50, "Enterprise  ·  Consumer  ·  Developer  ·  Public sector"),
    title(100, y + 80, "McKinsey: 94% of adopters report no significant value yet", size=15,
          color=RED),
    annot(100, y + 108,
          "Gartner: 88% of agent pilots fail to graduate to production  ·  the demand-side question on which the whole stack rests"),
]

# ─── Feedback loops panel (below customer layer) ──────────────────────────
panel_y, panel_h = 920, 210
elements += [
    rect(80, panel_y, 1020, panel_h, stroke=LOOP_STROKE,
         fill='transparent', stroke_width=1),
    title(100, panel_y + 12,
          "Two feedback loops drive the sector's circularity",
          size=17, color=LOOP_STROKE),
]
# Loop 1
elements += [
    title(100, panel_y + 50,
          "Loop 1 — Vendor financing  (chip-makers <-> labs)",
          size=14, color=LOOP_STROKE),
    body(115, panel_y + 78,
         "Chip-makers -> labs:  ~$188bn strategic equity  (Nvidia $100bn -> OpenAI;  AMD $90bn warrants -> xAI)",
         size=12, color=TEXT),
    body(115, panel_y + 100,
         "Labs -> chip-makers:  ~$1trn+ chip purchases  (Stargate, Broadcom custom, direct GPU orders)",
         size=12, color=TEXT),
]
# Loop 2
elements += [
    title(100, panel_y + 130,
          "Loop 2 — Anchor customer + investor  (hyperscalers <-> labs)",
          size=14, color=LOOP_STROKE),
    body(115, panel_y + 158,
         "Hyperscalers -> labs:  ~$88bn strategic equity  (Microsoft $13bn, Amazon $25bn, Alphabet $20bn)",
         size=12, color=TEXT),
    body(115, panel_y + 180,
         "Labs -> hyperscalers:  ~$1.5trn+ compute commits  (OpenAI-Oracle, Anthropic-AWS, Anthropic-GCP)",
         size=12, color=TEXT),
]

# ─── External capital column (right side) ─────────────────────────────────
cx, cy, cw, ch = 1280, 130, 300, 770
elements += [
    rect(cx, cy, cw, ch, stroke=CAPITAL_STROKE, fill=CAPITAL_FILL),
    title(cx + 18, cy + 10, "External capital", size=20),
    body(cx + 18, cy + 44, "(transverse — feeds multiple layers)", size=11, color=MUTED),
]

def cap_section(yoff, head, bullets):
    items = [body(cx + 18, cy + yoff, head, size=13, color=INK)]
    for i, b in enumerate(bullets):
        items.append(body(cx + 28, cy + yoff + 22 + i * 18, "·  " + b,
                          size=11, color=TEXT))
    return items

elements += cap_section(78, "Bond market", [
    "Big-5 hyperscalers $260bn IG since 2025",
    "xAI $5bn 12.5% secured notes",
])
elements += cap_section(146, "Private credit", [
    "Apollo + Blackstone $35bn -> Broadcom",
    "Apollo $3.5bn -> Valor SPV -> xAI",
])
elements += cap_section(214, "Sovereign wealth", [
    "Humain / PIF $3bn -> xAI",
    "QIA  ·  MGX  ·  OIA across rounds",
])
elements += cap_section(282, "VC pool", [
    "Sequoia  ·  a16z  ·  Valor  ·  Fidelity",
    "Mostly stacked on the model labs",
])
elements += cap_section(350, "Strategic equity (chip-makers)", [
    "Nvidia $100bn -> OpenAI",
    "AMD $90bn warrants -> xAI",
])
elements += cap_section(418, "Off-balance-sheet leases", [
    "Hyperscaler DC commits $662bn (Moody's)",
    "Meta Hyperion SPV $27.3bn (Beignet)",
])

elements += [
    title(cx + 18, cy + 520, "Headline magnitudes", size=14),
    body(cx + 28, cy + 552, "Operating commits (matrix)  ~$1.5trn", size=11, color=TEXT),
    body(cx + 28, cy + 574, "Financing commits (matrix)  ~$0.4trn", size=11, color=TEXT),
    body(cx + 28, cy + 596, "Off-balance-sheet leases   ~$0.7trn", size=11, color=TEXT),
    title(cx + 18, cy + 626, "Forward total  =  $2.6trn+ of paper", size=13, color=INK),
]

# Updated legend — no more loop arrows, add cash-flow badge explanation
elements += [
    title(cx + 18, cy + 680, "Legend", size=13),
    body(cx + 28, cy + 706, "->  primary contract flow (downstream)", size=10, color=TEXT),
    body(cx + 28, cy + 722, "->  external capital injection (yellow)", size=10, color=CAPITAL_STROKE),
    body(cx + 28, cy + 738, "+ / -  2026e net cash flow (incl. equity stakes)", size=10, color=TEXT),
]

# ─── External-capital → layer arrows ──────────────────────────────────────
elements += [
    arrow(cx, 355, 1100, 355, stroke=CAPITAL_STROKE),
    annot(1108, 332, "-> debt", color=CAPITAL_STROKE),
]
elements += [
    arrow(cx, 515, 1100, 515, stroke=CAPITAL_STROKE),
    annot(1108, 492, "-> equity", color=CAPITAL_STROKE),
]

# ─── Footer / source ──────────────────────────────────────────────────────
elements += [
    body(80, 1150,
         "ITK Research  ·  May 2026  ·  Layers 1, 2, 5 in CY2026 revenue; Layers 3, 4 in YE run-rate ARR",
         size=11, color=MUTED),
    body(80, 1170,
         "Layer sizes are NOT additive — same dollar flows through multiple tiers; net distinct merchant value-add across chain ~$700–900bn (not $3trn+)",
         size=11, color=MUTED),
    body(80, 1190,
         "Cash-flow badges are back-of-envelope; pending vetted per-layer FCF calculation (task #9)",
         size=11, color=MUTED),
]

# ─── Assemble + write file ────────────────────────────────────────────────
file_data = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "gridSize": None,
        "viewBackgroundColor": PAPER,
    },
    "files": {},
}

out = HERE / 'intro_diagram.excalidraw'
out.write_text(json.dumps(file_data, indent=2))
print(f'Wrote {out}')
print(f'Elements: {len(elements)}')
