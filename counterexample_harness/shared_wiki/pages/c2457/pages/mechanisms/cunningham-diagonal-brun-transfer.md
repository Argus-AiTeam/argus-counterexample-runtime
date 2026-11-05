---
title: Cunningham diagonal Brun transfer
description: Uniform exact Lemma-6 count and the frozen Theorem-5 C2 multiplier obstruction on the Cunningham diagonal.
---

For
\[
Q_h(n)=\prod_{\ell=1}^h(2^\ell n+1),\qquad
N=\left\lfloor\frac{C^h-1}{2^h}\right\rfloor,
\]
Henriot's proof parameters are
\[
\varepsilon_1=\frac{3\alpha}{25},\qquad
\varepsilon_2=\frac{\alpha}{25},\qquad
\varepsilon_3=\frac{\alpha}{50h}.
\]
Every legal Lemma-6 cutoff obeys
\[
z\leq N^{\varepsilon_3}<(C/2)^{1/50},
\]
so only finitely many primes depending on \(C\) occur. The corrected
\(\breve\rho\) conditions and the Chinese remainder theorem give the exact
full local-density main term. Uniformly in the height, cutoff, and
admissible valuation vector, its relative interval error is at most
\[
P_C N^{-19/25},
\]
where \(P_C\) depends only on \(C\). Thus the diagonal Brun remainder is
not the transfer obstruction.

The frozen proof of Theorem 5 fails later. If \(\eta\) is the
multiplicative-function parameter and
\[
u=50h(h+\delta^{-1})\eta,
\]
then the legal range is \(0<u<\alpha<1\), while the exponent in the
displayed \(C_2\) majorant satisfies
\[
h\beta_2=\frac{u-3\alpha}{50}.
\]
Its best closure saving is therefore only \(3/50\). Since
\(\log N=\Theta_C(h)\), this is a constant-size saving, whereas the local
Euler expression is at most
\[
\exp\left(-\frac12h\log h+h\log\log h+O_C(h)\right).
\]
Absorbing the frozen \(C_2\) majorant consequently requires an
\(\exp(\Omega(h\log h))\) envelope multiplier, not
\(\exp(O_C(h\log\log h))\).

This retires only the unmodified Lemma-6--Theorem-5 \(C_2\) absorption.
It neither lower-bounds the true full moment nor rules out a new
dyadic-specific conditional sieve.
