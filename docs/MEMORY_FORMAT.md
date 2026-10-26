# Markdown memory format (v0.1)

## Files
- profile.md: approved stable profile and priorities.
- council.md: seats, assigned advisor IDs and boundaries.
- memory/index.md: a small human-editable retrieval index.
- memory/<domain>.md: important facts, values and open questions by domain.
- advisors/*.md: user-specific advisors (private).
- decisions/YYYY-MM-DD-topic.md: one decision with later dated follow-ups.

## Format rules
Use UTF-8 Markdown, optional plain YAML frontmatter, ISO dates and relative Markdown links. Markdown remains readable without Obsidian, Notion or a database.

Example decision metadata:

~~~yaml
---
id: 2026-10-26-example-decision
date: 2026-10-26
domain: work
status: proposed
advisors: [peter-drucker, marcus-aurelius]
related: []
source: user-stated
---
~~~

The date and values above are **demonstration data**, not information about the repository owner.

## Provenance
- user-stated: the user explicitly said or confirmed this.
- documented-source: referenced writing or other identifiable source.
- inference: agent hypothesis, must be labeled and confirmed before being stored as fact.
- hypothetical: an intentionally imagined scenario, not a memory of reality.

## Write protocol
Show filename, a short proposed patch and provenance. Wait for explicit approval. If the user corrects a memory, preserve the correction date and reason without keeping unnecessary sensitive earlier details. Link a decision to another domain only if pertinent and within allowed privacy boundaries.

## Retrieval
Start at index.md; read only relevant linked files. Without filesystem access, state that older memories cannot be verified. For large archives, add short summaries to the index; no vector database required.

## Safety
Private data should not enter GitHub PRs, issues, public logs, public test fixtures or any cloud editor without informed consent. Ignore rules are a guardrail, not encryption.
