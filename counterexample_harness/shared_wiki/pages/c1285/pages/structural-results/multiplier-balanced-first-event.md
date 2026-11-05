---
title: Multiplier-balanced first-event forcing
description: Exact reduction-sensitive criterion under which a registered SQUFOF multiplier produces an index-2 mixed square and a one-step factor.
---

For the frozen multiplier-SQUFOF class, let `M=p*q` be a product of distinct
odd primes.  Suppose a registered odd square-free `k` is coprime to `M`,
`k*M=3 mod 4`, and `k=x*y`.  Attach `x,y` to opposite prime factors and
write the scaled factors as

```text
U=x*p < V=y*q,
A=(U+V)/2,
s=(V-U)/2.
```

If `s^2<A`, the actual normalized principal cycle has

```text
S=A-1,
Q_2=s^2
```

at form index `2`.  This is a mixed square because
`gcd(A-s,M)=p` and `gcd(A+s,M)=q`.  The source reverse initialization reaches
symmetry in one transition with raw denominator `2U`, and the required
normalization is exact:

```text
(2U)/gcd(2U,2k)=p.
```

Thus preprocessing either factors first or the registered multiplier returns
a verified prime factor in polynomial depth.  This excludes
multiplier-balanced first-event families, including the `k=1` near-square
subfamily, from any proposed all-global SQUFOF obstruction.  It does not show
that every semiprime has such a registered balance and leaves unbalanced
later-cycle incidence open.
