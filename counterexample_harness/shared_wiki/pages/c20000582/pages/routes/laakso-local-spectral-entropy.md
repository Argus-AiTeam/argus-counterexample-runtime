---
title: Depth-shifted Laakso local spectral entropy boundary
description: Exact newest-birth projected entropy and the failure of projected balls to lift to original diffusion balls.
---

For the unchanged depth-shifted Laakso metrics, write
\[
W_m(\theta)=\sum_{r=0}^m96^{r-m}
\left(\frac{1+\theta}{2}\right)^{2\cdot18^r},
\qquad
c_m=\sum_{r=0}^m96^r4^{-18^r}.
\]
Then \(W_m(0)=96^{-m}c_m\) and
\[
\frac14<c_m<\frac5{18}.
\]

There is one normalized localized arm mode for each of the
\(6^{m-1}\) newest cells. Its positive and negative middle vertices have
coordinates \(\pm a_m\), where
\[
a_m^2=3\cdot6^{m-1}W_m(0)=\frac{c_m}{2\,16^m}.
\]
Thus omitting any complete newest arm direction leaves spectral-tail
diameter at least \(2a_m\). In the isolated arm projection, all
\(6^{m-1}\) positive middle vertices lie in the radius-\(a_m\) ball about
an old vertex and have pairwise distance \(\sqrt2a_m\).

The endpoint-incidence eigenspaces have the same blockwise limitation.
Each of the \(6^{m-2}\) newest diamonds in \(L_{m-1}\) supplies disjoint
unit vectors
\[
\tfrac12(1,1,-1,-1)\in\ker B,\qquad
\tfrac12(1,-1,-1,1)\in\ker C.
\]
Their signed zero modes and both unsigned
\(\theta=\pm\sqrt{2/3}\) modes give \(6^{m-2}\) mutually orthogonal
three-coordinate projected blocks.

These projected packings are not original-metric packings. For every newest
cell not incident to the terminal \(s\), the time-one rows of \(s\) and
\(b_e^0\) have disjoint support and give
\[
\rho_m(s,b_e^0)^2\ge16^{-m}>4a_m^2.
\]
Hence \(6^{m-1}-1\) points in the isolated arm-projection ball are outside
the corresponding original \(\rho_m\)-ball.

The exact boundary is therefore limited to independent blockwise cutoff
arguments. A positive proof still needs an all-center, all-radius theorem
localizing which birth cells and endpoint-incidence supports can meet one
original ball, together with a summable finer-block tail. An explicit
sequence of original balls meeting unboundedly many cells at a scale
\(R<2\sqrt2a_m\) would instead be a divergent strict half-radius packing.
Neither alternative is currently established.
