---
title: Dyadic mixed-norm sieve boundary
description: A finite-height incidence saving does not extend to complete multiplier-SQUFOF events because every event has an infinite Pell-unit parameter fibre.
---

# Dyadic mixed-norm sieve boundary

For normalized `D=e*k*p*q` and a mixed label

```text
h=d*p,       hbar=(e*k/d)*q
```

(or with `p,q` interchanged), the exact event parameterization contains

```text
0 < abs(hbar*t^2-h*r^2)
  < (2*sqrt(2)/delta)*D^(1/4).
```

In balanced boxes `p,q in [X,2X]`, an elementary lattice-line count shows
that witnesses with `r,t<=T`, summed over both source branches, every
`k<=K`, every `d|e*k`, and both mixed labels, number at most

```text
O(
  X^(1/2)*K^(5/4)*log(2K)*T^2
  + X^(3/2)*K^(3/4)*log(2K)*log(2T)^2
).
```

This gives a power saving for polylogarithmic `K` and
`T<=X^(3/4-eta)`.

It does not count the complete event set.  If `x^2-D*y^2=1`, then

```text
(r,t) ->
(x*r+hbar*y*t, h*y*r+x*t)
```

preserves the signed gap, primitivity, both source parity branches, the
lifted residue modulo `s^2`, and the same reduced event.  Iteration produces
infinitely many raw tuples for one event.  Therefore an unrestricted tuple
union bound is vacuous, while imposing `T` changes the target.

The missing input is a count of canonical generalized-Pell orbit
representatives with their marked mixed class and exact lifted reducedness
condition.  That is the unresolved reduction-sensitive incidence problem.
The bounded-height estimate supplies neither an infinite SQUFOF
counterfamily nor a universal factoring result.
