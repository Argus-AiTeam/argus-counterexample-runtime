---
title: Strict-cone ray field nonmembership
description: Fixed-ideal norm obstruction excluding the reviewed singleton ray from the Pisot cubic field.
---

Let \(t_j=T_{j+1}\),
\[
W_j=
\begin{pmatrix}
t_j&t_j-1&t_j-1\\
1&1&1\\
1&0&1
\end{pmatrix},
\qquad
P_n=W_0\cdots W_n,
\qquad
Q_n=\prod_{j=0}^nt_j.
\]
The reviewed strict-cone itinerary has one normalized positive ray
\(r_m=(1,u_m,v_m)^t\).

If \(r_0\) had a representative \(z=(1,u_0,v_0)^t\in K^3\), then
\[
P_n^{-1}z=c_n(1,u_{n+1},v_{n+1})^t
\]
with
\[
0<(P_n^{-1}z)_2\leq\frac3{Q_nt_{n+1}}.
\]
For
\[
B_j=W_j^{-1}
=
\begin{pmatrix}
1&1-t_j&0\\
0&1&-1\\
-1&t_j-1&1
\end{pmatrix},
\]
the exact pair product satisfies
\(\|B_jB_{j-1}\|_\infty\leq4t_j\).
Writing \(H_n=\|e_2^tP_n^{-1}\|_1\), parity grouping gives
\[
\frac{H_n^2}{Q_nt_{n+1}}\longrightarrow0.
\]

A fixed integer \(d\) makes all coordinates of \(dz\) algebraic integers.
Thus the nonzero element \(d(P_n^{-1}z)_2\) has field norm of absolute value
at least one. The designated bound above and the two conjugate bounds
\[
|\iota_a((P_n^{-1}z)_2)|\leq
H_n\max_i|\iota_a(z_i)|
\]
instead force that norm to zero. Hence the singleton ray is not in
\(\mathbf P^2(K)\).

Its reviewed digit sequence is still exactly unbounded and therefore not
eventually periodic as a real ray. Field nonmembership means it is not an
admissible cubic basis and does not furnish the campaign counterexample.
