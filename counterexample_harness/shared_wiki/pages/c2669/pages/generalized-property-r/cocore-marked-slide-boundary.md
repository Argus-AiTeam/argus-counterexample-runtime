---
title: Cocore-marked slide law and GST Hopf-movie boundary
description: The inverse-transpose cocore law, complete C-star incidence action, a legal L3-to-L2 four-slide reduction, and the local triviality of every GST-direction Hopf-liberation slide and cancellation.
---

# Cocore-marked slide law and GST Hopf-movie boundary

## Stable facts

For an ordered oriented framed attaching link \(K\), the standard cocore disks
are represented by disjoint zero-framed blue meridians.  If handle \(i\) is
slid over handle \(j\) with sign \(\epsilon\), then
\[
A=I+\epsilon E_{ij},\qquad
\Lambda'=A\Lambda A^T,\qquad
D'=A^{-T}D.
\]
Equivalently, \(D'_j=D_j-\epsilon D_i\), while \(D'_i=D_i\).
The dual disk is represented by band-summing the old \(j\)-meridian with a
\(-\epsilon\)-oriented parallel of the \(i\)-meridian along the dual band.
A cup move supplies the parallel disk, and the band follows the framed
undotted component.  These are moves in Definition 2.22 of
arXiv:`2512.15395v1`.

The inverse slide changes \(\epsilon\) to \(-\epsilon\).  Component
permutations act by the same permutation on cocores.  Reversing an attaching
orientation requires reversing the paired cocore orientation; the diagonal
framing is unchanged and the corresponding off-diagonal linking signs
reverse.

For a regular banded unlink, let \(H_{\alpha i}\) be the linking matrix
between dotted and undotted components and let \(z_U\) be the linking row
of an oriented blue circle.  The complete Definition 2.22 move set
preserves, up to natural basis isomorphism, the surface-component total
\[
\left[\sum_{U\subset\Sigma}z_U\right]\in
\mathbb Z^m/\operatorname{rowspan}_{\mathbb Z}(H).
\]
An undotted component swimming through a band changes the two endpoint
rows by opposite unit vectors.  A blue circle sliding under a dotted
component changes its row by a row of \(H\).  Undotted slides apply the
same unimodular column operation to \(H\) and every blue row.  Adding a
canceling dotted/undotted pair sends \(H\) to
\(\operatorname{diag}(H,\pm1)\) and every blue row to \((z,0)\), so the
quotient is canonically unchanged.

## Source applicability

Definitions 2.10, 2.17, and 2.22 and Proposition 2.23 of
arXiv:`2512.15395v1` give the ambient 2-deformations, the definition of
1-isotopy, the band moves, and their exact diagrammatic completeness for
**ribbon surfaces**.  They do not state an inverse-transpose cocore law and do
not make an arbitrary proper disk system ribbon.  The standard cocores satisfy
the missing premise because their belt circles are represented by disjoint
small meridians.

Theorem 4.9 gives a 1-isotopy invariant only after choosing a unimodular
ribbon category and compatible banded-unlink, Bobtcheva--Messia, and Hennings
data.  It is not a complete invariant and supplies no GST endpoint value
without a concrete marked banded-unlink diagram.

GST Proposition 10.1, DOI `10.2140/gt.2010.14.2305`, assumes the full
generic-immersed-torus setup and a fiber \(C_0\) bounding a disk with algebraic
intersection \(\pm1\).  It proves that the \(L_n\) become slide equivalent
after one canceling Hopf pair.  For \(L_{n,k}\) it states that each adjacent
\(n\)-step uses four slides, but the sign depends on the choice of \(C_0\) and
travel direction.

## Remaining marked endpoint

The GST proof itself does not list:

1. the signed cyclic order and bands of the four slides in Figure 18; or
2. the number, order, signs, and bands of the strand-clearing slides through
   the disk bounded by the dotted component during Hopf liberation.

