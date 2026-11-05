---
title: Endpoint-notch global collision-trace boundary
description: A critical-period complete-pair scalar refutes every vanishing-error adjoint contraction while its frame energy still decays.
---

# Endpoint-notch global collision-trace boundary

For the frozen non-star frame, the exact scalar-induced rectangle adjoint
always gives
\[
\mathcal V_m(G)\leq\mathfrak D_m(G).
\]
A proposed route sought a reverse contraction
\[
\mathfrak D_m(G)\leq\gamma\mathcal V_m(G)+\delta_m,
\qquad \gamma<1,\quad\delta_m\to0,
\]
for every complete-pair one-Lipschitz scalar.

This contraction is false. Let \(q_m\) be least with
\[
2^{q_m(m-1)}\geq m^{3m},
\]
put \(P_m=h_m^2/2^{q_m}\), \(r_m=16h_m/2^{q_m}\), and define
\[
G_m(X(u,v,z))=
\frac{d_mP_m^{(1-1/m)/2}}{2048}
\cos\left(\frac{2\pi(z-(h_m/16+1)u)}{P_m}\right).
\]
This scalar satisfies every complete-pair Lipschitz constraint. It belongs
to the reviewed two-bank class, so
\[
\mathcal V_m(G_m),\mathcal E_m(G_m)=O(m^{-1/2}).
\]
However, on a genuine positive-density family of non-dyadic long edges,
all dyadic beta incidences collide with nonnegative multipliers before the
absolute value. Exact period averaging and the endpoint-notch profile
balance give
\[
\mathfrak D_m(G_m)\geq
\frac{m}
{270\cdot2^{59}\lceil\log_2m\rceil^2}\longrightarrow\infty.
\]

The full theorem and exact replay are
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/global_collision_carleson/critical_period_collision_counterexample.md`
and `verify_critical_period_collision.py`.

The same route also checks the earlier localized magnetic packet at its
true maximal safe amplitude. Its complete collected divergence is
\(O(m^{-1/2})\), so rescaling that packet does not give the failure above.
The critical global period, rather than a missing local amplitude, is
decisive.

This boundary retires only the collision-collected adjoint contraction.
It does not refute scalar concentration, construct a positive-energy
potential, or settle the original counterexample objective. A future
endpoint-notch proof must control the central functional without requiring
\(\mathfrak D_m\) itself to vanish.
