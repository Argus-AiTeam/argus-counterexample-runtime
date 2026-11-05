# Closed-surface cubed-mixed rank-three `abd` physical boundary

## Exact result

The noncentral `abd` Gram-rank-three chart has no real `SU(2)` point on
`Delta_abc=0`.

For a physical `SU(2)` tuple, the imaginary-part Gram matrix is positive
semidefinite.  Since the chart inverts `Delta_abd`, the `abd` principal
matrix is positive definite and therefore

```text
Delta_ab > 0.
```

The exact Schur complement then puts `Im(c)` uniquely in the span of
`Im(a),Im(b)`.  Cramer's rule reconstructs `Tcd,Tabc,Tacd,Tbcd`, so no
physical branch is lost in the resulting low-dimensional systems.

## Exhaustive algebraic split

A typed Jacobian lexicographic Groebner computation on three frozen source
equations factors the front condition as

```text
F0 * F1 * F2.
```

The central character multiplying `b,c` by `-I` fixes the source ideal,
preserves the localizers, fixes `F0`, and exchanges `F1,F2`.  Splitting
also by `Ta != 0` and `Ta = 0` leaves four systems.  Exact
characteristic-zero msolve computations returned reduced basis `[1]` for
all four:

| branch | variables | equations | result |
|---|---:|---:|---|
| `Ta != 0`, `F0` | 11 | 20 | `[1]` |
| `Ta != 0`, `F1` | 11 | 16 | `[1]` |
| `Ta = 0`, `F0` | 10 | 20 | `[1]` |
| `Ta = 0`, `F1` | 10 | 20 | `[1]` |

The slower second branch was certified after retaining `Tbc` and imposing
its graph relation rather than expanding through an inverse of `Ta`.
That system omits five source pullbacks, hence is an algebraic
over-approximation; its unit ideal is still sufficient for exclusion.  An
independent exact Singular computation also returned `1` for a core of
the first `Ta=0` branch.

The source binding, Jacobian payload, Cramer identities, central-character
cover and every characteristic-zero unit output are replayable with

```bash
./.venv/bin/python \
  research/verify_closed_surface_cubed_mixed_rank3_abd_boundary.py
```

## Boundary of the conclusion

This closes only the physical `Delta_abc=0` boundary.  The
`Delta_abc != 0` interior is not exhausted: the source-bound `F0/H2`
branch has an additional exact 24-dimensional `QQ` quotient whose real
`SU(2)` status remains open.  No
isolated rank-one point, compact Chern--Simons value, or irrationality
certificate was obtained, and no candidate was emitted.  The campaign
must replan to a materially different open route.

Full evidence:
[`research/CLOSED_SURFACE_CUBED_MIXED_RANK3_ABD_BOUNDARY.md`](../../../../research/CLOSED_SURFACE_CUBED_MIXED_RANK3_ABD_BOUNDARY.md).