Those are exactly the dual-band data that determine the image of the two
original cocores only when the slide direction can mix a marked dual row.
The source-bound circuit below fixes an attaching-slide representative and a
complete regular banded-unlink reduction for one instance of item 1.  Its
first naturality-based word remains rejected, but a replacement using
undotted-component swims is legal.  Item 2 is now settled uniformly: GST
explicitly makes the offending original strand the target and the meridian
\(C\) the source, so every original target cocore is fixed and only unmarked
\(D_C\) changes.  Cycle 14 fixes the \(L_{3,1}\) input and its zero surgery,
but it reconstructs Figures 9--13 rather than the complete remaining marked
movie.

Therefore no terminal ribbon surface in \(W_{U_2}\) is presently fixed, and
neither an explicit 1-isotopy to the standard unlink cocores nor a separating
full-move invariant has been obtained.  The cocore marking is a candidate
route, not a global handle-slide obstruction.

## Hopf-liberation locality

Orient the disk \(D\) bounded by the dotted \(C^*\) so that its zero-framed
meridian satisfies \(I(C,D)=+1\).  If an offending point of
\(K_i\cap D\) has sign \(\delta\), the clearing sign is
\(\epsilon=-\delta\) in
\[
K_i\leftarrow K_i+\epsilon C.
\]
The \(\epsilon=+1\) and \(\epsilon=-1\) local frames each have two old
\(C^*-K_i\) crossings and two oppositely signed crossings copied from the
\(C^*-C\) Hopf clasp.  Their complete cyclic crossing orders give two
same-component framed RII disks with empty interiors.  The slide band follows
the zero framing of \(C\), is disjoint from the physical marked meridian
\(\mu_i\), and preserves the framing of \(K_i\).

For the full dual basis,
\[
D'_{K_i}=D_{K_i},\qquad D'_C=D_C-\epsilon D_{K_i}.
\]
The parallel copy and dual band realizing the second formula both have the
unmarked physical surface ID `Sigma_C_aux`; neither is part of the marked
\(\Sigma_i\).  For an arbitrary finite word all factors share source \(C\),
so \(E_{iC}E_{jC}=0\), the factors commute, and every original cocore remains
fixed independently of order.  After all actual intersections are removed,
the isolated \(C/C^*\) 3-ball contains no surviving \(K_i\), marked blue
circle, or marked band.  Canceling the pair therefore leaves the identical
ordered marked unlink.  This uses no cap move and makes no carrier
reassignment.

The exact frames, physical IDs, framings, crossing carriers, inverse replay,
finite-word calculation, and cancellation-ball inventory are in
`research/cocore_marked_topology/hopf_liberation/`.  Independent Reviewer
replay of one positive and one negative frame, the finite induction, and the
cancellation ball is still required.

## Frozen \(L_{3,1}^*\to L_{2,1}^*\) circuit

One representative of the previously unspecified four-slide step is now
fixed.  Use the Cycle-14 orientations, identify the small fixed component as
\(P\) and the large \(n\)-dependent component as \(Q\), and take \(C_0\) to
be the oriented meridian of the red \([-1]\)-framed component.  Its auxiliary
coefficient is \(+1\) in Figure 18 and \(+2\) after red surgery.  Traveling
opposite Figure 16's positive \(t\)-direction gives
\[
 C\leftarrow C-P,\quad Q\leftarrow Q-C,\quad
 C\leftarrow C+P,\quad Q\leftarrow Q+C.
\]
The two local \(Q/C\) moves are Figure 17 backwards at the \(+3\) box and
forwards at the \(-3\) box, so
\[
 (3,-3)\longmapsto(2,-3)\longmapsto(2,-2).
\]
The reviewed Figure 18 source matrix, after adjoining this meridian and
blowing down the red unlink, is
\[
\begin{pmatrix}0&0&1\\0&0&-3\\1&-3&2\end{pmatrix}
\]
in order \((P,Q,C)\).  Frame-by-frame congruence ends at the same matrix with
\(3\) replaced by \(2\), and the net attaching slide is
\(Q\leftarrow Q+P\).

