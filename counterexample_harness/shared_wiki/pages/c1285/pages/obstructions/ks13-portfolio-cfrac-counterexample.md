---
title: KS13 portfolio CFRAC counterexample
description: Exact 120-bit semiprime on which all thirteen pinned KS13 multiplier streams have an independent retained-row matrix and the quadratic-budget candidate returns FAIL.
---

The preregistered candidate `KS13-PORTFOLIO-CFRAC(2,2)` uses the pinned
Math-Prime-Util-GMP KS13 table row, runs all thirteen listed multipliers with

```text
B=L=bit_length(N)^2,
```

combines every retained complete-denominator relation, computes its
deterministic full nullspace basis, and tests both extraction gcds for each
basis vector.

The first input in the preregistered Mersenne-semiprime search is

```text
N=664613999749367995379973941415116797
 =1073741827 * (2^89-1).
```

It has 120 bits and `B=L=14400`. All preprocessing and all four early gcds
on all `13*14400=187200` rows are trivial. The thirteen streams retain 269
rows in total. Their combined parity matrix has 1687 coordinates and exact
rank 269, so its complete nullspace has dimension zero. The basis and
extraction loops are empty by exact linear algebra rather than timeout or
truncation, and the candidate returns `FAIL`.

The producer-independent verifier receives a certificate whose candidate
input contains only `N`; it separately proves the displayed factorization,
replays every row and smoothness classification, rebuilds the matrix and
nullspace, and rejects ten transcript mutations.

This crosses the reviewed single-multiplier KS13 boundary. It does not invoke
the distinct-kernel square-first-row theorem because none of the thirteen
first denominators is a retained square. It refutes only this exact quadratic
budget portfolio, not unrestricted CFRAC, upstream SIQS, or general integer
factoring.
