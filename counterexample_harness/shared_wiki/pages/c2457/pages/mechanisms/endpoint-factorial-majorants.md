---
title: Endpoint-factorial incidence majorants
description: Exact support and limitation of scalar factorial-moment majorants for complete canonical-row state spaces.
---

For any finite candidate state space \(V\) covered by equality-corrected
canonical rows, let \(d(v)\) be the number of rows incident to \(v\),
\(M=\max_v d(v)\), \(N=|V|\), and \(U\) the number of zero-incidence states.
For even \(D\), the rational polynomial
\[
Q_{N,D}(t)=\frac1{N+1}+\frac{N}{N+1}
\sum_{j=0}^{D}(-1)^j\binom tj
\]
is a pointwise majorant of the zero-incidence indicator. Its full-state sum
is exactly
\[
\frac{N}{N+1}+\frac{N}{N+1}
\left(U+\sum_{d(v)>D}\binom{d(v)-1}{D}\right).
\]

Consequently:

- if \(D<M\), the sum is at least one;
- if \(D\geq M\), the sum is below one exactly when \(U=0\).

The complete exact-class state space includes every admissible class-one
seed, cofactor, length, and multiplier history below the endpoint. On its
seed-\(5\), all-multiplier-two slice,
\[
M(C,r)\geq
\left\lfloor\log_3(\lfloor r/2\rfloor+1)\right\rfloor-1
\]
for every fixed integer \(C\geq2\), so the required degree is unbounded.

This rules out a non-tautological zero proof from this scalar
endpoint-factorial family. It does not rule out weighted row-dependent or
genuinely multivariate polynomials.
