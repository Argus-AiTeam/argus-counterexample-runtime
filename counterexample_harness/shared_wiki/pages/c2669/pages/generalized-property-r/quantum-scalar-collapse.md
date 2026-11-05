---
title: Quantum scalar collapse for R-link traces
description: Published scalar no-go theorems, semidirect front gates, exact SF2 reductions, and the Cycle-14 root-projector contraction boundary.
---

# Quantum scalar collapse for R-link traces

For every zero-framed \(n\)-component R-link \(L\),
\[
W_L=B^4\cup_L n(2\text{-handles})
\]
has zero linking/intersection matrix,
\[
H_2(W_L)=\mathbb Z^n,\quad H_1(W_L)=0,\quad
\sigma(W_L)=0,\quad \chi(W_L)=n+1,
\]
and is spin with a unique spin structure.  For every abelian coefficient
group \(G\),
\[
\delta^*:H^1(\partial W_L;G)\xrightarrow{\cong}
H^2(W_L,\partial W_L;G).
\]

Using arXiv:2205.11385v2, Theorem 8.1, the restricted-quantum-group refined
profile of \(W_L\) is therefore the decorated boundary profile of
\(\#^n(S^1\times S^2)\): every spin or cohomological fiber in the
decomposition is a singleton.  After transporting decorations across a
boundary diffeomorphism, it agrees term by term with the unlink trace
\(\natural^n(S^2\times D^2)\).  Proposition 7.1 then gives equality for the
small-quantum-group scalar \(J_{\bar U}=J_U(-,0)\); in the spin case one
first composes the boundary map with sphere twists, which act transitively
on the spin structures of \(\#^n(S^1\times S^2)\).  Appendix A cannot change
the conclusion because both traces have the same Euler characteristic.

The factorizable inputs already factor through boundary and signature by
arXiv:2105.02789v2.  Thus the factorizable Bobtcheva--Messia inputs and the
restricted/small quantum \(\mathfrak{sl}_2\) scalars and refinements analyzed
in arXiv:2205.11385v2 cannot separate any R-link trace from the unlink trace.
This equality does not prove handle-slide equivalence.

Theorem 3.1 still leaves a precise general branch: for a specified
nonfactorizable unimodular ribbon Hopf \(G\)-coalgebra not covered by a
boundary decomposition,
\[
J_H(U_n,\alpha_1,\ldots,\alpha_n)
=\prod_i\lambda_{\alpha_i}(1_{\alpha_i}).
\]
A GST \(L_3\) test would require a complete oriented crossing diagram and
the Hopf-algebra structural data needed to compute its bead words.  No such
value has been computed, and the non-scalar functor, central-element
deformations, fixed boundary parametrizations, cocores, and ribbon-surface
decorations are not retired.

The full proof and exact computational contract are in
`research/quantum_invariants/rlink-scalar-collapse.md`.

## Semidirect \(N_4\) no-dotted collapse

The concrete `arXiv:2503.19532v2` example
\[
H=u_{e^{\pi i/4}}\mathfrak{sl}_2\ltimes N_4
\]
is \(4096\)-dimensional and is stated in Propositions 4.21--4.22 to be
unimodular, ribbon, and strongly nonfactorizable.  Its ordinary Hopf algebra
structure is the trivial-\(G\) case of Theorem 3.1.  The published
factorizable, cosemisimple, triangular, and Theorem 5.9 hypotheses do not
cover it, while the claimed semidirect product formula remains Conjecture
5.11 rather than a theorem.

For this particular ribbon structure there is nevertheless a shorter exact
collapse.  Its \(R\)-matrix is \(R_{\mathsf z}D\Theta\), its pivot is \(K\),
and neither contains \(X^+\) or \(X^-\).  Antipodes preserve the
\(X\)-free subalgebra.  The left integral, however, is supported only on a
PBW top term containing \(X^+X^-\).  A Kirby diagram without dotted
components never inserts the cointegral, so every component integral
vanishes:
\[
J_H(W)=0
\]
for every such diagram with at least one undotted component.  Consequently
\[
J_H(W_{\mathcal L_3^{ob}})=0=J_H(W_{U_2})=\lambda(1)^2.
\]

This retires only the displayed semidirect \(N_4\) structure on the
no-dotted diagram class.  It neither proves Conjecture 5.11 nor excludes
other semidirect families.  Since the equality is forced before crossing
data enter, no planar PD/Gauss code or bead-word expansion was needed or
claimed.  The source reconciliation, exact applicability matrix, and
integer congruence replay are in
`research/literature/l3-semidirect-hopf-scalar/applicability_matrix.md` and
`research/quantum_invariants/l3_semidirect_hopf_scalar/`.

## Semidirect \(\operatorname{SF}_2\) front gates

The support-reachable candidate
\[
H_{\mathrm{SF}}
=u_{e^{\pi i/4}}\mathfrak{sl}_2\ltimes\operatorname{SF}_2,
\qquad \alpha=1,\qquad \dim H_{\mathrm{SF}}=512
\]
does not repeat the \(N_4\) support collapse.  Writing
\[
A=Z^+\otimes K^2LZ^- - Z^-\otimes K^2LZ^+,
\]
the source monodromy formula becomes
\[
M=M_U\exp(2A),\qquad
\exp(2A)=1+2Z^+\otimes K^2LZ^-
-2Z^-\otimes K^2LZ^+
-4Z^+Z^-\otimes Z^+Z^-.
\]
The four fermion sectors are disjoint row and column blocks, each a
nonzero scalar multiple and permutation of the \(u_q\mathfrak{sl}_2\)
monodromy matrix.  Exact elimination over \(\mathbb Q(\zeta_8)\) gives
\[
\operatorname{rank}M_U=32,\qquad
\operatorname{rank}M=128,\qquad
\dim\ker M=384.
\]
The coefficient functional \(\delta_L\) is an explicit nonzero kernel
witness because no first tensor factor of \(M\) contains \(L\).
An independent direct reduction at
\(\zeta_8\mapsto2\in\mathbb F_{17}\) again gives rank \(128\), and a
Jacobian exact rational replay gives rank \(4\) for the fermionic block.

The bead support reaches the integral top term.  Four explicit local
\(R\)-summands supply \(E^3,F^3,Z^+,Z^-\), and the terminal pivotal
factor supplies \(K^3\).  The selected weighted word evaluates to
\[
\frac{\zeta_8-\zeta_8^3}{2048}\ne0.
\]
This proves only that the bead-generated support is not contained in
\(\ker\lambda\); it is not a summand of the GST evaluation and may cancel
there.

The audited proved collapses do not cover this semidirect input:
factorizability fails by the exact rank, it is not cosemisimple or
triangular, Theorem 5.9 treats the pre-semidirect Nenciu family, and
semidirect factorization remains Conjecture 5.11.  However, the reviewed
open-book record still has no lossless ambient planar projection.  Its
Figure 23(c) vector is a flattened human drawing without endpoint
pairings, over/under data, orientations, or a PD/Gauss code.  Consequently
the two GST component bead words and
\(J_{H_{\mathrm{SF}}}(W_{\mathcal L_3^{ob}})\) remain uncomputed.  No
separator or handle-slide obstruction has been promoted.

The exact matrix, independent replay, source applicability table, and
planar-input inspection are under
`research/quantum_invariants/l3_sf2_hopf_scalar/`,
`research/literature/l3-sf2-hopf-scalar/`, and
`research/l3_openbook/planar_kirby/`.

## Cycle-14 exact semidirect-\(\operatorname{SF}_2\) contraction boundary

Cycle 14 now supplies a frozen zero-framed 64-crossing ordered `[V,Q]`
PD/Gauss code, so the former planar-input gap is no longer the blocker for
this calculation.  The full scalar is nevertheless still **uncomputed**.

Exact exterior-degree filtering leaves 2,084 possible top-sector patterns:
38 single mixed quadratic patterns, 1,406 mixed linear pairs, and 640
self-crossing linear pairs.  For every one of these patterns, the complete
128-bit \(R_{\mathsf z}\) sum can be evaluated by a four-state
component-\(L\)-parity recurrence.  Two implementations, one projecting the
frozen PBW algebra and one cleanroom \(L,P,M\) replay, agree that 1,024 sums
are \(+1\), 1,060 are \(-1\), and none is zero.  Thus this exact Gauss sum
removes \(R_{\mathsf z}\) choices but does not cancel any remaining
\(D\Theta/U\) contraction.

The dense 512-state arc elimination is excluded by a certified treewidth
lower bound: even one `uint32` residue needs at least \(4\cdot512^5=128\)
TiB.  An explicit sparse modular frontier backend also fails within the live
resource envelope.  Exhausting all \(70\cdot58\) cyclic Gauss basepoint
pairs lowers the monotone open-crossing width only from 30 to 24.  At the two
optimal basepoints, the backend reaches 286,720 complete states by event 8,
or creates 5,576,704 unfinished event-10 entries and reaches 1,712,212 KiB
peak RSS before its 60-second stop.  Its four two-crossing controls match the
full PBW evaluator, but these bounded modular runs are performance evidence,
not values of the 64-crossing scalar.

No exact zero or nonzero value, full independent contraction, completed
basepoint/component-order control, global handle-slide obstruction, or
counterexample is claimed.  A different proved symbolic compression remains
open.  The exact reductions, cleanroom replay, bounded sparse probes, and
strict blocker statement are under
`research/quantum_invariants/l3_sf2_hopf_scalar_cycle14/`.

### Unified root-projector fusion still does not close the Cycle-14 scalar

Writing \(q=\zeta_8^2\) and
\[
P_j=\frac14\sum_{a\in\mathbb Z/4}q^{-aj}K^a
\]
gives the exact Fourier identity
\[
D=\sum_{i,j\in\mathbb Z/4}q^{ij}P_i\otimes P_j.
\]
The relations \(P_iE^n=E^nP_{i-n}\) and
\(P_iF^n=F^nP_{i+n}\) preserve
\(\sigma=s+e-f\pmod4\) on \(E^eF^fP_s\).  Separating the four values of
\(\sigma\) therefore reduces every component arc from 64 \(U\)-PBW states
to the 16 exact \(E/F\)-degree states.  The \(\Theta\) exponent is recovered
from adjacent degree changes, and
\([E^3F^3K^3](E^3F^3P_s)=q^{-3s}/4\) closes the transformed model without
approximation.

The 2,084 \(R_{\mathsf z}\) signs also compress exactly: the 1,444 mixed
patterns form a rank-one \(38\times38\) sign matrix, and the 640 self
patterns form a rank-one \(32\times20\) matrix.  A parity-defect bit and two
independent square-zero pairs give the exact seven-lane algebra
\[
1,X,Y,XY,S,T,ST.
\]
The \(XY\) lane now executes every mixed pattern and the \(ST\) lane executes
every self pattern; nonconstant mixed/self cross-products vanish because
they represent no allowed exterior-top pattern.  The earlier implementation's
component-word order was nevertheless wrong: it combined reverse Gauss
traversal with right multiplication, rather than reverse/left or the
equivalent forward/right convention.  A new implementation that does not
import the symbolic solver found the defect by comparing every surviving
\(\mathbb Q(\zeta_8)\) PBW coefficient, then passed all four signed mixed and
four signed self controls after correction.  The projector replay passes
41 two-prime checks, and the unified executable fuser passes 16 two-prime
mixed/self comparisons.  In particular, the self control is nonvacuous:
its individual pattern top coefficients are nonzero before exact
coefficientwise cancellation.

The 16 degree states still have exact observability rank 16 under the
allowed bead actions, so a weight-only or smaller linear quotient loses
closing information.  Searching all 4,060 cyclic cuts still gives 22
heuristic-width-12 cuts.  At the fixed representative cut
\((V,Q)=(8,30)\), adding all 640 self patterns multiplies factor-table key
support by only \(5/4\) and nonzero lane support by \(8/7\), so the fused
self implementation is not the source of the earlier explosion.  The old
100-million-entry target runs used the wrong word order and are superseded.
With the corrected order, a 500,000-entry factor table reaches 773,120 keys
at step 23 and emits no coefficient.

A structurally different exact backend stores the same seven-lane functions
as canonical 32-way algebraic decision diagrams.  It agrees with the
factor-table implementation in all seven lanes, all 16 projector-sector
pairs, two primes, and eight signed mixed/self controls (256 comparisons).
At the fixed Cycle-14 cut it compresses the step-23 table to 180,754 live
nodes and completes step 24.  A declared 2,000,000-node run reaches 41 of
126 eliminations with 1,146,255 live nodes; marginalizing step 42 reaches
2,000,001 nodes and emits no coefficient.  This is a bounded failure of
that ADD order, not a scalar value or an impossibility theorem.

The The 28-crossing diagram before the two Rolfsen blowdowns cannot replace this
calculation: the relevant unit-framed semidirect ribbon factors have
\(\lambda(v^{\pm1})=0\), so the blowdown operation cannot be inverted by
normalization.  The exact identities, full-PBW controls, rank certificate,
cyclic-cut search, and bounded contractions are under
`research/quantum_invariants/l3_sf2_hopf_scalar_symbolic/`.  The full
\(\mathbb Q(\zeta_8)\) scalar, independent complete replay, and scalar-level
basepoint/component-order controls remain absent; no handle-slide
obstruction follows.

## Ribbon-corrected semidirect-\(\operatorname{SF}_2\) framing control

The earlier all-framing extension was invalid: it represented a framing
change by a power of the finite-order pivot.  The
Beliakova--De Renzi crossing-plus-extrema walk instead gives
\[
\text{negative kink}=\sum R''g^{-1}S(R')=v,\qquad
\text{positive kink}=\sum S(R')g^{-1}S(R'')=v^{-1}.
\]
Thus an integer component framing \(f\) contributes \(v^{-f}\).
The old claim is retained only at \(f_A=f_B=0\), where no kink bead is
present.

Direct reduction for the three \(q=\zeta_8,\alpha=1\) inputs gives
\[
(v_U^2-1)^2=0,\qquad
(v_{\mathrm{SF}}-1)^2=0,\qquad
(v_{\mathrm{sd}}^2-1)^3=0.
\]
These minimal polynomials and
\[
v_{\mathrm{sd}}^n=v_U^nL^n(1-2nZ^+Z^-)
\]
give exact residue-plus-polynomial formulas for every
\(n\in\mathbb Z\), not a finite sample.  The normalized component
integrals are
\[
\lambda_U(v_U^n)=
\begin{cases}-n&n\text{ even},\\0&n\text{ odd},\end{cases}
\quad
\lambda_{\mathrm{SF}}(v_{\mathrm{SF}}^n)=-2n,
\quad
\lambda_{\mathrm{sd}}(v_{\mathrm{sd}}^n)=
\begin{cases}2n^2&n\text{ even},\\0&n\text{ odd}.\end{cases}
\]
Hence the first support-capable layer has zero non-framing crossings
and \(|f_A|=|f_B|=2\); support does not by itself make
\(\Delta\) nonzero.

Two exact implementations with separate component walks, framing
reductions, and PBW reducers computed the crossingless unlink and all
four fixed two-mixed-crossing codes at arbitrary integer framings.
Put \(n_i=-f_i\) and
\[
x(D)=
\begin{cases}
n_An_B-1,&D\text{ is either same-sign Hopf closure},\\
n_An_B,&D\text{ is an RII closure or the crossingless unlink}.
\end{cases}
\]
Their coefficientwise common answer is
\[
J_{\mathrm{SF}_2}(D)=4x(D),
\qquad
(J_U(D),J_{\mathrm{sd}}(D))=
\begin{cases}
(x(D),4x(D)^2),&n_A,n_B\text{ even},\\
(0,0),&\text{otherwise}.
\end{cases}
\]
Therefore
\[
\Delta(D)=J_{\mathrm{sd}}(D)-J_U(D)J_{\mathrm{SF}_2}(D)=0
\]
identically throughout this corrected layer.

The values are not periodic modulo four: on either Hopf closure,
framing \((-4,-4)\) gives the scalar triple \((900,15,60)\), while
\((0,0)\) gives \((4,-1,-4)\).  RII, explicit-kink,
zero-framing, and mirror controls all pass.  This retires only the
crossingless-plus-fixed-two-crossing corrected projection layer.  It
does not prove Conjecture 5.11, compute \(L_3^{ob}\), or provide a
handle-slide obstruction.

The signed PD/Gauss catalog, independent implementations, exact
all-integer reports, comparison, and bounded Jacobian minimal-polynomial
check are in
`research/quantum_invariants/sf2_ribbon_framing_control/`; the source
reconciliation is in
`research/literature/sf2-ribbon-framing-control/`.  Independent Reviewer
replay remains required.

## Semidirect-\(\operatorname{SF}_2\) zero-to-zero projection gap

The omitted, uncompiled `factorizingInvariant.tex` does not prove
Faes--Manko Conjecture 5.11.  Its displayed top powers are off by one:
at \(r=8\), \(E^{r'}F^{r'}K^{r'}=E^4F^4K^4=0\), while the integral top is
\[
E^3F^3K^3Z^+Z^-.
\]
The relevant \(U\)-parity is even because \(3+3=6\).

Correcting these two points does not repair the functor argument.  Let
\[
\mathcal F
=\langle E^eF^fK^aZ^+Z^-:e+a\equiv0\pmod2\rangle.
\]
Then \(\mathcal F^2=0\).  Nevertheless
\[
x=EZ^+,\qquad y=E^2F^3K^3Z^-
\]
satisfy
\[
xy=-E^3F^3K^3Z^+Z^-,
\qquad \lambda_A(xy)\ne0.
\]
Hence no retraction \(q:A\to\mathcal F\) with
\(\lambda_Aq=\lambda_A\) can preserve the transmuted product: the
right side \(q(x)q(y)\) lies in \(\mathcal F^2=0\), while \(q(xy)\) is
detected by the integral.  The normalized semidirect-minus-separated
local defect is exactly \(-2\).

This obstruction is independent of the chosen module complement.
There is still a module-level nuance: the naive PBW coordinate
projection onto \(Z^+Z^-\) is not adjoint-linear, but the retractions
induced through the Hopf maps \(p:A\to\operatorname{SF}_2\) and
\(j:A\to U\) are adjoint-linear.  Thus what fails is the passage from
an adjoint direct summand to compatible BP-Hopf operations, not merely
the existence of a module summand.

The local failure has not yet survived a legal closed evaluation.  Exact
\(\mathbb Q(\zeta_8)\) checks give \(\Delta=0\) for all eight
single-dotted two-incidence closures, all 48 oriented/orderings of the
three-incidence closure, the first 32 two-dotted/two-undotted balanced
closures, and all 16 two-crossing block-order extensions of that
balanced network.  A separate one-dotted/two-undotted network in which
a two-crossing block supplies the missing fermion support also has
\(\Delta=0\) in all 64 incidence, crossing-sign, and block-order cases.
The standard Sweedler powers \(n=1,2,3,4\) also factor, with scalar triples
\[
(J_A,J_U,J_{\mathrm{SF}_2})
=(1,1,1),(32,8,4),(81,9,9),(512,32,16).
\]
Finally, direct use of the published transmuted copairings gives
\[
\begin{array}{c|cc}
&(\lambda\otimes\lambda)w&\lambda\underline\mu w\\ \hline
w_+&(4,-1,-4)&(8,-2,-4)\\
w_-&(4,-1,-4)&(8,2,4),
\end{array}
\]
where each triple is
\((J_A,J_U,J_{\mathrm{SF}_2})\); all four differences again vanish.
These are finite exact exclusions, not a universal proof.  Only the
draft direct-summand-to-functor route is retired; Conjecture 5.11, the
closed counterexample search, and the \(L_3^{ob}\) scalar route remain
open.

The source separation, proof, exact reports, and bounded Jacobian rank
check are under
`research/literature/sf2-zero-to-zero-factorization/` and
`research/quantum_invariants/sf2_zero_to_zero_factorization/`.
Independent Reviewer replay remains required.

## Cycle-14 exact tensor-rank boundary

On the corrected forward/right unified mixed-XY/self-ST factors, natural
component/forward-arc order gives exact local TT ranks \((32,32,64,2)\) for
60 four-arc crossings; the four boundary crossings have ranks
\((32,8,2)\) or \((8,64,2)\).  This is substantially smaller than the
middle rank \(1024\) obtained when the global elimination order is also used
as the local TT order, so the two orders must remain distinct.

Generated-block row-space factorization removes the former materialized-matrix
barrier without changing the 40,000,000-entry matrix cap: every accepted
factorization retains a pivot-minor certificate and is replayed before use.
In the fixed \((0,0)\) sector over \(\mathbb F_{65537}\), the original
mixed-\(X\) suffix reaches 24 complete eliminations.  Its next streamed
\(32768\times6912\) matrix has certified rank lower bound \(4097\), exceeding
the unchanged rank cap \(4096\); this original suffix therefore emits no
coefficient.  The self-\(S\) branch, by contrast, completes the same step 25
with maximum TT rank \(1024\).

The two rank-one \(R_{\mathsf z}\) sign matrices have an additional exact
component-label symmetry.  Relabeling the physical component names transposes
the mixed and self matrices with common signs \(-1\) and \(+1\),
respectively.  Each artificial axis-square term contains two linear choices,
so the sign squares away in every projector sector and Galois embedding:
\[
F_X=F_Y,\qquad F_S=F_T.
\]
Consequently the actual exterior targets require only four degree-two
branches,
\[
F_{XY}=F_{\mathrm{mixed}+}-2F_X,\qquad
F_{ST}=F_{\mathrm{self}+}-2F_S
      =F_{\mathrm{self}+}-2F_T.
\]
The same trace calculation checks all \(512^2=262144\) ordered PBW pairs and
proves both cyclic-basepoint and component-order invariance, covering all
\(70\cdot58=4060\) basepoint pairs rather than sampling them.

Variable sums commute, so a deterministic exact-rank-aware suffix can start
from the immutable step-24 checkpoint.  At its first changed elimination it
selects variable 83, joining current bond ranks with product bound \(1024\);
that step completes in the same declared resource envelope with maximum TT
rank \(278\), whereas the original variable-62 cut fails at rank \(4097\).
This is a measured contraction-tree improvement, not a terminal scalar.

Starting instead from the stronger step-46 checkpoint exposes an exact
six-arc graph separator, but does not yet contract either side.  The canonical
first merge reports a \(10240\times49152\) streamed matrix of rank at least
4097 modulo 65537; its failure rollback did not retain that lower-bound
certificate, so it is not independently accepted evidence.  Two unchanged-cap
alternatives also remain non-conclusive: fusing the full arc-22 sum before
attaching the third factor and literal all-32-state arc-22 slicing each timed
out after 3,600 seconds before a merge or even state 0 was checkpointed.
Neither timeout retires the separator.

### Integer charge lift and exact case reduction

The eight whole-arc blocks above are not the maximal additive blocks.  On the
actual frozen mixed-\(X\) support, exact Hermite and Smith reduction of all
oriented state relations gives the universal reduced grading
\[
\mathbb Z\oplus\mathbb Z/2,\qquad
s=2(4e+f)+p\longmapsto(e-f,p).
\]
The same conservation law holds at source level for the four required
polarized branches, every projector sector, and every Galois specialization:
the latter choices alter coefficients or remove support, but cannot create
off-grade transitions.  All bond vectors in the 13 selected step-46 trains
are already homogeneous for this lift.  Eleven of their 78 cores split
strictly, and the largest stored charge block drops from \(128\) to \(96\).

For the canonical separator tree, an exact cut census gives at most nine live
physical arcs in every compared bond.  Since \(|e-f|\leq3\) on one arc, every
cumulative integer weight lies in \([-27,27]\).  Reduction modulo \(55\) is
therefore injective on every such bond and is the smallest cyclic
realization with that property.  This supplies an executable alias-free
six-arc block theorem without increasing the rank-\(4096\) or
40,000,000-entry limits.  A finer component-coloured parity grading exists
for the mixed-\(X\) lane, but leaves the worst stored block at \(96\), and a
single combined complex linear lane does not preserve that coloured
refinement.

Independent exact algebra also reduces the finite case grid.  The mixed and
self quadratic targets can be obtained in one degree-two coefficient lane by
\[
L=X-Y\mapsto(\zeta_8+\zeta_8^3)t,\quad
XY\mapsto t^2,\quad
S\mapsto\zeta_8^3t,\quad T\mapsto\zeta_8^5t.
\]
Diagonal gauges give
\(A_{s+2a,t+2b}=A_{s,t}\) after the closing factor, reducing 16 projector
sectors to the four parity representatives.  The four Galois embeddings are
not equal; they may instead be carried together in
\(\mathbb F_p[u]/(u^4+1)\).  Thus the nominal \(4\cdot16\cdot4=256\) field
cases reduce exactly to 16 independent field cases, or four direct-product
coefficient-ring cases.  This packages the outstanding contractions but does
not identify their values or bound their global TT ranks.

An exact reconstruction bound is also available.  In the cyclotomic basis
\((1,\zeta_8,\zeta_8^2,\zeta_8^3)\), the normalized answer may be written
with common denominator \(2^{259}\), and every integer coordinate numerator
has absolute value below \(2^{1665}\).  The sharper audited bound requires a
product of 53 specified 32-bit split primes before signed CRT reconstruction
is unique.  A single residue modulo \(65537\), even if zero, therefore cannot
decide any cyclotomic coefficient.

The normalized quantity has also been aligned move-by-move with the
Beliakova--De Renzi \(2\)-handlebody scalar.  The component functional is
\(\lambda(xg^{-1})\), with \(g=K\), and the implemented closing,
\(R_{\mathsf z}\), and two-component integral factors give exactly the
recorded \(-2^{-65}\) raw 16-sector normalization.  Theorem 3.1 therefore
makes it invariant under every ordinary framed component \(2\)-handle slide;
the unlink value is \(\lambda(1)^2=0\).  A nonzero Cycle-14 value would be a
global unstabilized slide obstruction, while a zero value would only retire
this invariant.  No Kirby-I, stabilization, or boundary-only invariance is
being used.

The source locator needed a correction: in `arXiv:2503.19532v2` the
semidirect \(\operatorname{SF}_2\) algebra is Example 4.15 and Proposition
4.16.  Example 4.17 and Proposition 4.18 concern \(N_4\).  The corrected
locator is recorded as a new assumption; the stale assumption was retired
rather than silently relabelled and requires fresh independent source review.

The theorem checks, source-level support audits, contraction implementations,
and bounded Jacobian charge-duality replay are under
`research/quantum_invariants/l3_sf2_hopf_scalar_exact/`.

For the first frozen field case, projector sector \((0,0)\),
\(\zeta_8\)-power \(1\), and \(p=65537\), the reviewed complete merge-3 train
has now been continued exactly through canonical merges 4, 5, and 6.  The
committed checkpoint records maximum exact rank \(512\) and maximum
materialized block size \(39{,}997{,}440\), within the unchanged limits.
The canonical merge-7 cut itself would require
\(2320\cdot17920=41{,}574{,}400\) entries and is therefore excluded by the
entry cap, not by a rank result.  Two alternative trees that first form the
complete \(D B\) boundary are also exactly excluded: both encounter the same
\(5632\times4928\) matrix of full column rank \(4928\) over
\(\mathbb F_{65537}\).  Those certificates retire only those two
parenthesizations.  A third interleaved tree,
\((C(F_{43}(F_{48}F_{49})))F_{16}\), completed variable \(24\) but made no
atomic variable-\(22\) progress in \(7500.4\) wall seconds; it was retired as
a bounded computation only, with no rank conclusion.  The active
minimum-width connected tree is
\[
  (F_{43}(C F_{48}))(F_{16}F_{49}),
\]
with shared sums \((22,119)\), then \((11,118)\), then \((2,12,23)\), under
rank \(512\) and the same entry cap.  Its first product \(C F_{48}\)
completes exactly at maximum rank \(384\).  A raw reverse sweep of the next
product reaches an \(8448\times4734\) streamed matrix at variable \(12\),
charge \(0\), with exact rank lower bound \(4502\), above the unchanged
global factorization cap \(4096\).  Because that matrix still contains
unreachable incoming rows, the report does not treat it as a full-tensor
rank limit.  The active continuation instead computes the exact prefix
through variables \(2,10,11\), sums shared variable \(11\), and applies this
reachable map before meeting the checkpointed reverse suffix at variable
\(12\).  Sparse nonzero-column accumulation, checked exactly against the
dense finite-field product, completes that inner meeting and creates the
downstream outer checkpoint.  The outer raw reverse sweep then completes
suffix variables \(121,117,100,99,24,23,21\), but makes no atomic
variable-\(14\) charge progress in \(6864.6\) wall seconds.  That bounded
stop is not a rank result.  The active nested continuation instead sums
shared prefix variables \(2\) and \(12\), retains variables \(3\) and \(10\),
and meets the stored suffix at variable \(14\), again without changing any
rank or entry limit.

There is still no complete modular projector sum, no four coefficients in
\(\mathbb Q(\zeta_8)\), no CRT uniqueness certificate, and no unlink
separation.  Thus these calculations neither support vanishing or
nonvanishing nor provide a handle-slide obstruction or a Generalized Property
R counterexample.  The code, exact reports, rank certificates, and independent
replay machinery are under
`research/quantum_invariants/l3_sf2_hopf_scalar_tensor/`.

### Local Pfaffian and termwise Ward shortcuts fail

The standard local binary matchgate ansatz fails in the canonical arc-state
encoding
\[
s=2(4e+f)+p,\qquad e,f\in\{0,1,2,3\},\quad p\in\{0,1\}.
\]
For crossing 0, projector sector \((0,0)\), and
\(\zeta_8=4096\in\mathbb F_{65537}\), pinning sixteen of the twenty local
bits leaves a four-bit lane-one slice with
\[
(g_{0000},g_{1111},g_{1100},g_{0011},
  g_{1010},g_{0101},g_{1001},g_{0110})
=(0,0,0,0,512,61425,0,0).
\]
Its necessary even matchgate relation has residual
\[
g_{0000}g_{1111}-g_{1100}g_{0011}
+g_{1010}g_{0101}-g_{1001}g_{0110}
=57377\ne0\pmod{65537}.
\]
An independent reader obtains the same eight entries from the immutable
exported crossing table.  There is also a basis-invariant strengthening for
product changes of the twenty binary wires.  The crossing-0 lane-one
\(6\mid14\) flattening has sixteen structural zero rows, so its
characteristic-zero rank is at most 48; an independently replayed
\(48\times48\) minor has determinant \(4096\) modulo 65537, proving that
the rank over \(\mathbb Q(\zeta_8)\) is exactly 48.  Every bipartite
flattening rank of a pure-spinor/matchgate signature is a power of two, and a
product \(\mathrm{GL}(2)^{20}\) basis change preserves that rank by
invertible left and right multiplication.  Since 48 is not a power of two,
no contraction-compatible product binary basis change repairs this local
tensor.  This does not exclude \(\mathrm{GL}(32)\) mixing within an arc,
mixing the seven coefficient lanes, or a genuinely nonlocal compression.
The corresponding necessary rank test for the larger whole-arc basis group
does not sharpen this result: exact elimination of all seven inequivalent
whole-arc flattenings gives
\[
32,32,32,32,16,1024,1024.
\]
All are powers of two.  Hence whole-arc flattening rank supplies no
obstruction to \(\mathrm{GL}(32)^4\); this is only a failed necessary test,
not evidence that a matchgate basis exists.

The exact \(R_{\mathsf z}\) total \(1024-1060=-36\) also cannot be pulled
out by assuming a pattern-independent \(D\Theta/U\) transfer.  Canonical
patterns 0 and 2 both have scaled \(R_{\mathsf z}\)-sum \(2^{64}\).  At
their common identity-sector crossing 10, the corrected forward/right
endpoint parities are respectively \((0,1)\) and \((0,0)\); the same degree
state \((0,0,1,1)\) has coefficients \(-1\) and \(+1\) modulo 65537.
The exported 32-state factor independently gives these at keys
\((1,1,2,2)\) and \((0,0,2,2)\).  Thus the naive termwise derivation of
\(J_A=-36J_U\) fails.  Grouping by the complete remaining local data does not
restore it.  Retaining identity/nonidentity choice and the exact transformed
\(D\Theta/U\) tensor at every crossing gives 901 tensor-equivalence classes;
their exact normalized \(R_{\mathsf z}\) weights have distribution
\[
-4:80,\quad -2:351,\quad -1:38,\quad +2:352,\quad +4:80.
\]
In particular, no class has zero weight.  An independent reconstruction of
the no-\(R_{\mathsf z}\) algebra reproduces the full census.  This retires
classwise Ward cancellation, but a relation among the values of different
closed networks remains open.  Such a relation also cannot be obtained from
an automorphism of the frozen decorated Gauss diagram: exhaustive
permutation, reversal, and cyclic-shift comparison leaves only the identity,
so all 901 class orbits are nonzero-weight singletons.  More strongly, the
weighted 64-fold residual tensor is already nonzero before arc contraction.
The separable functional that selects the nonidentity blocks at crossings
\(\{0,12\}\), identity blocks elsewhere, and the
\(((0,0,0),(0,0,0))\) bead-pair coefficient at every crossing leaves exactly
patterns \(0,1,32,33\) and evaluates their sum to
\[
4(1/4)^{64}=2^{-126}\ne0.
\]
An independent algebra reconstruction gives the same exact value.  Any
remaining Ward identity must therefore use the actual Cycle-14 arc
contraction; no universal precontraction tensor identity can prove zero.

The exact witnesses and their solver-independent replays are under
`research/quantum_invariants/l3_sf2_hopf_scalar_decision/`.

## Exact \(L_3^{ob}\) planar-input gate

A new pipeline drills the reviewed three-edge \(V_3^{ob}\) carrier directly
from the common PL subdivision, transports the mapping-torus peripheral data,
fills the four fake page cusps, and applies a seeded SnapPy DOR projection.  It
does not infer crossings from the flattened Figure 23(c) vector.  Canonical
crossing ordering and Gauss basepoints make two complete runs byte-identical.
The candidate has 121 crossings, source-oriented event counts \((70,172)\),
marked cusp maps \(+I,-I\) in component order \(Q,V_3^{ob}\), linking matrix
zero, blackboard self-writhes \((0,-3)\), and proposed surface-zero corrections
\((0,3)\).

The candidate is **not accepted as the true \(L_3^{ob}\) diagram**.  Regina 7.0
recognizes its meridian filling as \(S^3\), and the proposed zero filling has
\(H_1=\mathbb Z^2\), but exact connected-sum decomposition in two independently
serialized peripheral bases returns one 44- or 45-tetrahedron prime candidate,
not two minimal \(S^2\times S^1\) summands.  This contradicts the necessary
zero-surgery consequence of the reviewed homeomorphic-lift theorem.  The
planar claim therefore remains open, and no target bead contraction or scalar
comparison is licensed.

The repair must transport the reviewed `beta_2_meridian_lift` and
`gamma_2_zero_longitude_lift` from `component_peripherals.json.gz` directly to
the drilled cusp and prove their coordinates before regenerating the diagram.
The bounded diagnostic and exact replay paths are recorded in
`research/l3_openbook/planar_kirby_exact/result.md`.

### Direct peripheral repair remains blocked at the cap annulus

The reviewed 8-edge \(\beta_2\) meridian and 52-edge
\(\gamma_2\) page longitude have now been followed through the same two
vertex pinches and final loop drill.  The meridian needs one explicit
four-edge continuation in the first two-tetrahedron pinched-ball gadget.
The longitude remains closed through the pinches and needs one two-edge cusp
continuation in each gadget.  After calibrating the temporary cusp
orientation, their chain coordinates form the identity matrix and retain
\(\beta_2\cdot\gamma_2=+1\); the reviewed \(Q\) peripheral pair remains
disjoint.

This still does not identify the surface-zero longitude.  The current radial
map collapses every side-0 edge in all five cocore-boundary cap detours without
exhibiting a ribbon 2-chain.  The first unsupported collapse is cap 0 at
common edge 38, beginning with source edge 1309.  With that rule, both
meridians still fill to \(S^3\), but the declared \(V_3^{ob}\) longitude
filling has
\[
H_1=\mathbb Z\oplus\mathbb Z/5
\]
instead of preserving \(\mathbb Z^2\).  Independent Regina 7.0 replay gives
the same result.  Therefore this cap-collapsing cusp projection is retired;
the source peripheral certificate is not refuted, no replacement slope is
inferred from the torsion order, and planar extraction and bead contraction
remain blocked.  The exact chain and rejection records are under
`research/l3_openbook/planar_kirby_exact/peripheral_repair/`.

An independent source-only replay now sharpens this boundary.  Starting from
the same three hashed inputs, it reconstructs all three local operations and a
171-step finite-vertex removal without consuming the radial compiler or any
target triangulation.  The source-marked \(Q\) basis transports exactly, the
local undo-drill slope gives the \(V_3^{ob}\) meridian, the four page fillings
have \(H_1=\mathbb Z^2\), and the two certified meridians fill to a Regina
7.0-recognized \(S^3\); an independent dual-cell Smith calculation agrees.

The source-only replay again stops at cap 0, common edge 38, source edge 1309.
The source carries the 12-edge cocore-boundary arc but supplies neither its
common-subdivision cusp carrier nor a relative annulus/2-chain.  The tempting
frozen-fiber boundary is actually the undo-drill meridian, not the source zero
longitude.  Therefore no true \(\gamma_2\) slope is installed, no
\(\gamma_2\) filling is run, and the earlier
\(\mathbb Z\oplus\mathbb Z/5\) output is neither reproduced nor refuted by
this replay.  The radial route remains retired, while a distinct source-collar
transport route stays open and must construct the missing relative chain before
planar extraction.

### Exact source-collar transport also fails the longitude gate

The missing local chains can in fact be constructed without using the radial
output.  The reviewed move list consists of one identity isometry followed by
28 flips.  For every flip, the two page complexes and their four-sector common
fan now have explicit ordered degree-\(0,1,2\) bases, sparse integral boundary
matrices, and sparse matrices for both maps into the fan.  Direct matrix
multiplication gives zero coefficientwise residual for
\(\partial_1F_1-F_0\partial_1\) and
\(\partial_2F_2-F_1\partial_2\) on both sides of every span.

The edge coefficients are derived from the signed triangle occurrences in the
oriented quadrilateral boundary, not from unordered endpoint sets.  With radial
edge \(r_k\) oriented from the new center to occurrence corner \(q_k\), every
source diagonal has coefficient \(-1\) in the \(q_0\)-to-\(q_2\) path and every
target diagonal has coefficient \(+1\) in the \(q_1\)-to-\(q_3\) path.  At moves
17, 20, 23, and 26 the source diagonal is a loop after quotienting page
vertices; the two signed triangle occurrences still determine the coefficient
uniquely.  Reversing that coefficient at any one of the four moves makes the
independent verifier exit nonzero.  The verifier does not import the builder:
it reconstructs the bases and matrices from the three fixed source inputs and
treats the generated JSON as an untrusted witness to compare.

In the drilled cusp collar, each side-0 cap edge maps to the \(F\)-to-\(T\)
edge of its barycentric cusp triangle instead of being deleted.  This produces
continuous target arcs of lengths \(12,4,4,4,12\).  For every cap the standard
two-triangle-per-segment cylinder has the exact identity
\[
\partial C_i=a_i-t_i+e_{\partial,i}
\]
with zero coefficientwise residual.  Cap 0 has chain dimensions
\((26,49,24)\), so it exceeds Jacobian's certified 32-generator limit in
degree one; its integer matrix is checked directly.  The binding-\(Q\)
12-triangle annulus, which is not a \(V_3^{ob}\) cap annulus, is within that
limit and Jacobian independently returns
\(H_0=\mathbb Z,H_1=\mathbb Z,H_2=0\).

All five transported arcs and the remaining source segments assemble to a
68-edge barycentric representative of the 52-segment source
\(\gamma_2\), and the oriented peripheral basis satisfies
\(\beta_2\cdot\gamma_2=+1\) with determinant one.  This local success does not
pass the global zero-longitude test.  Starting afresh from the three reviewed
source inputs, both Regina and an independent integer dual-cell boundary
matrix give
\[
H_1=\mathbb Z\oplus\mathbb Z/5
\]
after the \(V_3^{ob}\) single-longitude filling and again after the
\(Q,V_3^{ob}\) double-longitude filling.  Thus the source-collar rule repairs
the empty carrier but fails the global homology gate in the same
\(\mathbb Z\oplus\mathbb Z/5\) way as the old radial computation.  Equality
of those homology groups is not an identification of the two slopes.  This
excludes this exact source-collar map;
it does not prove that no cap annulus exists, refute the reviewed source
longitude, license a slope correction, or establish a handle-slide
obstruction or counterexample.

The source hashes, complete page/common map, cap matrices, Jacobian exchange,
marked six-cusp triangulation, two filling computations, and source-only replay
are under
`research/l3_openbook/planar_kirby_exact/peripheral_repair/source_collar_transport/`.

### The full global collar determines an affine lattice, not one longitude

Expanding the collar calculation to every allowed cell removes the former
shortest-path choice but does not produce a unique target class.  The ordered
relative CW complex has dimensions
\[
(C_0,C_1,C_2)=(394,1203,920).
\]
It contains all 52 source-edge incidence projections, 125 radial edges, ten
forced cap connectors, all 58 connector cells in each of the three
two-tetrahedron gadget components, and all 684 barycentrically subdivided
\(V_3^{ob}\)-cusp faces.  The stored sparse boundary matrices have 2,406 and
2,812 nonzero entries, and all 920 columns satisfy
\(\partial_1\partial_2=0\).

Transformation-certified integer elimination gives a 795-dimensional
homogeneous solution lattice: 684 cusp-face units and 111 gadget
circulations.  Its image in the declared cusp homology coordinates is
\[
L=\mathbb Z(1,0),
\qquad
\{[t]\}=[3,-1]+L.
\]
Thus the full collar permits arbitrary meridian translation and cannot itself
select the surface framing.  The old shortest representative is not a
different affine mechanism: its saved 1,026-coefficient target chain has class
\([1,-1]\), and an explicit combination of one connector circulation and 341
cusp-face units realizes it coefficientwise from the new particular solution.

The particular solution is instead fixed before filling by declared cell order
and a depth-first spanning tree; it calls no shortest-path routine and has
primitive target class \([3,-1]\).  Filling only the four page cusps and
\(V_3^{ob}\) along this representative, while leaving \(Q\) unfilled, gives
\[
H_1=\mathbb Z\oplus\mathbb Z/7
\]
in both Regina and an independently assembled integer boundary matrix.  This
is an exact result for one source-linked integral relative 2-chain, not an
embedded annulus and not a refutation of every class in the affine lattice.
It therefore retires only the full collar as a unique compiler; the source
zero-longitude premise, another affine representative with independent
geometric meaning, and a non-radial ambient embedding remain unresolved.

The previously inspected Jacobian integral-homology operation is limited to
32 rows and columns, so the 52-segment global complex is outside its typed
contract and was not forced into a run.  The complete bases, carrier records,
boundary matrices, affine transformations, old-chain membership certificate,
single filling, and standalone replay are under
`research/l3_openbook/planar_kirby_exact/peripheral_repair/global_collar_target_class/`.

## Transmuted one-split/one-merge cancellation

The next route uses the actual Beliakova--De Renzi transmutation formulas.
For the legal typed BP word
\[
W_0=\underline\lambda\circ\underline\mu\circ
\underline\Delta\circ\underline\Lambda:0\to0,
\]
two exact implementations with different fields and reducers give
\[
\bigl(W_0(A),W_0(U),W_0(\operatorname{SF}_2)\bigr)=(32,8,4),
\qquad \Delta(W_0)=0.
\]
Grading by the two fermionic skew branches in
\(\Delta(\Lambda)\) and by degree in the fermionic \(R\)-exponential
gives two nonzero cells, \(16\) at degrees \((0,0)\) and \((2,0)\).
Each equals its factorized counterpart separately; all other cells are
zero.

This equality persists on the full reachable fragment rather than only
on \(W_0\).  Pair
\[
\underline\Delta_A(\Lambda_A)
\quad\hbox{with}\quad
\underline\Delta_U(\Lambda_U)\otimes
\underline\Delta_{\operatorname{SF}_2}(\Lambda_{\operatorname{SF}_2})
\]
and saturate over \(\mathbb Q(\zeta_8)\) under
\[
c^{\pm1},\quad
\underline S_1^{\pm1},\quad
\underline S_2^{\pm1},\quad
v_1^{\pm1},\quad v_2^{\pm1}.
\]
The exact invariant span has dimension \(42\).  All \(420\) generator
images reduce to recorded basis coordinates, and the restriction of
\[
\lambda_A\mu_A-
(\lambda_U\mu_U)\otimes
(\lambda_{\operatorname{SF}_2}\mu_{\operatorname{SF}_2})
\]
has rank zero.  The reviewed ribbon minimal polynomials and explicit
inverse elements make this an all-integer-framing statement, not a
finite framing sample.

The local product-defect coordinate
\[
(EZ^+)\otimes(E^2F^3K^3Z^-)
\]
already occurs in the root state and in 21 basis representatives.
Its complete paired input is nevertheless outside the reachable span,
and every reachable occurrence cancels under the closing functional.
Thus support reaches the defect but no scalar defect survives in this
entire fragment.

This is a computer-assisted exact factorization theorem only for words
with one split, one merge, and the listed intervening operators.  It
does not cover another split or merge, a copairing insertion, or every
\(0\to0\) BP morphism; hence it neither proves Conjecture 5.11 nor
computes an \(L_3^{ob}\) scalar or a handle-slide obstruction.  The
source contract, two \(W_0\) computations, saturated basis, and closure
certificates are under
`research/literature/sf2-transmuted-defect-closure/` and
`research/quantum_invariants/sf2_transmuted_defect_closure/`.
Independent Reviewer replay remains required.
