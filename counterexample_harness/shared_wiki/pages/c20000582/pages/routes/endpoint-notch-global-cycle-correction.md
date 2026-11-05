---
title: Endpoint-notch global cycle-correction boundary
description: A monotone two-gauge scalar makes every corrected slot vanish and proves kappa_m=0, while label swap exhausts the whole two-gauge lift class at vanishing energy.
---

# Endpoint-notch global cycle-correction boundary

For a frame slot, let \(d\) be its left increment, \(q\) the matched
right-horizontal increment, \(z=d-q\), and
\[
\ell=\frac{|d|+|z|-|q|}{2}.
\]
The corrected numerator has the exact zero set
\[
d^2+|dq|-|z|\ell=0
\quad\Longleftrightarrow\quad dq\leq0.
\]
Thus the aggregate corrected loss vanishes exactly when every retained
left/right increment pair has opposite orientation.

In incidence coordinates \(s=z-uv\) and \(t=z\), every scalar
\(f(X(u,v,z))=\Phi(s,t)\) with \(\Phi\) coordinatewise nondecreasing
has that orientation on both generators at every scale.  The explicit
complete-pair one-Lipschitz witness
\[
f_m(X(u,v,z))=
\frac1{48}{\bf1}_{\{z-uv\geq0,\ z\geq18\}}
\]
has zero corrected loss at every depth.

On the reviewed six-cycle it has alternating value \(1/48\).  The exact
772-occurrence dual flow annihilates every full two-bank competitor,
including all off-cycle values, so its controlled residual satisfies
\(D_m(f_m)>0\).  Therefore
\[
\boxed{\kappa_m=0\quad(m\geq4),}
\]
in particular on the complete \(B_4\) incidence graph.

This coherent zero kernel does not have a uniform energy floor.  Every
complete-pair one-Lipschitz scalar \(\Psi_m(z,z-uv)\) is invariant under
the reviewed label swap and satisfies
\[
{\cal E}_m(\Psi_m(z,z-uv))
\leq\frac{221184}{2^{K_m}}
+\frac{509607936}{\sqrt m}\to0.
\]
This exhausts all periodic, threshold, nonlinear, and telescoping
two-gauge orbit lifts, including the displayed monotone kernel.
Zero-kernel scalars with essential dependence on the horizontal labels
\(u\) or \(v\) remain outside this boundary.

The proof, exact replay, raw 772-edge certificate reference, and typed
Jacobian records are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/global_cycle_correction/`.
