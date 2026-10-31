#!/usr/bin/env python3
"""Read-only checks of exact load arithmetic and generated LaTeX tag freshness.

Display calculations use floats. These independent rational checks certify the
load outputs to their displayed rounding, not physical constitutive laws.
"""
from fractions import Fraction
from pathlib import Path
import re
import subprocess
import sys


def tags(text):
    pairs = re.findall(r"%<\*([A-Za-z0-9_]+)>(.*?)%</\1>", text)
    result = dict(pairs)
    if len(result) != len(pairs):
        raise SystemExit("Duplicate calculation tag")
    return result


def main():
    here = Path(__file__).resolve().parent
    saved = tags((here / "cosmology.tex").read_text())
    fresh = tags(subprocess.check_output(
        [sys.executable, str(here / "cosmology.py"), "--latex"], text=True))
    if not fresh:
        raise SystemExit("No calculation tags generated")
    if saved != fresh:
        changed = sorted(k for k in saved.keys() | fresh.keys() if saved.get(k) != fresh.get(k))
        raise SystemExit("Stale calculation tags: " + ", ".join(changed))

    load = 1 + Fraction(1, 32) + Fraction(2, 43) + Fraction(1, 172)
    if load != Fraction(1491, 1376):
        raise SystemExit("Load factor identity failed")
    expected = {
        "LoadFactorVal": load,
        "QuantizationStressVal": Fraction(1, 32),
        "TopologicalStressVal": Fraction(2, 43),
        "ManifoldStressVal": Fraction(1, 172),
        "HubbleLateVal": Fraction(674, 10) * load,
        "S8GeoVal": Fraction(832, 1000) / load,
        "HubbleLateInputSigma": Fraction(1, 2) * load,
        "S8GeoInputSigma": Fraction(13, 1000) / load,
    }
    for key, value in expected.items():
        displayed = Fraction(saved[key].split()[0])
        if abs(displayed - value) > Fraction(1, 2 * 10**9):
            raise SystemExit(f"Incorrect load-derived value: {key}")
    print(f"Exact load arithmetic and tag freshness passed: {len(fresh)} tags")


if __name__ == "__main__":
    main()
