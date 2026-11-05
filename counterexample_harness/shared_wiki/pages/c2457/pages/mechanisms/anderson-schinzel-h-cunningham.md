---
title: Anderson SAC Schinzel-H Cunningham boundary
description: Local admissibility survives, but the printed PPDI is marginal, the spectral bridge is undefined, and no growing-height uniformity is proved.
---

For
\[
F_j(n)=2^j(n-1)+1,\qquad 0\le j<L,
\]
each form is primitive and irreducible. The family is jointly admissible:
\(\nu_L(2)=1\), while for every odd prime
\[
\nu_L(p)=\min\{L,\operatorname{ord}_p(2)\}<p.
\]
It also satisfies
\[
F_{j+1}(n)=2F_j(n)-1,\qquad
F_j(n)\mid F_{j+1}(n)+1.
\]
Thus local non-obstruction is not the gap. If \(n\le A^L\), then
\[
F_{L-1}(n)<(2A)^L,
\]
so a positive simultaneous-prime count at this scale would produce the
desired fixed-exponential negative-residue chain.

The V3 SAC-01 source instead defines
\[
D_{L,N}=\frac1{LN}\sum_{j=0}^{L-1}\sum_{n=1}^N
{\bf1}_{\mathbb P}(F_j(n)),
\]
which averages individual prime values. It is not the simultaneous count
\[
S_L(N)=\sum_{n\le N}\prod_{j=0}^{L-1}
{\bf1}_{\mathbb P}(F_j(n)).
\]
The minimal-height exact row \(L=7,n=2179\) is
\[
(2179,4357,8713,17425,34849,69697,139393).
\]
Its six other entries have complete deterministic trial-division
certificates, while
\[
17425=5^2\cdot17\cdot41.
\]
Thus \(D=6/7>0.85\) while its simultaneous indicator is zero. This height
is minimal: a nonjoint row has \(D\le(L-1)/L\), and for \(L\le6\) that is
at most \(5/6<0.85\).

More generally, for any finite set \(P\) of odd primes, put
\[
Q=\prod_{p\in P}p,\qquad R=\prod_{p\in P}(p-1).
\]
Each \(F_j\) has one root modulo every \(p\in P\), and CRT gives the
uniform bound
\[
D_{L,N}\le\frac RQ+\frac{R+|P|}{N}.
\]
Since the product of \(1-1/p\) over odd primes tends to zero,
\[
D_{L,\lfloor A^L\rfloor}\longrightarrow0
\]
for every fixed \(A>1\). This concerns the source's marginal statistic;
it does not prove that simultaneous Cunningham tuples are finite or absent.

SAC-01's spectral lemma states no spectral map, statistic, hypotheses, or
error theorem. Its final bounded-to-infinite step explicitly invokes
heuristics, and neither SAC-01 nor SAC-02 gives an effective first-occurrence
threshold uniform in \(L\). The mechanism therefore supplies no
fixed-exponential family and no Erdos counterexample.
