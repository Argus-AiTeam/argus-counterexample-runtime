---
title: Nonquadratic complete-spectrum Fourier norm transfer
description: All global and conductor-band Fourier--Holder norm bounds inherit an exact unit floor from the residue-zero translate.
---

For the equality-safe truncated fractional wheel
\[
G_{h,y}(n)=\prod_{p\in{\cal P}_h(y)}
\left(1-\frac12\sum_{j=1}^h{\bf1}_{p\mid2^jn+1}\right),
\qquad Q_y=\prod_{p\in{\cal P}_h(y)}p,
\]
use the normalized coefficients
\[
\widehat G(a)=Q_y^{-1}\sum_{x\bmod Q_y}G_{h,y}(x)e_{Q_y}(-ax)
\]
and the exact transform of the actual interval
\[
K_{L,M}(a)=\sum_{u=1}^M e_{Q_y}(a(L+u)).
\]
Finite inversion retains the principal mode and every conductor:
\[
\sum_{u=1}^M G_{h,y}(L+u)
=\sum_{a\bmod Q_y}\widehat G(a)K_{L,M}(a).
\]

Every even coefficient moment is an exact cyclic additive energy:
\[
\sum_a|\widehat G(a)|^{2k}
=Q_y^{1-2k}\sum_t|G_{h,y}^{*k}(t)|^2.
\]
The local moments factor through the powers-of-two root orbit
\(R_{p,h}\):
\[
\sum_{\xi\bmod p}|\widehat g_p(\xi)|^{2k}
=\left(1-\frac h{2p}\right)^{2k}
+\frac{pE_k(R_{p,h})-h^{2k}}{2^{2k}p^{2k}}.
\]
Thus higher moments and all root collisions can be evaluated without
support truncation or an independence assumption.

The decisive boundary is translation invariance. Translating an interval
multiplies each \(K_{L,M}(a)\) by a unit complex phase, so every global
\(\ell^r\)-dual bound, every sum of exact conductor-block dual bounds, and
every canonical two-level mixed norm has the same value at every origin.
It therefore also bounds \(\{0,\ldots,M-1\}\). Since all wheel weights are
nonnegative and \(G_{h,y}(0)=1\), every such upper expression is at least
one, for every cutoff, exponent, and conductor partition.

This does not lower-bound the target fractional moment. It retires only
phase-blind norm closure. Exact target-phase cancellation before norms,
non-modulation-invariant transforms, and nonperiodic larger-prime
information remain outside the result. The mechanism is distinct from
Vaaler support interpolation, explicit translation-supremum discrepancy,
ordinary large-sieve \(L^2\), and physical-space nonquadratic support
polynomials.
