# PM-6-Cosmo: initial scaling checks

Lean 4.34.1, with pinned mathlib dependencies inherited from the sibling
PM-1-Arch/lean package. Run `./check.sh` with elan available. The existing
ignored cache directories are reused; no installation was needed.

`PMCosmo/Scaling.lean` checks:

* n_s=31/32, the load factor 1491/1376, and total/active ratio 31/6.
* Higher loaded Hubble input and lower loaded clustering input, with the exact
  invariant product of these two rescalings.
* A capacity refractive index on the domain 0≤occupancy<capacity: positivity,
  monotonicity and arbitrarily large values below saturation.
* A counting distinction: if 48 active modes are a subset of 248 total modes,
  inactive/active is (248-48)/48=25/6; total/active is larger by one.

The source formulas are model inputs. A Hubble ratio 23/43 is dimensionless and
needs a dimensional calibration. The saturation limit is distinguished from
Lean's total-division value at a zero denominator. If the intended dark sector
is disjoint from the active one, specify whether the count is total or inactive
before interpreting it as a density ratio.

A perturbation calculation of the spectral index, a Friedmann/metric dynamics,
a cosmological likelihood analysis, and a quantum derivation of black-hole
thermodynamics or information recovery remain open. A capacity denominator
alone does not establish those claims.

Verification: build and strict transitive axiom audit passed on 2026-10-27,
covering 86 project declarations. Only `propext`, `Classical.choice`, and
`Quot.sound` occur in the audit allowlist.

## Revised load and additional internal proofs

`SubstrateLoad.lean` imports the earlier paper 3 payload definition and proves
S_M=1−η=1/172. The complete load is 1491/1376. The adopted cosmological response
rules give H_late=502467/6880=73.032994… for the draft early input 67.4, and
S8=143104/186375=0.767828303… for the draft input 0.832. Exact rational rounding
bounds and fixed-load input-error propagation are proved.

The common-factor product constraint prevents independently tuning these two
outputs. Frozen central reference inputs do not obey it exactly; that is an
arithmetic fact, not a statistical rejection using their uncertainties.

`InformationCapacity.lean` proves that saturated finite storage cannot reversibly
absorb a fresh independent input without extra capacity or outcomes. Homogeneous
independent cells give q^n states, n log(q) nats and an area-proportional count
with coefficient log(q)/a. A physical black-hole entropy normalization and a
radiation mechanism are still open.

The slot count and complement relation are internal substrate consequences.
Adding the three terms with unit weights and identifying that load with a
cosmological rate multiplier remain constitutive assumptions.

The cosmology project now has a direct local dependency on `pm_nested`, in
addition to `pm_arch`, to keep the payload link mechanically checked.
`check.sh` also runs the independent fractional-arithmetic/tag-freshness check in
`calculations/check_load_consistency.py`. No new Python packages are needed.
