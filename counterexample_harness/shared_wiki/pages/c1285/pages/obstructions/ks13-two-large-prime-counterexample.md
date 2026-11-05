---
title: KS13 portfolio two-large-prime counterexample
description: A genuine distinct-prime graph cycle exists, but the complete augmented matrix remains full row rank.
---

`KS13-PORTFOLIO-CFRAC-DLP(2,2,1)` runs the reviewed thirteen KS13 multiplier
streams with `B=L=n^2` and admits residuals `1`, a prime `p<=R`, or
`p*q` with primes `p<=q<=R=n^3`. Its large-prime graph uses distinguished
vertex `1`; `p^2` keeps multiplicity two in reconstruction and has zero
incidence parity.

The first frozen family input,

```text
N=664613999749367995379973941415116797
 =1073741827 * (2^89-1),
```

completes all 187,200 rows. It retains 269 full rows, 2,333 single-prime rows,
and 4,975 two-prime rows, of which 4,974 join distinct primes. The graph has
cycle-space dimension 83. In particular,

```text
(1,18121), (1,30011), (18121,30011)
```

is a genuine three-edge cycle. Its large-prime incidence cancels, but its
augmented xor still has 16 nonzero sign/factor-base coordinates.

Across 10,636 used large primes, the complete matrix has 7,577 rows and 12,323
columns. Exact elimination gives rank 7,577 and zero kernel, so the complete
basis is empty and the candidate returns `FAIL`. A producer-independent
only-`N` replay uses a different residual-factor index and low-coordinate
pivots, obtains the same rank and graph-cycle dimension, checks `p^2`
multiplicity, and rejects 15 material mutations.

This refutes only the frozen KS13 portfolio with quadratic row/factor-base
budgets and cubic two-large-prime cutoff. It does not refute unrestricted
CFRAC, SIQS, another cutoff, another relation geometry, or integer factoring.
