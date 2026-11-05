---
title: Sutherland 4966/46432 admissible tuple
description: Exact source identity, combinatorial properties, and current limitation of the largest-surplus audited MIT tuple.
---

# Sutherland 4966/46432 admissible tuple

The MIT primegaps publisher file `admissible_4966_46432.txt` has SHA-256
`0630c24e8daa87cdcf8f98a8426c800b12ac2f1b7b3fd64e2f6d6439674b2393`.
MIT index row 4987 and accepted-ledger row 7445 identify it as Sutherland's
current, accepted, validation-passed tuple with `k=4966` and `H=46432`.

The file contains exactly 4,966 strictly increasing distinct offsets in
`[0,46432]` and is admissible modulo every prime. Exact computation gives
`pi(46433)=4797`, surplus 169, and a defect allowance of 168 when targeting an
interval with at least 4,798 primes.

The frozen source and executable verification are under
`research/sutherland-4966-source-preparation/`. This establishes a source-bound
input only: no translation domain has been preregistered or searched, and no
Hardy--Littlewood B candidate is known from this tuple.
