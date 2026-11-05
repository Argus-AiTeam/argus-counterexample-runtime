---
title: Endpoint-notch quotient-weighted threshold-loss boundary
description: The proposed quotient-weighted loss is quantitatively equivalent to the still-open scalar concentration theorem, while a genuine slot rules out local coercivity.
---

# Endpoint-notch quotient-weighted threshold-loss boundary

Let
\[
A_m=\frac{73728}{h_m}+\frac{169869312}{\sqrt m}
\]
and let \(D_m(f)\) be the minimum frame energy of \(f-b\) over all full
two-bank potentials \(b\) satisfying the controlled complete-pair
Lipschitz condition.  For every complete-pair one-Lipschitz scalar,
\[
\boxed{
{\cal E}_m(f)-9A_m
\leq{\cal R}^{\rm th}_m(f)
\leq{\cal E}_m(f)+\sqrt{3A_m}.}
\]
The lower comparison is the reviewed common-threshold coarea reduction.
For the upper comparison, the threshold overlap is at most the original
increment length, and its excess over the original squared increment is
bounded by the product of the original and pure-horizontal increments.
The complete normalized pure-horizontal energy is at most \(3A_m\).

Writing
\[
\zeta_m=\sup_{\operatorname{Lip}(f)\leq1}D_m(f),
\]
the full two-bank decay theorem gives
\[
\zeta_m\leq\eta_m\leq
\left(\sqrt{\zeta_m}+\sqrt{27A_m}\right)^2.
\]
Therefore an estimate
\[
{\cal R}^{\rm th}_m(f)
\leq{\cal E}_m(f)-\alpha D_m(f)+\delta_m
\]
with fixed \(\alpha>0\) and effective \(\delta_m\to0\) implies
\[
\zeta_m\leq(9A_m+\delta_m)/\alpha
\]
and hence proves scalar concentration.  Conversely, effective decay of
\(\zeta_m\) gives the estimate with
\(\alpha=1\) and
\(\delta_m=\sqrt{3A_m}+\zeta_m\).  The proposed inequality is thus an
equivalent restatement of the missing global cycle-space estimate, not a
strict-loss bridge obtained from local threshold geometry.

Local coercivity also fails exactly.  On the genuine slot
\[
X(0,1,0),\quad X(1,1,1),\quad X(1,1,0),
\]
the complete-pair-safe values \(0,-1/96,1/96\) give normalized increment
pattern \((d,q,z)=(1,-1,2)\).  The threshold remainder numerator is twice
the original energy numerator, while
\[
d^2+|dq|-|z|\ell=0.
\]
Thus any successful proof must use global cycle compatibility rather than
a positive slotwise gap.

The reviewed \(772\)-occurrence complete quotient certificate was reused
without recomputation.  It proves a genuine quotient direction but does
not control the entire growing quotient space.  The theorem, exact replay,
and typed Jacobian record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/quotient_weighted_threshold_loss/`.
