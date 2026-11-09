import Mathlib

theorem two_add_two : (2 : ℕ) + 2 = 4 := by norm_num

theorem sq_nonneg' (x : ℝ) : 0 ≤ x ^ 2 := by positivity
