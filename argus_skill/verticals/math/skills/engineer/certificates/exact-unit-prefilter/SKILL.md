---
name: exact-unit-prefilter
description: Avoid unnecessary full products in nonnegative routing algebras while preserving exact unit-target obligations, full positive supports, and runnable serialized certificate replays.
---

# Exact unit-target prefilter

Use this only when each basis pair maps to zero or one output basis type,
coefficients are nonnegative integers, and each required marked input
has an actual count-one witness.

1. Derive inverse target masks from the independent checker's own tensor,
   not a producer kernel or an unverified inverse table.
2. Multiply individually witnessed marker pairs first. Two distinct
   positive pairs targeting the same output rule out count one. For each
   surviving marked pair, intersect the inverse masks with both full
   positive supports, excluding only that pair. Any competitor rules out
   count one; no competitor makes its witnessed contribution exactly one.
3. Keep all positive competitors, including closed types and unmarked
   entries. Degree liveness is not the same as nonempty completion
   liveness. Apply only the original output projection.
4. If any unit obligation survives, reconstruct its entire positive
   output support before testing coverage. Never substitute completion
   masks for supports. If none survives, skip the full product but retain
   exact operation/orbit accounting.
5. Compare against literal full multiplication on bounded fixtures before
   production. Include asymmetric count witnesses, closed competitors,
   multiple unit markers, projection and interrupted prefixes. Controlled
   same-input comparisons must preserve semantic fields and every coverage
   counter; actual arithmetic-work counters may change and must count only
   work really performed.

Full-support automorphisms need not fix a witness's count vector. Transport
each marked input with its own realizable source origin; do not assume all
virtual markers are simultaneously unit in one graph.

To claim an empirical improvement, preserve the actual timing scope and
live resource evidence. A measured prefix does not establish a whole-search
speedup or a general CPU bottleneck.

## Serialized replay fidelity

Validate the exact published reproduction code against its serialized inputs,
not a nearby development helper. JSON arrays decode as lists; reconstruct
immutable tuple orders before calling memoized routing APIs that require
hashable arguments. In-memory tuple fixtures do not check this boundary.

Run the published replay verbatim from its declared project root with the
declared interpreter and import path. Preserve input hashes and check the
entire live coefficient domain or operation census actually claimed. A correct
mathematical identity does not make a failing reproduction program runnable.

Compare exact replay fields separately from declared timing metadata. If a
reproduction differs only in elapsed time, retain both source-bound outputs
and verify every mathematical field rather than requiring identical JSON
bytes or discarding the whole comparison. Never exempt counts, orders,
graph edges, coverage censuses or verdicts as nondeterministic metadata.
