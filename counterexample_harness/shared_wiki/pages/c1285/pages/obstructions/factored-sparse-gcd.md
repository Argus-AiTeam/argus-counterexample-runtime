---
title: Factorwise sparse-gcd batching obstruction
description: Exact order-4ell exclusion for adaptive gcds on unexpanded products of polynomially many sparse rational numerators.
---

# Factorwise sparse-gcd batching obstruction

`FACTORED-SPARSE-GCD` extends `SPARSE-RATIONAL-RING` with adaptive gcd calls
on

```text
product_j P_j^e_j,
```

where each `P_j` is a live explicit sparse numerator, polynomially many
factors may be listed, and each nonnegative multiplicity has polynomial bit
length. The product is evaluated modularly and is never expanded or retained.
Repeated factors, zero multiplicities, arbitrary batching, subbatch splitting,
and transcript-dependent schedules are included. The output remains one
ordinary sparse rational pair.

Over either CRT prime field, an active product is zero exactly when one active
factor is zero. Therefore the order-`4ell` construction needs to avoid only
the individual nonzero factor norms. Polynomially many additional factors
increase the bad-prime inventory by only a polynomial factor; the potentially
exponential multiplicities never enter the norm bound.

For every fixed resource tuple and advice sequence, a canonical infinite
actual-length CRT family satisfies

```text
Pr[proper factor or odd-factorial target]
  <= 2^(-bitlength(N)/100)
```

after an effective threshold. Modular binary powering also keeps every new
oracle call within polynomial classical bit complexity.

This excludes gcds of pure unexpanded products only. A gcd on an additive
combination of compressed products, or retention of an unexpanded product
inside a rational register, is a different and still-open representation
frontier.
