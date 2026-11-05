---
title: Unbalanced mixed-class orbit threshold
description: Exact reduction-orbit and least-representative criterion for mixed multiplier-SQUFOF ambiguous classes in both source normalizations.
---

For the frozen multiplier-SQUFOF source normalization, write

```text
D=e*k*p*q,
e=1 if k*p*q=3 mod 4 and e=2 if k*p*q=1 mod 4.
```

For every mixed ramified label `h=d*p` or `d*q`, with `d|e*k`, put
`hbar=D/h`.  The ambiguous form `[h,0,-hbar]` has the exact
complete-quotient reduction

```text
P_0=0, Q_-1=hbar, Q_0=h,
a_i=floor((sqrt(D)+P_i)/Q_i),
P_(i+1)=a_i*Q_i-P_i,
Q_(i+1)=(D-P_(i+1)^2)/Q_i.
```

The signed forms

```text
[(-1)^i Q_i, 2P_i, (-1)^(i+1) Q_(i-1)]
```

enumerate the reduced ambiguous cycle after the first reduced state.  This
works unchanged for `D=k*p*q` and `D=2*k*p*q`.

A mixed label occurs as the inverse square root of an eligible principal-cycle
square coefficient exactly when its class contains a primitive ideal

```text
j=(s,t+sqrt(D)),       gcd(s,2D)=1,
```

whose unique square lift `P mod s^2` makes

```text
[s^2,2P,(P^2-D)/s^2]
```

reduced.  The exact reducedness interval is

```text
abs(sqrt(D)-s^2)<P<sqrt(D).
```

If `s<D^(1/4)`, a representative of every residue class modulo `s^2` lies in
the required interval, so the mixed event is forced.  Conversely every
eligible event has

```text
s<sqrt(2)*D^(1/4).
```

Therefore an all-global obstruction must exclude primitive representatives
below `D^(1/4)` and every reduced lift in the transition band up to
`sqrt(2)*D^(1/4)`, simultaneously for every mixed label and every registered
multiplier.  The criterion is exact, but that uniform least-representative
exclusion and the required infinite preprocessing-evasive semiprime family
remain open.
