#!/usr/bin/env python3
"""Offline regressions for math-cite source downloads and legacy arXiv IDs."""

import contextlib
import gzip
import importlib.machinery
import importlib.util
import io
import tarfile
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


TOOL = Path(__file__).resolve().parents[2] / "tools" / "math-cite"
IDENTIFIER = "math/0611050v2"
METADATA = b"""<feed xmlns="http://www.w3.org/2005/Atom"><entry>
<title>Offline test</title><id>http://arxiv.org/abs/math/0611050v2</id>
<published>2006-11-02</published><updated>2006-12-01</updated>
<author><name>Test</name></author></entry></feed>"""


class MathCiteSourceTests(unittest.TestCase):
    def setUp(self):
        loader = importlib.machinery.SourceFileLoader("math_cite_test", str(TOOL))
        spec = importlib.util.spec_from_loader(loader.name, loader)
        self.module = importlib.util.module_from_spec(spec)
        loader.exec_module(self.module)

    def download(self, source, destination):
        requests = []

        def fake_get(url, timeout=60):
            requests.append(url)
            if url == "https://export.arxiv.org/api/query?id_list=math/0611050v2":
                return METADATA, "text/xml", url
            if url == f"https://arxiv.org/pdf/{IDENTIFIER}":
                return b"%PDF-offline-test", "application/pdf", url
            if url == f"https://arxiv.org/e-print/{IDENTIFIER}":
                return source, "application/octet-stream", url
            raise AssertionError(f"Unexpected network request: {url}")

        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(self.module, "get", side_effect=fake_get):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = self.module.arxiv(IDENTIFIER, destination)
        self.assertEqual(result, 0)
        self.assertEqual(len(requests), 3)
        self.assertIn(f"https://arxiv.org/pdf/{IDENTIFIER}", requests)
        self.assertIn(f"https://arxiv.org/e-print/{IDENTIFIER}", requests)
        self.assertEqual(stderr.getvalue(), "")
        self.assertNotIn("Traceback", stdout.getvalue())
        return stdout.getvalue()

    def test_normal_source_formats_through_arxiv(self):
        tex = b"\\documentclass{article}"
        archive = io.BytesIO()
        with tarfile.open(fileobj=archive, mode="w") as handle:
            info = tarfile.TarInfo("main.tex")
            info.size = len(tex)
            handle.addfile(info, io.BytesIO(tex))
        cases = [
            (tex, ".tex"),
            (gzip.compress(tex), ".tex.gz"),
            (gzip.compress(archive.getvalue()), ".tar.gz"),
        ]
        for source, suffix in cases:
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                output = self.download(source, root)
                saved = root / f"arxiv-math_0611050v2-source{suffix}"
                self.assertEqual(saved.read_bytes(), source)
                self.assertIn(f"saved {saved}", output)
                self.assertNotIn("TeX source not saved:", output)

    def test_corrupt_gzip_reports_failure_without_saving_source(self):
        cases = [
            b"\x1f\x8bbroken gzip",
            gzip.compress(b"test")[:-4],
            bytes.fromhex("1f8b0800000000000003070000000000000000"),
        ]
        for source in cases:
            with self.subTest(source=source.hex()), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                output = self.download(source, root)
                self.assertIn("TeX source not saved:", output)
                self.assertNotIn("(TeX source)", output)
                self.assertEqual([path.name for path in root.iterdir()], ["arxiv-math_0611050v2.pdf"])

    def test_metadata_failure_is_explicit_and_preserves_pinned_alternative(self):
        failures = [
            urllib.error.HTTPError("https://export.arxiv.org", 429, "Too Many Requests", {}, None),
            urllib.error.URLError("offline"),
        ]
        for failure in failures:
            with self.subTest(failure=str(failure)), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                output = io.StringIO()
                with patch.object(self.module, "get", side_effect=failure):
                    with contextlib.redirect_stdout(output):
                        result = self.module.main([IDENTIFIER, "--into", str(root)])
                self.assertEqual(result, 2)
                self.assertIn("metadata could not be retrieved", output.getvalue())
                self.assertIn(f"https://arxiv.org/pdf/{IDENTIFIER}", output.getvalue())
                self.assertEqual(list(root.iterdir()), [])

    def test_invalid_metadata_does_not_claim_missing_work(self):
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(self.module, "get", return_value=(b"not XML", "text/plain", "")):
                with contextlib.redirect_stdout(output):
                    result = self.module.arxiv(IDENTIFIER, Path(directory))
        self.assertEqual(result, 2)
        self.assertIn("metadata could not be retrieved", output.getvalue())
        self.assertNotIn("not found", output.getvalue())

    def test_unavailable_metadata_reports_failure_without_traceback(self):
        cases = [
            urllib.error.HTTPError("https://export.arxiv.org", 429, "Too Many Requests", {}, None),
            TimeoutError("metadata timed out"),
            self.module.ET.ParseError("invalid Atom feed"),
        ]
        for error in cases:
            with self.subTest(error=str(error)), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                output = io.StringIO()
                with patch.object(self.module, "get", side_effect=error) as request:
                    with contextlib.redirect_stdout(output):
                        result = self.module.main([IDENTIFIER, "--into", str(root)])
                self.assertEqual(result, 2)
                self.assertEqual(request.call_count, 1)
                self.assertIn("metadata could not be retrieved", output.getvalue())
                self.assertNotIn("Traceback", output.getvalue())
                self.assertEqual(list(root.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
