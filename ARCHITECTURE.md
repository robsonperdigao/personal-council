# Architecture — Personal Council v0.1

## 1. Objective

A portable, open-source, Markdown-first advisory council for decisions about work, family, relationships, identity, parenting and other domains. Users choose advisors for named seats and retain control over their own context and history. The core must work without an external service, database or required editor.

## 2. Non-goals for v0.1

No hosted application, vector database, native Obsidian plugin, Notion synchronization, persistent daemon, authentication server, automatically executed parallel LLM agents or recreation of a real person's consciousness. Platform-specific agent runtimes are optional adapters.

## 3. Components and contracts

| Component | Location | Contract |
| --- | --- | --- |
| Constitution | constitution.md | Normative rules for the entire council |
| Secretary-General | agents/secretary-general.md | Intake, retrieval, selection, debate, synthesis, follow-up |
| Advisor definition | advisors/ or private workspace advisors/ | Markdown with stable ID, type, competencies, principles, limitations and provenance |
| Seats | private workspace council.md | A named function mapped to an advisor ID; advisors can be replaced without changing seat identity |
| Skills | .agents/skills/<name>/SKILL.md | Procedures, triggered by task intent, without requiring a specific model |
| User context | private workspace profile.md and memory/*.md | Minimal, source-labeled, user-editable context |
| Decisions | private workspace decisions/*.md | Append-oriented records with IDs, context, rationale, status and links |
| Interfaces | any filesystem-capable agent/editor | Markdown is authoritative; Obsidian/Notion are optional views/integrations |

Agent Skills metadata follows https://agentskills.io/specification. The neutral Markdown advisor format is **our framework contract**, not an automatic native subagent format. Optional adapters can translate to runtime-specific formats.

## 4. Data location and privacy

The distribution repo contains reusable code, definitions and **fictional sample data only**. A user's working data defaults to .private/ (gitignored); an entirely separate private folder/repository is safer for long-term use. No public artifact may require or bundle personal content.

The directory named by the workspace root must be explicitly configured/discovered in each session. No automatic access to unrelated conversations or applications is assumed.

Suggested private tree:

~~~text
.private/
  profile.md
  council.md
  memory/
    index.md
    values.md
    family.md             # add as needed
    business.md           # add as needed
  advisors/
    personal-advisor.md  # optional, user authored
  decisions/
    2026-10-26-example.md
~~~

## 5. Advisor and seat contract

A seat has a stable slug, title, mandate, optional domains and an assigned advisor ID. An advisor is an independently selectable interpretation with a stable ID and type:

- historical: documented writings/biographical positions with citations or source notes; no invented quotations.
- fictional: clearly labeled as a character-inspired interpretation, not canonical fact.
- personal: constructed from user-provided memories/teachings; verified memories separated from inference; never impersonate a deceased person.
- original: transparent synthetic lens designed by the user.

A guest advisor may attend one session without changing seat configuration. Advisor replacement does not rewrite decision history: a past decision records participating advisor IDs as of the meeting.

## 6. Session flow

1. **Intake:** determine domain, the user's question, relevant constraints and whether they want a solo consult, thematic meeting or full council.
2. **Retrieve:** read only locally accessible and authorized profile, memory index, topic files and related decision records. Say when context is missing.
3. **Select:** use the user's assigned seats; invoke at most the perspectives relevant to the question; allow guest advisors.
4. **Deliberate:** independently state assumptions and each advisor's reasoning; compare strongest arguments and meaningful disagreements. If there are no real isolated subagents, label these as *simulated perspectives*.
5. **Synthesize:** present options, trade-offs, uncertainties, recommendation if justified, and what might change it.
6. **Record:** propose a brief summary/decision memory with source and related links, obtain user approval, then write. Do not presume agreement or completion.

## 7. Markdown memory protocol

Markdown files with small YAML frontmatter and portable relative links. No proprietary Obsidian wikilinks required.

- profile.md: stable information explicitly supplied by the user.
- memory/index.md: manually maintained pointers to domain memories and key records. Read first for relevant topics.
- memory/<domain>.md: curated facts/values/priorities for that domain, with dates and provenance.
- decisions/<date>-<slug>.md: dated record containing initial options, participants, outcome and a later review.

Cross-domain linking uses ordinary relative Markdown links, not automatic data leakage. Before surfacing sensitive information from another domain, consider whether it's necessary and request permission if disclosure could surprise the user. Prefer a neutral observation without reproducing the sensitive detail.

Provenance categories: **user-stated**, **documented-source**, **inference** (needs confirmation), **hypothetical**. Only user-stated/documented claims can be treated as facts; unconfirmed hypotheses are not stored as facts. See [docs/MEMORY_FORMAT.md](docs/MEMORY_FORMAT.md).

## 8. Memory updates and conflicts

Reads are always non-destructive. Writes require a proposed diff/summary and explicit approval. Avoid overwriting a decision silently; use an addendum or record a status revision. On conflicts, show both claims with dates and sources and ask the user to reconcile rather than choosing the newest automatically. Never fabricate dates, citations or quotes.

Markdown files are the only authoritative store in v0.1. External sync is optional and must define conflict resolution before writes. Git history is useful but not a replacement for backups or access controls.

## 9. Safety and representation

Advisor personas are analytical lenses. They do not have private knowledge or personal feelings. Special caution applies to personalized perspectives inspired by deceased loved ones: prefer teachings/values mode by default; simulated conversational style is optional, clearly signposted and never presented as genuine contact.

High-stakes medical, legal, safety or financial questions require factual grounding and, when relevant, qualified professional support. A council cannot manufacture expertise through character role-play.

## 10. Compatibility and limitations

The initial harness is file-based: a filesystem-capable agent reads AGENTS.md and relevant skills and accesses a configured Markdown workspace. Obsidian opens the folder directly; Notion can be a separate manual or future synchronized interface, not a required dependency.

An AI interface without writable file access can still run advisory prompts but **cannot** promise persistent memory. An AI interface without parallel agents can still provide structured perspectives; it must not claim independent model execution.

## 11. Evolution and exit criteria

M1: architecture, privacy defaults, templates, Secretary-General, representative advisors and foundational skills.
M2: seat management and advisor creation validation.
M3: robust retrieval, cross-domain reviews, reproducible decision audits.
M4: adapters, usability tests and opt-in integrations.

Success means a new user can clone, initialize a private council, swap an advisor, deliberate, and save/review a decision with only Markdown and a capable AI agent.

## 12. Advisor personality contract (M2)

A public advisor is a single Markdown profile under advisors/historical/ (with future fictional and original catalogs). It contains: mandate; source-backed principles; personality and communication; an ordered reasoning method; signature questions; dissent and blind spots; source notes; illustrative examples; limits. See [advisor design](docs/ADVISOR_DESIGN.md).

Advisor-architect prepares a distinct profile and add-advisor proposes its assignment to a seat. Existing user-selected seats and historical decision records are never silently rewritten.

Each selected advisor receives the SAME confirmed facts. Difference in catchphrases does not count as a distinct intellectual contribution. Contrast methods and disagreements; preserve uncertainty.

Historical advisors are interpretive simulations, not literal people. Personal/deceased loved-one profiles remain private and prioritize actual teachings over imitation. One model simulating three roles must not be described as three independently executed agents.

Static schema tests confirm file structure only; manual cases evaluate actual advisory usefulness. No knowledge database, vendor dependency or model fine-tuning is needed.
