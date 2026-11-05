---
title: Punctured-torus recurrence/lattice boundary
description: Exact literal square-class reduction, three higher-exponent rank-one orbit exclusions, and the missing factorwise Galois crossing.
---

# Punctured-torus recurrence/lattice boundary

At a nontrivial root of

```text
F_N(X)=(X-1)C_|N|(X)-X,
```

the Chebyshev discriminant identity reduces to

```text
-(3x-2)=(x-1)^2*(x+2)*U_(|N|-1)(x/2)^2.
```

Consequently the discriminants of `u` and `v=u^N` have the same square
class. This is tautological Kummer data, not a new parity character on
`L(P)`, `Lambda(P)`, or `T(P)[2]`.

A literal relation does force a stronger necessary square class. With

```text
A=x^2-3x+3
B=x^2+x-1,
```

the three cases are:

```text
q odd                 -> B/(x-1) is a square
q=2k with k even      -> A is a square
q=2k with k odd       -> A*B/(x-1)^3 is a square.
```

These conditions do not compute the complete lattice character. Excluding
them uniformly still requires the unproved statement that every irreducible
factor of the noncyclotomic part of `F_N` with a strict `SU(2)` root has a
real conjugate in the left interval

```text
(-2,(-1-sqrt(5))/2).
```

Three further exact all-nontorsion combined-rank-one orbits with primitive
exponent vectors `(2,1,6)`, `(3,2,5)`, and `(4,2,-5)` are now audited. Each
has two strict `SU(2)` trace embeddings and torsion quotient `Z/2`. The first
has half-relation value `-1`; the other two have squared peripheral value
`-1`. Exact finite-ring recurrence periods `7`, `26`, and `39` exclude
`v=u^N` for every integer `N`. They enlarge the pointwise list but are not an
exhaustive classification.

The literal matrix values are checked directly in the three exact
degree-eight \(u\)-fields. With \(D=\det W\), the verifier obtains
`C*D^6*W^-12=-I`, `C^2*D^5*W^-10=-I`, and
`C^2*D^-5*W^10=-I`. These are respectively the literal even-power product
and the squares of the two odd-power products, so they retain the distinction
between `I`, `-I`, and a noncentral `SU(2)` matrix.

The proof and replay are in
`research/PUNCTURED_TORUS_RECURRENCE_LATTICE_CHARACTER.md` and
`research/verify_punctured_torus_recurrence_lattice_character.py`.
