---
title: Subgroup-sumset doubling blocks
description: Exact anchored block congruence and the pointwise lower-coverage gap between BGK Fourier decay and Garaev's powers large sieve.
---

# Subgroup-sumset doubling blocks

For an anchored prefix
\[
P=A2^a3^b-D
\]
and its multiplier-\(2\) block
\[
Q_t=2^t(P-1)+1,
\]
every odd prime \(\ell\nmid A3^b\) satisfies
\[
\ell\mid Q_t
\quad\Longleftrightarrow\quad
2^a+(A3^b)^{-1}2^{-t}
=(A3^b)^{-1}(D+1)\pmod\ell.
\]
Over complete exponent periods this is the pointwise incidence
\[
|A3^bH_\ell\cap(D+1-H_\ell)|,
\qquad H_\ell=\langle2\rangle.
\]
If \(\ell\mid A3^b\), division is invalid and the exact replacement is
\[
Q_t\equiv1-(D+1)2^t\pmod\ell.
\]
This branch has no root when \(\ell\mid D+1\), and otherwise has one root
class precisely when \((D+1)^{-1}\in H_\ell\).  The prime \(2\), the
\(3\)-branch, partial power orbits, and divisor-equals-value cases must be
handled separately.

BGK Theorem 6 in the primary 2006 paper gives complete-subgroup Fourier
decay when \(|H|>p^\delta\).  The canonical DOI is
`10.1112/S0024610706022721`; the terminal digit `0` sometimes attached to
this citation is incorrect.  Applying its maximum bound independently to
the two nonzero factors of the two-fold Fourier convolution makes the
error smaller than the zero-frequency main term only if the decay exponent
exceeds \(1/2\), which the theorem does not assert.  Sum-product growth is
not pointwise sumset coverage.

Garaev arXiv:math/0505396v2 controls additive power sums through weighted
second moments over primes with
\(\operatorname{ord}_p(2)>\Delta>X^{1/3}\).  Its consecutive-power
Theorem 6 remains an averaged upper bound; its almost-all-prime corollary
has an unspecified exceptional set.  It supplies neither a lower
representation count at a prescribed target nor a theorem for every
coefficient prime.

The two sources therefore do not yield a uniform contraction for a
multiplier-\(2\) block in the complete exact-class-anchored family.
The missing input is an effective weighted lower-coverage or two-coset
correlation theorem uniform in prefix histories, partial exponent windows,
coefficient primes, and equality subtraction.  This is a boundary of this
specific source assembly, not a universal chain exclusion.
