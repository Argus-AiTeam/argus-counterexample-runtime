---
title: Agama area-method negative-chain boundary
description: Fixed-shift, triangular-domain, local-density, and uniform-constant obstructions to the proposed Cunningham-chain transfer.
---

The 2021 source is Theophilus Agama's *On the Infinitude of Sophie Germain
Primes*, viXra:2103.0150v3. It cites *The area method and applications*,
arXiv:1903.09257, without a version. The viXra v3 record is dated
2021-04-03 08:40:12 UTC. ArXiv v6 is dated 2020-10-11 11:02:47 UTC, while
v7 appeared at 2021-04-03 13:31:26 UTC. Consequently v6 is the exact latest
version that was available when viXra v3 appeared. The separately requested
v8 is dated 2026-03-21.

The v6 area-method Theorem 2.3 concerns one fixed additive shift \(l_0\) and
writes its constant as \(\mathcal C(l_0)\). Version 8 repeats this as Theorem
2.2. Their prime application is only the fixed shift
\(\Lambda(n)\Lambda(n+2)\); neither version states a \(2n-1\) application.

ViXra equation (3.1) instead substitutes \(l_0=n+1\) inside the summand to
obtain \(2n+1\). This is not a choice of one scalar shift. It also violates
the cited triangular domain \(j\le x-n\) whenever \(n>(x-1)/2\), although
the equation sums over every \(n\le x\).

With

\[
S_x=\sum_{n\le x}\vartheta(n)\vartheta(2n+1),\qquad
T_x=\sum_{2\le n\le x}\vartheta(n)\sum_{m<n}\vartheta(m),
\]

equation (3.1) defines \(D=xS_x/T_x\). Thus its unproved assertion
\(D\ge1\) is exactly the desired lower bound \(S_x\ge T_x/x\).

There are two exact counterexamples to the more general printed contracts.
At \(x=8\), the function supported by
\(f(1)=f(2)=1,f(4)=16,f(8)=256\) has shift-one sum \(1\) and triangular
sum \(4641\), forcing \(D=8/4641<1\). To rule out an ambiguity about zero
values, the strictly positive function

\[
g(1)=g(2)=1,\qquad
g(n)=
\begin{cases}
2^n,&4\mid n,\\
2^{-n^2},&4\nmid n
\end{cases}
\]

has shift-one sum at most \(3/2\), while at \(x=4K\) its triangular sum is
at least \(2^{8K-4}\). Any \(x\)-uniform printed constant must therefore be
at least \(2^{8K-4}/(6K)\), which is unbounded. Allowing the constant to
depend on \(x\) instead leaves no asymptotic positive constant.

This is a source-mechanism boundary. It blocks an \(L\)-fold negative-chain
extension from these papers but does not prove that second-kind Cunningham
rows fail to exist and does not settle the Erdos target.
