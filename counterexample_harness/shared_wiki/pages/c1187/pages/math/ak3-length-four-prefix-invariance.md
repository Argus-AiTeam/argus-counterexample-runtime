---
title: AK(3) length-four prefix classification
description: Exact length-four normalized cells, the reviewed first-cell exclusion, the direct coupled-cell replay, and withdrawal of the false residue extrapolation.
---

# AK(3) length-four prefix classification

Fix the four-update prefix \(G_2,H,K_{0,+}\), and compare fourth
bases under the full \(B_2^4\)-left and common-\(B_2\)-right normalized
cell action. Exact enumeration through total reduced image length four
checks 544 nonempty reduced word pairs and finds 200 free bases with
literal two-sided inverses. They form nine normalized keys: the five
independently reviewed keys through length three and four new
length-four keys. All four new keys are visible at a primitive seventh
root.

The first new visible key is represented by

\[
\lambda_0=(a^{-1}b^{-2},b^{-1}),\qquad
\lambda_0^{-1}=(b^2a^{-1},b^{-1}),\qquad
L_0=\begin{pmatrix}-1&-2\\0&-1\end{pmatrix}.
\]

Its exact cubic second residual is the same in all sixteen component
patterns and contains no \(r,g,w\) coefficient. The complete
unrestricted \(S_2\) fiber has \(x=A^2+(B-1)h\), so the accepted
completion would force a nonnegative complex norm to equal
\(-14/3\) if the residual vanished. Hence this complete cell does not
lift to \(S_3\).

The repeated collapse is not a prefix invariant, but the former
matrix-only arbitrary-\(L\) formula was also false. Its 24 regular
residue representatives all pass, yet the regular unimodular matrices

\[
\begin{pmatrix}7&2\\3&1\end{pmatrix},\qquad
\begin{pmatrix}7&5\\3&2\end{pmatrix}
\]

both have zero in the withdrawn formula and nonzero exact
\(g,w\)-coupling under original-word replay. In particular, the first
has

\[
[g^*w]R_{2,\chi}=-3-6\zeta_3.
\]

Therefore neither the old \(\alpha_L\) expression nor the criterion
\(3\nmid pr\) classifies arbitrary integral \(L\). The corrected
all-\(L\) result retains the deterministic signed-Nielsen section
defect, its Laurent unit and Fox row, and the full second-Fox cocycle;
see [AK(3) signed-Nielsen section cocycle](ak3-nielsen-section-cocycle.md).

A distinct new length-four key is represented by

\[
\lambda_c=(a^{-1},a^{-2}b^{-1}),\qquad
L_c=\begin{pmatrix}-1&0\\-2&-1\end{pmatrix}.
\]

Direct original-word collection gives
\([g^*w]R_{2,\chi}=-1-2\zeta_3\ne0\).
The literal complete-fiber point

\[
x=A^2-A^{-2}-A^{-3},\quad
y=-B^{-2}+1+2B+2B^2+B^3,\quad
g=-1,\quad w=1
\]

has \(R_{2,\chi}=0\) in all sixteen patterns, while
\(R_{1,\chi}=-4-8\zeta_3\ne0\). It is therefore not an \(S_3\) lift,
but it proves that the old \(h\)-only norm obstruction is not uniform
and supplies a genuinely new coupled fiber for the next route.

The exact proof and rerunnable certificates are in
[`THEOREM.md`](../../../../../research/experiments/ak3-length-four-prefix-invariance/THEOREM.md).
No Andrews--Curtis counterexample is claimed; \(C1187\) remains open.
