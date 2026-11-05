---
title: AK(3) exact n=3 four-column S3-lift boundary
description: Original-word reconstruction of the complete four-column relation-module image and an arbitrary-support irreducible-norm obstruction for the G3 Laurent fiber.
---

# AK(3) exact \(n=3\) four-column \(S_3\)-lift boundary

For

\[
G_3=((1,3),(1,4)),\qquad H=((0,1),(1,1)),\qquad L=I,
\]

no point of the complete unrestricted \(S_2\) Laurent fiber lifts the
alternating depth-two cell to \(S_3=F/F'''\), in any of the four
ordered component patterns.  This is an exact first-relative-grade
nonmembership theorem for one orbit, not an Andrews--Curtis
counterexample and not an exclusion of \(G_n\) for \(n\ne3\).

## Complete four-column image

The reconstruction starts from the original AK(3) words and the
automorphism chain with successive exponent bases \(G_3,H,I\).  It
retains both internal and both terminal \(F''/F'''\) correction slots.

Let

\[
R=\mathbb Z[X^{\pm1},Y^{\pm1}],\qquad
\Lambda=R[U^{\pm1},V^{\pm1}],
\]

with \(\sigma(U,V)=(X/U,Y/V)\), and put
\(A^-=\ker(1+\sigma)=\operatorname{im}(1-\sigma)\).  Finite free
words realize every scalar in \(A^-\).

After removing the endpoint factors, the complete \(2\times4\)
operator has image

\[
(X-1,Y-1)(A^-)^2
\]

in every component pattern.  Both terminal columns are nonzero, and
terminal axis powers only translate endpoint errors by outer Laurent
units.  The cokernel is therefore obtained by setting \(X=Y=1\), with
involution \(t^*=t(U^{-1},V^{-1})\).

## Full-fiber norm obstruction

The reviewed fiber can be written

\[
f=A^2+(B-1)h
\]

with arbitrary finite integral Laurent \(h\); the independent
\(K(A^{-1})\) and mixed \(q\) directions remain unrestricted in the
second conjugator.  Exact relative-grade collection gives the same
second cokernel coordinate in all four patterns:

\[
\Phi_3(h)=C+M^*h-h^*M+D h^*h,
\]

where

\[
D=U^{-1}V^{-4}(V-1)(UV^3-1)(UV^4-1).
\]

The complete sparse \(C,M\) are recorded in the exact certificate.
With

\[
z=M-Dh,\qquad N=M^*M+DC,
\]

one has

\[
z^*z=N-D\Phi_3(h).
\]

The cleared polynomial \(U^3V^6N\) has 51 terms, bidegree
\((6,12)\), and coefficient gcd one in \(\mathbb Q[V]\).  At
\(V=-2\), it becomes

\[
-396U^6+2436U^5+3555U^4-7955U^3
+5958U^2+1092U-1584.
\]

Its monic reduction modulo 31 passes the exact degree-six Rabin test.
Specialization preserves the \(U\)-degree, while the coefficient-gcd
calculation excludes a factor in \(\mathbb Q[V]\); hence \(N\) is
irreducible as a Laurent polynomial.

If \(\Phi_3(h)=0\), then \(N=z^*z\).  A nonunit \(z\) would factor the
irreducible \(N\), while a Laurent unit has norm one.  Thus
\(\Phi_3(h)\ne0\) for every finite \(h\), excluding the complete
four-column image.

The proof and replay are in
[`BOUNDARY.md`](../../../../../research/experiments/ak3-n3-four-column-lift/BOUNDARY.md),
`four_column_probe.py`, and `norm_obstruction.py`.
