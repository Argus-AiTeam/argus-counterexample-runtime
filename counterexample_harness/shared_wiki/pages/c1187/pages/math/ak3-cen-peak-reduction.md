---
title: AK(3) directed-CEN peak-reduction boundary
description: Exact height-15 critical plateau showing that the universal local CEN peak-replacement mechanism fails.
---

Write \(A=a^{-1}\), \(B=b^{-1}\).  In Ivanov's directed CEN graph, the AK(3)
tuple
\[
  (aaaBBBB,\;abaBAB)
\]
has an exact CT1--CT3 path to the cyclic classes represented by
\[
  (AAAAbbb,\;ABAbab)
\]
with maximum total cyclic length 15.  The path has seven CT2 moves with total
cancellation counts
\[
  2,3,3,3,3,3,4
\]
interspersed with explicit CT1 and CT3 moves.  Its complete literal witness is
recorded in
`research/experiments/ak3-cen-peak-reduction/certificate.json`.

The endpoint cannot be reached with maximum total cyclic length at most 14.
Modulo CT3, the complete AK(3)-reachable sublevel has exactly the four signed
states obtained independently inverting the two original components.  The
corresponding literal CT3 orbits contain 168 states.  Across all signs, both
choices of replaced component, and all \(7\cdot6\) cyclic alignments, at most
two inverse pairs cancel.  Thus replacing the length-7 component has target
total length at least 15, while replacing the length-6 component has target
total length at least 16.

At height 15 the full directed component has 104 CT3 quotient states (8 at
length 13 and 96 at length 15) and 5,520 literal states.  Exact
lexicographic Dijkstra replay for complexity
\[
  (\text{maximum length},\text{maximal-state occurrences},\text{edge count})
\]
gives \((15,6,8)\) in the CT3 quotient and \((15,9,13)\) to the displayed
literal endpoint.

Therefore the universal assertion that every AK(3)-reachable highest CT2
plateau admits a replacement of lower maximum length is false.  This is only
a boundary for that local peak-reduction strategy.  It does not show that
AK(3) reaches the basis, does not show that every hypothetical path to the
basis needs height above 13, and supplies no Andrews--Curtis obstruction.
