---
title: Self-channel internal Hopf boundary in Ver_7^+
description: Exact empty-scheme classification on 2*1+L_3 with a lifted unit-ideal certificate.
---

# Self-channel internal Hopf boundary in
\(\operatorname{Ver}_7^+\)

For
\[
H=2\mathbf1\oplus X,\qquad X=L_3,
\]
the exact trace-quotient fusion rule
\[
X^2=\mathbf1+X+L_5
\]
permits both \(\mathbf1\)- and \(X\)-output multiplication channels. The
complete standard-unit/counit gauge has 16 variables: five multiplication,
five comultiplication before cocommutativity, two antipode, two integral,
and two cointegral coefficients. No allowed channel is discarded.

The exact symmetry scalar on the self-output channel is
\(R_X^{XX}=-1\). Contracting cocommutativity in the complete quotient basis
therefore gives
\[
d_{aX}=d_{Xa},\qquad d_{XX}=0.
\]
All Hopf, cocommutativity, unimodularity, and normalization diagrams produce
44 distinct polynomial generators over \(\mathbb F_7\).

The structure scheme is empty. In its coordinate ring, integral,
cointegral, and normalization equations make
\[
L_aq_a(1+m_{aa}d_{aa})=1.
\]
They also identify
\[
m_{aX}=m_{Xa}=m_{aa}=u,\qquad
d_{aX}=d_{Xa}=d_{aa}=v.
\]
One complete bialgebra coordinate then becomes
\[
(1+uv)^2=0,
\]
contradicting the fact that \(1+uv\) is a unit. Independently, Singular
returns reduced Groebner basis \([1]\), and a 44-entry `liftstd` vector
reconstructs \(1\) from the original generators exactly.

Consequently there is no admissible Hopf point on this object and no
Bobtcheva endpoint value to compare. The AK(3) unequal-scalar locus is empty
because its complete structure base is empty. This exhausts only
\(2\mathbf1\oplus L_3\) in \(\operatorname{Ver}_7^+\); it does not establish
an Andrews--Curtis counterexample or a broader categorical collapse.
