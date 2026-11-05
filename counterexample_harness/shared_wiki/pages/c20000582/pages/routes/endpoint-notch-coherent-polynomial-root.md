---
title: Endpoint-notch coherent polynomial-root boundary
description: The lowest-degree coherent quartic has constant positive core demand, but an exact all-carrier right-horizontal flow makes its normalized transport vanish.
---

# Endpoint-notch coherent polynomial-root boundary

For the dilated six-cycle, let \(A\) and \(B\) shift the two horizontal
root coordinates backward by \(t\). The collected polynomial operator and
its translated demand are
\[
C_t=(1-A)(1-B)(1-AB),\qquad
D_t=-(A-1)(B-1)^2(AB-1).
\]
Consequently \(D_t\) kills all rational bivariate polynomials of total
degree below four, has image \(\mathbb Q[u,v]\), and has kernel
\[
\mathbb Q[v]+\bigl(\mathbb Q[u]+v\mathbb Q[u]\bigr)+\mathbb Q[u-v].
\]
On quartics, only the \(uv^3\) and \(u^2v^2\) coefficients contribute to
the constant output.

The frozen normalized representative
\[
\beta_{m,j}(U,V,\lambda)
=-\frac{U^2V^2}{4t_j^4}\,
\mathbf 1_{\{|U|,|V|\leq L_m,\ |\lambda|\leq L_m^2\}}
\]
is interpreted as zero off the displayed carrier. On the complete core,
\[
C_t\beta_{m,j}=-u/t_j-v/t_j+2,\qquad
D_t\beta_{m,j}=1.
\]
This common positive component occurs on more than \(Q_m/8\) points at
more than \(K_m/2\) scales, so polynomial coherence itself is genuine.

The full noncommutative cycle nevertheless factors as
\[
1-A+AB^2-AB^2A+BA^2-B
=(-1-AB^2+B+BA)(A-1),
\]
where now \(A=a^t\) and \(B=b^t\) are group elements. After taking the
left-\(b^t\) root difference, this identity is the divergence of four
right-\(a^t\) edge families. Extending the root coefficient by zero makes
the identity include every horizontal and central carrier boundary
without a separate periodic or infinite-core substitution.

The exact hard-boundary variation is
\[
\sum_V\left|
V^2\mathbf1_{[-L,L]}(V-1)
-V^2\mathbf1_{[-L,L]}(V)\right|=4L^2.
\]
It yields
\[
\operatorname{TC}_m(d_m)<28L_m^7.
\]
A unique-root upper-right carrier corner remains in the full collision
norm and gives
\[
\|y_m\|_2\geq
\frac{L_m^4\sqrt{N_m(2L_m^2+1)}}{64}.
\]
Using the reviewed genuine inner-ball count,
\[
\frac{\Gamma_m(y_m)}{\|y_m\|_2}
<\frac1{12\sqrt{K_m}}\to0.
\]

This excludes only the frozen quartic with its hard finite carrier. It
does not imply decay for arbitrary polynomial or spline fields and does
not settle the unrestricted transport dichotomy. The derivation, exact
replay, and typed Jacobian factorization are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/coherent_polynomial_root/`.
