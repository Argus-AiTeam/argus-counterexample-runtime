---
title: Endpoint-notch nonlacunary gauge-support boundary
description: Exact three-layer notch gate and an all-depth rank-21 compression for a centrally retuned nonlacunary two-row strip.
---

# Endpoint-notch nonlacunary gauge-support boundary

For depth \(k\), let \(m=k+8\), \(R=2^{m(m+1)/2}\),
\(Q=R/16\), and \(Z=R^2/256\). The frozen support has two rows
\[
 L_j=(Q+2j,0,Z),\qquad
 U_j=(Q+2j,2,-Z-4Q),\qquad 0\leq j\leq k.
\]
Its horizontal radii lie between \(Q\) and \(2Q\), while consecutive
columns are separated by 2. Explicit commutator words put every point in
the genuine endpoint-notch word ball.

Every vertical connector has
\[
 A_j=4,\qquad W_j=-2Z+8j,
\]
and satisfies
\[
 \frac1{256}<\lambda_m|A_j-iW_j|<\frac1{64}.
\]
All normalized distortion-\(D\) target maps have consecutive connector
norm ratios in \((1/(4D),4D)\), but
\[
 \max_j |W_j|/A_j=R^2/512\longrightarrow\infty.
\]
Thus the exact three-layer gate genuinely escapes the radial-lacunarity
defect of the preceding rank-ten boundary.

The pointwise gauge
\[
 \tau(u,v,\zeta)=\zeta+2uv
\]
is nevertheless coherent on the entire support and obeys
\[
 |W_{xy}-(\tau(y)-\tau(x))|\leq4A_{xy}.
\]
Consequently the phase-deleted complete Hilbert EDM
\[
 \Theta_k(x,y)=H_m(A_{xy})+
 C_m(|\tau(y)-\tau(x)|)
\]
satisfies
\[
 \Delta_k/33\leq\Theta_k\leq99\Delta_k.
\]
Combining the reviewed horizontal and pure-central atlases gives one
complete Euclidean EDM of centered rank at most 21 at every depth:
\[
 \Delta_k\leq E_k
 \leq3267(\beta_0/\alpha_0)\Delta_k.
\]

**Scope.** This is an all-depth compression boundary for the frozen
two-row support, labels, gauge, and connectors. It does not cover other
nonlacunary supports, embed the complete endpoint-notch word balls, or
solve the Lang--Plaut problem.
