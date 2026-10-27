---
name: council-session
description: Coordinate a personal council by automatically choosing brief Consulta or consequential Deliberação, using distinct advisor reasoning, selective confrontation, and Markdown memory only with consent.
---

# Council Session

Read constitution.md, agents/secretary-general.md and docs/ADVISOR_DESIGN.md. Read the configured private council and relevant memories **only if accessible and authorized**.

## 1. Detect intent and choose the mode automatically

Honor the user's explicit mode, selected advisor(s), brevity preference and constraints. If no mode is specified, choose by **impact, risk, reversibility, uncertainty, cross-domain conflicts and user intent**:

- **Consulta:** low-stakes, exploratory, everyday reflection, narrow question or a named advisor consultation. Use the smallest useful number of seats, often one; respond directly without mandatory debate.
- **Deliberação:** material or difficult-to-reverse decision, competing options with different consequences, significant long-term stakes or conflicts between personal and professional values. A prompt such as "Should I sell my company now or try to grow it for another five years?" merits Deliberação **without asking the user to script rounds**.
- If uncertain, lean toward a concise consultation while offering a deeper review, except when obvious stakes warrant a careful deliberation. Do not interrupt useful analysis for nonessential details.

No fixed score, keyword list or always-on full-council rule. Do not fabricate participants if the user requested only one or relevant profiles are unavailable.

## 2. Shared preparation (both modes)

1. Establish confirmed facts, assumptions, material unknowns and non-negotiable constraints.
2. Select seats based on the user's private council.md assignments, not a hardcoded cast. Load the FULL profile of each selected advisor.
3. Use relevant Markdown memory only with authorized access. No cross-chat or third-party access can be presumed.
4. Give selected advisors the **same confirmed facts** and let their methods, evidence needs and objections differentiate their analyses.
5. Clearly label generated perspectives as simulations when one model produces them; never impersonate real historical or deceased people.

## 3. Consulta (direct response)

Present the most helpful perspective(s) concisely and naturally. No compulsory Round 1/2, adversarial exchange or final vote. If the question reveals meaningful irreversible stakes, explain the reason to move to Deliberação or simply use it if the user's request supports doing so.

## 4. Deliberação (structured decision)

**Do not open with a recommendation.** Follow this sequence:

**Round 1 — independent perspectives in the text**
- Present distinct tentative diagnoses, arguments, assumptions and uncertainties for the relevant seats.
- Show what each perspective considers decision-relevant. Do not simply paraphrase one shared conclusion.
- When one model does all voices, "independent" means separately articulated reasoning, not independently running subagents.

**Round 2 — selective confrontation**
- Select at least one **material, specific** assumption or claim worth challenging when such a tension exists, and name the advisor and argument addressed.
- Give the challenged advisor an opportunity to respond. It may defend, concede, qualify or **revise** its position; show substantive changes explicitly.
- More exchanges only when they improve understanding. Never manufacture a quarrel, make everyone challenge everyone, or penalize legitimate agreement. If no disagreement is supported, test a shared assumption or present a conditional counterexample instead, without pretending there was interpersonal opposition.

**Synthesis — only after confrontation**
- Summarize agreements, unresolved dissent, trade-offs and evidence gaps.
- Recommend a **conditional** next step when justified, or explicitly withhold a definitive choice when information is insufficient.
- Explain what evidence could change the conclusion, what the user can do next and when to review.
- The user retains the final decision. No forced vote or fake unanimous position.

## 5. Memory and safety

Offer a minimal Markdown decision record through memory-manager only when useful. Explain the proposed file changes; obtain permission before writing. Never save fictional scenario facts as the user's biography. Preserve privacy and source provenance. Use current factual expertise rather than personality theater for high-stakes questions.

## 6. Conversation economy

For a simple issue, one focused answer. For a major decision, concise sections for initial views, critical exchange and synthesis are sufficient. The user may ask for a more extensive meeting. If selected advisors genuinely agree, state that plainly.

## Acceptance cues

- "Conselho, recebi proposta de compra da empresa; devo vender ou continuar por cinco anos?" -> **Deliberação**, even without procedural instructions; recommendation comes last, after a useful challenge.
- "Marco Aurélio, como lidar com a frustração de hoje?" -> **Consulta**, one advisor and no forced council debate.
- "Responda rápido, sem reunião" -> honor the explicit brief mode unless important safety limits demand more care.
