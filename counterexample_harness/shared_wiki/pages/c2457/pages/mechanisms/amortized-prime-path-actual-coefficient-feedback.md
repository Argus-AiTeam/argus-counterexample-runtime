---
title: "Actual-coefficient centered Type-II feedback"
description: "For b(L)=1, the exact centered terminal Type-II energy is a complete pair-of-prefix kernel; the universal strict Cauchy criterion fails exactly at L=3, while eventual failure remains open."
---

# Actual-coefficient centered Type-II feedback

For the complete \(D=4\) prime-prefix domain, let

\[
a_L(q)=
\sum_{\substack{\omega:\,P_{L-1}(\omega)=q\\
P_{L-1}(\omega)\le4^L}}
\prod_{i=0}^{L-1}\Lambda(P_i(\omega))\mu^2(P_i(\omega)).
\]

Freeze \(b(L)=1\), \(X_L=4^{L+1}\), and
\(U_L=V_L=\lfloor X_L^{1/3}\rfloor\).  For \(N=uv\), center the
terminal congruence before applying any norm:

\[
c_q(N)=\mathbf1_{q\mid N+1}-\frac1q.
\]

The terminal window \(J_q(N)=\mathbf1_{2q-1\le N\le X_L}\) retains the
exact multiplier \(m=(N+1)/q\).  With

\[
\rho_L(u,v)=\mu^2(uv)
\sum_{\substack{ef=v\\e>V_L}}\Lambda(e),
\]

the centered Type-II error is

\[
E_L=
\sum_{\substack{(u,v):\,u>U_L\\uv\le X_L,\ uv\ {\rm odd}}}
\mu(u)\rho_L(u,v)
\sum_\omega w_\omega J_{q_\omega}(uv)c_{q_\omega}(uv).
\]

Its weighted square expands exactly as

\[
\mathcal Q_L
=\sum_{\omega,\omega'}w_\omega w_{\omega'}
\mathcal C_L(q_\omega,q_{\omega'})
=\sum_{q,r}a_L(q)a_L(r)\mathcal C_L(q,r).
\]

Writing \(A_L(q,r)\) for true multiplier collisions \(mq=m'r\),
\(B_L(q\mid r)\) for one true congruence against the other endpoint's
window, and \(H_L(q,r)\) for the full overlapping windows gives

\[
\mathcal C_L(q,r)
=A_L(q,r)
-\frac{B_L(q\mid r)}r
-\frac{B_L(r\mid q)}q
+\frac{H_L(q,r)}{qr}.
\]

Every prefix word, endpoint cap, factorization \(uv=mq-1\), squarefree
factor, and endpoint multiplicity remains in this identity.  On the
endpoint diagonal,

\[
\mathcal C_L(q,q)
=\left(1-\frac2q\right)A_L(q,q)
+\frac{H_L(q,q)}{q^2}\ge0.
\]

All histories ending at the same \(q\) have the same centered column, so
their contribution is \(a_L(q)^2\mathcal C_L(q,q)\).  They do not yield an
independence gain.

After this diagonal is separated, the off-diagonal sum

\[
\sum_{q\ne r}a_L(q)a_L(r)\mathcal C_L(q,r)
\]

is signed.  No known consequence of the prefix recurrence controls it,
and a nonnegative envelope or generic norm loses the needed cancellation.
The frozen decomposition therefore supplies an exact reduction, not a
positive recurrence.

The proposed all-height strict criterion is false.  An exact rational
interval certificate at \(L=3\) gives

\[
84.705452<R_3<84.705453,\qquad
1652.121121<\mathcal Q_3<1652.121122,
\]

and

\[
222.913122<\mathfrak M_3<222.913123.
\]

Therefore

\[
R_3\mathcal Q_3>84\cdot1652>224^2>\mathfrak M_3^2,
\]

despite \(\mathfrak M_3>0\).  This refutes the claim that the strict
comparison holds for every \(L\), but it is not an eventual obstruction.

After grouping factor pairs by \(N\), write

\[
r_L(N)=\sum_{uv=N}\rho_L(u,v),\qquad
t_L(N)=\sum_{uv=N}\mu(u)\rho_L(u,v).
\]

Then \(E_L^2\leq T_L\mathcal Q_L\leq R_L\mathcal Q_L\), where
\(T_L=\sum t_L(N)^2/r_L(N)\).  Prime terminal rows have
\(r_L(P)=t_L(P)=0\), so the remaining eventual-failure obligation is a
new correlation between prime feedback and composite Type-II energy.
Neither \(t_L(N)=0\) rows nor the recursive endpoint congruences force that
correlation: the exact \(N=231\) row has positive \(r_3\), zero \(t_3\),
and can have zero centered value for a positive coefficient vector, while
the actual endpoint \(19\) has four prime candidates and only two
squareful composite candidates under the \(L=3\) cap.

Actual support can meet a dead row: at \(L=2\), the positive prefix
\(7\mapsto13\) has only the candidates \(25\) and \(51\) below the next
cap \(64\), so \(K_1(13;64)=0\).  Other endpoints still have positive
feedback.  This finite example neither proves all-height saturation nor
retires coefficient-sensitive feedback.

The full derivation and exact formal-log replay are in
`research/amortized_prime_path_actual_coefficient_feedback/`.
The separate `criterion_exact.py` certificate proves only the finite
\(L=3\) reversal and labels the eventual statement as open.
