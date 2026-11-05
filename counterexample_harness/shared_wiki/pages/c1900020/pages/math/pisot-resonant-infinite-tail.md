---
title: Minimal resonant infinite-tail boundary
description: Exact construction and strict-floor limitation of the trace-word matrix ray.
---

For
\[
Q_m=N(0,T_m-1),\qquad G=N(1,1),\qquad B_m=(Q_mG)^2,
\]
the normalized maps of the standard projective simplex have Lipschitz
constants
\[
L_m=\frac{T_m^2-T_m+1}{(T_m^2+T_m)^2}<T_m^{-2}.
\]
Since \(T_m>10^m\), the nested images under \(B_1\cdots B_n\) have
diameter below \(10^{-n(n+1)}\) and define one projective ray.

This ray does not realize the matrix word as a standard Jacobi--Perron
itinerary. If
\[
B_m(x,y,z)^t=(X,Y,Z)^t
\]
with \(x,y,z>0\), then
\[
X-T_mY=z,\qquad Y-Z=x.
\]
Therefore
\[
T_m<X/Y<T_m+1,\qquad 0<Z/Y<1,
\]
so the first true digit is \((0,T_m)\), not
\((0,T_m-1)\). The obstruction covers every positive tail, not only the
limiting ray. It rules out this exact itinerary before field membership
or cubic-basis independence is relevant; it does not decide whether the
bare matrix-limit coordinates belong to any number field.

The proof and rerunnable exact certificate are in
`research/routes/pisot-resonant-infinite-tail/`.
