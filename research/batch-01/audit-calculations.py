#!/usr/bin/env python3
"""Reproduce batch-01 scenario arithmetic; this does not validate economic inputs.

Run: python3 research/batch-01/audit-calculations.py
All prices/assumptions are frozen at the 12 September 2026 research cutoff.
Sources, security identifiers, dates and input limitations are in the dossiers.
No external dependencies. Values are per ordinary share in the stated currency.
EPS models retain only the stated dividends, not all accounting earnings, before
the terminal sale. Per-share growth embeds any buybacks: no second buyback credit.
"""

import json


def eps_value(eps, dividend, growth, multiple, hurdle, forward=False):
    """Five annual cash dates. forward=True means EPS/dividend are year 1.

    Otherwise they are the model's t=0 run rate, grown first for year 1.
    Calendar stubs, tax and friction are not modeled.
    """
    offset = 1 if forward else 0
    dividends = sum(dividend * (1 + growth) ** (t - offset) /
                    (1 + hurdle) ** t for t in range(1, 6))
    terminal = eps * (1 + growth) ** (5 - offset) * multiple / (1 + hurdle) ** 5
    return dividends + terminal


def cash_value(fcf, growth, terminal_growth, hurdle=0.09):
    """FCF t=0; five growth years followed by a Gordon terminal value."""
    assert hurdle > terminal_growth
    interim = sum(fcf * (1 + growth) ** t / (1 + hurdle) ** t
                  for t in range(1, 6))
    terminal = (fcf * (1 + growth) ** 5 * (1 + terminal_growth) /
                (hurdle - terminal_growth) / (1 + hurdle) ** 5)
    return interim + terminal


def book_value(book, roe, growth, hurdle):
    """Steady-state equity shorthand; requires consistent ROE/retention/book basis."""
    assert hurdle > growth and roe > growth
    return book * (roe - growth) / (hurdle - growth)


def reverse_growth(price, value_function):
    lower, upper = -0.5, 0.6
    assert value_function(lower) < price < value_function(upper)
    for _ in range(100):
        midpoint = (lower + upper) / 2
        if value_function(midpoint) < price:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def score(dimensions, sensitivity=False):
    weights = [20, 20, 5, 10, 15, 30] if sensitivity else [20, 20, 15, 10, 15, 20]
    assert len(dimensions) == 6 and all(1 <= x <= 5 for x in dimensions)
    return sum(d * w / 5 for d, w in zip(dimensions, weights))


