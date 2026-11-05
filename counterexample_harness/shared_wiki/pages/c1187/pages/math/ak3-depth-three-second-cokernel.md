---
title: AK(3) depth-three second-cokernel classification
description: Arbitrary-basis cubic response law, the unique jointly visible residue type, and the complete first-lift obstruction for its least representative.
---

# AK(3) depth-three second-cokernel classification

For

\[
K=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in
\operatorname{GL}_2(\mathbb Z),
\]

the third Laurent parameter in the normalized \(G_2,H,K,I\) cell is
determinant-visible at
\((U,V)=(\zeta_3^{-1},\zeta_3)\) exactly when

\[
b-a\not\equiv0,\qquad d-c\not\equiv0\pmod3.
\]

On this locus, exact Fox-cocycle collection gives the complete
second reduced outer-augmentation response

\[
\rho_{2,\chi}(f_1,f_2,f_3)
=Q_\chi(f_1+\alpha_Kf_3),
\]

where \(f_2\) cancels and

\[
\alpha_K=
\zeta_3^{\,b(a-1)+d(c-1)+2}
U_{-a}(\zeta_3)U_{-c}(\zeta_3).
\]

Thus the third direction is also second-cokernel-visible exactly
when \(3\nmid ac\). Combining the two criteria yields eight residue
matrices modulo three:

\[
\begin{pmatrix}a&0\\c&-c\end{pmatrix},
\qquad
\begin{pmatrix}a&-a\\c&0\end{pmatrix},
\qquad a,c\in\{\pm1\}.
\]

They form one signed-permutation residue type represented by

\[
K_1=\begin{pmatrix}1&-1\\1&0\end{pmatrix}.
\]

The integral cell-orbit set remains infinite. Its complete invariant
is still the reviewed signed-permutation cell key; the cubic
conditions above classify which keys are visible without identifying
distinct integral keys merely because they have the same residue.

Actual free maps

\[
(ab^2,ab^3),\quad
(a^{-1}b,ab^{-1}a),\quad
(ba^{-2},ba^{-1}),\quad
(b,a^{-1}b)
\]

realize successive bases \(G_2,H,K_1,I\) and compose to the identity.
The complete unrestricted \(S_2\) fiber has

\[
f_1+f_3=A^2+(B-1)h
\]

for arbitrary finite Laurent \(h\). Since
\(\alpha_{K_1}=1\), its second residual at the cubic character is
exactly the reviewed

\[
\Phi_2(h)=C+L^*h-h^*L+D\,h^*h.
\]

The completed norm remains \(-14\), so a zero residual would require
an Eisenstein norm to be negative. The full original-word
\(2\times5\) operator has zero outer augmentation in all five
relation-cycle columns and all eight component patterns; terminal
powers act by units. Consequently no point of the complete
\(G_2,H,K_1,I\) fiber lifts to \(S_3\).

This is a boundary for the second minimum-height jointly visible
three-update cell. Higher integral keys and four-update cells remain
open, and no Andrews--Curtis counterexample is obtained.

The exact derivation and replay are in
[`THEOREM.md`](../../../../../research/experiments/ak3-depth-three-second-cokernel/THEOREM.md),
`arbitrary_response.py`, `k1_s2_fiber.py`,
`k1_unrestricted_residual.py`, and `k1_five_column.py`.
