---
title: Balanced PBW leading-term collapse
description: All-presentation reduction of top-supported filtered Hopf scalars to their bicommutative associated graded.
---

# Balanced PBW leading-term collapse

Let \(H\) be a finite normalized unimodular cocommutative Hopf object with
an exhaustive filtration
\[
0=F_{-1}H\subset F_0H\subset\cdots\subset F_NH=H.
\]
Assume the associated-graded functor is strong symmetric monoidal, all Hopf
maps preserve total filtration, the cointegral \(l\) annihilates
\(F_{N-1}H\), and the leading integral
\(\ell\in\operatorname{gr}_NH\) pairs to one with the induced top
cointegral.

For a closed balanced presentation with \(n\) generators and \(n\)
relators, Bobtcheva's literal occurrence morphism
\[
C_P(H):H^{\otimes n}\longrightarrow H^{\otimes n}
\]
is filtered of degree zero.  The inserted integrals have maximum total
degree \(nN\), while \(l^{\otimes n}\) annihilates every output of total
degree below \(nN\).  Therefore the complete contraction factors through
the single top quotient:
\[
\overline\Omega_H(P)
=\overline\Omega_{\operatorname{gr}H}(P).
\]
This is a morphism-level filtration argument.  It does not use
representative coordinate degree or a finite set of presentations.

If \(\operatorname{gr}H\) is also commutative, commutativity and
cocommutativity turn the written word diagram into the integer matrix
morphism \(\Phi_E\), where \(E\) is the relator exponent-sum matrix.
Coordinate permutations, inversions, and integral shears all fix
\(\ell^{\otimes n}\).  Since these operations generate
\(\operatorname{GL}_n(\mathbb Z)\),
\[
E\in\operatorname{GL}_n(\mathbb Z)
\quad\Longrightarrow\quad
\overline\Omega_H(P)=1.
\]
Every balanced trivial-group presentation has a unimodular exponent matrix,
because its abelianization is trivial.

The reviewed instances satisfying these hypotheses are:

| Object | Top degree | Associated graded |
|---|---:|---|
| Restricted Heisenberg over \(\mathbb F_2\) | 3 | \(\mathbb F_2[x,y,z]/(x^2,y^2,z^2)\) |
| Odd-prime super-Heisenberg | \(p+1\) | \(\Lambda(x,y)\otimes\mathbb F_p[z]/(z^p)\) |
| \(S(L_3)\) in \(\operatorname{Ver}_7^+\) | 4 | itself |
| \(U(L_3)\) in \(\operatorname{Ver}_7^+\) | 4 | \(S(L_3)\) |
| Both \(U_t(L_3\oplus L_5)\) forms | 6 | \(S(L_3)\otimes S(L_5)\) |

The exact operation-table replay is
`research/experiments/pbw-balanced-leading-term-collapse/certificate.json`,
and the complete proof is its adjacent `THEOREM.md`.

This result eliminates Bobtcheva's scalar as a separator throughout the
stated filtered class.  It does not cover lower-supported cointegrals,
nonfiltered structure maps, or a noncommutative associated graded, and it
does not settle the Andrews--Curtis conjecture.
