---
title: Exact identity-gain search
description: Deterministic normal-form beam, compact exhaustive search, exact replay contract, and their limitations.
---

# Exact identity-gain search

For a frozen routing template, each type state has an exact increment in
Thompson group \(F\), and admissible state transitions form a finite directed
graph. The relation-guided search keeps, for each terminal state and exact
reduced product, one deterministic path whose product has low normal-form
complexity. Its score uses reduced length, the two abelianization coordinates,
and the largest generator index. This differs from exhaustive enumeration by
walk length: it retains a fixed-width exact frontier selected by algebraic
complexity.

A search hit is accepted only after
`scripts/ring_p22_overlap_gain.py` reconstructs every declared transition,
left-multiplies its labels in traversal order, and reduces the final product to
the identity. The stored finite state cycle is therefore an exact
identity-gain certificate. A beam miss is only a bounded search failure and
does not support injectivity, zero kernel, or grammar exhaustion.

The classifier applies previously stored exact relations first. For a template
that survives the short searches and exact degree-5 through degree-7
common-multiple probes, it runs the relation-guided beam before exhaustive
length-21 and length-24 searches and the degree-8 common-multiple probe. A miss
falls through to all unchanged exact mechanisms, whose phase timings are
reported separately. Exact records under
`research/ring_p22/overlap_gain/residual_relation/` cover both retained
routings for coefficient pairs \(24/290\), \(40/145\), \(40/194\),
\(144/261\), and \(144/262\), with cycle lengths between 25 and 44.

The exhaustive meet-in-the-middle fallback uses the same exact normal-form
rewriting in a native side library. Its retained normal-form keys store the
bounded length-24 representation inline rather than allocating two vectors per
key. On the fixed \(98/152\), R02/R01 length-19 absence replay, this changed
peak RSS from 1,008,856 to 576,496 KiB and elapsed time from 57.87 to 52.23
seconds. The compact and prior native implementations, together with the
Python implementation, agreed on all 141 tested routing pairs through length
eight; every returned cycle was replayed exactly. This is an implementation
improvement only: an exhaustive search miss remains bounded by the declared
walk length.

Repeated exact target-gain queries retain the typed native function for the
life of the Python process. The native side caches each exact half-path table
by routing and path length, while every target still receives an independent
normal-form lookup and exact replay. On one controlled \(42/145\) length-16
negative lookup, constructing the table took 3.300 seconds and the identical
lookup against the retained table took 0.896 seconds. This changes neither the
target language nor the evidentiary status of a miss.

An exact relation may also transfer when one of its increments is replaced by
an admissible path with exactly the same reduced gain. Applying this local
detour rule to reviewed relation `W18755` replaces two occurrences of \(a_2\)
by \((b_3,a_5,a_2,b_4)\). Direct replay gives length-61 identity-gain cycles
for \(38/152\) with routes R04/R00 and \(39/152\) with routes R06/R00. The
stored records are
`residual_relation/38-152-R04-R00.json` and
`residual_relation/39-152-R06-R00.json`. Exhausting a bounded detour grammar
without a transfer remains a search miss, not a no-cycle certificate.

Equal-gain block replacement can also expose an exact open identity relation
whose only defect is its cyclic join. For \(152/162\), routes R01/R02, two
copies of that relation have two bad joins. Enumerating the 651 admissible
connector paths of lengths one through four at each join found a pair with
mutually inverse gains. Inserting that pair gives an exactly replayed
length-54 admissible identity cycle. The same state sequence and labels replay
unchanged on the shared states of \(152/226\) and \(152/418\), also with routes
R01/R02. The wrapped records are under
`joint_connector/152-162-doubled-l4.json`,
`joint_connector/152-226-doubled-transfer.json`, and
`joint_connector/152-418-doubled-transfer.json`.
The same construction applied after two exact block replacements on
\(98/152\), routes R02/R01: doubling its length-25 one-defect relation and
pairing inverse-gain connectors gives the replayed length-52 record
`joint_connector/98-152-doubled-l4.json`.

For relations with several bad joins, the exact connector product can also be
split asymmetrically. After fixing short paths at all but one join, the group
equation determines the remaining connector gain, which is sent to the exact
target-path engine. A complementary split enumerates two longer connector
gain maps and looks up the required inverse product while the other joins stay
short. Both constructions replay the complete repaired cycle before emitting
a witness; failure at declared connector lengths remains bounded evidence.

An exact common multiple for a coefficient pair can also lift through a larger
target pair when each target routing restricts to a declared routing of the
source coefficients. The source even-incidence family then constructs an
identity cycle using only restricted states; extra target terms are never
visited, and target replay verifies that both gains and forbidden-transition
rules agree. The reviewed degree-ten \(34/152\) kernel lifts to length-110
cycles for \(35/152\) R03/R00 and, after swapping colours, \(152/290\)
R01/R02. The reviewed degree-ten \(42/144\) kernel lifts to length-110 cycles
for \(42/145\) R01/R03, \(42/400\) R00/R02, and \(42/464\) R00/R06.
`scripts/ring_p22_subkernel_transfer.py` replays the source common multiple,
checks the routing restriction, constructs the source cycle, and regenerates
the complete target record. The five certificates are stored under
`subkernel_transfer/`.

These certificates reject templates only inside
`B_leaf_identity_gain_pl_v1`. They are not common multiples unless a separate
even-incidence construction says so, and they do not settle any coefficient
pair globally or settle amenability of \(F\).
