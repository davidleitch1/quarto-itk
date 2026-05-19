# AI Finance — research project

Multi-session research effort to understand the economics of the AI sector from an investment-bank research-analyst perspective. Focus is on revenue trajectories, capital expenditure, cash-flow dynamics, and the contractual web binding the major players.

## Value chain (working segmentation)

Boundaries blur — the hyperscalers in particular sit in multiple buckets — but the four-bucket frame is a useful starting scaffold.

| Bucket | Role | Examples |
|:--|:--|:--|
| AI customers | Pay for AI products / API / inference | Enterprises (via SaaS or direct API), consumers (ChatGPT Plus, Claude Pro), developer subs |
| AI providers | Build and sell models or AI products | OpenAI, Anthropic, Google (Gemini), Meta (Llama/AI products), xAI, DeepSeek, Mistral, Cohere |
| Infrastructure customers | Buy compute, DC space, chips to run/train AI | The model-makers above; the hyperscalers themselves (Meta is a buyer not a seller); enterprises running private inference |
| Infrastructure providers | Sell compute capacity, DC space, chips, power | AWS, Azure, GCP, Oracle, CoreWeave, Crusoe, Lambda, Nebius; Nvidia, AMD, Broadcom, TSMC; DC developers; utilities |

Hyperscalers (Microsoft, Google, Amazon, Meta, Oracle) operate as both infra providers and infra customers, and Google/Meta/Microsoft also operate as AI providers. The interesting financial questions sit at these seams.

## Adjacent research already done

In `../../background/`:

- `training_v_inference.md` — workload, silicon, memory and lifecycle distinctions (technical, no economics yet)
- `token_memory.md` — token economics primer
- `data_centres_usa.md` — US DC market
- `data_centres_australia_top10_construction.md`, `data_centres_australia_community.md` — AU DC pipeline + community response
- `data_centres_community.md`, `data_centres_industry_response.md` — opposition + industry rebuttals
- `datacentre_locationfactors.md`, `datacentre_opex.md` — siting and operating cost detail
- `backup_power_market.md`, `dc_more_backup_notes.md` — DC backup gen market

These cover the **infrastructure-build physical layer** well. This project takes the next step — the *financial* layer above it.

## Workstreams (see task list)

1. Top-down overview research, last 3 months — **in progress**
2. AI providers list by revenue
3. Infrastructure providers list by GW capacity (extension of /background work)
4. AI customers — who is paying, how much, growth/churn
5. Catalogue of deals, contracts, and financing structures
6. Stage 2: develop informed analytical framework (after exploratory pass)

## Files in this folder

- `README.md` — this file
- `sources.md` — annotated source bibliography, populated as research progresses
- `Kamikaze capex.md` — Economist, 13 May 2026 — the article that prompted this project
- `overview_findings_YYYY-MM-DD.md` — synthesis notes by session

## Style

The reader is David, an experienced electricity-market research analyst now extending coverage into AI/data-centre finance. Numerate, skeptical, value-chain literate. No hand-holding on what EBITDA or capex is; do explain idiosyncratic AI-sector things (e.g. tokens, KV cache, contract terms like "committed cloud spend").
