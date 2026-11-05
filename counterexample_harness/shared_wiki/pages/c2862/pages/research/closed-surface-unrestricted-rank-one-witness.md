# Closed-surface F0/H2 residual no-go

The source-bound `F0/H2` residual for

```text
F = D_(b^-1 c) o (phi^3 union psi^3)
```

has now been classified exactly.  Its characteristic-zero ideal has a
29-generator leading ideal and 24 standard monomials.  Seven modular bases
were used only to reconstruct a candidate; exact `QQ` Buchberger reductions,
source reductions, leading-ideal equality, and dimension equality certify the
source ideal itself.

The separating element `X+2*U` gives a square-free irreducible degree-24
polynomial and exact coordinate maps for every residual and authoritative
trace coordinate.  All 33 frozen source equations vanish in the resulting
quotient.

Exact Sturm counting gives zero real roots.  Hence the quotient has no real
embedding, no compact irreducible `SU(2)` point, and no point at which a
thirteen-eigenvalue relation lattice must be computed.  The physical-point
list is empty and the number of rank-12 survivors is zero.

Jacobian `0.14.0` independently returned the same degree-24 characteristic
polynomial from the exact rational multiplication matrix.  The full proof and
replay are:

- `research/CLOSED_SURFACE_UNRESTRICTED_RANK_ONE_WITNESS.md`
- `research/verify_closed_surface_unrestricted_rank_one_witness.py`
- `roles/engineer/unrestricted_rank_one_witness_replay.json`

This is a bounded no-go for the residual one-angle mechanism, pending
independent Reviewer acceptance.  It emits no Chern--Simons candidate, does
not by itself restore the withdrawn four-component/32-point cover, and does
not terminate campaign 2862.
