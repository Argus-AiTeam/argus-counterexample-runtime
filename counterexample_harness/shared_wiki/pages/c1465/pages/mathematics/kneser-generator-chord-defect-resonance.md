---
title: Kneser generator-chord defect resonance boundary
description: Exact scalar normal form and uniform finite-turn boundary for the frozen generator-chord family.
---

# Kneser generator-chord defect resonance boundary

For the normalized Kneser Abel function \(A\), define
\[
E(x)=A(\log(1/A'(x)))-A(x)+1.
\]
The frozen family is
\[
A(y)-A(x)=h,\qquad
A(y)-A(y-x)=\lambda E(x),\qquad 0<h<1.
\]
The bound does not require a sign restriction on \(E(x)\); a
positive-defect guard is only a subfamily.

With \(T=A^{-1}\), \(p=T'\), and \(s=A(x)\), it has the exact scalar
normal form
\[
R_h(s)=
\frac{s+h-A(T(s+h)-T(s))}
     {A(p(s))-s}
=\lambda.
\]
The full two-equation Jacobian is nonzero exactly when \(R_h'(s)\ne0\).

The route theorem gives one parameter-uniform bound
\[
N=N_{\mathrm{mid}}+4
\]
for connected components and
\[
M=M_{\mathrm{mid}}+4
\]
for total analytic multiplicity.  The lower tail, compact middle, and upper
tail may all contain roots of the same fiber, so their multiplicities add:
\(2+M_{\mathrm{mid}}+2\).  Each noncompact tail has at most one critical
point, hence at most two roots of one level.  One compact projective
restricted-analytic family supplies \(N_{\mathrm{mid}}\) and
\(M_{\mathrm{mid}}\).

The two decisive coupled faces are:

- At \(s\downarrow-2\) and \(h\downarrow0\), the logarithmic chart
  \(T(-2+\alpha)=\log B(\alpha)\) reduces the critical equation to a
  single monotone transition in
  \(z=d/[A'(q)/(A(q)+3)]\).
- At \(s\to+\infty\) and \(h\downarrow0\), every possible critical
  sequence enters the superflat layer
  \(Z\to-\infty\), where
  \((\log R_h)''/[p(s-1)q'(s-1)]\to-1\).

This boundary applies only to this literal family.  It does not settle
the existence of another fixed Kneser formula with unbounded fibers or
the unrestricted o-minimality question.
