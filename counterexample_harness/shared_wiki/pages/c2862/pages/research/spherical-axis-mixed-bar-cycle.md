---
title: Spherical axis-mixed seed-subgroup boundary
description: Exact regular rank-one seed and the free-subgroup obstruction to internal relation-first closure.
---

# Spherical axis-mixed seed-subgroup boundary

The exact unit quaternions

```text
(sqrt(7)+i+j+k)/sqrt(10)
(sqrt(7)+i-j-k)/sqrt(10)
(sqrt(7)-i+j-k)/sqrt(10)
(sqrt(7)-i-j+k)/sqrt(10)
```

have Gram diagonal `1`, every off-diagonal entry `3/5`, and determinant
`112/625`. The tetrahedron is nondegenerate and non-join. For consecutive
edge labels `g,h,k`, all six words

```text
g, h, k, gh, hk, ghk
```

have spectrum `{u,u^-1}` for `u=(3+4i)/5`. The primitive polynomial
`5X^2-6X+5` is irreducible and nonmonic, so `u` is not an algebraic integer
and therefore not a root of unity. The labels are axis-mixed: their traces
are nonzero, while `(gh-hg)_j=12/25`, so they cannot lie in one maximal-torus
normalizer.

The seed does not support an internal relation-first closure. Over
`Q(sqrt(7))`, the star basis `g,gh,ghk` admits an exact asymmetric
`5`-adic ping-pong certificate and freely generates `F_3`. Consequently
every finite normalized bar `3`-cycle using only seed words is a boundary,
because `H_3(F_3;Z)=0`; moreover `dim H^1(F_3;Ad rho)=6`, so the controlling
angle is not locally constant.

This excludes only closure inside the seed-generated subgroup. Adding new
holonomy generators or starting from a closed topology remains open. No
non-boundary cycle or Chern--Simons candidate was emitted.

The proof and replay are
`research/SPHERICAL_AXIS_MIXED_BAR_CYCLE.md` and
`research/verify_spherical_axis_mixed_bar_cycle.py`. Jacobian `0.14.0`
independently returned the exact Gram determinant through
`matrix.determinant.compute`.
