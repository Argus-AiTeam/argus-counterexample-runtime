---
title: Ramadoss second-kind Cunningham source boundary
description: Restricted-source boundary and the exact distinction between a fixed infinite chain and target-compatible varying-seed chains.
---

DOI `10.5281/zenodo.21017797` identifies Shyam M.Ramadoss's
*Analysis on Safe-primes, Cunningham-Chain, and Sophie-Germain Primes*. The
official Zenodo record is public metadata with restricted files, no public file
entries, and no enabled access-request path. DataCite lists only the concept DOI
and this single version, both without content URLs. A bounded search of
OpenAIRE, OpenAlex, CORE, HAL, OSF, Internet Archive, Wayback, and the public
ORCID record found no independent complete copy. Therefore the abstract's
"Infinitude" wording cannot be promoted to a theorem statement or assigned
quantifiers; this mechanism is blocked on lawful source access, not retired
mathematically.

Independently of that source, the standard numerical second-kind recurrence
\[
q_{j+1}=2q_j-1
\]
has
\[
q_j=2^{j-1}(q_1-1)+1.
\]
For the fixed seed \(q_1=2\), the sequence begins \(2,3,5,9\) and
stops. For a fixed odd prime seed \(q_1=p\), if
\(d=\operatorname{ord}_p(2)\), then \(p\mid q_{d+1}\) and
\(q_{d+1}>p\). Thus one fixed seed cannot give a single infinite all-prime
chain. This does not rule out arbitrarily long finite chains with a seed that
depends on length.

The fixed-exponential target requires
\[
q_1(L)\le
1+\left\lfloor\frac{C^L-1}{2^{L-1}}\right\rfloor
\]
for one fixed \(C\), equivalently \(q_L(L)\le C^L\). Merely proving infinitely
many chains of one fixed length, or arbitrary lengths with uncontrolled first
terms, would not suffice.
