---
title: Product-difference gcd multiplicative barrier
description: Exact exponent compilation handles opaque products, low-L1 expansion handles adaptive visible calls, and bounded tensor expansion handles linear-rate mixed Jacobi and residue-equality feedback after one high-entropy gcd gate.
---

# Product-difference gcd multiplicative barrier

`PRODUCT-DIFFERENCE-GCD` extends the reviewed sparse-rational model only with
adaptive oracle calls

```text
gcd(product_j P_j^e_j - product_l Q_l^f_l, N).
```

Each factor is a live explicit sparse numerator, each nonnegative
multiplicity has polynomial binary length, and zero multiplicities are
omitted. Either side may be empty. Neither compressed product nor their
difference is retained, and the output remains an ordinary explicit sparse
rational pair.

Over a CRT field, both products are zero when each side contains an active
zero factor; they differ when exactly one side does. If all active factors are
nonzero, common factors cancel and equality becomes one compact
multiplicative relation. This last case is strictly beyond the reviewed pure
factored-product and dyadic power-difference zero sets.

The inherited direct norm bound grows with the numeric multiplicities, which
may be exponential in their legal encodings. Kummer characters remove that
numeric dependence modulo an auxiliary order, but the resulting proof needs
an unconditional supply of prescribed-Frobenius primes whose bit length stays
logarithmic in the growing cyclotomic conductor. Discriminant-scale bounds do
not preserve the campaign's actual-length advice closure. A raw transcript
pigeonhole also fails for arbitrary polynomial query depth because the short
prime/root pool has only exponential cardinality.

## Rank-one finite-pool synchronization counterexample

Finite multiplicative rank and finite pool cardinality alone do not force a
close pair. At actual length 200, an exact Lucas-certified pool of 32 primes
`p=13 mod 24` supports one 3188-bit integer `c` whose local orders are 32
distinct primes `r_i`. Indexing the sites by `v in F_2^5` and querying

```text
gcd(c^(product_(v dot t=1) r_v)-1,N)
```

on a uniform tape `t in F_2^5` makes the local equality word at site `v` the
linear word `t -> v dot t`. Every two of the 32 words differ on exactly 16 of
32 tapes. Consequently every one of the 496 site pairs returns a proper factor
with exact probability `1/2`, exceeding the frozen synchronization threshold
`2^(-200/100)=1/4`. The coefficient has 3188 bits, the largest multiplicity
has 319 bits, and no compressed value is retained.

This exact certificate refutes only the finite-rank-and-pool-size-only lemma.
The integer `c` was CRT-encoded from the finite site pool; doing the same for
the asymptotically exponential post-advice pool would exceed polynomial advice.
Thus the parent post-advice structural-entropy obligation remains open.

## Opaque single-base post-advice obstruction

The post-advice obligation is now settled for the strict opaque-handle
extension in which every live object remains a power of one hidden base.
Controllers may synthesize arbitrary polynomial-bit nonnegative scalars from
length advice, tape bits, and prior tags; retain scalar-powered handles; and
compare polynomial lists with repetitions, zero omission, and empty products.
The inherited pairwise signed gcd operations also remain available.

Every retained handle compiles to an integer exponent polynomial `E(X)`, and
every product side compiles to a sum of online multiplicities times such
exponents. Although the numeric exponents can be exponentially large, all
values at `X=1` have polynomial bit length. Exact tape-weighted counting over
all lengths through `12h` therefore selects a prime `ell` from
`(2^(h/2),2^h]` that divides only exponentially small tape mass. After that
selection, least primes in the classes `1` and `1+2ell` modulo `4ell` and a
CRT base of exact local order `2ell` make every good-tape product difference
simultaneously equal or unequal at both factors. Hence every good gcd is
`ONE` or `WHOLE`, and every good output misses the odd part of `(N-1)!`.

The resulting canonical actual-length infinite family has total
proper-factor-or-target success eventually at most
`2^(-bitlength(N)/24)`. An independent exact `N=1247` replay covers adaptive
online scalars, retained powers, repeated and empty products, zero omission,
all tag semantics, target exclusion, and mutation rejection. The finite
replay is illustrative; the asymptotic proof is the tape-weighted divisor
argument.

