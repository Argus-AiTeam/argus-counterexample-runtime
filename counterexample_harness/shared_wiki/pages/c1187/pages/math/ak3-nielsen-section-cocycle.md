---
title: AK(3) signed-Nielsen section cocycle
description: Deterministic all-integral section defects, full Fox-cocycle coefficient recurrence, and a necessary-and-sufficient cubic coupling classifier.
---

# AK(3) signed-Nielsen section cocycle

For the fixed \(G_2,H,K_{0,+}\) prefix, the arbitrary fourth basis is
now handled by a deterministic exact section

\[
s:\operatorname{GL}_2(\mathbb Z)\to\operatorname{Aut}(F(a,b)).
\]

The section uses Euclidean row reduction. Each nonterminal division
strictly decreases the absolute remainder, so every unimodular input
terminates. Reversing the reduction gives literal section words and a
literal two-sided inverse.

For each directed atomic signed-Nielsen generator \(\gamma\), the
certificate recovers and freely verifies the exact inner defect

\[
s(M)\circ\widehat\gamma
=\iota_{q(\gamma,M)}\circ s(\gamma M).
\]

It retains both \(\bar q^{-1}\) and the full rank-one Fox correction

\[
J_{\iota_q\circ s}(x_i)
=\bar q^{-1}J_s(x_i)
+\bar q^{-1}\bigl(\overline{s(x_i)}-1\bigr)J_q,
\]

together with the pre-specialization word state
\((\alpha,\beta,C,F,\eta)\). Product, inverse, substitution, and inner
conjugation recurrences update this state at every Euclidean step.
Applying the accepted original-word AK(3) response operator then
extracts every cubic second-residual coefficient exactly.

On the regular locus, coupling is necessary and sufficient precisely
when the resulting coefficient map has a nonzero monomial containing
both a third-family variable \(g,g^*,g_0,g_0^*\) and a fourth-family
variable \(w,w^*,w_0,w_0^*\). This is an algorithmic all-integral
criterion, not a residue formula. At the cubic character, the
unrestricted mixed kernels range independently, so no nonzero joint
coefficient can be hidden by the terminal-axis parameterization.

The old formula is disproved exactly by

\[
L_1=\begin{pmatrix}7&2\\3&1\end{pmatrix},\qquad
L_2=\begin{pmatrix}7&5\\3&2\end{pmatrix}.
\]

It assigned zero coupling to both. Original-word replay in all sixteen
component patterns instead gives

\[
[g^*w]R_{2,\chi}(L_1)=-3-6\zeta_3,\qquad
[g^*w]R_{2,\chi}(L_2)=3-3\zeta_3.
\]

The 24 old regular representatives still replay their finite tables,
and all nine existing length-four keys replay from literal lifts and
inverses. The independently reviewed first-cell exclusion remains
valid. The direct third-cell point still has \(R_2=0\) but
\(R_1=-4-8\zeta_3\), so it is not an \(S_3\) lift.

The exact proof and certificates are in
[`THEOREM.md`](../../../../../research/experiments/ak3-nielsen-section-cocycle/THEOREM.md).
No Andrews--Curtis counterexample is claimed; \(C1187\) remains open.
