---
title: Punctured-torus affine rank-one boundary
description: Exact affine fillings, four certified all-nontorsion rank-one orbits, and the unbounded exceptional-classification gap.
---

# Punctured-torus affine rank-one boundary

On the fixed curve

```text
tr(A)=x,
tr(B)=tr(AB)=y=x/(x-1),
phi(a)=aba,
phi(b)=ba,
```

the cubic points satisfy `v=zeta*u^0`, with `zeta=v` primitive of
order 14, and admit a determinant-one intertwiner with `C*T=I`.
Their local annular square-angle term is irrational by
Gelfond--Schneider.  The complete class is nevertheless rational:
this is slope `+/-1` filling of the figure-eight exterior, hence a
Seifert filling, and Auckly's component-defined theorem applies.
This is an exact control showing that the local term cannot replace
the endpoint and solid-torus contribution.

The nonzero affine relation

```text
v=-u^2
```

gives the unique physical root of

```text
x^3-x^2-x+2=0
```

and an explicit irreducible non-torsion `SU(2)` representation.
For the exact intertwiner `W`,

```text
W^6=det(W)^3*[A,B],
```

so either determinant-one normalization satisfies the literal
primitive relation

```text
C*T^-6=I.
```

The local term is, up to orientation,

```text
(-3*alpha^2+4*alpha-1)/4,  alpha=arg(u)/pi,
```

and is irrational.  This does not give an irrational closed class.
If `r=tau^2` is the squared stable eigenvalue, the quadratic square
classes have norm ratio `1/2`; hence `u` and `r` are multiplicatively
independent modulo roots of unity.  The complete filled value remains

```text
-6*m(1)^2 + 2*integral m dl  (mod Z)
```

along a fixed Kirk--Klassen boundary path.  It is a weight-two
logarithmic period, not a certified one-angle polynomial.  No
irrationality certificate is known for this value, so neither affine
point is a campaign candidate.

The exact proof and replay are in
`research/PUNCTURED_TORUS_AFFINE_RANK_ONE.md` and
`research/verify_punctured_torus_affine_rank_one.py`.

The wider slope-adapted exceptional locus is not exhausted by the
cubic.  Three further exact all-nontorsion rank-one orbits are now
certified:

```text
r=-u^3,       c=u^5,
r=-u^5,       c=-u^4,
r=zeta*u,     c=-u,       zeta^2-zeta+1=0.
```

Each has two strict `SU(2)` embeddings.  The first two have unique
primitive peripheral relations with literal value `-I`; they are
relations only after projection to `SO(3)` or `PSL(2,C)`.  The third
fails even the necessary squared central relation.  Exact recurrence
periods over finite quotient rings exclude `v=u^N` for every integer
`N` on all three.

These are certified points, not a complete exceptional list.  General
rank one permits `u=xi*t^a`, `r=eta*t^b`, `c=delta*t^d` with unbounded
integer exponents and root-of-unity orders.  Maurin gives finiteness
but no enumerated list, and Jacobian has no multiplicative-dependence
or varying-unit-equation classifier.  The exact evidence and replay
are in `research/PUNCTURED_TORUS_SLOPE_ADAPTED_RANK_ONE.md` and
`research/verify_punctured_torus_slope_adapted_rank_one.py`.
