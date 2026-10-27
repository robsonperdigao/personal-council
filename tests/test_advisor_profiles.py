"""Static contracts only; these tests do not evaluate AI model behavior."""
from pathlib import Path
import re
import unittest

CATALOG = Path(__file__).resolve().parents[1] / "advisors" / "historical"
SECTIONS = [
    "Mandate", "Core principles", "Personality and communication",
    "Reasoning method", "Signature questions", "Dissent and blind spots",
    "Source notes", "Response examples", "Limits",
]

class ProfileContracts(unittest.TestCase):
    def test_three_sample_advisors(self):
        self.assertGreaterEqual(len(list(CATALOG.glob("*.md"))), 3)

    def test_schema_and_differentiation(self):
        ids, methods, questions = [], [], []
        for file in CATALOG.glob("*.md"):
            with self.subTest(file=file.name):
                body = file.read_text(encoding="utf-8")
                match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
                self.assertIsNotNone(match)
                identifier = re.search(r"^id:\s*([a-z0-9-]+)\s*$", match.group(1), re.M)
                self.assertIsNotNone(identifier)
                self.assertEqual(identifier.group(1), file.stem)
                ids.append(identifier.group(1))
                self.assertIn("type: historical", match.group(1))
                for section in SECTIONS:
                    self.assertIn("## " + section + "\n", body)
                self.assertIn("Illustrative simulation, not an actual quotation.", body)
                self.assertIn("- ", body.split("## Source notes\n",1)[1].split("\n## ",1)[0])
                methods.append(body.split("## Reasoning method\n",1)[1].split("\n## ",1)[0].strip())
                questions.append(body.split("## Signature questions\n",1)[1].split("\n## ",1)[0].strip())
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(methods), len(set(methods)))
        self.assertEqual(len(questions), len(set(questions)))

if __name__ == "__main__":
    unittest.main()
