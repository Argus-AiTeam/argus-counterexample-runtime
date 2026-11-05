---
title: Depth-shifted Laakso center-relative birth-incidence boundary
description: Explicit actual-ball incidence bounds for the two newest spectral blocks and the exact failure of a fixed-offset extension to older births.
---

For the unchanged depth-shifted Laakso metric \(\rho_m\), let \(b_e^0\)
denote the positive representative of a level-\(k\) arm cell and define its
exact critical scale by
\[
4a_{m,k}^2=\rho_m(b_e^0,b_e^1)^2.
\]
The complete parent-arm odd block is used for endpoint incidence: it contains
the inherited arm descendants, signed zero modes, and both unsigned
\(\theta=\pm\sqrt{2/3}\) modes.  Its scale is
\[
4j_{m,k}^2=\rho_m(p_{f,1},p_{f,3})^2.
\]
Keeping this block coupled is necessary; separate four-cycle contrasts mix
with inherited arm energy after refinement.

An exact integer-kernel scan evaluated every actual center and every arm and
coupled endpoint birth level through depth three.  All nine tested
depth/birth families have maximum critical incidence one.  A complete
floating-point depth-four scan again found incidence one, but it is retained
only as falsification evidence.  On the exact depth-two coexistence graph,
Jacobian's bounded maximum-clique operation returned exact clique number one.

Finite propagation converts these observations into two all-depth newest-birth
theorems.  A graph ball of radius at most \(4^\ell\) lies in at most five
depth-\(\ell\) descendant cells, whose total full-degree volume is at most
\(10\cdot6^\ell+20\).  The scheduled band \(t=18^3\) then gives
\[
\left|\{e:b_e^0\in B_{\rho_m}(c,R)\}\right|
\le 5\cdot6^6=233280
\quad\text{when }R^2<8a_{m,m}^2.
\]
For the coupled endpoint block, every contributing lazy eigenvalue is below
\(31/32\).  The reviewed scheduled-multiplier bound and the band \(t=18^8\)
give
\[
\left|\{f:p_{f,1}\in B_{\rho_m}(c,R)\}\right|
\le5\cdot6^{16}=14105549537280
\quad\text{when }R^2<8j_{m,m}^2.
\]
Both statements hold for every actual center and depth.

For a retained level-\(k\) birth twin, put \(n=m-k\).  Its degree-two
horizontal row has level \(k\) as its last active bit, and its actual killed
path source is the center \(c_n=4^n\), not a source imported from another
horizontal fiber.  Thus
\[
a_{m,k}^2=\frac{16^{-m}}2
\sum_{r=0}^m96^r B_n^{\,2\cdot18^r}(c_n,c_n).
\]
The exact central Green moments are
\[
\mathcal H_{1,n}(c_n)=2\cdot3^n-\frac32,\qquad
\mathcal H_{2,n}(c_n)=\frac{40}{17}(54^n-3^n)+1.
\]
Their successive-depth margin is strictly positive:
\[
\mathcal H_{2,n}(c_n)
-60\cdot18^{n-1}\mathcal H_{1,n-1}(c_{n-1})
=\frac{120}{17}(54^{n-1}-3^{n-1})
+90\cdot18^{n-1}+1.
\]
Combining this identity with the reviewed scheduled-multiplier bounds, and
checking the bottom transition directly, proves
\[
a_{m,k}^2>5a_{m,k+1}^2
\quad(1\le k<m).
\]

The same fixed-offset certificate cannot control older births.  If the birth
is \(n\) levels old and the propagation band is shifted by any fixed \(s\),
the guaranteed support-volume scale grows at most as \((8/3)^n\), whereas
the required arm scale grows at least as \(5^n\).  Their ratio is bounded by
a constant times
\[
\left(\frac8{15}\right)^n\longrightarrow0.
\]
This retires only the fixed-offset disjoint-support plus cell-volume
recurrence.  A uniform incidence theorem for every birth level still needs a
cross-level heat-concentration argument with an offset growing with age, or a
different mechanism.  No uniform doubling constant and no divergent actual
packing has been obtained.
