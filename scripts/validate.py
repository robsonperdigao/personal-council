#!/usr/bin/env python3
"""Dependency-free Markdown contracts: repository, skills, public advisor profiles."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
CATALOG = ROOT / "advisors" / "historical"
REQUIRED = [
    "README.md", "AGENTS.md", "ARCHITECTURE.md", "constitution.md",
    "agents/secretary-general.md", "templates/private/council.md",
    "templates/private/profile.md", "templates/private/memory/index.md",
    "templates/decision-record.md", "docs/ADVISOR_DESIGN.md", "tests/scenarios.md",
]
SECTIONS = [
    "Mandate", "Core principles", "Personality and communication",
    "Reasoning method", "Signature questions", "Dissent and blind spots",
    "Source notes", "Response examples", "Limits",
]
errors = []
for path in REQUIRED:
    if not (ROOT / path).is_file():
        errors.append("Missing " + path)

skills = sorted(SKILLS.glob("*/SKILL.md"))
if not skills:
    errors.append("No skills found")
for path in skills:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        errors.append("Bad skill frontmatter " + str(path))
        continue
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", match.group(1), re.M)
    description = re.search(r"^description:\s*(\S.+)$", match.group(1), re.M)
    if not name or name.group(1) != path.parent.name or len(name.group(1)) > 64:
        errors.append("Bad skill name " + str(path))
    if not description or len(description.group(1)) > 1024:
        errors.append("Bad skill description " + str(path))

advisors = sorted(CATALOG.glob("*.md"))
if len(advisors) < 3:
    errors.append("Expected at least three public sample advisors")
ids = set()
for path in advisors:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("Bad advisor frontmatter " + str(path))
        continue
    ident = re.search(r"^id:\s*([a-z0-9-]+)\s*$", match.group(1), re.M)
    if not ident or ident.group(1) != path.stem or path.stem in ids:
        errors.append("Bad or duplicate advisor ID " + str(path))
    ids.add(path.stem)
    if "type: historical" not in match.group(1):
        errors.append("Public historical advisor has wrong type " + str(path))
    for section in SECTIONS:
        if "## " + section + "\n" not in text:
            errors.append(f"Missing {section} in {path}")
if (ROOT / ".private").exists():
    print("INFO: private workspace exists; do not add it to Git history")
if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)
print(f"PASS: {len(skills)} skills and {len(advisors)} public advisor profiles")
