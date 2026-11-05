# AK(3) exact \(n=2\) four-column \(S_3\)-lift boundary

## Corrected result

For

\[
G=((1,2),(1,3)),\qquad H=((0,1),(1,1)),\qquad L=I,
\]

no point of the complete unrestricted \(S_2\) Laurent fiber lifts the
alternating depth-two cell to \(S_3=F/F'''\), in any of the four
ordered component patterns.  This is an exact first-relative-grade
nonmembership theorem for this cell, not an Andrews--Curtis
counterexample and not an exclusion of other integral triples or
longer paths.

## Four-column correction

The earlier triangular calculation omitted the two terminal
\(F''/F'''\) columns.  Both are nonzero: the legal terminal cycle
\([c,c^a]\) changes the old \(\rho_2,\rho_3\) expressions.  The old
two-column certificate is therefore invalidated as a proof, although
its audit artifacts remain available.  The corrected calculation
uses both internal and both terminal slots throughout.

Let

\[
R=\mathbb Z[X^{\pm1},Y^{\pm1}],\qquad
\Lambda=R[U^{\pm1},V^{\pm1}],
\]

with \(\sigma(U,V)=(X/U,Y/V)\), and put
\(A^-=\ker(1+\sigma)\).  Exact finite \(F''\) words realize

\[
A^-=\operatorname{im}(1-\sigma).
\]

After removing the endpoint factors, the full \(2\times4\) operator
has image

\[
(X-1,Y-1)(A^-)^2
\]

in every component pattern.  This normal form includes all four
copies of the actual relation-cycle module.  Terminal axis powers
only multiply the endpoint rows by outer Laurent units and do not
change the resulting cokernel.

## Full-fiber norm obstruction

The reviewed \(S_2\) fiber may be written

\[
f=A^2+(B-1)h
\]

with arbitrary finite integral Laurent \(h\); the independent
\(K(A^{-1})\) and mixed \(q\) directions remain unrestricted in the
second conjugator.

After setting \(X=Y=1\) in the four-column cokernel, all four patterns
have the same second residual

\[
\Phi_2(h)=C+L^*h-h^*L+D h^*h,
\qquad r^*=r(U^{-1},V^{-1}).
\]

Here

\[
D=U^{-1}V^{-3}(V-1)(UV^2-1)(UV^3-1),
\]

and the complete sparse \(C,L\) are recorded in the exact
certificate.  Setting \(z=L-Dh\) gives

\[
z^*z=N-D\Phi_2(h),\qquad N=L^*L+DC.
\]

The Laurent polynomial \(N\) is irreducible.  After multiplication by
the unit \(-U^3V^5\) and specialization \(V=-2\), it becomes

\[
90U^6-606U^5-723U^4+2579U^3-1590U^2+444U-720.
\]

Its primitive mod-seven reduction passes the exact degree-six Rabin
test.  The multivariate polynomial has coefficient gcd one in
\(\mathbb Q[V]\), and specialization preserves its \(U\)-degree, so
the univariate irreducibility proves multivariate irreducibility.

If \(\Phi_2(h)=0\), then \(N=z^*z\), contradicting irreducibility:
a nonunit \(z\) gives a proper factorization, while a Laurent unit has
norm one.  Thus \(\Phi_2(h)\ne0\) for every finite \(h\), excluding
the complete four-column image in all four patterns.

The proof and replay are in
[`BOUNDARY.md`](../../../../../research/experiments/ak3-n2-four-column-lift/BOUNDARY.md),
`four_column_probe.py`, and `norm_obstruction.py`.
