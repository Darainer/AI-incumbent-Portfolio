# AI Incumbent Portfolio

**AI can make scarce business assets more productive. The investment question is who retains the gain.**

Research update **v0.4 · 12 September 2026** — all 100 companies ranked for operating fit; 25 candidates receive current-price investment judgments and 75 downside/base/bull scenarios.

This repository develops the AI Incumbent Productivity Regime into falsifiable industry theses and a global candidate universe. It begins with assets companies already possess: trusted content, scientific knowledge, customer relationships, operating networks and installed equipment. It then tests deployment, economic capture and valuation separately.

The [coverage dashboard](research/coverage.md) links all 100 company packets across ten completed batches. The [lead synthesis](research/coverage-synthesis.md) explains the findings, corrections and remaining evidence limits. Of the additional 90 packets, 56 passed the recorded source checks and 34 retain explicit limitations; acceptance is a research-completion judgment, not an investment endorsement. The authorized ranking phase is now complete for [all 100 operating ranks](research/ranking-2026-09-12/universe-ranking.md) and [25 investment cases](research/ranking-2026-09-12/lead-decision.md). The other 75 have no current-price valuation in this release. The earlier [batch-one review](research/batch-01/lead-review.md) is preserved as a provisional historical pass.

## Start here

| Read | Purpose |
|---|---|
| [Final ranking and investment judgment](research/ranking-2026-09-12/lead-decision.md) | Current-price priorities, five-year cases and evidence limits |
| [All 25 investment cases](research/ranking-2026-09-12/investment-ranking.md) | Lead ordering,75 downside/base/bull scenarios and entry thresholds |
| [Full universe coverage](research/coverage.md) | Batch progress, source-backed company packets and lead acceptance |
| [Lead synthesis](research/coverage-synthesis.md) | Conclusions from the completed evidence phase, review limits and next-phase boundaries |
| [First ten stock reviews](research/batch-01/README.md) | Ten evidence packets, independent decisions and reproducible valuation checks |
| [Investment thesis](framework/investment-thesis.md) | The central argument and competing explanation |
| [36 industry theses](industries/README.md) | Asset, AI mechanism, capture, measurement and falsification by area |
| [100-company universe](universe/README.md) | Global candidates with explicit provisional scores and evidence status |
| [First 18 diligence targets](research/priority-queue.md) | Company-specific questions that could reveal underpriced productivity |
| [Investor deck](deck/README.md) | Editable presentation, narrative and PDF reading copy |
| [Research standard](framework/research-standard.md) | Evidence ladder and promotion gates |
| [Original source register](sources/README.md) | 22 foundation source records and preserved origin documents; current company sources are in each research packet |

## Preserved foundation — v0.1 (11 September 2026)

- A thesis and research contract for 36 areas covering all 11 broad equity sectors.
- A 100-company research universe with six structural priors, 600 written dimension rationales, risks, KPIs and area mappings.
- An 18-company diligence queue spanning professional workflows, risk decisions, industrial operations and scientific output.
- Separate standards for data rights, economic capture, business quality and valuation.

**Scores are analyst hypotheses, not validated quality ratings or buy recommendations.** In the preserved v0.1 snapshot, fourteen companies had direct company-source coverage: nine at E1 (capability or offering) and five at E2 (reported production use); the other 86 were E0 structural candidates. That original snapshot contains no E3/E4 claims, completed security valuations or portfolio weights. The separate batch reviews add current diligence without overwriting those historical scores and evidence labels; use the current research packets and lead notes for evidence judgments.

The brief's eventual goal is a substantiated 10–20-company shortlist where productivity is underpriced. The current [lead judgment](research/ranking-2026-09-12/lead-decision.md) prioritizes Intuit and Wolters Kluwer, with Accenture as a conventional value candidate. Only those three exceed the illustrative 10% base-return hurdle, with thin cushions; none of the 25 clears 12%. The [valuation gate](framework/valuation.md) still requires sufficient evidence and margin before a name is labeled underpriced productivity.

## Repository structure

| Directory | Contents |
|---|---|
| `framework/` | Thesis, criteria, scoring, valuation, coverage and company memo template |
| `industries/` | One thesis per research area plus machine-readable area definitions |
| `universe/` | CSV/JSON candidate data, score rationales and summary statistics |
| `research/` | 100 dossiers, 90 additional review capsules, lead judgments, source/calculation audits and coverage indexes, alongside the original queue and briefs |
| `sources/` | Preserved user-provided sources and external evidence register |
| `deck/` | Investor presentation, speaker notes, build source and cover asset |
| `scripts/` | Reproducible research generators and integrity checks |

## Rebuild and validate

Python 3.10+ and the standard library are sufficient to validate the research files:

```bash
python3 scripts/validate.py
python3 scripts/coverage_status.py
```

The manually maintained batch dossiers, capsules, audit files and lead reviews are independent of the original generators. Run `python3 scripts/coverage_status.py --write` to rebuild only the coverage and batch indexes from those records.

The original `build_research.py` and `build_universe.py` scripts regenerate the foundation snapshot from their embedded source records; they do not refresh current company research. Edit framework documents directly. The deck uses the separate Artifact Tool workflow documented in [deck/README.md](deck/README.md).

## Research discipline

Use primary evidence, identify inference, retain negative results and distinguish classical ML improvements from new generative or agentic capabilities. Never equate time saved with profit, a product launch with deployment, or a high structural score with an attractive price.

No personal holdings, account balances or private portfolio details are included. This repository contains an investment research hypothesis, not a claimed investment track record.
