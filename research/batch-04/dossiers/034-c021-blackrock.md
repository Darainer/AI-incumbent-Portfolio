# BlackRock — evidence packet

**Identity/boundary.** BlackRock, Inc. common stock, NYSE:BLK, USD quote/reporting. Cutoff/retrieval 12 September 2026; latest H1/Q2 2026 published 15 July. Unreviewed, G3/G4 deferred. BlackRock has deployed GenAI inside Aladdin and has a first external wealth client, but AUM/fee growth is dominated by markets, flows and acquisitions. No public evidence isolates AI-driven renewal, adviser capacity or retained cash.

## Business and financial resilience

BlackRock earns base fees on public and private assets, performance fees, technology subscription revenue (Aladdin/eFront/Preqin), distribution and advisory fees. iShares scale, institutional relationships, risk infrastructure and switching costs support recurring economics. Market levels and product mix drive AUM and revenue; flows are competitive and fee compression persists. Recent GIP, HPS and Preqin acquisitions expanded private markets/data but increase debt, intangibles, shares and integration risk.

At 30 June 2026 AUM was **$15.345tn** after $192bn Q2 and $321bn H1 net inflows. H1 GAAP revenue was **$13.782bn**, operating income **$5.275bn**, and net income **$4.368bn**; Q2 technology services/subscription revenue grew 13%, ACV 15%. Q2 adjusted operating margin was 45.9%. [Q2 SEC release](https://www.sec.gov/Archives/edgar/data/2012383/000119312526304013/blk-ex99_1.htm) and [10-Q](https://www.sec.gov/Archives/edgar/data/2012383/000119312526337177/blk-20260630.htm), 15 July 2026. Cash-flow comparisons are distorted by consolidated sponsored funds and client settlements; acquisitions materially changed the capital base. Management increased 2026 planned buybacks to $2bn. The conventional business is resilient without incremental AI but exposed to markets, regulation, private-credit losses and fee pressure.

## Data and rights

| Input | Owner/exclusivity | Inference | Training/reuse | Labels/replication |
|---|---|---|---|---|
| Aladdin portfolio/risk data | Client and market/licensor data inside BlackRock platform | Permission-dependent client inference | Copilot page does not establish cross-client training; isolation implied | Rich positions/risk, but outcome labels reflect markets; Bloomberg/SimCorp compete |
| BlackRock investment research/trading history | BlackRock proprietary | Internal investment use | Internal model improvement plausible; exact rights/vendor terms unknown | Performance labels noisy/crowded; alpha decays |
| Preqin private-market data | Contracted/contributed/public; database rights | Licensed analytics | Contributor/licensing terms constrain generative reuse | Scarcer private data but self-reported/stale; PitchBook substitute |
| Morgan Stanley client portfolio/preferences | Morgan Stanley/client controlled | Customer-specific Auto Commentary | No BlackRock pooled-training right disclosed | Highly relevant context; bank owns relationship |

Aladdin’s secure permission layer and workflow integration are assets, but privacy is not exclusivity. Market data vendors and clients retain rights. Foundation-model suppliers can capture value, and customers can use Microsoft/enterprise copilots over their own warehouses.

## Mechanisms/challengers

1. **Aladdin Copilot (generative/agentic assistance).** Permissioned platform data → query/tool orchestration → faster portfolio/risk answers → user capacity and higher product value → subscription renewal/ACV. BlackRock says Copilot is available to all Aladdin clients, bounded to the platform, filtered and not investment advice. This is E2 product availability, not measured production outcome or E4.
2. **Auto Commentary for wealth advisers.** Aladdin risk analytics plus firm CIO view and client portfolio/preferences → generated narrative → reduced research time and more client conversations. Morgan Stanley began access in October 2025, an identified production client. No matched time, suitability-error, client retention or economics were disclosed.
3. **Internal systematic investing/risk.** ML can process signals and allocate risk, but competitive markets rapidly arbitrage common signals. Higher flows/performance cannot be attributed to AI without strategy cohorts and risk-adjusted benchmarks.

Bloomberg and SimCorp are incumbent challengers; Microsoft/custom bank copilots and open models are substitutes. Morgan Stanley owns adviser distribution and can capture most productivity. Market-data licensors may restrict training. Seat reduction could offset higher price if assistants let fewer users do the work.

## Evidence ledger

| Claim | Type/source/date | Scope | Stage | Confounder |
|---|---|---|---|---|
| H1 revenue $13.782bn, OP $5.275bn, net income $4.368bn | Fact, 10-Q, 15 Jul 2026 | Group | financial | HPS/GIP/Preqin, markets |
| AUM $15.345tn and Q2 flows $192bn | Fact, Q2 release | Group | financial | Market beta and acquisitions |
| Aladdin Copilot available to all clients with permission-dependent access | Company product fact, [BlackRock](https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot), opened 12 Sep | Aladdin | E2 offering | “Available” not active use; no denominator |
| Copilot limits advice/out-of-bound queries and filters outputs | Company control claim, same page | Aladdin | E1 | Control effectiveness undisclosed |
| Morgan Stanley first to implement Auto Commentary starting Oct 2025 | Joint company claim, [release](https://www.blackrock.com/aladdin/discover/press-release/aladdin-wealth-launches-ai-enabled-commentary-tool-at-morgan-stanley), 2 Oct 2025 | Wealth advisers | E2 | No productivity/quality result |
| Tech revenue +13% and ACV +15% in Q2 | Fact, Q2 release | Tech segment | financial | Acquisitions, cloud migration, non-AI products |
| Generic copilots yield mixed deep-context results | External qualitative study, [Bano et al.](https://arxiv.org/abs/2503.17661), 22 Mar 2025 | 27 users, other product | E3 external negative | Not Aladdin |

## KPI and materiality

| KPI | Comparator | Eligible workload | Quality | Known | Close gap |
|---|---|---|---|---|---|
| Minutes per resolved risk/workflow task | Existing Aladdin interface | Active Copilot users/tasks | Correct citations, permissions, override/error rates | Unknown | Randomized/stepped rollout telemetry |
| Adviser portfolios serviced/FTE | Morgan Stanley matched advisers | Auto Commentary users | Suitability, complaints, edits, engagement | Unknown | 12-month cohort |
| Incremental ACV/renewal gross profit | Non-Copilot client cohort | Copilot-enabled contracts | Seats/cannibalization and model cost included | ACV growth aggregate only | Renewal pricing disclosure |

Five percent of FY2025 normalized profit is unavailable here, so annualized H1 GAAP operating income gives a labeled scale proxy: `$5.275bn×2×5% = $527.5m/year`. Illustrative revenue bridge: assume $2.0bn eligible annual technology/subscription revenue × 15% price/upsell × 60% adoption × 75% contribution margin × 80% retention after seat cannibalization = **$108m/year**. Internal-cost bridge: $8bn eligible operating expense × 8% efficiency × 35% realization × 60% retention − $100m recurring AI cost = **$34m/year**. Total $142m is below the proxy. Required tech uplift alone after $34m internal benefit is `(527.5-34)/(2000×.6×.75×.8)=68.5%`. All inputs except H1 OP are assumptions.

## Hypotheses/falsifiers/gates

Positive: permissioned Aladdin context and switching costs let BlackRock turn an assistant into higher ACV and multi-product retention while improving internal scale. Negative: customers own the data/relationships, generic copilots replicate the interface, seats fall, and markets/acquisitions explain performance.

Falsifiers: Copilot cohorts show no higher net renewal/ACV after seat effects; adviser studies show no quality-adjusted capacity gain; model/data supplier and control costs consume contribution. Questions: active users, query success/override, pricing, model suppliers, cross-client training prohibition, and acquisition-adjusted tech revenue.

Confidence mechanism medium-high, deployment medium, capture low-medium. G0/G1 provisional pass; G2 provisional/insufficient: identified E2 deployments but no controlled result or retained economics. G3/G4 deferred.

## Sources

1. BlackRock Q2 2026 release, 15 Jul, opened 12 Sep: https://www.sec.gov/Archives/edgar/data/2012383/000119312526304013/blk-ex99_1.htm
2. BlackRock Q2 10-Q, 15 Jul 2026, opened 12 Sep: https://www.sec.gov/Archives/edgar/data/2012383/000119312526337177/blk-20260630.htm
3. BlackRock Aladdin Copilot page, undated, opened 12 Sep: https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot
4. BlackRock/Morgan Stanley Auto Commentary release, 2 Oct 2025, opened 12 Sep: https://www.blackrock.com/aladdin/discover/press-release/aladdin-wealth-launches-ai-enabled-commentary-tool-at-morgan-stanley
5. BlackRock Aladdin overview/customer evidence, opened 12 Sep: https://www.blackrock.com/aladdin
6. BlackRock annual reports, 2025 report, opened 12 Sep: https://ir.blackrock.com/financials/annual-reports-and-proxy/default.aspx
7. Bano et al., Copilot qualitative study, 22 Mar 2025, opened 12 Sep; external/preprint: https://arxiv.org/abs/2503.17661

Capsule: [c021.json](../capsules/c021.json). Verify financial/acquisition confounders, product availability versus active use and arithmetic. Unreviewed.
