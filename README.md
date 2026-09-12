# AI Incumbent Portfolio

**AI can make scarce business assets more productive. The investment question is who retains the gain.**

Research update **v0.3 · 12 September 2026** — continuing evidence coverage across the full100-company universe.

This repository develops the AI Incumbent Productivity Regime into falsifiable industry theses and a global candidate universe. It begins with assets companies already possess: trusted content, scientific knowledge, customer relationships, operating networks and installed equipment. It then tests deployment, economic capture and valuation separately.

The [coverage dashboard](research/coverage.md) tracks company research across ten batches. The first10 are reviewed; the remaining90 are being researched under the [evidence coverage contract](research/coverage-instructions.md). Comparative ranking and detailed bear/base/bull cases are deferred until coverage is complete. The earlier [batch-one review](research/batch-01/lead-review.md) is preserved as a provisional historical pass.

## Start here

| Read | Purpose |
|---|---|
| [Full universe coverage](research/coverage.md) | Batch progress, source-backed company packets and lead acceptance |
| [First ten stock reviews](research/batch-01/README.md) | Ten evidence packets, independent decisions and reproducible valuation checks |
| [Investment thesis](framework/investment-thesis.md) | The central argument and competing explanation |
| [36 industry theses](industries/README.md) | Asset, AI mechanism, capture, measurement and falsification by area |
| [100-company universe](universe/README.md) | Global candidates with explicit provisional scores and evidence status |
| [First 18 diligence targets](research/priority-queue.md) | Company-specific questions that could reveal underpriced productivity |
| [Investor deck](deck/README.md) | Editable presentation, narrative and PDF reading copy |
| [Research standard](framework/research-standard.md) | Evidence ladder and promotion gates |
| [Source register](sources/README.md) | 22 primary-source records and the preserved origin documents |

## Preserved foundation — v0.1 (11 September 2026)

- A thesis and research contract for 36 areas covering all 11 broad equity sectors.
- A 100-company research universe with six structural priors, 600 written dimension rationales, risks, KPIs and area mappings.
- An 18-company diligence queue spanning professional workflows, risk decisions, industrial operations and scientific output.
- Separate standards for data rights, economic capture, business quality and valuation.

**Scores are analyst hypotheses, not validated quality ratings or buy recommendations.** Fourteen companies have direct company-source coverage: nine at E1 (capability or offering) and five at E2 (reported production use). The other 86 remain E0 structural candidates. There are no E3/E4 claims, completed security valuations or portfolio weights in the original v0.1 snapshot; the separate v0.2 review above adds current diligence without overwriting that snapshot.

The brief's eventual goal is a substantiated 10–20-company shortlist where productivity is underpriced. This release builds the research foundation and candidate set. The [valuation gate](framework/valuation.md) must establish mispricing before any name receives that label.

## Repository structure

| Directory | Contents |
|---|---|
| `framework/` | Thesis, criteria, scoring, valuation, coverage and company memo template |
| `industries/` | One thesis per research area plus machine-readable area definitions |
| `universe/` | CSV/JSON candidate data, score rationales and summary statistics |
| `research/` | Original queue/briefs plus agent instructions, ten reviewed dossiers and lead judgment |
| `sources/` | Preserved user-provided sources and external evidence register |
| `deck/` | Investor presentation, speaker notes, build source and cover asset |
| `scripts/` | Reproducible research generators and integrity checks |

## Rebuild and validate

Python 3.10+ and the standard library are sufficient for the research files:

```bash
python3 scripts/build_research.py
python3 scripts/build_universe.py
python3 scripts/validate.py
```

The manually maintained `research/batch-01/` files and `research/agent-instructions.md` are independent of the original generators.

Edit the source records in the generator scripts and regenerate their Markdown/CSV/JSON views. Edit framework documents directly. The deck uses the separate Artifact Tool workflow documented in [deck/README.md](deck/README.md).

## Research discipline

Use primary evidence, identify inference, retain negative results and distinguish classical ML improvements from new generative or agentic capabilities. Never equate time saved with profit, a product launch with deployment, or a high structural score with an attractive price.

No personal holdings, account balances or private portfolio details are included. This repository contains an investment research hypothesis, not a claimed investment track record.
