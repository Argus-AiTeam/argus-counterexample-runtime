---
title: Cunningham soft half-sieve transfer
description: Exact squarefree root-class density and the all-level obstruction to the optimal Selberg Lambda-squared absolute-remainder closure.
---

For
\[
Q_h(n)=\prod_{j=1}^h(2^jn+1),
\]
the pointwise relaxation is
\[
2^{-\Omega(Q_h(n))}\leq2^{-\omega(Q_h(n))}
\leq\prod_{p<z}\left(1-\frac12{\bf1}_{p\mid Q_h(n)}\right).
\]
If \(t_p=\operatorname{ord}_p(2)\), the number of distinct roots is
\[
\rho_h(2)=0,\qquad \rho_h(p)=\min(h,t_p)
\]
for odd \(p\). A prime shared by several labelled forms is one root class
and contributes one factor \(1/2\), not one factor per label. The exact local
mean is therefore
\[
1-\frac{\rho_h(p)}{2p}.
\]

The soft weight has a positive abstract-sieve realization: independently
mark each distinct root modulo \(p\) with probability \(1/2\), and retain an
integer when it avoids every marked root. For squarefree \(d\), the resulting
density and fixed-prefix discrepancy are
\[
\varpi_h(p)=\frac{\rho_h(p)}2,\qquad
R_d=\frac{\varepsilon_d}{2^{\omega(d)}},\qquad
N_d=\frac{X\rho_h(d)}d+\varepsilon_d.
\]
At a prime,
\[
R_p=\frac{pN_p-X\rho_h(p)}{2p},\qquad
R_p=0\Longleftrightarrow p\mid X.
\]

At the fixed cutoff
\[
z_h=\exp\left(\frac{h}{\log^6(h+2)}\right)<2^{h-1},
\]
the reviewed regular-prime estimate gives
\[
\log V_h(z_h)\leq-\frac12h\log h
+\frac72h\log\log(h+2)+O(h).
\]

Heath-Brown's exact optimal Selberg \(\Lambda^2\) theorem gives, for every
level parameter \(\xi\),
\[
\frac{X}{G_h(\xi,z_h)}
+\sum_{\substack{d<\xi^2\\d\mid P(z_h)}}
3^{\omega(d)}|R_d|,
\qquad
g_h(p)=\frac{\rho_h(p)}{2p-\rho_h(p)}.
\]
This expression has an exhaustive obstruction. If a prime contributing to
\(G_h\) does not divide \(X\), its source-mandated remainder term is greater
than \(2^{-h}\). If every contributing prime divides \(X\), then
\[
G_h\leq\prod_{p\mid X}(1+g_h(p))
\leq\operatorname{rad}(X)\leq X,
\]
so the main term is at least one. Thus no legal \(\xi\) crosses the required
\(2^{-h}\) threshold, and the relative multiplier loses the full leading
\(\tfrac12h\log h\) local decay.

This boundary is specific to the optimal Selberg closure with an absolute
interval-discrepancy remainder. It is not a lower bound for the true moment
and does not exclude a theorem that retains signed fixed-origin
cancellation.
