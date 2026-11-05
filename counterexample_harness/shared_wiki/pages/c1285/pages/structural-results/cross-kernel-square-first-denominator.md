---
title: Cross-kernel square first-denominator forcing
description: Exact threshold under which two retained square first rows from distinct multiplier kernels must factor the semiprime.
---

For the frozen multiplier-CFRAC bounds, let `K=ceil(n^u)` and let
`N=p*q` be a preprocessing-evasive product of distinct odd primes. If two
multipliers `k_1,k_2<=K` have distinct squarefree kernels and first
denominators

```text
k_i*N-floor(sqrt(k_i*N))^2=y_i^2
```

that are retained, then their two-row dependency factors `N` whenever

```text
N>=64*K^3.
```

The proof bounds both cross terms by
`2*sqrt(2)*K^(3/4)*N^(3/4)<N`. A global dependency sign would then either
make a positive integer smaller than `N` divisible by `N`, or force
`k_1*y_2^2=k_2*y_1^2`, which says that the kernels are equal.

This is an orientation theorem, not a relation-yield theorem: it does not
show that every semiprime has two retained square first rows. It prevents the
reviewed global-sign saturation obstruction from retaining such rows across
two distinct kernels at sufficiently large input lengths.
