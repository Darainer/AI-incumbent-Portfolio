# Evidence coverage contract — remaining universe

Version 2.0 · 12 September 2026 · User-directed evidence phase

## Objective and phase boundary

Complete individual research for all remaining 90 companies in the 100-company universe, in nine batches of ten. Use the existing framework without redesigning it. The user has explicitly deferred comparative ranking and detailed bear/base/bull cases until all coverage is complete. Therefore do not generate price targets, investment rankings, new numeric scores, portfolio weights or scenario valuations in this phase. Preserve batch-one work as a historical completed review; its shortlist is provisional and not the final universe ranking.

This contract supersedes the valuation/scoring output requirements in agent-instructions.md for batches 02–10 only. Its evidence, rights, source and integrity requirements remain applicable. Financial baselines and an illustrative materiality bridge remain required because they establish scale, not a valuation.

## Model, ownership and persistence

Five GPT-5.6 Sol agents, medium reasoning, each own 18 companies: two per batch. Assignments and exact owned paths are in coverage-schedule.json. Each agent researches its assigned pair sequentially, writes both dossier and review capsule, notifies the lead as soon as each is ready, then continues to its next assigned pair without waiting for approval. No nested delegation. Write only assigned dossier/capsule paths. The lead owns indexes, acceptance notes and all GitHub mutations. Save source notes early and notify on a useful partial checkpoint if a company takes unusually long. Never wait until all 18 are done to save or notify.

## Required preparation

Read framework/investment-thesis.md, research-standard.md, scoring.md, valuation.md and company-memo-template.md. Read the company record in universe/companies.json, its primary industry thesis in industries, and any existing research/companies/cNNN.md brief. Absence of an initial brief is expected for most companies. These are priors, not verified company evidence. Apply the technical lessons in agent-instructions.md version 1.1.

## Research standard per company

Aim for 1,200–1,800 useful words, excluding the source register if necessary. Use roughly 6–10 useful, independent primary sources: current annual filing, latest interim/trading update, product/deployment evidence, permissions/privacy/contract evidence, and a customer/competitor/adverse source. Source quality and decision relevance take precedence over length or source count. Do not pad with repeated releases. Search for intervening adverse business developments before cutoff. Open decisive sources; snippets alone never establish them. State exact information boundaries if access fails. Never invent facts, links, dates, current availability or source contents. No post-cutoff evidence.

Every dossier must include:

1. Issuer/security identity and reporting currency; no live share quote needed in this phase. Give research cutoff, latest financial period and publication date.
2. Conventional business: assets, segments, customer economics, competition, financial resilience and capital allocation. Provide at least revenue, operating earnings or sector-appropriate profitability, cash/capital metric and debt/capital context. Distinguish reported versus adjusted metrics. Cite sources adjacent to numbers. Explain major cycle, mix, acquisition, accounting or capital confounders.
3. Scarce-asset/data-rights table: input owner, exclusivity, permitted customer-specific inference, training/cross-customer reuse, label quality and replication threat. Unknown contracts stay unknown; possession is not universal training permission.
4. Two or three specific AI mechanisms: asset → task → observed deployment → quality-adjusted output → economic line → retained shareholder gain. Classify classical ML, generative assistance, agentic execution or AI-infrastructure demand. Current deployed ML stays in the ordinary baseline.
5. Evidence ledger: 5–8 decisive claims, direct source, publication date/section, fact/claim/inference/assumption, scope, E0–E4 and confounder. Financial facts sit outside this ladder. E1 capability; E2 reported production; E3 controlled/matched quality-adjusted result; E4 retained incremental cash. Do not upgrade anecdotes, company-wide margin trends or vague transformation targets.
6. One credible incumbent challenger and one substitute/entrant where relevant, with sourced evidence; examine interface bypass, open data, price/seat cannibalization and supplier/customer capture.
7. Measurement contract: KPI/unit, baseline/comparator, eligible workload, quality condition, known result and reporting/research event that could close the gap.
8. Materiality/capture: the framework convention is 5% of normalized operating profit within five years, or risk-adjusted insurer/bank earnings/capital. If normalization is unavailable use a labeled reported-profit scale proxy. Show a reproducible illustrative bridge or break-even requirement using the company's own cost/revenue pool. Inputs that are assumptions must be labeled; no customer savings counted as company costs; no double subtraction of existing AI expense. For pharma use prospective stage-adjusted clinical productivity, not an invented near-term R&D cost percentage.
9. Strongest positive and negative hypotheses, three falsifiers and concrete unresolved questions. State confidence separately for mechanism, deployment and capture. G0/G1/G2 may receive a provisional evidence assessment; G3/G4 are DEFERRED BY USER. Do not label any stock a buy/sell or comparative favorite.
10. Source register: direct URL, publisher, publication date (or undated), retrieval date, section/pages and access limitations. Honor source word/quotation limits. End with a handoff capsule link.

## Mandatory review capsule

Write the assigned JSON capsule with these keys:
- id, company, batch, dossier, cutoff, latest_financial_period
- sources: array of objects {url, title, date, opened, supports}; identify at least one latest financial source and one decisive AI/challenger source
- financial_anchor: {metric, value, unit, period, source_url, caveat}
- ai_claim: {claim, stage, source_url, scope, limitation}
- strongest_counterevidence: {claim, source_url, limitation}
- rights_limit, materiality_summary, arithmetic (inputs/formula/result or not applicable)
- confidence: {mechanism, deployment, capture}
- g2_provisional, unresolved_questions (array), self_check_complete (boolean)

Keep capsules around 250–400 words. They are factual acceptance aids, not replacements for the full dossiers. The lead will independently open decisive sources, sample financial/causal claims, check formulas and reject unsupported assertions before marking coverage accepted. Never claim independent review yourself.

## Stop conditions and honesty

A documented negative result or unavailable company-specific AI proof is a valid completed packet when conventional business, source search, counterargument and gaps are covered. Do not fabricate an AI story merely to fill the universe. Technical source access failures must be explicit. Continue the remaining assignments autonomously, but never mark an unwritten or unsupported packet complete.
