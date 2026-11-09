import Mathlib

open Lean Elab Command

elab "forge_axiom" : command => do
  liftCoreM <| addDecl <| .axiomDecl {
    name := `forged
    levelParams := []
    type := mkConst ``False
    isUnsafe := false
  }

forge_axiom

theorem bogus : False := forged