This theorem does not conflict with the 32-site rank-one code. That code can
separate a finite pool because its generator is CRT-encoded after the sites
are chosen. It cannot make polynomial-bit specialized comparisons carry high
bad tape mass at every prime of an exponentially large post-advice window.

The exact finite anchor

```text
N = 96673 = 277 * 349
```

has refined order-12 local bases and

```text
ord_277(2)=92,     ord_349(2)=348.
```

Thus `2^92-1` and `2^348-1` expose opposite CRT factors even though the
individual factors `2` and `1` are nonzero in both fields. The independent
replay also covers repeats, zero multiplicities, local zero cases, common
factors, adaptive batching and splitting, all gcd tags, valid denominators,
early recursive completion, target exclusion, and modular-power bit cost.

This finite split still proves that individual-factor norm avoidance does not
extend mechanically to visible sparse factors. The new obstruction applies
only when all live factors are opaque powers of one synchronized base. Visible
sparse-ring addition, N-dependent residue computation, retained compressed
values, general sum-of-products circuits, width-two chains, and integer
factoring remain outside the claim.

## Adaptive low-L1 visible product differences

For every fixed rational `0<alpha<1/86`, the
`LOW-L1-PRODUCT-DIFFERENCE-GCD(alpha)` subclass requires each temporary call
to obey

```text
product_j ||P_j||_1^e_j + product_l ||Q_l||_1^f_l
  <= 2^floor(alpha*n).
```

The norm is the coefficient L1 norm of the stored visible sparse numerator.
On a nonzero product side, every norm-one factor is necessarily a signed
Laurent monomial and all of its polynomial-bit multiplicities aggregate into
one polynomial-bit exponent label. Every other factor has norm at least two,
so its total multiplicity is at most `floor(alpha*n)`. An active zero factor
is handled separately by compiling the entire side to zero; no false
multiplicity bound is asserted after that short circuit.

Consequently each complete product difference has a polynomial-size layered
Laurent ABP with at most `2^floor(alpha*n)` paths, polynomial exponent-
difference bit length, and root-of-unity absolute value bounded by the same
L1 budget. Add these residuals to the reviewed one-anchor conductor and norm
inventory. For the selected conductor `ell` and selected CRT primes `p,q`,
define `G` to be the event that the tape is conductor-nonexceptional and every
nonzero generic-inventory norm avoids both `p` and `q`. On `G`, every reached
denominator is a unit, every reached ordinary and product-difference tag
matches the generic transcript, no call returns a proper factor, and both
target signs are excluded.

If `delta_ell` is the conductor-exceptional tape mass and `w_p,w_q` are the
two selected-prime norm-bad masses, then

```text
Success subseteq G^c,
Pr(G^c) <= delta_ell+w_p+w_q.
```

This is a union bound; the bad events may overlap and no independence is
assumed. In the detailed proof, equations (22) and (26) bound the conductor
and selected-prime terms, while equation (30) applies this containment and
union bound.

The resulting canonical infinite actual-length order-`4ell` family satisfies

```text
Pr[proper factor or odd-factorial target]
  <= 2^(-(1/86-alpha)*bitlength(N))
```

eventually. The endpoint `alpha=1/86` is not included: there the conductor
decay exponent is zero. This result covers adaptive multi-call visible
products only under the displayed L1 promise. High-L1 compressed products,
retained products or differences, general sum-of-products circuits, and
integer factoring remain open.

## One terminal retained high-entropy difference

The first retained visible high-entropy state is also obstructed when it
produces no tag at assignment and is used exactly once in one terminal gcd
or target output. Before that assignment, the controller has the reviewed
ordinary sparse-rational registers and tags. The two multiplicative sides
and their multiplicities have no L1 or numeric-size ceiling.

Use the dense same-length pool of primes `p=1 mod 4` in the top quarter of a
dyadic interval and choose the local base to be a square root of `-1`.
Every ordinary sparse-rational expression then specializes to a Gaussian
integer because `N=pq=1 mod 4` makes every formal exponent satisfy
`E(N)=E(1) mod 4`. Only polynomially many pool primes can divide the
polynomial-bit Gaussian norm inventory on one tape, so the complete ordinary
adaptive transcript couples outside vanishing average tape mass.

On a coupled tape, one terminal high-entropy gcd contributes one Boolean
zero label per prime site. Averaging over distinct site pairs bounds its
proper-factor probability by `1/2+o(1)`, independently of expansion size or
multiplicity.

