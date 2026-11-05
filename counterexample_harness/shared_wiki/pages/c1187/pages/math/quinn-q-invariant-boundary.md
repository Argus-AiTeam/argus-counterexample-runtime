---
title: Quinn Q-invariant boundary
description: Exact support and limitation boundary for applying the Bobtcheva-Quinn homology collapse to AK(3).
---

Bobtcheva's construction in arXiv:math/0012121v1 defines \(Q(P)\) for
any finite semisimple stable autonomous tensor category over a field.
Bobtcheva--Quinn arXiv:math/0012212v1 proves homology dependence only
for the overlap obtained from a prime-root Lie-family nondegenerate tortile
category over \(\mathbb Z_{(p)}[v]\) and its mod-\(p\) reduction. The latter
corollary must not be extended to every category in the former paper.

For AK(3), the cellular boundary matrix is

\[
d_2=\begin{pmatrix}3&1\\-4&-1\end{pmatrix},
\qquad
d_2^{-1}=\begin{pmatrix}-1&-1\\4&3\end{pmatrix}.
\]

Thus both the AK(3) and standard rank-two presentation complexes have
\(H_0=\mathbb Z\), \(H_1=H_2=0\), and Euler characteristic one.
Corollary 1.2 therefore gives

\[
Q(\mathrm{AK3})=Q(\mathrm{standard})=1
\]

for every Bobtcheva--Quinn-covered Lie-family/Gelfand--Kazhdan
specialization.

The symmetric pointed finite-group category
\(\operatorname{Vec}_{C_2,\mathbb Q}\) lies in Bobtcheva's general
contract but outside the mod-\(p\) Lie-lift contract because its unit
endomorphism field is \(\mathbb Q\). A direct evaluation counts the kernel
of the exponent matrix on \(C_2^2\); unimodularity makes that kernel
trivial, so this excluded category also gives value one on both
presentations. This does not prove homology dependence for all categories
allowed by the general Q construction.

The exact derivation and replay are in
`research/experiments/quinn-collapse-hypothesis-map/`.
