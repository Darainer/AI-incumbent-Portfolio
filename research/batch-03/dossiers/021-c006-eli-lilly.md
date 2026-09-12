# C006 Eli Lilly — evidence dossier

**Unreviewed agent packet. Cutoff:** 12 September 2026. **Security:** Eli Lilly and Company common stock, NYSE: LLY; USD quote/reporting currency. **Latest period:** Q2 ended 30 June 2026, released 5 August 2026. Valuation and ranking are deferred.

## Business and current financial base

Lilly develops and commercializes patented medicines, with current economics increasingly concentrated in tirzepatide brands Mounjaro and Zepbound. Its durable assets are validated scientific/clinical capabilities, experimental history, manufacturing, regulatory execution and commercial access. AI discovery is economically relevant only if it raises prospective, stage-adjusted useful output; more virtual candidates alone do not matter.

The [Q2 2026 release](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full) reports revenue of $23.0bn, up 48%, and net income $7.1bn / reported EPS $7.94. Volume rose 60% while realized prices fell 13%. Mounjaro generated $9.94bn and Zepbound $4.93bn, nearly 65% of quarterly revenue, exposing the base to incretin competition, reimbursement and manufacturing execution. Guidance moved to $85–87bn 2026 revenue. FY2025 [Form 10-K](https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm) reports $65.179bn revenue, $26.30bn operating income, $20.63bn net income, $13.337bn R&D expense, roughly $16.8bn operating cash flow and $7.3bn year-end cash. Debt and very large manufacturing commitments matter; acquisitions and acquired IPR&D make annual earnings uneven.

