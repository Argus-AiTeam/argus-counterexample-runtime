---
title: Repeated-digit-3 schedule cross-band compensation boundary
description: Exact finite clock-prefix evidence and exclusions of first-clock-only, cumulative spectral-order, and one-source top-band charges.
---

For
\[
C_{k,r,\ell}=\sum_{j=0}^{\ell}
96^j[z^{2\cdot18^j}]A^rF_k,
\qquad
M_{k,r}=16^{-(k+r+2)}C_{k,r,k+r+2},
\]
the exact clock decompositions show that compensation is genuinely
cross-band.  At \((k,r)=(1,1)\), the first reserve is \(32/9\), but one
high-clock contribution is less than \(-26\); a middle clock greater
than \(47\) is essential to the positive complete margin.

The stronger lower-clock-prefix candidate survives every exact finite
test performed here.  Every prefix is positive for \(k=1\) and old
horizons \(r=0,\ldots,4\), and the prefixes through level two are
positive at all three phase-five states \((1,2),(2,1),(3,0)\).
It is not, however, an invariant of the information retained so far.
An explicit four-atom signed measure annihilates the current moments at
degrees \(0,2,36\), has every current scheduled moment positive, and has
an atomwise diagonal PSD realization with either exact reserve
\(107/36\) or \(32/9\).  Its first old prefix is strictly below \(-59\).
The old dual introduces the off-schedule degree
\(N_\ell/4=9\cdot18^{\ell-1}\), identifying the missing correlation
exactly.  This ambient measure is not asserted Laakso-reachable.

Both lower and upper cumulative spectral-weight orders also fail on the
genuine 73-atom base measure.

A feasibility-favorable exact transport LP also proves that positive
atom 64 cannot by itself pay the three highest negative atoms
70, 71, and 72 across \(r=0,\ldots,4\): its source capacity is below
\(1/20\), whereas the minimum required flow is above \(7/120\).
Jacobian returned an exact `INFEASIBLE` Farkas certificate.

This is a route boundary, not a universal sign theorem or a negative
witness.  A generator-stable invariant carrying stricter reachable
correlations remains open, all reviewed complete margins are positive,
and the counterexample campaign continues.
