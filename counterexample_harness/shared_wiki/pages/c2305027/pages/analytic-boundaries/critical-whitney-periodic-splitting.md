---
title: Periodic cancellation on a critical Whitney tail
description: Exact all-prefix splitting boundary for the quarter-turn self-similar chain.
---

# Periodic cancellation on a critical Whitney tail

For \(\lambda=2i\), delete the disks

\[
\overline{B(\lambda^{-k},2^{-k}/100)},\qquad k\in\mathbb Z,
\]

from \(\mathbb C^*\), and cover the result by the annular cells

\[
V_k=\{2^{-k-3/4}<|z|<2^{-k+3/4}\}\cap X.
\]

The one-sided tail \(\Omega=\bigcup_{k\geq1}V_k\) is a planar
quarter-turn hole chain accumulating only at \(0\).  Its transition
distance \(d_k\) and half-thickness \(r_k\) satisfy

\[
\frac1{32}<\frac{r_k}{d_k}<\frac18,
\]

so the absolute plane Cauchy-potential scale is nonsummable.

Despite that critical scaling, every bounded analytic edge cocycle on
every finite prefix has a primitive bounded by

\[
(1+C_YD_\chi)\|a\|_\infty,
\]

independently of prefix length.  The reason is periodic cancellation:
the two-sided chain covers the finite-type bordered surface
\(X/\langle z\mapsto2iz\rangle\), and every cutoff derivative projects
into one compact subset where Brudnyi's bounded \(\bar\partial\)
theorem applies.

Consequently every normalized two-function Corona datum on this
one-sided tail has bounded Bezout coefficients.  This rules out the
entire declared periodic critical class, not nonperiodic or localized
critical neck chains.

The proof, exact balance inequality, source scope, and replay are in
`research/routes/critical-whitney-tail/EXHAUSTED_BOUNDARY.md`.
