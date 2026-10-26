#!/usr/bin/env python3
"""Minimal dependency-free repository conventions check."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
REQUIRED = [
    "README.md", "AGENTS.md", "ARCHITECTURE.md", "constitution.md",
    "agents/secretary-general.md", "templates/private/council.md",
    "templates/private/profile.md", "templates/private/memory/index.md",
    "templates/decision-record.md",
]
ERRORS = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        ERRORS.append(f"Missing {rel}")

for skill in sorted(SKILLS.glob("*/SKILL.md")):
    data = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", data, re.S)
    if not match:
        ERRORS.append(f"Invalid YAML frontmatter delimiter: {skill.relative_to(ROOT)}")
        continue
    header = match.group(1)
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", header, re.M)
    description = re.search(r"^description:\s*(\S.+)$", header, re.M)
    if not name or name.group(1) != skill.parent.name:
        ERRORS.append(f"Name must equal directory name: {skill.relative_to(ROOT)}")
    if not description or len(description.group(1)) > 1024:
        ERRORS.append(f"Missing or oversized description: {skill.relative_to(ROOT)}")
    if name and (len(name.group(1)) > 64 or "--" in name.group(1)):
        ERRORS.append(f"Invalid skill name: {skill.relative_to(ROOT)}")
if not list(SKILLS.glob("*/SKILL.md")):
    ERRORS.append("No skills found")

if (ROOT / ".private").exists():
    print("INFO: .private exists; ensure it is not tracked or shared.")

if ERRORS:
    print("\n".join(f"FAIL: {problem}" for problem in ERRORS))
    sys.exit(1)
print("PASS: core documentation and skill metadata checks")
