---
title: Punctured-torus numerical cutoff
description: Primitive Chow norm, explicit BMZ constants, degree cutoff, and closed Northcott coefficient range.
---

# Punctured-torus numerical cutoff

The degree-ten genus-three eigenvalue curve has primitive Chow form
coefficient norm

```text
L_C = 1179684.
```

For the required `n=3`, curve-dimension `m=1`, non-torsion-rank
`r=1` specialization, one admissible fully numerical BMZ tuple is

```text
(c1,...,c12) = (1,2,2,8,5,50,50,16,1024,2048,4096,3200)
lambda = 5.
```

The only deep replacement is Amoroso--Delsinne's explicit relative
height theorem. With base field `K=Q` and abelian extension
`L=Q(zeta_N)`, its nominal unknown exponent occurs in `1^(-c)=1`, so
no hidden numerical constant remains.

The closed search range is

```text
B_star = 3539110 * 20^13223952691200
D0 = (113251520000000000 * 20^13223952691200)^2
coordinate degree <= D0
|minimal-polynomial coefficient| <= (2 * 3^B_star)^D0
torsion multiplier order <= 3 * D0^2.
```

The Chow form is saved by its exact line-resultant, Pluecker normal
form, and hyperplane-minor substitution; replay expands all 19,640
terms, checks integral content one, and recomputes `L_C`.

This supplies a genuine finite stopping certificate. It does not
claim that the astronomical Northcott box has been enumerated, that
the four known rank-one orbits are exhaustive, or that an irrational
`SU(2)` Chern--Simons candidate has been found.

The proof and replay are in
`research/PUNCTURED_TORUS_NUMERICAL_CUTOFF.md` and
`research/verify_punctured_torus_numerical_cutoff.py`.