def main():
    output = {"cutoff": "2026-09-12", "warning": "Conditional scenarios, not qualified price targets"}
    eps_inputs = {
        # currency, quote, EPS, dividend, year-1 inputs?, bear/base/bull (g, P/E, r)
        "RELX": ("GBP", 24.46, 1.372, 0.675, False,
                 [(0.02, 15, 0.10), (0.055, 18, 0.09), (0.085, 21, 0.085)]),
        "Wolters Kluwer": ("EUR", 66.20, 5.66, 2.52, False,
                           [(0, 12, 0.10), (0.05, 16, 0.09), (0.08, 19, 0.085)]),
        "Intuit": ("USD", 321.57, 20.24, 5.52, True,
                   [(0.02, 13, 0.10), (0.07, 17, 0.10), (0.11, 21, 0.10)]),
        "SAP": ("EUR", 177.26, 7.00, 2.50, True,
                [(0.04, 18, 0.09), (0.08, 23, 0.09), (0.14, 28, 0.09)]),
        "Siemens": ("EUR", 261.70, 11.35, 5.35, False,
                    [(0, 15, 0.10), (0.05, 19, 0.09), (0.08, 23, 0.08)]),
        "Schneider Electric": ("EUR", 287.40, 9.80, 4.20, False,
                               [(0.02, 18, 0.10), (0.07, 23, 0.09), (0.10, 28, 0.08)]),
    }
    values = {}
    for name, (currency, quote, eps, div, forward, cases) in eps_inputs.items():
        scenarios = [eps_value(eps, div, g, m, r, forward) for g, m, r in cases]
        _, base_multiple, base_hurdle = cases[1]
        values[name] = {"currency": currency, "observed_quote": quote,
                        "bear_base_bull": [round(v, 2) for v in scenarios],
                        "base_price_difference_pct": round((scenarios[1] / quote - 1) * 100, 2),
                        "reverse_growth_pct_at_base_multiple": round(100 * reverse_growth(
                            quote, lambda g: eps_value(eps, div, g, base_multiple, base_hurdle, forward)), 3)}

    for name, quote, fcf, cases, fx in [
        ("Thomson Reuters", 97.35, 2100 / 438.6, [(0.02, 0.02), (0.06, 0.025), (0.09, 0.03)], 1),
        ("Experian", 27.82, 1583 / 919, [(0.02, 0.02), (0.07, 0.025), (0.10, 0.03)], 1.3501),
    ]:
        scenarios = [cash_value(fcf, g, tg) / fx for g, tg in cases]
        values[name] = {"currency": "USD" if fx == 1 else "GBP",
                        "observed_quote": quote, "fcf_per_share_usd": round(fcf, 6),
                        "bear_base_bull": [round(v, 2) for v in scenarios],
                        "base_price_difference_pct": round((scenarios[1] / quote - 1) * 100, 2),
                        "reverse_growth_pct": round(100 * reverse_growth(
                            quote, lambda g: cash_value(fcf, g, 0.025) / fx), 3)}

    for name, currency, quote, book, cases in [
        ("Munich Re", "EUR", 503.40, 259.76,
         [(0.12, 0.03, 0.10, 0), (0.15, 0.04, 0.09, 0.003), (0.16, 0.045, 0.085, 0.008)]),
        ("Chubb", "USD", 338.25, 195.45,
         [(0.11, 0.03, 0.10, 0), (0.135, 0.04, 0.09, 0.0075), (0.15, 0.045, 0.085, 0.01)]),
    ]:
        values[name] = {"currency": currency, "observed_quote": quote,
                        "conventional_bear_base_bull": [round(book_value(book, roe, g, r), 2)
                                                       for roe, g, r, ai in cases],
                        "including_conditional_ai": [round(book_value(book, roe + ai, g, r), 2)
                                                     for roe, g, r, ai in cases],
                        "reverse_roe_pct_at_9pct_hurdle_4pct_growth": round(100 * (0.04 + quote / book * 0.05), 3),
                        "reverse_roe_pct_at_10pct_hurdle_4pct_growth": round(100 * (0.04 + quote / book * 0.06), 3),
                        "base_conventional_value_at_10pct_hurdle": round(book_value(book, cases[1][0], 0.04, 0.10), 2)}
    output["valuations"] = values
    output["lead_additional_sensitivities"] = {
        "WK_audited_eps_stress": round(eps_value(5.29, 2.52, -0.05, 10, 0.10), 2),
        "WK_audited_eps_conservative": round(eps_value(5.29, 2.52, 0.04, 14, 0.10), 2),
        "Intuit_reverse_growth_pct_at_18x": round(100 * reverse_growth(321.57,
            lambda g: eps_value(20.24, 5.52, g, 18, 0.10, True)), 3),
    }
    dimensions = {"RELX": [4, 5, 3, 4, 5, 4], "Wolters Kluwer": [4, 5, 3, 5, 5, 3],
                  "Thomson Reuters": [5, 4, 2, 4, 5, 3], "Experian": [4, 4, 3, 4, 5, 3],
                  "Intuit": [4, 5, 3, 4, 5, 3], "SAP": [5, 4, 3, 4, 5, 3],
                  "Siemens": [4, 4, 2, 4, 5, 3], "Schneider Electric": [4, 4, 2, 4, 5, 3],
                  "Munich Re": [4, 4, 3, 3, 5, 3], "Chubb": [4, 5, 3, 4, 5, 3]}
    output["lead_structural_scores"] = {
        name: {"dimensions": dims, "score": score(dims), "sensitivity_score": score(dims, True)}
        for name, dims in dimensions.items()}
    output["illustrative_economic_checks"] = {
        "RELX_incremental_legal_revenue_required_pct": round(90.5 / (959 * 2) * 100, 2),
        "SAP_cost_route_million_eur": round(17100 * 0.10 * 0.50 * 0.50 - 300, 2),
        "SAP_strong_cost_route_million_eur": round(17100 * 0.15 * 0.60 * 0.60 - 300, 2),
        "Chubb_admin_route_pretax_million_usd": round(4504 * 0.25 * 0.70 * 0.70 - 100, 2),
        "Chubb_secondary_target_after_tax_million_usd": round(45790 * 0.015 * (1 - 0.19), 2),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
