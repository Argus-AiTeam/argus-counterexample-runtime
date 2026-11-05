---
title: Closed-surface cubed-mixed rank-three abc complement
description: Exact degree-24 central-character component proving that the abc complement of the plastic and known (r,s) loci is nonempty.
---

# Closed-surface cubed-mixed rank-three `abc` complement

The noncentral `abc` Gram-rank-three fixed-character chart is not
exhausted by the reviewed plastic sublocus and the known `(r,s)` orbit.
The invariant fibre character

```text
chi_bc=(0,1,1,0)
```

multiplies the `b` and `c` holonomies by `-I`.  It negates exactly

```text
Tb,Tc,Tab,Tac,Tbd,Tcd,Tabd,Tacd
```

and sends every one of the frozen 33 source generators to itself or its
negative.  Applying it to the eight plastic relations produces the
exact residual ideal

```text
I_abc + (
  Tb^3-3*Tb^2+2*Tb+1,
  Tb+Td^2-1,
  Tc+Tb,
  Tcd+Td,
  Tbcd+Td,
  Tabc+Ta,
  Tbc-1-Td^2+2*Td^4,
  Tbd-3*Td+2*Td^5
).
```

Characteristic-zero FGLM gives rational degree `24` and Krull
dimension `0`.  The finite coordinate algebra is etale.  An exact
`15 x 15` minor of the original chart Jacobian is a unit on it, so it
is a Galois-stable orbit of isolated reduced components, not an
artificial slice.

Its `Tb` polynomial is coprime to both

```text
Tb^3+3*Tb^2+2*Tb-1
Tb^3+4*Tb^2+7*Tb+5,
```

the respective `Tb` consequences for the removed plastic and `(r,s)`
loci.  Explicit Bezout identities make both polynomials units on the
new component orbit.  Therefore

```text
V(I_abc) \ (V(P_plastic) union V(K_known))
```

is nonempty over characteristic zero.

This component does not classify the full residual or the other
rank-three charts.  In particular, a separate source-bound `F0/H2`
localization away from `P_plus` has an additional exact 24-dimensional
`QQ` quotient whose real `SU(2)` and multiplicative-rank screens remain
open.  No irrational Chern--Simons candidate is emitted.

Full proof and replay:
[`CLOSED_SURFACE_CUBED_MIXED_RANK3_ABC_COMPLEMENT.md`](../../../../../research/CLOSED_SURFACE_CUBED_MIXED_RANK3_ABC_COMPLEMENT.md).
