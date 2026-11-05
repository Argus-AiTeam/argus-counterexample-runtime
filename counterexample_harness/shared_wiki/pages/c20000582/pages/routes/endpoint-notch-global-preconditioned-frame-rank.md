---
title: Endpoint-notch global rooted-star preconditioning boundary
description: A complete radial-augmentation EDM bounds every positively weighted full-ball rooted-star Gram by stable rank 16/9.
---

# Endpoint-notch global rooted-star preconditioning boundary

For every endpoint-notch word ball \(B_m\), choose any root \(o\) and use
all \(|B_m|-1\) edges from \(o\) to the other labels, with arbitrary positive
weights.  These incidence columns are independent, span the full zero-sum
space, contain every word-ball label, and may be preconditioned using any
radial scale rule.

For a complete Euclidean EDM \(E\), zero-sum incidence gives the exact
identities
\[
\operatorname{tr}(A^{\mathsf T}G_EA)=\sum_e w_eE_e,
\]
\[
(A^{\mathsf T}G_EA)_{(x,y),(u,v)}
=\frac{\sqrt{w_{xy}w_{uv}}}{2}
 (E_{xv}+E_{yu}-E_{xu}-E_{yv}),
\]
and the Gram rank is at most the target dimension.

The entire rooted-star class nevertheless fails at the fixed pair
\((n,D)=(2,2)\).  The full-ball map
\[
x\longmapsto
\bigl(F_m(x),\sqrt3\,\rho_m(o,x)\bigr)
\]
has complete EDM
\[
E_o(x,y)=\Delta_m(x,y)
+3(\rho_m(o,x)-\rho_m(o,y))^2.
\]
The reverse triangle inequality proves
\(\Delta_m\leq E_o\leq4\Delta_m\) on every pair.  On every rooted edge, the
added coordinate has squared length three times the source squared length.
If \(T=\sum_{x\ne o}w_x\rho_m(o,x)^2\), the weighted Gram therefore has
trace \(4T\) and squared Frobenius norm at least \(9T^2\).  Its stable rank
is at most
\[
\frac{16T^2}{9T^2}=\frac{16}{9}<2,
\]
simultaneously for every positive weight vector.

**Scope.** This is an exact all-depth complete-EDM countermodel for every
root and weighting in the frozen global rooted-star class.  It retains the
full source Hilbert component and every complete distance; it is not a
finite projection or proper-support completion.  It does not cover non-star
incidence frames, produce a fixed-rank EDM, compress the complete
endpoint-notch blocks, or settle the Lang--Plaut problem.
