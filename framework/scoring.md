# Scoring without false precision

## Two different assessments

The supplied regime proposes 14 dimensions scored 0–5, including valuation. This release preserves the original document but changes the operational implementation: structural opportunity, evidence and valuation stay separate. A high asset score cannot compensate for unusable data, failed deployment or an excessive share price.

The initial universe contains **analyst structural priors**. These values express which hypotheses look promising enough to investigate. They are not evidence-calibrated probabilities, observed performance, buy ratings or expected returns. They must be revised after company research.

## Six structural dimensions

| Dimension | Weight | 1: weak hypothesis | 3: plausible but conditional | 5: especially strong structural hypothesis |
|---|---:|---|---|---|
| Scarce asset | 20% | Readily replicated inputs | Valuable asset with incomplete exclusivity | Hard-to-reproduce asset with potential lawful differentiated use |
| AI leverage | 20% | Peripheral administrative work | Material workflow with deployment limits | Core high-value decisions or output can change substantially |
| Feedback | 15% | Few useful outcome labels | Some reusable outcomes, uncertain rights or frequency | Frequent, relevant outcome feedback could reinforce performance |
| Testability | 10% | Slow or weakly observable outcomes | Matched pilots feasible with constraints | Rapid controlled tests and clear quality metrics |
| Distribution | 15% | Expensive new customer acquisition | Established access but costly integration | Existing channel can distribute improvements widely |
| Capture | 20% | Competitive or contractual pass-through likely | Partial retention under conditions | Strong structural mechanism to retain a meaningful share |

Scores 2 and 4 represent intermediate judgments. Zero means an explicitly failed mechanism. Unknown is blank/null, never zero. This first edition intentionally supplies all six *priors*, but none is promoted into an evidence-validated score. Read the 600 dimension rationales alongside the company risks.

`structural_prior = sum(weight × dimension_prior / 5)`

Weights sum to 100. Ranking is sensitive to reasonable weight changes and judgment error. Differences of a few points are not meaningful. The 18-name queue also values cross-industry learning and uncertainty reduction, so it is deliberately not the top 18 numeric scores.

## Original framework crosswalk

| Original dimension | Operational treatment |
|---|---|
| Proprietary data | Scarce-asset prior, then rights and replication audit |
| Data quality | Mandatory usability gate, unknown until verified |
| Feedback loop | Feedback prior, then marginal predictive lift and permissions |
| AI leverage | Core-economics prior and materiality test |
| Domain expertise | Business qualification and validation capability |
| Experiment capability | Testability prior |
| Scale | Asset and distribution hypotheses, no separate double-counting bonus |
| Capital | Balance-sheet and investment-capacity gate |
| Distribution | Distribution prior |
| Switching costs | Asset/capture hypotheses, tested against challengers |
| Market growth | Explicit demand-expansion scenario |
| Value capture | Capture prior, followed by cash-flow reconciliation |
| Management execution | Evidence of production adoption, incentives and process change |
| Valuation | Separate dated valuation gate, currently unassessed |

The original 55–70 interpretation must not be applied to the new 0–100 priors. There is no automatic threshold for a core holding.

## Evidence-adjusted work

During diligence, retain both the original prior and a newly justified posterior assessment. Cite evidence for every revision and record unresolved inputs. Avoid multiplying a subjective score by an evidence-stage number: it produces a precise-looking value without a defensible probability interpretation.

Check sensitivity with alternative weights, especially capture at 30% and feedback at 5%. If a candidate only looks attractive under one convenient weighting, treat it as fragile. Economic scenarios and failed gates carry more decision weight than a composite score.
