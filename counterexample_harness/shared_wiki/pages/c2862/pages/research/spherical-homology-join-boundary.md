---
title: Spherical homology and join boundary
description: Dupont's SU(2) normalized-volume bridge and the exact no-go theorem for finite orthogonal-join chains.
---

# Spherical homology and join boundary

Dupont's Theorem 1.7(c) and equation (7.15) place the spherical Dehn
kernel in the image of

```text
H_3(SU(2)^delta; Z) -> P(S^3)/Z[S^3].
```

His Theorem 10.2 and equation (10.7) identify the compact real
Cheeger--Chern--Simons coordinate as

```text
<C_2-hat, z> = Vol(sigma(z)) / (2*pi^2)  (mod Z),
Vol(S^3) = 2*pi^2.
```

This is the campaign's second-Chern `CS_SU2` normalization, not the
four-times-larger first-Pontryagin `SO(3)` normalization. The positive
torsion class `1/q` maps to the lune `L(2*pi/q)` and has value `1/q`.

For the orthogonal join `J(a,b)` of arcs in perpendicular great circles,
the exact vertex and normal Gram matrices are block diagonal:

```text
H = [[1, cos(a), 0, 0],       G = [[1, -cos(a), 0, 0],
     [cos(a), 1, 0, 0],            [-cos(a), 1, 0, 0],
     [0, 0, 1, cos(b)],             [0, 0, 1, -cos(b)],
     [0, 0, cos(b), 1]]             [0, 0, -cos(b), 1]].
```

For `0<a,b<pi`, `det(H)=sin(a)^2*sin(b)^2>0`. Its exact invariants are

```text
D(J(a,b)) = a tensor [b/pi] + b tensor [a/pi],
Vol(J(a,b)) = a*b/2.
```

For every finite integral chain of these joins, symmetry in
`R tensor_Q R` implies

```text
D(C)=0  =>  Vol(C)/(2*pi^2) in Q.
```

Thus non-root-of-unity algebraic angles cannot yield an irrational
zero-Dehn class inside this entire join family. The proof is in
`research/SPHERICAL_JOIN_NOGO.md`.

Genuine non-join rational orthoschemes are not a shortcut. Dupont's
Theorem 11.19 proves that a hyperbolic Galois conjugate obstructs
scissors congruence to a rational lune, but Corollary 11.20 derives
irrational volume only under the unresolved hypothesis that volume and
Dehn invariant classify spherical scissors classes. The Rational
Simplex Problem therefore remains a theorem-level gap, not an
irrationality certificate.
