import runpy
from pathlib import Path
import unittest


imports = runpy.run_path(
    str(Path(__file__).resolve().parents[2] / "tools" / "math-lean-source-closure")
)["imports"]


class ImportHeaderTests(unittest.TestCase):
    def test_mathlib_body_comment_marker_regression(self):
        self.assertEqual(imports(
            'import Mathlib\ndef marker : String := "/-"\n'
        ), ["Mathlib"])

    def test_body_strings_are_not_comments_or_imports(self):
        for marker in ('"/-"', '"-/"', '"--"', 'r#"/-"#',
                       '"\\nmeta import OAI.NotAnImport\\n"'):
            with self.subTest(marker=marker):
                self.assertEqual(imports(
                    f'import OAI.A\n\ndef marker : String := {marker}\n'
                ), ["OAI.A"])

    def test_meta_and_visibility_imports_are_retained(self):
        self.assertEqual(imports(
            "module\nprelude\n"
            "public import OAI.A\n"
            "meta import OAI.B\n"
            "public meta import OAI.C\n"
            "import all OAI.D\n"
            "meta import all OAI.E\n"
            "public section\n"
            'def marker : String := "/-"\n'
        ), ["OAI.A", "OAI.B", "OAI.C", "OAI.D", "OAI.E"])

    def test_nested_header_comments_and_multiline_directives(self):
        self.assertEqual(imports(
            "/- import Bad /- nested -/ -/\n"
            "import /- comment -/ OAI.A -- import Bad\n"
            "meta /- comment\n/- nested -/ -/ import\n OAI.B\n"
            "namespace Example\n"
            'def marker : String := "/-"\n'
        ), ["OAI.A", "OAI.B"])

    def test_malformed_or_unsupported_headers_are_rejected(self):
        for source in (
            "import\n", "meta import\n", "import all\n",
            "import ../Bad\n", "import OAI.A OAI.B\n",
            "import OAI.A.\n", "import «QuotedModule»\n",
            "import /- unfinished", "/- unfinished",
            "import Mathlib\n/- outer /- inner -/",
        ):
            with self.subTest(source=source):
                with self.assertRaises(ValueError):
                    imports(source)


if __name__ == "__main__":
    unittest.main()