For an output, the odd part of `(pq-1)!` modulo four is

```text
(-1)^(number of binary one-runs of (pq-1)/4).
```

This run-parity function has the carry property and square-root Fourier
decay. Mauduit--Rivat's arbitrary-weight Type-II estimate therefore makes
the two target-sign edge classes asymptotically balanced against every pair
of controller-selected site subsets. The target-success pair average is
again `1/2+o(1)`. Combining this with the ordinary bad-site mass gives a
canonical infinite actual-length family with total success eventually below
`2/3`.

This closes one tagless retained difference with one terminal use, and also
the one-call high-L1 product-difference slice. It does not close two
high-entropy tags: several Boolean coordinates can form a code with no close
site pair. Division by the retained state, another retained difference,
further nesting, representative inspection, unrestricted width-two chains,
and integer factoring remain open.

## One immediate gate followed by a reciprocal branch

The next explicit retained-state capability is also obstructed when the
unique high-entropy difference is immediately tested:

```text
D=A-B,
gcd(D,N),
WHOLE -> one ordinary terminal output,
ONE   -> one terminal H*D^s with polynomial-bit signed integer s.
```

The `ONE` tag certifies that negative `s` is evaluable by inversion. The
signed exponent is fixed by length, advice, tape, the coupled ordinary
transcript, and the gate tag; it cannot depend on an inspected representative
or a formal value of `N`. No later tag, second retained difference, nesting,
or width-two update is present.

Use a dense fixed-order-eight pool of primes `p=1 mod 8` and canonical local
primitive eighth roots. The odd part of `(pq-1)!` has the exact four-color
law

```text
U_(pq) = (-1)^(d1+d2) 3^(s2+d2) modulo 8,
```

where `s2`, `d1`, and `d2` are the binary digit, adjacent-pair, and
distance-two-pair parities of `(pq-1)/8`. All three nonprincipal characters
have exact scaled-unitary two- or four-state Laurent transfer matrices and
the Mauduit--Rivat carry property. The resulting arbitrary-weight Type-II
estimate mixes every target color against controller-selected site subsets.

Over `Z[zeta_8]`, polynomially many fixed-degree norms couple the complete
ordinary transcript outside a vanishing site fraction. On a coupled tape,
write `Z` for sites where `D=0` and `V` for sites where `D` is a unit. The
gate factors every crossing pair, while four-color mixing bounds correct
terminal outputs inside either same-label region:

```text
2|Z||V| + (|Z|^2+|V|^2)/4
  <= 5(|Z|+|V|)^2/8.
```

Thus every frozen controller has a canonical infinite actual-length
counterfamily with total success `5/8+o(1)`, and eventually at most `31/48`,
strictly below `2/3`. The exact replay covers 4,097 factorial values, all
three characters, the complete five-site order-eight anchor, 100,000
gate/branch/output labelings, concrete `PROPER`, `WHOLE`, and reciprocal
`ONE` branches, a typed Jacobian matrix product, and nine mutations.

Taken alone, this result did not cover a second retained difference or
retained nesting. The next result absorbs those capabilities when every new
operation is tagless and CRT-local. A second gate, a later tag, an
`N`-dependent retained exponent, representative inspection, width-two
updates, unrestricted rational circuits, and integer factoring were and
remain outside the immediate-gate theorem. It asserts no containment relation
with `WIDTH2-RATIONAL-TRANSFER`.

## Arbitrary tagless CRT-local DAG around one gate

`ONE-HIGH-ENTROPY-FEEDBACK-CRT-LOCAL-DAG` permits an arbitrary
polynomial-size DAG before the gate and a different arbitrary
polynomial-size DAG on each nonproper branch. Nodes may be copied and reused
without restriction and may apply addition, subtraction, multiplication,
polynomial-bit nonnegative powers, and inversion of an earlier certified
unit. The gate operand becomes certified only on `ONE`. Exactly one gcd gate
and one terminal output are allowed; there is no later equality, tag,
validity branch, representative inspection, or other observation.

