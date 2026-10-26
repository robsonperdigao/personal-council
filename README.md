# Personal Council

An open-source, Markdown-first framework for a personal advisory council powered by AI. Invite different perspectives to examine decisions, keep a portable record of what matters, and choose who occupies each advisory seat.

**Status: v0.1 foundation / experimental.** These are portable prompts, agent definitions, and skills, not a hosted app. Results and persistence depend on the AI tool and its filesystem access.

## Principles

- **Seats are roles; advisors are replaceable perspectives.** Users choose who advises them.
- **Local Markdown is the source of truth.** No database, paid service, Notion, or Obsidian required.
- **Privacy by default.** Personal data lives in the ignored .private/ directory or in a separate private location. Never publish it.
- **Disagreement is welcome.** No automatic consensus or fabricated quotations.
- **User autonomy.** The council advises; the person decides.
- **Transparent representations.** Historical, fictional and personal advisors are simulations of perspectives, not the real people.

## Get started

1. Clone this repository and open it in an AI coding/agent workspace that can read and write Markdown.
2. Create your private workspace from templates/private/:
   - macOS/Linux: `cp -R templates/private .private`
   - PowerShell: `Copy-Item -Recurse templates/private .private`
3. Open .private/council.md to choose seats and advisor IDs. Customize .private/profile.md and .private/memory/values.md only as much as you want.
4. Ask the agent: **"Use council-builder to set up my council"** or **"Use council-session to debate my decision about ..."**
5. Review suggested memory updates before allowing them to be written.

Start with [Getting Started](docs/GETTING_STARTED.md) and [Architecture](ARCHITECTURE.md).

## What's included

- [Constitution](constitution.md): principles and safety boundaries.
- [Secretary-General](agents/secretary-general.md): orchestration contract.
- [Advisor catalog](advisors/historical/): example historical perspectives.
- [Skills](.agents/skills/): council-builder, add-advisor, council-session, and memory-manager.
- [Private workspace templates](templates/private/): user profile, seats and Markdown memory.
- [Advisor creation guide](docs/ADDING_ADVISORS.md): add, replace or invite advisors.

## Compatibility

Skills follow the [Agent Skills specification](https://agentskills.io/specification). Codex can discover repository skills in .agents/skills/. Other environments may need an adapter, copied instructions or explicit skill invocation. This version does **not** claim independent multi-agent execution on every platform.

Obsidian can open the private Markdown folder as a vault. Notion is optional and may require manual import/export or a future adapter. Neither is a system of record.

## Sensitive data

This is a **public** repository. The .gitignore excludes .private/, my-council/ and personal-data/ but cannot protect content added with git -f or uploaded elsewhere. Keep private files outside the public repository if sharing the whole folder. Treat family stories, health details and financial decisions as sensitive. See [Memory Format](docs/MEMORY_FORMAT.md).

## Development

Run `python scripts/validate.py` to check repository conventions. The roadmap is in [docs/ROADMAP.md](docs/ROADMAP.md). Contributions and constructive dissent welcome.

MIT licensed. Advisors are interpretive tools and are not substitutes for qualified medical, legal, mental-health or financial professionals.

## Advisor personalities (M2)

The starter catalog now includes Marcus Aurelius, Peter Drucker and Daniel Kahneman, each with an explicit reasoning method, communication style, characteristic objections and **clearly simulated** examples. See [advisor design](docs/ADVISOR_DESIGN.md).

Use the **advisor-architect** Skill to draft and check a distinct personality, then **add-advisor** to place it in a seat. For behavioral testing, use [fictional evaluation scenarios](tests/scenarios.md). Profiles are Markdown, not necessarily independent running AI agents.

M2 validation: run Python with scripts/validate.py and the built-in unittest discovery in tests/.
