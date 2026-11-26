import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from privacy_check import check_bytes, jpeg_findings, private_path, text_findings

class PrivacyTests(unittest.TestCase):
    def test_detects_without_returning_values(self):
        values = ["person" + "@" + "example.test", "ghp_" + "a"*32, "sk-" + "a"*32, "AKIA" + "A"*16,
                  "C:" + r"\Users" + r"\sample\file", "pass" + 'word = "' + "abcdefgh" + '"',
                  "600" + " 123" + " 456"]
        for value in values:
            with self.subTest(kind=len(value)):
                result = text_findings(value)
                self.assertTrue(result)
                self.assertNotIn(value, repr(result))
        self.assertFalse(text_findings("123+example" + "@" + "users.noreply.github.com"))

    def test_private_paths_and_public_templates(self):
        for path in ["private/notes.md", "reportes/result.md", ".env.test", "credentials.json",
                     "export.csv", "Session_Review_20260101.md", "../file.md"]:
            self.assertTrue(private_path(path))
        for path in ["templates/Session_Errors_TEMPLATE.csv", "modules/profile.md", "index.html"]:
            self.assertFalse(private_path(path))

    def test_jpeg_metadata_and_binary(self):
        clean = b"\xff\xd8\xff\xe0\x00\x07JFIF\x00\xff\xda"
        self.assertEqual(jpeg_findings(clean), [])
        self.assertTrue(jpeg_findings(b"\xff\xd8\xff\xe1\x00\x06Exif\xff\xda"))
        self.assertTrue(jpeg_findings(b"\xff\xd8\xff\xfe\x00\x04hi\xff\xda"))
        self.assertTrue(check_bytes("unknown.bin", b"\xff\xfe"))
        self.assertFalse(check_bytes("readme.md", b"Generic learning material."))
