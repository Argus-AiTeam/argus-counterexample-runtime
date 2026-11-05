---
title: Punctured-torus candidate enumeration boundary
description: Exact four-orbit lattice table, closed numerical BHMZ range, and the still-unexecuted finite enumeration.
---

# Punctured-torus candidate enumeration boundary

The Habegger height envelope and BHMZ Lemma 3 prove classical
effectivity. A curve-specific rank-one specialization now evaluates
the primitive Chow norm as `L_C=1179684`, gives

```text
D0 = (113251520000000000 * 20^13223952691200)^2,
```

and closes the coordinate-polynomial box by

```text
degree <= D0
|coefficient| <= (2 * 3^B_star)^D0
B_star = 3539110 * 20^13223952691200.
```

The exact finite range is therefore present, but no complete Galois
orbit list has been generated from it. The remaining gap is execution,
not a missing stopping criterion.

For the four known all-nontorsion rank-one orbits, the canonical
torsion quotients are exactly

```text
A: r=u^-2,       c=u       -> T(P)=0
B: r=-u^3,       c=u^5     -> T(P)=Z/2
C: r=-u^5,       c=-u^4    -> T(P)=Z/2
D: r=zeta*u,     c=-u      -> T(P)=Z/6
```

All four have two strict `SU(2)` embeddings. Orbit A has a literal
primitive filling only for one stable sign, but `v^7=-1` excludes
`v=u^N`. Orbits B and C have only literal `-I` relations for both
stable signs, and exact finite-ring periods exclude every integer
`N`. Orbit D fails the squared filling relation and its full finite
period also excludes every integer `N`. Thus the retained list among
the known orbits is empty, but those orbits are not proved exhaustive.

For

```text
H_n = F_n/(X-2)
```

the exact identities

```text
H_(2m+1) = 1 + (X-1)*(1 + sum_(j=1)^m C_j)^2
H_(2m)   = 1 + (X-1)*(X+2)*U_(m-1)(X/2)^2
```

imply that every real noncyclotomic root lies in `(-2,1)`. After
removing the known cyclotomic factors, `J_n(-2)=J_n(1)=1`; every
irreducible factor consequently has even degree, and every remaining
one has degree at least four. This does not prove the required Galois
crossing: the irreducible quartic

```text
X^4+3*X^3+X^2-3*X-1
```

has a strict-`SU(2)` root but no root in the excluding left interval
while satisfying the same generic endpoint constraints.

The proof and replay are in
`research/PUNCTURED_TORUS_CANDIDATE_ENUMERATION.md` and
`research/verify_punctured_torus_candidate_enumeration.py`.

The numerical cutoff is in
`research/PUNCTURED_TORUS_NUMERICAL_CUTOFF.md` and
`research/verify_punctured_torus_numerical_cutoff.py`.
