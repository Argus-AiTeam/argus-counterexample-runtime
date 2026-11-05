---
title: KS13 portfolio all-residual gcd-closure counterexample
description: Genuine global cofactor splitting occurs, but every row of the complete augmented matrix has an exact singleton-pivot elimination.
---

`KS13-PORTFOLIO-CFRAC-GCD-CLOSURE(2,2)` preserves the thirteen reviewed
KS13 streams and `B=L=n^2`, retains every generated row, and removes
every residual-size and prime-count cutoff. Exact gcd refinement and
square normalization give pairwise-coprime nonsquare atoms; all
residual multiplicities remain available for reconstruction.

The exact certificate uses the first frozen input

```text
N=664613999749367995379973941415116797
 =1073741827 * (2^89-1).
```

All 187,200 rows complete. Global closure starts with 186,869
distinct nonunit residuals and ends with 197,374 atoms after 48,471
proper splits and one exact-square normalization.

The residuals of `(stream 0,j=8)` and `(stream 3,j=1706)` satisfy

```text
r=817429843445623237 =27077 *30189084590081,
s=215758985873      =27077 *7968349,
gcd(r,s)=27077.
```

The first row was rejected by the three-large-prime predecessor:
its factors at most `120^3` leave the cofactor `158591933>120^3`.
It is now retained and properly split. The residual `40507^2` at
`(stream 12,j=289)` is reconstructed with exponent two, even though
its atom parity vanishes.

The complete sign/factor-base/atom matrix has 187,200 rows and
199,061 columns. Its exact rank is 187,200, so its complete kernel
is zero and the candidate returns `FAIL`. An independent
all-incident-gcd construction gives the same atom basis; an
independent singleton-column elimination peels every row, with no
remaining Gaussian-elimination core.

Compared with the 9,542-row three-large-prime predecessor, this
certificate includes 177,658 additional rows and genuine splitting
of formerly rejected residuals, without increasing either quadratic
budget. Nonsquare composite atoms are legitimate: pairwise
coprimality makes their exponent parity exactly characterize square
residual products. Factoring those atoms is not part of the
candidate.

The source, mathematical definition, polynomial-bit argument
(including the `O(n^3)` bound for full convergents), and rerunnable
certificate are in
`research/routes/structured-relations/multiplier-cfrac/ks13-gcd-closure-counterexample/`.
This refutes only the frozen all-residual KS13 candidate, not other
row budgets, unrestricted CFRAC, SIQS, or general integer factoring.
