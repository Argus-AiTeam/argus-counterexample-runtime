---
name: jacobian-cnf-source-binding
description: Use when submitting mathematical CNFs through the Argus Jacobian sidecar and independently replaying their exact assignments.
---

Use the Argus Jacobian bridge, not an in-process Jacobian import.

Construct distinct sorted variable names and non-tautological named
clauses. Inspect both `sat.cnf.canonicalize` and `sat.solve`. Keep compact
JSON payloads within the adapter's file bounds; preserve rejected requests
and their errors rather than interpreting them as solver outcomes.

Canonicalize through the inspected operation instead of guessing clause
ordering. Check that the returned variable list and signed clause set
match the original request, allowing only documented normalization.
Retain the named request, canonical output, solver payload, and typed
solver response.

Before accepting SAT, bind both the adapter request and the typed
response's `source` to the exact solver payload. Expand any component or
compressed-variable assignment and independently check every original
mathematical constraint. Checking only the compressed CNF is insufficient
when the reduction itself is part of the evidence.

Adapter rejection, timeout, and UNKNOWN are non-conclusions. A finite SAT
assignment is a finite witness, not an arbitrary-size theorem. A bare
UNSAT solver answer is not an independently checked refutation.
