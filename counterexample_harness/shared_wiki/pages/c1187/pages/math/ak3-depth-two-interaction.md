---
title: AK(3) alternating-depth-two interaction boundary
description: Complete metabelian two-update law, genuine S2 solution fibers, and a fixed-basis S3 lift obstruction.
---

# AK(3) alternating-depth-two interaction boundary

For the reviewed normalized AK(3) pair, two genuinely internal AC3
stages separated by arbitrary signed Nielsen automorphisms have exact
normalized \(S_2\) determinant

\[
D=\Delta+(G_1-1)(G_2-1)f+(H_1-1)(H_2-1)g,
\qquad f,g\in\mathbb Z[A^{\pm1},B^{\pm1}].
\]

This formula retains the full Fox matrices, all inner-automorphism
factors, both arbitrary conjugators, and all four ordered component
choices.  The matrix update has no artificial \(fg\) term; the genuine
new freedom is the sum of two independently transported binomial
products.

The two stages collapse exactly to the reviewed depth-one family iff
the unordered primitive row directions of \(G\) and \(H\) agree up to
signs, equivalently iff \(H\) is a signed permutation of \(G\).  This
follows from unique factorization of the two primitive Laurent
binomials.  Every nonassociate pair is the genuine two-direction
stratum.

## The depth-one obstruction disappears

With terminal basis \(L=I\), take

\[
G=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad
H=\begin{pmatrix}1&-1\\2&-1\end{pmatrix},
\]

\[
f=A^2-A-1,\qquad g=B^3+B^2-1.
\]

Both exact terminal specializations are \(T^{-3}\).  Actual free
Nielsen automorphisms realize these three bases, and explicit products
of monomial conjugates of \([a,b]\) realize both Laurent parameters.
All other free automorphism lifts of the same matrices differ by inner
factors, whose common conjugations are absorbed exactly into the
adjacent arbitrary conjugators.
For every internal component pattern, both terminal Magnus equations
are divided exactly and converted to explicit terminal conjugators.
Thus this is a genuine path in \(S_2\), not a determinant or moment
candidate.

The first two logarithmic moments force every solution with these
bases to have

\[
k_1=k_2=-3,\qquad f(1,1)=-1,\qquad g(1,1)=1.
\]

Adding arbitrary multiples of \((A-1)(B-1)\) to either parameter
already gives an unbounded-support solution family.

## The complete fixed-basis fiber fails at \(S_3\)

Reduce the next Magnus relation module modulo three over the Heisenberg
group

\[
H_3=\langle\alpha,\beta,\kappa\mid
\alpha^3=\beta^3=\kappa^3=1,\ 
\kappa\text{ central},\
\alpha\beta=\kappa\beta\alpha\rangle.
\]

For \(C=\mathbb F_3[H_3]\), the kernel of

\[
C^2\longrightarrow C,\qquad
(x,y)\longmapsto x(\alpha-1)+y(\beta-1)
\]

has dimension \(28\).  Allowing this whole kernel independently for
both internal and both terminal conjugators enlarges every possible
\(F''\) lift change.  The terminal centralizers are exactly
\(\langle\alpha,\kappa\rangle\) and
\(\langle\beta,\kappa\rangle\), so their \(3^4\) paired coordinates
are exhaustive.

For all four internal component patterns and all 81 terminal
coordinates, the enlarged response matrix has rank \(45\); adjoining
the endpoint error raises the rank to \(46\).  Sparse left-kernel
witnesses certify every inconsistency.  Since all fixed-basis
\(S_2\) solutions have the same Heisenberg top data, this excludes the
entire fixed-basis solution fiber in \(S_3\), not only the displayed
free representatives.

Other nonassociate triples \(G,H,L\) are not covered.  The complete
alternating-depth-two family, an all-derived path, and the standard
Andrews--Curtis conjecture all remain open.

The global per-top affine-hull replacement in the same finite Magnus
quotient is too coarse: the start and target Nielsen hulls have
dimension 48 over each of 432 top states, while one internal AC3 raises
the start hulls to dimension 55 and makes all 432 intersect the target
hulls.  These are enlarged affine intersections, not paths.  In
particular they cannot replace the fixed-basis rank certificate or
support any AC-triviality claim.
