# Batch 01 — first ten individual stock reviews

Research cutoff: **12 September 2026**. Status: **ten dossiers completed; independent lead review complete**.

Start with the [lead judgment](lead-review.md). The priority underwriting shortlist is **RELX, Wolters Kluwer and Intuit**. None of the ten is yet designated demonstrably underpriced AI productivity or portfolio eligible.

The first ten follow the existing [priority queue](../priority-queue.md), not a score ranking. Five GPT-5.6 Sol agents with medium reasoning each researched two companies under the committed [agent instructions](../agent-instructions.md). The lead checked decisive evidence and calculations and owns final decisions. Provisional agent opinions remain in the packets for traceability; the lead review governs differences.

| Queue | Company | ID | Evidence packet | Lead disposition |
|---:|---|---|---|---|
| 1 | RELX | C034 | [Dossier](dossiers/01-relx.md) | Priority shortlist |
| 2 | Wolters Kluwer | C035 | [Dossier](dossiers/02-wolters-kluwer.md) | Priority shortlist |
| 3 | Thomson Reuters | C036 | [Dossier](dossiers/03-thomson-reuters.md) | Evidence/price watchlist |
| 4 | Experian | C031 | [Dossier](dossiers/04-experian.md) | Evidence/price watchlist |
| 5 | Intuit | C037 | [Dossier](dossiers/05-intuit.md) | Priority shortlist |
| 6 | SAP | C041 | [Dossier](dossiers/06-sap.md) | Deployment/price watchlist |
| 7 | Siemens | C059 | [Dossier](dossiers/07-siemens.md) | Deprioritize at observed price |
| 8 | Schneider Electric | C060 | [Dossier](dossiers/08-schneider-electric.md) | Deprioritize for this thesis at observed price |
| 9 | Munich Re | C015 | [Dossier](dossiers/09-munich-re.md) | Conventional insurance watchlist |
| 10 | Chubb | C018 | [Dossier](dossiers/10-chubb.md) | Conventional insurance watchlist |

## Review materials

- [Research-agent instructions](../agent-instructions.md): evidence, rights, economics, valuations, source handling and handoff.
- [Independent lead review](lead-review.md): ten decisions, conditional valuations, gate status, scores and conditions that would change the view.
- [Reviewer audit notes](reviewer-audit.md): checks, corrections, overrides and remaining limitations.
- [Reproducible calculations](audit-calculations.py): ten scenario/reverse valuations, scores and selected economics; Python standard library only.

Run `python3 research/batch-01/audit-calculations.py` from the repository root. Models are screening calculations, not qualified price targets. The original universe and framework remain preserved. These manually maintained dossiers must not be regenerated from the original brief generators.
