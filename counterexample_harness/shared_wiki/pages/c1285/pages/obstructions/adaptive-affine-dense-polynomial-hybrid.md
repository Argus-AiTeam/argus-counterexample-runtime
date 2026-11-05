---
title: Adaptive affine/dense-polynomial hybrid obstruction
description: Exact common-family exclusion for transcript-adaptive interleavings with all cross-trial state differences.
---

# Adaptive affine/dense-polynomial hybrid obstruction

## Frozen class

A member is one uniform randomized bit algorithm with worst-case polynomial
budgets. At each recursive call it may adaptively interleave and resume fresh
exactly uniform affine trials and fresh exactly uniform dense-polynomial trials.
A dense trial with `L` coefficients has at most `L` transitions. The controller
sees the full prior transcript and may use raw-sample gcds, every within- and
cross-trial orbit-state difference, arbitrary product batching and recursive
splitting, and `ONE`/`WHOLE` outcomes. A composite is split only by the exact
registered preprocessing or a verified proper gcd.

## Exact obstruction

For every fixed member with polynomial cap `Q(n)`, let

```text
ell_h = least prime > 2^h,
p_h   = least prime congruent to 1 mod 4 ell_h,
q_h   = least prime congruent to 1+2 ell_h mod 4 ell_h,
N_h   = p_h q_h.
```

The canonical family contains infinitely many preprocessing-evasive squarefree
semiprimes and eventually has `n_h=bit_length(N_h)<=12h`. Every fixed-time
state of either fresh trial type is exactly uniform over each local prime field:
for affine maps this follows from
`(A,B,x_0)->(A,B+(1-A)c,x_0+c)`, and for dense maps from
`(f,x_0)->(f(X-c)+c,x_0+c)`.

Combining these translation bijections with the exact affine short-order
classification and the adaptive Vandermonde first-repeat law gives

```text
Pr[complete factorization of N_h] < 2 Q(n_h)^4 / ell_h
                                    < 2^(-n_h/24)
```

eventually. The containment includes all raw operands, all same- and
cross-trial differences, interleaving and resumption, arbitrary batches and
splits, `ONE`/`WHOLE` control, sampler failure, recursion, and verification.

## Scope limit

This excludes only fresh exactly uniform affine trials and dense trials whose
orbit length does not exceed their coefficient dimension. It does not cover
fixed low-degree long orbits, nonuniform or factor-aware map distributions,
coefficients correlated with prior trials, unregistered gcd operands, ECM,
unrestricted Pollard rho, or general integer factoring.

The proof and exact replay are in
`research/routes/structured-relations/adaptive-affine-polynomial-hybrid/`.
