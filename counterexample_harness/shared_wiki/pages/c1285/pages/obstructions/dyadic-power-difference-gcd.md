---
title: Dyadic power-difference gcd obstruction
description: Exact refined order-4ell exclusion for adaptive oracle gcds on differences P^(2^t)-Q^(2^t) of live explicit sparse numerators.
---

# Dyadic power-difference gcd obstruction

`DYADIC-POWER-DIFFERENCE-GCD` extends `SPARSE-RATIONAL-RING` only with
adaptive oracle calls

```text
gcd(P^(2^t)-Q^(2^t),N),
```

where `P` and `Q` are single live explicit sparse numerators. The canonical
binary representation of the actual exponent `2^t` is charged and has
polynomial length, so the backend uses polynomially many repeated modular
squarings. Neither power nor their difference may be retained.

The hard family refines the reviewed split-prime pools to

```text
p congruent to 1+4ell modulo 8ell.
```

Thus `v_2(p-1)=2`. Over either CRT field, the exact root set of
`r^(2^t)=1` is

```text
t=0:   {1},
t=1:   {1,-1},
t>=2:  {1,-1,i,-i}.
```

Including zero operands, every new local equality is therefore the union of
at most four explicit sparse residual zero sets:

```text
P-Q, P+Q, P-iQ, P+iQ.
```

The reviewed tape-weighted cyclotomic norm argument can avoid these
polynomially many residuals without expanding either power. For every fixed
resource tuple and advice sequence, a canonical infinite actual-length CRT
family satisfies

```text
Pr[proper factor or odd-factorial target]
  <= 2^(-bitlength(N)/100)
```

after an effective threshold.

The producer-independent finite replay uses
`N=96673=277*349`, a 257-bit encoding of `2^256`, all three `t` regimes,
both-zero, exactly-one-zero, and two-nonzero operands, and adaptive `ONE` and
`WHOLE` schedules; exact success is `0/2`. A typed Jacobian table for
`x^8-1` over `GF(125)` independently has exactly four zeros.

This excludes only oracle-only dyadic powers whose full exponent encoding is
polynomial. Arbitrary differences of products, retained succinct values,
logarithmically encoded exponential squaring counts, explicit width-two
chains, unrestricted rational circuits, and general integer factoring remain
open.
