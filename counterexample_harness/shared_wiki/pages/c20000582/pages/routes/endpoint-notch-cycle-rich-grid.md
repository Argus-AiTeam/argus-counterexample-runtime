---
title: Endpoint-notch cycle-rich grid boundary
description: Exact depth-growing scalar circulation and an all-depth rank-66 compression by radial angular charts and a parity marker.
---

# Endpoint-notch cycle-rich grid boundary

For \(k\geq2\), put \(m=k+8\), \(R=2^{m(m+1)/2}\),
\(N=2^k\), \(L=R/64\), \(s=L/N\), and \(Z=4L^2\).  The frozen
complete grid is
\[
 g_{ij}=(is,js,(-1)^{i+j}Z),\qquad0\leq i,j\leq N.
\]
Explicit commutator words have length at most \(9R/64\), so the whole
grid is a genuine subset of the endpoint-notch word ball.  Its image is
intrinsically \((1280\cdot2^{160})^2\)-doubling.

Every nearest-neighbor edge has \(A=s^2\) and
\[
 \frac{15}{2}L^2\leq|W|\leq\frac{17}{2}L^2.
\]
Consequently all edges lie in the fixed window
\[
 \frac1{1024}<R^{-2}|A-iW|<\frac1{256}.
\]
The counterclockwise outer boundary has
\[
 \sum W=4L^2,\qquad \sum A=\frac{4L^2}{N}.
\]
Since every point-potential increment telescopes, a bound
\[
 |W_{xy}-(\tau(y)-\tau(x))|\leq C A_{xy}
\]
on those edges forces \(C\geq N\).  Scalar phase deletion therefore
fails at a depth-growing exact rate.

This circulation is not an arbitrary-map obstruction.  On each
same-parity layer, polar coordinates give
\[
 |W|=2r_xr_y\sin|\theta_x-\theta_y|.
\]
Five fixed radial-annulus colors apply the reviewed pure-central
\(\mathbb R^{11}\) atlas to the angular labels \(2^{2j}\theta\);
the reviewed horizontal \(\mathbb R^{10}\) atlas controls radial
separation and cutoff changes.  Opposite parities satisfy
\[
 Z\leq|W|\leq3Z,
\]
so one marker coordinate of squared length \(C_m(Z)\) controls every
cross-layer central distance.  The complete map has dimension
\[
 10+5\cdot11+1=66
\]
and one distortion bound independent of \(k\).

**Scope.** The scalar gate passes, but the complete frozen grids admit an
all-depth rank-at-most-66 EDM.  This retires only this checkerboard schema;
it neither embeds the complete endpoint-notch word balls nor settles the
Lang--Plaut problem.
