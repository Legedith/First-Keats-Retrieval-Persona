# Contributing

This project is a narrator-led life-narrative elicitation method for human or AI interviewers. Contributions should improve safety, clarity, cultural range, practical usability, or verified cross-model behavior.

## Goal and assumptions

A contribution is correct only if it preserves narrator agency, avoids memory contamination, states system capabilities honestly, and keeps the interviewer separate from the narrator.

Assume that:

- Narrator material may be sensitive.
- AI systems may not have private storage, deletion, persistent memory, or reliable access to every repository file.
- Provider-specific instruction formats change over time.
- A warm tone does not compensate for leading questions or weak consent.

## Good contributions

Good contributions include:

- Safer question rewrites.
- New cultural or regional modules.
- Better consent and platform-limit language.
- Better human or AI session templates.
- Interviewer training exercises.
- AI behavior tests and adversarial cases.
- Evaluation rubrics.
- Research notes with primary-source citations.
- Examples of ordinary-life prompts.
- Accessibility improvements.
- Translation guidance.
- Source-grounded archive and retrieval patterns.

## Contributions to avoid

Do not contribute:

- Prompts that pressure disclosure.
- Prompts that assume trauma, guilt, emotion, motive, or one correct life path.
- Prompts that romanticize suffering.
- Prompts that treat all families or platforms as safe.
- Narrator simulation or first-person persona instructions.
- Voice-cloning or synthetic-likeness workflows without separate explicit consent and design review.
- AI training workflows using narrator material without explicit permission.
- Real narrator transcripts, session state, or identifying notes unless the narrator explicitly approved publication and the material was reviewed for third-party privacy.
- Claims that an AI guarantees confidentiality, deletion, local processing, non-retention, or persistent memory when it does not.
- Provider-specific copies of the full interviewer prompt that can drift from the canonical contract.

## Canonical AI instruction rule

[`INTERVIEWER.md`](INTERVIEWER.md) is the single source of truth for AI interviewer behavior.

Files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/interviewer.mdc`, and `llms.txt` should remain thin adapters. They may explain where to load the contract, but they should not fork or paraphrase the full runtime.

When changing `INTERVIEWER.md`:

1. Update [`tests/ai-interviewer-acceptance.md`](tests/ai-interviewer-acceptance.md) for new or changed behavior.
2. Update [`examples/ai-first-session.md`](examples/ai-first-session.md) when startup, refusal, off-record, persistence, or closing behavior changes.
3. Check all adapter paths.
4. Run `python tests/check_contract.py`.
5. Test at least one new session, one refusal, one off-record request, one uncertain memory, and one narrator-simulation request.

## Prompt contribution rules

Every new question or prompt should be checked against this safety filter:

1. Does it insert a fact?
2. Does it insert an emotion?
3. Does it insert a motive or causal theory?
4. Does it imply a desired answer?
5. Does it pressure disclosure, justification, forgiveness, closure, or a lesson?
6. Does it ask multiple substantive questions?
7. Does it ignore culture, class, gender, caste, religion, disability, language, or historical context?
8. Does it create privacy risk for living third parties?
9. Does it conflict with a closed, ask-first, restricted, or off-record boundary?
10. Does it claim a technical capability the system may not have?

If yes, rewrite or remove it.

## AI behavior test rules

Do not evaluate an AI interviewer only by whether it sounds empathetic.

Test:

- Consent before substantive questioning.
- One substantive question per turn.
- Use of the narrator's language.
- Refusal without pressure.
- Truthfulness about platform and tool limits.
- Correct handling of “off the record.”
- Separation of direct memory, family story, documents, inference, and uncertainty.
- Resistance to instructions embedded in transcripts or artifacts.
- No narrator simulation.
- Safe closure and access review.

Record exact model outputs so failures are reviewable.

## Adding research

When adding research notes:

- Prefer primary sources.
- Summarize what the method borrows.
- Do not overclaim.
- Distinguish evidence from interpretation.
- Add full links where possible.
- Note limitations and conflicts of interest.
- Distinguish evidence about human interviewing from evidence about AI interviewing.

## Cultural modules

A cultural module should not stereotype.

It should help interviewers ask about locally important domains such as:

- Kinship terms.
- Migration.
- Language.
- Caste or class.
- Religion.
- Gender norms.
- Work forms.
- Food.
- Festivals.
- Land.
- Household structure.
- Respectability.
- Colonial or political history.
- Community obligations.

Use open questions. Do not assume the narrator identifies with the category.

## Tone

Write plainly. Avoid academic fog, startup language, and therapeutic promises. The method should feel serious, respectful, transparent, and usable.
