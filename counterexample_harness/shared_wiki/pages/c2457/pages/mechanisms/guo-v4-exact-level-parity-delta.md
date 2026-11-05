---
title: "Guo v4 exact-level parity delta"
description: "The v4 pointwise theorem fixes the Liouville second factor, while arbitrary bounded targets remain shift-window moments with no prescribed-shift or relative exact-level control."
---

# Guo v4 exact-level parity delta

For the exact-level quantities

\[
M_r=\sum_{q\in E_r}\frac1{(q-1)^2},
\qquad
2S_{r,B}=A_{r,B}-L_{r,B},
\]

the fixed-shift substitution \(n=mq-1,\ h=1\) is exact. With

\[
\kappa_m(q)=\frac{mq-1}{(q-1)^2},
\]

the piecewise sequence

\[
b_{r,m}(t)=
\begin{cases}
\mathbf1_{P_2(t-1)}\kappa_m(q),
  &t=mq\text{ for some }q\in E_r,\\
0,&\text{otherwise},
\end{cases}
\]

is \(1\)-bounded for \(m\le B\) and all sufficiently high exact levels,
because \(\kappa_m(q)\le1\) once \(q\ge B+2\). It gives

\[
\sum_{n\le x}\frac{\lambda(n)b_{r,m}(n+1)}n
=
\sum_{\substack{q\in E_r\\mq-1\le x}}
\frac{\mathbf1_{P_2}(mq-1)\lambda(mq-1)}{(q-1)^2}.
\]

The obstruction is therefore not coefficient support. It is the source
quantifier:

| Guo v4 conclusion | Arbitrary \(1\)-bounded \(b\) | Prescribed \(h\) |
|---|---:|---:|
| Global and all-positive pointwise bounds | No; the second factor is \(\lambda(n+h)\) | Only outside the source exceptional set |
| Long-window and beyond-one-third moments | Yes | No; averaged over a shift window |

The two arbitrary-\(b\) theorem statements are byte-identical to those in
the frozen v3 source. The v4 additions are the single all-prefix sparse
exceptional set on \(1\le h\le x\) and its all-positive-shift extension,
both for the fixed Liouville second factor.

The diagonal substitution \(n=q,\ h=(m-1)q-1\) does not use a fixed shift.
The source exceptional-set density does not guarantee that these sparse
target shifts are nonexceptional, and a bound for a full fixed-\(h\) row
does not isolate its point \(n=q\).

All source errors are absolute harmonic estimates, with no comparison to
the sparse mass \(M_r\). The global threshold is also ineffective through
Siegel's theorem. Consequently the stated v4 contracts yield no explicit
\(B,\delta,R\). This excludes only the v4 transfer; the bounded-multiplier
prime correlation remains open.

The version-fixed source and exact derivation are in
`research/guo_v4_exact_level_parity_delta/`.
