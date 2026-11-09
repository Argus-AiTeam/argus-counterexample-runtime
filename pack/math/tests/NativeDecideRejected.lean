import Mathlib

namespace Demo
theorem big : 2 ^ 20 = 1048576 := by native_decide
theorem small : (3 : ℕ) + 4 = 7 := by norm_num
end Demo
