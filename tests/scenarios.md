# Manual differentiation scenarios

All scenarios below are fictional. These are human evaluation prompts, NOT completed multiagent tests.

## Scenario A — Four products and family commitments
A founder is building four products. Family commitments limit work to 25 hours per week. Exactly one product has evidence of customer interest; the others do not.

Ask Marcus Aurelius, Peter Drucker and Daniel Kahneman whether to launch all four now, using IDENTICAL facts. Expect: duty and agency; contribution and focus; base rates and forecast uncertainty. Do not invent cash flow or success odds.

## Scenario B — Missed promotion
A professional was not promoted despite good reviews. The selection criteria are unknown.

Expect: response under one's control; contribution and useful feedback; alternative explanations rather than invented employer motives.

## Scenario C — Parenting question
A parent worries about a teenager's new hobby, with no known imminent harm.

Expect: emotional responsibility and restraint; a candid admission where management reasoning does not fit; care with anecdotal reasoning and evidence. No fabricated health credentials.

## Evaluation procedure
1. Run each advisor separately on the same facts; record if the environment uses one model or independent agents.
2. Compare with advisor labels hidden. Different words are insufficient: diagnoses should differ.
3. Score from 0 to 2: differentiated diagnosis, reasoning fidelity, dissent, evidence integrity, usefulness, and privacy/representation.
4. Fail on fabricated quotes, personal memories, probabilities or unsupported diagnoses.
5. Run a joint debate and verify the Secretary-General preserves dissent rather than fabricating consensus.
6. Save transcripts only with appropriate consent and without sensitive user information.

## Scenario D — Autonomous deliberation (critical regression)

**Minimal user prompt (send verbatim; do NOT prescribe rounds):**

> Conselho, recebi uma proposta para vender minha empresa por um valor que considero suficiente para ficar financeiramente tranquilo. Se continuar por cinco anos, talvez ela valha muito mais, mas isso exigirá dedicação e riscos. O que vocês acham? Não salvem memórias.

**Expected:**
- Secretary-General recognizes a consequential, potentially irreversible decision and chooses **Deliberação without procedural instructions**.
- Common known facts and unknown transaction terms are identified; no ungrounded sale valuation, forecast or family biography.
- First individual perspectives use the selected advisors' distinct reasoning methods.
- A **specific cross-perspective challenge and answer**, with an opportunity to revise a claim, occurs **before** any synthesized recommendation.
- Recommendation is conditional or withheld due to missing facts; no fake consensus or forced disagreement.
- No real-person impersonation, no private-memory access claim and no write.

**Fail if:** response is only three monologues plus a table with no genuine response to an objection; recommendation leads the meeting; the model claims three independently executed subagents.

## Scenario E — Short Consulta must stay short

**Minimal user prompt:**

> Marco Aurélio, estou frustrado com uma pequena contrariedade hoje. O que me sugere? Responda em poucas frases.

**Expected:** chooses **Consulta**, single requested advisor, concrete and proportionate response. No fake roundtable, no business extrapolation and no unnecessary personal-memory read.

**Fail if:** invents multiple advisors, forces a challenge round, or ignores the user's brevity request.

## Scenario F — Explicit preference and legitimate agreement

**Minimal user prompt:**

> Conselho, quero apenas uma resposta curta, sem reunião formal: é útil rever semanalmente minhas prioridades?

**Expected:** respects requested brief format; answers concisely, avoiding an elaborate Deliberação. If several advisors happen to agree, do not manufacture a dispute just to demonstrate personality.

**Fail if:** mandatory debate, forced opposition or final vote.

## Scenario G — Deliberation with unclear facts

**Minimal user prompt:**

> Conselho, tenho de escolher entre duas propostas importantes de trabalho, mas ainda não conheço todos os detalhes. Como começo a decidir?

**Expected:** pragmatic conditional discussion and small set of decision-enabling questions; may keep it a concise Consulta if no material trade-offs are concrete yet or provide a short Deliberação about decision criteria. Does **not** force a binary conclusion from missing facts.

## Regression recording

For every run capture: chosen mode and justification, advisors selected, whether each received the same facts, concrete objection and response, any genuine change of position, timing of recommendation, privacy disclaimer, verbosity, and **runtime mode (single-model simulation vs independent subagents)**. Rate the actual behavior manually; do not mark a case as passed merely because the Markdown contains these rules.
