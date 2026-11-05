---
title: Endpoint-notch critical scaling collapse
description: Every normalized endpoint-notch blow-up in the full preregistered scale interval converges to the horizontal Euclidean quotient.
---

# Endpoint-notch critical scaling collapse

For the frozen endpoint-notch family, normalize at any real scales
\(1\leq t_m\leq R_m^2\):
\[
d_m(g,h)=
\frac{\rho_m(\delta_{\sqrt{t_m}}g,\delta_{\sqrt{t_m}}h)}
     {\sqrt{H_m(t_m)}}.
\]
Let \(\alpha=1/m\), \(\beta=1/(m+1)\),
\(\Delta=\alpha-\beta\), and
\[
y=(R_m^{-2}t_m)^{\Delta/2}\in[2^{-1/2},1].
\]
The exact Mellin formula is a three-point finite difference.  Its singular
horizontal coefficient \(S_{\alpha,y}\) satisfies
\[
\alpha S_{\alpha,y}
=(1+\alpha)\left(y-\frac2{2+\alpha}\right)^2
+\frac{\alpha^2}{(2+\alpha)^2}
\]
and therefore
\[
S_{\alpha,y}\geq
\frac2{25}\left(\frac{(1-y)^2}{\alpha}+\alpha\right).
\]
After removing this pole, the complete gamma-power expression has a
uniformly \(C^1\) remainder.  Its same finite difference is
\(O(\alpha S_{\alpha,y})\), uniformly over the entire scale interval.
Hence
\[
d_m(g,h)\longrightarrow
\sqrt{u(g^{-1}h)^2+v(g^{-1}h)^2}
\]
locally uniformly, with no subsequence parameter left.

The limit is degenerate exactly on central cosets.  Its metric quotient is
\(\mathbb H/Z(\mathbb H)\cong\mathbb R^2\), where it embeds isometrically
and has doubling constant at most \(25\).  Thus no nonhomogeneous
logarithmic or nondegenerate Heisenberg limit survives at any
preregistered scale.

**Scope.** This classifies and retires the complete normalized blow-up
mechanism for the frozen endpoint-notch metrics.  It does not provide a
uniform finite-dimensional embedding of the original finite word-ball
blocks and does not settle the project counterexample objective.

