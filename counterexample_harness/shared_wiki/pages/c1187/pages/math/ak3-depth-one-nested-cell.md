---
title: AK(3) depth-one nested Nielsen--AC3 boundary
description: Exact discriminant-five obstruction to every single internal AC3 between arbitrary Nielsen blocks.
---

# AK(3) depth-one nested Nielsen--AC3 boundary

For the reviewed normalized AK(3) pair \((P,Q)\), consider arbitrary
\(\Phi,\Psi,\Theta\in\operatorname{Aut}(F_2)\), either internal
component, and arbitrary conjugators in

\[
(P,Q)\xrightarrow{\Phi}X\xrightarrow{C_i(h)}Y
\xrightarrow{\Psi}Z\xrightarrow{C_1(u)C_2(v)}
\Theta(a,b)\xrightarrow{\Theta^{-1}}(a,b).
\]

This entire family is empty in the free metabelian quotient
\(S_2=F/F''\), with no Nielsen-word, matrix-entry, conjugator-length, or
Laurent-support cutoff.

## Exact reduction

Writing \(G_1,G_2\) for the abelianization basis selected by \(\Phi\),
the monomial part of the internal conjugator is removed exactly: powers
of the conjugated component centralize it, while the transverse power
is a common conjugation that propagates through \(\Psi\) and is absorbed
by the terminal conjugators. Every remaining metabelian conjugator has
Fox row

\[
f(1-B,A-1),\qquad
f\in\mathbb Z[A^{\pm1},B^{\pm1}].
\]

Keeping the full Fox matrices of all three automorphisms until their
Laurent-unit determinants cancel avoids any
\(\operatorname{IA}_2\) kernel ambiguity. For either internal
component, the normalized relative determinant is exactly

\[
D=\Delta+(G_1-1)(G_2-1)f,
\]

where

\[
\Delta=-AB^{-1}+A-A^2B^{-1}+A^3B^{-4}
+A^3B^{-3}+A^3B^{-2}-A^4B^{-4}.
\]

## Universal incompatibility

Let the terminal basis have rows
\(\ell_j=(m_j,n_j)\), and write its coordinates in the internal basis
as \((r_j,s_j)\). Exact metabelian conjugacy of the two terminal
components is equivalent to both specializations of \(D\) being
positive Laurent monomials.

The centered second logarithmic derivative of \(\Delta\) in direction
\((m,n)\) is twice

\[
q(m,n)=m^2-mn-n^2.
\]

The two terminal equations therefore force one common integer
\(\lambda=f(1,1)\) with

\[
q(\ell_j)=\lambda r_js_j,\qquad j=1,2.
\]

In a unimodular terminal basis, \(q\) has discriminant \(5\). In a
unimodular internal coordinate basis, the product form \(rs\) has
discriminant \(1\). If \(b,d\) are their cross coefficients, the two
equations imply

\[
b^2-5=\lambda^2(d^2-1).
\]

Both \(b\) and \(d\) are odd. The left side is \(4\pmod8\), while the
right side is \(0\pmod8\), a contradiction. Axis cases would require
\(q(m,n)=0\), which has no nonzero integral solution.

The exact replay is in
`research/experiments/ak3-depth-one-nested-cell/`. The result requires
any surviving elementary path to contain at least two genuinely
internal AC3 stages. It is not an Andrews--Curtis counterexample.
