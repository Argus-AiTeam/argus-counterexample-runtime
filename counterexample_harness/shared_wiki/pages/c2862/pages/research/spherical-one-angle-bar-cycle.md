---
title: Spherical one-angle monomial bar-cycle boundary
description: Exact common-normalizer no-go and the remaining axis-mixed finite-phase gap.
---

# Spherical one-angle monomial bar-cycle boundary

Fix an algebraic unit-circle number `u`, a root of unity `zeta_m` with
`4 | m`, and

```text
D(q) = diag(q,q^-1),
J    = [[0,1],[-1,0]].
```

The all-parameter common-basis monomial group

```text
N(u,m) = {D(zeta_m^r u^n), J D(zeta_m^r u^n)}
```

is closed under multiplication. Its diagonal elements have eigenphases in
`mu_infinity*u^Z`, while every anti-diagonal element has eigenvalues `+i,-i`.

Under `SU(2)=S^3`, the two components lie on two orthogonal great circles.
For any bar term `[g|h|k]`, all cumulative vertices

```text
1, g, gh, ghk
```

remain on those circles. Four such vertices are geometrically degenerate
unless exactly two lie on each circle. In the two-and-two case the Gram
matrix is

```text
[[1,x,0,0],
 [x,1,0,0],
 [0,0,1,y],
 [0,0,y,1]]
```

with determinant `(1-x^2)(1-y^2)`, and the tetrahedron is an orthogonal
join. Therefore every finite normalized bar cycle in this group maps to a
zero-Dehn integral join chain. The reviewed join-kernel theorem forces its
complete compact second-Chern value to be rational in `R/Z`, independently
of whether a presentation realizing the representation is isolated.

This excludes the entire common-normalizer monomial ansatz. It does not
exclude an axis-mixed finite configuration whose selected eigenphases lie in
`mu_infinity*u^Z` but whose matrices do not share one torus normalizer.
Eigenvalues determine angles, not axes, so that remaining case requires a
materially different construction.

The proof and exact replay are
`research/SPHERICAL_ONE_ANGLE_BAR_CYCLE.md` and
`research/verify_spherical_one_angle_bar_cycle.py`. Jacobian `0.14.0`
independently returned the displayed determinant through
`matrix.symbolic.determinant.compute`.
