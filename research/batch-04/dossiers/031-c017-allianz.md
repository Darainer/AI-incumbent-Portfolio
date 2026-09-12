# C017 Allianz — evidence dossier

**Unreviewed agent packet. Cutoff:** 12 September 2026. **Security:** Allianz SE registered shares, Xetra: ALV; EUR. **Latest period:** H1 ended 30 June 2026, published 7 August 2026. No valuation/ranking.

## Business and financial baseline

Allianz combines Property-Casualty, Life/Health and Asset Management (PIMCO and AllianzGI). Its insurer asset is claims/exposure history plus distribution; asset-management economics depend on AUM, fees and flows. AI must be separated from pricing cycles, catastrophe luck, reserve development, markets and acquisitions.

The opened [H1 2026 release](https://www.allianz.com/en/mediacenter/news/media-releases/financials/260807-2q-2026-earnings-release.html) reports €98.6bn total business volume, €9.390bn operating profit, €6.385bn shareholder core net income, 20.7% annualized core ROE and 225% Solvency II ratio. P&C operating profit was €4.871bn. Q2 P&C combined ratio was 91.9% (68.1% loss, 23.8% expense), versus 91.2%; prudent run-off affected the loss ratio. Group Q2 operating profit was €4.874bn. Restructuring and IT modernization costs reduce net income and complicate an AI cost-benefit inference.

FY2025 [results](https://www.allianz.com/en/mediacenter/news/media-releases/financials/260226-4q-2025-earnings-release.html) were €186.9bn business volume, €17.374bn operating profit, €11.113bn core net income, 18.1% core ROE and 218% solvency. P&C combined ratio was 92.2%, helped by lower catastrophe losses and underwriting actions; this cannot be attributed to AI. The board proposed €17.10 dividend and announced up to €2.5bn buyback. Capital is strong, but policy liabilities and required solvency replace an industrial net-debt/FCF test.

## Rights audit

| Input | Owner/exclusivity | Use/reuse | Labels | Threat |
|---|---|---|---|---|
| Claims/exposure files | policyholders, brokers and Allianz under policy/privacy terms; partial exclusivity | underwriting/claims inference is plausible; pooled training by jurisdiction/product unknown | frequent retail claims, sparse commercial tails, reserve labels mature slowly | AXA, Zurich and reinsurers have comparable history |
| Telematics/images/documents | customer and third-party provenance | consent and purpose limitation apply; exact retention/training terms unknown | driving/repair labels can be rich but biased | OEMs, repair networks and computer-vision vendors |
| Adviser/policy servicing records | customer/allianz workflows | customer-specific retrieval plausible; cross-client generative use unknown | completion, lapse and complaint labels observable | CRM/LLM vendors commoditize task |
| Asset-management research/client data | proprietary/licensed/confidential mix | licence and fiduciary limits; pooled reuse unknown | trading/flow outcomes noisy and market-driven | BlackRock, Amundi and data platforms |

Allianz privacy and AI-governance statements establish controls, not exclusive training permission. EIOPA's 2025 AI opinion requires fairness, data governance, record keeping, human oversight and cybersecurity.

## Mechanisms and challenge

**Claims triage (ML/computer vision/generative assistance):** documents/images → severity/fraud/next-action → faster accurate resolution → lower loss-adjustment expense and leakage. Allianz has public AI governance and digital claims initiatives, but no opened company source discloses a matched claim cohort, eligible denominator or net expense reduction. Productive use is at most management-reported E2.

**Underwriting/risk selection (classical ML):** exposure and claims histories → price/accept decision → lower accident-year loss ratio at the same risk/price → retained underwriting margin. Current combined ratios reflect rate, mix, cat losses and reserve actions. Without vintage-matched cohorts, company-wide loss performance is not E3.

**Service/adviser assistance (generative/agentic):** policy context → answer, document or action → fewer handling minutes/higher retention → expense ratio or growth. Q2 expense ratio improved only 0.1 point while major restructuring supports IT/AI readiness. This is compatible with investment ahead of benefits, but not cash proof.

AXA is the incumbent challenger; Lemonade and software vendors are entrants/substitutes. Brokers, policyholders and regulators can capture benefits through lower premiums, better service or capital requirements. Model suppliers can capture recurring expense. Negative evidence includes the lack of controlled outcomes, higher Q2 loss ratio, and large restructuring expense associated with legacy-system decommissioning. The strong core business therefore remains the case; AI increment is unproven.

## Evidence ledger

| Claim | Type | Source/date | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| Allianz uses AI and is modernizing systems | management claim | [2025 annual report](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/investor-relations/en/results-reports/annual-report/ar-2025/en-Allianz-Group-Annual-Report-2025.pdf), 2026, digitalization/risk | group | E2 | deployment denominator absent |
| H1 operating profit reached €9.390bn | fact | [H1 release](https://www.allianz.com/en/mediacenter/news/media-releases/financials/260807-2q-2026-earnings-release.html), 7 Aug 2026 | group | financial | markets/mix |
| Q2 P&C ratio 91.9% and expense ratio 23.8% | fact | same, P&C | P&C | financial | cat/run-off/rate |
| AI could improve claims/underwriting | inference | annual report and industry mechanisms | selected workflows | E1 | price/cycle |
| Controlled cohort and retained cash are not disclosed | negative finding | searched issuer/regulatory sources | company | E0 | nondisclosure |
| AI governance creates cost and constrains automation | fact/inference | [EIOPA opinion](https://www.eiopa.europa.eu/publications/opinion-artificial-intelligence-governance-and-risk-management_en), 6 Aug 2025 | EU insurance | E1 | proportionality |

## KPI and materiality

| KPI | Comparator | Eligible | Quality | Known | Proof event |
|---|---|---|---|---|---|
| accident-year loss ratio | matched product/state/rate vintage | AI-priced policies | same exposure/capital/fairness | unknown | 3–5 year cohort |
| claims expense per closed claim | randomized rollout | AI-triaged claims | leakage, appeal, satisfaction | unknown | audited rollout |
| policy handling cost/persistency | matched service books | assistant users | complaints and suitability | unknown | renewal cohort |

Five percent of FY2025 operating profit is **€868.7m**; insurer materiality should ultimately use risk-adjusted earnings/capital. Illustrative P&C bridge: 10 basis points sustainable combined-ratio improvement on €86.7bn FY2025 P&C business volume is €86.7m pre-tax before implementation; achieving €868.7m would require roughly **100 bps**, holding earned premium close to volume and all else constant. Those assumptions are rough and public evidence does not attribute even 10 bps to AI.

## Falsifiers and gates

Positive: scale and claims labels allow better risk and service at lower expense. Negative: cycle/reserving explains results, rules constrain reuse, and savings pass through premiums or vendor cost. Falsifiers: no matched loss-ratio lift; claims speed worsens leakage/appeals; expense gains fail to exceed AI/restructuring cost. Unknown: eligible share, rights, model cost, cohort results and pricing retention.

Confidence: mechanism **medium**, deployment **low-medium**, capture **low**. G0 met; G1 provisionally met; G2 **not passed/limited** because company-specific controlled production economics are absent. G3/G4 deferred.

## Source register

Opened 12 Sep 2026: [H1 2026 release](https://www.allianz.com/en/mediacenter/news/media-releases/financials/260807-2q-2026-earnings-release.html) (7 Aug 2026); [FY2025 results](https://www.allianz.com/en/mediacenter/news/media-releases/financials/260226-4q-2025-earnings-release.html) (26 Feb 2026); [FY2025 annual report](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/investor-relations/en/results-reports/annual-report/ar-2025/en-Allianz-Group-Annual-Report-2025.pdf) (2026); [Allianz privacy](https://www.allianz.com/en/privacy-statement.html) (undated); [Allianz AI governance](https://www.allianz.com/en/about-us/strategy-values/artificial-intelligence.html) (undated); [EIOPA AI opinion](https://www.eiopa.europa.eu/publications/opinion-artificial-intelligence-governance-and-risk-management_en) (6 Aug 2025); [AXA AI](https://www.axa.com/en/press/publications/axa-and-artificial-intelligence) (challenger); [Lemonade annual report](https://www.sec.gov/edgar/browse/?CIK=1691421&owner=exclude) (entrant economics). AI pages support capabilities/governance, not E3 efficacy.

**Handoff:** verify H1 operating profit/solvency; FY2025 P&C ratio confounders; absence of controlled AI cohort. Files: this dossier and [capsule](../capsules/c017.json).