The 2026 surge comes from marketed medicines and supply, not evidence that AI improved discovery. The [11 September AtaiBeckley completion](https://lilly.gcs-web.com/news-releases/news-release-details/lilly-completes-acquisition-ataibeckley-advance-therapies) also shows Lilly still buys external pipeline assets. Capital allocation spans internal R&D, manufacturing capacity, acquisitions and dividends; attribution must compare matched programme cohorts.

## Scarce assets and rights

| Input | Owner/exclusivity | Inference/training rights | Labels/quality | Replication |
|---|---|---|---|---|
| Lilly assays and experimental results | Lilly-generated; some partner/licensor obligations | TuneLab shows Lilly can train and expose selected models, not that every partnered dataset is reusable | rich failed/successful assays; laboratory endpoints can be noisy proxies | rival pharma also owns large archives |
| Clinical-trial/patient data | participants, sites, sponsors under consent and regulation | secondary use depends on consent, protocol and jurisdiction; cross-trial training scope unknown | clinically meaningful but slow, missing and population-shifted | public trials plus licensed real-world datasets |
| TuneLab partner data | biotech partner proprietary data | platform is described as federated/privacy-preserving; direct transfer is limited | new partner experiments could improve local decisions; pooled feedback rights undisclosed | Benchling, NVIDIA and biotech platforms can distribute models |
| Patents/validated molecules | Lilly/license owners | conventional IP and licence terms control commercialization | regulatory endpoints are high-quality late labels | competing mechanisms and generics after exclusivity |

## Mechanisms and challenge

**Discovery-model assistance (ML/generative).** Experimental data → molecule/property prediction → laboratory candidates → validated leads → eventually risk-adjusted pipeline value. [Lilly TuneLab](https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies) launched in September 2025 with models built from data generated through more than $1bn of research investment. Benchling announced access for 1,300-plus biotech customers in January 2026. This is real product/platform availability and internal daily use (E1/E2 by management), but no prospective phase-transition result.

**AI factory and active learning.** An owned NVIDIA DGX SuperPOD is intended to train on millions of experiments, select new experiments and support discovery, development, manufacturing and medical imaging. This expands search and may shorten design-make-test cycles; wet-lab capacity, toxicity and clinical validation remain bottlenecks. It is E1 infrastructure/deployment, not clinical efficacy.

**Federated partner learning.** External biotechs access Lilly models without exposing raw proprietary data. Lilly may gain ecosystem reach and possibly privacy-safe model improvement, but commercial terms and reciprocal-learning rights are undisclosed. It could transfer more value to partners or NVIDIA than Lilly shareholders.

Merck, Roche and AstraZeneca are incumbent challengers with their own archives and partnerships. Insilico, Recursion and Variant Bio are specialized entrants; Variant's 2026 Boehringer collaboration illustrates that exclusive human-genetic or platform data can compete. Negative evidence is decisive: no AI-originated Lilly cohort has disclosed matched Phase II/III success or risk-adjusted value. TuneLab's openness may diffuse models. Massive compute and lab investment raises cost before outcomes, and current earnings concentration in two drugs makes AI immaterial to the near-term base.

## Evidence ledger

| Claim | Type | Source/date | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| TuneLab exposes models trained on >$1bn research investment | management fact/claim | [launch](https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies), 9 Sep 2025 | discovery models | E1 | spend is not data value |
| Models are used every day by Lilly scientists | management claim | same | undisclosed internal population | E2 | eligible workload absent |
| Benchling makes TuneLab available to 1,300+ biotechs | partner fact | [Benchling](https://www.benchling.com/blog/benchling-lilly-tunelab-partnership), 8 Jan 2026 | potential users | E1 | access is not adoption/outcome |
| SuperPOD trains on millions of experiments | supplier/company claim | [NVIDIA](https://blogs.nvidia.com/blog/lilly-ai-factory-drug-discovery/), 28 Oct 2025 | Lilly R&D | E1 | no prospective success data |
| Federated design limits raw-data exposure | company/supplier claim | same | TuneLab partners | E1 | improvement rights unknown |
| AI has improved clinical transitions | unsupported hypothesis | searched sources through cutoff | company pipeline | E0 | no matched cohort disclosed |
| Current profit growth reflects GLP-1 volume | financial fact | [Q2 release](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full), 5 Aug 2026 | company | financial | price, mix, supply |

## KPI and materiality contract

| KPI | Baseline/comparator | Eligible workload | Quality | Known | Closing event |
|---|---|---|---|---|---|
| validated leads per lab-dollar | matched modality/area/vintage conventional programmes | prospective AI-assisted campaigns | same potency, selectivity, toxicity | unknown | preregistered cohort after lead optimization |
| Phase II→III and approval transition | matched stage/area/vintage | AI-influenced programmes identified ex ante | safety, efficacy, diversity | unknown | cohort maturity over 3–7 years |
| time/spend to kill weak programmes | historical matched programmes | AI-ranked candidates | no later false-negative harm | unknown | portfolio review with abandoned projects |

The 5% annual operating-profit screen is 5% × FY2025 $26.30bn = $1.315bn annual pre-tax profit. Programme NPV cannot be compared directly with that annual hurdle. A valid bridge must annualize and tax/discount on a common basis. Illustrative only: if AI creates $2.0bn incremental **after-tax NPV** across a five-year cohort (assumption), an equivalent five-year annuity at an 8% discount rate is $2.0bn / 3.9927 = **$0.501bn after tax per year**. Converting the $1.315bn pre-tax hurdle at an assumed 18% tax rate gives $1.078bn after tax annually; the illustration falls short. No source establishes the $2bn input, so materiality remains unbridged. Do not apply a percent saving to the $13.337bn R&D line: faster discovery may shift spend into more experiments or clinical development.

## Falsifiers and gates

Positive: Lilly's unusually broad proprietary experiment base plus wet-lab and clinical execution improves prospective stage-adjusted output. Negative: models diffuse through partners while biology and trials remain bottlenecks; current profit rests on GLP-1, and compute increases expense.

Falsifiers: (1) prospective AI cohorts do not improve matched lead/transition rates; (2) validation spend and time rise enough to offset design acceleration; (3) licensing/partner terms prevent useful feedback or competitors match performance on public/licensed data. Unresolved: programme tagging, negative-result coverage, rights, total AI cost and stage-specific transition data.

Confidence: mechanism **medium**, deployment **medium**, capture **low**. G0 met; G1 provisionally met with concentration/capital risks; G2 **not yet passed** because deployment is E1/E2 but prospective clinical/productivity evidence is absent. G3/G4 deferred.

## Source register

Opened/accessed 12 Sep 2026: [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm) (12 Feb 2026; statements/R&D/debt); [Q2 2026 results](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full) (5 Aug 2026); [TuneLab launch](https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies) (9 Sep 2025); [Benchling integration](https://www.benchling.com/blog/benchling-lilly-tunelab-partnership) (8 Jan 2026); [NVIDIA AI factory](https://blogs.nvidia.com/blog/lilly-ai-factory-drug-discovery/) (28 Oct 2025); [pipeline](https://www.lilly.com/discovery/clinical-development-pipeline) (accessed cutoff); [FDA AI medical-products paper](https://www.fda.gov/media/177030/download) (Mar 2024); [Variant Bio entrant](https://www.variantbio.com/newsroom/variant-bio-launches-inference) (6 Jan 2026); [AtaiBeckley completion](https://lilly.gcs-web.com/news-releases/news-release-details/lilly-completes-acquisition-ataibeckley-advance-therapies) (11 Sep 2026). The exact issuer Q2 2026 results and TuneLab release URLs were independently reopened during source audit. The corrected FY2025 SEC accession is 0000059478-26-000013. No controlled Lilly AI clinical cohort was found.

**Handoff:** verify Q2 concentration/financials; TuneLab's >$1bn data claim/daily use; lack of prospective transition proof. Counterargument: current economics are GLP-1-driven and AI may diffuse. Files: this dossier and [capsule](../capsules/c006.json).
