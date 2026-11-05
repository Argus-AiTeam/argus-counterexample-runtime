---
title: GST L3 open-book input and primitive Floer boundary
description: Exact 3/7 open-book input, ambient-normalized peripheral transport, finite-diagram surgery mismatch, and the unresolved Floer count.
---

# GST \(L_3\) open-book input and primitive Floer boundary

## Exact representative now available

An invariant of the ordinary handle-slide orbit does not require recovery
of the missing bands from GST Figure 1.  Scharlemann supplies a different
exact representative:

- the page is the genus-two square-knot fiber
  \(F=F_+\natural F_-\);
- its monodromy is the boundary connected sum of the right-trefoil
  monodromy and its reflected inverse;
- after slides of \(V_3\) over the binding \(Q\), the second component
  lies in \(F\), has surface framing zero, and has pillowcase class
  \(3/7\);
- the selected representative uses sextant \(0\), increasing
  development orientation, and Scharlemann's left-trefoil closure when
  the curve is moved off the capping disk.

These choices define one oriented zero-framed \(S^3\) link in the
ordinary handle-slide orbit of GST \(L_3\).  They do not assert a
crossing-by-crossing equality with Figure 1.

The cap choice is now part of the rational CW data rather than a
reference to the source drawing.  In sextant \(0\),
\[
D_{\rm cap}=[2/25,9/50]\times[11/50,9/25],
\]
the points at \(t=1/100,199/100\) are recorded only as the two
intersections with \(Q\).  The retained lift instead ends at
\(t=2/175,348/175\), on the outer \(1/100\)-collar, and the selected
left closure is a rational west-collar push-off strictly in
\(F\setminus Q\).  Its first and last edges are positive multiples of
the lift tangent \((3,7)\), recording straight-through smooth joins.
Exact segment tests now certify
\(Q\cap V_3^{\rm ob}=\varnothing\), self-embeddedness of
\(V_3^{\rm ob}\), and that the bouquet interiors miss both link
components.

The two theta spines carried by the \(T\)- and \(B\)-edge lifts specify
the four twist curves \(a_\pm,b_\pm\); their twist annuli miss
\(D_{\rm cap}\), so the stored monodromy word is boundary fixing.  A
spec-only replay emits `punctured_page_link.svg`, including the
disjoint components and checked polygonal bouquet.

The six-sextant gluing has four vertices, twelve edges, six faces, Euler
characteristic \(-2\), and genus \(2\).  The exact \(3/7\) development
has seam counts \(T=B=7\), \(R=L=3\).  Exact replay checks its primitive
minimal period, branch offset \(1/25\), embeddedness, and three
pairwise-disjoint degree-one lifts; the selected lift closes on sextant
\(0\).  The finite specification, rational replay, and vector drawings are under
`research/l3_openbook/`.

The Argus Jacobian adapter independently computed a transformation-
certified Smith form of the \(6\times12\) dual incidence matrix:
Jacobian 0.14.0, protocol `2025-11-25`, operation
`matrix.normal_form.smith.certified.compute`, rank \(5\), invariant
factors \((1,1,1,1,1)\), full unimodular transformations, runtime 9 ms,
and no error or timeout.  This checks connectedness of the dual graph
only; it is not surgery or Floer evidence.

