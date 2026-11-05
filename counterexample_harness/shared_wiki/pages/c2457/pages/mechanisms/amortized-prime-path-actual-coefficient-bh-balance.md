---
title: "Actual-coefficient one-hot B-H balance"
description: "Distinct actual endpoints never collide under the one-step cap; the residual B,B,H energy is a one-hot square, and direct combination with the complete Vaughan main saturates exactly at the original feedback F_L."
---

# Actual-coefficient one-hot B-H balance

For the complete \(D=4\) prime-prefix measure, freeze

\[
b(L)=1,\qquad X_L=4^{L+1},\qquad
U_L=V_L=\lfloor X_L^{1/3}\rfloor.
\]

The independently reviewed endpoint-separation input states that the
smallest complete length-\(L\) state endpoint is \(2^L+1\), uniquely, and
every other endpoint is at least \(2^{L+1}+1\). Its all-height conclusion
for distinct actual prime endpoints is

\[
qr>(4^{L+1})/2.
\]

Therefore the true off-diagonal collision term is identically zero:

\[
A_L(q,r)=0\qquad(q\ne r).
\]

This route imports that reviewed theorem and does not rebuild its finite
probe.

Define

\[
\begin{aligned}
I_q(N)&=J_q(N)\mathbf1_{q\mid N+1},\\
S_L(N)&=\sum_q a_L(q)J_q(N)/q,\\
A_L^\star(N)&=\sum_q a_L(q)I_q(N).
\end{aligned}
\]

The endpoint events \(I_q(N)\) are mutually exclusive, and the complete
centered energy is pointwise

\[
Z_L(N)^2=(A_L^\star(N)-S_L(N))^2.
\]

After expansion, this is exactly the endpoint diagonal plus the two
negative \(B\)-terms and the positive \(H\)-term. Every labelled prefix
word, terminal window, factor pair \(uv=N\), and squarefree correction is
retained.

The direct signed balance is saturated more strongly. On every Vaughan
factor pair, the principal and centered pieces satisfy

\[
\mu(u)\rho S_L+\mu(u)\rho(A_L^\star-S_L)
=\mu(u)\rho A_L^\star.
\]

Restoring the other three Vaughan pieces yields

\[
\mathfrak M_L+E_L
=\sum_N A_L^\star(N)\Lambda(N)\mu^2(N)
=F_L.
\]

Consequently this direct one-hot \(B\)-\(H\) reorganization has no positive
margin independent of the original prime-extension event. The positive
\(L=1\) base remains true, but no induction step follows. This closes only
the frozen direct balance route; other coefficient-sensitive analytic
estimates and unbounded \(D=4\) positivity remain open.

The full all-height proof, exact formal-log replay, reviewed input
provenance, and bounded Jacobian record are in
`research/amortized_prime_path_actual_coefficient_bh_balance/`.