Before the red blow-downs, the dotted push-off \(C^*\) has row
\((0,1,0,0,0)\) against \((R_+,R_-,P,Q,C)\), represented by two positive
\(C^*-R_-\) crossings.  The \(R_+\) blow-down does nothing to this row.
The \(R_-\) blow-down creates signed full twists giving
\((1,-3,1)\) against \((P,Q,C)\).  Copying the complete signed crossing
multiset through the four slides gives
\[
(1,-3,1),(1,-3,0),(1,-3,0),(1,-3,1),(1,-2,1)
\]
at \(F_0,\ldots,F_4\).

The physical ribbon-handle expansion is not the four-letter algebraic word.
At the third ambient slide, the copied current \(C\)-disk already contains
the band created at the second slide.  The transport therefore has physical
band counts
\[
 0,1,2,4,5,
\]
with five bands \(a,b,c,d,e\) at \(F_4=B_0\).  The first reduction move
slides the endpoint of the same physical band \(d\) over \(c\); it
preserves the physical ID set \(\{a,b,c,d,e\}\) and reaches \(B_1\).

The old continuation incorrectly used naturality to reassign crossings
from \(c_\pm,q_\pm\) to bands and remains rejected.  The legal continuation
uses four undotted-component swims.  Swimming \(C\) through \(a,c\)
transfers the opposite Hopf clasps from \(c_\pm\) directly to \(p0\).
Two framed RII moves then involve the same pair \((p0,C)\); two reverse
cups remove \(a,c,c_\pm\).  Swimming the current \(Q\)-component through
\(b,e\) similarly transfers the \(q_\pm\) clasps to \(c0\), where two RII
and two reverse cups remove them.  Therefore
\[
 5\longrightarrow5\longrightarrow3\longrightarrow3\longrightarrow1
\]
is reached by a 13-move Definition 2.22 movie.

The failure occurs before the proposed reverse cups.  Definition 2.22
naturality moves a \(U\cap B\) attachment through a crossing; it does not
replace either strand at that crossing.  Consequently the fixed cup-target
crossings retain their blue carriers, and their linking numbers remain
\[
\operatorname{lk}(c_+,C)=1,\quad
\operatorname{lk}(c_-,C)=-1,\quad
\operatorname{lk}(q_+,Q)=1,\quad
\operatorname{lk}(q_-,Q)=-1.
\]
The proposed LC_C/LC_Q words instead perform 16 carrier reassignments from
cup circles to bands.  Their four claimed Reidemeister-II pairs also combine
crossings on two different blue components, so they do not bound RII disks.
Finally, a ball disjoint from the target and containing one of these cup
circles would make that circle bound a disk in the target complement and
force the corresponding linking number to vanish.  Hence none of the four
claimed isolation balls can exist after the listed move prefixes.

The rejected word does not reach \(B_2,B_3,B_4\), but the replacement
undotted-swim word does.  Its endpoint has one physical band and relation
\[
D_P\longmapsto D_P-D_Q,\qquad D_Q\longmapsto D_Q,\qquad
D_C\longmapsto D_C
\]
with no auxiliary \(C\)-branch.

The source binding pins `gompf6.eps` by SHA-256, marks \(C_0\) on red path
13, the two \(P\)-supports on the two arcs of path 2, and the two
\(Q\)-supports on the \(+n\) and \(-n\) boxes.  The complete
\(F_0\)-\(F_4\) transport, \(C^*\) signed incidence, rejected naturality
word, and replacement \(B_0\)-\(B_4\) movie are recorded in
`research/cocore_marked_topology/four_slide_circuit/`.  In particular,
`linked_cup_reduction.json` preserves the failed word,
`linked_cup_verification.json` records the 16 carrier, four RII-incidence,
and four isolation-ball failures, and
`full_move_cancellation.md` gives the full generator calculation and legal
replacement.
The bounded Jacobian `ACCEPTING_PAIR` result replays only the encoded 52-edge
forward/inverse token path.  Its state omitted crossing-component incidence,
so it is not topological evidence.

The \(C^*\) row, first swim, full four-slide reduction, and Hopf-liberation
locality theorem still require independent Reviewer replay.  The
strand-clearing bands may remain unfrozen because the theorem covers every
correctly directed finite word, but the complete remaining marked GST
endpoint, a full-move separator, and a global handle-slide obstruction remain
open.
