---
title: AK(3) fourth-basis cokernel visibility boundary
description: Exact arbitrary-lift response, a least visible non-adjacent transition, and a support-unbounded exclusion of its complete S2 fiber.
---

# AK(3) fourth-basis cokernel visibility boundary

Fix

\[
K_{0,+}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]

in the normalized four-update path

\[
G_2,\ H,\ K_{0,+},\ L,\ I.
\]

For an actual free lift \(\lambda\) of
\(L\in\operatorname{GL}_2(\mathbb Z)\), the exact transition path is

\[
\Phi_0,\ \Phi_1,\ H^{-1}K_{0,+},\
K_{0,+}^{-1}\lambda,\ \lambda^{-1}.
\]

Substituting these actual words through the Fox--Magnus product,
inverse, conjugation, and terminal-normalization laws gives an exact
fourth-response operator for every lift.  If the lift is changed by
the inner automorphism \(\iota_q\), its abelian Fox rows obey

\[
J_{\iota_q\lambda}(x_i)
=\bar q^{-1}J_\lambda(x_i)
+\bar q^{-1}(\overline{\lambda(x_i)}-1)J_q.
\]

The first term is a Laurent unit multiple and the second is a
rank-one inner row killed by the reduced endpoint cokernel.  Therefore
inner changes do not alter visibility.

The response is not universally zero.  Every free lift of total image
length two is a signed permutation and is invisible by componentwise
terminal absorption.  The length-three lift

\[
\lambda=(ab,b),\qquad\lambda^{-1}=(ab^{-1},b),\qquad
L=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

is visible and therefore has least possible complexity.  Its transition
from \(K_{0,+}\) is

\[
LK_{0,+}^{-1}=
\begin{pmatrix}1&-1\\1&0\end{pmatrix},
\]

not the retired adjacent pure shear.  In all sixteen component patterns,

\[
R_1=\mathcal F(h,r+w)+A(1-B)g^*w
+A^{-1}(B^{-1}-1)gw^*.
\]

At a primitive seventh root \(A=B=t\),

\[
[g^*w]R_1=t-t^2\ne0.
\]

For a general
\(L=\left(\begin{smallmatrix}p&q\\r&s\end{smallmatrix}\right)\), the
complete \(S_2\) fiber has axis equations

\[
U_2U_3x_+ +y_+ +U_qU_sw_+=-T^{-2},
\qquad
T^{-2}x_-+U_{-p}U_{-r}w_-=T^{-4}.
\]

The remaining axes are free subject only to matching augmentations,
and every parameter has an independent
\((A-1)(B-1)\)-Laurent kernel.  Thus the parameterization has no
support bound.

For the selected \(L\), this reduces to

\[
x_-=T^{-2},\qquad
y_+=-T^{-2}-U_2U_3x_+-w_+,
\]

with \(x_+(1)=1\), \(w_+(1)=w_-(1)=\nu\), and
\(y_-(1)=-7-\nu\).  Hence

\[
x=A^2+(B-1)h
\]

for arbitrary finite Laurent \(h\).  At
\((A,B)=(\zeta_3^{-1},\zeta_3)\), the second residual is independent
of the other three families and equals

\[
R_2=C+ah-a^*h^*+Dh^*h,
\]

where

\[
C=\frac{-7-14\zeta_3}{3},\qquad
a=\frac{5+\zeta_3}{3},\qquad
D=-1-2\zeta_3.
\]

Exact completion gives

\[
(a^*-Dh)^*(a^*-Dh)=-\frac{14}{3}-DR_2(h).
\]

If \(R_2(h)=0\), a nonnegative complex squared norm would equal
\(-14/3\).  Therefore the complete selected \(S_2\) fiber has no
lift to \(S_3\), without a Laurent support or coefficient bound.

All six relation-cycle columns remain harmless: their source response
\(h^{-1}(g-1)e\) has zero ordinary augmentation, and the downstream
matrices are

\[
H^{-1}M_{\Phi_1},\ H^{-1},\ K_{0,+}^{-1},\ L^{-1},\ I,\ I.
\]

Terminal powers act by nonzero units.  This excludes one least visible
cell, not all \(L\), and does not produce an Andrews--Curtis
counterexample.

The proof and exact certificate are in
[`THEOREM.md`](../../../../../research/experiments/ak3-fourth-basis-cokernel-visibility/THEOREM.md)
and `arbitrary-l-fourth-response.json`.
