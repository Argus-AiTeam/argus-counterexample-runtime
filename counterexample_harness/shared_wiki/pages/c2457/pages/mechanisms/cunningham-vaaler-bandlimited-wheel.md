---
title: Vaaler band-limited fractional wheel
description: Exact sampled aliases, the low-bandwidth zero-mode floor, and interpolation back to the unresolved fractional moment.
---

For a truncated regular-prime wheel
\[
G_{h,y}(n)=\prod_{p\in{\cal P}_h(y)}
\left(1-\frac12\sum_{j=1}^h{\bf1}_{p\mid2^jn+1}\right),
\qquad
Q_y=\prod_{p\in{\cal P}_h(y)}p,
\]
let \(T=mQ_y\) be the least multiple of \(Q_y\) above the prefix endpoint.
Place the integer interval \(\{L_h+1,\ldots,X_h(C)\}\) between half-grid
endpoints on \(\mathbb R/\mathbb Z\).

Vaaler Theorem 19 gives a degree-\(N\) interval majorant with continuous
excess \(1/(N+1)\).  If its coefficients are \(c_k\), exact sampling gives
\[
U=T\sum_{a\bmod T}\widehat G_T(-a)
\sum_{\substack{|k|\leq N\\k\equiv a\pmod T}}c_k.
\]
The inner sum is mandatory: it contains every finite-group alias.  Wheel
periodicity gives
\[
\widehat G_T(a)=0\quad(m\nmid a),\qquad
\widehat G_T(mb)=\widehat G_Q(b).
\]

This creates an exact dichotomy.  If \(N<m\), only the zero wheel mode
couples and
\[
U=\delta_y\left(X_h(C)-L_h+\frac{T}{N+1}\right)
>\delta_yQ_y
=\prod_{p\in{\cal P}_h(y)}\left(p-\frac h2\right)>1.
\]
Once the bandwidth admits a nonzero wheel slot, its first possible slot is
\(b=1\), which has the full CRT conductor \(Q_y\).  Compact integer
frequency support therefore does not isolate low CRT conductors.

At the legal bandwidth \(N=2T-1\), every displacement from a sampled point
to either half-grid endpoint is an odd multiple of \(1/(2T)\).  Both Fejer
kernels vanish, so Vaaler Theorem 18 makes the sampled majorant equal the
interval indicator exactly.  Consequently
\[
\inf_N U_{h,C}(y,N)
=\sum_{L_h<n\leq X_h(C)}G_{h,y}(n),
\]
and optimizing the cutoff gives the original full fractional moment.

This boundary is not the box-Riesz negative shoulder, the causal hard
endpoint, an ordinary large-sieve \(L^2\) diagonal, or a total-variation
support mismatch.  It retires only the claim that Vaaler's excess and
compact support alone create a new contraction.  A new signed
full-conductor theorem, the actual strict fractional bound, and the
multiplier-two zero theorem remain open.