Every inverse has a typed derivation rooted in an earlier `ONE` certificate.
Topological induction then proves that every node commutes with both CRT
projections. Copies and ring operations are immediate; powers preserve a
ring homomorphism; and projecting `u*u^(-1)=1` gives the unique local inverse.
This induction is independent of DAG depth, reuse, expanded support, formal
degree, and algebraic entropy.

After the reviewed ordinary transcript is coupled, the tagless DAG needs no
new norm inventory. At each prime site the unique gate operand is simply zero
or nonzero. For a squarefree pair this gives exactly

```text
Z x Z -> WHOLE,
Z x V or V x Z -> PROPER,
V x V -> ONE.
```

The two branch DAGs therefore define one site-local output on `Z` and one on
`V`. Sorting each output by the four possible odd powers of the canonical
eighth root gives the same eight disjoint sets used by the reviewed
four-color argument. Arbitrary-weight Type-II mixing and the exact gate table
again give

```text
2|Z||V| + (|Z|^2+|V|^2)/4
  <= 5(|Z|+|V|)^2/8.
```

Consequently every frozen controller has a canonical infinite actual-length
counterfamily with total success `5/8+o(1)`, eventually at most `31/48`.
Online evaluation remains polynomial because all nodes hold `O(n)`-bit
residues, powers use binary modular exponentiation, and certified inverses use
extended Euclid.

The producer-independent finite replay uses the complete five-site
order-eight anchor and `x=401*409`. Its ten pairs realize one `WHOLE`, six
`PROPER`, and three `ONE` gates. It checks 216 global-to-local node
projections, rejects 14 illegal programs including hidden feedback and
uncertified inversion, and rejects ten certificate mutations. It does not
repeat the previously reviewed factorial, Fourier, prime-pool, or Jacobian
certificates.

The remaining frontier requires a second high-entropy observation or a
departure from CRT locality. In particular, a second gate, later tag,
representative-sensitive operation, unchecked validity branch, residue-chosen
exponent, `WIDTH2`, unrestricted rational controller, and general factoring
remain open.

## Linear-rate adaptive Jacobi feedback after the gate

`LINEAR-JACOBI-FEEDBACK-CRT-LOCAL-DAG` adds, on either nonproper branch,

```text
K(n)=floor(n/2400)
```

adaptive Jacobi-symbol queries of currently certified unit DAG values.
Tagless CRT-local work may occur between queries and depend on every earlier
tag. A Jacobi tag adds no unit certificate, so a nonunit query and its zero
outcome remain outside the grammar.

For a squarefree pair `N=pq`, every legal query has the exact form

```text
Jacobi(u/N)=Legendre(u(p)/p) Legendre(u(q)/q).
```

After fixing a transcript prefix, both Legendre factors are site-local signs.
For a leaf `tau` of depth `k`, its exact consistency indicator is

```text
2^(-k) product_j (1+tau_j ell_j(p)ell_j(q)).
```

Expanding this product gives `2^k` rank-one bounded pair weights. The reviewed
arbitrary-weight Type-II estimate absorbs each one. Summing every leaf, target
color, character, and both nonproper gate regions gives the sharper error
`6*2^K*Delta_h`, hence the conservative bound `O(4^K*Delta_h)`. At actual
length `n=2h`,

```text
4^K*Delta_h/M_h^2
 = O(h^(11/4) 2^(-h/600))
 = o(1).
```

The principal character contributes at most one quarter of each same-gate
region because every pair realizes one leaf and at most one common output
color. Adding the crossing-factor region preserves the reviewed optimization:

```text
2|Z||V|+(|Z|^2+|V|^2)/4 <= 5(|Z|+|V|)^2/8.
```

Thus every frozen controller has a canonical infinite actual-length
counterfamily with total success `5/8+o(1)`, eventually at most `31/48`.
An independent exact replay uses eight Proth-certified 2400-bit primes, so all
28 products have 4800 bits and genuinely permit two queries. It covers every
gate outcome, all four adaptive transcripts on both nonproper branches,
Jacobi-Legendre factorization, exact rank-one expansion, illegal nonunit
queries, and certificate mutations.

This intermediate result closes the first globally computed but
rank-one-separable feedback primitive after the unique gcd. It leaves equality
feedback to the mixed theorem below. A second factor-producing gate, a Jacobi
zero branch from an uncertified operand, validity feedback,
representative-sensitive operations, larger query rates, unrestricted rational
controllers, and general factoring remain open.

