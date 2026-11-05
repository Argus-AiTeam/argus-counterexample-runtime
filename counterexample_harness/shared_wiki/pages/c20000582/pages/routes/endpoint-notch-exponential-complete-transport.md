---
title: Endpoint-notch exponential-period complete-transport boundary
description: Complete-period central-fiber flows give the preregistered exponential-period survivor a normalized full-transport gap below 14/m.
---

# Endpoint-notch exponential-period complete-transport boundary

The preregistered profile-balanced field
\[
q_m=2^{\lfloor K_m/4\rfloor}-1,\qquad
f_m=\chi_3+\psi_{q_m}/8
\]
really does survive the earlier direct-versus-primitive upper-bound screen.
That survival is not a lower bound for complete transport.

Extract a central-root interval whose length is divisible by both \(3\) and
\(q_m\). On each complete output fiber, the six collected square-wave terms
become three periodic differences with cyclic shifts
\[
t,\qquad t+2t^2,\qquad 2t+2t^2.
\]
If \(S_{m,j}\) is the sum of their cyclic distances modulo \(q_m\), then
\[
S_{m,j}\leq\min\{4t^2+4t,3q_m/2\},
\]
and
\[
\sum_j q_m^{(1-1/m)/2-1}
\frac{S_{m,j}}{t^{1-1/m}}<40.
\]
Greedy transport inside each complete period uses only central complete
pairs. Equal-length shifted interval corrections are routed in complete
period blocks, with the final incomplete blocks paired explicitly across
the core length. Horizontal root-box boundaries, unused central layers,
and the eleven largest or unmatched scales have separate exact costs.

The resulting flow has the exact frozen demand as its divergence and gives
\[
\operatorname{TC}_m(d_m)<2600mQ_m,\qquad
\frac{\Gamma_m(y_m)}{\|y_m\|_2}<\frac{14}{m}\to0.
\]
Thus the exponential-period field is ruled out as a positive
complete-transport-gap candidate. This does not establish decay for
arbitrary exponential-primitive fields or resolve the unrestricted
full-transport dichotomy.

The proof, exact replay, and typed Jacobian flow-conservation record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/exponential_complete_transport/`.
