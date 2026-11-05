---
title: AK(3) global Nielsen-sandwich boundary
description: Exact all-Aut(F2) metabelian obstruction obtained from primitive one-parameter specializations of the Fox determinant.
---

Let \((P,Q)\) be the pair obtained from the AK(3) relators by the
reviewed five signed AC2 normalizations. Its abelianization is the
standard basis, and its abelian Fox determinant is

\[
\Delta=-AB^{-1}+A-A^2B^{-1}
 +A^3B^{-4}+A^3B^{-3}+A^3B^{-2}-A^4B^{-4}.
\]

For any primitive word \(W\) with exponent vector \((m,n)\), exact
Magnus conjugacy and the Fox chain rule imply the necessary condition

\[
W(P,Q)\sim W(a,b)\text{ in }S_2
\quad\Longrightarrow\quad
\Delta(T^{-n},T^m)=T^k
\]

for some integer \(k\). The sign is positive because the abelianization
of a conjugator is a group monomial.

This condition fails for every primitive vector. Outside a direction
parallel to a difference of two support points of \(\Delta\), all seven
projected exponents are distinct. The 21 support-point differences give
only eight primitive directions up to sign:

\[
(0,1),(1,0),(1,-1),(1,-2),(1,-3),(2,-1),(2,-3),(3,-4).
\]

Exact aggregation leaves at least two nonzero Laurent terms in every
case; reversing a direction only sends \(T\) to \(T^{-1}\). Thus

\[
W(P,Q)\not\sim W(a,b)
\]

for every primitive \(W\).

Each component of every finite signed Nielsen automorphism has a
primitive exponent vector. Consequently no
\(\Phi\in\operatorname{Aut}(F_2)\) makes both
\(\Phi_i(P,Q)\) conjugate to \(\Phi_i(a,b)\) in \(S_2\); in fact each
component already fails separately. Projection gives the same
obstruction in every \(S_d\), \(d\geq2\).

This exhausts one global Nielsen transformation followed by
componentwise AC3 moves and the inverse transformation. It does not
cover genuinely nested paths with repeated Nielsen--AC3 interleaving,
and it does not establish an Andrews--Curtis counterexample.
