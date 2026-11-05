---
title: Centered fixed-origin Cunningham shift dispersion
description: The signed one-step Fejer statistic retains target phase and has a negligible complete-period main, but its target-origin RMS discrepancy remains open.
---

# Centered fixed-origin Cunningham shift dispersion

For the truncated equality-safe wheel \(G_{h,y}\), set
\(f_{h,y}=G_{h,y}-\delta_y\), where \(\delta_y\) is its exact CRT mean.
Montgomery--Vaughan Lemma 16.8, equations (16.9)-(16.10) before the final
correlationwise triangle inequality, gives for every \(1\le H\le M\)
\[
\left|\sum_I f_{h,y}\right|^2
\le \frac{M+H-1}{H}B_I(H),
\]
where
\[
B_I(H)=C_I(0)+2\sum_{1\le r<H}(1-r/H)C_I(r)
\]
retains the full signed target-anchored correlations.

The exact local two-orbit factor is
\[
\mathbb E_{n\bmod p}g_p(n+r)g_p(n)
=1-\frac hp+\frac{\nu_{p,h}(r)}{4p},
\]
with \(\nu_{p,h}(r)=|R_{p,h}\cap(R_{p,h}-r)|\).  Every root collision,
zero shift, endpoint length \(M-r\), and prime-equality half weight is
retained.

The complete-period part is the translation average of \(B_I(H)\) and obeys
\[
0\le B^{\rm per}_{M,H}
\le MH\prod_{p\in{\cal P}_h(y)}\left(1-\frac{3h}{4p}\right).
\]
At \(y=z_h\), this is \(o(4^{-h})\) uniformly for \(H\le M\), while
\(M\delta_{z_h}=o(2^{-h})\).  Thus neither the zero shift nor collision
shifts create an asymptotic floor in the complete-period model.

An exact \(h=5\), \({\cal P}_5(13)=\{11,13\}\) cutoff-prefix replay
distinguishes the target \(\{3,\ldots,8\}\) from the equal-length translate
\(\{0,\ldots,5\}\):
their interval Fourier magnitudes and wheel sums agree, but their signed
Fejer statistics differ by \(-463/1716\).  The mechanism is therefore not
phase-blind.

The remaining obligation is target-specific.  At \(H=M\), if
\(P_k=\sum_{n=L+1}^{L+k}f_{h,z_h}(n)\), then
\[
B_I(M)=\frac1M\left(\sum_{k=1}^MP_k^2+
\sum_{k=1}^{M-1}(P_M-P_k)^2\right).
\]
No available theorem bounds this fixed-origin RMS prefix/suffix discrepancy
at the required \(O(4^{-h})\) scale, and no symbolic lower obstruction covers
all legal \(y,H\).  The route remains open rather than retired; the
multiplier-two zero count and Problem 1055 remain unresolved.

The exact completion of squares is
\[
B_I(M)=\frac{M+1}{2M}P_M^2+
\frac2M\sum_{k<M}(P_k-P_M/2)^2.
\]
Hence the requested RMS inequality is slightly stronger than the original
mass bound.  This identity does not create a deterministic obstruction:
balanced rounding of \(\delta\) between adjacent dyadic values gives an
abstract positive dyadic sequence with \(B_I(M)<2\delta^2\).  Any obstruction
must therefore use the actual fixed-origin CRT geometry.

A concrete sufficient remaining estimate is
\[
\sum_{n\in I}G_{h,z_h}(n)^2
\le \exp(o(h\log h))M
\prod_{p\in{\cal P}_h(z_h)}(1-3h/(4p)).
\]
It follows from the operator bound
\(B_I(M)\le M\sum_I f^2\).  This transfer has effective sieve dimension
\(3h/4\), while \(\log M/\log z_h=\Theta_C(\log^6h)=o(h)\);
the reviewed standard-sieve and fixed-degree Henriot bounds do not supply
the needed diagonal uniformity.

An exact all-translate sweep over 19 complete order-qualified structural
prefixes found target/translation-mean ratios from \(0.393\) to \(1.306\)
and target percentiles from \(0.070\) to \(0.846\).  Thus no persistent
one-sided endpoint bias was detected.  These moderate-height prefixes are
neither legal asymptotic cutoffs nor mean-compatible, so the sweep selects
against that proof mechanism only and is not evidence for either conclusion.
