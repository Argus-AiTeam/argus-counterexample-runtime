---
title: AK(3) depth-two orbit and first-lift survivor boundary
description: Complete integral orbit key and S2 fiber criterion, an infinite inequivalent S2 family, and the failure of the fixed-basis S3 rank defect to persist orbitwise.
---

# AK(3) depth-two orbit and first-lift survivor boundary

Let \(B_2\) be the signed permutation subgroup of
\(\mathrm{GL}_2(\mathbb Z)\).  Under simultaneous coordinate changes
and independent signed row operations,

\[
(G,H,L)\mapsto(PGC,QHC,RLC).
\]

Normalizing \(L\) gives

\[
(X,Y)=(GL^{-1},HL^{-1}),\qquad
(X,Y)\sim(PXR^{-1},QYR^{-1}).
\]

The lexicographically least of these \(8^3\) transforms is a complete
integral orbit key.  Equivalently, the block Gram matrix formed from
\(XX^t,XY^t,YX^t,YY^t\), modulo independent signed row actions, is
complete.  The stabilizer is

\[
B_2\cap X^{-1}B_2X\cap Y^{-1}B_2Y.
\]

The integral orbit set is infinite; the finite key computation does
not turn it into a finite classification.

## Exact solvability of an orbit in \(S_2\)

Write

\[
GL^{-1}=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
HL^{-1}=\begin{pmatrix}r&s\\u&v\end{pmatrix}.
\]

After restricting the reviewed depth-two determinant to the two
terminal axes, exact solvability is equivalent to

\[
\begin{aligned}
(T^b-1)(T^d-1)F_1+(T^s-1)(T^v-1)K_1&=E_1,\\
(T^{-a}-1)(T^{-c}-1)F_2
 +(T^{-r}-1)(T^{-u}-1)K_2&=E_2,
\end{aligned}
\]

together with

\[
F_1(1)=F_2(1),\qquad K_1(1)=K_2(1).
\]

Here each \(E_j\) is the target terminal monomial minus the
corresponding specialization of the normalized AK(3) determinant.
These are exact Laurent ideal-membership equations.  Their complete
solution sets, followed by arbitrary multiples of
\((X-1)(Y-1)\), parameterize every global Laurent solution; there is
no support cutoff.

## An infinite inequivalent exact \(S_2\) family

For every \(n\geq2\),

\[
G_n=\begin{pmatrix}1&n\\1&n+1\end{pmatrix},\qquad
H=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad L=I
\]

is nonassociate and has stabilizer \(\{\pm I\}\).  The invariant
multiset \(\{1,1,n,n+1\}\) of absolute \(G_n\)-entries makes these
orbits pairwise inequivalent.

With \(U_m(T)=1+\cdots+T^{m-1}\), one exact seed is

\[
f=A^2,\qquad g=-B^{-2}-U_n(B)U_{n+1}(B).
\]

The complete fiber is

\[
\begin{aligned}
f={}&F(B)+A^2-1+(A-1)(B-1)p,\\
g={}&-B^{-2}-U_n(B)U_{n+1}(B)F(B)
 +K(A^{-1})-\mu_n+(A-1)(B-1)q,
\end{aligned}
\]

where \(F(1)=1\), \(K(1)=\mu_n=-1-n(n+1)\), and \(p,q\) are arbitrary
Laurent polynomials.  Explicit free automorphisms, internal
commutator products, and both terminal conjugators realize all four
component patterns.

## The first-lift defect is not orbit-global

For \(n=2\), the complete mod-three Heisenberg response rank is 48.
Each component pattern has 9 consistent systems among its 81 exact
terminal coordinates.  The other 72 systems have augmented rank 49.
The complete system is exactly periodic under \(n\mapsto n+9\), so
all nine residue classes have the same survivor count.

The actual image of \(F''\) in the 28-dimensional Heisenberg relation
kernel has dimension 16.  Explicit translates of
\([c,c^a]\) and \([c,c^b]\), with \(c=[a,b]\), realize tested
survivors after an exact \(S_2\)-fiber shift.  Thus the survivors are
not created solely by enlarging this 16-dimensional image to the full
kernel.

The displayed words still have nonzero exact Fox residual over
\(\mathbb Z[S_2]\), so they are not \(S_3\) paths.  Complete
class-two tests in characteristics 2, 3, and 5, a class-three
order-32 metabelian top group, and a noncentral dihedral metabelian
top group also retain linear survivors.  These are necessary quotient
systems, not path certificates.

The stable boundary is therefore:

* the fixed-basis rank-\(45\) versus rank-\(46\) defect is not an
  invariant of the full triple orbit;
* an infinite family of pairwise inequivalent exact \(S_2\) paths has
  genuine first-lift candidates;
* the exact system over
  \(\ker(\mathbb Z[S_2]^2\to\mathbb Z[S_2])\cong F''/F'''\) remains
  unresolved;
* no exact \(S_3\), free, or all-derived path and no
  Andrews--Curtis counterexample is known from this route.

