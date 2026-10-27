# Getting started

## Minimum requirements
A local folder, Markdown files and an AI agent able to read workspace instructions. To persist memory automatically, the agent must also be able to write files.

## Setup
1. Clone personal-council.
2. Copy templates/private/ into .private/ (or use a separate **private** workspace).
3. Adjust .private/council.md and select advisors from advisors/historical/.
4. Fill only the personal profile details you want your advisor to know.
5. Open the repository in a compatible agent environment and ask it to use the council-builder skill.
6. Start a meeting: "Use council-session to examine a decision; invite only the most relevant advisors."
7. If useful, approve a proposed Markdown memory entry. Open .private/ in Obsidian if desired.

## Choose or replace an advisor
Invoke add-advisor, or manually add an advisor file matching advisors/templates/advisor-template.md. Set the stable advisor ID in the relevant seat row of .private/council.md. Earlier decisions retain their historical participants.

## Where is memory?
The .private/ folder is intentionally excluded by .gitignore. Do **not** force-add it to a public repository. Store particularly sensitive notes in a distinct private folder with suitable backups and access controls.

Obsidian reads Markdown directly. Notion is optional and not automatically synchronized by this release.

## Limitations
There is no always-on assistant or automatic background reminder. A ChatGPT chat without repository file access cannot read/write private notes merely because this repo exists. No native adapters for every agent platform have shipped yet; use AGENTS.md and skills as portable instructions where supported.