GST Corollary 6.4 identifies zero surgery on this homeomorphic lift with
\(\#^2(S^1\times S^2)\).  An explicit Heegaard-move reduction of the
output diagram is still absent.

## Verified common page triangulation

The six-sextant CW page and the 14-triangle Flipper page are now connected
by an explicit PL transport.  Cone the cap face from
\(P=(13/100,29/100)\) and split each of the other five square faces along
\(TL\)-\(BR\).  The resulting oriented triangulation has 5 vertices,
21 edges, and 14 triangles.  A signed simplicial isometry sends
\((BL,TL,TR,BR,P)\) to \((0,1,2,3,4)\).

Exact crossing transport sends \(V_3^{\rm ob}\) to the weight-36 normal
vector
\[
(3,2,2,1,1,1,3,2,2,1,1,1,1,3,2,3,1,2,1,2,1).
\]
The anchored ribbon boundaries of
\[
a_+=T03-T25,\quad b_+=T14-T25,\quad
a_-=B03-B25,\quad b_-=B14-B25
\]
are exactly the four stored twist curves.  Clockwise \(Q\) maps to the
binding-cusp link \(20,19,18,17,20\), and the bouquet proper arc maps
through target triangles \(1,2\), crossing only target edge \(18\).
Component orientations and both zero framings are included in the finite
record.

The public `verify_relative_input.py` reads `openbook_spec.json` directly
and reconstructs every triangle, signed edge image, rational crossing,
ribbon frontier, the annulus from \(Q\) to the cusp link, and the proper
arc before checking the 98-tetrahedron canonical mapping torus.

## Source-to-finite monodromy mismatch

The common page triangulation above is a valid static marked-page
transport, but it does not certify the monodromy identification currently
used by the finite lineage.  An independent cellular reconstruction gives
the clockwise six-sextant capped rotation, in the declared basis
\((a_+,b_+,a_-,b_-)\), as
\[
R_*=
\begin{pmatrix}
1&1&0&0\\
-1&0&0&0\\
0&0&1&1\\
0&0&-1&0
\end{pmatrix}.
\]
The boundary-fixed twist word stored for the fourteen-triangle mapping
torus acts in that same declared basis by
\[
W_*=
\begin{pmatrix}
0&1&0&0\\
-1&1&0&0\\
0&0&1&-1\\
0&0&1&0
\end{pmatrix}.
\]
Thus \(R_*\ne W_*\), so the identity-marked page transport does not
intertwine the two declared monodromies.  The first failed stage is
`six_sextant_marked_capped_page_to_14_triangle_boundary_fixed_monodromy_alignment`,
before construction of the canonical mapping torus.  This refutes the
current source-to-finite marking bridge, not the reviewed GST open-book
surgery theorem and not either monodromy description in isolation.

The frozen source contract and independent calculation are recorded in
`research/l3_openbook/source_marked_exterior/source_manifest.json` and
`source_alignment_report.json`.  Jacobian operation
`combinatorial_map.euler_characteristic.compute` independently returns
\(4-12+6=-2\) for the six-sextant cell data; it is only a local cell-count
check, not a relative-homeomorphism or surgery certificate.  Repair
requires an explicit orientation-preserving marked-page homeomorphism or
common subdivision that conjugates the monodromies and simultaneously
carries \(Q\), \(V_3^{\rm ob}\), both component orientations, both
surface-zero framings, and all four auxiliary page-vertex links.  A
homology basis change alone is insufficient.

## Regenerated marked exterior and relative diagram

The finite objects below remain internally replayable, but they are
quarantined as models of GST \(L_3\) until the source-to-finite monodromy
bridge is replaced and independently reviewed.  All current markings were
transported through the same 29-move V-short
conjugation: the weight-36 \(V_3^{\rm ob}\), four twist curves, binding
peripheral, and the band-sum frontier encoding the edge-18 proper arc.
After tightening, the selected and band-sum frontiers have weights \(2\)
and \(4\), supported respectively on edges \(3,14\) and \(0,4,6,9\).
There are three equivalent binding triangle-corner representatives; the
lexicographically first, triangle \(0\), corner \(0\), fixes the finite
layout without asserting a unique representative.

The regenerated common subdivision has 728 tetrahedra and contains the
complete connected four-vertex/four-edge rank-one bouquet.  Its derived
frontier is a single genus-two surface.  The marked clipping has 22,584
tetrahedra, one real genus-two boundary, and four ideal torus cusps; the
four filled-page fiber slopes are exact cusp-link cycles of lengths
\(8,8,12,8\).  The public exterior verifier reads the current
`relative_splitting_input.json`, replays all seven marked trajectories and
checks that the target bundle word is inverse conjugation followed by the
current 68-move monodromy and forward conjugation.  It then replays the
graph/frontier/cusp construction and returns `bouquet_exterior_ok`.

The resulting relative Heegaard surface has 17,472 squares and genus
\(729\).  Its five-root primal forest produces 727 disjoint alpha
meridians; its dual tree produces 729 disjoint beta meridians.
`verify_relative_diagram.py` checks every cyclic disk boundary against the
same marked source and returns `relative_heegaard_diagram_ok`.

The former weight-38/edge-19 route remains retired, as does the direct
genus-four open-book identification ruled out by the \(H_1\)
split-injection obstruction.

## Filling compression and component peripherals

The four fake-cusp filling handles are now explicit rather than pending.
For page vertices \(0,1,2,3\), the deterministic bridge exchanges use
common edges \(20,67,7,123\), respectively.  They merge the five primal
forest roots into one connected rank-one graph while avoiding all four
fiber-slope vertices.  The exchanged disk system has 723 remaining primal
cocores and four filling disks, hence still 727 compression curves.

The intermediate frontier has
\[
(V,E,F)=(9902,27384,17472),\qquad \chi=-10,\qquad g=6.
\]
Compressing its four recorded torus slopes, capping the resulting spheres,
and cancelling the four necks gives the original bouquet frontier with
\[
(V,E,F)=(1308,3866,2556),\qquad \chi=-2,\qquad g=2.
\]
`verify_filling_compression.py` reconstructs every negative-torus attaching
cycle, abstract parallel ribbon lane, bridge exchange, cocore path, and
frontier count from the marked exterior and reports
`filling_compression_ok`.

The same surface now carries the actual four peripheral curves.  On the
binding component \(Q\), a genuine \(S^3\)-recognized Dehn filling,
together with the Gordon--Luecke/Property P consequence quoted by
Kronheimer--Mrowka, identifies the lifted meridian up to orientation; the
fiber curve is its Seifert zero longitude.  On \(V_3^{\rm ob}\), the
meridian is the primal meridian of selected-cycle common edge \(2\), and
the zero longitude is lifted from the exact weight-two page ribbon, with
five cap-center passages replaced by separate deterministic meridian
lanes.

The quadrangulation rotation system finds one positive
\(\beta_2\)-\(\gamma_2\) crossing, at surface vertex \(170\), and no
cross-component crossing.  Together with the binding pair this gives
\[
(\beta_i\cdot\gamma_j)=
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]
`verify_component_peripherals.py` replays the recognized filling, both
normal lifts, all five cap detours, the local rotation, and all carrier
disjointness checks and reports `component_peripherals_ok`.  The Property P
attribution is recorded in the claim ledger and remains due for independent
source attribution.

The coarse paths alone are not the simultaneous disk system: all six
filling--filling pairs and 35 filling--cocore pairs share at least one
surface edge.  `simultaneous_disk_system.json.gz` resolves those
identifications globally.  It records all 727 curves at once, with an
ordered lane for every occurrence on each of 256 shared surface edges and
the induced connection pairing at each of 278 shared surface vertices.
The order at the larger endpoint of an edge is the reverse of the order at
the smaller endpoint, as required by the oriented edge band.  At every
vertex, the recorded pairings are nonalternating chords in the cyclic
surface rotation.  Thus the edge lanes and vertex-disk arcs give one
simultaneous PL realization, not separate pairwise perturbations.
The inventory binds these boundaries to 723 distinct primal 1-handle
cocores and four distinct attached filling 2-handle cores.  Their interiors
are disjoint by the handle decomposition, and the global boundary routing
makes the attaching collars disjoint as well.

The resulting exact routing problem has maximum lane multiplicity three
and 44 unary plus 234 binary vertex constraints.  Arc consistency fixes
the stored witness without backtracking.  Independent replay checks every
lane and chord and finds zero crossings, including all six
filling--filling and all 35 filling--cocore shared-carrier pairs; no two
retained cocores share a carrier edge.

The same replay derives the four cap cancellations rather than inferring
them from genus arithmetic alone.  For each fake cusp it reconstructs a
closed connected oriented Euler-zero cellulation, verifies that the
embedded fiber slope has connected complement, and hence identifies the
cut surface as an annulus.  Capping its two boundary circles gives a sphere.
The bridge foot avoids the slope, so this cap and its bridge neck can be
cancelled independently for all four cusps.  Compressing the 723 cocores
first gives the recomputed genus-six frontier; the four certified
sphere-cap eliminations then give the recomputed genus-two bouquet
frontier.  `verify_simultaneous_disk_system.py` reports
`simultaneous_disk_system_ok`; a second compilation gives the same
compressed artifact hash
`0c0705a3c31b1b8fc45613af10a7f9d95653fb075995c2a6abcfb4e79868a71f`.

Jacobian 0.14.0, protocol `2025-11-25`, operation
`chain_complex.homology.compute`, independently returned
\(\dim H_0=\dim H_1=1\) for the exact four-vertex/four-edge bouquet incidence
complex over \(\mathbb F_2\), with no adapter error or timeout.  This is only
a graph-rank cross-check.

## Alpha--gamma standard-form certificate

The move artifact records every disk bigon isotopy, same-family disk-band
handle slide, and punctured-torus destabilization.  Its completion status is
not evidence: the independent verifier derives completion from the replayed
terminal rotation system.

For a proposed terminal pair \(H=\alpha_i\cup\gamma_j\), delete every other
curve from the full disk cellulation.  Full faces are joined across deleted
edges, and each crossing of two deleted curves restores one vertex disk.  For
each resulting component \(C\), the verifier computes
\[
\chi(C)=\#\{\text{full faces in }C\}
       -\#\{\text{deleted edges in }C\}
       +\#\{\text{deleted--deleted crossings in }C\}.
\]
The restricted rotation on \(H\) independently gives every boundary cycle,
so \(b(C)\) and \(g(C)=(2-b(C)-\chi(C))/2\) are checked rather than supplied
by the artifact.

Let \(N(H)\) be the oriented regular neighborhood read from the same
restricted rotation.  A pair is certified parallel only when capping the
disk components of its complement turns \(N(H)\) into a connected
\((g,b,\chi)=(0,2,0)\) subsurface, while the marked point lies in the unique
outside component of genus one with two boundary circles.  Thus the finite
data construct an embedded basepoint-free annular support containing both
essential curves; homology equality or a claimed `parallel` label is not
used.  At genus two, completion additionally requires a bijection between
the two surviving alpha and two surviving gamma disk-system components for
which both annular-support checks pass.  The replayed same-family slides and
destabilizations preserve both disjoint complete disk systems, so this
bijection identifies the same two-component multicurve; the gamma system can
be moved into disjoint collars of the two alpha cores.  Those collars are the
simultaneous standard summand annuli.  Otherwise the artifact remains
`genus_two_without_standard_summands`.

## Current geometric-reduction frontier

The strongest independently replayed prefix now reaches genus four.  The
canonical artifact records 5,004 moves:
\[
725\text{ destabilizations},\qquad
1,666\text{ same-family handle slides},\qquad
2,613\text{ disk bigon isotopies}.
\]
It terminates with four alpha curves, four gamma curves, and 175 crossings.
The verifier reconstructs the reviewed lane/chord/rotation input, every
embedded band and quotient/cap, and the terminal state without trusting the
compiler's summary.  It reports `bounded_reduction_prefix_replayed`, not
completion.

The earlier 175-crossing descendants carried an incorrect lineage marker:
they labelled a 177-crossing state at operation 4,946 as the first genus-four
state.  Exact replay locates the actual first genus-four state at operation
4,372 with 246 crossings.  The canonical artifact explicitly names that
ancestor and then records the 632-move suffix (23 slides and 609 isotopies)
to 175 crossings.  This repairs replayability; it does not lower the genus.

Two bounded primitive-disk searches found no next destabilization.  First,
an exact enumeration of all 8,362 simple family-complement bands of dual
length at most four found no slide whose resulting opposite-family word is
primitive; the smallest Whitehead minimum remained 41.  Second, the complete
shared-face depth-two search generated all 684 first slides, deduplicated
them to 66 states, and checked 51,480 second-slide word actions.  It found no
primitive word, with no candidate or beam truncation.  These results exclude
only those finite band classes and do not obstruct longer paths or other
genus-four states.

A separate, not-yet-independently-replayed 228-crossing genus-four prefix has
smallest Whitehead minimum 12.  Its complete shared-face depth-two pass
generated 694 first slides and 72 distinct first descendants, then checked
all 60,908 second-slide word actions.  It again found no primitive, with no
candidate or beam truncation.  On the same four-word systems, a finite
algebraic probe checked every sequence of length at most three in its declared
canonical-product model, where a move replaces the chosen canonical
representative of \(w_i\) by the cyclic class of
\(w_iw_j^{\pm1}\), followed by canonicalization under cyclic conjugacy and
inversion.  It checked 8,342 third-level gamma descendants and 8,318
third-level alpha descendants, with no word-length discard and no primitive
component.  This last computation has no embedded bands or independently
chosen relative conjugators.  It is an exact three-move exclusion only for
that declared finite model, not a Heegaard-move result or a general Nielsen
exclusion.

A materially different genus-five search starts from a 97-crossing state
with five individually ambient-primitive curves.  Geometric Whitehead
realizations made \(\gamma_{1463}\), \(\gamma_{1880}\), and
\(\alpha_{101}\) actual degree-one curves and then performed one replayable
destabilization in each branch.  Their genus-four descendants have,
respectively, 375, 205, and 982 crossings.  None retains an ambient-primitive
curve; their smallest Whitehead minima are 31, 35, and 12.  Thus an
ambient-primitive word at genus five is a lead to one cancellation, not
evidence of a path to genus two.

The path-length-four realization focused on \(\gamma_{1459}\) lowers its
freely reduced word to length one, but the geometric curve still has degree
23 and no opposite curve occurs uniquely in its raw intersection word.  It is
therefore not a cancellable pair.  A targeted all-candidate geometric-clearing
attempt reached its 1,200-second bound without writing an artifact.  That
timeout is a non-conclusion and excludes no clearing move.

A primitive-preserving variant now branches over both adjacent sides at each
of the twelve \(\alpha_{101}\)-clearing steps and retains every distinct
endpoint-local, basepoint-free, shared-face band before applying a width-64
beam.  It checks 64 complete genus-four descendants of the exact genus-five,
97-crossing state.  None is ambient-primitive; the selected 364-crossing
descendant has minimum Whitehead length 12.  Its 4,416 recorded operations
(725 destabilizations, 1,674 slides, and 2,017 isotopies) replay
independently, but there is still no genus-four-to-three destabilization.
This excludes only the retained endpoint-local beam, not arbitrary clearing
bands.

A separate meet-in-the-middle search tests simple dual-cellulation curves of
length exactly 18 on the canonical 175-crossing genus-four state.  Equal
reduced labels on the two half paths force both the alpha-handlebody and
gamma-handlebody words to be trivial.  Across all 168 canonical start faces,
669,178 half paths and 32,688,472 equal-label pairs yield 1,852,683 simple
common-zero-word curves.  A complete connectivity pass finds every one
separating.  Two disjoint exact Euler-characteristic shards, on start indices
\([0,21)\) and \([21,168)\), classify respectively 1,233,965 and 618,718
curves; every curve has a genus-zero side and is contractible.  Thus this
finite class contains no essential common-disk curve.  It says nothing about
other lengths or curves outside this dual-cellulation class and is not a
global handle-slide obstruction.

The nonlocal band search has now been widened without identifying algebraic
words with surface isotopy classes.  At dual-path length at most six, the
canonical state has 14,154 embedded-band candidates but only 584 distinct
target Nielsen words.  A diversity-first ordering replayed representatives of
all 584 word actions plus selected geometric variants: 782 bands applied,
18 failed the recorded basepoint-anchor merge condition, and normalization
left 745 distinct genus-four states.  The continuation beam retained 256 of
them.  From those states the exact word lookahead generated 3,847,568
second-band candidates and checked all 142,853 distinct target words; none was
primitive, and the best Whitehead minimum was 40.  The 489 discarded
first-level states and unretained geometric variants remain outside the
result, so this is not a complete depth-two disk-complex search.

Two abstract probes give search guidance only.  The first checked all 806,724
words
\[
w_i g w_j^{\pm1}g^{-1}
\]
from the 36 ordered actions passing the necessary abelianization test and
every freely reduced \(g\) of length at most five.  None was primitive.  The
second used a focus-stratified width-16 Andrews--Curtis beam through depth 12,
generating 38,232 moves in each family.  It found no primitive word; every
continuation level was beam-truncated, and 100 final gamma moves exceeded the
declared word-length cap 256.  Neither computation supplies embedded bands or
an algebraic obstruction.

A direct disk-boundary search now covers every fixed dual-cycle length from
2 through 19, both choices of compression-body side, and all 168 canonical
start faces.  For every odd length there is no endpoint pair with matching
reduced word on the proposed disk side.  For every even length, every such
pair has the identity word on the opposite side as well, rather than a
primitive word.  At length 18 alone the two-sided pass enumerates 1,338,356
half paths and 65,376,944 matching one-side-word pairs; the full length
2-through-19 series contains 79,813,742 such pairs and zero nontrivial
opposite words.  Thus no simple
basepoint-free curve in these fixed dual-cellulation classes has trivial word
on one side and primitive word on the other.  This excludes neither length
20 and above nor disk boundaries outside this normal form.

The canonical evidence is
`alpha_gamma_heegaard_reduction_low_whitehead_canonical.json.gz` and
`alpha_gamma_heegaard_reduction_low_whitehead_canonical_verify_report.json`.
The new bounded evidence is
`alpha_gamma_heegaard_reduction_endpoint_beam64_verify_report.json`,
`alpha_gamma_heegaard_reduction_common_disk_mitm_length18_nonseparating.json`,
`alpha_gamma_heegaard_reduction_common_disk_mitm_length18_leading.json`, and
`alpha_gamma_heegaard_reduction_common_disk_mitm_length18_tail.json`.
The abstract three-move reports and their bounded probe are
`alpha_gamma_heegaard_reduction_nielsen_alpha_depth3_report.json`,
`alpha_gamma_heegaard_reduction_nielsen_gamma_depth3_report.json`, and
`alpha_gamma_heegaard_reduction_nielsen_probe.py`.
The new bounded evidence is
`alpha_gamma_heegaard_genus4_destabilization_complete_path6_depth2_compile_report.json`,
`alpha_gamma_heegaard_genus4_destabilization_conjugator_probe.json`,
`alpha_gamma_heegaard_genus4_destabilization_ac_beam_depth12_narrow.json`,
and the
`alpha_gamma_heegaard_genus4_destabilization_disk_curve_length*.json`
series generated by
`alpha_gamma_heegaard_genus4_destabilization_disk_curve_search.py`.
No terminal standard annulus has been certified.

## Genus-four positive control and complete-search boundary

The direct dual-cycle implementation had omitted every primal edge whose two
sides lie in the same complementary face.  Such an edge represents a valid
one-edge dual loop and is exactly how the smallest displayed stabilization
appears.  The corrected search handles these loops separately rather than
feeding them into the face-simple half-path recursion.  The canonical
175-crossing diagram has zero such edges, so the length-2-through-19 counts
above are unchanged.

The former 12-crossing calibration fixture was not a Heegaard diagram:
although its gamma complement was a sphere with eight boundary components,
its alpha complement had components
\((g,b,\chi)=(1,4,-4),(1,1,-1),(0,3,-1)\).  The depth-two and
normal-weight-one searches stored in
`alpha_gamma_heegaard_genus4_positive_control_standardization_depth2.json`
therefore remain diagnostics of that rejected fixture only.

The replacement positive control is an explicit cellular 22-crossing
genus-four rotation system.  Before any hiding slide, compiler-side and
independent reconstructions each show that both four-curve systems have
complement exactly one sphere with eight boundary components.  Its gamma
relators in the alpha handlebody freely reduce to
\[
\langle x_1,x_2,x_3,x_4\mid 1,1,x_3,x_4\rangle
\cong F(x_1,x_2).
\]
Thus Kneser--Milnor decomposition, the sphere theorem, and the Poincare
theorem identify the represented closed manifold as
\(\#^2(S^1\times S^2)\); Hensel--Schultens Proposition 1.2 then identifies
the splitting as a stabilization of the standard splitting.

The rotation system has a recorded bigon at crossings \(19,20\).  Cancelling
that bigon exposes the unique pair
\((\alpha_3,\gamma_{1461})\) at crossing \(21\).  Removing its
once-punctured-torus neighborhood gives genus three, where both surviving
three-curve systems independently have complement one sphere with six
boundary components.  The artifact also records the exact inverse bigon
isotopy and a same-family slide
\(\alpha_0\leftarrow\alpha_0\#\alpha_1\), after which no pair is displayed.
The complete weight-zero normal-arc implementation recovers the same pair
on its first replayed candidate using one recovery slide, six isotopies,
and one destabilization.  The independent verifier reconstructs the two
slides, the inverse relation, every embedded support, basepoint avoidance,
nonparticipant disjointness, intersection number one, and both terminal
complement audits.  It separately distinguishes a contractible
both-zero bigon boundary, essential common-zero meridians, and disk
boundaries whose opposite word is primitive.

The authoritative calibration evidence is
`alpha_gamma_heegaard_genus4_positive_control.json` and
`alpha_gamma_heegaard_genus4_positive_control_verify_report.json`.  This
certifies the implementation on a standard positive control; it is not a
destabilization of the canonical GST diagram.

Hensel--Schultens, Proposition 1.2
(doi:10.2140/agt.2024.24.2707), proves that every Heegaard splitting of
\(\#^n(S^2\times S^1)\) is a stabilization of the standard splitting.
Thus the reviewed \(W_2\) identification promises that the canonical
genus-four splitting has a stabilizing pair.  Ennes--Maria,
arXiv:2507.11406v2, Section 2.1, states that finite disk slides and
isotopies connect equivalent complete meridian systems; its Theorem 4.7
detects only a trivial pair already displayed.  Dovetailing over every
finite slide sequence and every bounded-weight normal band arc is therefore
complete and terminating for this promised input, but no complexity bound
is supplied.

The global implementation now enumerates every finite dual walk through the
cut cellulation up to the current weight, including repeated faces and edges,
all repeated-edge lane orders, and independently reconstructed noncrossing
face chords.  Breadth-first sequence layers use literal equality of the full
exported `genus`, curve words, signed crossings, protected anchors, and next
crossing identifier, encoded as readable canonical JSON rather than a digest.
The independent global verifier reopens the canonical 175-crossing input and,
only when a witness exists, replays every PL move, basepoint check,
nonparticipant disjointness check, the intersection-one pair, and the
genus-three terminal state.  Budgets zero and one are now complete.  Budget
one replayed all 2,200 embedded candidates, retained 401 non-root exact
states, skipped 481 unreplayable bigon choices, and found no witness.
Independent verification reports only `bounded_prefix_only`: this excludes
the single-slide, normal-weight-at-most-one class and is not a global
negative result.

Budget two uses recoverable full-state sharding.  Immutable gzip shards cover
consecutive candidate ranges for each parent state and retain the complete
structural state, normal-arc candidate, operation suffix, and rooted lineage;
parent and depth manifests record every shard hash and inventory total.  A
controlled interruption/resume and a separate two-depth A/B matched the
uninterrupted in-memory algorithm.  Durable task
`2669-canonical-global-dovetail-b2-sharded`, run
`2669-canonical-global-dovetail-b2-sharded-1788131897101656793`, is running
with a 24-hour timeout.  Until its manifest says complete and the independent
verifier accepts the result, it is neither a witness nor a bounded miss.

Masur--Schleimer Theorem 21.1 supplies only a coarse distance estimate, and
neither Strong Haken nor normal-sphere recognition constructs an
intersection-one pair for this surface.  The exact statements, hypotheses,
locators, source copies, algorithm contract, and capability limits are
recorded in
`alpha_gamma_heegaard_genus4_global_destabilization_theorem_contract.md`.
The first completed algebraic dovetail prefix covers every primitive cyclic
domain word of lengths one through six on both sides: each side has 11,918
cyclic classes, of which 10,360 are primitive domain words with distinct image
classes, and neither side has a primitive image.  The runs were interrupted
before length seven and therefore make no claim about longer words, relative
conjugations, or geometric bands.
Consequently the positive-control calibration is certified, but no canonical
genus-four-to-three move is currently certified.

## One-sided normal-disk primitive route

The paired marked simplification has a 21-tetrahedron alpha handlebody and a
43-tetrahedron gamma handlebody with the same one-vertex, 14-triangle
genus-four boundary.  A normal alpha disk boundary is transferred through the
recorded simplicial boundary maps, traced as normal arcs on the gamma side,
and homotoped into the gamma triangulation's primal one-skeleton.  The
resulting 54-generator, 93-relator edge presentation is sent by Regina 7.4's
explicit deterministic Tietze map to a four-generator, zero-relator
presentation recognized as `Free(4)`.  Regina verifies the forward
homomorphism and supplies a declared inverse; its general
`verifyIsomorphism()` heuristic returns inconclusive on the unsimplified
domain, so that boolean is not presented as an additional proof.

The calibration applies this map to Regina's exact weight-196 gamma
compressing disk.  Its 196 boundary crossings trace to 44 primal edge steps
and then to the empty free word, while all four inverse/forward free-generator
round trips are exact.  The complete alpha quadrilateral vertex stratum has
163 independently replayed compressing disks.  None has primitive gamma
word.  This is only a vertex-stratum exclusion: it does not exclude a
fundamental nonvertex disk or a compatible sum of fundamental surfaces.

Jacobian 0.14.0, protocol `2025-11-25`, supplied the bounded typed operation
`topology.simplicial.edge_path.word.compute`.  On the six-step primal path
with signed edge indices \((-5,-31,-8,11,-27,6)\), it returned the same six
formal edge letters with `EDGE_LABEL_REDUCTION` in 0 ms and no adapter error
or timeout.  The discovery response, inspected contract, exact payload, and
typed output are retained in the one-sided search directory.  This only
checks the edge-label transcription; it does not perform the Tietze or
Whitehead step and is not a primitive certificate.

The unbounded replacement enumerates standard-coordinate fundamental normal
surfaces and then dovetails their compatible nonnegative coefficient vectors
by increasing total coefficient sum.  Euler characteristic and quadrilateral
tests are used only as necessary-condition filters.  Every completed
coefficient budget is therefore a finite prefix, never a negative decision.
A primitive hit remains an algebraic lead until an explicit dual gamma disk,
intersection one, both original 1050-tetrahedron lifts, and the canonical
genus-three PL replay all pass.

It is not valid to read only those canonical gamma edges that survive the
boundary contractions.  All original boundary vertices collapse to the
marked vertex, so the four disjoint gamma meridians become a bouquet and
their turns through the vertex neighborhood are lost.  That shortcut produced
spurious primitive words and was discarded before any claim was recorded.
The primal gamma-handlebody group map above avoids this loss.

For the geometric implication, Cho--Koda--Lee,
arXiv:1812.10241v1, Section 3, define a primitive boundary curve by a
properly embedded dual disk meeting it once (PDF p. 3), and Lemma 3.1
(PDF p. 4) states that this is equivalent to representing a primitive
element of the handlebody fundamental group.  The lemma is attributed there
to Gordon.  This theorem supplies existence, not the explicit normal or PL
dual disk required here.

## Why the primitive multiplier is still unknown

A complete non-torsion minus/infinity computation needs a region-level
pointed triple subordinate to a specified bouquet, all periodic domains,
a strong-admissibility certificate, an explicit reduction of the
\(\alpha\)-\(\gamma\) diagram, and every punctured Maslov-zero triangle
class with a justified mod-2 holomorphic count.

The first common overlay has now been built, but it rejects the current
peripheral input.  The wound graph has 5,438 crossings and 10,876 edges.
Its source-cell replay gives 3,982 disk regions and one annulus, with
annulus boundaries 48 and 208 joined through edge gaps
\((1264,0)\) and \((1266,0)\); the total Euler characteristic is
\(-1456\).

The decisive obstruction is algebraic, not a missing region.  Exact
elimination gives
\[
\det M_{\alpha\beta}=-1,\qquad
M_{\alpha\beta}^{-1}M_{\alpha\gamma}\sim
I_{727}\oplus
\begin{pmatrix}0&0\\0&8\end{pmatrix}.
\]
Hence the current \(\alpha\)-\(\gamma\) diagram presents
\(\mathbb Z\oplus\mathbb Z/8\), and its pointed periodic-domain rank is
one rather than two.  The local peripheral intersection matrix \(I_2\)
therefore did not certify that the lifted \(\gamma_2\) has the required
global zero-framing class.  The compiler and an independent replay are
`compile_pointed_subordinate_triple.py` and
`verify_pointed_subordinate_triple_obstruction.py`; the finite report is
`pointed_subordinate_triple_obstruction_report.json`.

This candidate is not a subordinate triple for the stated zero surgery.
No primitive rank-two Spin\(^c\) label or strong-admissibility certificate
for the intended cobordism can be attached to it.  The current-peripheral
route is retired, and triangle enumeration remains prohibited.

The relative-chain replay now identifies the exact defect.  Starting from
the 728 tetrahedra, 17,472 squares, 723 cocores, four filling disks, and
the complete lane/chord witness, it obtains
\[
[\gamma_2^{\rm old}]=[\lambda_{\rm page}]+8[\beta_2].
\]
A 13,164-square integer 2-chain together with 203 alpha disks and 655
compression-tail disks bounds
\(\gamma_2^{\rm old}-8\beta_2\) without either component-meridian disk.
The reviewed zero surface framing therefore uniquely selects the embedded
\(-8\) Dehn twist about \(\beta_2\); this is derived from the chain
equation, not chosen to force a Smith form.

Global replay of the corrected curve finds
\(\beta_2\cdot\gamma_2=1\), no self-crossing, and no cross-component
intersection.  The corrected overlay has 5,446 crossings, 10,892 edges,
3,990 disk regions and one annulus, and its exact gate is
\[
\det M_{\alpha\beta}=-1,\qquad
\operatorname{SNF}(M_{\alpha\gamma})
=(\underbrace{1,\ldots,1}_{727},0,0).
\]
Thus the framing and target first-homology gate now pass.  The remaining
obligations are the corrected periodic-domain bases, primitive Chern
functional, strong-admissibility certificates, and an explicit
alpha-gamma Heegaard-move reduction.  Triangle enumeration is still
prohibited.

Jacobian 0.14.0 operation
`topology.simplicial_homology.integral.compute` independently recognizes
the six-vertex local twist annulus as torsion-free with Betti numbers
\((1,1,0)\).  Its chain-group bound is 32, so it does not cover the global
34,944-edge complex; the global claim rests on the replayable project
integer witness.

## Fixed-collar affine filling family

The complete reviewed global collar complex does not select one target
longitude.  Its target projection is exactly
\[
[3,-1]+\mathbb Z(1,0).
\]
The fixed marked SnapPea artifact installs the affine generator
\(\beta=(1,0)\) as peripheral curve zero and \(t_0=[3,-1]\) as peripheral
curve one.  Hence \(t_k=[3+k,-1]\) is the installed slope \([k,1]\).

After filling the four page cusps and leaving \(Q\) unfilled, the exact
dual-spine presentation has shape \(1080\times1077\) with 2,926 nonzero
entries.  A replayable integral reduction consists of 1,072 unit pivots and
a final transformation-certified \(5\times4\) Smith block of rank three.
It leaves two free generators and sends the two \(V_3^{\rm ob}\) peripheral
classes to
\[
i_*(\beta)=(1,0),\qquad i_*(t_0)=(7,0).
\]
Therefore the \(t_k\) filling appends precisely the relation
\((k+7,0)\).  Its complete \(1\times1\) minor set is \(k+7,0\), so
\[
H_1(t_k)\cong
\begin{cases}
\mathbb Z^2,&k=-7,\\
\mathbb Z\oplus\mathbb Z/\lvert k+7\rvert,&k\ne-7.
\end{cases}
\]
The unique class in this fixed family passing the necessary
\(H_1=\mathbb Z^2\) test is \(t_{-7}=[-4,-1]\).

This is a parameterized integer calculation, not a finite search.  The only
new topological sample was the preregistered neighbor
\(t_1=[4,-1]\): Regina and an independent integer dual-boundary matrix both
give \(\mathbb Z\oplus\mathbb Z/8\).  The reviewed \(k=0\) and \(k=-2\)
outputs remain regression anchors with torsion orders \(7\) and \(5\).
The standalone verifier reconstructs the full presentation from the frozen
marked triangulation, imports no builder, and replays every transformation.

The conclusion is only a necessary-class classification for the fixed collar
complex.  It does not geometrically select \(t_{-7}\) as the source
longitude, construct an embedded annulus, license a planar certificate, or
provide a handle-slide obstruction or counterexample.

## Ambient simplex-level transport and remaining gamma collar gap

The completed original-handlebody face-link scan exhausts every
Regina-normalized thin link of an individual primal triangle: all 2,450
alpha-side and all 2,450 gamma-side surfaces are topological disks, and
none is a compressing disk.  This is only a finite one-triangle linking
class; it says nothing about other normal or almost-normal disks and does
not change the genus-four destabilization claim.

The earlier blinded nonradial artifact is not an accepted ambient transport.
It uses the final cusp-link cellulation for both its labelled source and
target tori.  In its alleged common refinement, all 108 triangles belonging
to the three edge tubes have only target-gadget carriers and no concrete
source tetrahedron.  Its abstract product cylinder for corrected
\(\gamma_2\) has 232 triangles, none with a three-dimensional ambient
carrier.  Thus its oriented identity map is an identity relabelling of one
target complex; the resulting \([1,-1]\) class does not exclude the fixed
Regina move realization.

A source-only replay now records the exact local incidence for the two
distinct-endpoint pinches of common edges \(2,47\) and the loop drilling of
edge \(4\).  The first move acts on the degree-four edge star
\[
\{0,5,716,721\}
\]
and inserts gadget tetrahedra \(728,729\).  The reviewed corrected
\(\gamma_2\) coefficient chain is reconstructed independently from all 116
oriented source segments.  Of these, 72 have an ambient occurrence in that
closed star, and together they meet all four tetrahedra.  Therefore the first
move cannot be justified by a closed-star-disjoint identity argument.

That fixed three-dimensional local model is now exactly excluded.  Before
the move, the four-tetrahedron closed star is a valid triangulated 3-ball
with spherical boundary and disk vertex links.  In the proposed target
support, tetrahedron \(729\) identifies face \(1\) to its own face \(2\) by
the permutation \([0,2,1,3]\).  The resulting boundary vertex has an
annular link with
\[
(V,E,F)=(11,25,14),\qquad \chi=0,
\]
two boundary components and mod-two first Betti number one.  Hence the
source closed star and the closed-star-plus-gadget target cannot have a
face-compatible bijective PL common subdivision: their local vertex links
and boundary types differ.

The separate `relative_pinch_drill_transport` replay independently rebuilds
the same two induced complexes from the reviewed 728-tetrahedron source.  It
also records the stronger whole-support mismatch: source boundary Euler
characteristic two and \(H_1=0\), versus target boundary Euler
characteristic one and \(H_1=\mathbb Z\).  This remains a narrow obstruction
to that induced carrier, not to the ambient pinch.

Including both complete endpoint stars repairs the truncation.  Their union
has 56 source tetrahedra, while the pinched carrier has 58; both are valid
3-balls with the same 52-triangle frontier and trivial homology.  After
attaching one uniquely labelled locked tag tetrahedron to every frontier
face, the source and target reduce through respectively four and six legal
Regina moves to 99-tetrahedron terminals.  An orientation-preserving
terminal isomorphism fixes all 52 tags pointwise.  Thus the first pinch now
has an explicit relative PL equivalence, even though the earlier
closed-star-plus-gadget carrier does not.

For the second distinct-endpoint pinch, truncating to its induced endpoint
region is again not a manifold carrier: completing the bad vertex stars
propagates through the triangulation.  The replay therefore keeps the full
ambient complex and uniquely labels and locks all 644 old tetrahedra outside
the endpoint region.  A 25-move source chain and a 28-move target chain end
at the literally identical oriented 648-tetrahedron triangulation.  Every
locked exterior tetrahedron is fixed.  This is an ambient relative
equivalence, not a conclusion inferred from matching isomorphism
signatures.

The source torus is now also a genuine normal surface rather than a copy of
the final cusp with renamed cells.  The sum of the thin links of abstract
edges \(2,47,4\) splits into vertex-link spheres with coordinate sums
\(52,8,36\) and one connected orientable torus with 72 normal triangles and
12 normal quadrilaterals.  Splitting those quadrilaterals gives a strict
simplicial torus with
\[
(V,E,F)=(48,144,96).
\]
Every triangle retains its original ambient tetrahedron.  Regina
`cutAlong()` independently sees the corresponding two 96-triangle torus
boundary components.

After all three pinches, the ideal cusp link has
\[
(V,E,F)=(57,171,114).
\]
The source-to-cusp vertex map records a cusp germ
`(old tetrahedron, local cusp corner, other local vertex)`, since a global
loop-edge number alone does not distinguish its two germs.  Seventy-two
source normal triangles map directly to old-corner target triangles in the
same tetrahedra.  For each of the three pinched edges, the remaining
eight-triangle source normal-quad annulus and fourteen-triangle target
old-corner-plus-gadget annulus have exactly the same eight labelled boundary
edges.  Boundary-tagged Pachner chains give pointwise-relative
orientation-preserving equivalences for all three annulus pairs.

The standalone verifier reconstructs the two three-dimensional relative
maps, the normal-surface component split, all 96 source and 114 target
triangle carriers, and all three tagged annulus replays without importing
the builder or search module.  It rejects mutations of a gadget gluing,
attachment orientation, edge-2 move selector, normal split triangle, and
target tetrahedral carrier.  These legal move chains certify a carried
relative PL equivalence; a single composed common subdivision has not been
materialized.  This is Engineer-supported computational evidence pending
independent Reviewer replay.

There is nevertheless a valid two-dimensional lateral-tube map once the
invalid induced three-dimensional support is not mistaken for the carrier
itself.  The barycentric midpoint frontier of edge \(2\) has four
tetrahedral sectors, subdivided into sixteen exact quadrilaterals and 32
triangles.  The actual gadget-link annulus has six triangles; splitting its
four boundary edges gives ten.  Seven \(2\)-\(2\) flips, one \(1\)-\(3\)
subdivision, and two further \(2\)-\(2\) flips connect the coarse source
annulus to that target.  Overlaying the exact source subdivision produces an
oriented common refinement with
\[
(V,E,F)=(107,305,198),\qquad \chi=0.
\]
It is connected and orientable, has two boundary components, every internal
edge has valence two, and each triangle has rational barycentric carriers in
both its source tetrahedron and its target gadget tetrahedron.  Independent
replay reconstructs both Regina annuli, all ten moves, both area partitions
and every ambient face gluing; carrier and orientation mutations are
rejected.

The same incidence separates the 72 closed-star hits of corrected
\(\gamma_2\) into 66 genuine tube segments and six adjacent vertex-link
segments.  The common mesh transports the 66 tube segments coefficientwise:
64 are the eight meridional correction turns and two are the entry/exit
segments.  The remaining indices
\[
65,66,67,112,113,114
\]
form two three-edge paths in the punctured endpoint-link pieces.  The initial
annulus parameterization had to be replaced because its unique terminal
isomorphism swapped the endpoint boundary components.  An
endpoint-preserving source self-parameterization gives the same 198-triangle
mesh and passes the independent annulus replay.

The boundary map now extends over both full punctured endpoint-link disks.
The source disks contain the retained direction-star sectors and all nonstar
link triangles; the target disks are the 52- and 8-triangle components of the
merged vertex link.  Fixing each eight-edge annulus boundary and the relevant
outer gamma anchor, exact rational disk overlays produce 250 and 104 common
triangles.  Gluing them to the tube gives a connected orientable common sphere
with
\[
(V,E,F)=(278,828,552),\qquad \chi=2,
\]
and every edge has valence two.  A builder-free Regina verifier checks both
area partitions, pairwise non-overlap, all source and target ambient face
gluings, and signed coefficient transport.  For each of the six connectors it
binds the reviewed edge and oriented source endpoints to the exact
Regina-incidence source-mesh edge, requires the ordered common path to be a
gap-free monotone subdivision of that edge, reconstructs every target ambient
carrier, and matches the corresponding full-chain record fieldwise.  It
rejects carrier, orientation, boundary, anchor, and cross-segment path
mutations; in particular replacing segment `112`'s common path with segment
`113`'s path is rejected.  The six connector segments now join the 66 tube segments and 44
unchanged-complement segments into an ambient-continuous first-pinch transport
of all 116 reviewed segments.

A first bounded three-dimensional pilot now crosses the gadget.  Segment
`0`'s first transported edge is radially pushed from merged-vertex link height
\(2/3\) to \(3/4\) inside tetrahedron `729`, producing two exact oriented
trace triangles.  Independent Regina replay binds the bottom edge to common
edge `53` and the reviewed full-chain record, checks the tetrahedron
self-gluing and quotient embedding, and tests all six local ambient edges.
Although the carrier itself contains pinched bouquet edge `4` and proper-arc
edge `5`, the trace misses the entire ambient 1-skeleton.  It also misses the
vertex stars for \(Q\) and all four page cusps and remains in gadget
tetrahedra `728,729`, outside the 644 locked protected carriers.  Four
targeted carrier, orientation, bouquet-intersection, and locked-carrier
mutations are rejected.

This is one local product strip, not the missing embedded product annulus.
The transported coefficient chain has 148 step occurrences but only 71
distinct oriented ambient geometries; 11 groups repeat, with maximum
multiplicity eight.  Segments `0` and `8` already give identical bottom
edges, so a uniform radial extrusion self-overlaps.  The full construction
must transfer the reviewed occurrence-level lane order and genericized vertex
chords through the common surface before checking annulus topology, global
self-intersection, both boundary curves, and all disjointness conditions.  It
does not start the second pinch or license a target class or filling.

The occurrence-labelled reconstruction has now reached the full normal
frontier boundary, but the first global carrier fails.  The reviewed
116-segment chain subdivides into 954 embedded source pieces, and its
U-routed mate is an embedded 954-piece curve on 84 genuine normal disks.
The two curves are disjoint.  The two uniform-diagonal triangulations of the
straight stripwise mapping cylinder are abstract annuli with
\((V,E,F)=(1908,3816,1908)\), two boundary components, and Euler
characteristic zero.  Exact rational replay nevertheless finds a transverse
interior self-intersection for each diagonal: pieces `404,514` in original
tetrahedron `0`, and pieces `747,750` in original tetrahedron `2`.

There are actually \(2^{954}\) independent per-strip diagonal choices, not
only the two uniform choices.  Exact enumeration gives 279 strict
intersection clauses.  Their 954-variable 2-SAT formula is unsatisfiable,
with 35 contradictory variables and a four-clause core: choice `0` on piece
`674` conflicts with both choices on piece `680`, while choice `1` on piece
`674` conflicts with both choices on piece `679`.  All four core
intersections are strict in original tetrahedron `5`.  This excludes every
no-extra-vertex straight PL carrier for the fixed boundaries.

This is not a nonexistence proof for an embedded product annulus: a
non-ruled carrier with local interior vertices can evade the clauses.  The
construction below does so without changing either fixed boundary.

The tetrahedron-5 core now has a positive non-ruled resolution.  Instead of
retaining the intersecting internal strip seams, take the fixed source arc
through pieces `674`--`682`, the reversed target arc, and the two outer seams
as one 20-edge relative boundary.  Coning it to the interior rational point
\((23/2000,187/400,233/1000,36/125)\) gives an embedded 20-triangle disk.
Its explicit regular neighborhood is the join of a central edge with the
20-cycle: a geometrically embedded 20-tetrahedron PL 3-ball with
\(f=(22,61,60,20)\) and spherical boundary \(f=(22,60,40)\).  Exact replay
keeps every boundary edge pointwise, checks all target endpoints on the
genuine normal quadrilateral, and finds no improper intersection with either
diagonal choice of any of the 227 outside strips in tetrahedron `5`.  The
carrier lies in the open original tetrahedron, hence is quotient-injective
and misses \(Q\), the bouquet 1-skeleton, and the five named ideal vertices.
Face-pairing replay identifies tetrahedron `5`'s global vertices as
`[1,2,6,0]`, disjoint from the named cusp vertices
`[176,166,173,171,150]`; consequently the carrier misses their closed stars
as well.

The complete construction uses six such patches on piece intervals
`[674,683)`, `[701,710)`, `[714,723)`, `[829,838)`, `[840,846)`, and
`[945,954)`.  They replace 51 strips and all remaining contradiction
components; the fourth interval also removes piece `845`, whose individual
quadrilateral folds under either diagonal.  Of the original 279 strict
conflict clauses, 81 remain.  Fixing the two independently checked nonfolded
choices `751=1` and `923=1` leaves a satisfiable formula: 873 of the 903
remaining strips use diagonal `0`, and 30 use diagonal `1`.

The resulting complex has
\[
 (V,E,F)=(1914,3834,1920),\qquad \chi=0.
\]
It is connected and orientable, and its two boundary components are exactly
the 954-edge reviewed source curve and the 954-edge normal-frontier target
curve.  Independent replay reconstructs all 116 source segments and matches
all 60 nonzero coefficients of the reviewed sparse gamma chain.

Each patch has an explicit \(D^1*S^1\) join-ball carrier.  Five use 20
tetrahedra and one uses 14.  Exact replay checks their projected embeddings,
22,256 triangle--carrier-tetrahedron clips, and all three same-tetrahedron
carrier pairs.  Patch `P3` touches original face `0` only in the prescribed
outer seam `S829--T829`; the face pairs from tetrahedron `25` to `648`, so
the carrier is still quotient-injective.  The surface check covers 273,672
same-tetrahedron triangle pairs and 2,202 quotient-face trace pairs, with no
improper intersection.  The annulus misses the original 0/1-skeleton
containing \(Q\) and the bouquet.  At every named ideal vertex its
barycentric coordinate is at most \(1/2\), so it misses the open cusp sectors
beyond the normal frontier.

Independent content replay establishes this full product annulus.  It
reconstructs the frozen inputs rather than trusting completion flags and
confirms the topology, both boundary branches, coefficient chain, six
carriers, quotient embedding, and named-obstacle disjointness described
above.  The annulus alone still gives no surgery, SF2, or global
handle-slide conclusion.

## Ambient normalization of the target peripheral

The relative annulus maps do not by themselves determine a peripheral
framing: a boundary-pointwise annulus homeomorphism still has an integral
Dehn-twist ambiguity.  The ambiguity is fixed without consulting a filling
or a previously proposed slope.  On the first-pinch barycentric common
refinement, use the exact transverse tube seam through vertices
`[18,22,33]` at lifted coordinate \(x=0\).  Its relative image, ambient
image, and unique boundary connector give a closed comparison cycle in the
target annulus.  A saturated integral \(H^1\) generator evaluates that
cycle to \(-1\).  Thus the ambient map is the relative map precomposed with
one positive twist,
\[
 (x,y)\longmapsto(x+4y,y).
\]

The twist is not only a homology correction.  Intersecting all lifted
source triangles with translated target triangles gives an explicit
96-triangle exact-rational common refinement.  Exact area sums give full
cover on both sides, and the map fixes both boundary components modulo the
period.  Independent replay reconstructs this refinement and then
transports every one of the 954 target pieces through all three relative
PL equivalences.  The final path has 1,834 exact subsegments, is closed and
primitive, and has coordinates
\[
  (8,-1)\quad\hbox{in the source basis},\qquad
  (5,-1)\quad\hbox{in the native final-cusp basis}.
\]
The temporary SnapPea marking is
\[
  \mu=(-1,0),\qquad \lambda=(-5,-1),\qquad
  \det(\mu,\lambda)=1.
\]
Neither the builder nor the independent verifier opens a filling result,
stored target slope, or planar code.

Using this normalized marking, a fresh deterministic extraction gives an
oriented 121-crossing two-component diagram.  Its component event counts
are \((70,172)\), source-orientation signs are \((1,1)\), linking matrix is
zero, self-writhes are \((0,-3)\), and the blackboard-to-surface-zero
corrections are \((0,3)\).  A separate verifier reconstructs the PD, Gauss,
and DT encodings, component order, cusp maps, zero framings, and marked
exterior.

## Exact surgery mismatch for the finite diagram

The planar checks do not license the intended GST identification.  The
fresh temporary exterior has SHA-256
`1380594a465a381f66bdca7b2c3b7cbc674b94b6dd5cfa0cf9d9d1afc548e4e2`,
byte-for-byte equal to the earlier finite exterior, and the normalized
slope \((-5,-1)\) is the same unoriented filling as the earlier
\((5,1)\).  Independent Regina exact connected-sum decompositions of the
simultaneous zero filling return one prime summand with
\(H_1\cong\mathbb Z^2\).  They do not return the two minimal
\(S^2\times S^1\) summands required for
\(\#^2(S^1\times S^2)\).  Simplification produced 44- and
45-tetrahedron representatives in the two runs; tetrahedron count is not
canonical and does not affect the one-prime-summand conclusion.

Consequently this finite pinch/drill/page-filling diagram cannot be
standardized to the required target and is not a verified representative
of theorem-level GST \(L_3\).  This does not refute the open-book surgery
theorem quoted above; it refutes the present finite ambient-lineage route.
The next required comparison is stage-by-stage, starting from the marked
open-book representative and checking the component-labelled exterior and
exact zero surgery after the first pinch, edge-47 pinch, loop drill, and
each page filling.  The normalized longitude must not be changed in
response to this failure.

Jacobian 0.14.0 was invoked through protocol `2025-11-25` with operation
`topology.simplicial_complex.f_vector.compute`.  On the dedicated four-strip
payload it returned exact \(f=(8,16,8)\), dimension two and Euler
characteristic zero, deterministically in 0 ms with no adapter error or
timeout.  The inspected contract is capped at 64 vertices and 128 facets, so
this checks only the local abstract strip convention.  It does not verify
the full 1908-triangle annulus or either three-dimensional intersection.

The nice-triple algorithm of Lipshitz--Manolescu--Wang computes the hat
map from unpunctured domains.  It cannot substitute here because the
primitive non-torsion hat target is zero regardless of the desired
minus/infinity multiplier.  Setting \(U=1\) at divisibility one happens
only on homology; it does not erase basepoint multiplicities in the
triangle count.  A \(U\)-adically completed substitute also loses this
summand because \(U-1\) is a unit in \(\mathbb F_2[[U]]\).

Therefore \(m_{L_3,a}\bmod2\) has not been computed.  The non-torsion
image ideal remains a global handle-slide obstruction candidate, not a
separation and not a counterexample certificate.
