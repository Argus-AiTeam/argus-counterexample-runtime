---
title: D81 cancellation-strip transition kernel
description: Exact Euclidean fibers give a cutoff-free pointwise successor, and a finite anchor-affine partition completely classifies the h=21 level-zero source domain.
---

For fixed \(h=21\) and level \(j\), let
\[
m_j=(\mu_{1,j},\mu_{2,j}),\qquad
n_j=(\nu_{1,j},\nu_{2,j})
\]
be the incoming and outgoing quotient rows.  If
\[
g_j=\gcd(|\mu_{1,j}|,|\mu_{2,j}|),\quad
m'_j=m_j/g_j,\quad m'_j\cdot e_j=1,\quad
k_j=(m'_{2,j},-m'_{1,j}),
\]
then every integer column has unique coordinates
\[
c=\sigma e_j+qk_j.
\]
Primitivity is exactly \(\gcd(\sigma,q)=1\), the physical incoming tail
is \(s=g_j\sigma\), and
\[
\beta=(n_j\cdot e_j)\sigma+(n_j\cdot k_j)q.
\]
The exact beta bound therefore gives a sign-correct integer interval for
\(q\).  This affine-fiber parameterization includes every nonconvergent
strip point; continued-fraction convergents and semiconvergents are only
distinguished boundary records.

At \(j=0\), the beta step is
\[
D=9624333135714003390997
\]
and the full beta-window width is
\[
2M=86264932325536585776<D.
\]
Consequently each
\(0\le\sigma\le5312538103\) has at most one beta-bounded fiber,
\[
q_*(\sigma)=\operatorname{nearestInteger}
\left(-\frac{A\sigma}{D}\right),\qquad
A=-3106646497415492117680.
\]
The old two-shear cells are exactly the two anchor-coordinate lines
\((p,q)=(1,v)\) and \((v,1)\); they are not the complete fiber family.

A valid full source state retains the fiber, orientation, canonical
Bezout shear, derived shear interval, shared normalization carry, order
cosets, and exact incoming and outgoing coordinates.  It reconstructs
one normalized saturated basis.  Exact Jacobi--Perron replay then tests
the target before strict crossing under the proved three-steps-per-halving
bound.  On equality, complete incoming reverse peeling and complete
equality-aware \(W_j\) peeling are applied.  If both accept, the terminal
basis gives the unique successor by
\[
B_{j+1}=t_j^{-2h}T_j.
\]
Thus no independent target-level primitive column remains.

The complete \(h=21,j=0\) domain is also finitely parameterized in the
unimodular anchor
\[
E=\begin{pmatrix}-7283&525\\652&-47\end{pmatrix}.
\]
For a primitive first column \((u,v)\), put
\[
s=402561u+1172998v,\qquad
\beta=8006820250944691u-577177111037539v.
\]
The exact first-column polygon is
\[
0\le s\le F_0,\qquad |\beta|\le2F_1,\qquad \gcd(u,v)=1.
\]
It contains 47,617,404 lattice points and 28,947,904 primitive points.
An independent exact floor-sum count reproduces the first number, and
Möbius inversion reproduces the second; the inversion ends at \(d=5386\)
because the scaled polygon at \(d=5387\) contains only the origin.
If \(au+bv=1\), every oriented completion is uniquely
\[
(x,y)=(-\delta b,\delta a)+k(u,v),
\]
where the complete derived interval for \(k\) is exactly
\[
s\le t\le F_0,\qquad |\gamma|\le2F_1-|\beta|.
\]
This finite affine-fiber partition covers every non-semiconvergent source;
it is not a continued-fraction boundary approximation.

The 79 continued-fraction boundary records contain 73,766 derived shears.
The Python kernel explicitly records every shear: 21,093 fail a named
source gate and 52,673 cross strictly, with no target equality.  The full
affine classifier uses the same canonical shear, normalization carries,
shared carry, conductor cosets, source gates, and target-first orbit.
All algebraic signs and digit floors are certified by integer evaluation
on a rational isolating interval, refined whenever needed, and the orbit
ends under the theorem-derived 195-step bound.  An independent
cross-implementation check matches all 9,056 records in the complete
\(u=0\) slice, including every crossing step and carry extremum.

Across the complete affine domain there are 40,130,215 derived shears.
Exactly 15,756,640 fail \(t\le\rho\), 7,177,328 fail the outgoing
\(L^1\) gate, and the remaining 17,196,247 pass every source gate.
Every passing source crosses strictly at a step from 13 through 64; there
are zero target equalities and zero unresolved records.  Therefore no
\(W\) matrix or \(j=1\) successor is formed.

The resulting aggregate classification closes the fixed
\(h=21,j=0\to1\) source domain.  It has not produced a recursively closed
accepting component, a uniform all-\(h\) descent rank, or a counterexample.

The earlier reviewed paired-state successor changes the height
\(h\mapsto h+1\) while holding a basis fixed.  This kernel instead handles
the actual fixed-\(h\) level change \(j\mapsto j+1\), where the middle row
changes and a successor exists only after target equality.

Jacobian operation `lattice.dual.compute` was run on the level-zero
quotient rows.  Its typed `dual_basis` fails the contract's integral
row-pairing postcondition, so the output is retained but is not used as
mathematical evidence.
