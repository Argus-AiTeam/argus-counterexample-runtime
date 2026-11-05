---
title: Minimal Hopf-object boundary in Ver_4^+
description: Empty normalized cocommutative Hopf scheme and exact scalar identity on 1+P.
---

# Minimal Hopf-object boundary in \(\operatorname{Ver}_4^+\)

Over an algebraically closed field of characteristic two,
\[
\operatorname{Ver}_4^+
=\operatorname{Rep}(k[d]/d^2,R=1\otimes1+d\otimes d).
\]
The indecomposable projective is \(P=k[d]/d^2\).  The carrier \(P\)
alone cannot be unital and counital because
\(\ker d=\operatorname{im}d\), so every \(d\)-linear unit is killed by
every \(d\)-linear counit.  Thus \(\mathbf1\oplus P\) is the minimal
carrier containing the higher projective direction.

For \(H=\mathbf1\oplus P\), every unit and counit admit a lossless
canonical gauge.  In a basis \(1,x,y\) with \(dx=y\), they are
\(\eta(1)=1\), \(\epsilon(1)=1\), and
\(\epsilon(x)=\epsilon(y)=0\).  Every \(d\)-linear counital product and
braided-cocommutative coproduct then has the form
\[
\begin{array}{ll}
x^2=(e+g)x+by,&xy=cx+ey,\\
yx=cx+gy,&y^2=cy,
\end{array}
\]
and
\[
\Delta x=1\otimes x+x\otimes1+
p(x\otimes y+y\otimes x)+q\,y\otimes y,\qquad
\Delta y=1\otimes y+y\otimes1.
\]

The coefficient of \(x\otimes y\otimes y\) in the coassociator of
\(x\) is \(p^2\).  The coefficient of \(x\otimes y\) in braided
bialgebra compatibility on \(x\otimes y\) is \(cp+1\).  These equations
generate the unit ideal in characteristic two:
\[
1=(cp+1)^2+c^2p^2.
\]
Hence \(H\) has no unital counital cocommutative bialgebra structure and
therefore no normalized unimodular cocommutative Hopf structure.  This
is an empty structure scheme over every commutative characteristic-two
base, not finite-field point enumeration.

There is also an independent scalar boundary.  Streamed
left-associated contraction and complete-placement right-associated
contraction both give, identically,
\[
\Omega_{\operatorname{AK}(3)}
=\Omega_{\mathrm{standard}}=u^2w^2,
\]
where \(L=u1+vy\) and \(\ell(1)=w\).  Normalization gives \(uw=1\), so
both formal scalars reduce to one.  Thus the unequal locus is empty
both because the Hopf scheme is empty and because its defining
difference polynomial is zero.

The replayable proof, full axiom system, Singular certificates, and
typed Jacobian record are in
`research/experiments/ver4plus-minimal-hopf/`.  This closes only
\(\mathbf1\oplus P\) in \(\operatorname{Ver}_4^+\); it says nothing
about larger higher-Verlinde carriers and does not settle the
Andrews--Curtis conjecture.
