from __future__ import annotations

import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_source_package_imports(self) -> None:
        __import__("src")

    def test_example_csv_has_non_empty_identifiers(self) -> None:
        example = ROOT / "examples" / "compounds.csv"
        with example.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            self.assertIsNotNone(reader.fieldnames)
            self.assertIn("name", reader.fieldnames)
            rows = list(reader)

        self.assertTrue(rows, "example input must contain at least one compound")
        for line_number, row in enumerate(rows, start=2):
            self.assertTrue(
                row.get("name", "").strip(),
                f"missing compound identifier on CSV line {line_number}",
            )


if __name__ == "__main__":
    unittest.main()
