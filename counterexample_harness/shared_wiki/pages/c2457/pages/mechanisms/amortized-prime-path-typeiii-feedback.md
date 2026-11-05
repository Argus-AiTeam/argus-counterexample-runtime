---
title: "Prime-sensitive three-block path feedback"
description: "The exact two-cut actual-path decomposition is a compatible transfer-matrix product; its boundary indices scalarize to the original feedback and do not create an independent Type-III gain."
---

# Prime-sensitive three-block path feedback

For old prefix length \(L\), set \(Y_L=4^L\), \(X_L=4^{L+1}\), and
\(\Psi=\Lambda\mu^2\). The exact cap at old-prefix position \(t<L\) is

\[
C_t(L)=1+\left\lfloor
\frac{Y_L-1}{2^{L-1-t}}
\right\rfloor,
\]

while \(C_L(L)=X_L\) for the final extension. Let
\(T_t^{(L)}(x,y)\) carry weight \(\Psi(y)\) exactly when
\(y=mx-1\leq C_t(L)\) for an even \(m\geq2\), and let
\(B_{a,b}^{(L)}=T_{a+1}^{(L)}\cdots T_b^{(L)}\). Every labelled
multiplier word is retained, and the boundary weight occurs exactly once.

For

\[
h_1=\lfloor L/3\rfloor,\qquad
h_2=\lfloor2L/3\rfloor,
\]

the complete old-scale feedback has the exact three-block form

\[
F_L=s_LB_{0,h_1}^{(L)}
B_{h_1,h_2}^{(L)}
B_{h_2,L}^{(L)}\mathbf1.
\]

The two internal endpoints are compatibility indices, not independent
variables. Defining

\[
\alpha_L=s_LB_{0,h_1}^{(L)},\qquad
\gamma_L=B_{h_2,L}^{(L)}\mathbf1,\qquad
\eta_L=B_{h_1,h_2}^{(L)}\gamma_L
\]

gives

\[
F_L=\sum_u\alpha_L(u)\eta_L(u)
=\sum_q a_L(q)K_1(q;4^{L+1}).
\]

Thus the bare split scalarizes exactly to the original prime-extension
sum. Removing compatibility creates non-path Cartesian cross terms;
keeping it requires a new lower bound for the actual compatible
coefficient support. Positive marginal mass in all three blocks is not
enough.

For a fixed complete multiplier word, every vertex is
\(A_tn-B_t\), where

\[
A_t=m_tA_{t-1},\qquad B_t=m_tB_{t-1}+1.
\]

The split therefore retains \(L+1\) simultaneous affine-prime weights in
the start variable. It does not reduce the problem to three independent
prime variables. A future positive recurrence must prove this
growing-dimension compatible affine-prime correlation directly.

This boundary retires only the two-cut decomposition as an independent
positivity mechanism. It does not refute such a future correlation and
does not prove unbounded \(D=4\) positivity.
