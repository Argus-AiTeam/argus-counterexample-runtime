---
title: Endpoint-notch direct-versus-primitive routing screen
description: Subexponential collision-nondegenerate root fields decay uniformly, while one exponential-period field leaves more than one eighth of the genuine scales unscreened.
---

# Endpoint-notch direct-versus-primitive routing screen

For a rational periodic zero-mean root field, let \(A_m\) be its
amplitude and let \(B_m\) be the smallest sup norm among its periodic
primitives. Suppose fixed \(a,\alpha,\beta>0\) give collision magnitude
at least \(a\) on at least \(\beta Q_m\) common-interior points at each
of at least \(\alpha K_m\) matched scales. The profile-balanced
six-cycle then satisfies the explicit all-depth bound
\[
\frac{\Gamma_m(y_m)}{\|y_m\|_2}
<
\frac{4A_m(J_m+5)+1+8B_mK_m/(2L_m+1)}
 {1000a\sqrt{2\alpha\beta}\,K_m},
\]
where
\[
J_m=\min\left\{K_m-5,
\left\lceil
\frac{2(\lceil\log_2(1+B_m)\rceil+\lceil\log_2m\rceil+12)}
 {1-1/m}
\right\rceil\right\}.
\]
Consequently every uniformly bounded, uniformly
collision-nondegenerate field with
\(\log(1+B_m)=o(K_m)\) has normalized gap tending to zero. This
simultaneously excludes all polynomial and subexponential primitives
in that precise class.

The preregistered successor uses
\[
q_m=2^{\lfloor K_m/4\rfloor}-1,\qquad
P_m=\operatorname{lcm}(3,q_m),\qquad
f_m=\chi_3+\psi_{q_m}/8.
\]
It has exact zero mean, amplitude \(9/8\), protected collision
magnitude at least \(3/4\), and optimal primitive norm
\[
P_m/192<B_m<P_m/16,\qquad
2^{K_m-8}<P_m^4<81\cdot2^{K_m}.
\]
For more than \(K_m/8\) genuine scales, the exact screening expression
chooses the direct certificate \(9/2\); hence this field survives the
restricted direct/primitive upper-bound screen. The direction-correct
certificate uses
\[
R_{m,j}\geq
2\sqrt{\Phi_m(1,8\cdot2^j)/H_m(4^j)}.
\]
The weakest endpoint \(m=8,j=4\) is enclosed rigorously with
\(B_8R_{8,4}>291/25\); an integral profile lower bound and an exact
integer induction cover every \(m\geq13\).

Screen survival is not a lower bound on complete transport and is not
a counterexample. It only keeps this exponential-period field eligible
for an unrestricted Kantorovich-dual lower-bound route. The proof,
exact replay, and typed Jacobian record are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/direct_primitive_screen/`.
