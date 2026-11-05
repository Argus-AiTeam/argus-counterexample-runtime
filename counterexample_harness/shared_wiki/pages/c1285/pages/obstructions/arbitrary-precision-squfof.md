---
title: Arbitrary-precision polynomial-cycle SQUFOF obstruction
description: Exact infinite absolute-failure family for source-grounded multiplier-free SQUFOF with full event handling and verified recursion.
---

# Arbitrary-precision polynomial-cycle SQUFOF obstruction

For fixed positive rational `c,f,r`, `AP-SQUFOF(c,f,r)` uses exact
arbitrary-precision arithmetic, complete preprocessing through
`ceil(n^c)`, the Gower--Wagstaff `N` versus `2N` normalization, at most
`ceil(n^f)` forward transitions, every eligible square-form event, and
at most `ceil(n^r)` reverse transitions per event. A reverse output is
normalized by `Q/gcd(Q,2)`, checked by gcd against the original
recursive input, and accepted only through verified prime-leaf
recursion.

For every fixed `c`, an elementary odd-Bonferroni count constructs
infinitely many preprocessing-evasive inputs

```text
N=m^2+2,      N=3 mod 8,
```

with a prime `q` dividing `N` to exact valuation one and no prime
divisor through `ceil(bit_length(N)^c)`. Thus each input is composite,
not a square, and not a perfect power.

Standard normalization gives `D=N`. The complete-quotient states
alternate forever:

```text
even form index:  (Qhat,P,Q)=(2,m,1),
odd form index:   (Qhat,P,Q)=(1,m,2).
```

Every eligible square event therefore has `Q=1`. Its inverse-square-root
cycle starts at `(Qhat,P,Q)=(1,m,2)`, reaches symmetry in one step, and
normalizes the raw output `2` to `1`; the gcd with `N` is always `1`.
This is an absolute failure for any forward or reverse budget, not a
timeout.

The exact replay anchor

```text
N=10046646470827523=10009*1003761261947,
n=54, c=f=r=2
```

executes all `2916` forward transitions and all `1458` eligible events.
Every reverse cycle gives the same trivial extraction. Separate controls
recover `23*31` from `N=713` through the `D=2N` branch and reproduce the
published factorization `22117019=4451*4969`.

This excludes only multiplier-free polynomial-cycle SQUFOF. Racing
`kN`, adaptive multipliers, fallback factorers, and general integer
factorization remain open.
