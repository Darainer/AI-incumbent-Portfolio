# Research-agent instructions — individual stock diligence

Version 1.0 · 12 September 2026 · Owner: lead reviewer

## Mandate and division of responsibility

Collect a falsifiable evidence packet for each assigned company under the existing AI Incumbent Productivity Regime. The question is whether AI makes a scarce incumbent asset more productive, whether shareholders retain a material gain, and what the stock price requires. Do not write promotional investment copy.

Research agents collect facts, test competing explanations, construct transparent scenarios and offer provisional assessments. The lead reviewer audits decisive claims, resolves inconsistencies, calibrates confidence and owns final investment judgments. An agent's recommendation is never automatically promoted to a portfolio decision.

Use GPT-5.6 Sol with medium reasoning for this first batch. One agent handles two related companies, sequentially, so comparisons are consistent. Maximum five concurrent researchers. No nested delegation. This is a bounded initial underwriting pass: aim for 8–12 genuinely useful sources and roughly 1,800–2,800 words per company. Stop repetitive searching when a gap is clearly documented. Quality of sources matters more than count. Seek additional evidence only to resolve a decision-critical uncertainty.

## Inputs and precedence

Read these files before research:
- `framework/investment-thesis.md`
- `framework/research-standard.md`
- `framework/scoring.md`
- `framework/valuation.md`
- `framework/company-memo-template.md`
- The assigned company's existing `research/companies/cNNN.md` and its linked industry thesis.

The live repository framework is the operational standard. Its six structural dimensions and separate evidence/valuation gates supersede operational use of the original 14-dimension score. Preserve the original prior; do not treat it as established evidence. Do not change the framework or generated universe during research.

First ten means the first ten entries in `research/priority-queue.md`, not the ten highest scores.

## Research sequence

### 1. Identify the security and establish the ordinary business

Record issuer, chosen ordinary listing/share class, ticker, exchange, quote currency and reporting currency. Resolve ADR ratios, pence versus pounds and multiple share classes before comparing prices and earnings.

Use the latest annual filing and latest subsequently available reporting update. Capture the fiscal period, publication date and retrieval date separately. Search explicitly for intervening adverse developments, profit warnings, acquisitions, disposals, dilution, debt, litigation and accounting changes.

Explain segments, customer economics, recurring revenue, competitive advantage, balance-sheet resilience and capital allocation. Show how the business performs with zero *additional* AI improvement; existing classical ML and deployed AI remain in the reported baseline.

Minimum financial record, where available:
- Revenue, operating profit and margin; distinguish reported and adjusted definitions.
- Operating cash flow, capex and free cash flow with the exact reconciliation.
- Diluted EPS and share count; net debt/cash, leases or other material claims.
- For insurers: underwriting/combined ratios, reserve effects, catastrophe burden, investment result, book value, regulatory capital and capital returns. Do not impose industrial-company FCF/EV measures on insurance.
- Latest guidance with its exact period and basis.
- Dated ordinary-share price and quote source. Never substitute an undated web snippet for a current quote.

Missing financial items must be marked unknown, with the consequence for valuation.

### 2. Audit the scarce asset and data rights

For every claimed data moat, distinguish:
1. Owned/licensed proprietary content.
2. Customer-specific context used for that customer's workflow.
3. Permissible pooled learning across customers.

Make a compact table of input, origin/owner, exclusivity, retrieval/inference rights, training/cross-customer rights, labels/quality and replication threat. Unknown rights remain unknown. Possessing data does not imply legal permission to train on it. The existence of privacy safeguards does not itself establish economic exclusivity.

Compare the asset with at least one incumbent rival and one credible entrant or substitute. Find primary competitor/customer evidence; recycled coverage of the same press release is one source.

### 3. Trace two or three specific mechanisms

For each material use case, document:
- Scarce asset → task/decision → deployment → quality-adjusted output → economic line → retained shareholder benefit.
- Classification: classical ML/optimization, generative assistance, agentic execution, or AI infrastructure demand.
- Current best alternative and where the incumbent's unique asset improves on a generic model.
- Actual availability, customer deployment and eligible workload; distinguish pilot, rollout and widespread use.
- Whether the feedback is observable, reusable, lawful and incrementally predictive.

Avoid treating equipment sold into data centers as evidence that AI improves the vendor's own operating productivity.

### 4. Build an evidence ledger and challenge attribution

Every decisive claim needs a direct source link, publication date (or undated), access date, page/section, scope, evidence stage and confounder. Tag claims as fact, management claim, inference or assumption.

Use the repository E0–E4 definitions precisely:
- E0: unverified company hypothesis.
- E1: offering/program/capability.
- E2: reported production use, explicitly identifying who reports it.
- E3: controlled or carefully matched quality-adjusted improvement.
- E4: incremental cash economics retained through relevant cohorts/renewals.

Grade individual mechanisms. Strong evidence for one pilot does not grade the entire company. A customer time-saving anecdote is not automatic E3, and aggregate margin expansion is not E4 AI attribution.

