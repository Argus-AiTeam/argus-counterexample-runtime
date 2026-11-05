---
title: Strict-cone trace itinerary
description: Exact all-phase floor certificate for the one-trace two-spacer infinite word.
---

For
\[
W_m=N(0,T_{m+1}-1)N(0,1)^2,\qquad m\geq0,
\]
the normalized block map on
\(\Delta=\{[1:u:v]:0\leq u,v\leq1\}\) is
\[
\Phi_t(u,v)=
\left(
\frac{1+u+v}{t+(t-1)(u+v)},
\frac{1+v}{t+(t-1)(u+v)}
\right),
\qquad t=T_{m+1}.
\]
It maps \(\Delta\) into its strict interior and has sup-norm Lipschitz
constant at most \(1/t\). Since \(T_{m+1}>10^{m+1}\), the nested positive
cones have one projective ray.

The generic inverse branch
\[
N(a,b)(r,s,q)^t=(br+q,r,ar+s)^t
\]
has true standard digit \((a,b)\) exactly when \(0<s<r\) and
\(0<q<r\). Every block-tail ray lies in this strict cone. If
\(r_{m+1}=(x,y,z)^t\), its internal suffixes are
\[
(x,y,z)^t,\qquad
(x+z,x,y)^t,\qquad
(x+y+z,x+z,x)^t,
\]
and all three also lie in the strict cone. Their exact ratio intervals
give the digits
\[
(0,1),\qquad(0,1),\qquad(0,T_{m+1}-1)
\]
in reverse suffix order. Hence the unique ray realizes the full frozen
word at every phase.

This is an exact positive-real-ray candidate only. It does not decide
whether the ray lies in \(\mathbf P^2(K)\).
