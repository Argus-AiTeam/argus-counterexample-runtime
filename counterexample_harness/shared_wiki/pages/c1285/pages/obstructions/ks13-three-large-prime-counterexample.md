---
title: KS13 portfolio three-large-prime counterexample
description: Genuine three-prime hypergraph cancellation exists, but the complete augmented matrix remains full row rank.
---

`KS13-PORTFOLIO-CFRAC-3LP(2,2,1)` preserves the reviewed thirteen KS13
streams with `B=L=n^2`, `R=n^3`, and admits residuals factoring exactly,
with multiplicity, into at most three primes at most `R`.

The first frozen family input,

```text
N=664613999749367995379973941415116797
 =1073741827 * (2^89-1),
```

completes all 187,200 rows. It retains 269 full rows, 2,333 one-prime rows,
4,975 two-prime rows, and 1,965 three-prime rows. Of the last class, 1,964
have three distinct primes and one has shape `p^2*q`.

The partial-row incidence kernel has dimension 84. One exact four-row
dependency has large-prime multisets

```text
[312047], [94331], [94331,166303,312047], [166303].
```

It contains a genuine three-distinct-prime relation and cancels every
large-prime coordinate, but leaves 16 factor-base coordinates. Across 14,594
used large primes, the complete matrix has 9,542 rows and 16,281 columns.
Exact elimination gives rank 9,542 and zero kernel, so the complete basis is
empty and the candidate returns `FAIL`.

A producer-independent only-`N` replay uses a block-product factor index and
lowest-coordinate pivots, obtains the same incidence nullity and augmented
rank, checks `p^3` and `p^2*q` multiplicity semantics, and rejects 15 material
mutations.

This strictly extends the reviewed full-, single-, and double-large-prime
counterexample chain. It refutes only the frozen cubic-cutoff, quadratic-row
KS13 portfolio, not unrestricted CFRAC, SIQS, another cutoff or relation
geometry, or general integer factoring.
