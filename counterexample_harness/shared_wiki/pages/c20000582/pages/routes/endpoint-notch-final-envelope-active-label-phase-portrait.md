---
title: Endpoint-notch final-envelope old-depth erasure
description: Every d=42 longest-envelope edge decays after old-scale normalization, without selecting an active controller.
---

# Endpoint-notch final-envelope old-depth erasure

For the canonical longest final envelope, freeze old depth \(d=42\).
For every \(m\ge512\), both parity shifts \(\epsilon\), and
\[
J=S_m-(30m+\epsilon+42),
\]
the two adjacent edges of the genuine old-screw triple satisfy
\[
\left(
 \frac{F_{m,\epsilon}(q_{r+1})-F_{m,\epsilon}(q_r)}
 {\sqrt{C_m(t_{30m+\epsilon+42})}}
\right)^2
\le
e_{m,\epsilon}
:=(2^{20}m)^2 2^{-2J/m},
\qquad r=0,1.
\]
Here \(J/m>m/8-31\), so
\[
e_{m,\epsilon}<m^2 2^{102-m/4}\longrightarrow0.
\]
Consequently the normalized genuine two-edge contribution is at most
\(2e_{m,\epsilon}\) and also tends to zero.

The proof is active-controller independent. An explicit genuine
finite-carrier periodic controller first gives a common envelope upper
bound below \(-2c_{S_m}/3\). This confines every actual endpoint
minimizer to a fixed final-scale box. A complete all-band raw-amplitude
bound then shows that every such minimizer remains at normalized metric
distance at least \(1/8\) from the entire neighboring query segment.
On this compact annulus the exact three-power endpoint-notch profile has
the uniform derivative bound
\[
|\partial_A D_m|,\ |\partial_wD_m|<2^{15}m.
\]
The query motion changes both pair variables by less than \(9\,2^{-J}\),
giving
\[
\frac{|F(q_{r+1})-F(q_r)|}{c_{S_m}}
<2^{20}m\,2^{-J}.
\]
Finally, exact central-profile monotonicity yields
\[
\frac{c_{30m+\epsilon+42}}{c_{S_m}}
>2^{-J+J/m},
\]
which supplies the extra \(2^{-J/m}\) decay.

At each endpoint the argument may choose any attained minimizer and test
it at the other endpoint. Reversing the test gives the opposite
inequality, so every tie in the genuine finite carrier is covered.
This bypasses rather than classifies the globally active controller
labels.

This result retires the fixed-\(d=42\) final-top flip as a seed for a
positive-density all-scale theorem. It does not control depths growing
with \(m\), decide the fixed complete \({\mathsf Q}_m\) form, or provide
the campaign counterexample.

Evidence:
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/full_4adic_slack_tree/complete_period_quadratic_persistence/global_incidence_aggregate/reachable_suffix_retention/horizontal_controller_migration/final_envelope_active_label_phase_portrait/`.
