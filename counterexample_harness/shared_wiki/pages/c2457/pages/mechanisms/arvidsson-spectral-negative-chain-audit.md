---
title: Arvidsson spectral heat-trace negative-chain boundary
description: The displayed v1 heat-trace interval admits fixed-dimensional kernels; its endpoints cannot be equated.
---

Viktor Arvidsson's `viXra:2506.0023v1`, *Twin Primes: A Spectral
Proof of the Infinitude*, defines a diagonal penalty matrix and identifies its
kernel dimension with a pattern count. Section 5, Lemma 2 claims a nonzero
spectral gap \(3/10\). Section 6, Theorem 1 uses \(t=2\) and writes, under a
bounded-kernel hypothesis \(|T_N|\le C\),

\[
(N-C)e^{-3/5}\le \operatorname{Tr}(e^{-2H_N})
\le C+(N-C)e^{-3/5}.
\]

These bounds are compatible. For any fixed integer \(K\ge1\), set

\[
H_N=\operatorname{diag}(0_K,(3/10)I_{N-K}),\qquad N\ge K.
\]

Then

\[
\dim\ker H_N=K,\qquad
\operatorname{Tr}(e^{-2H_N})=K+(N-K)e^{-3/5}.
\]

Taking \(C=K\), the true trace equals the displayed upper endpoint and exceeds
the lower endpoint by exactly \(K\). Thus both inequalities hold for every
\(N\ge K\) while the kernel stays bounded. The paper's negative-kernel
contradiction arises only after its sentence "Equating the lower and upper
bounds to analyze feasibility," which adds an equality not implied by the
interval.

The displayed lower estimate also has the wrong general direction:
\(\lambda\ge3/10\) implies \(e^{-2\lambda}\le e^{-3/5}\). The diagonal
countermodel does not rely on this additional defect because all its nonzero
eigenvalues equal \(3/10\), making that displayed lower estimate true.

This retires only the generic Arvidsson v1 spectral transfer. The failure
occurs before any growing Cunningham-row specialization, and it proves
neither a statement about twin-prime infinitude nor a fixed-exponential
negative-residue chain or an Erdos counterexample.
