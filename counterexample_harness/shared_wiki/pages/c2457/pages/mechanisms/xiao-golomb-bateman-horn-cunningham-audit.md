---
title: Xiao Golomb-Abel-Bateman-Horn Cunningham boundary
description: The legal f(x)=x specialization makes the printed Abel series diverge, while the Cunningham tuple fails hypothesis F and has no growing-L threshold.
---

Huan Xiao's *From Golomb to Bateman-Horn*, DOI
`10.20944/preprints202512.2666.v1`, states Theorem 3.1 as a
monotone-convergence bridge and derives Theorem 1.2 and the advertised proof
of Theorem 1.1 through that bridge.

The first legal specialization already contradicts the bridge. Take
\(k=1\) and \(f(x)=x\). Hypothesis F is vacuous, and

\[
N_f(d)=1,\qquad
\sum_{\substack{1\le n\le d\\d\mid f(n)}}z^n=z^d.
\]

Thus the normalized summand is

\[
c_d(z)=\frac{d(1-z)z^d}{1-z^d}-1
=\frac{d z^d}{1+z+\cdots+z^{d-1}}-1.
\]

For \(d\ge1\) and \(0<z<1\),

\[
1+z+\cdots+z^{d-1}-d z^d
=\sum_{j=0}^{d-1}(z^j-z^d)>0,
\]

so \(-1<c_d(z)<0\), not \(c_d(z)\ge0\) as used in the source.
For each fixed \(z\in(0,1)\), \(c_d(z)\to-1\). Hence

\[
\sum_d c_d(z)=-\infty,\qquad
\sum_d\left(-c_d(z)+\frac1{d^2}\right)=+\infty.
\]

At the exact rational value \(z=1/2\),

\[
c_d(1/2)=\frac{d}{2(2^d-1)}-1\le-\frac12,
\]

because \(2^d-1\ge d\). In particular,
\(c_2(1/2)=-2/3\), and the corresponding equation-(18) summand is
\(11/12\). Theorem 3.1 and Theorem 1.2 are therefore false as printed.

The source explicitly derives equations (24)-(25), and hence Theorem 1.2,
from equation (18). Theorem 4.1 then invokes Theorem 1.2 to claim Agnew's
absolute-sum condition, although the source substitutes a signed sum for
\(\sum_d|c_d|\). The proof of Theorem 1.1 invokes Theorem 4.1. This breaks
the advertised proof chain; it does not refute the Bateman-Horn conjecture.

For second-kind Cunningham forms

\[
F_j(n)=2^j n-(2^j-1)=2^j(n-1)+1,
\]

the useful recurrence \(F_{j+1}=2F_j-1\) holds. But the tuple fails Xiao's
hypothesis F for every \(L\ge3\): at \(n=3\),
\(F_0(3)=3\), \(F_2(3)=9\), and their gcd is \(3\).
The source's reduction and asymptotics are qualitative for each fixed
finite tuple. They contain no error term or threshold uniform as \(L\)
grows, and therefore do not imply \(S_L(A^L)>0\) for one fixed \(A\) and
unbounded \(L\).

This boundary retires only Xiao version 1 as a source mechanism for the
fixed-exponential Cunningham family. It neither excludes Cunningham rows
nor settles the Erdos target.
