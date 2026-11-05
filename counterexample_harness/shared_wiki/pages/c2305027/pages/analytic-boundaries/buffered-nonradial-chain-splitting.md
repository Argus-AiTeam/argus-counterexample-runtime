---
title: Uniform splitting on buffered nonradial chains
description: Exact scope and limitation of the Cauchy-potential obstruction to scalar Bezout cocycle drift.
---

# Uniform splitting on buffered nonradial chains

For a chain cover with arbitrary-angle neck centers
\(c_j=p+Rq^j e^{i\theta_j}\), radii
\(r_j\leq\varepsilon Rq^{2j}\), and prefix partitions satisfying

\[
\sum_i|\bar\partial\chi_i|
\leq C_0\sum_j r_j^{-1}\mathbf 1_{B(c_j,r_j)},
\]

every bounded analytic additive cocycle has a holomorphic primitive of
norm at most

\[
(1+K_0)\|a\|_\infty,\qquad
K_0=18C_0\left(1+\frac{4\varepsilon q}{(1-q)^2}\right).
\]

The estimate is independent of prefix length and cell connectivity.  A
normalized fixed-gap pair with cellwise Bezout rows bounded by \(M\)
therefore has prefix Bezout norm at most

\[
M+(1+K_0)\min(2M^2,2M/\delta).
\]

The result permits arbitrary nonradial turning and unbounded topology in
cell cores.  It does not cover nonsummable Whitney-scale transitions:
when the transition-gradient Cauchy potential is unbounded, this
splitting argument gives no conclusion.

The proof and exact rational replay are in
`research/routes/nonradial-cech-chain/`.
