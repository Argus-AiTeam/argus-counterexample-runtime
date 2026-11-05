---
title: Planar hard-block equivalence and perturbation transfer
description: Exact lower-bound transfer for approximate assembly and the circularity of assuming planar hard blocks.
---

# Planar hard-block equivalence and perturbation transfer

Suppose fixed-length data \(f^{(n)}\) on finite planar domains \(D_n\)
have exact minimal Bezout lower bounds \(M_n\), and one global tuple \(F\)
approximates them with error \(\varepsilon_n\) on biholomorphic copies of
the **whole** \(D_n\). Every global Bezout row of norm \(C\) then satisfies

\[
 C\geq\frac{M_n}{1+m\varepsilon_nM_n}
   =\frac1{M_n^{-1}+m\varepsilon_n}.
\]

This follows by restricting the row, bounding its residual by
\(m\varepsilon_nC\), and applying an exact Neumann correction when that
residual is below one; the complementary case already gives the same lower
bound. Therefore \(M_n\to\infty\) and \(\varepsilon_n\to0\) suffice. No
rate such as \(\varepsilon_n=o(M_n^{-1})\) is required.

Approximation on a proper compact core does not transfer a lower bound
certified on \(D_n\), and blockwise gap control does not certify the gap on
connectors.

Gamelin, *Localization of the corona problem*, DOI
`10.2140/pjm.1970.34.73`, Theorem 3.4, proves that unbounded fixed-length,
fixed-gap Corona constants over finitely connected planar domains already
produce a connected planar Corona failure. The reverse implication follows
by restricting any negative witness to a finitely connected inner
exhaustion. Hence planar fixed-gap hard-block supply is equivalent to the
campaign goal, not a weaker input to a later assembly stage.

Oh's explicit hard surface in arXiv `1307.8028v1` has

\[
 b(R_n)=n^2+n,\qquad
 g(R_n)=\frac{(n-1)(n^2-2)}2,
\]

so every hard case \(n\geq2\) is nonplanar. Cutting or descending it does
not preserve its lower bound without a separate argument.

These facts retire only robust approximate assembly **as a noncircular
reduction from independently supplied planar blocks**. They do not obstruct
general approximate gluing or supply a counterexample.
