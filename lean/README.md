# PM-6-Cosmo: cosmological applications and proof boundaries

Lean 4.34.1; keep Papers I–VI as sibling directories. Run `./check.sh` with
elan available, or set `PM_LAKE_BIN` to the pinned Lake executable. Local
requirements now include Papers IV and V as well as Papers I and III.
Existing mathlib caches are reused; no additional package installation is needed.

## Checked modules

| Module | Results and hypotheses |
| --- | --- |
| `Scaling` | Candidate tilt `31/32`, load `1491/1376`, count ratios; conditional Hubble/clustering rescaling; local index bounds and unboundedness below saturation. |
| `SubstrateLoad` | 172 coordinate slots, one-slot complement of the earlier payload fraction, exact revised outputs, fixed-load error propagation and joint product constraint. |
| `InformationCapacity` | Saturated finite storage cannot absorb fresh independent labels reversibly without extra outcomes/capacity; independent-cell state counts and conditional area law. |
| `Primordial` | Tilt/channel link, impossibility of injective 32→16 relabeling without retained information, sufficient binary record, two distinct CP-to-baryon estimates, baryon-label conservation under iteration, nonzero source-free oscillator counterexample. |
| `Saturation` | Residual-capacity speed and its saturation limit, exact weak-load remainder and strict two-load mean-index inequality. The local law is supplied; there is no exterior metric theorem. |
| `Background` | Matter/radiation equality under stipulated dilution laws, density derivative and effective equation of state under a load-proportional density and supplied continuity equation. |
| `Thermodynamics` | Entropy derivative, first-law temperature, conditional `1/(8πM)` comparison and cell-area normalization. Geometry, entropy coefficient and energy law are inputs. |
| `NeutrinoCompatibility` | Direct use of upstream small-sum bounds and factor-six exclusion; no common rescaling/relabeling of the tower fits the fixed two splitting windows. |

## Numerical and upstream consistency

The revised load is `1 + 1/32 + 2/43 + 1/172 = 1491/1376`.
With the supplied cosmological response laws and fixed draft inputs, this gives
`H_late = 73.032994186…` km/s/Mpc and `S8 = 0.767828303…`.
The additive weights and the response law remain constitutive assumptions.
The exact joint product constraint prevents independently tuning both outputs.

Paper IV's complete unitary CKM ansatz gives `J ≈ 3.02287×10⁻⁵`; the older
independent geometric formula gives `J_geo ≈ 3.08490×10⁻⁵`.
The proposed conversion `eta_B(J) = J/(16168π)` therefore gives approximately
`5.95132×10⁻¹⁰` versus `6.07344×10⁻¹⁰`. The calculator now displays both rather
than silently identifying them. The former differs from the draft's fixed
`(6.12 ± 0.04)×10⁻¹⁰` reference by about 4.22 quoted errors. This is conditional
arithmetic, not a likelihood analysis or a derivation of baryogenesis.

The historical factor-six contextual neutrino proposal is retained as a tested
candidate, not a resolution. A common multiplier cannot change the tower's
squared-gap proportions `(1,1849,1850)`. A small mass sum does not establish an
acceptable oscillation spectrum. A different propagation law remains possible.

## Verification and generated values

`check.sh` builds the default library, audits all project declarations against
only `propext`, `Classical.choice` and `Quot.sound`, and runs
`../calculations/check_load_consistency.py`. The restored Python checker uses
exact fractions for the load-derived displays and checks every generated LaTeX
tag against the calculator. It has no third-party dependencies.

The display calculator uses ordinary floating-point arithmetic; Lean supplies
exact rational enclosures for the certified quantities. Observational inputs
are frozen comparisons from the draft, not an updated survey.

On 2026-10-30, the pinned `./check.sh` passed **3248 build jobs**, the
strict audit of **146 PMCosmo declarations**, and all **53 generated tags**.
The existing `paper/_main.tex` also compiled successfully in the desktop editor.

## What remains

See `REVIEW-AND-NEXT.md`. The leading task is a substrate-to-background evolution
and readout law, followed by its perturbations. Counts and positive finite
budgets alone do not determine an expansion history, a spectral index, a CP-to-
baryon conversion, a global horizon, Hawking radiation or a dark-sector density.
The manuscript now separates these proposals from the consequences Lean checks.
