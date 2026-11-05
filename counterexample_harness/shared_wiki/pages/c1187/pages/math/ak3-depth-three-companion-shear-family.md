---
title: AK(3) depth-three companion-shear family
description: Exact all-integer exclusion of the two-sign companion-shear family by retained-jet recurrences and one shared seventh-cyclotomic full-residual obstruction.
---

# AK(3) depth-three companion-shear family

For

\[
K_{n,\epsilon}=
\begin{pmatrix}
-n&\epsilon\\
-1&0
\end{pmatrix},
\qquad n\in\mathbb Z,\quad\epsilon\in\{-1,+1\},
\]

the complete unrestricted \(S_2\) Laurent fiber of the normalized
AK(3) cell \(G_2,H,K_{n,\epsilon},I\) has no lift to \(S_3\).
This support-unbounded theorem covers all eight component patterns,
all three internal and both terminal relation-cycle freedoms, and all
terminal powers.

The exact free lift and inverse are

\[
T_{n,\epsilon}=(b^\epsilon a^{-n},a^{-1}),
\]

\[
T_{n,+}^{-1}=(b^{-1},ab^{-n}),\qquad
T_{n,-}^{-1}=(b^{-1},b^na^{-1}).
\]

The retained first-Fox/second-Fox state has exponent 18.  The complete
fiber parameter jets are also 18-periodic because \(U_{18}\) and its
first derivative vanish modulo three at both retained axis points.
Exact comparison inside that proved period sharpens the systems to
period six.  The only first-jet survivor classes are

\[
\epsilon=-1:\ n\equiv2,3\pmod6,\qquad
\epsilon=+1:\ n\equiv3,4\pmod6.
\]

They have respectively 486 and 243 common zeros over the eight
retained \(\mathbb F_3\) parameter values.  These are necessary local
solutions, not lifts.

At \(A=B=t\), with \(t\) a primitive seventh root, the complete
original-word residual coefficients are seven-periodic in \(n\):
the specialized Fox--Magnus states of \(a^7\) and \(b^7\) are the
identity because \(t^7=1\) and \(U_7(t)=0\).  Exact collection for the
fourteen sign/residue representatives gives one common Hermitian
quadratic form.  Its leading minor, determinant, and completed-square
numerator are

\[
13+33s+17s^2,\quad
-56-175s-91s^2,\quad
-1583-4318s-1703s^2,
\]

where \(s=t+t^{-1}\) lies in
\((-223/500,-89/200)\).  Exact endpoint bounds make all three
strictly positive.  Hence the first full residual cannot vanish for
any values of the arbitrary finite Laurent parameters.

The response created by inserting a relation-cycle row \(e\) into an
actual Magnus conjugator \(H=(h,d)\) of \(X=(g,r)\) is exactly

\[
\operatorname{row}(H_e^{-1}XH_e)
-\operatorname{row}(H^{-1}XH)=h^{-1}(g-1)e.
\]

Its ordinary augmentation is zero.  Fixed conjugation preserves that
zero, and every later free substitution multiplies the two-row
augmentation state by its exponent matrix.  For the three internal
slots the downstream matrices are respectively
\(H^{-1}M_{\Phi_1}\), \(H^{-1}\), and \(K_{n,\epsilon}^{-1}\);
the two terminal slots have identity transport.  Combining this with
the two exact endpoint-factor quotients gives a zero \(2\times5\)
outer-augmentation matrix for every \(n\), both signs, and all eight
patterns.  The two terminal powers independently multiply the
residuals by nonzero Laurent units.

The proof and rerunnable certificate are in
[`THEOREM.md`](../../../../../research/experiments/ak3-depth-three-companion-shear-family/THEOREM.md)
`companion-shear-certificate.json`, and
`relation-cycle-operator.json`.  The theorem excludes this family
only; it is not an Andrews--Curtis counterexample and does not decide
arbitrary integral \(K\).