## Linear-rate adaptive equality and Jacobi feedback after the gate

`LINEAR-EQUALITY-JACOBI-FEEDBACK-CRT-LOCAL-DAG` permits each of the

```text
K(n)=floor(n/2400)
```

adaptive post-gate observations to be either a certified-unit Jacobi query or
global equality between two current CRT-local residues. Arbitrary tagless
CRT-local work may occur between observations and depend on the complete mixed
transcript. Equality creates no unit certificate: `FALSE` can mean that the
difference is a zero divisor, while `TRUE` makes it zero.

At a fixed transcript prefix, let `e(r)` be the local equality bit at prime
site `r`. CRT injectivity gives the exact branch indicators

```text
TRUE  = e(p)e(q),
FALSE = 1-e(p)e(q).
```

Their tensor-L1 costs are one and two. A Jacobi branch indicator has tensor-L1
cost one through its two-term Legendre expansion. If `T_d` is the sum of leaf
tensor masses below a node with `d` observations left, a Jacobi node gives
`2T_(d-1)` and an equality node gives at most `3T_(d-1)`. Therefore every
fully adaptive mixed tree has total tensor mass at most `3^K`.

The reviewed arbitrary-weight four-color Type-II estimate absorbs every
rank-one term. Across both nonproper gate regions the nonprincipal error is at
most

```text
6*3^K*Delta_h.
```

At actual length `2h`, `K=floor(h/1200)` and

```text
3^K*Delta_h/|P_h|^2
 = O(h^(11/4) 2^(-h/600+O(1)))
 = o(1).
```

Every pair still realizes exactly one leaf, so the principal contribution is
one quarter of each same-gate region. The unique gcd gate consequently retains
the same optimization

```text
2|Z||V|+(|Z|^2+|V|^2)/4 <= 5(|Z|+|V|)^2/8.
```

Every frozen controller therefore has a canonical eligible actual-length
counterfamily with success `5/8+o(1)`, eventually at most `31/48`. This closes
linear-rate arbitrary interleavings of the two displayed observations, not
just a fixed query order.

The remaining feedback frontier needs an observation with uncontrolled tensor
complexity or another factor-producing gate. In particular, a second gcd,
certificate inference from equality, an uncertified Jacobi zero branch,
validity or representative-sensitive feedback, larger observation rates,
unrestricted rational controllers, and general factoring remain open.

## Exactly two adaptive factor-producing gates

`TWO-GATE-LINEAR-EQUALITY-JACOBI-CRT-LOCAL-DAG` now freezes exactly one
additional gcd on every first-gate nonproper path. Its operand may depend on
the complete earlier mixed transcript; observations may occur before and after
it, with the same total

```text
K(n)=floor(n/2400).
```

At a fixed prefix let `d(r)` indicate that the second operand is zero at the
prime site `r`. The exact second-gate indicators are

```text
WHOLE  = d(p)d(q),
ONE    = (1-d(p))(1-d(q)),
PROPER = d(p)(1-d(q))+(1-d(p))d(q).
```

Their tensor-L1 costs are `1,1,2`. The two nonproper branches therefore make
the no-factor terminal mass at most `2*3^K` per first-gate nonproper region,
and the complete nonprincipal target error is

```text
12*3^K*Delta_h=o(|P_h|^2).
```

The new obstruction is principal. If `A_h` and `Q_h` are the normalized
masses factored by the first and second gcd, respectively, the reviewed
order-eight method gives only

```text
success <= 1/4+3(A_h+Q_h)/4+o(1).
```

A counterfamily strictly below `2/3` now requires a new arithmetic estimate
`A_h+Q_h<=5/9-eta`. No reviewed result supplies it. In the narrower case where
the second operand is independent of pairwise observation transcripts, four
zero-signature cells give the sharp relaxation

```text
success <= 1-(3/4)sum_i x_i^2 <= 13/16.
```

The exact SOS identity

```text
sum_i x_i^2-(sum_i x_i)^2/4
  = sum_(i<j)((x_i-x_j)/2)^2
```

certifies the last optimization. Since `13/16>2/3`, this is a proof-method
boundary, not an asymptotic counterfamily for the two-gate class.

The value is genuinely attainable inside the legal transcript-independent
subgrammar. At length 20, the two advised operands

