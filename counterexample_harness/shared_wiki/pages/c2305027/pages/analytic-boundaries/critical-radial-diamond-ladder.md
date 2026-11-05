---
title: Aperiodic critical radial diamond ladders
description: Uniform Corona and complete-cocycle splitting bounds for the binary-radius radial ladder class.
---

# Aperiodic critical radial diamond ladders

Fix \(q=1/4\), and delete from \(B(1,1)\) the first \(N\) disks with
centers \(q^k\) and radii chosen independently from

\[
\left\{\frac{q^k}{64},\frac{q^k}{32}\right\}.
\]

Every resulting domain is planar, genus zero, and has connectivity
\(N+1\). Choosing the larger radius exactly at perfect-square indices
gives a non-eventually-periodic all-depth family. A planar spine has
\(N\) diamonds in series, and transition tubes of width comparable to
\(q^k\) have the critical scale sum

\[
\sum_{k=1}^N\frac{2^{-12}q^k}{q^k}=2^{-12}N.
\]

The constant forward incidence cocycle on this diamond graph has exact
primitive norm and flow-dual ratio \(N\). This is only an abstract graph
calculation.

After \(w=1-z\), the deleted-disk centers are \(1-q^k\). The
Jones-Marshall radial deleted-disk argument splits the Green critical
points into two uniformly interpolating sequences. The fixed ratio
\(q\) gives one Green-superlevel threshold for every depth and every
binary radius word. Hence, for each fixed Corona gap \(\delta>0\),

\[
\beta_{D_N}(F)\leq B_\delta
\]

for every normalized analytic pair, with \(B_\delta\) independent of
\(N\), the radius word, and the pair.

If local Bezout rows \(R_i\) have norm at most \(M\), and \(G\) is the
global row above, then

\[
b_i=\det(R_i,G),\qquad a_{ij}=b_i-b_j,\qquad
\|b_i\|_\infty\leq2MB_\delta.
\]

Thus every complete difference cocycle splits uniformly. The abstract
diamond flow cannot be realized with both uniformly bounded local rows
and bounded analytic adjoint defect.

This exhausts the radial binary-radius bounded-width class only.
Angularly turning and unbounded-width critical ladders are not covered.
The proof and exact replay are in
`research/routes/critical-diamond-planar-corona/`.
