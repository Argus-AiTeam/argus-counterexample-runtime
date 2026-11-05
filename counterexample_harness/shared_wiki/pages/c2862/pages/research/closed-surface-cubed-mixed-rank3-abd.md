---
title: Closed-surface cubed-mixed rank-three abd checkpoint
description: Exact degree-96 component lower bound in the abd chart and the remaining Delta_abc boundary.
---

# Closed-surface cubed-mixed rank-three `abd` checkpoint

The frozen noncentral `abd` Gram-rank-three chart is bound exactly to
the authoritative 33 fixed-character equations.  Four known
characteristic-zero degree-24 components enter this chart:

```text
P_plus, P_minus, K_plus, K_minus.
```

Their `Tb` polynomials are pairwise coprime, so they give a pairwise
comaximal degree-96 lower bound.  Exact reduction proves that
`Delta_abd` and the noncentral `b^-1 c` factor are units on both
component orbits.  For the known `(r,s)` orbit this includes a bounded
Jacobian Gröbner calculation over `QQ[r,s]` whose exact typed result is
the unit basis `[1]`.

The chart is not exhausted.  Besides the separately treated
`Delta_abc=0` boundary, the source-bound `F0/H2` Cramer branch leaves an
additional exact 24-dimensional `QQ` quotient after the `P_plus`
polynomial is inverted.  Its real `SU(2)` points and complete
thirteen-eigenvalue lattices are not yet classified.
The later one-shot full-chart test used the frozen 25-equation input
over the Pratt-certified prime `32003`.  Exact replay shows that its
SHA-256 is
`f0be3932790f88f359cd488d4759944b6f39cf22443906c748f08755e7fc8769`,
that it is the coefficientwise reduction of the characteristic-zero
chart, that its only denominators `1,2` are units, and that its
Rabinowitsch localizer survives reduction.  The exact sparse F4 run
reached its 7200-second durable boundary during a
`118921 x 305501` degree-eight matrix.  The wrapper recorded `crashed`
because no exit sidecar remained; both the leading-ideal file and
standard output are empty.  Hence it supplies no leading ideal,
standard-monomial staircase, finite-field length, or
characteristic-zero conclusion.  The run was not repeated with another
prime or schedule.

The earlier `Delta_abc` boundary saturation likewise produced no basis.
Neither operational failure is a modular exclusion.  No exhaustive
real `SU(2)` screen, irrational class in `R/Z`, or candidate follows.

Full checkpoint and replay:
[`CLOSED_SURFACE_CUBED_MIXED_RANK3_ABD.md`](../../../../../research/CLOSED_SURFACE_CUBED_MIXED_RANK3_ABD.md).
