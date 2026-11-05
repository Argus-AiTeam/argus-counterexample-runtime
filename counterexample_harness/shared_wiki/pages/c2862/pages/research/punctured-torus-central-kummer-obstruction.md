---
title: Punctured-torus central Kummer boundary
description: Canonical lattice character for literal SU(2) filling, exact odd/even stable-sign dichotomy, and the remaining all-N arithmetic gap.
---

# Punctured-torus central Kummer boundary

For an all-nontorsion rank-one point \(P=(u,r,c)\), the evaluation map
on

```text
Lambda(P) = sat L(P)
```

induces the canonical injective character

```text
chi_P : T(P)=Lambda(P)/L(P) -> roots of unity.
```

If \((p,q)\) is the unique possible primitive squared-filling slope and
\(\ell=(0,q,2p)\), the literal `SU(2)` test is:

```text
ell not in L(P)                 -> no central/projective filling
ell in L(P), q odd             -> one stable sign gives I, the other -I
ell in L(P), q even            -> value chi_P(0,q/2,p), same for both signs
```

For odd \(q\), the squared relation itself gives

```text
rho = c^(-p) r^(-(q-1)/2),  rho^2=r,  c^p rho^q=1.
```

Thus the Kummer extension is not an obstruction in that case; it
constructs a literal determinant-one lift.

Exact full-matrix replay gives the three previously observed outcomes:
the cubic orbit has `I` for one stable sign but fails every integer
`N`; the first two quartic orbits have `-I` for both signs; and the
third quartic orbit has a noncentral order-three peripheral value.
Their torsion quotients are respectively `0`, `Z/2`, `Z/2`, and
`Z/6`.

This classification includes arbitrary root-of-unity multipliers and
all primitive slopes, but it is not an all-`N` no-go. A complete
exclusion still requires an arithmetic theorem ruling out odd-`q`
exact relations and zero even-`q` half classes on every unenumerated
integer-`N` specialization.

The proof and replay are in
`research/PUNCTURED_TORUS_CENTRAL_KUMMER_OBSTRUCTION.md` and
`research/verify_punctured_torus_central_kummer_obstruction.py`.
