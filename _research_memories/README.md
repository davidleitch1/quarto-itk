---
title: "Research memories — persistent log of past research projects"
draft: true
---

# Research memories

This directory is a persistent log of past research projects, kept separate from the auto-memory system in `~/.claude/projects/.../memory/` so that long-form project records don't clog the daily-use memory.

## What goes in here

One file per research project / publication thread. Each file captures:

- **Topic and dates** — what was researched, when
- **Key outputs** — published articles, background notes, charts, data files
- **Headline numbers** — the load-bearing figures that future work may reference
- **Methodology notes** — assumptions, calibration choices, sensitivity ranges
- **User preferences expressed during the work** — voice, framing, what was approved vs declined
- **Open questions** — what wasn't resolved, what to pick up next time

## What does NOT go in here

- Short-term task state (use a Plan)
- General preferences / feedback (use `~/.claude/.../memory/` for those)
- Code or scripts (those live in the relevant project folder)
- Draft article text (that lives in `background/_research_drafts/`)

## How to use

When starting work on a topic that may have been covered before, **check this directory first**. The file names should make the index navigable. Cross-references to other directories (`posts/`, `background/`, `aemo_spot/pngs/`) are preserved relative to the `itk_articles/` repo root.

## Quarto rendering

This directory begins with `_` so Quarto will skip it during the website build. Files inside also use `draft: true` for belt-and-braces — but the leading underscore is the load-bearing protection.

## Index

| File | Topic | Period |
|:-----|:------|:-------|
| `data_centre_backup_2026.md` | Data centre backup architecture: diesel, batteries, OCGT, transmission cost allocation | 2026-05 |
| `diesel_oil_imports_2026.md` | Australian diesel use & oil imports: consumption data sources, electrification scorecard, Fortescue, coal-intensity signal | 2026-03/04 |
