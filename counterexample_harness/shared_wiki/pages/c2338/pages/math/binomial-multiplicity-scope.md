---
title: Exact binomial multiplicity scope
description: Counting convention, verified examples, row-window bounds, lower-index restrictions, and prime-support constraints for Problem 849.
---

# Exact binomial multiplicity scope

For a positive integer `a`, the project counts

`P(a)={(n,k): n,k positive, 1<=k<=floor(n/2), C(n,k)=a}`

and sets `m(a)=|P(a)|`.  For `a>=2`, remove the always present `(a,1)`
and write `S(a)=P(a)\{(a,1)}`; then `m(a)=1+|S(a)|`.  The input `a=1`
has no counted occurrence.

The exact campaign certificate lists:

- `P(2)={(2,1)}`;
- `P(6)={(4,2),(6,1)}`;
- `P(120)={(10,3),(16,2),(120,1)}`;
- `P(3003)={(14,6),(15,5),(78,2),(3003,1)}`.

Completeness is finite for each fixed value because
`C(n,k)>=C(n,1)=n` in the left half, so a solution of `C(n,k)=a` has
`n<=a`.

## Collision mechanisms and support limits

- Lind 1968, Section 5 and Theorem 7
  ([official scan](https://www.fq.math.ca/Scanned/6-3/lind.pdf)),
  classifies every adjacent-row equality `C(n,k)=C(n-1,k+1)` by a
  Fibonacci/Pell parametrization with source parameter `s>=1`.
  Its `s=1` term has `(n,k)=(2,0)` and lies outside the campaign domain
  `k>=1`, so campaign-admissible members begin exactly at `s=2`.
  The source identifier is MR0231784, with the precise result in
  Section 5, equations (5)-(7), Theorem 7 and the concluding paragraph,
  pp. 91-93.  It classifies only that geometry and does not exclude
  other diagonals.
- Bugeaud-Mignotte-Siksek-Stoll-Tengely 2008, Theorem 1.2
  ([doi:10.2140/ant.2008.2.859](https://doi.org/10.2140/ant.2008.2.859)),
  completely solves the `(2,5)` diagonal intersection.  The positive
  nontrivial values are 3003 and 11628.  It gives no information about
  a third lower index.
- Jenkins 2016, Theorem 1
  ([arXiv:1411.4111v1](https://arxiv.org/abs/1411.4111v1)), proves
  finiteness for each fixed unequal pair of row/diagonal offsets.  The
  balanced adjacent family is excluded, and the theorem is not uniform
  over offsets.
- Matomaki-Radziwill-Shao-Tao-Teravainen 2022, Theorem 1.3 and
  Remarks 1.5 and 1.7
  ([arXiv:2106.03335v1](https://arxiv.org/abs/2106.03335v1)), bounds
  sufficiently large coefficients only in the stated interior region.
  It leaves the small-`k` region containing the known Diophantine
  collisions.  Remark 1.7 says the sufficiently-large threshold is
  effective but supplies no numerical value; the separate ineffective
  observation in Remark 1.5 concerns a Siegel-theorem reduction in the
  small-`k` region, not Theorem 1.3.

At commit
[`9cfb265`](https://github.com/teorth/erdosproblems/commit/9cfb265f9fa57390908d80624d61b9551d454398),
the maintained Erdős Problems data marked Problem 849 open at the
2026-08-27 audit cutoff.  Neither that status nor the lack of a
maintained `t>=5` example proves nonexistence.

## Retired compatibility obstruction

The global pair of lemmas

1. `|S(a)|=4` forces an adjacent-row edge; and
2. an adjacent-row edge forces `S(a)` to consist of its two endpoints

would exclude `m(a)=5`.  The second lemma is exactly false at `a=3003`:
`(15,5),(14,6)` are adjacent, while `(78,2)` is an additional
nontrivial occurrence.  This retires that route but says nothing about
whether `m(a)=5` is realizable.

The strongest current scope boundary is therefore structural: known
interior and fixed-curve results do not supply a uniform all-`k`
compatibility obstruction.

## Prime-factor row window

For `a>=2`, write `p+(a)` for the largest prime divisor of `a` and
`N(a)=max{n:C(n,2)<=a}`.  Every nontrivial occurrence `(n,k)` satisfies

`p+(a)<=n<=N(a)`.

The upper bound follows from `C(n,2)<=C(n,k)=a`.  For the lower bound,
`C(n,k)` divides `n!`, so every prime divisor of `a` is at most `n`.
Strict row monotonicity permits at most one occurrence per row.  Thus

`|S(a)|<=max(0,N(a)-p+(a)+1)`.

Any multiplicity-five value must therefore satisfy
`p+(a)<=N(a)-3`.  In particular, if `q>=5` is prime, then
`N(C(q,2))=q` and `p+(C(q,2))=q`, giving the exact infinite family

`P(C(q,2))={(C(q,2),1),(q,2)}`.

The complementary region `p+(a)<=N(a)-3` remains unresolved and
contains `3003`; the theorem does not prove that `t=5` is impossible.

An exact merged-stream search found no `m(a)=5` for `a<=10^18`.
This is recorded only as a finite search boundary, not as
nonexistence evidence.

## Near-prime band

The subsequent theorem in `research/near_prime_band.md` proves the
stronger statement

`N(a)<2p+(a) => |S(a)|<=1`.

The key is the coefficient-size bound
`a<C(2p,2)`.  For `p>=17`, an occurrence with `k>=3` would instead
give `a>=C(p,3)>C(2p,2)`, so only the unique possible `k=2`
occurrence remains.  An exact exhaustive certificate handles
`p in {2,3,5,7,11,13}` and again finds at most one nontrivial
occurrence.

The first-order p-adic strategy is not itself valid.  The exact local
configuration

`p=89`, `(d,k)=(0,42),(1,40),(2,25),(3,18)`

has strictly decreasing lower indices, valuation one, and common unit
`C(p+d,k)/p == 36 (mod p)` at all four pairs.  Its four coefficients
are unequal, so it refutes only the proposed local obstruction, not
the band theorem.

Consequently every possible multiplicity-five value now lies in the
strictly smaller global region

`2p+(a)<=N(a)`.

This remains an all-`a` obligation; the campaign has not proved
`m(a)!=5` globally.

## Multiplicity-smoothness boundary

For every `a>=2` and every integer `t` with `2<=t<=m(a)`, the proof in
`research/multiplicity_smoothness.md` gives

`C(p+(a),t)<=a`.

Indeed, the `t-1` nontrivial occurrences have distinct lower indices
at least two, so one has lower index `k>=t`.  Its row satisfies
`p+(a)<=n`, and monotonicity gives

`C(p+(a),t)<=C(n,t)<=C(n,k)=a`.

If `p+(a)<t`, the first binomial coefficient is zero by convention, so
the assertion includes that boundary case.

Thus every possible multiplicity-five value satisfies

`C(p+(a),5)<=a<C(N(a)+1,2)`

and therefore

`p+(a)<=4+(120a)^(1/5)
        <4+(60N(a)(N(a)+1))^(1/5)`.

This is strictly stronger than the near-prime exclusion.  For every
prime `q>=11`, the value `a=2q^2` has largest prime divisor `q` and
`N(a)=2q`, so it lies outside the strict near-prime premise.  But
`C(q,5)>2q^2`, and the smoothness theorem excludes `m(a)>=5`.
Consequently an infinite subset of the previous residual region is
removed.

The unresolved region consists of values satisfying both
`2p+(a)<=N(a)` and `C(p+(a),5)<=a<C(N(a)+1,2)`.  This remains a
necessary-condition reduction, not a proof that multiplicity five is
impossible.

## Largest-prime-power row window

Write `p=p+(a)`, `e=v_p(a)`, and `Q=p^e`.  The proof in
`research/prime_power_row_window.md` strengthens every nontrivial
occurrence `(n,k)` to

`k<p` and `Q<=n<=N(a)`.

The `k<p` step uses exactly Sylvester's 1892 theorem that a consecutive
sequence whose first term exceeds its number of terms has a term
divisible by a prime larger than that number.  For the numerator block,
`n-k+1>=k+1` supplies the strict hypothesis.  The primary locator is
J. J. Sylvester, *On Arithmetical Series*, reprinted in *Collected
Mathematical Papers*, vol. IV, paper 72, Section 2, p. 690, Internet
Archive ARK `ark:/13960/t50g3m65p`.

Because `k<p`, the denominator `k!` contains no `p`, and the length-`k`
numerator block contains exactly one multiple of `p`.  That term has
valuation `e`, so it is at least `Q`.  The whole block is `p`-smooth.
It follows that

`|S(a)|<=max(0,N(a)-Q+1)`

and, for `2<=t<=m(a)`,

`C(Q,t)<=a`.

Thus a multiplicity-five value must satisfy

`Q<=N(a)-3` and `C(Q,5)<=a`,

with all four numerator blocks `p`-smooth.  This is strictly stronger
than the previous deep-smooth condition: for every prime `q>=5`,
`a=2q^5` satisfies `2p+(a)<=N(a)` and
`C(p+(a),5)<=a<C(N(a)+1,2)`, but has `Q=q^5>N(a)` and therefore
exactly `m(a)=1`.  The remaining prime-power residual region is still
open, so this theorem does not settle `C-T5`.

## All-primary-power row window

Define the largest primary component of `a` by

`R(a)=max_{q|a} q^{v_q(a)}`.

The proof in `research/all_primary_power_row_window.md` applies
Legendre's factorial-valuation formula separately to every prime
`q|a`.  In

`v_q(C(n,k))=sum_{j>=1}
  (floor(n/q^j)-floor(k/q^j)-floor((n-k)/q^j))`,

each summand is zero or one, and it vanishes when `q^j>n`.  Therefore
`v_q(C(n,k))<=floor(log_q n)` and hence
`q^{v_q(a)}<=n`.  Taking the maximum over all prime divisors gives

`R(a)<=n<=N(a)`

for every nontrivial occurrence.  It follows that

`|S(a)|<=max(0,N(a)-R(a)+1)`

and, for every `2<=t<=m(a)`,

`C(R(a),t)<=a`.

Thus every multiplicity-five candidate must satisfy

`R(a)<=N(a)-3` and `C(R(a),5)<=a`.

This strictly strengthens the reviewed largest-prime-power residual.
For every integer `E>=4`, `a=7*2^E` has largest-prime primary power
`Q=7` and satisfies all previous residual inequalities, while
`R(a)=2^E` and

`C(2^E,2)>7*2^E`.

Hence `R(a)>N(a)`, so the new theorem gives the exact conclusion
`m(a)=1`.  The narrower all-primary residual is still open; this is a
necessary-condition reduction, not a proof of `C-T5`.

Independent review confirmed the theorem and the full strictness
family.  As a boundary check, exact evaluation at `a=112` gives
`N(112)=15<R(112)=16` and `m(112)=1`; this sample supports but is not
needed by the universal argument.

## Lower-index-six exclusion

For nonempty `S(a)`, define

`K(a)=max{k:(n,k) in S(a)}`.

A proof in `research/lower_index_six.md`, now independently reviewed,
establishes, conditional on three complete published classifications,

`m(a)=5 => K(a)>=7`.

If `m(a)=5` and `K(a)<=6`, the four distinct nontrivial lower indices
must be one of the five four-element subsets of `{2,3,4,5,6}`.  Three
contain `{2,5}` and are reduced by the reviewed BMSST-2008
classification to `a=3003` or `11628`; their exact multiplicities are
`4` and `3`.

The set `{2,3,4,6}` contains a `(2,3)` collision.  Avanesov,
Acta Arithmetica 12 (1967), pp. 409-410,
DOI `10.4064/aa-12-4-409-420`, proves that the only common triangular
and tetrahedral values are

`1,10,120,1540,7140`.

Exact full enumeration of `P(a)` for those five values gives
multiplicities `0,2,3,3,3`.

The remaining set `{3,4,5,6}` contains a `(3,4)` collision.  From

`binomial(Y,3)=binomial(X,4)`

put

`u=Y-2`, `v=X(X-3)/2`.

Then `v(v+1)=u(u+1)(u+2)`.  Mordell,
Pacific Journal of Mathematics 13 (1963), pp. 1347-1351,
DOI `10.2140/pjm.1963.13.1347`, proves that the complete integer list
has `u in {-2,-1,0,1,5}` with the corresponding values recorded in
the source.  Left-half rows require `u>=4` and `v>=20`, while the only
source solutions with `u>=4` are `(u,v)=(5,14),(5,-15)`.  Thus no
left-half `(3,4)` collision exists.

`research/lower_index_six_certificate.py` exactly checks both variable
recoveries, all five lower-index sets, and every finite candidate
occurrence set.  The certificate is complete relative to the cited
classifications; it is not a finite-search claim about the two
unbounded curves.

Jacobian 0.14.0 has no installed Mordell--Weil basis, height-bound, or
complete integral-point operation.  The bounded typed operation
`algebraic_geometry.affine_plane_curve.check` only confirmed that the
exact `(2,3)` polynomial is a valid degree-three affine curve.  It is
not used for point completeness.

Independent review confirmed the Avanesov and Mordell source
attributions, reused the previously reviewed BMSST classification,
reran the exact certificate, and accepted the five-set implication.
The all-primary residual frontier therefore has `K(a)>=7`; `C-T5`
itself remains open.

## Seven-prime support and exact primary offsets

For

`R(a)=max_{q|a} q^v_q(a)` and `s=omega(a)`,

the factorization of `a` gives `a<=R(a)^s`.  Under the contrary
assumption `m(a)=5` and `s<=6`, let `(n,K)` be the occurrence with
maximum nontrivial lower index.  The reviewed all-primary row window
and the left-half convention give

`C(max(R,2K),K)<=a<=R^6`.

The exact monotonicity argument in
`research/support_capacity_seven.md` first forces `K<=16`.  Reusing
the reviewed certificate `a<=10^18 => m(a)!=5` then gives `R>1000`,
which forces `K=7`.  The adjacent exact threshold

`C(5060,7)<5060^6`, `C(5061,7)>5061^6`

finally yields

`1000<R<=5060` and `1001<=n<=5060`.

`research/support_capacity_seven_certificate.py` exactly factors all
4060 values `C(n,7)` on this interval.  It computes Legendre
valuations over the complete prime basis through 5060, verifies each
factor's primality by trial division, and checks every prime-power
product against the exact binomial value.  The minimum distinct-prime
count is seven and there is no row with count at most six.  Thus the
analytic reduction plus the exhausted finite kernel, now independently
reviewed, proves

`m(a)=5 => omega(a)>=7`.

This is not a larger finite search for `m(a)=5`, and it does not prove
`C-T5`.  A single pinned Jacobian factorization of the minimum-support
row `n=1439` matches the project certificate but is only a bounded
cross-check; full completeness comes from the exact project program.

There is also a direct exact-offset consequence.  If `m(a)=5`,
`q>K(a)` is prime, and `e=v_q(a)`, each of the four nontrivial
numerator blocks has length less than `q`.  Its denominator is
`q`-free, so the block has exactly one `q`-divisible term, of valuation
exactly `e`.  For an occurrence `(n,k)`, its unique offset is

`d=n mod q^e`, `0<=d<k`,

with `v_q(n-d)=e`.  Hence the full primary component has one exact
position in every block.  Together with `omega(a)>=7`, this gives at
least three primes `q>K(a)` when `K(a)<=10`, and at least two when
`K(a)<=12`.

Independent review confirmed the analytic thresholds, all 4060 exact
factorizations, and the complete-primary offset argument.  The four
support-capacity and primary-offset nodes are therefore reviewed
results.

## Three primes above the maximum lower index

The proof in `research/three_large_primes.md` applies Theorem 1 of
Laishram--Shorey, *Acta Arithmetica* 113 (2004), pp. 327--341,
DOI `10.4064/aa113-4-3`, with the exact locator at pp. 327--329,
equations (3), (6), (7).  For the maximum-lower-index occurrence
`(N,K)`, put `s=N-K+1`.  Since `N>=2K`, one has `s>K`, and

`Delta(s,K)=K!*C(N,K)=K!*a`.

Every prime at most `K` occurs in `Delta`, while a prime `q>K` does
not occur in `K!`.  Hence the number of prime divisors of `a` above
`K` is exactly `omega(Delta)-pi(K)`.  Outside the source's explicit
exception set, its theorem gives at least

`floor(3*pi(K)/4)-1+delta(K)`,

which is at least three for every `K>=7`.

`research/three_large_primes_certificate.py` transcribes all 23 `S1`
templates and 63 `S2` templates, expands them to 199 distinct pairs,
and exactly factors every corresponding `C(s+K-1,K)`.  There are 180
applicable pairs with `K>=7`.  Exactly nine have fewer than three
prime divisors above `K`, and their largest coefficient is
`C(30,7)=2035800`.  Thus all nine lie inside the already reviewed
`a<=10^18` exclusion; that search was neither rerun nor enlarged.
Every other applicable exception has at least three large primes.

Independent review of the source statement, all 199 expanded
exceptions, the exact factorizations, and the implication proves

`m(a)=5 => #{q prime:q|a and q>K(a)}>=3`.

Combined with the reviewed exact-offset lemma, a hypothetical
multiplicity-five value has three distinct complete primary components
whose exact offsets must hold simultaneously in all four nontrivial
numerator blocks.

## Finite-primary local realizability

The elementary CRT theorem in
`research/local_primary_realizability.md` shows that those finite local
conditions alone cannot be an obstruction.  More generally, fix any
distinct lower indices

`2<=k_1<...<k_r<=K`,

any finite set of distinct primes `q_j>K`, arbitrary exponents
`e_j>=1`, offsets `0<=d_ij<k_i`, and nonzero target units
`u_j mod q_j`.  For one row and prime, writing

`n=d+q^e m`

gives the exact congruence

`C(n,k)/q^e == m*(-1)^(k-1-d)/(k*C(k-1,d)) (mod q)`.

The denominator is a unit because `k<q`.  Thus an arbitrary `u_j` is
obtained by prescribing `m mod q`, equivalently one residue for `n`
modulo `q_j^(e_j+1)`.  CRT combines all primes independently for each
row.

Inside each resulting row residue class, representatives can be chosen
within a bounded distance of the real solution to `C(x,k_i)=X`.
As `X` tends to infinity, all resulting coefficient ratios tend to
one.  Choosing row `i` from `i` nearby representatives avoids the
`i-1` previously selected coefficient values, so the coefficients
remain pairwise unequal.  The asymptotics

`x_i~(k_i!X)^(1/k_i)`

also force the correct reverse row order for increasing lower
indices.

The exact certificate
`research/local_primary_realizability_certificate.json` checks four
rows at lower indices `2,3,5,7` for primes `11,13,17`, exponents
`1,2,3`, and common per-prime units `3,5,7`.  It verifies every exact
offset and valuation, a common coefficient image modulo

`11^2*13^3*17^4=22202972077`,

strict reverse row order, pairwise inequality, and relative spread
below `10^-6`.  A bounded Jacobian CRT operation independently matches
the first row's residue.

This retires the finite-primary first-order congruence obstruction,
not the multiplicity-five residual.  The certificate's four
coefficients are unequal.  The open claim
`L-T5-THREE-PRIMARY-OFFSET-RESIDUAL` still requires their exact integer
equality, together with the global all-primary conditions.  Any
successful remaining obstruction must therefore use exact-equality or
global smooth-block/S-unit compatibility; `C-T5` remains open.

Independent review accepted this finite-primary theorem and its exact
certificate.  Its proof-graph node is therefore reviewed, not merely an
Engineer-level construction.

## Global valuation fingerprint and canonical stripping

Suppose several nontrivial left-half rows satisfy
`C(n_i,k_i)=a`, put `K=max_i k_i`, and write

`Delta_i=product_(0<=h<k_i)(n_i-h)=k_i!*a`.

For every prime `p>K`,

`v_p(Delta_i)=v_p(a)`

in every row.  Define

`L_K(a)=product_(p>K)p^v_p(a)`, `b=a/L_K(a)`,

`lambda_(i,h)=product_(p>K)p^v_p(n_i-h)`, and
`u_(i,h)=(n_i-h)/lambda_(i,h)`.

Within one block, no prime above `K` can divide two terms.  Hence the
`lambda_(i,h)` are pairwise coprime and multiply to the same `L_K(a)` in
every row.  Every `u_(i,h)` is `K`-smooth and

`product_h u_(i,h)=k_i!*b`.

The exact consecutive and cross-row identities are

`lambda_(i,h)u_(i,h)-lambda_(i,h+1)u_(i,h+1)=1`,

`k_j!*Delta_i=k_i!*Delta_j`, and

`k_j!*product_h u_(i,h)=k_i!*product_g u_(j,g)`.

Also

`Delta_i*Delta_j/(k_i!*k_j!)=a^2`,

so `Delta_i*Delta_j` and `k_i!*k_j!` have the same squarefree kernel.

The exact `a=3003` control has `K=6`, `L_K=1001`, `b=3`, and checks all
these identities on its three nontrivial rows.  Its length-5 and length-6
windows overlap, so left-half order does not imply disjoint blocks.
This control shows compatibility at three lower indices; it is not a
four-row construction or a nonrealizability proof.

The primary-source audit in
`research/global_valuation_fingerprint.md` found no direct global
exclusion.  Tao's arXiv:2603.27990v2 results relevant here are
asymptotic exceptional-set/anatomy bounds, not emptiness.  The
Tengely-Ulas disjoint-block source chain concerns differently normalized,
often equal-length and genuinely disjoint products; even fixed-tuple
finiteness would not imply uniform all-`K` emptiness.  The
Evertse-Schlickewei-Schmidt theorem bounds nondegenerate solutions of one
fixed finite-rank linear equation by
`exp((6n)^(3n)(r+1))`; here the natural rank grows with `pi(K)` and the
group can require further generators when large-primary pieces are
absorbed into the variables.  A finite count is not an exclusion.

Thus direct use of those three theorem families is retired.  The canonical
stripped system is an exact universal reduction, but
`L-T5-GLOBAL-UNIFORM-BLOCK-EXCLUSION`,
`L-T5-THREE-PRIMARY-OFFSET-RESIDUAL`, and `C-T5` remain open pending a
deterministic global argument.

## Four-row row-gap primary constraint

For four hypothetical nontrivial representations, order the lower indices
as `k_1<k_2<k_3<k_4=K` and the rows as
`n_1>n_2>n_3>n_4`.  For each complete primary
`Q=q^v_q(a)` with `q>K`, the reviewed exact-offset theorem selects one
term

`x_i(q)=n_i-d_i(q)`

in every numerator window.  Hence

`Q | (n_i-n_j)-(d_i(q)-d_j(q))`,

and the six offset differences come from one four-tuple and satisfy the
cocycle identities.

Let

`F_ij(X)=product_(s=-(k_j-1))^(k_i-1)(X-s)`.

When two windows overlap, `F_ij(n_i-n_j)=0`.  Delete that one distinct
zero factor and call the resulting nonzero integer `R_ij`.  If `E_ij`
is the product of primaries whose selected term is literally common to
the two windows, then

`L_K(a)/E_ij | R_ij`.

Across four rows, equality of the selected terms has partition types
`4`, `3+1`, `2+2`, `2+1+1`, and `1+1+1+1`; their exact exponents after
multiplying the six pair constraints are respectively
`0,3,4,5,6`.  If `C` denotes the type-`4` mass, this gives

`(L_K(a)/C)^3 | product_(i<j)|R_ij|`.

For pairwise disjoint windows the stronger condition is

`L_K(a) | gcd_(i<j)(|R_ij|)`.

The part `C` is not an accounting artifact: it is exactly the
above-`K` primary part of the product of the terms in the fourfold
window intersection.  It divides `a`, and cancellation preserves

`Delta_i/C=k_i!*(a/C)`.

If the overlap graph is connected, let `B` be the largest diameter of
the union of two consecutive overlapping windows.  Then

`B<=2K-3`,

and every primary outside `C` is a first power of a prime in
`K<q<=B`.  Combining this with the independently reviewed theorem that
a multiplicity-five value has at least three primes above `K` proves
the following new branch exclusion:

`m(a)=5 and K(a)<=9 and connected overlap`

implies that the four windows have a common integer term.

The exact controls in
`research/row_gap_primary_resultant_certificate.json` cover the partial
overlap at `a=3003`, the disjoint `(2,5)` collision at `a=11628`, the
next campaign-domain Lind pair `C(104,39)=C(103,40)` where all
large-primary mass is common, and a deliberately unequal four-row
`2+2` offset configuration.  These controls are not a fourfold
binomial collision.  Independent review accepted the universal theorem
and the `K<=9` corollary.  `C-T5` remains open for the surviving
resultant/cancellation branches.

## Exact low-index common-intersection exclusion

For a hypothetical `m(a)=5` value, the four nontrivial representations have
strictly increasing lower indices and strictly decreasing row indices.
If their numerator windows share an integer `x`, write `n_i=x+d_i`.  Then

`0<=d_i<k_i`, `d_1>d_2>d_3>d_4`,

and the left-half condition gives

`x>=max_i(2k_i-d_i)`.

Using the reviewed `K>=7` theorem and restricting to `K<=9`, the complete
parameter space has 65 raw lower-index sets, 15 admissible lower-index sets,
and 45 lower-index/offset tuples.  Equality of the smallest- and
largest-lower-index coefficients gives 15 distinct integer polynomials after
the universal factor `x` is removed.  Each has leading coefficient `-1` and
nonzero constant, so every integer root divides that constant.

The exact certificate in
`research/k9_common_intersection_certificate.json` scans every resulting
integer root range, whose largest endpoint is `77616`.  The union of all
positive integer roots is `{1,2}`, while every left-half configuration has
`x>=14`.  Hence no `K<=9` fourfold-common system exists.  Combining this
with the reviewed row-gap corollary forces every hypothetical
`m(a)=5`, `K(a)<=9` system into disconnected overlap.

A bounded typed Jacobian root-isolation call on one representative polynomial
returns the same singleton integer roots `1,2`; the project certificate,
not that call, establishes completeness.  Independent review accepted both
the common-intersection exclusion and its connected-overlap consequence.
The disconnected-overlap and `K>=10` branches remain open, so this is not a
proof of `C-T5`.

## Uniform common-anchor block reduction

For the unbounded common-intersection branch, shift any common anchor by the
smallest offset so that the smallest row is the anchor itself.  With

`K=k_4`, `y=x-K`, `h=K-k`,

every smaller equal representation is then exactly equivalent to

`product_(r=1)^(h+d)(y+r)`

` = [K!/(K-h)!] product_(r=1)^d(y+K+r)`,

where `y>=K`, `h,d>0`, and `h+d<K`.  Four equal representations would give
three coordinatewise increasing nonzero pairs `(h,d)` satisfying this one
equation for the same `y,K`.

Taking quotients between successive pairs gives three consecutive-product
block equations.  Their row-gap/lower-index slopes `b/a` must be strictly
increasing.  If `s=a+b`, polynomial reduction also gives

`Y | s!-(L+b)!/(L-a)!`,

`Y+s | L!/(L-s)!`,

and

`Y+L+r | (L+r-1)!/(L+r-1-s)!` for `1<=r<=b`.

These are universal necessary conditions, not an exclusion.  The exact
integer blocks

`(48,26;7,1)`, `(56,19;6,1)`, `(63,13;5,2)`

satisfy the full domain, strictly increasing slopes, and every displayed
divisibility, while all three original product equalities fail.  Thus the
ratio/strict-convexity and endpoint-divisibility mechanism is insufficient.

One fixed geometry can be eliminated uniformly.  For pairs `(h,d)=(1,1)`
and `(2,2)`, the exact resultant in `y` is

`-K^3(K-1)(25K^2-35K-14)`,

which is nonzero throughout the admissible integer domain `K>=5`.  The
project certificate computes the Sylvester determinant independently and a
bounded typed Jacobian resultant agrees.  This does not extend to arbitrary
unbounded pairs, whose elimination polynomials vary with the geometry.

The remaining claim is exactly the nonexistence of three simultaneous
block-product equations above.  Neither that claim nor its negation is
proved.  The ratio/divisibility/resultant route is therefore retired, while
the uniform common-anchor exclusion and `C-T5` remain open.

### Exact zero-set sign boundary

For fixed `y,K`, the exact ratio matrix is a positive row/column scaling of
the Hankel moment kernel

`m_(h+d)=(y+1)_(h+d)`.

The gamma-integral representation proves that every admissible minor of this
kernel is strictly positive.  Also, every mixed logarithmic forward
difference has alternating sign; in particular, both mixed differences of
total order three are negative.

Neither fact bounds the level-one set.  Positive row scaling preserves strict
total positivity, but

`(y+1)_(h+d)/(y+1)_(2h)=1`

at every `(h,d)=(h,h)`.  Mixed differences are likewise blind to the
corresponding additive row term.  For the actual level-shifted common-anchor
kernel at `(y,K)=(9,8)`, the order-three minors on rows `(1,2,3)` and columns
`(1,2,3)` and `(1,3,4)` are exactly

`3436012800` and `-521340019200`.

Thus it is not sign-regular of order three, and total positivity,
third-difference signs, or their standard variation-diminishing consequences
cannot alone prove the three-zero residual.

Full-equation elimination does settle the unique shortest geometry.  Three
strictly increasing positive block slopes have total length at least eight,
with unique minimizer

`(a,b)=(2,1),(1,1),(1,2)`.

The cumulative zero coordinates are `(2,1),(3,2),(4,4)`.  Their exact
Groebner basis contains

`K^2(K-1)^2(K-2)`,

so this geometry has no admissible root.  Any exact three-zero system must
therefore have `h_3+d_3>=9` and `K>=10`.  This is an exact fixed-geometry
exclusion, not a finite-search conclusion; the unbounded geometries and the
uniform common-anchor claim remain open.  The proof and replayable typed
elimination are in `research/common_anchor_exact_zero_set.md` and its
companion artifacts.

### Full factorial-ratio curvature and secant boundary

The exact Gamma continuation of the normalized common-anchor equation has a
unique real zero graph `d=f(h)` on the complete triangular arc.  With

```text
t=K-h,
u=y+h+f(h)+1,
v=t+1,
w=u+t,
A=psi(u)-psi(v),
B=psi(w)-psi(u),
```

implicit differentiation, including both endpoints, gives

```text
f'=A/B,
f''=[psi_1(v)+psi_1(u)(1+f')^2-psi_1(w)(f')^2]/B
   >2/(K-h)>2/K.
```

For three integer graph points with successive increments `(a,b)` and
`(c,e)`, strict convexity gives the positive integer area
`Delta=ae-bc` and an exact intermediate point with

```text
f''(xi)=2Delta/[ac(a+c)].
```

Optimizing this expression over the full triangular lattice gives the sharp
domain-only threshold `2/Q_K`, where

```text
Q_K=(K-5)floor((K-5)^2/4)  for even K,
Q_K=(K-6)floor((K-6)^2/4)  for odd K.
```

Since `Q_K>K` for every `K>=10`, the global small-curvature inequality
needed by this unlocalized primitive-area argument is uniformly false.
Curvature augmented by new arithmetic localization is not excluded.

The obstruction occurs on exact real zeros of the full kernel.  If `y=K`
and `16|K`, the terminal-ratio estimate

```text
exp q(K/4)<[(5/3)(8/11)^3]^(K/4)
          =(2560/3993)^(K/4)<1
```

puts `K/16,K/8,3K/16` inside the triangular zero arc.  The corresponding
exact real Gamma zeros have oriented secant area

```text
A_K>K^2/2048>=2  for K>=64.
```

Thus the complete real zero equation cannot itself force a uniform
three-point area below the integer lattice unit.  The missing condition is
integrality of the ordinates, which is arithmetic rather than a sharper
curvature constant.

The complementary complete-log determinant also has no uniform sign.  For
the fixed cumulative pairs

```text
(h,d)=(2,1),(3,3),(4,8),
```

whose successive slopes are `1/2<2<5`, exact rational Taylor bounds prove
for every `K>=2^20`

```text
D(K,K)>0,
D(K,K^2-K)<0.
```

Thus the determinant vanishes at an intermediate real Gamma parameter and
cannot support a parameter-uniform fixed-sign proof.  This does not prove
vanishing at an integer `y`, and none of the three displayed points is an
exact product zero.  The universal three-zero residual and a multiplicity
counterexample remain open.  The proof and replay are in
`research/common_anchor_factorial_ratio_three_zero_boundary.md` and its
companion artifacts.

### Interior reduction to a finite remainder

The full common-anchor product equality gives a stronger uniform reduction.
For one non-anchor representation write `k=K-h`.  Splitting the equality
after its first `h` factors gives

`product_(i=1)^h (y+i)/(K-i+1)`

` = product_(r=1)^d (1+k/(y+h+r))`,

with `d<k`.  If `k<=K/4`, the left side has at least
`floor(K/4)` factors at least `2`, while every right factor is below `5/4`
and there are fewer than `k` of them.  This is impossible, so `k>K/4`.
If `y>=K^2`, the left side exceeds `K`, while the right side is below
`(1+1/K)^K<3`, again impossible for `K>=4`.  Hence

`k>K/4`, `y<K^2`, and `n<2K^2`

for every one of the four representations.

Take `epsilon=1/12`.  If `log K>=432`, then

`(log n)^(3/4)<(3 log K)^(3/4)<=log K/2`,

so

`exp((log n)^(3/4))<sqrt(K)<K/4<k<=n/2`.

Also the common value satisfies
`binomial(y+K,K)>=binomial(2K,K)>=2^K`.  MRSTT Theorem 1.3 therefore
contradicts four left-half solutions once both `log K>=432` and the
source's sufficiently-large coefficient threshold hold.  Thus all
fourfold common-anchor collisions form a finite set of normalized tuples.

This is not an exclusion.  Remark 1.7 says the MRSTT threshold is effective,
but the paper does not state its numerical value and the present reduction
does not extract the hidden constants.  Consequently no explicit `K` cutoff
or exhaustive finite-remainder certificate is currently available.  The
proof and exact controls are in
`research/common_anchor_interior_reduction.md` and its companion artifacts.

### Effective-threshold audit boundary

Direct inspection of `arXiv:2106.03335v1` identifies the first missing
numerical interface at Proposition 1.9: its distance estimate has an unnamed
`<<_epsilon` constant.  The deduction of Theorem 1.3 then retains an
unspecified `O`-constant.  Internally, Corollary 2.3 uses an unstated starting
range to obtain its strict curvature inequality, Lemma 3.1 compares `>>` and
`O` scale counts without constants, and Proposition 4.2 uses an unspecified
absolute exponent and starting range.  The v1 Type I display also has
`(1+F)^c` where the cited estimate supplies `(1+F)^(-c)`, so a numerical audit
must first correct that apparent sign typo.

The exponent choices themselves are not the blocker.  At `epsilon=1/12`,
taking the distance parameter `1/240` gives
`(4/3)(2/3+1/240)=161/180<9/10`, but the source does not say when that
comparison dominates its hidden constants.  Therefore the
published-proof-plus-enumeration route has no executable remainder.  It is
retired unless a new explicit-constants proof supplies a concrete threshold
and every smaller tuple is actually certified.

The exact first-edge family confirms that individual collisions cannot simply
be cut off: `(h,d)=(1,1)` is equivalent to
`X^2-5Z^2=-4` and contains the reviewed infinite Lind family.  These are
one-block collisions, not three-block counterexamples.  The source audit,
Pell transform, and bounded typed Jacobian factorization are in
`research/common_anchor_effective_closure.md` and its companion artifacts.
The universal three-block claim remains open.

### Proposition 1.9 explicit-reproof boundary

The complete official source archive for `arXiv:2106.03335v1` is now pinned
under `research/common_anchor_prop19_explicit_source.tar.gz`; it contains
exactly `main.tex` and `main.bbl`.  The exact source hashes and original
Proposition 1.9 quantifiers are replayed by
`research/common_anchor_prop19_explicit_certificate.py`.

At distance parameter `epsilon=1/240`, the target exponent is `161/240`.
The scale exponent `107/160` and input exponent `3599/2400` have product
`1+1093/384000`, so the scale selection has strict exponent slack.  The
source's later use of `3/2-epsilon/2` is stronger than Lemma 3.1(i), but this
bookkeeping slip can be repaired by invoking Proposition 1.11 with parameter
`epsilon/20=1/4800`.  The common-anchor conversion remains exactly

`(4/3)(2/3+1/240)=161/180=9/10-1/180`.

The first unavailable numeral is earlier than any common-anchor enumeration.
MRSTT Lemma 4.1 cites Iwaniec--Kowalski Theorem 8.25 and states

`|S| <= C_8.25 alpha X exp(-2^(-18)(log X)^3/(log F)^2)`

with an unnamed absolute `C_8.25`.  With
`alpha=(log X)^(4A)`, obtaining even the local target
`X(log X)^(-2A)` requires

`2^(-18)(log X)^3/(log F)^2 >= log C_8.25+6A log log X`.

Neither the v1 source nor the cited theorem statement supplies a numerical
upper bound for `C_8.25`, so no numerical starting point `N_dist` is
certified.  Correcting the separate v1 Type-I sign from `(1+F)^c` to the
apparent intended decay `(1+F)^(-c)` would not fill this gap.  This retires
only constant extraction from the stated citation interface; an independent
constant-tracking reconstruction of the underlying Vinogradov proof remains
a materially different possible route.  Proposition 1.9's explicit distance
claim, Theorem 1.3's threshold, and the common-anchor residual all remain
open.

### Proposition 1.9 repaired bottom-up constant boundary

The previous bottom-up conclusion overstated the obstruction.  Proposition
4.2 has two right-hand terms.  At `epsilon=1/240`, its high-frequency
Vinogradov envelope has decay `exp(-c(log X)^(1/120))`; this need only enter
the separate `X(log X)^(-A)` remainder.  It need not dominate `F^(-c)` at
the maximum permitted `log(F)` power `359/240`.  The earlier power comparison
is therefore withdrawn.

The two literal downstream defects are repairable.  The Type-I substitution
preserves `F` exactly and forces `(1+F)^(-c)`.  For `0<c<1`, the exact
Type-II row bound is

`sum_n (1+|n-n'|F/N_r)^(-c) <= 1+2N_r F^(-c)/(1-c)`.

The leading `1` contributes `O(K_r N_r polylog(P))` to the squared Type-II
sum, while the target has scale `K_r N_r^2 log(P)^(-30A)`.  Since the
Vaughan supports have `N_r>>P^(1/3)`, every fixed logarithmic loss is
eventually absorbed.  Thus neither the high-frequency term nor the Type-II
diagonal is a strategy-level obstruction.

The route still stops numerically at the source interface.  The IK Theorem
8.25 polynomial/bilinear core on pages 217--224 was not lawfully accessible
on this host; its statement gives `2^(-18)` but no numerical multiplicative
constant.  The explicit MRSTT wrapper only shows
`C_8.25<=C_core+6`, leaving `C_core` unknown.  IK Theorem 8.4 later leaves
its multiplier and `alpha`-loss exponent unstated, and the Vaughan
decomposition, PNT invocation, and downstream Fourier/covariance argument
also retain unnamed constants.  Hence no complete threshold `n0` can be
evaluated from the sources actually opened.

Conditional on such an `n0`, the endpoint conversion remains
`C_dist=1, N_dist=2n0`; no numerical pair is certified.  The corrected proof,
exact certificate, and typed Jacobian replay are in
`research/common_anchor_bottom_up_distance_repair_boundary.md` and its
companion artifacts.  This retires only numerical propagation from currently
available interfaces, not the repaired analytic strategy, Proposition 1.9,
or the common-anchor residual.

### IK 8.25 explicit-core reconstruction boundary

The next bounded reconstruction exposes all elementary losses around the
polynomial core. Put

```text
kappa=log(F)/log(X), R=10ceil(kappa), s=R+1,
V=floor(X^(1/4)), D=log(X)/(2^18 kappa^2).
```

The original derivative hypotheses imply that at least `R/100` indices in
`[21kappa/20,8kappa/5]` satisfy

```text
V^(-(199/100)r) <= |f^(r)(n)/r!| <= V^(-r/100).
```

The exact Taylor margin is `1399/16000`.  A common shifted block has endpoint
loss at most `V^2`, and the Taylor error is `<33/896`; together they cost less
than `2 alpha X exp(-D)`.  In the nontrivial range `D>log 2`,

```text
log(V)/(256R^2)
  > log(X)/(200000kappa^2)
  > D,
```

with exact rate gap `971/819200000`.  Thus a numerical multiplier `C_B>=1`
for the fully quantified moderate-coefficient bilinear estimate

```text
|sum_(x,y<=V) e(sum_(r=1)^R a_r(xy)^r)|
  <= C_B V^2 V^(-1/(256R^2))
```

would give, under the certificate's normalization,

```text
C_core=(3/2)C_B, C_V=C_core+2.
```

For the MRSTT phase each derivative cancellation set is one interval, so the
`R+1` required derivatives leave at most `R+2` clean components.  For every
explicit rational `A,B,C_V` and integer component count, the certificate gives
a monotone integer threshold.  Its direct nontrivial check at
`(A,B,C_V,m)=(1,1,10,2)` uses

```text
X_H=ceil(exp(2^3960)),
32768 > 19825
```

to verify the complete high-frequency inequality.

No checked lawful source supplies the required numerical `C_B`.  IK and
MRSTT leave it unnamed; Ford's explicit `9.463` applies only to the
logarithmic phase, and his displayed general mean-value ranges do not cover
every `R>=40` without a new deep constant audit.  Hence the bilinear
inequality is the first exact unclosed statement.  It is unproved, not
refuted.  The route boundary and replay are
`research/common_anchor_ik825_explicit_core_boundary.md` and its certificate.
No numerical `C_core,C_V,N_dist`, common-anchor exclusion, or counterexample
is claimed.

### `R=40` exact phase-lock and complete-moment boundary

The first direct decision pass does not settle the `R=40` bilinear
inequality.  It does close two narrower mechanisms exactly.

If an admissible degree-40 polynomial has

```text
|sum_(x,y<=V) e(P(xy))|=V^2,
```

then all phases agree.  The `x=1` terms make `P(n)-P(1)` integral at
`1,...,V`.  For `V>=41`, Newton interpolation in the basis
`binom(t-1,j)` puts every nonconstant monomial coefficient in
`(1/40!)Z`.  A moderate coefficient therefore forces

```text
V <= (40!)^(100/r).
```

The normalized ratio is consequently below
`(40!)^(1/4096)<2`; for `V<=40` it is also below `2`.  Thus exact phase
locking, including integer-valued-polynomial resonance, cannot yield an
unbounded counterfamily.

The standard two-Hölder complete-system Fejér-majorant route is also
quantitatively insufficient for the stated one-coefficient class.  With
complete-system weight `K=1+...+40=820`, diagonal solutions force the
mean-value defect `Delta_u>=max(0,820-u)`.  The target exponent would require

```text
r/100-Delta_u-Delta_v >= uv/(128*40^2).
```

A positive left side forces `u,v>=820`, but then the right side is at least

```text
820^2/(128*40^2)=1681/512>2/5>=r/100.
```

This contradiction retires only that complete-system moment scheme.  An
incomplete-system argument, a structured multi-coefficient argument, or a
different inverse theorem is not excluded.  In particular there is still no
numerical `C_40`, no universal `C_B`, and no unbounded exact counterfamily.
The proof and exact replay are
`research/common_anchor_ik825_r40_bilinear_boundary.md` and its companion
certificate and typed Jacobian records.

### `R=40` arbitrary-weight single-coordinate fiber boundary

Tracking only the controlled `r`-th power-sum coordinate cannot preserve a
power saving if every other phase is subsequently used only through its
modulus-one bound.  For arbitrary factorable base weights, put

```text
B=sum_(y,n<=V) w_(y,n)e(a y^r n^r),
Q=sum_(y<=V)|sum_(n<=V)w_(y,n)e(a y^r n^r)|^(2u).
```

The first Holder step is `|B|^(2u)<=V^(2u-1)Q`.  For every `1<=r<=40`,
every `V>=2`, and every fixed positive `u,v`, the admissible choice

```text
a=V^(-r),  w_(y,n)=e(-a(yn)^r)
```

gives `B=V^2`, `Q=V^(2u+1)`, and equality in Holder.  The powered
first-step bound needed for saving `1/(256*40^2)` then fails by the factor

```text
V^(uv/204800)/C_(r,u,v),
```

which is unbounded for every fixed constant.  On the merged fiber
`Delta_r=c`, the weight is exactly `e(-a y^r c)`, so multiplication by the
controlled character makes every fiber positive.  The ordinary Fourier
coefficient argument still gives `|F_c|<=|F_0|`; zero-fiber dominance is
valid but contains no remaining spacing cancellation.

These cancelling weights need not be generated by coefficients of degrees
`j!=r`.  The result therefore retires only the weights-only single-coordinate
mechanism.  An incomplete argument retaining the shared polynomial structure
of all uncontrolled coefficients, the original `R=40` bilinear inequality,
and numerical `C_40` remain open.  The proof and exact replay are
`research/common_anchor_ik825_r40_incomplete_fiber_boundary.md` and its
companion certificate and typed Jacobian records.

### Source-structured `F=X^4`, `R=40` bilinear bound

Restoring the complete MRSTT source class changes the bounded verdict.  With

```text
F=X^4, kappa=4, R=40, V=floor(X^(1/4)),
a_j=f^(j)(n)/j!,
```

the source condition gives

```text
alpha^(-j^3)X^4/n^j <= |a_j| <= alpha^(j^3)X^4/n^j
```

for every `1<=j<=40`, not merely a modulus-one remainder after one
coordinate is selected.  The interval
`[21kappa/20,8kappa/5]=[21/5,32/5]` has integer points exactly `5,6`.

For `q<=V^2`, the full polynomial derivatives of orders `5,6,7` differ
from `f^(k)(n)` by at most `1/16` relatively once `X>=2^110`.  This keeps
their signs and makes the fifth and sixth derivatives monotone.  Explicit
iterated van der Corput differencing then gives

```text
y<=V^(79/100):
  |sum_(x<=V)e(P_n(xy))|/V
  <=2^(53/16)(1+log V)^(1/4)V^(-3/10240),

y>V^(79/100):
  |sum_(x<=V)e(P_n(xy))|/V
  <=2^(103/32)(1+log V)^(5/32)V^(-973/80000).
```

Both exponents strictly exceed `1/409600`.  Their displayed constants are
absorbed for `V>=2^(2^20)`; below that threshold the trivial estimate is
absorbed because `2^20<3*409600`.  Hence the exact source class satisfies

```text
|sum_(x,y<=V)e(P_n(xy))| <= 8 V^2 V^(-1/409600).
```

The old cancelling weight cannot occur in this class: exact cancellation by
the missing degrees would force `a_5` or `a_6` into `(1/40!)Z`, whereas the
source upper bounds make it nonzero and smaller than `1/40!` in the large
range.  The proof and replay are
`research/common_anchor_ik825_r40_source_structured_bound.md` and its
companion certificate and typed Jacobian records.  This exact-source claim is
independently reviewed.  The broader arbitrary-coefficient `R=40` claim and a uniform
constant for all `R>=40` remain open.

### Uniform adaptive classical-differencing boundary

The reviewed `kappa=4` proof cannot be extended uniformly by selecting
adjacent derivative orders from

```text
21kappa/20<=k<=8kappa/5
```

on successive `y`-ranges and applying its pointwise classical differencing
lemma.  With `r=k-1`, that lemma contains the unavoidable term `1/H` with
`H<=V`; after taking the `2^r`-th root, its exponent is at most
`1/2^(k-1)`.

Put `n=ceil(kappa)` and `R=10n`.  On the first full ceiling interval
`(23,24]`, the minimum controlled order is `25`, and

```text
2^24=16777216>25600*24^2=14745600.
```

The minimum order increases by at least one on each subsequent ceiling
interval, while the quadratic right side grows by a factor below two.
Therefore, for every real `kappa>=23`,

```text
2^(k-1)>256R^2,
1/2^(k-1)<1/(256R^2).
```

No fixed constant absorbs that power mismatch as `V` tends to infinity.
Changing only the `y`-cuts or choosing neighboring controlled orders does not
alter the ceiling.  The range is nonvacuous: for fixed `kappa`, the functions
`f(t)=X^kappa log t` with `alpha=2` satisfy the complete source derivative
window once `X` is sufficiently large.

This is a method-specific nonclosure, not a counterexample to the uniform
source estimate.  A continuation needs cancellation across `y` or a
polynomial-strength mean-value input.  No uniform `C_B`, actual
`C_core,C_V`, or all-`kappa` high-frequency threshold follows.  The exact
argument and replay are
`research/common_anchor_ik825_uniform_source_boundary.md` and its companion
certificate and typed Jacobian records.

### `kappa=23` full-rectangle bivariate scalar A-process boundary

The first route that keeps the complete two-variable correlation still fails
at a precise, narrower interface.  Freeze

```text
F=X^23, kappa=23, R=230, V=floor(X^(1/4)),
1<=j<=231,
529 log(alpha)/log(X)<1/1000.
```

The controlled integer orders are exactly `25,...,36`.  With

```text
P_n(xy)=sum_(j=1)^230 f^(j)(n)(xy)^j/j!,
```

all coefficients remain in every correlation.  For `X>=2^822`, direct
source bounds show that `P_n^(k)` has the sign of `f^(k)(n)` with relative
error below `2^(-16)` for every `25<=k<=37`.

Apply two-dimensional translate-and-Cauchy with scalar shifts in either axis,
keeping the other axis inside every correlation.  After `d` scalar steps the
majorant contains its last zero or partial diagonal as `H_d^(-1)` at moment
power `2^d`.  A controlled order `k` cannot enter a terminal
first-derivative estimate before `d>=k-1`, so the optimal exponent over every
axis word, shift length, and controlled order is

```text
1/2^24.
```

It is strictly weaker than the target:

```text
1/(256*230^2)-1/2^24
  =3159/221878681600>0.
```

The exact family `X=2^(4m)`, `V=2^m`, `F=2^(92m)`, `alpha=2`,
`f(t)=F log t`, `m>=132251`, satisfies every source condition and makes this
power mismatch unbounded relative to any fixed constant.  This retires only
the scalar A-process that bounds zero and partial diagonals by support.  A
new polynomial mean-value estimate for those diagonals, the numerical
`C_23`, the source core itself, and the multiplicity counterexample remain
open.  Evidence is
`research/common_anchor_ik825_kappa23_bivariate_boundary.md` and its exact
certificate and typed Jacobian records.

### `kappa=23` terminal mixed-box partial-diagonal boundary

The proposed polynomial saving on the last partial diagonal fails for the
natural twelve-paired-round translation-box mean.  Each paired round applies
one `x` and one `y` phase difference, so twelve rounds have moment power
`2^24`.  Differences of translations from `{0,...,H-1}` carry their exact
triangular weights

```text
mu_H(t)=(H-|t|)/H^2,  |t|<H.
```

Fix eleven earlier nonzero shifts in both axes, write
`A=sum_i |h_i|`, `B=sum_i |l_i|`, and let `(h,l)` be the final pair.  In the
complete `2^24`-corner expansion, `h=0` pairs corners by flipping the last
`x` bit; the arguments of the full common phase `P_n(xy)` agree and the signs
are opposite.  The same holds for `l=0`.  Hence all terminal partial
diagonals have zero phase and the exact correlations are

```text
C(0,0)=(V-A)(V-B),
C(0,l)=(V-A)(V-B-|l|),
C(h,0)=(V-A-|h|)(V-B).
```

Their normalized triangular-weighted union is exactly

```text
1/(HV^2) [
  (2-1/H)(V-A)(V-B)
  -(H^2-1)/(3H)((V-A)+(V-B))
].
```

For `H=V/64`, every support side is at least `13V/16`, while the partial
union has weight `2/H-1/H^2>=1/H`.  Thus the mean is at least
`169/(256H)`.  It cannot have any further fixed positive power saving in
`V`, in particular not the required

```text
V^(-3159/13225),
(1+3159/13225)/2^24=1/(256*230^2).
```

The exact source family `X=2^(4m)`, `V=2^m`, `H=2^(m-6)`,
`F=X^23`, `alpha=2`, `f(t)=F log t`, `m>=132251`, satisfies all derivative
conditions through order `231`, so this is an unbounded source-class
obstruction rather than a finite experiment.  It retires only absolute or
nonnegative terminal mixed-box averaging.  Signed elimination,
distinct-nonzero-shift moments, numerical `C_23`, and the source core remain
open.  Evidence is
`research/common_anchor_ik825_kappa23_partial_diagonal_boundary.md` and its
exact certificate and typed Jacobian records.

### `kappa=23` truncated-divisor reindexing boundary

For every integer `V>=1`, the square-truncated divisor weight is exactly

```text
d_V(q)=#{x|q:ceil(q/V)<=x<=V},
sum_(q<=V^2)d_V(q)=V^2.
```

Pullback along `(x,y)->xy` is an isometric bijection from functions on the
weighted product set `(Q_V,d_V)` to arrays on `[1,V]^2` that are constant on
product fibers.  Therefore

```text
sum_(q<=V^2)d_V(q)e(P(q))=sum_(x,y<=V)e(P(xy))
```

and every estimate for one side is an estimate for the other with exactly the
same quantifiers, constant, and exponent.  Reindexing alone is not a new
analytic invariant.  Replacing `d_V` by the complete divisor function is also
not exact:

```text
S(P)=T_tau(P)-2 sum_(m>V, xm<=V^2)e(P(xm)).
```

The wing is nonempty for every `V>=2`.  Bag--Mazumder,
`arXiv:2408.02020v1`, Theorem 1.1, states a complete-`tau` estimate with a
leading-coefficient approximation, an unnamed implied constant, and an
`N^epsilon log N` loss; it does not state a derivative estimate for `d_V` or
control this wing.  The favorable hypothetical margin
`1/2^24-1/27084800=5033/221878681600` is consequently unused.  This retires
only reindexing plus an unsupported transfer of an unweighted or
complete-`tau` theorem.  A genuine truncated-weight estimate, numerical
`C_23`, and the source core remain open.  Evidence is
`research/common_anchor_ik825_kappa23_truncated_divisor_boundary.md` and its
exact certificate, primary-source excerpt, and typed Jacobian records.

### `kappa=23` qualitative Heath--Brown VMVT fiber bound

For the exact `F=X^23`, `R=230`, `V=floor(X^(1/4))` source class, retain
the complete phase and set

```text
g_y(x)=P_n(xy).
```

The reviewed full-phase estimate gives, for `X>=2^822`,

```text
(65535/65536)|f^(k)(n)|
 <= |P_n^(k)(q)|
 <= (65537/65536)|f^(k)(n)|,
```

with constant sign for `25<=k<=37` and `0<=q<=V^2`. Thus
Heath--Brown `arXiv:1601.04493v2`, Theorem 1, applies to every fiber with
`N=V`, derivative ratio at most `65537/65535`, and all 230 source
coefficients still present.

Take `epsilon=1/10000`, use `k=25` for `y<=V^(1/4)`, and use `k=31`
for `y>V^(1/4)`. The exact `lambda` envelopes are

```text
k=25:
  c_25 V^(-8589/1058)
    < lambda <= b_25 V^(-3453/2116);

k=31:
  c_31 V^(-6473707/264500)
    < lambda <= b_31 V^(-102459/132250).
```

After the theorem's `V^epsilon` loss, its three savings are

```text
k=25:
  27717/10580000, 47/30000, 6827/3174000;

k=31:
  120213/163990000, 907/930000,
  1075613/3050214000.
```

The final entry is the unique minimum and

```text
1075613/3050214000 - 1/13542400
  =68824817/195213696000>0.
```

Hence every fiber is
`O(V^(1-1/13542400))`, and summing over `y` proves the qualitative
complete bound `O(V^(2-1/13542400))`. The range `X<2^822` is covered
trivially because `V<2^(411/2)`, so all floors, endpoints, and small
values are included.

This qualitative argument by itself does not give a numerical `C_23`. Its
critical-moment extraction would require
explicit constants in exactly the two critical mean-value instances

```text
J_(300,24)(H) <= M_25 H^(300+3/100),
J_(465,30)(H) <= M_31 H^(465+93/2000),
```

and a finite propagation of the hidden elementary constants through
Heath--Brown Sections 2--4 at `k=25,31`. The paper explicitly notes that
its VMVT inputs do not provide those constants. The resulting fixed theorem
constants `H_25,H_31` would feed an explicit sufficient formula for
`C_23`; this critical-moment route was superseded, not disproved, by the
effective high-moment route below.
Evidence is
`research/common_anchor_ik825_kappa23_vmvt_fiber_bound.md`, its exact
certificate, the pinned primary source and excerpt, and the typed Jacobian
records.

### `kappa=23` effective high-moment VMVT fiber bound

Raphael S. Steiner's `arXiv:1603.02536v2` gives an epsilon-free
fully displayed high-moment constant for

```text
S >= (5/2)l^2+l.
```

A conservative extraction uses the total-variable Theorem 7.3 above
`H>=(2S)^10` and the trivial `J_(S,l)(H)<=H^(2S)` below that threshold.
For all needed degrees, elementary rational bounds give `D<=22` and a
power-of-two upper bound for every printed `M_0` and mean-value constant.

Reproving the moment-dependent part of Heath--Brown Sections 2--4 gives,
from `J_(S,k-1)(H)<=C H^(2S-k(k-1)/2)`, the three explicit terms

```text
N lambda^(1/(2S)),
N^(1-1/(2S)),
N^(1-1/S) lambda^(-1/(kS)).
```

The proof keeps the exact integer parameters `H,K,D`, the harmonic sum,
the complete third term, and all small-`H` branches. An exact finite
optimization over all `25<=k<=36` and one fiber cut selects

```text
(k,l,S)=(27,26,1716) below the cut,
(k,l,S)=(32,31,2434) above the cut,
cut=1290671299/2286271875.
```

After reserving `1/1000000` for the logarithm, the weakest net saving is

```text
129054413/731607000000
```

and its margin over `1/13542400` is

```text
2064006233/11705712000000.
```

The resulting Engineer-supported numerical source constant is

```text
C_23=2^312118767803953694369567457664167546.
```

Thus the exact `F=X^23` source class satisfies
`|S|<=C_23 V^(2-1/13542400)`.  This closes only the numerical
`kappa=23` source-core node; a uniform all-`kappa` core, downstream
explicit Proposition 1.9 constants, and a multiplicity counterexample
remain open. Independent attribution of both Steiner propositions and
Reviewer replay are pending. Exact evidence is
`research/common_anchor_ik825_kappa23_effective_vmvt_*`.

### Uniform effective high-moment printed-constant boundary

The fixed `kappa=23` success cannot be parameterized uniformly by literally
substituting Steiner's displayed constants into finitely many power-fiber
Heath--Brown estimates and then gluing to the trivial bound. Freeze any finite
power partition, one controlled order
`21kappa/20<=k<=8kappa/5` and any fixed legal
`S>=ceil((5/2)(k-1)^2+(k-1))` on each nonempty range, triangle summation over
the ranges, and the minimum with `V^2`.

For `kappa=q` an integer, `R=10q`, `delta=1/(25600q^2)`, and every controlled
degree `l=k-1` satisfies `l>=q`. Steiner's printed constant obeys

```text
C_l>=4l^(30l^3).
```

The reviewed arbitrary-moment derivative lemma has, on the terminal fiber
range,

```text
B>=C_l^(1/(2S)),  e<=1/(2S).
```

For the normalized stitch

```text
min(V^delta,B V^(-(e-delta))),
```

the integer choice `V=floor(B^(1/e))` gives cost at least
`2^(-delta)B^(delta/e)`. Hence, even after taking the infimum over every legal
order, moment, and finite partition, the cost is at least

```text
q^(3q/2560) -> infinity.
```

Phase, alpha, floor, and Steiner-length thresholds cannot lower this value:
if the analytic estimate starts later, the same scale is covered trivially.
The exact family `X=V^4`, `F=X^q`, `alpha=2`, `f(t)=F log t` realizes the
needed arbitrarily large source scales and has full-phase relative error at
most `2^(-16)` once `V^2>=2^18k`.

This retires only direct use of Steiner's printed constants in the frozen
finite-fiber scheme. It does not lower-bound the best VMVT constant, refute
the uniform source estimate, or affect the reviewed
`C_23=2^312118767803953694369567457664167546`. Exact evidence is
`research/common_anchor_ik825_uniform_effective_vmvt_*`; the bounded Jacobian
call checks only `30/25600=3/2560`.

### Low-growth effective VMVT transfer and Wooley boundary

For every real `kappa>=100`, the two orders

```text
ceil(6kappa/5),  ceil(7kappa/5)
```

and the split at `y=V^(1/2)` give a numerical conditional transfer.
If the complete derivatives have ratio at most `2`, and the effective inputs
satisfy

```text
l(l+1)/2<=S_l<=2l^2,  eta_l<=1/4,
log(H_l)/l^2<=1,  log(T_PS)/ceil(kappa)^2<=1,
log(Q_l)/l^2<=1,
```

then every fiber saves more than `1/(64ceil(kappa)^2)`, four hundred
times the target. Exact integer stitching gives

```text
kappa_0=100,  C_infty=2.
```

This sufficient theorem is not instantiated by the proposed source route.
The original derivative envelope ceases to certify the needed complete-phase
ratio at `kappa>=145`. The reviewed explicit Heath--Brown reconstruction has
`Q_l` containing `(4L_k)^(2S_l)` with
`L_k=9(1+4k(k-1))`, hence
`log(Q_l)/l^2>log(144l^2)`. In Wooley
`arXiv:1101.0574v1`, finite stopping at mean exponent defect at most `1/4`
requires `N>=8l^4`; the proof's required prime set then forces

```text
log H_l >= 2l^(N+1) log(2l^(N+4)).
```

Thus the literal reviewed reconstruction with that source cannot yield one
uniform constant. Ford `arXiv:1910.08209v1` does not repair it: Theorem 3's
general constants have cubic degree exponents, while Theorem 2's `9.463`
is restricted to a logarithmic phase. This is a source/method capability
boundary, not nonexistence of low-growth VMVT. Exact evidence is
`research/common_anchor_ik825_low_growth_vmvt_*`.

### Moving-center reconstruction and printed-BDG boundary

The phase and reconstruction obstructions above are not intrinsic. For every
real `kappa>=100`, restrict the Taylor base to the common interior block, so
that `[z,z+V^2]` remains in the MRSTT source interval. For

```text
k=ceil(6kappa/5), ceil(7kappa/5)
```

and both `r=k,k+1`, moving-center Taylor comparison gives relative error
below `2^(-157)` uniformly on `0<=u<=V^2`. Hence `P_z^(k)` and
`P_z^(k+1)` have fixed signs and `|P_z^(k)|` is monotone. No comparison
with the fixed value `f^(k)(z)` and no uniform derivative ratio is used.

Partitioning that monotone amplitude into `2^k`-adic ranges makes the shift
lengths geometric. Replacing the old coefficient boxes by half-widths
`(8j^3)^(-1)H^(-j)` gives an absolute coefficient-replacement Abel factor;
the inverse box volume `4^l(l!)^3` stays under the final `2S`-th root.
Summing all ranges before that root yields

```text
Q_l<=C_l 2^(33l^2),
log(T_kappa)<=(17A_H+2)ceil(kappa)^2,
e>1/(64ceil(kappa)^2).
```

Thus mean inputs with `log(H_l)<=A_Hl^2`,
`log(C_l)<=A_Cl^2`, `S_l<=2l^2`, and `eta_l<=1/4`
would give the explicit conditional bound

```text
C_infty <= max(
  exp((17A_H+2)/25600),
  exp((A_C+33log(2))/400)
).
```

Bourgain--Demeter--Guth `arXiv:1512.01565v3`, Theorem 1.1, fits the
critical moment `S_l=l(l+1)/2`, defect `1/4`, and all positive lengths.
It does not print its degree-dependent multiplier or a uniform bound for
its logarithm. Proposition 4.2 obtains a required uniform multilinear
constant by neighborhood finiteness and compactness without numericalizing
the cover or supremum. Consequently the printed BDG interface does not
instantiate `A_C`, and no numerical `C_infty` follows.

This retires only the literal moving-center plus printed-BDG splice. The
moving-center reconstruction now remains a viable reusable reduction for a
genuinely quantitative VMVT input. The uniform source core and multiplicity
counterexample remain open. Exact evidence is
`research/common_anchor_ik825_moving_center_*`.

## Complete prime-power assignment boundary

For successive blocks, let `H_t,D_t,S_t=H_t+D_t` be the cumulative
lower-index, row, and total increments.  The middle, low, and high block
products concatenate into intervals of lengths `S_t,H_t,D_t`.  If

`c_q(u,m)=floor((u+m)/q)-floor(u/q)`,

then the exact prefix valuation difference is

`Phi_(p,t)=sum_(e>=1)[c_(p^e)(Y,S_t)`

` - c_(p^e)(L-H_t,H_t)-c_(p^e)(Y+L,D_t)]`.

All three products hold if and only if `Phi_(p,t)=0` for every prime `p`
and every prefix `t=1,2,3`.  For `p>S_3`, the three full intervals contain
at most one multiple of `p`, so complete `p`-primary mass must enter both
sides in the same step.

The apparently stronger rule that each `p^e` layer must balance separately
is false.  In the exact Lind block `9*10=6*15`, the `q=3` layer difference
is `-1` and the `q=9` layer difference is `+1`; only their sum, the actual
`3`-adic valuation difference, is zero.  Thus a primary component may split
between the low and high factors.

Exact product equality also gives the strict arithmetic-mean condition

`sL>a(Y+s)`, where `s=a+b`.

It follows from strict majorization of the factor logarithms.  This rejects
the previous three-step divisibility model, whose gaps are
`-184,-245,-259`; prime `53` independently witnesses a complete valuation
mismatch in its first block.  The condition itself does not close the
domain: `(30,30;3,1),(34,27;2,1),(37,25;1,1)` has increasing slopes and
positive gaps `18,7,11`, but unequal products.

The complete prime-summed rule is therefore an exact reformulation, while
the nontrivial layerwise strengthening is false.  No uniform theorem
forcing a mismatch prime for arbitrary parameters is present.
`research/three_block_exact_residual.md` and its pure-integer certificate
record the proof and controls.  The prime-power assignment route is retired;
the three-block residual, uniform common-anchor exclusion, and `C-T5` all
remain open.

### Large-prime suffix and its exact limitation

For one exact block with `s=a+b`, any prime `p>L` in a middle factor
`Y+i` must match a unique high factor `Y+L+r`.  Their positive difference
is below `2p`, so

`L+r-i=p` and `1<=i<r<=b`.

Both valuations are one.  Therefore every middle factor from index `b`
through `s` is `L`-smooth, and all primes of the middle and high products
are at most `L+b-1`.  This condition correctly allows Lind and rejects the
old local model, whose first block has `b=1` but contains the prime
`53>L=26` at middle index five.

The condition still cannot close three steps.  CRT gives the infinite
residue class

`X=125742796162202 (mod 152125131763605)`

for which

`(X,X;3,1)`, `(X+4,X-3;2,1)`, `(X+7,X-5;1,1)`

has increasing slopes and positive strict-mean gaps
`X-12,X-23,X-19`.  Prescribed small divisors make all nine middle factors
and all three high factors smooth below every applicable `L_j`; low factors
are already bounded by `L_j`.  Nevertheless the first right-minus-middle
product is

`X^4-15X^3-34X^2-48X-24>0`.

This is an infinite countermodel to the sufficiency of large-prime support,
not an exact three-block solution.  A typed Jacobian CRT call and an
independent pure-integer reconstruction certify the displayed residue
class.  Any remaining factor-matching argument must control exact
valuations at primes at most `L_j`.

### Fixed-prime stability and its exact limitation

On that entire CRT progression, the fixed pairs for which
`Phi_(p,t)` is nonzero for every member are exactly

`(7,1),(11,1)`;

all three prefixes for `p=13,17,19`;

prefixes two and three for `p=23,29,31`; and

prefix three for `p=37,41`.

Every other fixed pair is zero infinitely often.  The proof separates
`p|M` from `p` outside the squarefree CRT modulus.  For the former, exact
linear-factor root patterns and complete higher valuations give the list.
For `p=2`, explicit power-of-two classes neutralize each prefix.  For every
`p>=43`, the reachable class `X=10 (mod p)` makes every factor through the
third prefix a unit.

These stable pairs are properties of the chosen congruences, not a uniform
three-block obstruction.  In the same block geometry, every preselected
prime-prefix pair has an infinite neutralizing class.  Moreover,

`X=4595263054458926 (mod 11997602058422981)`

simultaneously neutralizes the complete stable list above.  The exact proof,
certificate, and one bounded typed Jacobian valuation cross-check are in
`research/crt_small_prime_stability.md` and its companion artifacts.

Thus the globally fixed small-prime/fixed-prefix mechanism is exhausted.
A mismatch whose prime and prefix depend on the full parameters remains
exactly the open three-block residual; neither it nor `C-T5` is settled.

## Disconnected row-gap topology boundary

Four numerator windows ordered by increasing lower index have both endpoints
strictly decreasing.  Their disconnected overlap graph therefore has exactly
nine forms: no edges; one of the three consecutive edges; the two edges
`12,34`; or a path or clique on either consecutive triple plus one
singleton.

For `K<=9`, the two path-plus-singleton types are impossible under
`m(a)=5`.  The selected terms of any complete primary `Q` larger than the
two-edge union bottleneck would agree throughout the path, contradicting
the missing endpoint edge.  Hence every one of the at least three primes
`q>K` must lie in `(K,2K-3]`; this interval contains only `11` for `K=7`
and only `11,13` for `K=8,9`.

This does not close the remaining seven types.  Exact common-translation
families at lower indices `(6,7,8,9)` and primes `11,13,17` satisfy the
left-half and row order, unique exact valuation-one offsets, one coherent
four-row cocycle per prime, every zero-free row-gap and ordered-cut gcd
divisibility, the partition weights, and selected common mass `C=1`.
Analogous families at `(17,18,19,20)` and primes `23,29,31` cover all nine
topologies, showing why the path prime-count argument is not uniform in
`K`.

These are row-gap necessary-condition models, not binomial collisions.
Exact polynomial comparison makes their four coefficients strictly
unequal.  They neither synchronize primes above `K` outside the selected
three nor make every stripped remainder `K`-smooth, and their residual
coefficients have no common `b`.  Thus the row-gap route is exhausted while
the seven low-`K` exact-equality topologies, the full disconnected residual,
and `C-T5` remain open.  The proof, sixteen exact families, and bounded
typed Jacobian CRT cross-check are recorded in
`research/disconnected_row_gap_residual.md` and its certificate.

## Exact `K=7` columns 6 and 7 overlap exclusion

The reviewed complete classifications for column pairs `(2,3)`, `(2,5)`,
and `(3,4)` reduce a hypothetical `m(a)=5`, `K(a)=7` system to exactly
three lower-index sets:

`{2,4,6,7}`, `{3,5,6,7}`, `{4,5,6,7}`.

Thus the last two ordered nontrivial representations are always in columns
`6` and `7`.  If the column-7 row is `x`, strict reverse row order writes
the column-6 row as `x+g`.  Their numerator windows intersect exactly for
`1<=g<=5`, while the left-half condition gives `x>=14`.  Cancelling their
common positive numerator factors reduces exact coefficient equality to

`product_(j=6-g)^6 (x-j) = 7 product_(i=1)^g (x+i)`.

The five resulting monic polynomials have degrees `2,3,4,5,6`.
Exact rational Sturm chains isolate all of their real roots, and the
integer-root theorem followed by evaluation of every signed constant-term
divisor finds no integer root for any gap.  Therefore the final two
windows are disjoint in every hypothetical `K=7` multiplicity-five
system.

Combined with the reviewed disconnected topology and path exclusions,
this closes `edge_34`, `edges_12_34`, and `clique_234`.  The exact
disconnected `K=7` frontier is reduced to `all_disjoint`, `edge_12`,
`edge_23`, and `clique_123`.  This result does not address `K>=8` and
does not settle `C-T5`.  The full derivation and rerunnable certificate
are in `research/k7_67_overlap_equality.md` and
`research/k7_67_overlap_equality_certificate.json`.

## Exact `K=7` first-three overlap classification

For the three reviewed surviving lower-index sets, an overlap on edge `12`
or `23` has one of the five lower-index pair types

`(2,4)`, `(3,5)`, `(4,5)`, `(4,6)`, `(5,6)`.

If the larger lower index is `l`, the smaller one is `k`, and their rows
are `x,x+g`, respectively, strict reverse row order gives `g>=1`.  Their
numerator windows intersect exactly when `1<=g<=k-1`.  The five pair types
therefore give exactly `1+2+3+3+4=13` fixed-gap equations

`C(x+g,k)=C(x,l)`, with `x>=2l`.

After reversible cancellation of their common positive numerator factors,
exact rational Sturm isolation and complete signed-divisor evaluation leave
one admissible solution:

`C(15,5)=C(14,6)=3003`.

The complete finite check justified by `C(n,k)>=n` gives

`P(3003)={(14,6),(15,5),(78,2),(3003,1)}`.

Thus `m(3003)=4`, `K(3003)=6`, and the value supplies neither required
four-index set containing `7`.  Hence `edge_12`, `edge_23`, and
`clique_123` cannot occur for `m(a)=5`, `K(a)=7`.  Combined with the
reviewed columns-6/7 and topology exclusions, every hypothetical `K=7`
candidate has four pairwise disjoint numerator windows.

The all-disjoint `K=7` branch, every `K>=8` branch, and `C-T5` remain open.
The exact derivation and rerunnable certificate are in
`research/k7_first_three_overlap_equality.md` and
`research/k7_first_three_overlap_equality_certificate.json`.

## Complete column-2/column-4 intersection

For the first surviving all-disjoint `K=7` lower-index set, the required
pair collision is

`C(Y,2)=C(X,4)`, with `Y>=4` and `X>=8`.

The reversible substitutions

`U=X^2-3X+1`, `Z=2Y-1`, `V=2X-3`

give

`U^2-3Z^2=-2`, `V^2=4U+5`,

and hence

`48Z^2=V^4-10V^2+57`.

De Weger, Quarterly Journal of Mathematics 47 (1996), Theorems 1-3,
pp. 221-228, DOI `10.1093/qmath/47.2.221`, proves the complete integer
classification by reducing this quartic to two completely solved Thue
families. The proof uses global Baker--Wustholz bounds followed by lattice
reduction and a proven finite terminal check; it is not a bounded search or
an unsaturated Mordell--Weil computation.

The full polynomial-equation solution set is

`{0,1,2,3} x {0,1}`

together with the independent involution orbits under
`X -> 3-X`, `Y -> 1-Y` of

`(X,Y)=(4,2),(6,6),(10,21)`.

Thus the unique left-half point is `(X,Y)=(10,21)`, giving

`C(10,4)=C(21,2)=210`.

Complete recovery gives

`P(210)={(10,4),(21,2),(210,1)}`,

so `m(210)=3`, `K(210)=4`, and lower indices `6,7` are absent. Therefore
the lower-index set `{2,4,6,7}` is excluded. The complete classification,
source attribution, and branch implication have been independently reviewed.

`research/k7_24_intersection_certificate.py` verifies the exact polynomial
identities, all twenty integer points, the left-half filter, and the complete
`P(210)`. It also replays de Weger's six terminal Thue equations with
PARI/GP `thueinit(P,1)`, whose output is unconditional. A bounded Jacobian
`0.14.0` call validates only that the entered quartic is a degree-four
affine curve; it supplies no completeness evidence.

## Complete column-3/column-6 and column-4/column-6 intersections

Stroeker and de Weger, *Mathematics of Computation* 68 (1999),
Theorems A36, B36, A46, and B46, Tables 1, T36, and T46,
pp. 1259-1263, DOI `10.1090/S0025-5718-99-01047-9`, classify all
integer solutions of both equations. Their elliptic-logarithm proofs and
terminal exhaustive reductions are on pp. 1264-1268 and 1275-1280.
The source works over all integer rows, so it contains the campaign's
positive left-half domains.

For `(3,6)`, the substitutions

`U=n-1`, `V=(m^2-5m+6)/2`

give the exact identity

`15U^3-15U-(V^3-4V^2+3V)`

`=90*(C(n,3)-C(m,6))`.

The complete integer binomial solution set is

- `{0,1,2} x {0,1,2,3,4,5}`, of value `0`;
- `{3} x {-1,6}`, of value `1`;
- `{9} x {-4,9}`, of value `84`.

Thus none satisfies the left-half conditions `n>=6`, `m>=12`.

For `(4,6)`, the substitutions

`X=(15m^2-75m+50)/2`,

`Y=(225n^2-675n+224)/2`

give

`Y^2+Y-(X^3-525X+10156)`

`=303750*(C(n,4)-C(m,6))`.

The complete integer binomial solution set is

- `{0,1,2,3} x {0,1,2,3,4,5}`, of value `0`;
- `{-1,4} x {-1,6}`, of value `1`;
- `{-7,10} x {-5,10}`, of value `210`.

Thus none satisfies `n>=8`, `m>=12`. The certificate also checks all
11 integral points of the `(3,6)` cubic and all 42 integral points of the
`(4,6)` Weierstrass curve, including points that have no integer row
preimage.

The exceptional positive values have complete campaign occurrence sets

`P(84)={(9,3),(84,1)}`,

`P(210)={(10,4),(21,2),(210,1)}`.

The bound `C(n,k)>=n` makes both recoveries exhaustive. Since the reviewed
`K=7` reduction leaves exactly `{2,4,6,7}`, `{3,5,6,7}`, and
`{4,5,6,7}`, the reviewed `(2,4)` result and the two empty intersections
exclude every `K=7` branch. Therefore `m(a)=5 => K(a)>=8` holds at
Engineer level. The two source readings and the final implication have
since been independently reviewed. Every `K>=8` branch and `C-T5` remain
open.

The 2017 `10^60` result is not used: its Section 2.2 explicitly describes
a finite computer search, while Theorem 1 separately attributes the
complete fixed-index classifications to the 1999 paper. Jacobian validates
only the entered degree-three curve and supplies no integral-point
completeness.

The derivation and exact certificate are in
`research/k7_36_46_intersections.md` and
`research/k7_36_46_intersections_certificate.json`.

A dedicated synthesis now fixes the exact SHA-256 content of the reviewed
`K>=7` bound, the exhaustive ten-set `K=7` reduction, and the complete
`(2,4)`, `(3,6)`, and `(4,6)` classifications. Its executable replay
checks the three campaign domains and all exceptional multiplicities, then
matches the three surviving lower-index sets bijectively with their
exclusions. It therefore obtains

`m(a)=5 => K(a)!=7 => K(a)>=8`

without rerunning an integral-point classification or extending a finite
search. The same replay confirms that the complete next `K=8` residual is
the two all-disjoint systems `{3,5,7,8}` and `{5,6,7,8}`. The dedicated
artifacts are `research/k7_total_exclusion_synthesis.md` and
`research/k7_total_exclusion_synthesis_certificate.json`. The new
total-exclusion graph node awaits its mission-specific independent replay;
`C-T5` and both `K=8` systems remain open.

## Exact `K=8` lower-index and overlap reduction

Stroeker and de Weger, Theorems A28/B28 and A48/B48, Tables 1, T28,
and T48, pp. 1259-1264, give complete all-integer classifications of
`(2,8)` and `(4,8)`. Their common elliptic-logarithm completeness proof is
Section 3, pp. 1268-1275.

Exact two-way recovery checks all 26 T28 points and all 12 T48 points.
For `(2,8)`, the unique campaign left-half collision is

`C(221,2)=C(17,8)=24310`,

and complete occurrence recovery gives

`P(24310)={(17,8),(221,2),(24310,1)}`.

Thus it has multiplicity 3. The point
`C(78,2)=C(14,8)=3003` is retained but correctly filtered because
lower index 8 is outside the left half of row 14. For `(4,8)`, the
campaign left-half intersection is empty; in particular the source point
`C(12,4)=C(12,8)=495` is filtered because lower index 8 is outside the
left half of row 12.

There are exactly twenty four-element subsets of `{2,...,8}` containing
8. Ten contain 2 and are excluded by the complete `(2,8)` result. Of the
remainder, six contain 4 and are excluded by `(4,8)`. Two further sets
contain `(3,6)` and are excluded by its reviewed complete classification.
Exactly

`{3,5,7,8}`, `{5,6,7,8}`

survive.

For an adjacent pair `k<l`, strict reverse row order writes the rows as
`x+g,x`, and numerator-window overlap is equivalent to
`1<=g<=k-1`. Cancelling the common positive numerator factors reduces the
original equation to

`product_(j=k-g)^(l-1)(x-j)`

`=(l!/k!)*product_(r=1)^g(x+r)`.

The four `(5,7)` and six `(7,8)` equations give ten monic integer
polynomials with nonzero constant term. Exact evaluation of every positive
and negative constant divisor finds no integer root; every candidate is
also substituted into the original factorial-scaled equation. Reusing the
reviewed `(3,5)`, `(5,6)`, and `(6,7)` overlap classifications closes the
remaining adjacent pairs. Consecutive disjoint numerator intervals with
strictly decreasing right endpoints are totally ordered, so all four
windows are pairwise disjoint.

Independent review accepted the A28/A48 source readings, exact recovery,
all twenty decisions, all signed-divisor checks, and the all-disjoint
conclusion. The two surviving all-disjoint exact-equality systems, every
`K>=9` branch, and `C-T5` remain open. Full evidence is in
`research/k8_lower_index_overlap_reduction.md` and its certificate.

## Columns `(5,6)`: genus-4 quotient and global boundary

For the surviving `{5,6,7,8}` branch, an even stronger possible exclusion is
the campaign-domain pair

`C(r,5)=C(s,6)`, with `r>=10`, `s>=12`, and `r-s>=5`.

The reversible centered variables

`u=r-2`, `V=2s-5`, `T=V^2`

give

`(V^2-1)(V^2-9)(V^2-25)=384u(u^2-1)(u^2-4)`

with exact domain

`u>=8`, `V>=19` odd, `2u-V>=11`.

The last inequality is precisely the condition that the two numerator
windows are disjoint in the required order. The `V -> -V` quotient is

`(T-1)(T-9)(T-25)=384u(u^2-1)(u^2-4)`.

Its two critical-value resultants are coprime. Its Newton triangle has
vertices `(0,0),(3,0),(0,5)`, four interior lattice points, and primitive
sloping edge, so the smooth normalization has genus `4` and one rational
infinity place.

Exact counts over the first four extensions at good primes `5,7,11` give

```text
#J(F_5)=5041, #J(F_7)=8892, #J(F_11)=33636.
```

The first two orders are coprime, hence `J(Q)_tors=0`. The degree-eight
prime-11 Frobenius polynomial factors into irreducible degrees `[4,4]`
modulo `19` and `[2,6]` modulo `23`. The proper subset-degree sets are
disjoint, proving irreducibility over `Q`; therefore the Jacobian is simple
up to `Q`-isogeny. A lower-dimensional rational-factor decomposition cannot
drive Chabauty.

The fifteen points with `T in {1,9,25}` and
`u in {-2,-1,0,1,2}` give classes
`D_(T,u)=[P_(T,u)-P_infinity]`. Their three horizontal and five vertical
principal-divisor relations have rank seven; no completeness of those
relations is assumed. Exact `divisors.lib` arithmetic on the smooth canonical
complete intersection at `p=7,11` proves that both local 2-Sylow groups are
`C2 x C2`. In the resulting joint quotient, the four classes

```text
D_(9,0), D_(25,0), D_(1,-2), D_(9,1)
```

have matrix

```text
1 0 0 0
0 1 0 1
1 0 1 0
1 0 1 1
```

of determinant one over `F_2`. Any integral relation therefore has all
coefficients even. Writing it as twice another combination gives a
2-torsion point; the reviewed `J(Q)_tors=0` cancels this factor of two.
Iteration forces every coefficient to be divisible by every power of two,
hence to vanish. Thus these four classes are independent and
`rank J(Q)>=4`. This rules out strict classical Chabauty on the genus-4
quotient.

An exact continuation uses good reductions at `p=11,13`. Their degree-eight
Frobenius polynomials are irreducible, and the complete degree-56
root-quotient factorizations have no cyclotomic factor. Tate's theorem
therefore identifies the geometric reduction endomorphism algebras with the
two Frobenius fields. The complete `nfsubfields` lattices have degrees
`1,2,4,8` at `11` and `1,4,8` at `13`; the unique quartics are nonisomorphic
with compositum degree `16`, and the octic fields have compositum degree
`64`. Hence their only common subfield is `Q`, giving

```text
End^0(J_Qbar)=Q, End(J_Qbar)=Z, rho(J/Q)=1.
```

Together with `rank J(Q)>=4`, standard depth-two quadratic Chabauty requires
the false strict inequality `rank J(Q)<4+1-1=4`. This gives no exact rank,
finite-index subgroup, or point classification; covering descent,
finite-index Mordell--Weil sieve, and effective-height routes remain open.

The independently reviewed direct theta-two-cover calculation gives the
following exact boundary. At the unique infinity point the Weierstrass
semigroup is `<3,5>`, so
`K_C~6P_infinity` and `3P_infinity` is the unique rational even theta
characteristic. The exact square-contact equations for normalized tritangent
planes give one irreducible degree-`120` odd-theta orbit. Two certified
one-node reductions and Picard--Lefschetz force the full action
`O_8^+(2)` on `J[2]`; its natural module is irreducible, and an exact
`E8` Coxeter-relation calculation gives

```text
H^1(O_8^+(2),J[2])=0.
```

It follows that every nonzero genuine `[2]`-twist has a single degree-`256`
arithmetic infinity orbit, whereas the zero twist has orbit sizes
`1,120,135`. The grid class `D_(25,2)` is nonzero modulo `2J(Q)` and its
twist contains the rational point `(P_(25,2),0)`. It is therefore globally
soluble, meets the real component containing the campaign domain, and has
Levin count `r=1=|S|` for `S={infinity}`. The required strict inequality
fails, and irreducibility leaves no proper detecting quotient.

The extension-stability continuation is stronger. Write the affine pole-fiber
monodromy as

```text
G=(F_2)^8 semidirect O_8^+(2).
```

Complete enumeration of all `417198` proper subspaces of `(F_2)^8` shows
that the least index of an intransitive subgroup is `240`. It is attained by
`H=W semidirect Stab_O(e_0)`, where `q(e_0)=1` and
`W=e_0^perp`; its two boundary orbits both have size `128`. Thus the least
splitting intermediate field has degree `240`, but already has at least
`120` archimedean places.

For an arbitrary number field `K`, double-coset counting and maximality of
the affine point stabilizer give

```text
r_K <= [K:Q]/2 <= |S_infinity(K)| <= |S_K|
```

outside the unchanged transitive case `r_K=1`; the point-stabilizer
exception has `r_K=3`, degree `256`, and satisfies the same bound. Hence no
finite base extension can restore direct theta-cover Runge for the
`D_(25,2)` twist.

The next true/fake descent stage now has several exact pieces. For the
120-point odd-theta permutation module, both invariant quotients vanish, so
the global true-to-fake map has kernel zero. The safe bad-place set is

```text
S={infinity,2,3,58411,6179021}.
```

The complete fake local images have dimensions `2` at `p=3`, `0` at each
of `58411,6179021`, and `1` at infinity. At `p=2`, the stable factor
degrees `12,12,96` prove `J[2](Q_2)=0` and hence
`dim J(Q_2)/2J(Q_2)=4`, but the exact four-dimensional fake image still
needs the genuine maximal-order completion. Four rational divisor classes
give a certified 16-element globally soluble lower subspace containing
`D_(25,2)`; it is not yet an exhaustive survivor table.

Direct `nfbasis` computed a 120-element maximal order with discriminant

```text
2^222 * 3^100 * 58411^28 * 6179021^28.
```

Maximality follows because the order is maximal at those four primes and
its discriminant has no other prime support. The odd-theta field has no
quadratic subfield: `O_8^+(2)` has abelianization `C2`, while the
odd-theta point stabilizer is not contained in its unique index-two
subgroup. A first full `nfinit` reconstruction timed out after `1800 s`
with no output; a materially lower-height monic scaling is running
durably as `k8-56-theta-integral-nfinit-v4`.

Thus the complete `p=2` fake image, unconditional `S`-class/S-unit upper
bound, no-omission survivor table, and campaign-domain point
classification remain open. The uniform normalization theorem is already
proved and will use this same `S` once the survivor table is exhaustive.
Exact new evidence is in
`research/k8_56_theta_true_descent_certificate.json`,
`research/k8_56_theta_true_descent_small_local_bounds.json`,
`research/k8_56_theta_true_descent_3adic_local_certificate.json`,
`research/k8_56_theta_true_descent_real_local_certificate.json`, and
`research/k8_56_theta_true_descent_integral_basis_certificate.json`.

Bilu--Tichy supplies a finiteness criterion, not the finite integral-point
list. Tengely's complete effective algorithm requires
`gcd(deg F,deg G)>1`, which fails for degrees `(3,5)`. Exact search through
`s<=10^6` finds only `(r,s)=(5,6),(11,11),(15,14)`, none in the campaign
domain; this remains a finite checkpoint. No rank upper bound, finite-index
Mordell--Weil subgroup, complete quadratic-Chabauty or descent calculation,
effective height bound, pair emptiness, or `{5,6,7,8}` exclusion has been
proved.

The exact evidence is `research/k8_56_global_classification.md`,
`research/k8_56_grid_rank.md`, `research/k8_56_geometric_ns.md`,
`research/k8_56_theta_2cover_runge_boundary.md`,
`research/k8_56_theta_2cover_extension_stability_theorem.md`, and their
certificates.

## Columns `5,7,8`: exact high-genus boundary

Both surviving `K=8` lower-index sets contain columns `5,7,8`. Their common
subproblem is

`C(x,5)=C(y,7)=C(z,8)`,

with `x>=10`, `y>=14`, `z>=16`, `x-y>=5`, and `y-z>=7`.
Writing `P_k(T)=T(T-1)...(T-k+1)` gives the reversible equations

`P_7(y)=42P_5(x)`, `P_8(z)=8P_7(y)`.

Exact Singular normalization computes genera `12`, `21`, and `14` for the
pair curves `(5,7)`, `(7,8)`, and `(5,8)`. Rakaczki, Acta Arithmetica 110
(2003), Theorems 1-2 and 4-6, proves that these curves are irreducible and
have only finitely many integer and rational points. The proof explicitly
uses ineffective Siegel/Faltings theorems, so it supplies neither a height
bound nor a complete point list. This is not an emptiness theorem.

An exact monotone merge finds no campaign-domain triple for `z<=10^6`.
Blokhuis--Brouwer--de Weger's separate `10^60` finite computation implies
that any triple has larger common value. Both statements are finite
boundaries only.

For a hypothetical common value `a`, let

`L=product_(p>8) p^v_p(a)`, `b=a/L`.

Then `b` is `8`-smooth and `b<=z^4`. If `d=x-y` and `e=y-z`, the complete
large-prime part satisfies

`L | gcd(R_57(d),R_78(e),R_58(d+e))`,

where

`R_57(D)=product_(s=-6)^4(D-s)`,

`R_78(D)=product_(s=-7)^6(D-s)`,

`R_58(D)=product_(s=-7)^4(D-s)`.

All 280 offset triples obey the exact cocycle. These are necessary
conditions, not a contradiction; retaining the entire canonical
common-`L`, common-`b` system is equivalent to the original equalities.
Thus the triple intersection and `m(a)=5 => K(a)>=9` remain open.

The derivation and exact certificate are in
`research/k8_578_triple_intersection.md` and
`research/k8_578_triple_intersection_certificate.json`.

## Columns `5,7,8`: all centered gcd branches are locally soluble

Centering by

`u=x-2`, `v=y-3`, `W=2z-7`

and putting `d=gcd(W,v)`, `W=dA`, `v=dB` gives exactly the 18
primitive branches

`d in {1,3,5,7,15,21,25,35,49,75,105,147,175,245,525,735,1225,3675}`.

Each branch consists of the reviewed equation `E_d(A,B)=0` from the
centered `(7,8)` descent together with

`G7(dB)=42H5(u)`,

where

`G7(v)=v(v^2-1)(v^2-4)(v^2-9)` and
`H5(u)=u(u^2-1)(u^2-4)`.

Every one of the 18 branches has a primitive, signature-compatible
`Z_p` point for every prime `p`. If `p` does not divide `d`, the exact
choice `A=B=d^-1,u=1` works. At `p=3`, the only possible exponent is one
and the exact centered root is `dA=dB=3,u=0`. At exponent one for
`p=5,7`, use `dA=p,dB=u=0`.

At exponent two for `p=5,7`, set `A=0`. Modulo `p`,

`E_d(0,B) = 11025/d+73728B`

has a nonzero simple root. For `p=5`, the second equation then has the
simple root `u=0 mod 5`. For `p=7`, writing `u=7T` makes
`Q_d(B,7T)/49` integral and congruent to

`6(d/49)B+4T mod 7`,

again with a simple root. The elementary Hensel induction therefore
gives compatible solutions through every `p^k`.

CRT strengthens this to the finite-congruence boundary: for every
`M>=1` and every branch there are positive integers `A,B,u` satisfying
all campaign inequalities, `A` odd, `gcd(A,B)=1`, every mandatory
`3`, `5`, and `7` signature, and both branch equations modulo `M`.
Consequently no branch has a `p`-adic obstruction and no fixed modulus
can exclude one.

These local points and congruence pseudopoints are not global integer
points. All 18 branch-emptiness claims, the triple intersection, both
surviving `K=8` systems, and `C-T5` remain open. Exact evidence is
`research/k8_578_gcd_local_obstruction.md` and its Python/JSON
certificate.

## Columns `5,7,8`: normalized-fiber Runge boundary

The exact common-value model is the rank-`280` fiber product over the
`t`-line

`P_5(x)=t`, `P_7(y)=42t`, `P_8(z)=336t`.

Exact discriminants show that the finite branch supports of the three
polynomial covers are pairwise disjoint. Therefore the affine fiber product
is smooth, including all `280` points above `t=0`. Its ordinary projective
closure is the `W`-saturated complete intersection

`prod_(i=0)^6(Y-iW)=42W^2 prod_(i=0)^4(X-iW)`,

`prod_(i=0)^7(Z-iW)=8W prod_(i=0)^6(Y-iW)`.

At `W=0` its support is the single point `[1:0:0:0]`. Over
`Qbar((1/t))`, reciprocal coordinates give Eisenstein extensions of degrees
`5`, `7`, and `8`. Their coprime compositum has degree `280`, equal to the
full generic rank, so the curve is geometrically integral and the
normalization has exactly one point above infinity. That point is
`Q`-rational, and

`(t)_infinity=280P`, `(x)_infinity=56P`,
`(y)_infinity=40P`, `(z)_infinity=35P`.

Finite ramification contributions `224+240+245` and the infinity
contribution `279` give geometric genus `215`. There is one geometric
infinity point and one absolute-Galois orbit.

Levin, `arXiv:0805.1345v1`, Theorem 2, requires the number `r` of
`Q`-irreducible pole-support components to satisfy `r>|S|`. For ordinary
integral points `S={infinity}`, while every nonconstant regular affine
function has pole support `{P}`. Thus `r=1=|S|`, the strict direct Runge
condition fails, and this mechanism gives neither an effective height bound
nor a complete point list. This is a strategy boundary only; the triple
intersection and both surviving `K=8` branches remain open.

The exact derivation and certificate are in
`research/k8_578_normalized_fiber_runge.md` and
`research/k8_578_normalized_fiber_runge_certificate.json`.

## Columns `(5,7)`: reflection quotient and gcd boundary

Centering by `u=x-2`, `v=y-3` turns the pair equation into

`v(v^2-1)(v^2-4)(v^2-9)=42u(u^2-1)(u^2-4)`.

The simultaneous reflection `(u,v)->(-u,-v)` has invariants
`A=u^2,B=uv,C=v^2`. Exact elimination gives

`B^2=AC`,

`C(C-1)(C-4)(C-9)=42B(A-1)(A-4)`,

`B(C-1)(C-4)(C-9)=42A(A-1)(A-4)`.

On `v!=0`, the birational quotient chart `q=u/v,s=v^2` is

`s^3-(14+42q^5)s^2+(49+210q^3)s-(36+168q)=0`.

The source and quotient have geometric genera `12` and `6`. The quotient
genus follows both from exact Singular normalization and from
Riemann--Hurwitz: the involution has only the smooth affine origin and the
unique normalized point at infinity as fixed points. The projective quotient
chart has one branch over `[0:1:0]` and two over `[1:0:0]`; the latter recover
the deleted `v=0` orbits with `u^2=1,4`. All 35 common-zero points are retained
by the global invariant model. A campaign point is recovered from the affine
chart exactly when `s` is a positive integer square and `q*sqrt(s)` is an
integer satisfying the translated gap.

For `u=da,v=db`, with `gcd(a,b)=1` and `D=d^2`, exact expansion gives

`D[D^2b^7-D(14b^5+42a^5)+49b^3+210a^3]=12(14a+3b)`.

Thus `D|12(14a+3b)`, but this is not a finite descent. For every `n>=1`,

`d=14n+1`, `b=1`, `a=42n^2+6n`

is primitive, satisfies all translated campaign inequalities, and has
`12(14a+3b)/d^2=36`; direct inequalities show that it is not on the curve.
Retaining the full bracket equality is reversibly the original centered
equation. Hence this route supplies neither an effective height bound nor a
complete point list. The `(5,7)` campaign intersection and every consequence
requiring its complete classification remain open.

The exact derivation and certificate are in
`research/k8_57_effective_integral_points.md` and
`research/k8_57_effective_integral_points_certificate.json`.

## Columns `(6,8)`: Runge/norm boundary and exact gcd split

The independently reviewed `K=8` reduction leaves two genuinely separate
branches.  The set `{5,6,7,8}` contains a campaign-domain pair

`C(r,6)=C(s,8)`, with `r>=12`, `s>=16`, `r-s>=6`.

Centering by `w=2s-7`, `v=2r-5` gives the reversible equation

`prod_(j=1,3,5,7)(w^2-j^2)`

`=224 prod_(j=1,3,5)(v^2-j^2)`,

with `w>=25`, `v>=19`, `v-w>=14`, and both variables odd.  Exact monotonic
comparison of `C(s,8)` with `C(s+6,6)` sharpens every possible solution to
`s>=23`, hence `w>=39`, `v>=53`.

If `d=gcd(w,v)`, `w=da`, and `v=db`, exact expansion gives

`d^2[d^6a^8-d^4(84a^6+224b^6)`

`    +d^2(1974a^4+7840b^4)`

`    -(12916a^2+58016b^2)]=-61425`.

Since `61425=3^3*5^2*7*13`, every point lies in exactly one of the four
cases

`gcd(w,v) in {1,3,5,15}`.

Tengely, Acta Arithmetica 110.2 (2003), DOI
`10.4064/aa110-2-8`, gives an effective algorithm only when both separated
polynomials are monic over `Z`, their difference is irreducible, and the
degrees have gcd greater than one.  Simultaneous rational monicity here
would require `alpha^8=56 beta^6`, or after centering
`alpha^8=224 beta^6`; both are impossible because `56` and `224` are
nonsquares.  The two source branches at infinity are conjugate over
`Q(sqrt(14))` and form one rational Puiseux system, so an irrational
rescaling cannot be used as an integral Runge bound over `Z`.

The double-reflection quotient `X=w^2`, `Y=v^2` is the smooth plane quartic

`X^4-84X^3+1974X^2-12916X`

`-224Y^3+7840Y^2-58016Y+61425=0`,

of genus `3`.  Its 12 product-zero points, all 48 source sign lifts, the
unique smooth quotient point at infinity, the two conjugate source branches,
and the positive-square campaign lift are all explicit.  No complete
rational-point computation or effective height bound is available.

The direct quadratic norm is also nonclosing.  It yields
`alpha/beta=(1+sqrt(14)t)/(1-sqrt(14)t)` with rational
`t=U/(56M)=4L/W`, which is the original product equality in Hilbert-90
form.  At the exact off-domain point `(r,s)=(14,14)`, the quotient is
`(81+20sqrt(14))/31`, so it is not an algebraic-integer unit and its
denominator support is not fixed by the coefficient `224`.

Thus the planned Runge and naive unit routes are exhausted, while all four
primitive gcd cases remain open.  The `{5,6,7,8}` and `{3,5,7,8}` branches
remain distinct open dependencies of `m(a)=5 => K(a)>=9`; no complete
`(6,8)` point list or branch exclusion has been proved.  The exact evidence
is in `research/k8_68_integral_points.md` and its certificate.

### The `(6,8)` variable-gap divisibility boundary

Put `x=w^2` and `Delta=v^2-w^2`. Exact subtraction of the common cubic
`G(T)=(T-1)(T-9)(T-25)` gives

```text
P8(w)-224P6(v)
=G(x)(x-273)-224 Delta
  [Delta^2+(3x-35)Delta+3x^2-70x+259].
```

Every solution therefore satisfies

```text
224(v^2-w^2) divides (x-1)(x-9)(x-25)(x-273).
```

This stronger, variable-modulus condition still does not close any of the
four gcd cases. For each `d in {1,3,5,15}`, let `D=d^2+1` and

```text
b_n+a_n sqrt(D)=(d+sqrt(D))^(2n+1),
w_n=d a_n,  v_n=d b_n.
```

Then `a_n,b_n` are odd and coprime,
`gcd(w_n,v_n)=d`, and

```text
v_n^2-w_n^2=d^2(w_n^2-1).
```

On the infinite index classes `n=4 mod 3` for `d=1,15` and
`n=3 mod 8` for `d=3,5`, the recurrence is periodic modulo `7` and forces
`7 | x-25` or `7 | x-9`. The three factors `x-9,x-25,x-273` each supply
three powers of `2`, while `d^2` divides `(x-9)(x-25)`. Hence every family
member satisfies the displayed divisibility and all campaign inequalities.

These are pseudopoints, not solutions. Substitution gives

```text
P8(w_n)-224P6(v_n)=(x-1)(x^3-A_d x^2+B_d x-C_d),
```

with explicit positive integers `A_d,B_d,C_d` satisfying
`B_d A_d>C_d`; every listed family begins beyond `x=A_d`, so the difference
is strictly positive for every member. Thus a successful fixed-gcd descent
must control the exact gap quotient, not only its integrality. The four
gcd-subcase emptiness claims and the complete `(6,8)` classification remain
open. Exact evidence is `research/k8_68_classification_gap.md` and its
certificate.

### The `(6,8)` plane-quartic rank decision

For the quotient Jacobian `J`, exact counts at `p=113` give

`#J(F_113)=1487760=2^4*3*5*6199`.

After projection by the odd part, the four grid-point classes represented by

`(1,1)`, `(25,25)`, `(9,1)`, `(25,1)`

give all `16` elements of the Sylow-2 subgroup, and every element is killed
by `2`.  The classes from `(1,1)`, `(9,1)`, `(25,1)` are therefore
independent modulo `2J(F_113)`.  Since good reduction at `17` has
`#J(F_17)=5647`, rational 2-torsion is trivial; infinite division proves

`rank J(Q)>=3`.

The exact Frobenius polynomials at `13` and `17` are irreducible.  Their
degree-30 root-ratio polynomials have no cyclotomic factor, so the geometric
reduction endomorphism algebras are the respective sextic Frobenius fields.
Each field has only subfields of degrees `1,3,6`; their unique cubic
subfields and the sextic fields themselves are pairwise nonisomorphic.
For good reduction, the needed geometric-endomorphism specialization
injection follows directly: extend an endomorphism over a finite local
extension by the Neron mapping property, then use the functorial
generic/special identification of every finite etale `ell^n`-torsion group
and the Zariski density of `ell`-power torsion. Applying this injection at
both primes gives

`End(J over Qbar)=Z`, hence `rho(J/Q)=1`.

The final Neron-Severi/Rosati identification is Birkenhake--Lange,
*Complex Abelian Varieties*, Proposition 5.2.1.

Thus both strict entrances are the same false inequality:

`rank J(Q)<3` for classical Chabauty, and

`rank J(Q)<3+rho(J/Q)-1=3` for standard quadratic Chabauty.

This is a rank obstruction, not a point classification.  The four gcd
subcases and `L-K8-68-POINT-CLASSIFICATION` stay open.

The Bruin--Lewis two-cover implementation also does not supply a rank upper
bound here: exact enumeration of all `183` lines over the good reduction
`F_13` finds only two rational bitangents, whereas that implementation
requires all `28` bitangents rational over `Q`.  The more general
Bruin--Poonen--Stoll degree-28 etale-algebra descent was not computed, and
its absence is not a rank conclusion.

The exact evidence is
`research/k8_68_plane_quartic_chabauty.md`,
`research/k8_68_plane_quartic_chabauty_certificate.json`, and the mechanical
sources under `research/plane_quartic/`.

### The two `(6,8)` single-square Prym entrances

The remaining natural low-genus lifts adjoin one campaign square at a time:

```text
C_X: F(w^2)=224G(Y),       C_Y: F(X)=224G(v^2),
F(T)=product_(a in {1,9,25,49})(T-a),
G(T)=product_(b in {1,9,25})(T-b).
```

At the unique base point at infinity,
`ord_I(X)=-3` and `ord_I(Y)=-4`. Thus `C_X` branches at the three simple
points with `X=0` and at infinity, while `C_Y` branches at the four simple
points with `Y=0` and is unramified at infinity. The two points of `C_Y`
above infinity are conjugate over `Q(sqrt(14))`. Riemann-Hurwitz gives genus
`7` for both normalizations and dimension `4` for both Pryms. The maps

```text
(w,Y)=(w,v^2),       (X,v)=(w^2,v)
```

give the exact campaign lifts in the two directions.

Exact point counts through degree four recover the Prym Weil polynomials.
Sage function-field Riemann-Roch arithmetic then gives the following
full-rank residue matrices. For `C_X`, the columns are

```text
D(1,1), D(1,9), D(3,1), D(5,1)
```

and the rows over `F_5`, from `p=11,11,23,43`, are

```text
[1 2 0 4], [0 0 1 2], [0 0 1 0], [1 1 1 0].
```

For `C_Y`, the columns are

```text
D(1,3), D(1,5), D(9,1), D(9,3)
```

and the rows over `F_3`, from `p=11,13,29,41`, are

```text
[1 2 2 1], [1 2 1 1], [0 1 2 2], [1 1 0 1].
```

Both determinants are nonzero. The good-reduction orders
`#P_X(F_13)=67642` and `#P_Y(F_17)=180680` exclude rational `5`- and
`3`-torsion, respectively, so infinite division proves

```text
rank P_X(Q)>=4,       rank P_Y(Q)>=4.
```

Both strict Prym rank-`<4` entrances therefore fail. This supplies no rank
upper bound, finite-index Mordell-Weil basis, relative-Chabauty point list,
or `(6,8)` classification. All four gcd cases,
`L-K8-68-POINT-CLASSIFICATION`, `{5,6,7,8}`, and `C-T5` remain open. The
Engineer-level evidence is `research/k8_68_square_lift_prym.md` and its
exact certificate; independent review is pending.

### The `(6,8)` exact-descent boundary

For

```text
x=w^2, Delta=v^2-w^2,
H=Delta^2+(3x-35)Delta+3x^2-70x+259,
```

an exact point satisfies

```text
224 Delta H=(x-1)(x-9)(x-25)(x-273).
```

Since `H=3x^2-70x+259 mod Delta`, the exact resultant

```text
Res_x(3x^2-70x+259,
      (x-1)(x-9)(x-25)(x-273))
=-2^26*3^2*7*457
```

proves

```text
gcd(Delta,H) divides 2^26*3^2*7*457.
```

This bounded gcd still does not close a subcase. On each retained Pell
pseudofamily `Delta=d^2(x-1)` and the specialized value at `x=1` is
`H(1)=192`, so every family satisfies the stronger bound
`gcd(Delta,H)|192d^2`. The prior exact recurrence proof gives infinitely
many campaign-domain members in every `d in {1,3,5,15}` that satisfy the
necessary gap divisibility but not the original equality. The full value of
`H`, not only its gcd with `Delta`, remains uncontrolled.

The generalized bitangent descent also has no small-orbit shortcut. The
line at infinity is a rational hyperflex bitangent, while exact elimination
in the chart `Y=mX+b` gives one irreducible degree-`27` factor for all other
bitangents. Thus the degree-`28` etale algebra has orbit degrees `1+27`.
The universal degree-`27` line is checked by the exact identity
`F(X,alpha X+b(alpha))=(X^2+u(alpha)X+v(alpha))^2`. For the integral
generator `t=14alpha`, its field has signature `(7,10)` and discriminant
`2^34*3^30*7^18*31^6*199^6*312331759^6`.
Bruin--Poonen--Stoll descent would require arithmetic in that degree-`27`
field, including its class and unit groups and all relevant local images;
none has been completed. With exact number-field proofs enabled, the
maximal-order discriminant completed, but the unconditional class-group
step did not finish within `1800 s`; the unit group and local images were
not reached. This is a scoped runtime boundary, not a Selmer, rank, or
point-classification result.

More decisively, the natural `gcd(w,v)=1` restricted fake-Selmer
intersection cannot be empty.  The primitive off-domain point `(w,v)=(9,7)`
defines a global bitangent-descent class of norm `14` modulo squares.  It
belongs to the integral primitive-square local image at every finite prime.
At the real place, the exact quartic point with `w=39` and
`53<v<54` satisfies all campaign inequalities and has the same all-positive
seven-place signature.  Hence that global class survives every restricted
local image.  The exact certificate is
`research/k8_68_exact_descent_fake_selmer_obstruction.json`.  This rules out
only emptiness of the fake-Selmer set; it neither supplies a campaign point
nor excludes one.  A successful continuation must classify the surviving
cover using global point or integral-point information.

Finally, for the subgroup `H` generated by the supplied rational divisor
classes, exact diagonal-Prym reductions at the good primes `11,17,19`
compute rank `3` for the displayed quotient `H/2H`, and rank `4` after
adjoining the rational branch two-torsion class. This does not determine or
upper-bound the ambient Prym image rank. The attempted prime `13` has source
genus `8`, not `9`, and is not a good reduction for that calculation. These
data neither prove nor refute the preregistered six independent non-torsion
directions.

No gcd-subcase emptiness claim and no campaign point follows. Exact evidence
is `research/k8_68_exact_descent.md`,
`research/k8_68_exact_descent_certificate.py`, and the dedicated
bitangent, Prym, and Jacobian records with the same prefix.

### The `gcd(w,v)=5` global finiteness boundary

Writing `w=5a` and `v=5b` gives the reversible equation

```text
(a^2-1)(25a^2-1)(25a^2-9)(25a^2-49)
 =224(b^2-1)(25b^2-1)(25b^2-9),
```

with exact campaign domain

```text
a,b odd, a>=9, b-a>=4, gcd(a,b)=1.
```

Modulo `5`, every point has `(a,b)=(+/-1,+/-1)`. For the full centered
separated equation, the squarefree critical-value polynomials of its
degree-six and degree-eight sides are

```text
(z+50400)(27z^2+4587520z-473520144384),

(z-11025)
(z^3+145152z^2-3567255552z-78275778969600).
```

The first has exactly three distinct roots and their exact gcd is `1`.
Brindza--Pinter Theorem A, restating Davenport--Lewis--Schinzel, therefore
makes the full integral-point set, and hence the `d=5` subclass, finite;
independent source attribution is still required.

This finiteness is ineffective. After `d=5` scaling the leading-coefficient
ratio is `224/25`. Any simultaneous rational monic normalization would
require `alpha^8/beta^6=224/25`, impossible because the left side has even
`7`-adic valuation and the right side has valuation `1`. Thus the retained
Tengely algorithm still gives no height bound or point list. No finite search
cutoff is promoted to global evidence, no campaign point is found, and
`L-K8-68-D5-EMPTY` remains open. The exact derivation, source, Jacobian gcd
record, and replay are in `research/k8_68_d5_global_finiteness.md` and its
certificate.

### The `d=5` four-branch direct-cover boundary

The four modulo-`5` classes do not define separate algebraic components.
The double-square source has genus `17`, and each map

```text
(x,y) -> (a,b)=(5x+epsilon,5y+delta)
```

is an affine `Q`-isomorphism with an exact inverse. Thus the four classes
partition integral points on four isomorphic presentations of the same
curve.

For the exact split `UW=224LM`, primes above `7` occupy one of four cross
cells. For every fixed modulus `M`, branch, cross cell, prime
`q` not dividing `lcm(M,10)`, and positive odd `e`, the congruences

```text
5a=rho+14 sigma q^e,
5b=sigma-3 rho q^e              (mod q^(e+1))
```

match to first order because

```text
P8'(rho)=-18432 rho, P6'(sigma)=384 sigma.
```

CRT adds parity, the selected branch, `gcd(a,b)=1`, and the campaign
inequalities while retaining every fixed curve congruence. The chosen cross
factors have exact odd `q`-valuation. The construction also forces a
strictly nonzero polynomial difference, so these are congruence
pseudopoints, not integral curve points.

Consequently the four branches, internal gcds, and any fixed finite local
data do not yield a finite direct cross-gcd squareclass list. This does not
exclude a genuine finite Selmer or theta-group descent. The standard
full-bitangent presentation still has etale algebra degrees `1+27`, and no
finite-index Mordell--Weil input is available for an exhaustive quotient
sieve. The point classification and `L-K8-68-D5-EMPTY` remain open.
Exact evidence is `research/k8_68_d5_cover_boundary.md` and its certificate.

### The `d=5` restricted BPS control-class boundary

For the genus-3 quartic, exact critical-value elimination gives

```text
-2^80*3^7*31*199*312331759.
```

Together with the characteristic and coefficient primes, this gives the
safe finite bad set

```text
{2,3,7,31,199,312331759}.
```

Its support agrees with the exact discriminant support of the irreducible
degree-`27` bitangent field. There are `29` field primes above this set.
Conditional on the unproved assertion that its `S`-class group has no
2-torsion, the field `S`-unit space modulo squares has dimension `46`;
this dimension is not a Selmer result.

The `d=5` restricted fake-Selmer/theta intersection is provably nonempty.
The off-domain quartic point `(X,Y)=(25,25)`, or `(w,v)=(5,5)`, gives

```text
delta5=25-25alpha-b(alpha),
N(delta5)=14*(358478031955622363136/16807)^2.
```

It is a valid `d=5` local point at every finite prime and has all-positive
signature at the seven real field places. A real quartic point with `w=50`
and `74<v<75` satisfies the scaled campaign inequalities and has the same
signature. Hence this exact global class survives every restricted local
condition; an empty restricted list is impossible. It is distinct from the
previous `(9,7)` control class.

For this class, the complete restriction-of-scalars equation is obtained by
equating all `27` power-basis coefficients in

```text
delta5*zeta^2=Y-alpha*X-b(alpha),
X=25a^2, Y=25b^2.
```

Its rational points map in both directions to `d=5` points in this one fake
class. The raw fixed-class scheme has `2^21` geometric components, each of
degree `64` and genus `129`; adjoining both square coordinates gives degree
`256`, genus `1025` components. This is one exact surviving cover, not the
complete restricted class list.

Bruin--Poonen--Stoll's completeness gate still requires unconditional
`S`-class 2-torsion, a certified `S`-unit basis and norm kernel, global and
local bitangent actions, complete local images, and either full Frobenius
coverage or a matching global lower bound. None is completed. Thus the
empty-list shortcut is closed, while the nonempty complete-list computation,
the cover classifications, and `L-K8-68-D5-EMPTY` remain open. Evidence is
`research/k8_68_d5_bps_selmer_boundary.md` and its exact certificate.

## Columns `(6,8)`: the surviving `(9,7)` cover boundary

For the surviving fake class, put

```text
delta0=49-81alpha-b(alpha),
delta(X,Y)=Y-alpha X-b(alpha)
```

in the irreducible degree-`27` bitangent field. The single-bitangent
equations over that field are

```text
F(X,Y)=0,  delta0*z^2=delta(X,Y).
```

Using

```text
F(X,alpha X+b)=(X^2+uX+c)^2,
```

exact elimination and normalization give a connected unramified double
cover of the genus-`3` quartic, hence genus `5`. It has two geometric points
at infinity forming one degree-`2` closed point over the bitangent field.
The control point `(X,Y,z)=(81,49,1)` recovers `(w,v)=(9,7)` and
`C(6,6)=C(8,8)=1`; it remains outside the campaign domain.

Writing `zeta=sum z_i alpha^i` gives the exact rational fixed-class scheme
by taking all `27` power-basis coefficients of

```text
delta0*zeta^2-delta(X,Y).
```

Its rational points recover exactly the rational base points in this square
class. The norm equation is automatic and cannot replace these coefficient
equations. The 27 bitangent squareclasses span the six-dimensional `J[2]`,
so the scheme has `2^21` geometric connected components, each an unramified
degree-`64`, genus-`129` cover. Adding the campaign equations `X=w^2`,
`Y=v^2` gives degree `256` and genus `1025` on every component. The
component through the control point is the multiplication-by-two pullback

```text
{(P,Q): 2Q=[P-(81,49)]}.
```

Isolating it in bitangent coordinates requires 21 syzygetic relations.
The reviewed equality `#J(F_17)=5647` also gives `J(Q)[2]=0`, so this
component has no nontrivial rational quadratic character quotient.

Keeping one bitangent and both square coordinates gives a connected
`(Z/2Z)^3`-cover over the degree-`27` field. Its genus is `33`; its seven
quadratic character quotients have genera

```text
5,7,7,9,7,7,9.
```

It has four geometric infinity points forming one degree-`4` closed point,
with pole orders `(3,4,4,6,8)` for `(w,v,z,X,Y)`. Thus the strict direct
Runge orbit condition fails.

The unramified genus-`5` cover has a dimension-`2` Prym. Bruin's conic
determinant construction gives an exact smooth genus-`2` curve over the
bitangent field whose Jacobian is that Prym; its sextic has one linear and
one irreducible quintic factor. This curve is an auxiliary Prym model, not a
quotient of the genus-`5` curve. No rank upper bound or finite-index
Mordell--Weil basis over the degree-`27` field is available, so neither
Prym Chabauty nor a Mordell--Weil sieve can be completed.

This exactly exhausts the natural-quotient, norm-form, direct-Runge, and
currently available Prym route for the `(9,7)` class. It does not classify
the cover, produce a campaign point, or prove `gcd(w,v)=1` empty. Full
equations, maps, genus and infinity checks, and the explicit Prym sextic are
in `research/k8_68_d1_surviving_cover.md` and its exact certificate.

## Columns `(3,5)`: quotient, Prym, and rank boundary

For the remaining `{3,5,7,8}` branch, the campaign-domain equation
`C(r,3)=C(s,5)`, with `r>=6`, `s>=10`, and `r-s>=3`,

has the exact genus-2 quotient

`y^2=400q^6+200q^3-80q+9`

and genus-4 square lift

`v^4-(5+20q^3)v^2+4+20q=0`.

The quotient Jacobian has reviewed lower bound `rank>=2` and
Neron--Severi rank `1`, so neither classical nor the standard rational
quadratic-Chabauty strict inequality applies.  The square lift is a
two-point cover whose dimension-2 Prym is represented by

`H: Y^2=W^6-12W^4+48W^2+800W+1936`.

The previously reviewed points `(-2,20)` and `(0,44)` first gave
`rank J_H(Q)>=1`.  A complete Stoll even-degree 2-descent gives the
unconditional upper boundary:

```text
dim Sel_fake^2(J_H/Q) = 4,
dim Sel^2(J_H/Q) = 5,
dim J_H(Q)[2] = 0,
rank J_H(Q) <= 5.
```

The calculation uses
`L=Q[theta]/(theta^6-12theta^4+48theta^2+800theta+1936)`.
PARI's unconditional `bnfcertify` verifies
`Cl(L)=(Z/2Z)^2`, `Cl_{2,5}(L)=Z/2Z`, and signature `(2,2)`.
Eight explicit global square classes consist of three prime `S`-units,
three fundamental units, `-1`, and one residual `S`-class lift.  Their only
norm relation is the equality of the two prime-over-5 exponents.

The necessary local images are complete.  They are zero at infinity and
at `5`; at `2`, the raw local square-class space has dimension `8`,
the norm-kernel quotient by diagonal `Q_2*` has dimension `2`, and the
Jacobian image has dimension `1`.  Pulling that local image back to the
global basis adds no relation beyond the global norm relation.  The bad
prime `23470571` occurs only to the first power in the polynomial
discriminant, so Stoll's exact sequence makes the valuation-zero condition
automatic there.

Thus the prequotient has dimension `7`; quotienting by the three rational
classes `(-1,2,5)` gives fake dimension `4`.  The sextic and its
partition resolvent show that Stoll's even-degree condition `(double
dagger)` fails, adding one dimension to the true Selmer group.  The known
infinite-order class maps to one of the four displayed fake generators.

The first two explicit rational classes sharpened the lower boundary:

```text
D1=[(-2,20)-(0,44)],
D2=[(2,60)-(0,44)].
```

At good reduction `11`, exact Cantor arithmetic and exhaustive enumeration
of all `232` reduced Mumford classes show that `|2J_H(F_11)|=58` and that
`D1`, `D2`, and `D1+D2` are outside `2J_H(F_11)`.  Thus their images form a
basis of `J_H(F_11)/2J_H(F_11)=(Z/2Z)^2`.  Good reduction at `7` has
`|J_H(F_7)|=95`, excluding rational 2-torsion.  Infinite descent on any
integral relation between `D1,D2` proves

`2 <= rank J_H(Q) <= 5`.

The third class

```text
D3=[(-9/2,415/8)-(0,44)]
```

gives a stronger source-curve decision. At the good prime `433`,

```text
#J_H(F_433)=188208=2^4*3^2*1307.
```

Multiplication by the odd part projects `D1,D2,D3` to elements of orders
`2,2,4`. Exact Cantor arithmetic gives 16 distinct generated elements,
so they form the complete Sylow-2 subgroup. Its double has order 2, and
the eight binary combinations of the three classes give all eight cosets.
Reduction at `7` still excludes rational 2-torsion; infinite descent now
proves

`rank J_H(Q) >= 3`.

This direct lower bound verifies the three rational points, their exact
Mumford representatives, all `16` elements of the Sylow-2 subgroup, both
elements of its double, and both members of each of the eight quotient
cosets. It does not use the separate Selmer upper-bound calculation.

A fourth already known rational class,

```text
E0=[(-8,460)-(0,44)],
```

changes the rank boundary.  Exact square-class reconstruction in the
retained `L(S,2)` basis gives, in fake-basis order `(g1,g4,g5,g8)`,

```text
E0 -> (0,0,0,1),
D1 -> (0,1,0,0),
D2 -> (1,1,1,1),
D3 -> (1,0,0,1).
```

These four rows have rank `4` over `F_2`: they respectively recover
`g8`, `g4`, `g5` via `D2+D1+D3`, and `g1` via `D3+E0`.
They therefore span the complete four-dimensional fake 2-Selmer group.
Their independence in the fake quotient implies independence in
`J_H(Q)/2J_H(Q)`; since the retained descent proves `J_H(Q)[2]=0`,

```text
4 <= rank J_H(Q) <= 5.
```

This exactly refutes the proposed `rank J_H(Q)=3` Cassels--Tate route.
There are not two nonrational fake complementary directions after the
three preregistered rational classes.  The remaining true-Selmer
direction is invisible in the fake quotient, and the present calculation
does not decide rank `4` versus `5` or claim a nonzero Cassels--Tate
pairing.

The source involution `v->-v`, pullback/norm splitting, and the explicit
bigonal tower give a `Q`-isogeny

`J_X ~ J_D x J_H`.

The exact source certificate reruns the reviewed pair of independent
quotient classes, giving `rank J_D(Q)>=2`. Rank additivity under the
`Q`-isogeny therefore gives

`rank J_X(Q) >= 5`.

Both branch sextics have good-prime factor patterns `[6]`, `[1,5]`, and
`[1,1,1,1,2]`, so each has Galois group `S6` and geometric endomorphism
ring `Z`. Their complete Frobenius polynomials at `7` are different, which
excludes a `Q`-homomorphism between the two absolutely simple factors.
The product Neron--Severi formula and isogeny invariance give the exact
value

`rho(J_X/Q)=2`.

Thus the standard source depth-two condition becomes

```text
rank J_X(Q) < 4+2-1 = 5,
```

and fails because `rank J_X(Q)>=5`. This rigorously exhausts the current
source-curve quadratic-Chabauty entrance; it does not determine the exact
rank, prove any rank upper bound, or classify the `(3,5)` points. The
campaign emptiness claim, the `{3,5,7,8}` exclusion, and `C-T5` remain
open.

The exact global generators, all sixteen fake classes, local bases,
relation matrices, and Jacobian adapter record are in
`research/k8_35_prym_2descent.md` and its certificate.  The exact rational
Mumford representatives, all `58` elements of `2J_H(F_11)`, the four
quotient cosets, and the rank argument are in
`research/k8_35_prym_cassels_tate.md` and its certificate.
The source decomposition, third independent class, exact Neron--Severi
rank, direct factor rank lower bounds, and strict quadratic-Chabauty
failure are in `research/k8_35_source_quadratic_chabauty.md` and its
certificate.
The exact fourth fake-Selmer image, all square-class witnesses, the
rank-4 matrix, and the refutation of rank `3` are in
`research/k8_35_prym_ct_rank3.md` and its certificate.

### The `(3,5)` quotient fake two-covering boundary

The monic quotient sextic

```text
g(q)=q^6+(1/2)q^3-(1/5)q+9/400
```

defines the same degree-six field as the Prym sextic, via

```text
q=(W^2-4)/20,  W=-(5+20q^3)/2.
```

Reusing and independently recomputing the certified `L(S,2)` basis,
Stoll's even-degree descent on `J_D` again has fake dimension `4` and
true dimension `5`. Nine known quotient points occupy nine distinct
fake classes; the four rows `0001`, `1000`, `0010`, and `0101` are
independent. Since the sextic is irreducible and `J_D(Q)[2]=0`, the
stronger quotient rank boundary is

```text
4 <= rank J_D(Q) <= 5.
```

The curve fake Selmer set requires local curve images, not just local
Jacobian images. Those images are complete at infinity, `2`, and `5`;
the three residue factors at `3` are handled with exact valuation and
unit-square coordinates. Every good prime `7<=p<=1153` is enumerated
exactly, all larger good primes satisfy the Bruin--Stoll genus-`17`
Weil bound, and the simple bad prime `23470571` satisfies its
simple-bad-reduction bound. No place removes a class. Thus the complete
fake two-covering collection has all `16` classes in basis
`(g1,g4,g5,g8)`.

For each class `delta`, the four exact quadrics

```text
Q_delta,2=Q_delta,3=Q_delta,4=Q_delta,5=0 in P^5
```

define a genus-`17`, degree-`16` cover of `D`, with maps

```text
q=-Q0/Q1,  y=+-20 kappa N(z)/Q1^3.
```

Pulling back `t=(5+20q^3+y)/2=v^2` through both maps gives `32`
explicit curves

```text
2Q1^3 v^2 = 5Q1^3-20Q0^3 +- 20 kappa N(z).
```

Each has genus `49`: the degree-two pullback over a genus-`17` cover
is branched at the `32` inverse images of the two branch points on
`D`. Exact canonical cover coordinates replay the nine known quotient
points and all their rational-square lifts; none meets
`u>=5`, `v>=8`, `u-v>=4`.

This is a complete local-covering computation but not a global point
classification. All `16` base covers survive, and all `32` signed
genus-`49` pullbacks lack a complete rational/integral-point
classification or certified finite-index Mordell--Weil input. Hence
the quotient-covering local sieve is exhausted while
`L-K8-35-CAMPAIGN-EMPTY`, `{3,5,7,8}`, and `C-T5` remain open. The
exact quadrics, local records, maps, known lifts, and bounded Jacobian
adapter result are in `research/k8_35_quotient_covering_sieve.md` and
its Python/JSON certificate.

### The `(3,5)` even-degree kernel and exact factor ranks

Both genus-2 factors have square leading coefficient and two rational
points at infinity. With

```text
P_D=(0,3),     P_H=(0,44),     m=infinity_plus+infinity_minus,
```

Poonen--Schaefer's explicit kernel theorem, as restated in Stoll
Lemma 5.1, gives

```text
K_D=[2P_D-m],     K_H=[2P_H-m].
```

The author final Poonen--Schaefer PDF labels the explicit generator
statement Theorem 11.3, preceded by the criterion in Lemma 11.2; Stoll
cites the corresponding source result as `[13, Thm. 11.2]`. For `p=2`,
the formal action `phi` on a degree-one divisor is multiplication by
two, so the source generator `m-phi(P)` is `m-2P`, whose negative is the
displayed class.

Exact PARI computations give Galois group `S6` for both sextics. Thus
neither has an odd-degree factor, and neither admits a Galois-stable
partition of the six roots into two triples. Stoll's condition `(double
dagger)` fails, while each displayed rational point supplies condition
`(dagger)` and a degree-one divisor. The theorem therefore proves that
each `K` is the unique nonzero element of `ker(delta)/2J(Q)`.

For `D`, the four classes based at `(0,3)` and ending at

```text
(2/3,191/27), (7/6,1903/54), (-1/2,11/2), (-1,17)
```

have fake rows `0001,1000,0010,0101`. For `H`, the four classes based
at `(0,44)` and ending at

```text
(-8,460), (-2,20), (2,60), (-9/2,415/8)
```

have fake rows `0001,0100,1111,1001`. Each matrix has rank four and
spans its complete fake group. Adjoining the corresponding nonzero
kernel class gives five independent elements of `J(Q)/2J(Q)`. Since
both retained true 2-Selmer groups have dimension five and both
rational 2-torsion groups are trivial,

```text
rank J_D(Q)=rank J_H(Q)=5,
Sha(J_D/Q)[2]=Sha(J_H/Q)[2]=0.
```

The displayed five-generator subgroups `M_D` and `M_H` have finite odd
index: they surject onto `J(Q)/2J(Q)`, so multiplication by two is
surjective on each finite quotient `J(Q)/M`. Through the retained
`Q`-isogeny `Phi:J_D x J_H -> J_X`, the ten images generate the
finite-index rank-ten subgroup `Phi(M_D x M_H)` of `J_X(Q)`. No exact
factor index or source-index parity is claimed.

This closes the factor-rank and finite-index input but does not classify
the genus-4 source points or any of the 32 genus-49 pullbacks.
`L-K8-35-CAMPAIGN-EMPTY`, `{3,5,7,8}`, and `C-T5` remain open. Exact
evidence is `research/k8_35_even_kernel_mw.md`, its Python/JSON
certificate, the author-final source PDF and excerpt under
`research/literature/`, and the dedicated typed adapter payload/result
under `research/jacobian/`.

### The `(3,5)` flat two-primary Mordell--Weil-sieve boundary

The reviewed odd index of

```text
M_D=<D1,D2,D3,D4,K_D>
```

implies, for every `e>=1`,

```text
M_D/2^eM_D ~= J_D(Q)/2^eJ_D(Q).
```

This is the finite-index specialization allowed by Bruin--Stoll's
Mordell--Weil-sieve algorithm: the omitted index is coprime to the
two-power modulus. No parity of the induced subgroup in `J_X(Q)` is
used.

The complete projective quotient model has infinity points
`(1:20:0)` and `(1:-20:0)`. For a campaign integer pair, an affine
reduction must have square
`t=(5+20q^3+y)/2`. If `q=u/v` has a pole at a good odd prime, then
`p|v` and `y/q^3` reduces to `-20`, so the reduction is the second
infinity point. Thus the campaign local target is the affine square-`t`
locus together with `infinity_minus`; it does not silently discard the
`p|v` case.

Exact Cantor arithmetic and independent `F_p`, `F_{p^2}`, and
Frobenius point-count checks give the following flat local result:

```text
p = 73,97,137,241,281,283,
1 <= e <= 4:
campaign image in J_D(F_p)/2^eJ_D(F_p) = the full quotient.
```

Consequently all `2^(5e)` coefficient vectors survive at each tested
depth, including `1048576` vectors modulo `16`. This is a bounded exact
measurement, not a statement about every prime.

There is also a general obstruction to making this unmodified flat
target empty: the zero class is represented by `(q,y)=(0,3)`, whose
square lift is the off-domain integer pair `(u,v)=(0,2)`, and the four
unit generator classes likewise have known off-domain square lifts.
These classes meet every flat local target. For example `D2` recovers
`(r,s)=(8,8)`, common value `56`, and the complete left-half set
`P(56)={(8,3),(56,1)}`.

Therefore congruence information alone does not identify a surviving
coefficient class with its known point. Completing the campaign
classification still needs an explicit global height bound plus
lattice enumeration, or a proved local/analytic isolation theorem.
The flat two-primary route is exhausted at this boundary, while
`L-K8-35-CAMPAIGN-EMPTY`, `{3,5,7,8}`, `C-T5`, and the campaign
counterexample remain open. Exact evidence is
`research/k8_35_mw_sieve.md` and its Python/JSON certificate.

## Lind family: common-primary absorption boundary

For `s>=2`, put

```text
n=F_(2s)F_(2s+1),  k=F_(2s-2)F_(2s+1),  A=C(n,k).
```

The two Lind numerator windows are `[n-k+1,n]` and
`[n-k-1,n-1]`. Fibonacci determinant identities give

```text
n-k=F_(2s-1)F_(2s+1),  n-k-1=F_(2s)^2,
k+1=F_(2s)F_(2s-1).
```

Their symmetric difference is `{n-k-1,n-k,n}`. Every prime divisor of
these three integers is smaller than `k+1`. Hence, in any collection
containing the Lind pair with maximum lower index `K>=k+1`, every primary
`q^v_q(A)` with `q>K` is selected at the same literal term of the two
windows' intersection. In the reviewed row-gap notation this is exactly

```text
E_Lind=L_K(A),  L_K(A)/E_Lind=1.
```

Thus the direct large-primary resultant on the Lind edge is identically
vacuous after common-term removal. The Lind indices `k,k+1` are consecutive
in any ordering that adds two other distinct lower indices, so the
four-window system is never all-disjoint.

Exact monotone-column recovery determines the complete left-half occurrence
sets for the first four campaign members:

```text
m(A_2)=4,  m(A_3)=m(A_4)=m(A_5)=3.
```

Only `A_2=3003` has an extra nontrivial occurrence, namely `(78,2)`.
These are finite results and confer no conclusion for `s>=6`.

MRSTT Theorem 1.3 places both Lind occurrences in its two-slot interior for
all sufficiently large `s`, so every hypothetical extra occurrence is in
the small-index boundary. Its nonnumerical coefficient threshold and lack
of a boundary multiplicity bound prevent an explicit finite remainder.
Canonical stripping also uses an ambient `K`-unit group of rank `pi(K)`,
with `K>=k_s+1` unbounded, so the reviewed fixed-rank S-unit count is not a
uniform emptiness theorem. The all-`s` assertion `m(A_s)<=4` and an exact
`m(A_s)=5` counterexample both remain open.

The proof, complete finite certificate, and dedicated Jacobian typed records
are `research/lind_family_multiplicity.md`,
`research/lind_family_multiplicity_certificate.json`, and
`research/lind_family_multiplicity_jacobian_*.json`.

## Lind edge34-only: exact elimination and real-spacing boundary

Order a putative pair of extra representations before the Lind pair as

```text
(N,r), (M,t), (n,k), (n-1,k+1),
2<=r<t<k, N>M>n.
```

Because both right and left endpoints decrease in this order, the four
numerator windows have exactly the Lind edge `34` if and only if

```text
N-M>=r, M-n>=t.
```

Let `P_j(X)=X(X-1)...(X-j+1)`, let `J` be the product of the common
Lind-window terms, and let

```text
K=k+1,
L=product_(q>K) q^v_q(A),
b=A/L.
```

Every `q>K` primary lies in `J` and is common to the two Lind rows. The
full stripped equations for the two extra rows and the fixed Lind anchor
are therefore

```text
P_r(N)=r!Lb, P_t(M)=t!Lb, nJ=k!Lb.
```

For fixed `s,r,t`, eliminating `b` over `QQ` gives exactly

```text
k!P_r(N)=r!nJ, k!P_t(M)=t!nJ,
```

which are the two original separated binomial equations. It supplies no
new cross-row condition. If the Lind anchor is discarded first, only

```text
t!P_r(N)=r!P_t(M)
```

survives, and this is strictly weaker: relative to the `s=2` Lind pair,
`(N,r)=(56,2)` and `(M,t)=(22,3)` have exactly the requested edge-34
topology and both equal `1540`, while the Lind value is `3003`. Thus both
anchor equations fail. This is a projection pseudopoint, not a fourfold
collision.

Pure real spacing also cannot exclude this topology. If `X_j` is the
unique real root of `C(X_j,j)=A_s`, then for every `s>=2`,

```text
A_s>=C(n_s,5)>C(n_s+2,3), so X_3>n_s+2,
X_2>=78 and C(X_2-1,3)>C(X_2,2), so X_2-1>X_3.
```

Hence the real windows at columns `2,3,k_s,k_s+1` already have exactly
edge `34` for every member of the family. A successful continuation must
use simultaneous integrality, not interval order or real convexity alone.

The exact derivation and rerunnable controls are in
`research/lind_p34_edge34_exclusion.md` and its certificate. A bounded
typed Jacobian elimination of the `s=2,r=2,t=3` ideal returned the two
separated generators exactly. The all-`s` integer exclusion
`L-LIND-P34-EDGE34-EXCLUSION` remains open, and no counterexample was
found.

## Lind edge34-only: Kummer and finite p-adic fingerprint boundary

Kummer's theorem identifies `v_p(C(x,j))` with the number of carries in
`j+(x-j)` in base `p`; it does not make the carry positions an invariant
of the coefficient. The exact Lind equality

```text
C(15,5)=C(14,6)=3003
```

has one base-`3` carry in each row, at positions `0` and `1`
respectively. Thus equating complete carry-position words would reject a
genuine collision.

For fixed `A`, write `e=v_p(A)`. Matching both the valuation and `h`
digits of the normalized unit of `C(x,j)` is exactly

```text
C(x,j)==A (mod p^(e+h)).
```

This condition depends only on

```text
x modulo p^(e+h+v_p(j!)).
```

Indeed, the integer polynomial
`G_j(X)=j!C(X,j)` satisfies `X-Y | G_j(X)-G_j(Y)`. Hence any finite
collection of valuation/unit conditions defines a separate finite
residue set for each row. For two extra rows the joint set is their
Cartesian product. Whenever both factors are nonempty, positive CRT
representatives can be chosen successively so that

```text
N-M>=r, M-n_s>=t, N>=2r, M>=2t.
```

Therefore finite rowwise p-adic fingerprints cannot yield an obstruction
that disappears when either extra row is deleted.

The quadratic row is especially permissive at positive-valuation primes.
For every odd `p|A`, `C(X,2)=A` has the two simple roots `0,1 mod p`,
which lift to `Z_p`; at `p=2`, the discriminant `1+8A` is `1 mod 8` and
is a 2-adic square. A prime with `p` not dividing `2A` can make the
discriminant a nonresidue, but that excludes the quadratic row alone and
does not provide the required coupling.

Infinite precision does not repair the finite route: for an ordinary
integer `x`, congruence `C(x,j)==A mod p^H` for every `H` is exactly the
integer equality `C(x,j)=A`. Applied to both rows, this is the original
pair of separated equations.

The exact control for `A_2=3003`, primes `3,7,11,13`, and three
normalized-unit digits constructs

```text
(N,r)=(154616924616232,2),
(M,t)=(86606431540785,3).
```

Both rows match every prescribed valuation and unit, and their four
windows with the Lind pair have exactly edge `34`, but their coefficients
are unequal. A bounded typed Jacobian CRT operation returned residue
`73292438292151` modulo `81324486324081` in `1 ms`, with adapter exit
`0`, no timeout, and no structured error. The proof and exact records are
`research/lind_p34_kummer_coupling.md`, its certificate, and the dedicated
Jacobian JSON files.

This retires only Kummer/finite-unit fingerprint comparison as a source
of deletion-sensitive coupling. It proves no infinite Lind exclusion,
and `L-LIND-P34-EDGE34-EXCLUSION` remains open.

## Lind family: triangular subproblem boundary

For

```text
A_s=C(F_(2s)F_(2s+1),F_(2s-2)F_(2s+1)),  s>=2,
```

the exact exceptional identity is

```text
A_2=3003=C(78,2),  1+8A_2=155^2.
```

Lucas reductions give finite nonresidue witnesses for `s=3,4,5,6` at
primes `13,11,17,79`, respectively. These four instances do not imply an
all-parameter classification.

There is a uniform obstruction to any fixed finite modular cover. Write
`u=F_(2s)`, `a=F_(2s-2)`, and `w=F_(2s+1)`, so `n=uw`, `k=aw`, and
`gcd(a,u)=1`. From

```text
k C(n,k)=n C(n-1,k-1)
```

one obtains `u|A_s`. For any fixed finite modulus set with least common
multiple `M`, periodicity of Fibonacci pairs modulo `M` supplies
infinitely many `s` with `M|F_(2s)|A_s`. Therefore
`1+8A_s==1` simultaneously modulo every fixed modulus. Any successful
modular proof must construct a modulus depending on `s`; a finite table
cannot cover the family.

A natural primitive-factor shortcut also has an exact counterexample. At
`s=6`, the discriminant is a quadratic residue at every odd prime dividing

```text
F_10 F_11 F_12 F_13 L_12 F_14,
```

including the primitive prime `233|F_13`; the working witness `79` lies
outside that factor set.

The remaining global equation has an exact prime-allocation form. Let
`P_s` be the product of all primes `p>sqrt(n_s)` dividing `A_s`, and put
`C_s=2A_s/P_s`. Legendre's formula shows that `P_s` is squarefree,
`gcd(P_s,C_s)=1`, and `C_s` has only primes at most `sqrt(n_s)`. Then
`1+8A_s` is square exactly when complementary prime-power factorizations

```text
P_s=QR,  C_s=cd
```

satisfy `|cQ-dR|=1`. Every prime in `n_s-k_s<p<=n_s` belongs to `P_s`,
so a solution must split that whole moving prime product between two
consecutive integers. No uniform exclusion of these partitions is known.

The exact proof and controls are
`research/lind_triangular_classification.md` and its Python/JSON
certificate. A bounded typed Jacobian Legendre-symbol operation confirmed
`(41/79)=-1` with protocol `2025-11-25`, Jacobian `0.14.0`, adapter exit
`0`, and no timeout or structured error. The target
`L-LIND-TRIANGULAR-CLASSIFICATION` remains open.

### Source provenance and the first large-prime lift

For a large prime `p>sqrt(n)` with `v_p(C(n,k))=1`, write

```text
k=hp+k_0,  n-k=ell*p+r_0,  n=qp+n_0.
```

Then `q=h+ell+1`, and with `delta=p-r_0` the possible numerator source
positions are exactly

```text
delta, delta+p, ..., delta+hp.
```

Size and support alone cannot obstruct the allocation: for every `m>=2`,
the identity `2C(m,2)=m(m-1)` assigns each prime above `sqrt(m)` to the
one of `m,m-1` that it divides and gives a complete allocation with
`cQ-dR=1`.

The source is unique only for `p>k`. The true pronic identity

```text
C(17,8)=24310=C(221,2)
```

has two possible sources for `p=5`, namely `10` and `15`, so source
location and its small cofactor cannot be assigned canonically to one of
the consecutive factors.

The exact stripped unit is

```text
C(n,k)/p ==
(-1)^(delta+1) q C(q-1,h)
* (delta C(k_0,delta))^(-1)                 (mod p).
```

This determines both roots of `Z(Z-1)=2A (mod p^2)`. For a complete
allocation

```text
P=QR,  C=cd,  D=cQ-dR,
```

the tentative endpoint `cQ` passes every large-prime `p^2` condition
exactly when `PR|D-1`, while `dR+1` passes exactly when `PQ|D-1`.
Both pass exactly when `P^2|D-1`. In the Lind family `C<P` for every
`s>=2`, so `|D-1|<=PC<P^2`; hence the two-sided lift is equivalent to
the original equation `D=1`.

A one-sided lift is strictly weaker: `Q=c=1`, `R=P`, `d=C` makes
`dR+1=PC+1` pass every `p^2` condition although `D=1-PC`. Pairwise
source gcds remove all large primes and reflection only detects whether
`p|F_(2s+1)^2+1`; neither supplies an allocation direction.

The exact certificate enumerates 32 primary allocations for each of the
two genuine pronic controls and all 524288 allocations for `s=3`. It
recovers the unique allocations for `C(15,5)=C(78,2)` and
`C(17,8)=C(221,2)`, and finds none for `C(104,39)`. This last result is
finite and is not extrapolated.

The proof and controls are
`research/lind_triangular_moving_prime.md` and its Python/JSON
certificate. A bounded typed Jacobian factorization of `24310` returned
`COMPLETE` with `2*5*11*13*17`, protocol `2025-11-25`, Jacobian
`0.14.0`, runtime `1916 ms`, adapter exit `0`, no timeout, and no
structured error. Source provenance, source-cofactor matching,
gcd/reflection pairing, and the first `p`-adic endpoint lift are retired;
higher balanced information and the all-`s` classification remain open.

## The `C_0101` fixed-cover torus boundary

For each of the two fixed signed pullbacks

```text
Y_0101_plus -> X,  Y_0101_minus -> X,
```

the actual integral boundary consists of one degree-16 Galois orbit.
The degree-zero boundary module splits into the 15 nontrivial
characters of `J_D[2]`. Exact good reductions give incompatible orders
`2526` and `630` for the corresponding conjugate elliptic infinity
differences, so every character class is non-torsion. Consequently both
geometric function-unit lattices modulo constants have rank zero.

The coordinate functions of a morphism to `G_m^2` are units. Hence
neither of these two covers itself admits a nondegenerate morphism to
`G_m^2`, and neither yields a numerical Baker--Bilu height bound. This
is a fixed-cover exclusion only. It does not exclude a different
connected finite etale cover, a further cover dominating either one, or
a cover appearing after an additional finite base extension; it also
does not classify either genus-49 curve.

Landesman--Poonen, `arXiv:2306.11799v1`, attributes to Bilu Theorem E
an existential criterion over a connected finite etale cover after
base-field extension. Bilu's primary article is
`doi:10.1007/BF02783215`. Its DOI, Crossref, Springer, and JSTOR records
resolve, but no lawful readable full text was available on this host:
OpenAlex reports the work closed with no repository copy, HAL and
Internet Archive exact-title searches return no record, and the
publisher/JSTOR endpoints return client-challenge pages. Therefore the
original theorem's exact quantifiers and effective conclusion are not
certified here; authenticated library access or document delivery is
still required.

## The `C_0101` degree-15 elliptic quotient boundary

Let

```text
g(q)=q^6+(1/2)q^3-(1/5)q+9/400
```

and let `{alpha,beta}` be an unordered pair of its roots. The retained
`S6` Galois certificate and an exact pair-sum resultant give

```text
K=Q(alpha+beta,alpha*beta),  [K:Q]=15.
```

For the `C_0101` representative `delta`, write

```text
g(q)=(q-alpha)(q-beta)h(q),
c=delta(alpha)delta(beta).
```

The exact single-character quotient is the smooth genus-one quartic

```text
E/K: W^2=c h(q).
```

If `delta(T)z(T)^2=Q0+Q1*T` is a rational cover point, then
`q=-Q0/Q1` and

```text
W=y Q1/(20 z(alpha)z(beta)).
```

The two `Q1=0` fibers are irreducible degree-16 closed points, so they
contain no rational point; for finite rational `q`, irreducibility of
`g` removes the remaining denominator cases. Thus every projective
`C_0101(Q)` point maps to an `E(K)` point with `q in Q`.

The known control point has

```text
q=-1,  delta*z^2=-(T+1)/2,  N(z)=-17/72,  y=17.
```

Its two square signs give `t=1`, recovering the off-domain point
`(u,v)=(-1,1)`, and `t=-16`, which is not a rational square.

Bruin's author-cached primary paper
`doi:10.1515/crll.2003.076` is retained. Sections 3.3 and 4.2 and
Lemmas 4.1-4.3 show that a complete use here needs an unconditional
`rank E(K)<15` bound, sufficient finite-index Mordell--Weil data with
local index control, and a linear or quadratic uniqueness certificate
for every surviving residue/coset. None was obtained. Bounded
Jacobian discovery has no matching number-field rank or elliptic
Chabauty operation; local PARI has no number-field rank command, and
Sage/Magma are absent.

Accordingly the quotient construction is exact, but the elliptic
Chabauty route is retired at a computation-capability boundary. This
does not show that the rank threshold fails, does not enumerate the
rational `q`-coordinates, and does not exclude the `C_0101` campaign
class. Exact evidence is
`research/k8_35_c0101_elliptic_chabauty.md` and its Python/JSON
certificate.

## The columns `(3,8)` plane-quartic boundary

With

```text
u=r-1, W=2s-7, T=W^2,
```

the equality `C(r,3)=C(s,8)` is bidirectionally equivalent to

```text
(T-1)(T-9)(T-25)(T-49)=1720320u(u^2-1).
```

The exact campaign domain is

```text
u>=5, W>=25 positive and odd, 2u-W>=11.
```

The quotient in `(T,u)` is a smooth genus-3 plane quartic with unique
point at infinity `[0:1:0]`.  Its rational divisor classes

```text
[(1,-1)-I], [(1,0)-I], [(9,-1)-I]
```

have order-three projection matrices at `p=13,23,59`

```text
[1 0 1]
[1 2 1]
[1 0 0],
```

whose determinant is `1 mod 3`.  Since `3` does not divide
`#J(F_11)=2846`, infinite 3-divisibility proves `rank J(Q)>=3`.
Exact Frobenius computations at `11` and `13`, together with the cited
Tate and Neron-Severi/Rosati inputs, give

```text
End(J_Qbar)=Z, rho(J/Q)=1.
```

Thus both strict entrances

```text
rank J(Q)<3,
rank J(Q)<3+rho(J/Q)-1=3
```

fail.  Bitangent elimination gives the orbit degrees `1+27`: the
rational component is the hyperflex at infinity and the other
`27` bitangents form one irreducible orbit.  This removes the
all-rational and small-orbit shortcuts but does not execute generalized
descent in the degree-27 field.

The complete rational-point table, unconditional class/unit and local
descent data, surviving-cover classifications, square/domain filtering,
and hence the campaign-domain `(3,8)` pair classification all remain
open.  On the pinned local toolchain, exact polynomial reduction took
`0.16 s`, but the proof-enabled degree-27 class-group computation
returned no result within `1800 s`; this is a computation boundary, not
a class-group or point-set verdict.  No pair miss or finite search is
used as global evidence.
Exact replay is
`research/k8_38_plane_quartic_classification_certificate.py`.

## The columns `(3,8)` independent Hecke boundary

The campaign-local environment under `.tools/k8_38_hecke/` pins Julia
`1.10.10`, Hecke `0.40.1`, Nemo `0.56.1`, and
`FLINT_jll 301.600.0+0`; its manifest has no PARI dependency.  Exact
Hecke arithmetic proves the original `t=1680m` bitangent polynomial and
the persisted reduced polynomial irreducible and isomorphic in both
directions.  The inverse map sends the reduced generator `beta` to
`alpha^3/44100`.  With no discriminant hint, Hecke computes the maximal
order in `0.328743062 s`, including its full integral basis and
equation-order index, and recovers signature `(7,10)` and discriminant

```text
2^34 * 3^34 * 5^18 * 7^18 * 167^6 * 27652954808363^6.
```

The subsequent `class_group(...; GRH=false)` call remains in Hecke's
default LLL relation collector for the complete `1800 s` durable bound
and produces no class group.  It never reaches the unit stage.  Hence
there is still no unconditional class/unit or S-arithmetic data, complete
safe bad set, local-image table, true/fake Selmer comparison, true-cover
list, or surviving-cover point classification.  This retires only the
bounded Hecke `0.40.1` implementation run and gives no class-group,
point-set, or emptiness verdict.  Exact evidence is
`research/k8_38_degree27_hecke_descent.md` and its TOML/JSON records.

## The columns `(3,8)` square-lift Prym boundary

Restoring `T=W^2` gives a ramified double cover of the preceding
genus-3 quotient:

```text
X: (W^2-1)(W^2-9)(W^2-25)(W^2-49)
     =1720320u(u^2-1).
```

The three finite branch points are the simple roots of

```text
16384u^3-16384u-105=0,
```

whose discriminant is
`288150469627346944=2^28*23677*45337`.  The fourth branch point is the
unique quotient point at infinity, where `T` has pole order `3`.
Riemann--Hurwitz therefore gives

```text
g(X)=7, dim Prym(X/C)=4.
```

Exact finite-field point counts and Riemann--Roch divisor arithmetic at
`p=11,13,19,37,43` give a full-rank mod-3 matrix for

```text
D(1,-1), D(1,0), D(3,-1), D(3,0), D(5,0),

D(W,u)=[(W,u)-(-W,u)].
```

The control order `#Prym(F_17)=138436` is prime to `3`, so infinite
3-division proves

```text
rank Prym(X/C)(Q)>=5.
```

The strict relative-Chabauty entrance `rank Prym(Q)<4` is therefore
false.  This sharper lower bound supplies neither the exact rank nor a
finite-index basis.  Saturation, complete local images, a full
Mordell--Weil/covering sieve, and the terminal point table are absent,
so the campaign-domain `(3,8)` classification remains open.  No finite
search miss is used as nonexistence evidence.  Exact replay is
`research/k8_38_square_lift_prym_certificate.py`.

## The `{5,6,7,8}` integral-primary recurrence boundary

The exact full-system tensor has `5*6*7*8=1680` possible cells and 26
column marginals.  Every hypothetical campaign point has at least 14
occupied cells.  Integer cell values and pairwise coprimality do not by
themselves close that residual.

For every `14<=c<=1680`, take the first fourteen cells

```text
H_i=(i mod 5,i mod 6,i mod 7,i mod 8)
```

followed by arbitrary remaining distinct cells, and assign distinct primes
`p_i>8`.  Put `a_c=product_i p_i` and `M_c=a_c^2`.  Exact CRT rows can be
chosen so that every `p_i` occupies its prescribed offset in all four
windows, has coefficient valuation one, and has the same first-order unit
as `a_c`.  Choosing representatives separated by `8M_c,6M_c,4M_c,2M_c`
puts all rows in the campaign domain.  Every marginal is nontrivial and,
with

```text
L_(k,h)=product_(i:h_k(i)=h) p_i,
u_(k,h)=(n_k-h)/L_(k,h),
```

all consecutive recurrences

```text
u_(k,h)L_(k,h)-u_(k,h+1)L_(k,h+1)=1
```

hold exactly.  Moreover,

```text
binomial(n_k,k) == a_c (mod a_c^2)
```

for every `k`.

Nevertheless the construction has the strict order

```text
binomial(n_5,5)<binomial(n_6,6)
<binomial(n_7,7)<binomial(n_8,8).
```

The missing equations are

```text
product_h u_(k,h)=k!.
```

They are equivalent to `binomial(n_k,k)=a_c`, so reinstating them
reinstates the original full-system point problem rather than following
from integral cells, coprimality, or the recurrences.  Thus this exact
unbounded family retires only recurrence-based integer rigidity.  It is
not a full-system point, an emptiness proof, or a counterexample to
universal multiplicity realizability.  Exact evidence is
`research/k8_5678_integral_primary_nonclosure.md` and its Python/JSON
certificate.

## The `{5,6,7,8}` global factorial-cofactor boundary

Writing `n_k-h=L_(k,h)u_(k,h)`, the missing global identities force

```text
product_h u_(k,h)=k!,
gcd(u_(k,h),u_(k,j)) divides |h-j|.
```

The product and generalized gcd criterion first give exactly
`350,1404,25872,92160` candidate vectors in columns `5,6,7,8`.  An exact
primewise classification, including every high-valuation ray, retains
`225,756,4851,23040` vectors that arise from primary allocations.
Requiring the same `v_p(a)` in all four columns leaves

```text
p=2: 7632,  p=3: 1305,  p=5: 1680,  p=7: 56
```

primewise patterns, hence exactly

```text
7632*1305*1680*56 = 937014220800
```

four-column cofactor tuples.  This is an exhaustive finite type theorem,
not a bounded row search.  It genuinely rejects the reviewed `c=14`
recurrence countermodel because all four of that sample's cofactor products
are larger than their factorial targets.

The classification does not decide the branch.  Every cofactor type has an
unbounded CRT progression of rows with positive pairwise-coprime marginals.
At most four small-primary cells are prescribed, and the cyclic 14-cell
support extends any such requirements to every support size from `14` to
`1680`.  Finally, imposing one common numeric cell tensor gives

```text
product_h(n_k-h)
 = (product_h L_(k,h))(product_h u_(k,h))
 = a*k!,
```

which is exactly `binomial(n_k,k)=a` in all four columns.  Thus finite
cofactor stratification leaves the original moving-large-prime equality
rather than a simpler terminal equation.  This route is exhausted, while
the full `{5,6,7,8}` integer-point residual remains open.  Exact evidence is
`research/k8_5678_global_cofactor_classification.md` and its Python/JSON
certificate.

## The actual reciprocal-phase Ford reconstruction

The arbitrary-coefficient IK 8.25 bilinear claim remains open, but it is no
longer needed for the actual high-frequency phase in MRSTT Proposition 4.2.
For fixed `epsilon,A,B,J,H`, define

```text
Q=ceil(max(2,A,B,J,H,1/epsilon)),
X_rec=ceil(exp(2^(2^(2^20 Q^4)))),
C_rec=2^1000000,
c_rec=2^(-4096).
```

For every `X>=X_rec`, every

```text
2<=j<=J sqrt(log X),
|N|,|M|<=H exp(B(log X)^(3/2-epsilon)),
F=|N|/X+|M|/X^j>=X^4,
kappa=log(F)/log(X),
I subset [X,X+X(log X)^(-100)],
```

the numerical estimate is

```text
|sum_(n in I)e(N/n+M/n^j)|
 <=C_rec X exp(-c_rec log(X)/kappa^2)+X(log X)^(-2A).
```

The first term is also at most `X(log X)^(-2A)` at this threshold. The
proof reconstructs Ford Lemma 5.1 rather than applying Ford Theorem 2 to a
nonlogarithmic phase. For `kappa>=220`, it changes Program 2's Taylor degree
to `ceil(8kappa/5)` and the exact normalized exponent is less than
`-1/1000`; for `4<=kappa<=220`, finite-degree classical differencing gives
the uniform saving `2^(-230)`.

The Reviewer-requested component bridge is now explicit. For a clean
integer component of length `ell`, put
`Q_0=floor(M_1)floor(M_2)`. If `ell>Q_0`, every product shift `ab` uses the
same interior of length `ell-Q_0`; its translate remains in the real clean
component and omits exactly `Q_0` integer points. Taylor contributes exactly
`2pi(ell-Q_0)T_K`, and Ford's two Holder inequalities give the complete
multiplier

```text
C_3^(1/R_0)
[(5R_0)^k k^((23291/10000)k^3) C_2
 2^((2g+4)(g-h+1))]^(1/(2R_0s)).
```

Thus the main term is proportional to `ell-Q_0`; it sums by total length,
while all short components and endpoints total at most
`(2kappa+3)X^(877/2500)`. The schema-2 replay checks the symbolic Holder
exponents, 43,680 endpoint sanity cases, every real-`kappa` floor envelope,
Ford (5.7), and all Theorem 3--4 applicability conditions. The clean
decomposition has at most `2kappa+3` components and keeps the short MRSTT
endpoints.

Ford Lemma 6.3's printed single-strip assertion is false verbatim for
`X^(2m)/x^m`, but counting all crossed strips repairs it; no impossibility
claim is made from that mismatch. Exact evidence is
`research/common_anchor_ford_reciprocal_bound.md` and its Python/JSON replay.
Ford Theorems 3--4 have independent source attribution, and independent
review now confirms the schema-2 clean-component bridge.  Thus the
`F>=X^4` branch is a reviewed project input.

## Explicit low frequency and the complete integer-sum proposition

For the same exposed parameters, put

```text
epsilon_0=min(epsilon,1/2),
Q=ceil(max(2,A,B,J,H,1/epsilon_0)),
X_int=ceil(exp(2^(2^(2^20 Q^4)))).
```

For every `X>=X_int`, every allowed `j,N,M,I`, and
`F=|N|/X+|M|/X^j`, the Engineer-supported all-frequency estimate is

```text
|sum_(n in I)e(N/n+M/n^j)|
 <=64X[(1+F)^(-1/16)(log X)^(2A+3)+(log X)^(-A)].
```

For `F<X^4`, the proof differentiates the exact reciprocal phase:

```text
f^(5)(t)=-120t^(-5)(N/t+binom(j+4,5)M/t^j),
f^(6)(t)= 720t^(-6)(N/t+binom(j+5,6)M/t^j).
```

Each derivative has at most one positive zero.  With
`rho=(log X)^(-32(A+1))`, the opposite-sign fifth-derivative cancellation
hull has at most `17rho X` integers.  Outside it, splitting at the
sixth-derivative zero and into dyadic fifth-derivative amplitudes gives at
most `log X` monotone cells.  Cells shorter than
`X(log X)^(-(A+3))` have total length at most `X(log X)^(-A)`;
the others use the independently reviewed fourfold-difference lemma with
`K=floor(min(N_0,(8lambda)^(-1/4)))`.  Its exact roots give
`lambda^(1/64)` and `F^(-1/16)`, while every endpoint, short-cell, and
cancellation contribution enters the displayed logarithmic remainder.

The ranges `F<1` and
`1<=F<=(log X)^(16(2A+3))` are covered by the same displayed main term and
the triangle inequality.  The reviewed Ford estimate covers `F>=X^4`.
Independent review now supports the resulting all-frequency Proposition
4.2. It does not by itself numericalize `C_dist,N_dist`, the common-anchor
remainder, or `C-T5`. Exact evidence is
`research/common_anchor_prop42_explicit_low_frequency_bound.md` and its
Python/JSON replay.

## Explicit prime equidistribution propagation

For `epsilon>0`, `A>0`, and `B,H>=1`, put `a=max(A,1)`. A direct
pointwise Vaughan identity, rather than MRSTT's implicit
shorter-than-dyadic decomposition, propagates the reviewed Proposition 4.2
to both parts of Proposition `equid`. The final constant is

```text
E_eq=2^20.
```

The displayed integer threshold `P_eq(epsilon,A,B,H)` is the maximum of
two explicit tower expressions: one for the exponential mode and one for
the Fourier modes up to `ceil((log P)^(a+4))`. Its base construction uses

```text
T=200, R=a+210, A_0=8R, C=544R+640,
L_*=8*2^(2^(2^20*Q^4)), P_*=ceil(exp(L_*)).
```

The exact convolution identity is

```text
Lambda
 =Lambda_<=U+mu_<=U*log-mu_<=U*Lambda_<=U*1
  +mu_>U*Lambda_>U*1,
```

where the `<=U` symbols are pointwise truncations. It gives coefficient
bounds `1`, `log d`, and `log n` with no hidden multiplier. Additive cells
of length `P(log P)^(-200)` handle arbitrary `I subset [P,2P]`.
Geometric Type-II blocks have exact endpoints
`U(1+(log P)^(-200))^s` and count at most `3(log P)^201`.

The Type-I exponent remains negative. In Type II the `n=n'` term is kept
exactly; after Cauchy and summing the geometric blocks it is at most
`2^10 P^(5/6)(log P)^102`, hence the displayed threshold absorbs it.
The off-diagonal Proposition 4.2 term has final logarithmic exponent
`-A-225`. The cases `j=1`, all larger natural `j`, empty fragments, and
prime powers are separate explicit steps.

For small phase, Johnston--Yang `arXiv:2204.01980v2`, Theorem 1.1 supplies

```text
|psi(x)-x|
 <=9.39x(log x)^1.515 exp(-0.8274sqrt(log x)), x>=2.
```

Two Abel summations convert this first to the weighted prime sum and then
to `dt/log t`. Three integrations by parts in one Fourier coordinate give
an absolute coefficient sum below `2||W||_C3`, a tail below
`||W||_C3/Z`, and include the zero frequency. The amplified frequencies
remain inside the explicitly enlarged `(B,H)` envelope.

Exact evidence is
`research/common_anchor_explicit_prime_equid_bound.md` and its Python/JSON
replay. Independent review confirms both parts, including the retained
Type-II diagonal and the Johnston--Yang proposition at its exact locator.
This result alone does not supply a common-anchor exclusion or a
multiplicity counterexample.

## Explicit `epsilon=1/240` distance specialization

The reviewed prime-equidistribution theorem now propagates through the
scale and covariance argument in MRSTT Proposition 1.9 with no unnamed
constant. With

```text
Q_eq=662570,
L_eq=8*2^(2^((2^20)*Q_eq^4)),
Y_*=(L_eq+2)^2,
C_dist=1,
N_dist=2^(2Y_*+1),
```

every two distinct left-half equal-binomial solutions with
`n+n'>=N_dist`, ordered by `m'<m`, satisfy

```text
m-m'<=exp((log(n+n'))^(161/240)).
```

If both lower indices are at least the exponential scale on the right,
then `n'-n` obeys the same bound. The source at `main.tex:232-238`
prints `m'-m`, but its proof orders `m'<m`; the positive distance used
by the argument is therefore `m-m'`.

The power-of-two selection has at least
`(log n')^(107/160)/2` candidates. All bad scales together number at
most `130896324*(log n')^(46/125)`, leaving the exact exponent surplus
`1203/4000`. The normalized prime average uses the reviewed PNT input to
give at least `P/(4(log P)^101)` primes before division. Explicit `C^3`
sawtooth envelopes, every degree `2<=j<=sqrt(log P)`, and all reduced
small-ratio cases leave total error below the smallest exact gap `1/72`.

Exact evidence is
`research/common_anchor_prop19_explicit_distance_reproof_bound.md` and
its Python/JSON replay. The fixed-`epsilon` result is supported at
Engineer level and by independent review. By itself it does not
numericalize MRSTT Theorem 1.3, exclude the common-anchor remainder, or
produce a multiplicity counterexample.

## Explicit `epsilon=1/12` interior threshold

The reviewed distance theorem now feeds a direct explicit reconstruction
of the left half of MRSTT Theorem 1.3. Define

```text
L_eq=8*2^(2^((2^20)*662570^4)),
N_dist=2^(2*(L_eq+2)^2+1),
T_int=2^N_dist.
```

For every integer `t>=T_int`, there are at most two integer solutions of

```text
binomial(n,m)=t,
exp((log n)^(3/4))<=m<=n/2,
```

where `log` is natural. The proof corrects the real inverse-binomial domain
to `x>0`, derives its monotonicity and strict convexity directly from the
Gamma product and the digamma/polygamma series, and uses no asymptotic
estimate. For a maximal-lower-index solution `(n,m)`, every other solution
has `m'<m,n'>n`. The exact conversion

```text
(4/3)*(161/240)=161/180=9/10-1/180
```

triggers both conclusions of the reviewed distance theorem. An explicit
first-derivative bound gives `m>n^(9/10)` and places every lower index in the
real interval `[m-m^(1/100),m]`. Throughout that interval,

```text
0<f_t''(x)/2<|I|^(-3),
```

so a fully expanded quadratic Lagrange/Rolle argument permits at most two
integer arguments with integer values.

Instantiating the independently reviewed common-anchor interior reduction
gives

```text
K_0=max(4,ceil(exp(432)),ceil(log_2 T_int))
   =N_dist.
```

Every fourfold common-anchor collision therefore has `K<K_0`. This is an
explicit finite cutoff, not an enumeration or an emptiness result. The
explicit interior theorem and cutoff have independent Reviewer support; no
multiplicity counterexample follows yet.

### Three-block continuum entropy boundary

For each exact quotient block, write `H(u)=u log(u)-u`, with `H(0)=0`.
Normalizing by

```text
M=Y+L+sum_j(a_j+b_j)
```

gives the continuous residual

```text
E_j =
 H(y_j+a_j+b_j)-H(y_j)-H(l_j)+H(l_j-a_j)
 -H(y_j+l_j+b_j)+H(y_j+l_j).
```

The coefficient of `log M` is exactly
`(a_j+b_j)-a_j-b_j=0` in each block. Uniform factorial bounds therefore
place every unbounded exact sequence, after a subsequence, in the compact
closed normalized domain satisfying `E_1=E_2=E_3=0`. The closure includes
`l=0`, `y=l`, every vanishing block-coordinate face, the terminal
`sum(a_j+b_j)=l` face, and all intersections, so scale separation and
multiple degeneracy are not discarded.

The limiting system is nonempty away from every boundary. Starting from
`Y=6/5,L=1` with `a_1=a_2=a_3=1/10`, exact rational interval signs and
nested IVT certify roots in

```text
b_1 in [0.05302535376,0.05302535378],
b_2 in [0.1180555649,0.1180555652],
b_3 in [0.233196947,0.233196950].
```

All state updates, positivity and capacity conditions, total-length
inequality, increasing slopes, and strict mean gaps hold uniformly on these
boxes. Thus no uniform positive principal-entropy gap can dominate a
Stirling remainder, even after adding convexity and the reviewed mean
conditions. This is a strict real limiting trajectory, not an exact integer
collision. The exact small-prime valuation residual and the common-anchor
claim remain open. Exact evidence is in
`research/common_anchor_three_block_entropy_limit.md` and its pure-rational
certificate.

### Moving-prime principal-scale collapse

The independently attributed Johnston--Yang estimate

```text
|psi(x)-x|
 <=(939/100)x(log x)^(303/200)
   exp(-(4137/5000)sqrt(log x))
```

implies the explicit prime-gap envelope

```text
G(x)=512x(log x)^2 exp(-(4/5)sqrt(log x)),
log x>=10000.
```

Every real interval `(x,x+G(x)]` contains a prime. The deduction explicitly
subtracts all powers `p^k`, `k>=2`: their total contribution below `2x` is
at most `24sqrt(x)(log x)^2`, while the two `psi` errors and this
prime-power mass are each less than `G(x)/4`. The function is increasing
and `G(x)/x->0`; for integer endpoints use
`g(n)=ceil(G(n))`.

For one exact common-anchor block `(Y,L;a,b)`, a prime `p>L` in a middle
factor has one high partner. The two positions satisfy

```text
L+s-r=p,  r<s<=b,
```

and both valuations are exactly one. A prime cannot therefore be a factor
in `(Y+b,Y+a+b]` or `(Y+L,Y+L+b]`. Applying the gap envelope at the two
integer endpoints gives

```text
a<g(Y+b),  b<g(Y+L).
```

For three successive exact blocks and
`M=Y+L+sum_j(a_j+b_j)`, all local endpoints are at most `M`, while
`Y<=M<3Y`. Hence every one of the six block lengths is less than `g(M)`
and is `o(M)`. This excludes a principal-scale lift of the independently
reviewed strict positive-block entropy trajectory.

The exact residual is still open. If `L/Y` stays bounded below, the total
block length is `o(L)`. If `L/Y->0`, then

```text
sum_j(a_j+b_j)<=(6+o(1))G(Y),  sum_j(a_j+b_j)<L=o(Y);
```

a branch with a positive lower bound for the block-total-to-`L` ratio
requires `L=O(G(Y))`, while branches with another scale separation remain
unexcluded. This is a quantitative boundary theorem, not common-anchor
emptiness or a multiplicity counterexample. Exact evidence is in
`research/common_anchor_moving_prime_envelope.md` and its replay.

### Secondary slope and prefix-divisibility boundary

For each exact block, cancellation and logarithms give

```text
b/a =
 average_i log((Y+i)/(L-i+1))
 / average_r log((Y+L+r)/(Y+a+r)).
```

Monotonicity gives the exact two-sided endpoint interval. If
`rho=Y/L`, `x=(a+b)/L`, and `1<=rho<=R`, then for
`x<=1/[2(R+1)]`,

```text
0<=b/a-Phi(rho)
 <=[6(R+1)+2(R-1)(R+1)^2]x,
Phi(rho)=log(rho)/log(1+1/rho).
```

For `rho>=2`, `x<=1/4`, the large-ratio statement is instead

```text
1<=(b/a)/(rho log rho)<=1+1/rho+(80/3)x.
```

Thus `(Y/L)log(Y/L)` is the correct unbounded-ratio normalization.
The three cumulative original equations directly give

```text
Y+S_t divides L!/(L-S_t)!,  t=1,2,3.
```

These consequences still do not close `S/L->0`. For every integer `n>=200`,
the exact family in
`research/common_anchor_secondary_slope_nonclosure.md` has
`a_j=n^2`, `L=n^3`, `Y/L->3`, `S->infinity`, and `S/L->0`; it satisfies
the full state domain, strictly increasing reduced slopes, both sides of all
three slope intervals, exact Farey spacing, and all three displayed prefix
divisibilities. A deterministic `3`-step adjustment of the first two `b_j`
forces the first original block product to fail while preserving every listed
condition. This is an unbounded integer pseudomodel, not an exact collision.
It retires only the slope-plus-prefix mechanism; a stronger
parameter-dependent valuation or congruence is still needed.

### Full six-endpoint-congruence boundary

The same cumulative equation also gives the companion evaluations

```text
Y divides S_t!-(L+B_t)!/(L-A_t)!,  t=1,2,3.
```

These three additional congruences still do not close the scale-separated
branch. For every integer `n>=200`, set

```text
Y=L=n^3,
(a_1,b_1)=(n^2-n,n),
(a_2,b_2)=(n^2-4n,4n),
(a_3,b_3)=(n^2-7n,7n).
```

Every block has total length `n^2`, so `S=3n^2` and `S/L=3/n->0`.
The reduced slopes are strictly ordered as

```text
1/(n-1)<4/(n-4)<7/(n-7).
```

Exact rational logarithm bounds put all three slopes strictly inside the
reviewed endpoint windows. Farey spacing follows after reduction.

For each prefix, `Y+S_t=n^2(n+t)` divides `(tn^2)!`, witnessed by the
three factors `n,2n,n+t`. Also `Y=n^3` divides `(n^2)!`, witnessed by
`n,2n,3n`. Since every interval product

```text
(L+B_t)!/(L-A_t)!
```

is a product of `S_t` consecutive integers and hence a multiple of `S_t!`,
all six endpoint congruences follow. Equivalently, the adjacent-prefix
factor recurrences show

```text
Y divides gcd(D_1,D_2,D_3),
D_t=S_t!-(L+B_t)!/(L-A_t)!.
```

The first original block product nevertheless fails uniformly: its cancelled
left logarithm is greater than `3n/4`, whereas its right logarithm is less
than `n log 2<3n/4`. Thus this is an exact unbounded integer pseudomodel, not
an exact collision. It retires slope/Farey spacing plus the six endpoint
evaluations only. Parameter-dependent non-endpoint evaluations, valuation
witnesses, and exact common-anchor chains remain open.

### Dynamic medium-prime near-diagonal boundary

Let `H,D,S=H+D` be the final cumulative lengths and let
`Delta=Y-L`. For every fixed `epsilon>0`, an unbounded legal sequence with

```text
S/L -> 0,
Delta <= (121/50-epsilon)S
```

cannot balance every prime above `S`. The three reviewed upper slope windows
give `D<14(S/L)H`, hence `D/S->0`. Define

```text
p=P(product_(r=D+1)^S (Y+r)).
```

The consecutive-product bound
`P(n(n+1)...(n+k-1))>(221/50)k` for `n>4k` gives
`p>(221/50)H>Delta+2S` eventually. If `p` also divided a low factor, it
would divide a positive integer `Delta+r+u<p`; if it divided a high factor,
it would divide `Delta+2r-d`, again strictly between zero and `p`.
Therefore the full valuation, including all powers, satisfies
`Phi_(p,3)>0`.

This rules out the reviewed `Y=L=n^3` six-endpoint family as an
all-`p>S` countermodel. It does not decide the region
`Delta >= (121/50-o(1))S`: there the same two differences can exceed the
available prime-factor lower bound. No all-`p>S` balanced unbounded family
or global exact-chain exclusion is known.

### Macroscopic far-center allocation split

For `p>S`, vanishing of all three complete prefix differences does not give
an indivisible factor matching. If the unique middle, low, and high
occurrences have entry steps and exponents

```text
(tau_M,alpha), (tau_L,beta), (tau_C,gamma),
```

then consecutive prefix differences imply a common entry step and only

```text
alpha=beta+gamma.
```

Both right-hand exponents may be positive. At any entry step, write

```text
u=H_(j-1), d=D_(j-1)+1, r=S_(j-1)+1=u+d.
```

The aligned new factors satisfy `high=middle+low`. Choosing

```text
Y=p^2-r, L=pk+u, 1<=k<p
```

makes them `p^2,pk,p(p+k)` and realizes the exact split `2=1+1`.
The `p` layer has discrepancy `-1`, the `p^2` layer has discrepancy `+1`,
and the full valuation is zero. The raw template has both `Y/L->2` and
`Y/L->infinity` macroscopic far-center scalings.

Exact finite controls at `p=127,Y/L>2` and `p=50021,Y/L>224` satisfy the
full three-step domain, increasing slopes, every reviewed two-sided slope
window, and all strict mean inequalities while exhibiting the split. They
also have explicit other mismatch primes and fail every original block
product. Thus they are not all-`p>S` balanced families or exact chains.

This retires only the inference from complete valuations to one-side
whole-factor matching and a quotient-multiplier lattice. A coupled
allocation retaining two-sided split hyperedges, or a `p<=S` carry
invariant, would be a different route. Macroscopic far-center exact-chain
exclusion remains open.

### Unbounded global split-balance boundary

The coupled local allocation has now been classified completely. If a prime
`p>S` occurs in all three intervals at one entry block, the index ranges and
the three congruences force

```text
r=u+d,  Y+L+d=(Y+r)+(L-u).
```

Complete prefix balance and the nonarchimedean valuation rule then force

```text
(alpha,beta,gamma)=(2e,e,e).
```

The only alternatives are an equal middle-low match or an equal middle-high
match. In particular, `(2,1,1)` is not just an example but the first member
of the only possible two-sided valuation pattern.

For `R_S(N)=product_(p>S)p^v_p(N)`, the three complete prefix balances are
exactly

```text
R_S(binomial(Y+L,L))
 =R_S(binomial(Y+L+D_t,L-H_t)),  t=1,2,3.
```

Thus the global problem is a four-term moving binomial `S`-unit system, not a
support matching or a square-total condition. Complete balance would force

```text
P(product_(r=1)^S(Y+r))<=L+S.
```

The strict reviewed slope windows and rational spacing also imply

```text
Y log(Y/L)<=80S^3
```

eventually in every legal `Y/L->infinity`, `S/L->0` sequence.

The cited literature does not close this system. Bauer--Bennett Theorem 2.2
constructs infinitely many disjoint length-four blocks whose one total
product is a square; it gives no prefixwise valuation equality.
Shorey--Tijdeman `arXiv:1612.05438v1`, Sections 5--6, gives aggregate radical
and `m`-powerfree-part bounds, not an odd-valuation or entry-step selector.
Novakovic `arXiv:2602.23838v1`, Theorems 1.1, 1.2, and 1.4, obtains the
relevant factorial-product finiteness only under the explicit `abc`
conjecture; Theorem 1.3 is only a positive-density statement about the
parameter region. Balog--Wooley's unconditional smooth strings show that the
two raw scale limits alone do not force a prime above `L+S`, but their
iterated-logarithmic length violates the displayed slope-scale inequality and
does not give a legal balanced family.

This exhausts only the split-hypergraph plus these source inputs. No
all-`p>S` balanced unbounded family and no universal mismatch theorem is
known from this route. A continuation needs a genuinely coupled moving
`S`-unit theorem or a growing `p<=S` carry invariant; the exact
common-anchor chain and multiplicity counterexample remain open.

### Growing carry-unit medium-band exclusion

The `p>S` rough-balance survivor is now excluded throughout the unbounded
ratio regime after descending one growing prime band.  Put

```text
B_0=C(Y+L,L),
B_t=C(Y+L+D_t,L-H_t).
```

For `S/3<p<=S`, the bound

```text
Y log(Y/L)<=80S^3
```

eventually puts every top argument below `p^3`.  Kummer therefore reduces
the valuation comparison to the `p` and `p^2` interval counts.  Granville's
Theorem 1, equation (3), gives the exact normalized unit modulo `p^2`,
including the factor `(-1)^(e_1)`.  Its exceptional positive sign occurs
only for `p=2,q>=3` and is irrelevant here.

The exact Lind equality

```text
C(15,5)=C(14,6)=3003
```

has its sole base-3 carry at positions zero and one respectively, while both
normalized units are `2 mod 9`; thus carry positions themselves are not
equated.  More generally, the one-prefix family

```text
S=p, H=1, D=p-1, L=cp, Y=c^2p^2-p+1
```

has carry vectors `(0,1)` and `(1,0)` and equal units modulo `p^2`.
This is a local nonmonotonicity control, not a rough-balanced three-prefix
family.

The global step uses all primes in `(S/3,S]`.  If a fixed prefix had equal
valuations and normalized units at every such prime, its reduced quotient
`u_t/v_t=B_t/B_0` would be `S/3`-smooth and would satisfy

```text
product_(S/3<p<=S) p^2 | u_t-v_t.
```

Kummer bounds its height by

```text
max(u_t,v_t)<=N^(pi(S/3)),  N=Y+L+S,
```

whose logarithm is `(1+o(1))S`.  The reviewed Johnston--Yang prime estimate
and prime-power removal give logarithm `(4/3+o(1))S` for the displayed
modulus.  Hence the quotient is exactly one.  Applying this to all three
prefixes would produce a fourfold common-anchor collision with largest lower
index `L`; the independently reviewed explicit cutoff `L<K_0=N_dist`
contradicts `S<L` and `S->infinity`.

Consequently every sufficiently large rough-balanced unbounded-ratio
survivor has a prime `S/3<p<=S` and a prefix where the total carry or
normalized unit modulo `p^2` differs.  The isolated half-band
`S/2<p<=S` remains nonclosing by this size argument: its residual height has
leading exponent `3/2`, while its squared-prime modulus has exponent `1`.
The finite common-anchor residual and the multiplicity counterexample remain
open.

### K-scale carry-unit restatement boundary

For every residual `K>=10` and prime `K/2<p<=K`, the bounds `y<K^2` and
`D_t<K` put all four top arguments below `p^3`.  Hence the complete Kummer
state has only `p` and `p^2` crossings.  If

```text
X_t=[K!/(K-H_t)!] product_(d=1)^D_t(y+K+d),
Y_t=product_(s=1)^S_t(y+s),
```

then the valuation discrepancy is exactly

```text
1_(H_t>K-p)
+c_p(y+K,D_t)+c_(p^2)(y+K,D_t)
-c_p(y,S_t)-c_(p^2)(y,S_t).
```

After equal valuations, Granville's normalized-unit equality is the
congruence of the corresponding `p`-free interval products modulo `p^2`.
Writing `u_t/v_t` for the reduced ratio `X_t/Y_t`, agreement throughout the
band is therefore exactly

```text
product_(K/2<p<=K) p^2 | u_t-v_t.
```

This is the original cumulative product residual in a finite quotient, not a
new integer relation.  If `W_j=(X_j/Y_j)/(X_(j-1)/Y_(j-1))` is the successive
block ratio, the cumulative fingerprints are

```text
W_1,  W_1W_2,  W_1W_2W_3.
```

Their exponent matrix is integral unimodular, so all three cumulative
fingerprints are trivial exactly when all three block fingerprints are
trivial.  Exact Groebner elimination returns
`{w1-1,w2-1,w3-1}` from
`{w1-1,w1w2-1,w1w2w3-1}`.  Thus eliminating row-local states creates no
cross-prefix invariant beyond the three modular images of the original
equations.

The old medium-band size argument cannot simply be transferred.  Under the
`S`-rough equalities, the reduced ratio is supported on
`q<=min(S,K/2)` and divides the restricted prime-power capacity

```text
product_(q<=min(S,K/2)) q^floor(log_q N).
```

At the permitted edge `S>=K/2`, `N=(1+o(1))K^2`, both this capacity and the
squared-prime band modulus have logarithm `(1+o(1))K`; the strict
`1<4/3` margin is gone.  This retires only K-scale state elimination.  It
does not give an arbitrary-`K` rough-balanced kernel family, prove band
injectivity, enumerate `10<=K<K_0`, or settle the common-anchor conjecture.

### Bounded-ratio common-root elimination boundary

For `s=h+d`, the exact factorial polynomial

```text
P_(h,d)(Y;K)
 = (Y+1)_s-[K!/(K-h)!](Y+K+1)_d
```

has `y` as an integer root exactly when

```text
binomial(y+K+d,K-h)=binomial(y+K,K).
```

For nested pairs, exact factorial cancellation gives

```text
P_j=A_ij P_i+C_i G_i R_ij,
```

where `R_ij(y)=0` is the corresponding successive block product. Hence the
three shared-root equations, the three block products, and the four
left-half Pascal representations are equivalent without a congruence or
asymptotic replacement.

At a candidate common integer root, every integer polynomial Bezout
combination is divisible by `Y-y`; in particular

```text
(P_1,P_2,P_3) intersect Z = {0}.
```

Every polynomial subresultant retains that factor. If the gcd is exactly
linear, its first nonzero raw subresultant is `c(Y-y)` with nonzero integer
`c`; its content has absolute value at least one and its primitive part is
`+-(Y-y)`. Dividing out the root only produces monic integer quotients whose
nonzero resultants again have absolute value at least one.

Complete synthetic division adds no integrality condition. For every
integer `y`, even when `P(y)` is nonzero,

```text
[P(Y)-P(y)]/(Y-y)
 = sum_(k=0)^(n-1)
   [sum_(j=k+1)^n a_j y^(j-k-1)]Y^k
```

already belongs to `Z[Y]`. The coefficient recurrences are triangular, and
their only final remainder is `P(y)`. Across nested factorial polynomials,
the quotient relations reduce to the same block identity and its exact
cocycle, not a fourth equation. At a positive root the quotient is monic,
primitive, and coefficientwise positive, so sign or content does not close
the route either.

There is also a growing-degree obstruction to taking a fixed limiting
subresultant. With `Y=KX` and `u=1/K`, the limiting polynomial is

```text
f_(h,d)(X)=X^(h+d)-(X+1)^d.
```

For every positive integer `n`, the cumulative geometry

```text
n(5,2), n(7,4), n(8,8)
```

has successive slopes `2/5<1<4`, but all three limiting polynomials are
divisible by `X^2+X+1`. Choosing `K=bn^2,y=an^2` realizes any prescribed
rational center ratio `a/b` in a compact subinterval of `(1,infinity)` and
gives `S/K=16/(bn)->0`. This is a legal parameter geometry, not an exact
product solution. It proves that compact ratio, scale collapse, and strict
slope order do not imply leading Sylvester nondegeneracy uniformly in the
growing degrees.

Thus primitive-subresultant/Bezout gaps and complete synthetic-quotient
integrality are exact restatements or degenerate at the proposed entrance.
They do not exclude the bounded-ratio unbounded class, and no integer triple
or multiplicity counterexample follows. Arithmetic-enhanced elimination and
the exact bounded-ratio chain question remain open.

## Cyclotomic deformation and cubic sensitivity

For unequal slopes, the zero-order polynomials

```text
f_(h,d)(X)=X^(h+d)-(X+1)^d
```

have gcd either `1` or `Phi_3=X^2+X+1`.  A common root must satisfy both
`|X|=1` and `|X+1|=1`, hence must be a primitive cube root.  The exact
criterion is

```text
Phi_3 divides f_(h,d)
iff d is even and h-d is divisible by 3,
```

and the factor is simple.  Legal strict block slopes make the cumulative
slopes distinct, so this classifies every zero-order common factor.

For the exact scaling

```text
F_(h,d)(X,u)
 = product_(r=1)^(h+d)(X+ru)
   -product_(r=0)^(h-1)(1-ru)
    product_(r=1)^d(X+1+ru),
```

the first remainder coefficient at a primitive cube root `zeta` is

```text
[u]F_(h,d)(zeta,u)
 = -(1/2)zeta^(h+d)(P+Qzeta),

P=(d+1)(2h+d), Q=h(h+2d+1).
```

Its Eisenstein norm `P^2-PQ+Q^2` is positive.  In particular, all three
rays `n(5,2),n(7,4),n(8,8)` split at first order, with pairwise velocity
gaps of order `n`.

This local result does not yield a square-root exclusion.  With

```text
q_m=F_(2m), r_m=F_(2m+1),

(h_1,d_1)=(r_m,q_m),
(h_2,d_2)=(r_m+q_m,r_m),
(h_3,d_3)=(r_m+q_m+1,r_m+1),
```

Cassini's identity makes the successive block slopes strictly increasing
and gives determinant one for the first two cumulative pairs.  Their
zero-order gcd is therefore `1`.  Nevertheless, their two positive real
root branches cross at real parameters `u_m>0` satisfying

```text
q_m r_m(r_m-q_m)u_m -> c>0,
S_m^2u_m -> 0.
```

Thus their exact real resultant vanishes inside the proposed
square-root deformation regime even after every zero-order cyclotomic factor
is removed.  The crossing occurs at `u=Theta(S^-3)`, matching the existing
`S>>K^(1/3)` slope/Farey scale.

The `u_m` are not known to equal reciprocal integers, the roots are not known
to be `y/K`, and the third polynomial is not asserted to vanish.  This is a
boundary for continuous deformation/resultant arguments, not an integer
three-zero collision.  A successful continuation must use the discrete
conditions `u=1/K`, `X=y/K`, and all three exact product equations.

## Exact Fibonacci reciprocal-grid exclusion

The discrete continuation of that determinant-one family is now completely
excluded.  For

```text
q=F_(2m), r=F_(2m+1)
```

and cumulative pairs

```text
(r,q), (r+q,r), (r+q+1,r+1),
```

the three scaled equations at `u=1/K`, `X=y/K` are exactly the original
integer product equations after clearing `K^(h+d)`.  Their successive blocks
are `(r,q)`, `(q,r-q)`, and `(1,1)`.

The terminal block has the complete negative-Pell parametrization

```text
K=F_(2ell-1)F_(2ell)+r+q,
y=F_(2ell)^2-1-q-2r.
```

Substitution into the middle block reduces it to

```text
product_(j=1)^r(B^2-j)
 =product_(i=1)^q(AB+i)
  product_(j=1)^(r-q)(B^2+AB-j),
```

where `A=F_(2ell-1)` and `B=F_(2ell)`.  For `m=1` the left side is strictly
smaller.  For every `m>=2`, the domain forces

```text
B^2>=64r/5,  3/5<A/B<=5/8,
```

and elementary logarithmic bounds give the exact positive lower margin

```text
6/13-(15/59+5/128+5/32)=1177/98176.
```

Hence the left side is strictly larger for `m>=2`.  The middle block never
vanishes, so there are no requested integer `K,y` for any `m>=1`.

This is an all-index symbolic exclusion, not a finite search miss.  It closes
only the displayed Fibonacci geometry; the unrestricted three-block
common-anchor claim and `C-T5` remain open.  The exact proof and replay are in
`research/common_anchor_fibonacci_discrete_lift_exclusion.md` and
`research/common_anchor_fibonacci_discrete_lift_certificate.json`.

## Unrestricted terminal `(1,1)` route boundary

The same negative-Pell classification parameterizes every terminal unit
block, not only the preceding Fibonacci geometry.  Put

```text
A=F_(2ell-1), B=F_(2ell), X=B^2, T=AB, H=X+T.
```

An arbitrary reverse block `(a,b)` has state

```text
Y=X-1-a-b, L=T+a
```

and is legal exactly when `2a+b<=A^2-2`.  Its exact product ratio is

```text
R(a,b)
 =product_(j=1)^(a+b)(X-j)
  /[product_(i=1)^a(T+i) product_(j=1)^b(H-j)]
 =binomial(H-1-b,T+a)/binomial(H-1,T).
```

If the inner predecessor is `v` and the preceding block is `u`, all three
original blocks `(u,v,(1,1))` are exact if and only if

```text
R(v)=R(u+v)=1
```

with the full initial domain and strict slope order.  Thus the live branch is
exactly the question whether this Lind-value level set has two legal integral
points on its high-column side.

The proposed uniform sign is false on an infinite exact family.  For every
`ell>=3`, both points below are legal and have `b<a`, but

```text
R(2,1)>85095/68224>1,
R(A+1,A)<1.
```

The second sign follows from the exact diagonal recurrence and a summed
strict margin greater than `1/2`; it is not a finite numerical observation.
Exact finite differences show that `log R` increases with `a`, decreases
with `b`, and is strictly subadditive under positive translations.  A
hypothetical chain would force the unused corner `R(u)>1`, which is a new
necessary condition but not a contradiction.

Complete Legendre valuation equations for every prime are if and only if
`R(a,b)=1`.  They also contain literal moving Fibonacci cancellations.  If

```text
Q_k(Z)=Z^2+(k+1)Z-k^2,
f=F_(2m), g=F_(2m+1),
```

then

```text
(T+k)(H-k)=Q_k(X),
Q_(fg)(X)=(X-f^2)(X+f^2+fg+1).
```

Taking terminal index `ell=m+2` and `(a,b)=(fg+1,fg)` puts this common factor
inside the legal domain for every `m>=1`.  Hence unmatched-prime forcing and
complete valuation bookkeeping do not close the branch: the former has an
infinite symbolic obstruction, while the latter is the original equality.

No first predecessor, second predecessor, integer chain, or branch exclusion
is obtained.  The sign-plus-valuation route is retired, while
`L-COMMON-ANCHOR-TERMINAL-UNIT-BLOCK-EXCLUSION` remains open.  Exact evidence
is `research/common_anchor_terminal_unit_block_boundary.md` and its
Python/JSON replay; the bounded typed Jacobian call checks only
`Q_15(X)=(X-9)(X+25)`.

### The nested oriented-area condition is automatic

For the Gamma extension `F=log R`, the restriction
`g(t)=F(ta,tb)` to every positive ray satisfies

```text
g''(t)
 =-(a+b)^2 psi_1(X-t(a+b))
  -a^2 psi_1(T+ta+1)
  +b^2 psi_1(H-tb)
 <0.
```

Indeed, the positive decreasing trigamma series and
`H-tb-[X-t(a+b)]=T+ta>0` make the positive last term strictly smaller
than `b^2 psi_1(X-t(a+b))`.  Also `partial_b F<0`.  Consequently, if
`p,q` are positive real zeros with `p_a<q_a`, strict ray concavity gives

```text
q_b/q_a<p_b/p_a.
```

For nested points `q=p+u`, this is exactly the required block-slope order
and says

```text
Delta=det(u,p)=det(q,p)>0.
```

Thus two nested integral zeros would automatically have
`Delta in Z_(>=1)`; slope order and bare determinant integrality impose no
additional arithmetic condition.

An exact `ell=4` sign box shows that this is not merely infinitesimal.
There are unique real zeros

```text
p=(14,b_p), 11<b_p<12,
q=(55,b_q), 27<b_q<28,
```

all strictly inside `2a+b<=13^2-2`, and

```text
det(q,p)>55*11-14*28=213.
```

Therefore continuous finite-difference or four-point area arguments cannot
force a subunit determinant.  A complete exact scan found no integral zero
for `3<=ell<=6` among `37+2269+110592+5223241` legal pairs, but this is
only a finite control and is not a branch exclusion.  The proof and replay
are `research/common_anchor_terminal_unit_nested_area_boundary.md` and
`research/common_anchor_terminal_unit_nested_certificate.py`.

### Terminal prime-power source-resultant boundary

For the terminal state

```text
A=F_(2ell-1), B=F_(2ell), X=B^2, T=AB, H=X+T
```

and

```text
Q_i(Z)=Z^2+(i+1)Z-i^2,
```

the exact identities

```text
Q_i(X)=(T+i)(H-i),
Q_i(r)-Q_i(X)=(r-X)(r+X+i+1)
```

turn every factor `T+i` or `H-i` in a zero of `R` into a complete
prime-power divisibility of `product_(r=1)^(a+b) Q_i(r)`.  More strongly,
if `p^e` divides the target factor, the original product records

```text
sum_(k=1)^e #{1<=r<=a+b:r=X mod p^k}>=e.
```

Thus the actual oriented source residues survive; the result is not merely
the automatic quadratic-residue condition.  Also

```text
gcd(T+1,H-1)|7.
```

At `i=1`, `Q_1(Z)=Norm(Z+1+sqrt(2))`.  Complete trial division and exact
legal-prefix maxima show that the oriented source is absent for a prime
factor at `ell=3,5,12`, so every legal zero is excluded at those three
terminal indices.

This detector is not uniform.  For every `ell=4h+2`, both terminal factors
are divisible by `7`; after removing it, their coprime cofactors are shorter
than an explicit legal prefix.  Two floor-defined nested lattice points then
satisfy the complete oriented `i=1` source condition.  At the first member
`ell=6`, the points

```text
(2693,2297), (2772,2336)
```

have source factors `7,7,1831,4793`, but their two original product
equalities have unequal residues `11399/14399` and `9535/28266` modulo
`40009`.  Hence the `i=1` source condition is strictly weaker than `R=1`.
This retires only a uniform first-discriminator obstruction; higher-`i`
coupled allocation, the integral nested-zero problem, and `C-T5` remain
open.  Exact evidence is
`research/common_anchor_terminal_unit_source_resultant_boundary.md` and its
Python/JSON replay.

### Joint directed-source conditions at every fixed depth

The next two-sided level has the exact Fibonacci crossing

```text
Q_2(Z)=(Z-1)(Z+4),
X-1=F_(n-2)F_(n+2), X+4=F_(n-3)F_(n+3),
T+2=F_(n-3)F_(n+2), H-2=F_(n-2)F_(n+3),
```

where `n=2ell`.  At `ell=6`, seven distinct source factors with indices

```text
1,2,9,30,595,606,1564
```

supply the complete product
`(T+1)(H-1)(T+2)(H-2)` inside both prefixes `4990` and `5108`.
The original block products nevertheless remain unequal modulo `40009`.

This compatibility persists at every fixed source depth.  For arbitrary
fixed `m`, start at `ell_0=4m+2`, freeze every `T_0+i` and `H_0-i`
modulo its square, and take an infinite Fibonacci-period progression of
terminal indices.  Each later target splits into a fixed component and a
coprime moving component.  All `4m` components are eventually at most
one `4m`-th of the shorter legal prefix, so their oriented residue classes
have enough representatives for a distinct full-multiplicity matching.
Thus both nested floor-defined points satisfy all joint source conditions
through `i=m`.

No fixed finite depth can exclude the branch.  At full point-dependent
depth, source capacity alone is the strict intermediate divisibility
`W_(a,b)|L_(a+b)`; requiring exact use of all source valuations is
precisely the original factorial equality `R(a,b)=1`.  The fixed-depth
result does not decide the intermediate condition when the depth grows
with the point.  Thus it retires only a uniform fixed-depth obstruction,
not the whole directed-source route or the integral two-zero problem.
Exact fixed-depth evidence is
`research/common_anchor_terminal_unit_joint_source_boundary.md` and its
Python/JSON replay.

### Point-dependent growing source depth

At `ell=6`, with

```text
(A,B,X,T,H)=(89,144,20736,12816,33552),
```

the two prior pseudopoints have prefixes `4990` and `5108`.  Exact oriented
valuation accounting gives

```text
m_max(6,4990)=m_max(6,5108)=4.
```

All prime powers in `D_4` occur in both prefix products.  At depth five,
however,

```text
T+5=12821, X mod 12821=7915,
H-5=33547>X,
```

and both prime factors have zero source capacity in either prefix.  This
also yields a complete local exclusion.  If a legal `ell=6` point has
`a<=4`, then `a+b<=7` and the prime `1831|(T+1)` has oriented residue
`595`; if `a>=5`, legality gives `a+b<=7914` and `12821|(T+5)` has
oriented residue `7915`.  Hence every legal `ell=6` point violates
`W_(a,b)|L_(a+b)`.

This does not extend uniformly: the fixed-depth Pisano theorem specialized
to `m=5` gives infinitely many other terminal indices whose floor-defined
nested pair passes `D_5|L_s`.  Conversely, that fixed-`m` theorem supplies
no depth growing with `ell`.  The previous all-route retirement inference
is therefore withdrawn.  Point-dependent growing source divisibility
remains open.  Exact evidence is
`research/common_anchor_terminal_unit_growing_source_boundary.md` and its
Python/JSON replay.

### All-index prime-gap source exclusion above `T/5`

Nagura's 1952 theorem gives, for every `T>=25`, a prime

```text
T<p<6T/5.
```

Every terminal index `ell>=3` has `T=AB>=40`.  Write `p=T+i`.  If a legal
point has `a>=T/5`, then `5i<T<=5a`, so the target product contains the
factor `T+i=p`.  The terminal Pell identity and consecutive-Fibonacci
bounds give

```text
X=T+A^2-1, p<X<2p,
X mod p=X-p=A^2-1-i.
```

Legality gives `a+b<=A^2-2-a`, and hence

```text
(X mod p)-(a+b)>=a+1-i>=2.
```

Thus `v_p(L_(a+b))=0` while `v_p(W_(a,b))>=1`.  This proves uniformly for
every `ell>=3` and every legal point with `a>=T/5` that
`W_(a,b)` does not divide `L_(a+b)`.

The conclusion applies without finite extrapolation to both existing
floor-defined pseudopoints for every `ell=4h+2`.  Their smaller first
coordinate is `floor(17A^2/50)`, and the preserved bound
`B/A<13/8` gives

```text
5 floor(17A^2/50)>=17A^2/10-5>13A^2/8>AB=T
```

from the base `A=89`; the other first coordinate is larger.  Hence neither
point can satisfy full point-dependent source divisibility at any family
index.  The exact residual is `a<T/5`; this theorem does not exclude that
region, the terminal two-zero branch, or `C-T5`.  Evidence is
`research/common_anchor_terminal_unit_prime_gap_source_boundary.md`, its
Python/JSON replay, the official Nagura excerpt, and the dedicated typed
Jacobian records.

### Pell-companion remainder determinant boundary

For

```text
P_(a,b)(X,Z)
 =product_(r=1)^(a+b)(X-r)
  -product_(i=1)^a(Z+i) product_(j=1)^b(X+Z-j),
Q_X(Z)=Z^2+XZ-X(X+1),
```

monic division in `Z[X][Z]` gives a unique remainder
`U_(a,b)(X)Z+V_(a,b)(X)`.  At the terminal roots `T,-H`, exact
interpolation gives

```text
(T+H)U_(a,b)
 =(-1)^(a+b)
   product_(i=1)^a(H-i) product_(j=1)^b(T+j)
  -product_(i=1)^a(T+i) product_(j=1)^b(H-j).
```

For odd `a+b` this is a negative sum.  For even `a+b`, legality gives
`X>2a`, and the ratio of the first positive product to the second is

```text
product_(k=b+1)^a (H-k)/(T+k)>1.
```

Hence `(-1)^(a+b)U_(a,b)(B^2)>0` throughout the legal domain.  In
particular, a terminal zero at `T` has a strictly nonzero companion value
at `-H`.

This nondegeneracy does not yield a new two-point obstruction.  Writing

```text
E_r=P_r(B^2,T),
D_(p,q)=U_pV_q-U_qV_p,
```

one has identically

```text
D_(p,q)=U_pE_q-U_qE_p.
```

Therefore, after `E_p=0` is imposed, `D_(p,q)=0` is equivalent to
`E_q=0`, and conversely after swapping `p,q`.  Equivalently,

```text
(T+H)D_(p,q)=E_p Ebar_q-Ebar_p E_q.
```

The two strict companion values cancel identically when both original
terminal residuals vanish.  Thus the determinant-plus-one-residual system
is an invertible rewriting of the two original product equations, not an
arithmetic enhancement.  This all-parameter degeneration includes the
residual `q_a<T/5` region and retires only the Pell-companion determinant
mechanism.  The terminal two-zero problem remains open.  Exact evidence is
`research/common_anchor_terminal_unit_pell_companion_boundary.md` and its
Python/JSON replay, with a bounded typed Jacobian factorization of one
sample determinant.

### Residual nested-divisibility large-prime boundary

For a residual point `a<T/5`, exact prime offsets give the necessary box

```text
a<g_+(T), b<g_-(H).
```

Indeed, a prime `T+i`, `i<=a`, has oriented source residue
`A^2-1-i>a+b`, while a prime `H-j`, `j<=b`, is larger than `X`.
These are pointwise obstructions, not a uniform bound on either prime gap.

More generally, if `p>a+b` divides `T+i` and
`W_(a,b)|L_(a+b)`, its unique source `r` satisfies

```text
p | Q_i(r), Q_i(r)=r^2+(i+1)r-i^2,
|Q_i(r)|<=5a^2-3a.
```

The zero case is now completely classified:

```text
Q_i(r)=0
iff (i,r)=(F_(2m)F_(2m+1),F_(2m)^2), m>=1.
```

Outside this Fibonacci cancellation locus, a prime at the reviewed
consecutive-product scale obeys only

```text
221a/50<p<=5a^2-3a.
```

Thus the linear lower bound gives uniqueness but does not cross the
quadratic source ceiling. At `ell=22`, the legal nested residual points
`P=(13,1)<Q=(27,2)` and `p=137` give

```text
Q_13(2)=-137,
v_137(T+13)=v_137(X-2)=v_137(H+11)=1,
137>221*27/50, 137>2(27+2).
```

The source `r=2` is already inner and its paired high-side index is
`-11`, so nesting creates no crossing. This is not a full-depth
pseudopair: `1993|(T+1)` and `X mod 1993=1505>29`, excluding both points.
An exact unsigned-64-bit replay checks all `8100` prime-gap-reduced
candidates for `3<=ell<=23` and finds no divisibility point; this finite
miss is not extrapolated.

Consequently the combination of the `221/50` size bound, unique source,
small `Q_i(r)` cofactor, and nested-prefix crossing is exhausted. Closure
would require a new global theorem forcing the relevant greatest prime
above `5a^2-3a` or excluding all smooth/residue alternatives
simultaneously. The full point-dependent divisibility criterion, residual
nested pair, terminal branch, and `C-T5` remain open. Exact evidence is
`research/common_anchor_terminal_unit_residual_nested_divisibility_boundary.md`
and its Python/JSON replay, with a certified typed Jacobian factorization
of `137`.

### All-sufficiently-large terminal thin diagonal

Let `d=a-b` and `theta=21/40`. Baker--Harman--Pintz, Theorem 1,
p. 532, gives a prime in `[x-x^theta,x]` for every sufficiently large
`x`. Applying it directly at `H` and at the translated endpoint
`T+2T^theta`, then using the exact necessary conditions

```text
a<g_+(T), b<g_-(H),
```

shows that every sufficiently large legal integral zero satisfies

```text
a,b<2T^(21/40).
```

The exact product logarithm, with `s=a+b`, is

```text
d log(B/A)
 =b log(1+1/X)
  +sum_(j=1)^s[-log(1-j/X)]
  +sum_(i=1)^a log(1+i/T)
  -sum_(j=1)^b[-log(1-j/H)].
```

The signed integral bounds

```text
0<=-log(1-u)-u<=u^2,
0<=u-log(1+u)<=u^2/2
```

first give

```text
1<=d<(33/2)a^2/T,
a>sqrt(2T/33),
d<66T^(1/20).
```

Keeping the quadratic sums and substituting `b=a-d` gives the uniform
exact-Fibonacci expansion

```text
d log(B/A)
 =[2A/B+B/(2(A+B))]a^2/T+rho,
|rho|<142a^3/T^2<1136T^(-17/40)=o(1).
```

For coordinatewise nested zeros, strict ray concavity and decrease in the
second coordinate give `q_b/q_a<p_b/p_a`, hence the outer cumulative
defect is strictly larger than the inner defect. This is a localization
theorem only: it neither supplies nor excludes a nested integral zero pair.
Exact evidence is
`research/common_anchor_terminal_unit_thin_diagonal_boundary.md` and its
Python/JSON replay. The BHP citation is DOI
`10.1112/plms/83.3.532`, Theorem 1, p. 532; DOI existence has been
resolved, while independent proposition attribution and proof replay are
pending.

### Terminal medium-prime canonical-core boundary

Dusart, arXiv `1002.0442v1`, Proposition 6.8, p. 8, gives a prime

```text
x<p<=x(1+1/(25 log^2 x)) for every x>396738.
```

The first terminal product above this threshold is `T_8=602070`.
Forward application at `T` and an explicit backward conversion at
`H-H/(24 log^2 H)` show that every exact zero from `ell=8` satisfies

```text
a<T/(25 log^2 T), b<H/(24 log^2 H),
d/a<33/(50 log^2 T), d log T/a<33/(50 log T).
```

Thus the intended near-equal regime is explicit, not merely ineffective.
Nevertheless, complete Legendre valuations and all Granville `q=2`
two-digit windows for `a/3<p<=a` give exactly

```text
product_(a/3<p<=a)p^2 | u_(a,b)-v_(a,b),
```

where `u/v` is the reduced original product ratio. This is the original
equation in a finite quotient.

The unique canonical reduction by `TH=X(X+1)` is stronger:

```text
P_(a,a-d)=Q_X S+U_(a,a-d)(X)T+V_(a,a-d)(X),
deg U=2a-d-1, lc U=(-1)^d F_d.
```

At an exact-zero candidate, `|U|>T^(2a-d-1)/4`. For two points,

```text
D_(p,q)=U_pV_q-U_qV_p=U_pE_q-U_qE_p.
```

After imposing `E_p=0`, determinant vanishing is therefore equivalent to
the second original equation; a nonzero determinant retains the
linear-scale multiplier `U_p`. The hoped-for nonzero
`exp(O(d log T))` edge defect does not exist, so the squared-prime height
comparison cannot close the nested-zero branch. Exact evidence is
`research/common_anchor_terminal_unit_medium_prime_defect_boundary.md`,
its Python/JSON replay, the archived Dusart source and excerpt, and the
typed Jacobian multivariate-division record. Independent source attribution
and proof replay remain pending.

### Odd-theta `p=2` local image for columns `(5,6)`

For the genus-four quotient

```text
(T-1)(T-9)(T-25)=384u(u^2-1)(u^2-4),
```

the odd-theta factor degrees over `Q_2` are `12,12,96`, so
`J[2](Q_2)=0` and the true Kummer quotient has dimension four.
Precision-340 Hensel and strict Krasner bounds identify both degree-12
completions. Their exact fake-image projection has rank two modulo the
scalar diagonal, with kernel

```text
span{D_(1,0),D_(9,-1)}.
```

Independent Hecke prime decomposition identifies the remaining component
as fully ramified, `(e,f)=(96,1)`. In its certified maximal-order prime
lattice, `v_P(2)=96`, the square threshold is `192`, and the exact
quadratic-defect filtration gives

```text
D_(1,0):          32,56,64,119                    nonsquare
D_(9,-1):         12,...,180,188, then >=193      square
D_(1,0)D_(9,-1): 12,...,116,119                  nonsquare
```

The middle row contains 43 exact even corrections. The bound `>=193`
crosses `2v_P(2)`, so Hensel proves squareness; the two odd terminal
defects prove nonsquareness. The decisions also satisfy squareclass group
law. Thus the four displayed classes have fake-image rank `2+1=3`, and
their unique fake relation is `D_(9,-1)`. An inspected Jacobian
`prime_field.matrix.rank.compute` call independently returns rank `3` on
the exact quotient matrix.

This does not prove that the four classes form a basis of
`J(Q_2)/2J(Q_2)`: that is equivalent to proving
`D_(9,-1) notin 2J(Q_2)` with a coordinate or finite quotient known to be
faithful on the true local group. The BPS Appendix A `r/tau_*` lift has now
been constructed exactly for each of the two degree-12 whole-orbit
relations. Both characters take the value `+1` on `D_(9,-1)`, with
`v_2(chi-1)=7`, while `v_2(chi+1)=1`; the section-kernel residual margins
are `21,25` and the independent square-identity margins are `16,14`.
Thus these two faithful coordinates detect no obstruction. Triviality of
two characters does not construct a half of the divisor and does not
exclude a nontrivial degree-96 or non-orbit relation coordinate.
Consequently the certified bounds are

```text
3 <= rank(true span of the four displayed classes) <= 4,
3 <= dim(full fake local image) <= 4,
0 <= dim(local true-to-fake kernel) <= 1.
```

If the missing true test proves rank `4`, rank-nullity then strictly gives
fake dimension `3` and kernel dimension `1`. Exact bounded evidence is
`research/k8_56_theta_true_descent_2adic_local_proof.md`, its Python/JSON
certificates, the maximal-order TOML, and the saved Jacobian discovery,
contract, payload, and typed-result records. The degree-12 whole-orbit
route is exhausted; a degree-96 relation calculation or a direct exact
local-halving quotient is a materially different unresolved route.

For the global closure, a 313-bit reduced polynomial and 120-element
compact maximal basis reproduce
`2^222*3^100*58411^28*6179021^28`. PARI `nfinit` produced no structure
at exact 3600- and 7200-second bounds despite sustained CPU and roughly
3.4 GiB RSS; these are implementation limits only. Hecke independently
reconstructs the same compact order from 6751 nonzero basis entries and
computes GRH factor-base bound `803898`. Its durable class/unit relation
run is `k8-56-theta-hecke-class-unit-v3`. The unconditional `S`-class
2-primary bound, 121 independent `S`-unit squareclasses, joint bad-place
kernel, no-omission survivor table, and uniform integral-lift
instantiation remain open. No multiplicity counterexample or
nonexistence theorem follows yet.
