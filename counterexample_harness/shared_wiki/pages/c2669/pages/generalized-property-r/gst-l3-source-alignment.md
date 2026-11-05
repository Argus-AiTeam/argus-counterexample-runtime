---
title: GST L3 source alignment
description: Source-level identification of the campaign-2669 candidate, including the unresolved Meier-Zupan/Diao-Pan-Yan slope-sign convention.
---

# GST L3 source alignment

## Scope verdict

The designated sources fix the GST/Scharlemann candidate
\[
L_3=L_{3,1}=Q\cup V_3
\]
and its zero-framed surgery. They do **not** presently give a source-level
identification between Meier-Zupan's parameter \(-6/7\) and Diao-Pan-Yan's
parameter \(+6/7\). They also provide no invariant separating \(L_3\) from the
unlink under every unstabilized handle slide. Thus \(L_3\) remains a potential
counterexample, not a counterexample.

## Exact GST/Scharlemann object

- \(Q=T_{2,3}\#\overline{T_{2,3}}\) is the square knot.
- \(V_3=T_{3,4}\#\overline{T_{3,4}}\).
- GST Figure 1 and its following paragraph support precisely the
  \(L_{n,1}=Q\cup V_n\) component types and describe the \(+1\) and \(-1\)
  labels as full twists in the spiral presentation of \(V_n\). That passage
  neither defines general \(L_{n,k}\) nor states surgery framings.
- GST Corollary 6.4 places the relevant second component, after slides over
  \(Q\), on a square-knot fiber as a lift of an essential pillowcase curve.
  This is a fiber-position classification, not an unlinking theorem.
- GST Section 7 gives
  \[
  S^3_0(L_{n,k})\cong \#^2(S^1\times S^2).
  \]
  Proposition 2.2 says that any specified framing producing this surgery must
  be the zero framing on every component (and that the components are
  algebraically unlinked). Applied to the Section 7 conclusion, it fixes both
  surgery coefficients of \(L_{3,1}\) as \(0\). Thus \(L_{3,1}\) is a
  two-component R-link. This verifies the hypothesis of Generalized Property R
  and supplies no orbit obstruction.

## Parameter crosswalk

Scharlemann identifies his \(L_n=Q\cup V_n\) with GST's \(L_{n,1}\). His
Theorem 4.1 assigns the pillowcase slope
\[
s_{\mathrm{GST/SCH}}=\frac{n}{2n+1},
\qquad s_{\mathrm{GST/SCH}}(L_3)=\frac37.
\]

Meier-Zupan Remark 4.12 explains that the \(q=2\) branched-cover coordinate
change doubles the numerator and that their slopes switch signs:
\[
\frac13,\frac25,\frac37
\longleftrightarrow
-\frac23,-\frac45,-\frac67.
\]
Thus their stated dictionary is
\[
s_{\mathrm{MZ}}=-2s_{\mathrm{GST/SCH}},
\qquad \frac37\longmapsto-\frac67.
\]

Diao-Pan-Yan instead write
\[
L_n\sim L\!\left(3,2;\frac{2n}{2n+1}\right),
\qquad L_3\sim L(3,2;6/7).
\]
None of the designated passages supplies the orientation reversal, deck
transformation, mirror convention, or framed-link calculation needed to turn
the Meier-Zupan minus sign into the Diao-Pan-Yan plus sign. Proposition 1.4 of
Meier-Zupan constructs \(L^{p,q}_{c/d}\) as an R-link when \(c\) is even; it
does not identify the \(+c/d\) and \(-c/d\) links.

The exact arithmetic \(-2\cdot(3/7)=-6/7\) was checked through the isolated
Argus Jacobian adapter:

| Field | Recorded value |
|---|---|
| Server | `jacobian` 0.14.0 |
| Protocol | `2025-11-25` |
| Operation | `algebraic_number.multiply.compute` |
| Typed input | Two `RealQuadraticValue` values in `Q(sqrt(2))`, with zero radical coefficients |
| Exact output | rational part `-6/7`, radical coefficient `0/1`, radicand `2` |
| Adapter status | success; no structured error or timeout; runtime 1 ms |
| Payload | `research/jacobian/slope-conversion-payload.json` |
| Full typed output | `research/jacobian/slope-conversion-output.json` |

This operation verifies only rational multiplication. It does not prove that
the \(+6/7\) and \(-6/7\) framed links are topologically identical.

## Group-presentation notation

GST use
\[
\langle x_G,y_G\mid y_Gx_Gy_G=x_Gy_Gx_G,\;
x_G^{n+1}=y_G^n\rangle.
\]
Meier-Zupan and Diao-Pan-Yan use
\[
\langle x_L,y_L\mid x_Ly_Lx_L=y_Lx_Ly_L,\;
x_L^n=y_L^{n+1}\rangle.
\]
The substitution \(x_L=y_G,\ y_L=x_G\) gives the later presentation exactly.
No change of \(n\), inversion, or mirror operation is needed for this
presentation-level crosswalk. This generator renaming does not resolve the
pillowcase slope-sign issue.

## Known status and stabilization boundary

- GST Section 8 and Diao-Pan-Yan's introduction record exact unstabilized
  simplifications for \(L_0,L_1,L_2\).
- Diao-Pan-Yan state that exact GPRC remains unknown for \(L_n\), \(n\geq3\).
  Hence \(L_3\) is the first unresolved member of this indexed family.
- GST prove weak simplification of \(L_{n,k}\) after adding a Hopf pair.
- Meier-Zupan prove Weak Property 2R for generalized square knots using at
  most two Hopf pairs, improved to one in the \(q=2\) case.
- Diao-Pan-Yan Theorem 1.1(1) states that, in its convention, \(L_3\) is
  stably handleslide equivalent to \(L(4,3;2/3)\). Part (2) proves stable
  triviality only for \(L(3,2;4/d)\) in its stated finite range, not for
  \(L(3,2;6/7)\).

Stable GPRC permits distant zero-framed unlink components, corresponding to
canceling 2/3-handle pairs. Weak GPRC also permits Hopf pairs, corresponding to
canceling 1/2-handle pairs. Neither conclusion supplies a slide sequence or an
obstruction for the original two-component link. Standardness of an associated
homotopy 4-sphere likewise does not imply exact handleslide triviality of the
original attaching link.

GST establish only the implication
\[
L_n\text{ exact handleslide trivial}
\Longrightarrow
P_n\text{ Andrews-Curtis trivial}.
\]
No cited source proves that \(P_3\) is Andrews-Curtis nontrivial. Belief,
homology checks, group consistency, or failure of a bounded slide search is
not a counterexample certificate.

The exact \(P_3\) tuple has now been matched to the \(n=3\)
Akbulut--Kirby tuple in Borovik--Lubotzky--Myasnikov. Their finite-group
theorem, together with the unimodular exponent-sum matrix, rules out every
unadorned finite-quotient AC graph as a separator. See
[Finite-quotient AC no-go for GST P3](finite-quotient-ac-no-go.md).

## Source locators

| Source | Required passages | What they support |
|---|---|---|
| GST, DOI `10.2140/gt.2010.14.2305` | Figure 1 and following paragraph; Proposition 2.2; Corollary 6.4; Sections 7, 8, 9, 10; Proposition 10.1 | \(L_{n,1}\) component types and full twists; zero framing from Proposition 2.2 plus Section 7 surgery; fiber position; small-\(n\) cases; AC implication; weak result |
| Scharlemann, `arXiv:1208.1299v3` | Introduction; Section 4, Figure 25, Theorem 4.1 | \(L_n=L_{n,1}\) and slope \(n/(2n+1)\) |
| Meier-Zupan, `arXiv:1904.08527`, DOI `10.4310/jdg/1668186788` | Proposition 1.4; Remark 4.12; Theorem 1.2; Proposition 7.3; Remark 7.4 | \(L^{p,q}_{c/d}\) construction, doubled negative slope, weak result |
| Diao-Pan-Yan, `arXiv:2604.17737v1` | Introduction; Theorem 1.1 | Positive parameter convention, current open status, bounded stable equivalences |

The proposition-level assumptions and the retired routes are recorded in
`research/MATH_STATE.json`. The retained scope attributions have independent
Reviewer support, including the narrowed Figure 1 assumption and the
Proposition 2.2 application confirmed in the second scope review. The new
solve-stage constructions below remain pending independent review.

## Earlier bounded reconstruction boundary (superseded by Cycle 14)

Before the primary Kirby reconstruction in Cycle 14, the Scharlemann \(3/7\)
fiber representative had only the following machine-readable
**abstract** curve encoding:

- `research/l3_reconstruction/pillowcase_3_7.json` fixes a two-square
  pillowcase, branch-point and seam labels, the branch-avoiding development
  line
  \[
  (x,y)=(13/100,29/100)+t(3,7),\qquad 0\leq t\leq2,
  \]
  its 20-letter seam word, and the closed six-sextant sheet sequence;
- `research/l3_reconstruction/render_pillowcase.py` checks those words and
  redraws `pillowcase_3_7.svg` deterministically;
- the line crosses the top and bottom seams seven times each and the left and
  right seams three times each. Its chosen lift starts and ends on sheet \(0\),
  while adding \(2\) or \(4\) modulo \(6\) gives the other two lifts.

This was a finite construction of the post-slide curve on the abstract
square-knot fiber. It is **not** a PD, Gauss, DT, or braid-with-axis code for
the original GST Figure 1 embedding in \(S^3\). In particular, `Ln1.eps`
leaves the \(n\)-strand spiral and covered connection regions parametric, and
the Scharlemann proof explicitly does not give the bands for the slides that
put \(V_3\) on the fiber. The partial component specification and the exact
missing data are recorded in
`research/l3_reconstruction/l3_framed_link_spec.json`.

## Earlier zero-surgery certificate boundary (superseded by Cycle 14)

Before Cycle 14, `research/l3_reconstruction/kirby_boundary_argument.json`
replayed only what GST
Section 7 actually supplies. The argument dualizes a handle decomposition,
slides auxiliary components, cancels an auxiliary pair, changes a bracketed
\(0\)-framing to \(+1\) by a slide over a \(-1\)-framed component, and finally
blows down bracketed \(+1\) and \(-1\) circles to obtain \(L_{n,1}\). For the
quantified slide, compatible orientations give linking number \(-1\), so the
new coefficient is
\[
0+(-1)-2(-1)=+1.
\]

This proves the surgery boundary through dual handles, but it does not give a
local Kirby sequence beginning at a crossing-level \(L_3\) and ending at a
standard \(0\)-framed two-component unlink. The Section 10 sequence additionally
uses a Hopf pair. Blow-downs, auxiliary cancellations, and that Hopf pair are
not moves in the original unstabilized two-component handle-slide problem.

## Positive/negative slope isolation

With slope \(a/b\) represented by \((a,b)^T\), the \(q=2\) coordinate
conversion in Meier--Zupan is
\[
\begin{pmatrix}-2&0\\0&1\end{pmatrix}
\binom{3}{7}=\binom{-6}{7}.
\]
It has determinant \(-2\), so it is a covering-coordinate conversion rather
than a pillowcase automorphism. The reflection
\(\operatorname{diag}(-1,1)\) sends \((-6,7)\) to \((6,7)\) and respects the
two branch-order rows when realized as the vertical-axis reflection. Its lift
therefore relates abstract closed-fiber multicurves. The cited sources do not
show that this lift extends across the relevant filling as a component-labelled
map of the exact \(S^3\) links while tracking the selected derivative curves
and their framings.

Diao--Pan--Yan explicitly use \(L(p,q;c/d)\) only up to handle slides and also
for stably equivalent representatives. Their paper says the core construction
algorithm will appear elsewhere; the arXiv source contains no program or data,
and the printed summary has unresolved variable and branch errors. Consequently
their \(+6/7\) computations are **not safe input for an invariant of the exact
GST \(L_3\)**. This does not prove that the \(+6/7\) and \(-6/7\) links differ;
the exact link identification remains unresolved. The coordinate calculations
and the remaining extension obligation are in
`research/l3_reconstruction/slope_sign_analysis.json`.

## Jacobian boundary and algebraic cross-check

The installed Jacobian catalog contains no framed-link reconstruction, Kirby
move, Dehn-surgery, pillowcase-cover, or knot-diagram operation. The inspected
nearest operation was
`matrix.normal_form.smith.certified.compute`. Applied to the zero \(2\times2\)
linking matrix, it returned certified rank \(0\) with no invariant factors.
This is only the expected \(H_1\cong\mathbb Z^2\) cross-check; it neither
identifies the surgery manifold nor certifies any handle-slide sequence.
The exact contract, payload, output, server metadata, and applicability
assessment are under `research/jacobian/`.

## Cleanroom marked-monodromy bridge exclusion

A source-only reconstruction now starts from the reviewed
`openbook_spec.json` and no other project input. An empty-root mount namespace
exposes only the sealed copy, the builder or verifier, and its output
directory; the old mapping-torus, slope, diagram, and filling paths are
unresolvable. Independent implementations recover the six-face cellular
boundary maps with ranks \(3\) and \(5\), the integral ordered basis
\((a_+,b_+,a_-,b_-)\), its intersection form, the disjoint oriented \(Q\) and
\(V_3^{ob}\) embeddings, positive meridians, page-zero longitudes, all four
CW-vertex filling slopes, and the capped rotation
\[
S=\begin{pmatrix}
1&1&0&0\\-1&0&0&0\\
0&0&1&1\\0&0&-1&0
\end{pmatrix}.
\]
The sealed reconstruction and its independent replay are under
`research/l3_openbook/source_marked_exterior_cleanroom/`.

Only after that seal was fixed was the old fourteen-triangle page copied into
`research/l3_openbook/quarantine/source-finite-lineage-cycle4/`, excluding its
layered bundle and every downstream filling choice. Its recorded signed-edge
map is a genuine orientation-preserving simplicial bijection: all 21
underlying edges and all 14 oriented triangles map bijectively. It transports
the compact \(Q\)-annulus, the oriented weight-36 \(V_3^{ob}\) curve, both
component framings, and the four page-vertex links. It also sends each oriented
theta-ribbon basis curve to the equally named target curve, so its induced
candidate is \(P=I_4\). This candidate is unimodular and symplectic but does
not satisfy \(TP=PS\), where the quarantined boundary-fixed word acts by
\[
T=\begin{pmatrix}
0&1&0&0\\-1&1&0&0\\
0&0&1&-1\\0&0&1&0
\end{pmatrix}.
\]

The failure is not limited to that candidate. With the declared intersection
form \(J\), associate to a symplectic monodromy \(M\) the symmetric form
\[
B_M=J(M-M^{-1}).
\]
Any symplectic conjugator would force \(P^TB_TP=B_S\). Exact arithmetic gives
\[
B_S=\begin{pmatrix}
-2&-1&0&0\\-1&-2&0&0\\
0&0&-2&-1\\0&0&-1&-2
\end{pmatrix},
\qquad
B_T=\begin{pmatrix}
-2&1&0&0\\1&-2&0&0\\
0&0&2&-1\\0&0&-1&2
\end{pmatrix}.
\]
Their exact LDL pivots are respectively
\((-2,-3/2,-2,-3/2)\) and
\((-2,-3/2,2,3/2)\). Thus their inertias are \((0,4,0)\) and
\((2,2,0)\), so Sylvester's law excludes congruence over \(\mathbb R\).
Consequently no element of \(Sp(4,\mathbb Z)\), and hence no
orientation-preserving page homeomorphism, conjugates these two marked
monodromies. This is a complete obstruction, not a bounded search miss.

Jacobian operation `matrix.normal_form.smith.certified.compute` independently
returns a certified rank-eight Smith form for the full 16-variable linear
system \(TP-PS=0\). That typed result describes the unrestricted integral
linear solution lattice; the inertia argument is what excludes its symplectic
points. The exact payload, typed output, local certificate, and independent
replay are
`jacobian_smith_payload.json`, `jacobian_smith_result.json`,
`bridge_obstruction.json`, and `bridge_obstruction_verification.json` in the
cleanroom directory.

This refutes only the proposed bridge to the quarantined fourteen-triangle
monodromy. It does not refute the reviewed GST open-book representative or
zero-surgery theorem, and it produces neither a replacement mapping torus nor
a handle-slide obstruction. A later route must correct the source
marking/monodromy identification rather than reuse any descendant of this
finite lineage.

## Cycle 7 source-only adjudication

The value-free cycle-7 projection fixes source labels, component orientations,
the selected lift branch, theta markings, the verifier, marked-isomorphism
contract, status codes, and sealing policy before either isolated reducer runs.
Its public identifiers are:

| Item | Value |
|---|---|
| Projection SHA-256 | `94e857d7f400eb804a6eb11f41022f6e8e693432a427490fc066886a0de47e06` |
| Preregistration SHA-256 | `0741c860cbfb856e5f6ecdd646dc42d7c83fe406dccf2073123158153a56ebc8` |
| Private archive SHA-256 | `1fe01df28250f7c66c56a54d1e7c73a09afdca4a85e38ee35cb1b0457538557a` |
| Phase codes | `FROZEN_BEFORE_REDUCERS`, `PACKET_VALID`, `MARKED_ISOMORPHIC`, `NON_ISOMORPHIC`, `SEALED_PRIVATE` |
| Adjudication category | `NON_ISOMORPHIC` |

Both independently implemented packets pass their frozen derivational replay
and are connected by explicit mutually inverse marked chain maps. Independent
review nevertheless rejected the resulting `NON_ISOMORPHIC` conclusion:
neither reducer nor the reference replay uses the anchor geometry to select a
ribbon frontier, and their derived marked intersections do not satisfy both
source declarations. The private archive remains useful only as a record of
that failed route. Its monodromy and peripheral conclusions are not accepted.

This bounded adjudication is not a surgery certificate, a handle-slide
obstruction, or a Generalized Property R counterexample.

## Cycle 8 anchor-aware ribbon adjudication

Cycle 8 froze the Cycle 7 source projection and its read-only archive before
running two new local algorithms. One algorithm constructs derived
neighborhoods from positive oriented face sectors; the other independently
constructs the dart rotation system and annular face orbits. They agree on
every theta-vertex cyclic order and derive exactly two frontier components for
each named theta cycle.

The projection does not, however, define the `P-*` anchors sufficiently to
select either frontier. It gives only the strings `P-TL`, `P-TR`, and `P-BR`;
there is no anchor-to-face-sector incidence. Even reading each suffix as a
corner leaves two complementary sectors. Two distinct completions remain
compatible with the explicit rule that paired curves occupy opposite sides of
their shared spine edge:
\[
(a_+,b_+,a_-,b_-)=(L,R,L,R)
\quad\text{or}\quad
(R,L,R,L).
\]

The adjudication status is therefore `SOURCE_UNDERSPECIFIED`. No selected
frontiers exist, so no local signed-crossing list was promoted, the two source
intersection declarations were not compared, and no monodromy or peripheral
reducer was run. The minimal repair is a per-curve record binding the existing
anchor label to one incident oriented face-sector and hence to a unique
frontier. The replayable certificate is under
`research/l3_openbook/source_ribbon_cycle8/`.

This is an underdetermination of the current finite projection, not evidence
that no source-level marking exists.  A later source-complete replay confirms
that the omitted incidence is present in the original fourteen-triangle
subdivision, so the Cycle 8 verdict must not be broadened from its frozen
projection to `openbook_spec.json`.

## Cycle 9 source-complete ribbon sign gate

The source-complete projection now derives
\[
P=(13/100,29/100)
\]
directly from `pillowcase_curve.development.(x0,y0)` and verifies that it lies
strictly inside the declared face-0 cap disk.  It cones face 0 from \(P\) to
the four corners and splits faces 1 through 5 along their oriented
`TL-to-BR` diagonals.  All 14 oriented triangles, 21 oriented edges, 42
oriented triangle sectors, and `P-*` incidences are explicit.  Cancelling the
auxiliary `P-*` edges and diagonals recovers the original six-face CW chain
complex face by face.

The orientation is the one used by the original source replay: a front face
has cellular boundary `-(T+R+B+L)`, while a back face has boundary
`T+R+B+L`.  With every frontier oriented with degree \(+1\) over its stored
theta path, both independent constructions select
\[
(a_+,b_+,a_-,b_-)=(R,L,R,L).
\]
The barycentric normal-arc construction and the independent
rotation-system/chord-alternation construction both give one plus crossing at
vertex `b` with sign \(+1\), and one minus crossing at vertex `k` with sign
\(-1\).  Thus, in the ordered theta basis,
\[
J_{\mathrm{derived}}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix}.
\]
This form is alternating and unimodular, but it conflicts with the source
text, which declares both \(a_+\cdot b_+\) and \(a_-\cdot b_-\) to be \(+1\).
The discrepancy is local and precedes every packet, monodromy, mapping-torus,
or peripheral calculation.

Accordingly, the complete source geometry repairs the Cycle 8 incidence gap
but does not pass the source packet gate.  A subsequent route must correct or
justify the minus theta-path orientation, the semantic use of its anchor, or
the source intersection declaration before any downstream reducer runs.
Replayable normal arcs, half-edge cycles, mutations, and the minimal conflict
witness are under
`research/l3_openbook/source_complete_ribbon_cycle9/`.  This solve-stage
conclusion remains subject to independent review.

The mutation evidence is content-level.  Reversing the oriented `P-TL` edge
while preserving its underlying geometric edge keeps the selected
`a_plus:right` frontier but reverses the oriented anchor--frontier local sign.
A separate valid cyclic re-pairing of the three back-face `L` seams changes the
actual vertex rotations; both local algorithms then add crossings `r:-1` and
`w:+1`, making both pair totals zero.  The replay identifies exact stale
anchor, normal-sector-cycle, half-edge-rotation, and local-sign fields rather
than treating a changed file hash as certificate invalidation.

## Cycle 10 primary reflection marking

Two reconstructions were completed before comparison.  The vector route reads
the TeX and the named EPS/PDF figures; the textual route reads only the TeX.
Both identify \(S_-\) as the outer left-trefoil punctured hexagon, \(S_+\) as
the inner reflected right-trefoil punctured hexagon, and the reflection as
orientation reversing across the inner circle.  The source fixes the
top--middle--bottom theta-arrow relation, but it puts no arrows on the
individual doubled twist curves and does not select an absolute color-to-CW
cyclic phase.

Consequently the Cycle 9 minus sign is a property of its degree-\(+1\)
frontier orientation convention, not a contradiction in the underlying
source curve.  Cycle 10 keeps both \(a\)-orientations and reverses \(b_-\):
\[
D=D^{-1}=\operatorname{diag}(1,1,1,-1),\qquad
J_{\rm v2}=D^TJ_9D=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]
This is explicitly declared orientation gauge, not a source fact.  The four
anchor-selected geometric frontiers remain \(R,L,R,L\), while both independent
local certificates now give plus \(=+1\) and minus \(=+1\).

The source fixes the clockwise order-six rotation but does not state an
\(a,b\) factor word.  Applying
\[
(a_+,+1),(b_+,+1),(a_-,-1),(b_-,-1)
\]
in listed geometric order is the unique order of the two fixed underlying
curves on each summand whose exact action equals that rotation.  Swapping
either summand order breaks the equality.  The transported action is
\[
M_{\rm v2}=
\begin{pmatrix}
1&1&0&0\\
-1&0&0&0\\
0&0&1&-1\\
0&0&1&0
\end{pmatrix}.
\]

Two new reducers, using direct cochain solving and an independent
spanning-tree quotient respectively, derive the same \(4\)-vertex,
\(12\)-edge, \(6\)-face chain object.  Explicit mutually inverse maps in
degrees \(0,1,2\) preserve both theta markings and the two components.  Both
derive
\[
[V_3^{ob}]_{B_9}=(4,-3,4,-1),\qquad
[V_3^{ob}]_{B_{\rm v2}}=(4,-3,4,1),
\]
zero surface framing, and positive-meridian/zero-longitude coordinates
\((1,0),(0,1)\).  Peripheral data is attached only to the boundary-fixed
`Qmon` collar lift, never to a bare capped rotation.  Single source-edge
reversals, summand exchange, wrong reflection side, either factor-order swap,
and removal of the \(b_-\) gauge all fail content certificates; simultaneous
reversal of all theta arrows remains the expected global gauge.

The replayable Engineer result is under
`research/l3_openbook/primary_reflection_marking_cycle10/` with status
`SOURCE_PACKET_PASS`.  The claim ledger records independent Reviewer support
for both the packet and the corrected source-marked object.

## Cycle 10 source-aligned mapping torus

The accepted packet now has a fresh finite PL realization under
`research/l3_openbook/source_aligned_mapping_torus_cycle10/`.  This
construction does not reuse the quarantined fourteen-triangle target
monodromy, the 98/728/954-piece finite lineage, the 121-crossing diagram, or
any of their fillings.  It stellar-subdivides source triangle `F3T0` and
recomputes every marked normal curve on a 16-triangle, 24-edge genus-two page
with one binding vertex.  The source representative of \(V_3^{ob}\) has
normal weight 39.

Each of the four packet twists has an explicit orientation-preserving PL
annulus map, a two-sided inverse, positive support clearance, and pointwise
binding-collar fixation.  On each capped summand, the two-flip word `BA` has
inverse `ab`, exact order six, and exact signed-edge isometry
`[-2,-3,-1]`; the full Alexander-system identification, rather than only its
\(H_1\) action, matches the declared component- and theta-marked rotation.
The two intersection-one pairs have unimodular symplectic blocks, so their
one-holed-torus neighborhoods have a pair-of-pants complement.  Capping the
binding changes that complement to an annulus.  The common `BA` chain-relation
boundary twist pulls back with opposite signs through the degree \(-1\)
\(S_+\) chart and degree \(+1\) \(S_-\) chart, so the sixth powers cancel
there.  Thus finite order is asserted only after capping, not for the
boundary-fixed punctured lift.

The resulting layered model has 106 tetrahedra.  Independent Engineer replay
reconstructs all 424 face pairings, finds 106 circular edge links and six
orientable torus vertex links, and verifies the embedded 16-face fiber and
return map.  Each of the five ordinary page vertices carries an explicit raw
cusp-link fiber cycle that is embedded, connected, nonseparating, and
primitive; filling those five slopes leaves exactly the binding boundary
torus.  The 26 source segments of \(V_3^{ob}\) give 39 fiber arcs, and its
two-component normal push-off certifies surface framing zero.  The \(Q\),
\(V_3^{ob}\), theta, orientation, and peripheral labels are retained.

Jacobian 0.14.0, protocol `2025-11-25`, operation
`combinatorial_map.vertex_face_incidence.compute`, independently confirms
that every one of the four source CW vertices is incident once with each of
the six source faces.  Its exact contract, payload, typed output, 1 ms
runtime, null structured error, and false timeout flag are preserved under
`jacobian/`; this bounded incidence calculation is not treated as the
topology proof.

The status is `SOURCE_ALIGNED_MAPPING_TORUS_VERIFIED`, and the Cycle 10
claim has independent Reviewer support in the ledger.  This establishes
neither a component-labelled exterior nor either final campaign gate.

## Cycle 11 source-aligned exterior exclusion

Cycle 11 used only the reviewed Cycle 10 packet and 106-tetrahedron
mapping torus.  It made all 39 normal arcs into one directed
39-edge subcomplex, removed its derived regular neighbourhood, and
idealized the new torus boundary.  The exact intermediate sizes are
2,594 adapted tetrahedra, 50,664 tetrahedra with a real drilled
boundary, and 61,632 tetrahedra after idealization.  Raw cusp-link
cycles give the five auxiliary fiber slopes and determinant-one Q and
\(V_3^{ob}\) peripheral pairs.  Attaching the five auxiliary solid
tori leaves a 39-tetrahedron orientable two-cusp exterior with
\(H_1=\mathbb Z^2\).  Refilling the derived \(V_3\) meridian gives the
independently constructed square-knot exterior with undecorated isosig
`eLPkaccddjggan`.

The final zero-framing gate rejects this route.  With the recorded
component order `Q,V3_ob`, exact integral homology is:

| Fixed filling | Homology |
|---|---|
| Q surface cycle only | \(\mathbb Z^2\) |
| \(V_3^{ob}\) cut-fiber cycle only | \(\mathbb Z\oplus\mathbb Z/16\) |
| both surface cycles | \(\mathbb Z\oplus\mathbb Z/16\) |
| both positive meridians | \(0\) |

Regina 7.4 exactly recognizes the double-meridian filling as \(S^3\).
For the double-surface filling, the wrong homology already excludes
\(\#^2(S^1\times S^2)\), so no prime-decomposition claim was made.
The same order-16 defect appears before and after finite-vertex
removal on the raw 61,632-tetrahedron object; it is not a simplifier or
basis-installation artifact.  No slope was searched or changed.

`research/l3_openbook/source_aligned_exterior_cycle11/verification_report.json`
seals the raw pairing hash
`22a418dd51849636a619c00bef0f088f7fa35dcb9f0b56e7d727d331c3485f4b`,
the marked exterior hash
`87615952a4bd5c9a920ce9b6477c368107391d207b781ffbc0ff0cb4a7dda60f`,
both closed triangulations, and the mutation replay.  Swapping the
cusps, reversing one meridian, adding a Q meridian twist, deleting one
V3 arc, or altering an auxiliary fiber slope each fails its specified
combinatorial or marking gate.

This is an Engineer route exclusion pending independent Reviewer
replay.  It does not identify the source of the framing-16 discrepancy,
refute the theorem-level GST surgery statement, close the independent
alpha-gamma route, or supply a handle-slide obstruction.

## Cycle 12 preferred-longitude diagnosis

A clean-room cellular calculation now determines the signed defect without
importing any Cycle 11 production module.  In the ambient basis
\((\mu_Q,\mu_{V_3})\), with each boundary basis ordered as meridian then
recorded cut-fiber cycle, both the 61,632-tetrahedron raw replay after the
five fixed attachments and the independent 39-tetrahedron replay give

\[
i_Q=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
i_{V_3}=\begin{pmatrix}0&0\\1&16\end{pmatrix}.
\]

After filling the other component's positive meridian, the primitive
kernels are \((0,1)\) for \(Q\) and \((-16,1)\) for \(V_3\).  Hence

\[
\lambda_Q^{S^3}=c_Q,\qquad
\lambda_{V_3}^{S^3}=c_{V_3}-16\mu_{V_3},
\]

so the installed orientations give the exact decomposition
\(c_{V_3}=\lambda_{V_3}^{S^3}+16\mu_{V_3}\).

Before the auxiliary attachments, the determinant-one raw basis consisting
of the five fixed attaching slopes followed by \(\mu_Q,\mu_{V_3}\) gives

\[
[c_Q]=(-1,1,-1,-1,1,0,0),\qquad
[c_{V_3}]=(3,-5,4,4,-6,0,16).
\]

The cut cycle becomes a pure meridian multiple only after the fifth fixed
attachment.  Explicit dual 2-chains witness \(i_Q(c_Q)=0\) and
\(i_{V_3}(c_{V_3}-16\mu_{V_3})=0\).  A 5,232-triangle boundary annulus
between the two parallel 234-edge cut cycles, together with the inverse
idealizing-cone map, excludes idealization; finite-vertex removal and
simplification preserve the same signed coefficient.

The first unsupported comparison was therefore the transport from Cycle 10's
source-zero surface push-off to the post-drilling cut cycle.  Cycle 12 did not
contain a relative annulus or cap-chain identifying those two classes.  The
algebraic preferred longitude was not thereby a source push-off: the corrected
direct route remained retired, and the class was not authorized as alpha-gamma
input.

The exact certificate and standalone verifier are under
`research/l3_openbook/source_aligned_framing_diagnosis_cycle12/`.  Adding one
positive meridian changes \(k\) to 17, while meridian reversal, arc deletion,
cusp exchange, and an altered auxiliary slope each fail their designated
gate.  Bounded Jacobian certified only the resulting \(2\times2\) Smith
matrix, with invariant factor 16; it did not replace the cellular
calculation.  The ledger now records independent Reviewer support for this
diagnosis.  It is not a surgery certificate, global obstruction, or
counterexample.

## Cycle 13 source-to-drilled transport exclusion

Cycle 13 resolves the previously unsupported interface, but in the negative
direction.  Starting with the doubled Cycle 10 normal curve, the exact
subdivision maps select one oriented 39-arc source push-off and carry its core
to the 39-edge adapted curve.  The positive drilled cut cycle visits the same
marked crossings in source order, with six boundary edges per crossing.  An
explicit 78-cell mapping-cylinder annulus has

\[
\operatorname{rank}(C_0,C_1,C_2)=(312,390,78),\qquad d_1d_2=0,
\]

both subdivision maps satisfy \(dF_1=F_0d\), and its oriented boundary is

\[
d_2A=p_{\mathrm{source}}-c_{V_3}.
\]

Thus the source push-off reaches \(c_{V_3}\), with terminal coordinates
\((0,1)\) in the primitive ordered basis
\((\mu_{V_3},c_{V_3})\); it does not reach the algebraic preferred longitude
with coordinates \((-16,1)\).

The calculation replays the five fixed cap contributions directly from the
reviewed raw Smith basis:

\[
[c_{V_3}]=(3,-5,4,4,-6,0,16).
\]

After the five attaching classes are killed, the primitive cokernel
functional with \(\omega(\mu_{V_3})=1\) gives

\[
\omega\!\left(
p_{\mathrm{source}}-(c_{V_3}-16\mu_{V_3})
\right)=16.
\]

This proves that the specified corrected relative chain does not exist in the
fixed interface complex.  No target slope or expected coefficient was input.
The exact source cycle, chain maps, 78 cell boundaries, inverse cone map, cap
replay, and cokernel certificate are under
`research/l3_openbook/source_to_drilled_framing_transport_cycle13/`.
The ledger records independent Reviewer support.  The corrected direct-filling
route remains retired and alpha-gamma input remains unauthorized.

## Cycle 14 primary Kirby forward reconstruction

Cycle 14 avoids the retired source-to-drilled framing route.  It uses only
GST's `Text.tex` and `Gompffig1b.eps`--`Gompffig5.eps`; it does not read
`Ln1.eps`, `Ln1.pdf`, or an earlier target PD, Gauss, exterior, crossing, or
filling artifact.  An affine PostScript compiler reconstructs the lower-right
panel of Figure 12 as four closed labelled components
\((R_+,R_-,V,Q)\).  There are exactly 16 box-exterior crossings, and each has
exactly one EPS under-gap.  The paths labelled \(-n\) and \(n\), specialized
at \(n=3\), expand mechanically to twelve more crossings.  Figure 12 port
order fixes the two alternating over-phases; flipping either phase, or both,
fails the planar rotation-system check.

The strengthened movie no longer treats the intervening figures as prose.
All 13 panels of Figures 9--13 are independently parsed into 431 oriented EPS
strand fragments with named component anchors and explicit boundary ports.
Eighty-seven transverse source witnesses pair a broken under-strand with the
continuous over-strand.  The move list separately encodes Figure 9
dualization, the Figure 10 slide and Hopf cancellation, the Figure 11 handle
subtraction and flype, the \(k=1\) flype, the clockwise Figure 12 sequence
\(\mathrm{UL}\to\mathrm{UR}\to\mathrm{LR}\to\mathrm{LL}\), the Figure 13
\(Q\)-sublink movie, both Rolfsen blow-downs, and the final square-knot
isotopy.  Every before/after tangle carries component labels, oriented ports,
over/under crossings, integer framings, and a linking update.  The verifier
deletes and separately tampers with each of the 13 moves in memory; all 26
mutations are rejected before any filling recognition is run.

The Cycle-14 source-anchor defect was a closure-table error, not a target-code
correction.  Figure 9-left component \(C\) had been rooted at EPS path 17;
the source \(0\) label and panel specification anchor path 20 in the source
direction.  The corrected traversal is
\[
20^+,19^+,15^+,18^-,17^-,14^-.
\]
A full 13-panel audit found the same stale-root problem elsewhere and
source-visible broken-stroke misjoins in Figure 10-left, Figure 11-left/right,
and Figure 12 upper-right.  The closure generator now takes every anchor from
the panel specification, while compiler and independent verifier both demand
the complete `(path_id,direction)` anchor.

The strengthened schema also freezes all 431 adjacent endpoint pairs
separately from those traversals.  Each record contains the two frozen EPS
points, their outward tangents, gap geometry, any broken-under crossing
witness, and a deterministic crossing-cut digest over all same-component,
same-colour endpoint chords.  Independent parsers reproduce every record and
the 102 geometric gaps used by the movie.  They reject both the previously
decisive mutation reversing non-anchor Figure 9-left path 19 and a
degree-preserving Figure 10-left endpoint rematching, in addition to the old
root, anchor-orientation, and path-deletion controls.

Fresh compilation preserves the ordered `[V,Q]` code and the marked exterior:
their SHA-256 values remain respectively
`2f5345b81d54c6a198e6bfd1d1951f671f6b7bf1daadf46ff716aff853dff8f5`
and
`16d39856cafd0f840d66f782527ab53ccd8ac057a2e3e0361a9eb6c44d17e641`.
Thus scalar artifacts frozen to the first hash remain applicable; this says
nothing about whether any such scalar is nonzero or handle-slide invariant.

An output tree that was empty before compilation,
`primary_kirby_forward_cycle14/fresh_replay_v3/`, receives every compiler
output through explicit paths.  Its independent replay passes all 13 stages,
ordered codes, component gates, and both fillings.  The isolated mathematical
`link` payload equals the canonical one exactly, while the complete JSON file
differs only because its provenance correctly points to isolated outputs.
The isolated exterior is byte-identical to the canonical exterior.

The resulting 28-crossing framed source diagram has
\[
K_0=
\begin{pmatrix}
1&0&-3&1\\
0&-1&-3&1\\
-3&-3&0&0\\
1&1&0&0
\end{pmatrix}.
\]
The red sublink simplifies from two cancelling crossings to two split
unknots.  The Figure 11 handle subtraction changes its \(0\)-framing by
\(0+(-1)-2(-1)=+1\).  Applying
\[
K'_{ij}=K_{ij}-K_{iR}K_{Rj}/K_{RR}
\]
to \(R_+\), then \(R_-\), gives
\[
K_1=
\begin{pmatrix}
-1&-3&1\\
-3&-9&3\\
1&3&-1
\end{pmatrix},
\qquad
K_2=
\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\]

The final artifact is a 64-crossing oriented PD/DT/Gauss code ordered
`[V,Q]`, with framing zero on both components.  Two-edge dual splitting
circles in the one-component projections give
\[
Q=\overline{T_{2,3}}\#T_{2,3},
\qquad
V=\overline{T_{3,4}}\#T_{3,4};
\]
the summand braid words and the cyclic-conjugation/\(121=212\) replays are
recorded explicitly.  SnapPy checks that the saved PD has an ordered exterior
isometry to the two-cusp triangulation produced by the two auxiliary
fillings.

Regina 7.4 independently recognizes the two closed fillings in the saved
`[V,Q]` bases.  Double meridian filling has trivial group and homology and
passes `isSphere`, hence is \(S^3\).  Double zero filling has
\(H_1=\mathbb Z^2\) and group \(\langle a,b\rangle\).  After a bounded
fast simplification and, only when its result has more than seven tetrahedra,
a finite strict-descent sequence of bounded height-one Pachner searches, an
explicit connected two-sided normal sphere, given as a recorded
sphere-plus-torus Haken sum, separates the manifold into two components.
Every exhaustive step is required to reduce the tetrahedron count.  Crushing
gives two 2-tetrahedron `LayeredLensSpace`
triangulations, each recognized as \(L(0,1)=S^2\times S^1\); Regina's
independent prime decomposition returns exactly the same two summands.

The compiler, final code, marked exteriors, Kirby movie, normal coordinates,
and independent verifier are under
`research/l3_reconstruction/primary_kirby_forward_cycle14/`.  Jacobian 0.14.0
operation `matrix.normal_form.smith.certified.compute` checks only the exact
Smith form of the auxiliary red framing matrix
\(\operatorname{diag}(1,-1)\); it is not used to prove unlinking or filling
topology.  The round-1 Reviewer objection that the first six move records could
be deleted without detection is resolved by the source-panel reconstruction
and per-move mutation gate above.  Independent replay recomputed all 431
source adjacencies from the frozen EPS, rejected the non-anchor reversal and
wrong endpoint rematching, regenerated the empty output tree through all 13
stages, and confirmed the ordered codes, zero framings, and both fillings.
Thus the Cycle-14 reconstruction, explicit oriented link code, and zero-surgery
certificate are independently confirmed.  This supplies no handle-slide
obstruction.

## Remaining bar

Only the global-obstruction bar remains: a theorem-level invariant preserved
under every unstabilized handle slide must distinguish \(L_3\) from the
zero-framed two-component unlink.  Until that bar is met, no campaign artifact
may label \(L_3\) a counterexample.
