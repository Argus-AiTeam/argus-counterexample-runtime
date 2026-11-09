# Reviewing an OpenAI family with Argus on ts-core

1. Install the `math` pack (`pack/math/`) into Argus: copy the folder to `<argus home>/skill-packs/math`.
   Argus runs its setup once (Lean 4.31.0 and Mathlib). To reuse an existing Mathlib build instead of
   downloading about 5 GB, start Argus with `MATH_PACK_MATHLIB_FROM=<workspace>` set.
2. Make a workspace for the family:

       ops/openai-family/make-workspace 127 ~/workspaces --lang zh    # or --lang en

   It copies the family's papers from openai/math @ 4eaee875 and Argus's earlier drafts from
   argus-mathematics (without earlier verdicts, so they are rechecked), and writes `REQUEST.md`.
3. Open an Argus project on that workspace and paste `REQUEST.md` as the request.

What comes back: `guide/<paper>.md` for each paper (a reader's guide, then the verdict; the one
record of the work), any Lean or computations next to it, and a letter that opens with the verdict
for each paper. Routes given up are in the team wiki.
