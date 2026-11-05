---
title: "Pascadi sparse-Fourier prefix dispersion"
description: "The genuine off-diagonal prefix block has Pascadi's dispersion form and a growing sparse parameter, but the regular spectrum plus endpoint diagonal loses at least Y^(1/3+o(1))."
---

# Pascadi sparse-Fourier prefix dispersion

For the exact multiplier-\(16\) terminal Type-II block, the
quotient-isolating Poisson transform has a mandatory frequency range
\(H\asymp T\). After Cauchy--Schwarz in the Vaughan factor, two distinct
predecessor primes \(q_1,q_2\) give

\[
n=h_1q_2-h_2q_1,\qquad \varrho=2q_1q_2.
\]

This is source-faithfully Pascadi's Theorem 3 sequence with
\(\ell_1=q_2,\ell_2=q_1\), level \(\varrho\asymp Q^2\), and
\(L\asymp Q\). Its Assumption-14 parameters satisfy

\[
A_N\asymp T,\qquad
Y_N\asymp T^2/Q
=Y^{\tau-\kappa+o(1)}
\ge Y^{1/3+o(1)}
\]

in the genuine region
\(\theta=\tau+\kappa\), \(\tau\ge2/3\), \(\kappa\ge0\),
\(\theta\le1\). Thus sparse-Fourier admission itself succeeds.

Exact secondary completion uses every residue modulo \(t\) and maps
Corollary 16 with source level \(r=2q_1q_2\), \(s=1\), modulus
\(c=t\), and full dual length \(M\asymp T\). The Corollary-16 regular
factor is already at least \(QT^{5/2}\) before the three exact
\(T^{-1}\) normalizations. The resulting off-diagonal squared majorant is
at least \(QT^{-1/2}\). The excluded source diagonal
\(q_1=q_2,\ h_1=h_2\) has scale one and must be retained separately.

Writing \(A_1=\|a\|_1\), \(A_2=\|a\|_2\), comparison with the largest
absolute zero-mode envelope gives a dichotomy:

\[
A_1^2<2A_2^2
\Longrightarrow \text{diagonal loss }\gg Y^{1/3+o(1)},
\]

\[
A_1^2\ge2A_2^2
\Longrightarrow \text{off-diagonal loss }\gg Y^{1/2+o(1)}.
\]

The uniform \(1/3\) exponent is worse than the reviewed fixed-modulus
\(13/45\) obstruction by \(2/45\). Pascadi's \(Y_M,Y_N\) occur only in
an exceptional-spectrum multiplier which is at least one; they do not
reduce this regular term. This is a boundary of the stated source
assembly, not a lower bound for the true oscillatory sum or a universal
chain exclusion.

The primary-source map, exact identities, finite replay, and typed Jacobian
record are in `research/pascadi_sparse_fourier_prefix_dispersion/`.
