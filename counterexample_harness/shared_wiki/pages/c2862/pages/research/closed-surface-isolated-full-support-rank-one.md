---
title: Closed-surface isolated full-support rank-one boundary
description: Filling even-connector word, smooth quartic fixed arc, and exact cancellation to class 1/2.
---

# Closed-surface isolated full-support rank-one boundary

The explicit genus-two word

```text
F=D_(b^-1 c)^2 o ((D_a^+ o D_b^-)^3 union
                   (D_d^- o D_c^+)^3)
```

uses the filling curve set `a,b,c,d,b^-1 c`.  The reviewed quartic matrices

```text
rho(a,b,c,d)=(A,B,-B,A),       rho(t)=T^3
```

give an exact irreducible fixed `SU(2)` representation.  Its noncentral
twist eigenvalues are `u,u^4,-u^4,u`, with algebraic non-root-of-unity
`u`; the connector has holonomy `-I`.

This does not satisfy the rigidity gate.  The point lies on the smooth
irreducible fixed arc

```text
z=y,       y(x-1)=x,
```

whose transverse Jacobian determinant is `1-x`.  Since `tr(A)=x` varies,
the fixed character is not isolated and its controlling angle is not
locally constant.

The complete standard-left mapping-torus bar cycle has `324` terms and
exact zero boundary.  In the second-Chern `SU(2)` normalization,

```text
local twist sum                 =3*alpha-5/2,
endpoint/mapping-cone correction=3-3*alpha,
complete class                  =1/2 in R/Z.
```

Thus the local term is irrational at the quartic point but the full class
is rational.  This retires only the even central-connector insertion, not
full-support words with noncentral connector holonomy.  No candidate or
generic manifold-realization output is emitted.
