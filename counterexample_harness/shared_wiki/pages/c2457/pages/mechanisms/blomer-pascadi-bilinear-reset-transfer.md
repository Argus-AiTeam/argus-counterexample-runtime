---
title: "Blomer-Pascadi bilinear-reset transfer"
description: "Exact divisor-pair completion reaches one fixed Kloosterman kernel only at full dual length; the critical estimate supplies neither complete dispersion nor positive prime mass."
---

# Blomer-Pascadi bilinear-reset transfer

For the primitive seed block

\[
Q_0=26uv-1,\qquad Q_1=52uv-3=2Q_0-1,
\]

the exact identity

\[
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d
\]

expands the two-prime weight into square-free divisor pairs \(d\mid Q_0\),
\(e\mid Q_1\). Such pairs satisfy
\((d,e)=(d,26)=(e,52)=1\). Outside the separable \(3\)-adic case
\(3\mid e\), CRT gives a unit residue \(\rho\bmod c\), \(c=de\), and exact
Fourier completion gives

\[
\mathcal C_{d,e}
=c^{-2}\sum_{h,k\bmod c}
\widehat A(h)\widehat B(k)S(\rho k,h;c).
\]

This is a genuine instance of the kernel in Blomer--Pascadi
arXiv:2607.24311v1. The exact completion uses all \(c\) frequencies in both
variables. The direct source application that removes its gcd restriction
therefore has \(M=N=c\), where Theorem 1.1 contributes the non-saving factors

\[
c^{1/32},\quad c^{1/8},\quad c^{5/18}.
\]

Critical \(\sqrt c\)-blocks do receive the advertised
\(c^{-1/32+o(1)}\) saving, but the source does not localize the full spectra,
treat all complementary gcd strata, or recombine the blocks and varying
divisor moduli. In the balanced zero-mode benchmark, the displayed direct
envelope is \(c^{7/9+o(1)}\); even perfect localization into one critical
block leaves \(c^{15/32+o(1)}\), while the algebraic zero mode has exponent
zero. These are limitations of the stated upper bound, not lower bounds for
the true oscillatory error.

The paper contains no Vaughan or Heath-Brown prime expansion, positive prime
main term, Type-I package, growing-form uniformity, or iterable-prefix
theorem. Hence it does not by itself prove positive mass even for the first
two forms, and gives no \(K,\eta,s_0\) or fixed endpoint base. A future route
would need an additional modulus-summed dispersion and main-term theorem; the
reviewed reset class, primitivity, and conditional cost identities remain
valid.

The immutable v1 source, exact theorem dependency chain, full expansion, and
finite identity replay are in
`research/blomer_pascadi_bilinear_reset_transfer/`.