```text
469711931057 = 769*809*857*881,
541539533233 = 769*809*929*937
```

give the four zero-signature cells `ZZ,ZU,UZ,UU` on eight explicit primes
`1 mod 8`. Choosing cell labels independently, using distinct primes on the
diagonal, and guessing the odd target exponent uniformly from `{1,3,5,7}`
gives exact weighted success `3/4+(1/4)(1/4)=13/16`.

For an asymptotic legal bank, partition the first `4h` primes of `P_h` into
four cells of size `h` and advise the two corresponding products. Each
operand has fewer than `2h^2+1` bits, every pair has actual length `2h`, and
the exact average over distinct pairs is

```text
(13h-1)/(16h-4) = 13/16+9/(64h-16).
```

This is a controller-encoded polynomial-size bank, so it neither supplies a
uniform advice-free controller nor defeats a hard distribution chosen from
the exponentially large pool after the controller is fixed. It does show
that locality, tensor cancellation, and four-cell simplex optimization alone
cannot force success below `2/3`. A uniform controller, a post-advice
arithmetic theorem controlling combined proper-factor mass, and general
factoring all remain open.

The post-advice quantifiers are now explicit. For fixed resources, controller,
length advice, and a tape-independent input law `mu_h`, condition on the
reviewed prelude-good ordered pairs and let `S_omega(p,q)` be the indicator
that the first gate is nonproper and the transcript-selected second gate is
`WHOLE` or `ONE`. Exact path partitioning gives

```text
A_h+Q_h = 1-E_(omega,(p,q)~mu_h) S_omega(p,q).
```

Thus the missing mass theorem is precisely a lower bound
`E S_omega>=4/9+eta`. For each fixed tape, diagonal transcript
synchronization does produce a target-balanced no-factor class of size at
least `(M_h-poly(h))/2^(K+2)`. It cannot be averaged into a valid hard law,
because that class depends on the realized tape. A legal four-site,
eight-tape certificate has a hard pair on every tape while every fixed pair
is factored with probability at least `5/8`, making the quantifier failure
exact.

Raw characteristic-zero norm height also does not provide the needed
post-advice compression. The legal operand
`2^(2^(n^2))-1` has a polynomial-bit exponent label and polynomial modular
cost, but bitlength `2^(n^2)`, already far beyond the logarithm of the product
of the complete order-eight pool. This rules out height-only divisor counting,
not a stronger arithmetic theorem about prime divisors of low
straight-line-complexity values. Both the combined mass claim and the
two-gate class obstruction remain open.

## One visible binomial in the one-call no-output slice

The first visible-addition boundary is settled under a narrower frozen
protocol: each tape sees only length, advice, and tape bits, forms
`b=1+a`, makes one unretained product-difference gcd whose factors are `a`
or `b`, and has neither prior tags nor target output.

For every prime `r=1 mod 3`, choose the least nontrivial cube root `alpha_r`.
Then

```text
1+alpha_r=-alpha_r^2,
alpha_r^u(1+alpha_r)^v=1
  iff v=0 mod 2 and u+2v=0 mod 3.
```

The criterion is identical in every characteristic in the pool. Pairing
canonical primes from this class and taking the CRT lift of their local roots
therefore makes every legal product equality true at both factors or false at
both factors. Every gcd is `WHOLE` or `ONE`, so proper-factor probability is
exactly zero for every tape.

An elementary Euclid-style construction proves that primes `1 mod 3` occur
beyond every bound. Recursively choosing the least two beyond the preceding
semiprime gives an effective canonical family with strictly increasing actual
bit lengths. The exact `N=91`, `a=16`, `b=17` replay checks 6,561 bounded
exponent quadruples, including list semantics and mutation rejection, but the
infinite theorem rests on the displayed identity rather than the finite box.

This cubic-torsion route crosses visible addition only for the one-call,
no-output slice. The separate low-L1 theorem now covers adaptive multiple
calls, unrelated visible sparse numerators, ordinary sparse-rational
operations, and target output below its expansion-entropy threshold. Retained
handles, high-L1 compressed products, and integer factoring remain open. The
cubic route does not revive the refuted 32-site rank-one argument: that finite
code installed different local kernels, whereas this canonical infinite pool
has the same complete six-torsion relation kernel at every site.
