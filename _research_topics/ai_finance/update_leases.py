"""One-off update to companies.csv:

1. Drop the redundant `symbol` column (use `ticker` as canonical)
2. Add `leased_usd_bn` column for off-balance-sheet lease commitments
3. Populate cell-by-cell ONLY where we have a defensible per-firm source

Off-balance-sheet lease commitments are the "not yet commenced" lease piece
that sits OUTSIDE GAAP debt — the material gap flagged by Moody's Feb 2026
($662bn aggregate for the Big-5 US hyperscalers). The aggregate is sourced;
the per-firm breakdown is NOT publicly disclosed by Moody's and would
require mining each hyperscaler's 10-K lease footnote.

Cell-by-cell decisions documented below.

Run once: python3 update_leases.py
"""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
CSV = HERE / 'companies.csv'

df = pd.read_csv(CSV)

# ── 1. Drop symbol column ─────────────────────────────────────────────────
if 'symbol' in df.columns:
    df = df.drop(columns=['symbol'])

# ── 2. Add leased_usd_bn column ───────────────────────────────────────────
if 'leased_usd_bn' not in df.columns:
    df['leased_usd_bn'] = pd.NA

# ── 3. Per-cell decisions (defensible source required) ────────────────────
#
# CHIP layer (rows 2-11): off-balance-sheet leases not material for chip
# designers/foundries. TSMC has large equipment finance leases but those
# are ON-balance-sheet under ASC 842 / IFRS 16. Leave blank.
#
# INFRA layer:
#   Microsoft, Alphabet, Amazon, Oracle — Moody's Feb 2026 reports $662bn
#     OBS aggregate for the Big-5 US hyperscalers but does NOT publish a
#     per-firm split. 10-K mining required. LEAVE BLANK (see task #10).
#   Meta — has one publicly-disclosed SPV: Beignet Investor / Hyperion,
#     $27.3bn 144A bond Oct 2025 (DCD source in our sources.md).
#     This is a PARTIAL figure (Meta's total OBS higher), populated with
#     source flagging the partiality.
#   CoreWeave — large GPU + DC lease obligations; not publicly broken out
#     by category. Leave blank.
#   Equinix, Digital Realty — REITs, OBS lease commitments minor relative
#     to property; ground leases are footnoted. Leave blank.
#   Vantage / QTS / CyrusOne — private, unknown.
#   Dell / SMCI / HPE / Lenovo — server OEMs, not lessees of DCs. Blank.
#
# LABS layer:
#   OpenAI / Anthropic — vendor compute commitments ($1.5trn+ aggregate)
#     are NOT off-balance-sheet leases in the traditional sense; they are
#     long-term purchase commitments (compute capacity contracts). Different
#     accounting category. Leave the `leased_usd_bn` column blank for these.
#     (We could add a separate `compute_commits_usd_bn` column later.)
#   SpaceX — inherits xAI's Valor SPV chip lease ($5.4bn, Jan 2026,
#     contracts.csv-sourced). Populate with explicit source.
#   Mistral / Cohere / DeepSeek / Stability / Black Forest / Databricks
#     — small or unknown. Blank.
#
# PRODUCTS layer (SaaS):
#   Salesforce / ServiceNow / Adobe / Workday — office property leases on
#     balance sheet under ASC 842; OBS commitments not material to AI story.
#     Blank.
#   AI-native SaaS — small, unknown. Blank.
#
# FINANCIER layer:
#   Blue Owl / Apollo / Blackstone — they are PROVIDERS of lease financing
#     (via SPVs to hyperscalers); they don't sit on the lessee side. Blank.
#   PIF / QIA / MGX — sovereign, not relevant. Blank.

leased_cells = {
    'Meta Platforms': {
        'value': 27.3,
        'source_note': "leased: DCD Oct 2025 Hyperion/Beignet SPV ($27.3bn) only — partial; total OBS higher per Moody's Feb 2026 Big-5 $662bn aggregate",
    },
    'SpaceX': {
        'value': 5.4,
        'source_note': "leased: contracts.csv Valor Compute Infra LP $5.4bn xAI Colossus 2 GPU triple-net lease (Jan 2026)",
    },
}

for company, data in leased_cells.items():
    idx = df[df['company'] == company].index
    if len(idx) == 0:
        print(f"  WARN: {company} not found")
        continue
    i = idx[0]
    df.loc[i, 'leased_usd_bn'] = data['value']
    existing = df.loc[i, 'source']
    if pd.isna(existing) or not existing:
        df.loc[i, 'source'] = data['source_note']
    else:
        df.loc[i, 'source'] = f"{existing}  |  {data['source_note']}"

# ── 4. Reorder columns ────────────────────────────────────────────────────
col_order = ['company', 'layer', 'sub_segment', 'listing_status',
             'ticker', 'country',
             'mkt_cap_usd_bn', 'debt_usd_bn', 'leased_usd_bn', 'ev_usd_bn',
             'performance_12m_pct', 'source', 'notes']
df = df[col_order]

# ── 5. Write ──────────────────────────────────────────────────────────────
df.to_csv(CSV, index=False)

# ── 6. Cell-by-cell summary printout ──────────────────────────────────────
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print()
print("leased_usd_bn populated:")
print(df[df['leased_usd_bn'].notna()][
    ['company', 'leased_usd_bn', 'source']
].to_string(index=False))
print()
print(f"leased_usd_bn BLANK for {df['leased_usd_bn'].isna().sum()} rows")
print("  Reasons by layer:")
for layer in df['layer'].unique():
    n_blank = df[(df['layer'] == layer) & df['leased_usd_bn'].isna()].shape[0]
    print(f"    {layer}: {n_blank} blank")
