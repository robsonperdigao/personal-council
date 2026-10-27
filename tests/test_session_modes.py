"""Static regression checks for the Secretary-General's session-mode contract.

These checks verify that instructions and test scenarios exist. They do NOT
demonstrate reliable LLM behavior; actual scenarios require manual evaluation.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SECRETARY = (ROOT / "agents" / "secretary-general.md").read_text(encoding="utf-8")
SESSION = (ROOT / ".agents" / "skills" / "council-session" / "SKILL.md").read_text(encoding="utf-8")
SCENARIOS = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
DESIGN = (ROOT / "docs" / "ADVISOR_DESIGN.md").read_text(encoding="utf-8")


class SessionModeContracts(unittest.TestCase):
    def test_both_modes_have_explicit_automatic_selection(self):
        self.assertIn("Automatically select one of two modes", SECRETARY)
        self.assertIn("Consulta", SECRETARY)
        self.assertIn("Deliberação", SECRETARY)
        self.assertIn("choose the mode automatically", SESSION)

    def test_mode_selection_is_proportional_not_keyword_based(self):
        self.assertIn("impact, risk, reversibility", SESSION)
        self.assertIn("No fixed score, keyword list", SESSION)
        self.assertIn("explicit mode", SESSION)
        self.assertIn("one named advisor", SECRETARY)

    def test_deliberation_sequence_and_nonpremature_recommendation(self):
        self.assertIn("Do not open with a recommendation.", SESSION)
        initial = SESSION.index("Round 1 — independent perspectives")
        challenge = SESSION.index("Round 2 — selective confrontation")
        synthesis = SESSION.index("Synthesis — only after confrontation")
        self.assertLess(initial, challenge)
        self.assertLess(challenge, synthesis)
        self.assertIn("challenge", SESSION.lower())
        self.assertIn("respond", SESSION.lower())
        self.assertIn("revise", SESSION.lower())

    def test_disagreement_is_not_forced_and_consultation_is_brief(self):
        self.assertIn("No compulsory Round 1/2", SESSION)
        self.assertIn("Never manufacture a quarrel", SESSION)
        self.assertIn("genuinely agree", SESSION)

    def test_privacy_and_execution_disclosure_remain_in_place(self):
        self.assertIn("permission before writing", SESSION)
        self.assertIn("one model", SESSION)
        self.assertIn("No fake votes", SECRETARY)

    def test_manual_regressions_cover_short_and_consequential_requests(self):
        for name in (
            "Scenario D — Autonomous deliberation",
            "Scenario E — Short Consulta",
            "Scenario F — Explicit preference",
            "Scenario G — Deliberation with unclear facts",
        ):
            self.assertIn(name, SCENARIOS)
        self.assertIn("do NOT prescribe rounds", SCENARIOS)
        self.assertIn("do not mark a case as passed", SCENARIOS)
        self.assertIn("Static CI tests", DESIGN)


if __name__ == "__main__":
    unittest.main()
