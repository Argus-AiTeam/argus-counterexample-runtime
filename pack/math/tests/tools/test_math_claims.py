#!/usr/bin/env python3
"""Offline regressions for claims evidence paths and source classification."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


TOOL = Path(__file__).resolve().parents[2] / "tools" / "math-claims"
HEADER = "| Claim | Source | Basis | Evidence |\n|---|---|---|---|\n"


class MathClaimsPathTests(unittest.TestCase):
    def run_claims(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOL), *map(str, args)],
            capture_output=True, text=True, check=False,
        )

    def test_all_basis_paths_and_legacy_check_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "report.md"
            for basis in ("checked by hand", "conditional on a cited result"):
                with self.subTest(basis=basis):
                    report.write_text(HEADER + f"| local claim | ours | {basis} | `missing.pdf` |\n")
                    self.assertEqual(self.run_claims("--check", report).returncode, 0)
                    checked = self.run_claims("--check-paths", report)
                    self.assertEqual(checked.returncode, 1)
                    self.assertIn("missing.pdf not found", checked.stdout)
            (root / "present.pdf").write_bytes(b"evidence")
            report.write_text(HEADER + "| local claim | ours | checked by hand | `present.pdf` |\n")
            self.assertEqual(self.run_claims("--check-paths", "--check", report).returncode, 0)

    def test_column_counts_and_escaped_bars(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.md"
            for row in (
                "| norm |x| | ours | checked by hand | report section |\n",
                "| claim | ours | checked by hand |\n",
            ):
                with self.subTest(row=row):
                    report.write_text(HEADER + row)
                    checked = self.run_claims("--check-paths", report)
                    self.assertEqual(checked.returncode, 1)
                    self.assertIn("report.md:3: expected 4 claims columns", checked.stderr)
            report.write_text(HEADER + r"| norm \|x\| | ours | checked by hand | report section |" + "\n")
            self.assertEqual(self.run_claims("--check-paths", report).returncode, 0)
            report.write_text(
                "| Claim | Source | Basis | Evidence | Extra |\n|---|---|---|---|---|\n"
                "| claim | ours | checked by hand | section | extra |\n"
            )
            checked = self.run_claims("--check-paths", report)
            self.assertEqual(checked.returncode, 1)
            self.assertIn("report.md:1: expected 4 claims columns", checked.stderr)

    def test_missing_computation_evidence_and_lean_path_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "report.md"
            report.write_text(HEADER + "| claim | ours | checked by computation | none |\n")
            self.assertEqual(self.run_claims("--check-paths", report).returncode, 1)
            (root / "Main.lean").write_text("-- path-only test; do not compile\n")
            report.write_text(HEADER + "| claim | ours | proved in Lean | `Main.lean` |\n")
            self.assertEqual(self.run_claims("--check-paths", report).returncode, 0)

    def test_prose_numbered_locators_are_not_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.md"
            for basis in ("checked by hand", "conditional on a cited result"):
                for evidence in ("\u672c\u6587 \u00a71.2", "Theorem 1.4", "Sections 1.2-1.4"):
                    with self.subTest(basis=basis, evidence=evidence):
                        report.write_text(HEADER + f"| claim | ours | {basis} | {evidence} |\n")
                        for flags in (("--check-paths",), ("--check-paths", "--check")):
                            checked = self.run_claims(*flags, report)
                            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            for evidence in ("Theorem 1.4; missing.pdf", "evidence/missing", "`1.4`"):
                with self.subTest(evidence=evidence):
                    report.write_text(HEADER + f"| claim | ours | checked by hand | {evidence} |\n")
                    self.assertEqual(self.run_claims("--check-paths", report).returncode, 1)
            (Path(directory) / "present.pdf").write_bytes(b"evidence")
            report.write_text(
                HEADER + "| claim | ours | checked by hand | Theorem 1.4; present.pdf |\n"
            )
            self.assertEqual(self.run_claims("--check-paths", report).returncode, 0)
            report.write_text(
                HEADER + "| claim | ours | checked by computation | Theorem 1.4 |\n"
            )
            for flag in ("--check", "--check-paths"):
                self.assertEqual(self.run_claims(flag, report).returncode, 1)

    def test_help_exit_status(self):
        for flag in ("--help", "-h"):
            with self.subTest(flag=flag):
                result = self.run_claims(flag)
                self.assertEqual(result.returncode, 0)
                self.assertIn("--check-paths", result.stdout)
        self.assertEqual(self.run_claims().returncode, 2)

    def test_chinese_claim_header_and_basis_labels(self):
        cases = (
            ("手算核验", "hand"),
            ("计算核验", "computation"),
            ("条件于已核文献", "conditional"),
            ("未定", "open"),
            ("反驳", "refuted"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "report.md"
            evidence = root / "evidence.txt"
            evidence.write_text("test evidence\n")
            for basis, expected in cases:
                with self.subTest(basis=basis):
                    report.write_text(
                        "| 主张 | 来源 | 依据 | 证据 |\n|---|---|---|---|\n"
                        f"| claim | 本文，按论文推导 | {basis} | `evidence.txt` |\n"
                    )
                    result = self.run_claims("--list", "--check-paths", report)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn(f"[{expected} · ours] claim", result.stdout)
            evidence.unlink()
            result = self.run_claims("--check-paths", report)
            self.assertEqual(result.returncode, 1)
            self.assertIn("evidence.txt not found", result.stdout)

    def test_leading_source_label_precedes_later_citations(self):
        cases = (
            ("ours, consequence of the paper proof", "ours"),
            ("ours, \u4ece\u539f\u6587\u5f15\u7406\u63d0\u53d6", "ours"),
            ("\u6211\u4eec, \u6cbf\u539f\u6587\u8bc1\u660e", "ours"),
            ("earlier draft, compared with the paper", "earlier draft"),
            ("literature, arXiv theorem cited by the paper", "literature"),
            ("paper, comparison with ours", "paper"),
            ("\u8bba\u6587\uff0c\u00a74 \u547d\u9898\uff1b\u6587\u732e\u8f93\u5165", "paper"),
            ("\u6587\u732e\uff0c\u88ab\u8bba\u6587\u5f15\u7528", "literature"),
            ("the paper proof", "paper"),
        )
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.md"
            for source, expected in cases:
                with self.subTest(source=source):
                    report.write_text(
                        HEADER + f"| claim | {source} | checked by hand | section |\n"
                    )
                    result = self.run_claims("--list", report)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn(f"[hand \u00b7 {expected}] claim", result.stdout)


if __name__ == "__main__":
    unittest.main()
