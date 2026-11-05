---
title: Exact Karlsson MUB triple
description: Degree-eight algebraic witness for a full non-Fourier, non-Tao MUB triple in dimension six.
---

# Exact Karlsson MUB triple

There is an exact order-six MUB triple whose Hadamard anchor belongs to
Karlsson's H2-reducible family but is monomially equivalent to neither the
two-parameter Fourier family (including its transpose) nor Tao's matrix.

Let \(\alpha\) be the root with negative imaginary part of

\[
x^8-6x^7+16x^6-24x^5+27x^4-24x^3+16x^2-6x+1
\]

for which \(\alpha+\alpha^{-1}\) lies in

\[
\left(
-\frac{350527140862341144237}{1181697165526292162857},
-\frac{2622249731937520232}{8840128806886223725}
\right).
\]

The trace interval lies strictly inside \((-2,2)\), so this embedding has
\(\overline{\alpha}=\alpha^{-1}\). All Karlsson and vector phases are explicit
rational polynomials in \(\alpha\), recorded in
`research/classification_search/ramification_continuation/exact_algebraic_triangle_certificate.json`.

Exact reduction modulo the irreducible polynomial verifies:

- all 36 anchor entries have modulus one and its 36 Gram entries form \(6I\);
- all 36 entries of the completed character basis have modulus one and its
  complete 36-entry Gram matrix is \(6I\);
- all 36 anchor-basis squared overlaps equal 6;
- all four Karlsson Möbius relations hold.

For the coordinate order

\[
((1,1),(0,0),(0,1),(1,0),(1,2),(0,2))\subset C_2\times C_3,
\]

let \(S(x,y)=(-1)^x\), \(P(x,y)=\omega^y\), and let \(D\) be the diagonal
formed from the exact base vector. The original three C10 vectors are exactly
\(D\{1,S,P\}\). Their orthogonal complement is
\(D\operatorname{span}\{P^2,SP,SP^2\}\).

For

\[
f=D(aP^2+bSP+cSP^2),
\]

the five nontrivial Fourier autocorrelations are

\[
a\bar c+\bar a c,\quad \bar b c,\quad b\bar c,\quad
a\bar b,\quad \bar a b.
\]

Thus every flat complement vector is either the isolated \(D\,SP\) orbit or,
up to global phase, the one-parameter family

\[
D\left(\frac{q+q^{-1}}2P^2+
       \frac{q-q^{-1}}2SP^2\right),\qquad |q|=1.
\]

The isolated vector is exactly unbiased to the anchor. Two family vectors are
orthogonal only at parameters \(q\) and \(\pm iq\); their paired anchor
equations reduce in every column to \(q^4=1\). Taking \(q=1\) gives the two
missing characters \(P^2\) and \(SP^2\). Hence
\(D\{1,S,P,P^2,SP,SP^2\}\) is the third full basis.

After normalization by \(1/\sqrt6\), the standard basis, the columns of the
anchor, and this character basis are pairwise mutually unbiased orthonormal
bases. Arb isolation of the same algebraic embedding and an exhaustive
\(720^2\cdot2\) dephased monomial search give a positive Fourier-family
maximum-entry error lower bound. The exact Haagerup cross ratio \(-1\)
excludes Tao's cube-root equivalence class.

The rerunnable completion is
`research/classification_search/ramification_continuation/certify_c10_character_complement.py`,
with certificate
`research/classification_search/ramification_continuation/c10_character_complement_certificate.json`.
It proves C11, an exact MUB triple. It does not supply a fourth basis and does
not prove the campaign objective.
