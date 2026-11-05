---
title: Punctured-torus effective candidate bound
description: Degree-independent height envelope and terminating exact enumeration for every candidate-qualified rank-one point.
---

# Punctured-torus effective candidate bound

The fixed \((u,r,c)\) eigenvalue curve is the torus image of

```text
Y^2=x^2-4,
Z^2=(x^2-3*x+3)*(x^2+x-1),
u=(x+Y)/2,
r=(x^2-x+1+Z)/(2*(x-1)),
c=x^2-x-1-x*(x-2)*r/(x-1).
```

Its normalization is a genus-three degree-four `V_4` cover of
`P^1`. Exact localized elimination gives projective degree `10` in
the embedding

```text
(u,r,c) -> [1:u:r:c].
```

The divisors above `x=1` and `x=infinity` show that
`u^a*r^b*c^d` can be constant only for `a=b=d=0`. Thus the curve is
contained in no translate of a proper subtorus.

Let `L_C` be the coefficient `l1` norm of its primitive integral Chow
form. Habegger's explicit height theorem gives every rank-one point
the degree-independent bound

```text
B_C = 20^13223952691200 * (1 + log(L_C) + 55/3).
```

Exact line-incidence elimination now gives

```text
L_C = 1179684.
```

The Chow form, and hence `L_C`, is computable by exact projective
elimination. Bombieri--Habegger--Masser--Zannier Lemma 3 then
effectively finds every point in the dimension-one subgroup locus
with coordinate-sum height at most `3*B_C`, without an algebraic-degree
cutoff.

The finite output is filtered exactly by all campaign conditions:
non-torsion, saturated rank one, `v=u^N` for an arbitrary integer
`N`, the strict `SU(2)` inequalities, and a literal primitive
`c^p*(+/-tau)^q=1` relation with `tau^2=r`. This is a terminating
candidate-only enumeration theorem, not an executed enumeration or
an all-family no-go.

The proof as printed still leaves curve-dependent constants implicit,
but the rank-one specialization has now been quantified. One
admissible tuple is

```text
(c1,...,c12) = (1,2,2,8,5,50,50,16,1024,2048,4096,3200)
lambda = 5.
```

It gives

```text
B_star = 3539110 * 20^13223952691200
D0 = (113251520000000000 * 20^13223952691200)^2
|a_j| <= (2 * 3^B_star)^D0
```

for every coordinate minimal polynomial. This is a closed finite
Northcott range, but that enormous range has not been enumerated.

For a point `P`, use the canonical lattices

```text
L(P)      = {m in Z^3 : u^m1*r^m2*c^m3 = 1},
Lambda(P) = sat(L(P)),
T(P)      = Lambda(P)/L(P).
```

When the free rank is one, `Z^3/Lambda(P)=Z`; the images of the three
coordinate vectors give the primitive exponent vector `(a,b,d)`,
unique up to sign. The invariant torsion datum is `T(P)`, not the
presentation-dependent orders of multipliers after changing the free
generator by a root of unity.

Orr's 2026 theorem does not provide this result: its affine closure
must be a line and its height depends polynomially on point degree.
A direct fixed-number-field S-unit reduction is also unavailable
because the arbitrary-`N` specializations are not placed in one
uniform number field and finite `S`.

The proof and replay are in
`research/PUNCTURED_TORUS_EFFECTIVE_CANDIDATE_BOUND.md` and
`research/verify_punctured_torus_effective_candidate_bound.py`.

The execution boundary is in
`research/PUNCTURED_TORUS_CANDIDATE_ENUMERATION.md`.

The numerical instantiation and replay are in
`research/PUNCTURED_TORUS_NUMERICAL_CUTOFF.md` and
`research/verify_punctured_torus_numerical_cutoff.py`.
