---
title: AK(3) coupled fourth-cell \(S_3\) boundary
description: Exact simultaneous cubic zero followed by a support-unbounded seventh-cyclotomic exclusion of the complete coupled length-four cell.
---

# AK(3) coupled fourth-cell \(S_3\) boundary

Fix

\[
L_c=\begin{pmatrix}-1&0\\-2&-1\end{pmatrix},\qquad
\lambda_c=(a^{-1},a^{-2}b^{-1}),\qquad
\lambda_c^{-1}=(a^{-1},b^{-1}a^2)
\]

in the normalized path \(G_2,H,K_{0,+},L_c,I\). Its complete
unrestricted \(S_2\) fiber has four independent finite Laurent mixed
kernels and the forced determinant axes

\[
x_-=T^{-2}-T^2U_1U_2w_-,
\qquad
y_+=-T^{-2}-U_2U_3x_+.
\]

The exact cubic lattice is genuinely coupled. Each mixed kernel maps
to \(3\mathbb Z[\zeta_3]\), and there is an explicit complete-fiber
point at which both cubic residuals vanish. Its two full Laurent
residuals remain nonzero, so cubic vanishing is only a sieve.

The full first residual gives a support-unbounded exclusion at
\(A=B=t=\exp(4\pi i/7)\). It is identical in all sixteen component
patterns, depends only on \(x,y\), and becomes a Hermitian quadratic
after multiplication by a nonzero cyclotomic scalar. With
\(s=t+t^{-1}\), its leading minor, determinant, and Schur numerator
are

\[
13+33s+17s^2,\quad
-56-175s-91s^2,\quad
-1583-4318s-1703s^2.
\]

The root \(s\) lies in
\((-223/500,-89/200)\), where exact rational endpoint and derivative
bounds make all three quantities strictly positive. Completing the
square therefore proves that the full first residual never vanishes,
for arbitrary finite Laurent support and coefficients. All six
relation-cycle columns have zero reduced outer augmentation, and
terminal powers act by nonzero units.

Hence the complete fixed \(L_c\) cell does not lift to \(S_3\). This
settles only that cell; it does not produce an Andrews--Curtis
counterexample, and the global campaign remains open.

The rerunnable proof and typed certificates are in
[`THEOREM.md`](../../../../../research/experiments/ak3-coupled-fourth-cell-s3/THEOREM.md).
