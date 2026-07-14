---
name: newswatch
description: Weekly AI-infrastructure newswatch run — scans inbox, diffs pinned pages, checks earnings and EDGAR, emails David a delta report. Use when the user says "run the newswatch", "/newswatch", or a scheduled session is invoked for the weekly datacentre watch.
---

# Weekly AI infrastructure newswatch

You are running David Leitch's weekly newswatch for the AI-infrastructure coverage program
(context: `data_centres/_work_program.md`, watch-list rationale in `posts/token-industry.md`).
Everything you need to know about WHAT to watch lives in the config; this file is HOW to run.

## Mission — why this watch exists

The phrase lists are aids, not the job. The job is to test a thesis weekly. Read everything you
find against the standing questions in the config ("Standing questions" section) — an event that
matches no phrase but bears on those questions matters MORE than a phrase-match that doesn't.
David is an ex-sell-side utilities analyst covering AI infrastructure for Australian investors,
positioned for the Firmus ASX IPO; judge relevance the way an analyst preparing for that event
would.

## Escalation protocol — how to act on a finding without chasing rats

Default action on anything interesting is to REPORT it in one line, not investigate it.
Escalate to a deep-dive only if the finding plausibly does one of:
  (a) moves a watch-item threshold (config thresholds),
  (b) is a watch-item-3-class event — a deal, rating action, backstop invocation, or prospectus,
  (c) directly contradicts the base case (crossover ~2028; shortage until then).
Limits: at most ONE deep-dive per run; primary sources first (the parties' own releases/filings —
check every party in the chain); stop when you can state what happened, what it changes, and what
to watch next — not when you know everything. Output contract: a ≤300-word annex at the top of
the email plus a dated note in `data_centres/_news/`, and an indicator-log line.
Everything else that tempted you goes in a **Nominations** line in the email — one clause each —
for David to promote or ignore. His replies are your calibration: check state for which past
nominations he engaged with, and weight accordingly.

**Config:** `data_centres/_models/newswatch_config.md` — read first, every run. It is the living
document; if it conflicts with this skill, the config wins.
**State:** `data_centres/_models/newswatch_state.json` — last-seen values. Everything you report
must be a DELTA against state, not a restatement.

## Run procedure

1. **Read config and state.** Note today's date and the window (last run date → today; default 7 days).

2. **Inbox scan.** Using fastmail search_emails, pull the window's emails from each sender on the
   config sender list. Read only those bearing on watch items; summarise deltas in one line each.

3. **Pinned pages.** WebFetch each URL in config `pinned_pages`. Compare the values you extract
   against state. New monthly SemiAnalysis print → report numbers and direction vs thresholds.
   METR doubling-time revision → report. Page unchanged → one line in "Unchanged". A page
   unchanged for >5 weeks → staleness flag. A fetch failure → say so explicitly in the email.

4. **Earnings awareness (dynamic — no static calendar).** WebSearch upcoming earnings dates for
   the config entity list. Flag any reporting in the next 7 days. For any that reported in the
   window just past: search coverage for (a) capex guidance changes, (b) token-volume prints,
   and report against the thresholds in config.

5. **Event queries.** Run each config search phrase through WebSearch (add "past week" framing);
   run each EDGAR phrase against the EDGAR full-text API (URL template in config). Suppress hits
   already in state `seen`. For anything new and material: one line + link + which watch item it
   bears on.

6. **Local data pull.** Run (note: source .zshrc for OPENROUTER_API_KEY — login shells don't read
   it — and use uv if bare python3 lacks matplotlib):
   `source ~/.zshrc; cd "<repo>/../aemo_spot/pngs/scripts" && uv run --with matplotlib,pandas python3 token_demand_meters.py --update`
   Report the new OpenRouter weekly tokens figure and its ~4-week trend.

7. **Compose ONE email** (fastmail send_email) to the address in config:
   - Subject: exactly `[datacentre_agent] AI infrastructure newswatch — YYYY-MM-DD`
     (the bracketed token is constant — David's smart mailbox keys on it; never vary it).
   - If the send tool supports a from/display name, use `datacentre_agent`; otherwise default.
   - Body sections, in order: **Deltas** (each: what changed → which watch item → why it matters,
     one line each); **This week** (earnings/events due); **Unchanged** (single sentence listing
     what was checked and didn't move); **Needs David** (decisions/config suggestions, if any).
   - Hard cap ~300 words unless a threshold was breached or a watch-item-3 event landed —
     then lead with it and take the space it needs.
   - No filler. If a quiet week, the email can be five lines; that is success, not failure.

8. **Log and persist.** Append dated one-line entries for anything that moved to
   `data_centres/_sources/indicator_log.md`. Write updated state JSON (values, seen-lists,
   last_run). Both files must be written even on a quiet week.

9. **Monthly self-review** (first run of each calendar month): end the email with a short
   "Config suggestions" list — entities recurring in results but absent from config; watch items
   unmoved for a quarter that could be demoted; new deal-structure phrases worth adding.
   Propose only; David decides. If he has replied to a previous newswatch email with config
   changes (check inbox scan), apply them to the config file and confirm in this email.

## Style

Australian English. No emphasis adjectives — numbers instead. Never "genuine/genuinely".
Label every figure reported/estimate. Plain prose, no headers beyond the four sections.
