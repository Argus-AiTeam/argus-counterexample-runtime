---
title: KS13 portfolio single-large-cofactor counterexample
description: Exact 120-bit semiprime with 56 repeated residual labels whose 2,602-row KS13 augmented relation matrix still has full row rank.
---

`KS13-PORTFOLIO-CFRAC-SLP(2,2,1)` retains the reviewed thirteen-multiplier
portfolio with `B=L=bit_length(N)^2`, then admits every exact post-factor-base
residual `1<r<=R=bit_length(N)^3`, adds one parity column per exact whole
integer `r`, and reconstructs each selected label to half its row multiplicity.

The first input in the frozen predecessor family is

```text
N=664613999749367995379973941415116797
 =1073741827 * (2^89-1).
```

It has 120 bits, so `B=L=14400` and `R=1728000`. All thirteen streams and all
187,200 rows complete with trivial preprocessing and early gcds. Exact division
admits 269 full-smooth rows and 2,333 partial rows. The partial rows contain
2,275 distinct labels, 56 of which repeat; two labels occur three times and the
other 54 occur twice.

Despite those genuine collisions, the full matrix with one sign column, 1,686
factor-base columns, and 2,275 exact-label columns has rank 2,602 on its 2,602
rows. Its complete nullspace basis is empty, so the frozen candidate returns
exact `FAIL`.

The producer-independent verifier receives candidate input containing only
`N`, derives the two factors outside the candidate, replays every recurrence
row and residual division, and obtains the same rank with an independent
lowest-coordinate-pivot elimination. It rejects mutations to residual labels,
factor multiplicities, rank, dependencies, and final status.

This refutes only the exact cubic-cutoff, one-label, basis-only candidate. It
does not cover a two-large-prime graph cycle, another cutoff, unrestricted
CFRAC, SIQS, or general integer factoring.
