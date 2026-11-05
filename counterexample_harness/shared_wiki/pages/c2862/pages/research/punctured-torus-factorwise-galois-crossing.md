---
title: Punctured-torus factorwise Galois-crossing boundary
description: Exact diagonal reduction, complete cyclotomic factors, primary-source theorem limits, and the finite no-counterfactor range.
---

# Punctured-torus factorwise Galois-crossing boundary

For

```text
F(U,V)=(U^2-U+1)(V^2+1)-(U^2+1)V
P_n(U)=F(U,U^n),
```

the discriminant in `V` is

```text
-(U-1)^2*(3*U^2-2*U+3).
```

Thus `F` is geometrically irreducible, and its support differences generate
the full lattice `Z^2`. With `X=U+U^-1`,

```text
U^(-n-1)*P_n(U)=(X-1)*C_n(X)-X,
```

where `C_n(U+U^-1)=U^n+U^-n`.

The complete cyclotomic part is exactly

```text
(U-1)^2
* Phi_4(U)^[n odd]
* Phi_5(U)^[n mod 5 in {2,3}],
```

with the latter two factors simple. Removing these gives the reciprocal lift
of `J_n`.

The audited general theorems do not prove that `J_n` is irreducible:

* fixed two-block Schinzel theorems do not represent the three moving
  exponent blocks of `P_n`;
* Filaseta's multi-block theorem controls only the non-reciprocal part, so
  even under all hypotheses it cannot bound the number of reciprocal
  factors;
* irreducibility of every bivariate `F(U,V^m)` does not imply irreducibility
  after the additional diagonal substitution `V=U^n`;
* complex toric Bertini and its Kronecker corollary retain a free cover
  variable and do not assert one Galois orbit over `Q`.

The generic Pell/norm shape is also insufficient. The irreducible degree-eight
polynomial

```text
1+(X-1)*(X+2)*(X^3+2*X^2-1)^2
```

has endpoint values `1` at `-2`, `-1`, and `1`, but its only two real roots
both lie strictly inside the `SU(2)` interval. This is not a `J_n` factor; it
shows that a direct proof must use the specific Chebyshev square rather than
only the norm form and endpoint units.

Exact PARI factorization finds no reducible `J_n` through `n=1000`.
Jacobian and an independent PARI replay both return one degree-300 factor
for `J_301`. This is a finite negative experiment, not an all-`n` theorem.
The factorwise Galois-crossing claim and the complete slope-adapted no-go
therefore remain open.

The detailed source audit and replay are in
`research/PUNCTURED_TORUS_FACTORWISE_GALOIS_CROSSING.md` and
`research/verify_punctured_torus_factorwise_galois_crossing.py`.
