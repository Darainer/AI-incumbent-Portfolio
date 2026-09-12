#!/usr/bin/env python3
"""Validate research coverage and rebuild evidence-phase indexes (no network calls).

Existing framework/universe and batch-one work are never modified.
An agent's completed packet and a lead-accepted packet are different states.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Rebuild coverage and batch indexes")
    parser.add_argument("--capsules", nargs="*", help="Print selected available capsules by company ID")
    args = parser.parse_args()
    schedule = json.loads((RESEARCH / "coverage-schedule.json").read_text())
    review_file = RESEARCH / "coverage-review.json"
    reviews = json.loads(review_file.read_text()) if review_file.exists() else {}
    universe = json.loads((ROOT / "universe/companies.json").read_text())
    expected = {x["id"] for x in universe}
    scheduled = [x["id"] for x in schedule["remaining"]]
    initial = schedule["completed_batch_01"]
    assert len(expected) == 100 and len(scheduled) == 90 and len(set(scheduled)) == 90
    assert set(initial).isdisjoint(scheduled) and set(initial + scheduled) == expected
    required = {"id", "company", "batch", "dossier", "cutoff", "latest_financial_period",
                "sources", "financial_anchor", "ai_claim", "strongest_counterevidence",
                "rights_limit", "materiality_summary", "arithmetic", "confidence",
                "g2_provisional", "unresolved_questions", "self_check_complete"}
    results, capsules = [], {}
    for item in schedule["remaining"]:
        path, capsule_path = ROOT / item["dossier"], ROOT / item["capsule"]
        row = {k: item[k] for k in ["order", "id", "company", "batch", "dossier", "capsule"]}
        issues = []
        row.update(status="scheduled", words=0, sources=0)
        if path.exists():
            body = path.read_text()
            row["words"] = len(body.split())
            row["status"] = "draft"
            if not capsule_path.exists():
                issues.append("capsule not yet present")
            else:
                try:
                    cap = json.loads(capsule_path.read_text())
                    capsules[item["id"]] = cap
                    missing = required - set(cap)
                    if missing:
                        issues.append("missing capsule keys: " + ", ".join(sorted(missing)))
                    if cap.get("id") != item["id"] or cap.get("dossier") != item["dossier"]:
                        issues.append("identity/path mismatch")
                    if cap.get("cutoff") != schedule["cutoff"]:
                        issues.append("cutoff mismatch")
                    sources = cap.get("sources", [])
                    row["sources"] = len({s.get("url") for s in sources if isinstance(s, dict)})
                    if row["sources"] < 4:
                        issues.append("fewer than four distinct capsule sources")
                    placeholders = [s for s in sources if isinstance(s, dict) and re.search(
                        r"dated or undated|effective date on page|latest available|current hub|^current$|undated/current|latest filing available",
                        str(s.get("date", "")), re.I)]
                    if placeholders:
                        issues.append("source dates contain unresolved template placeholders")
                    anchor = cap.get("financial_anchor", {})
                    if re.search(r"sector-appropriate|latest revenue and profitability", str(anchor.get("metric", "")), re.I):
                        issues.append("financial anchor needs an exact metric, not template wording")
                    if not cap.get("self_check_complete"):
                        issues.append("agent self-check incomplete")
                    if len(body.split()) < 700:
                        issues.append("packet below 700 words; lead must review scope")
                    if not re.search(r"G3", body) or not re.search(r"G4", body):
                        issues.append("valuation/portfolio deferral not explicit")
                    if not issues:
                        row["status"] = "ready_for_lead_review"
                except (ValueError, TypeError) as exc:
                    issues.append("invalid capsule: " + str(exc))
        review = reviews.get(item["id"])
        if review:
            row["lead_review"] = review
            if review.get("status") == "accepted" and not issues and path.exists():
                row["status"] = "lead_accepted"
            elif review.get("status") == "revision_requested":
                row["status"] = "revision_requested"
        row["issues"] = issues
        results.append(row)

    accepted = 10 + sum(r["status"] == "lead_accepted" for r in results)
    available = 10 + sum(r["words"] > 0 for r in results)
    summary = {"cutoff": schedule["cutoff"], "scope": 100, "packets_available": available,
               "lead_accepted": accepted, "remaining_to_accept": 100 - accepted,
               "phase": "evidence coverage; comparative ranking and valuation cases deferred",
               "companies": results}
    if args.write:
        (RESEARCH / "coverage-index.json").write_text(json.dumps(summary, indent=2) + "\n")
        lines = ["# Universe research coverage", "", "**Cutoff: 12 September 2026 · Scope: 100 companies.**", "",
                 f"Packets available: **{available}/100**. Lead accepted: **{accepted}/100**. Remaining acceptance: **{100-accepted}/100**.", "",
                 "The user requested evidence coverage before explicit comparative ranking and detailed bear/base/bull cases. The [coverage contract](coverage-instructions.md) governs batches 02–10. Batch-one valuation work is preserved as an earlier provisional pass; it is not the final universe ranking.", "",
                 "A completed evidence packet may conclude that AI proof is weak or unavailable. Lead acceptance means it is suitable for the later comparison with limitations stated; it does not mean the investment thesis or G2 passes.", "",
                 "| Batch | Companies | Lead acceptance |", "|---|---|---|",
                 "| [01](batch-01/README.md) | Original first ten priority names | 10/10 reviewed |"]
        for batch in range(2, 11):
            subset = [r for r in results if r["batch"] == batch]
            done = sum(r["status"] == "lead_accepted" for r in subset)
            lines.append(f"| [{batch:02d}](batch-{batch:02d}/README.md) | " + ", ".join(r["company"] for r in subset) + f" | {done}/10 |")
            out = [f"# Batch {batch:02d} — company evidence research", "",
                   "Cutoff: 12 September 2026. Comparative ranking and detailed bear/base/bull cases are deferred by the user.", "",
                   f"Lead accepted: **{done}/10**. See the [coverage contract](../coverage-instructions.md) and [full coverage](../coverage.md).", "",
                   "| Order | Company | ID | Packet status |", "|---:|---|---|---|"]
            for r in subset:
                link = "[" + r["company"] + "](" + str(Path(r["dossier"]).relative_to(f"research/batch-{batch:02d}")) + ")" if r["words"] else r["company"]
                out.append(f"| {r['order']} | {link} | {r['id']} | {r['status'].replace('_', ' ')} |")
            out += ["", "## Lead acceptance notes", ""]
            for r in subset:
                rev = r.get("lead_review")
                if rev:
                    out += [f"**{r['company']} ({r['id']}):** {rev.get('note', '')}", ""]
            out += ["Acceptance checks source support, scope, materiality arithmetic and explicit limits. It is neither an audit opinion nor a buy/sell recommendation. Raw capsules preserve the researcher's handoff; lead notes govern unresolved differences.", ""]
            (RESEARCH / f"batch-{batch:02d}" / "README.md").write_text("\n".join(out))
        lines += ["", "[Lead synthesis](coverage-synthesis.md) · [Machine-readable coverage](coverage-index.json) · [Lead acceptance record](coverage-review.json) · [Research schedule](coverage-schedule.json)", "",
                  "Evidence dates and access limitations remain company-specific. G3/G4 for batches 02–10 are deferred; no new numeric scores, target prices or allocations are produced.", ""]
        (RESEARCH / "coverage.md").write_text("\n".join(lines))
    if args.capsules is not None:
        chosen = set(args.capsules) if args.capsules else set(capsules)
        print(json.dumps({k: v for k, v in capsules.items() if k in chosen}, indent=2))
    else:
        print(json.dumps({"available": available, "accepted": accepted,
                          "ready": [r["id"] for r in results if r["status"] == "ready_for_lead_review"],
                          "issues": {r["id"]: r["issues"] for r in results if r["issues"]}}, indent=2))


if __name__ == "__main__":
    main()