Open the sources behind decisive claims. Search snippets are discovery leads. If access fails, label snippet-only information and exclude it from decisive conclusions. Do not invent links, dates, prices, outcomes or precision. Do not use source content dated after the research cutoff. If the latest verifiable source predates the cutoff materially, state the actual information boundary.

Actively seek negative results: failed deployments, weak renewal, price pressure, seat cannibalization, agent bypass, data portability, lower switching costs, model supplier bargaining, inference costs, human verification and customer/regulatory capture.

### 5. Specify measurable proof and economic capture

Provide a KPI contract: KPI/unit, known baseline, comparator, eligible population, quality constraint, observed result/uncertainty and next reporting event. Unknown baselines are a research gap, not zero.

Identify a credible route to at least 5% of normalized operating profit within five years, following the framework's research convention. Label this hurdle as an assumption. Use risk-adjusted earnings/capital for insurers.

For cost mechanisms use:
`retained operating benefit = eligible cost × efficiency × realization × retained share − recurring AI expense`

For revenue mechanisms use incremental contribution after cannibalization, servicing and model costs. For insurance distinguish risk selection from rate cycle, business mix, reserve releases and catastrophe luck. Avoid counting the same capacity as both labor savings and incremental output. Include capex, tax and working capital consistently.

If the inputs are undisclosed, give a clearly illustrative sensitivity or break-even requirement, not a claimed company forecast. Show what must be true, and whether the available evidence establishes it.

### 6. Evaluate the security separately from the mechanism

Supply a simple, reproducible bear/base/bull valuation with dated inputs and transparent formulas where evidence permits. Show:
- Conventional-business economics with no incremental AI uplift.
- Incremental AI contribution separately, including zero/adverse outcomes.
- Horizon, growth, normalized profitability, capital needs, discount/return hurdle and terminal assumptions.
- Equity versus enterprise-value bridge, dividends and dilution treatment.
- Reverse valuation: the growth, margin or sustainable ROE required by the observed price.
- Sensitivity to at least one business and one valuation assumption.

A per-share earnings/dividend model is acceptable for an initial pass if its limitations are explicit; use a suitable equity model for insurers. Never mix adjusted EPS with reported multiples silently. Do not call an option free from a low P/E alone.

If verified price/share/earnings inputs are unavailable, complete the business and AI assessment and mark G3 blocked. Provide conditional valuation thresholds only if the denominator and security are verified. No fabricated buy zone. Do not imply that one year's old earnings are current.

### 7. State competing hypotheses and falsifiers

Provide the strongest positive case and strongest negative case. Separate:
- Core-business failure.
- AI advantage/capture failure.
- Price too demanding despite a good business.

State three specific falsifiers and what observable event would change the assessment. Describe alternatives among peers or waiting for a defined entry/evidence condition.

## Required output per company

Write `research/batch-01/dossiers/NN-company-slug.md` with:
1. Identity, cutoff, actual source/quote dates and short provisional conclusion.
2. Conventional business and dated financial table.
3. Data-rights table.
4. Mechanisms and competitive comparison.
5. Evidence ledger (normally 6–10 material claims).
6. KPI contract and retained-economics bridge.
7. Bear/base/bull and reverse valuation, or explicit blocked items.
8. Risks, falsifiers and peer/inaction alternative.
9. Original six priors and proposed revisions with reasons; unknowns remain unknown.
10. G0–G4 status with reasons and confidence separately for mechanism, deployment, capture and valuation.
11. Source register with titles, direct URLs, publication/access dates and limitations.

Use inline Markdown links near facts and avoid oversized extracts. Write your own synthesis. No more than 25 words quoted from a single non-lyrical source; keep derived prose within each web source's word limit. Prefer tables for exact mappings.

End with a handoff containing: three decisive claims for reviewer verification, strongest counterargument, unresolved blocking questions, provisional disposition, and files written. Agent outputs must be labeled unreviewed until lead review.

## Preservation and handoff

Create a source ledger in the dossier as soon as the first useful sources are found; save progressively. Notify the lead when each company is reviewable so it can be committed remotely immediately. Each agent owns only its assigned dossier paths. Do not overwrite another agent's work, generated files or original briefs. The lead owns GitHub writes, batch index and final judgments; this prevents competing index/branch mutations.

Lead checkpoints: publish this instruction set before dispatch; commit each completed dossier (or valuable partial work if research runs long); commit the review separately. A local save or local commit alone is not proof of remote preservation.

## Lead acceptance checklist

- Security/currency/periods reconcile; live-data limits are conspicuous.
- Every decisive claim has opened primary evidence or a clearly stated limitation.
- Rights, challenger and adverse-evidence checks are present.
- Announcements, deployment, measured efficacy and cash capture are separated.
- Arithmetic reconciles and scenarios are not passed off as facts.
- Prior versus revised judgment and all failed gates remain visible.
- Final conclusion is written by the lead, with reasons for overriding any agent conclusion.
- Do not claim a buy recommendation or valuation qualification where G3 is blocked.
