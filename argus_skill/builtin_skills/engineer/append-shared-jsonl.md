---
name: append-shared-jsonl
description: Append public records at the real log end while preserving other writers' records.
---

Read the actual final record immediately before constructing an append patch. The last known record for your own role may precede other writers' records.

Anchor an `apply_patch` update at the observed file tail and use `*** End of File` to require an end-of-file match. If the tail changes, read it again and update the anchor instead of overwriting another writer.

Afterward, verify that the original record sequence, excluding only records you created, is unchanged and that new records form a suffix. When repairing your own misplaced insertion, move only your records; preserve every other record and its relative order.
