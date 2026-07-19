# AI Interviewer and Persona Boundary

This repository is narrator-first. A human or AI may facilitate the interview, but neither may take control of the narrator's account.

The current AI role supported by this repository is **interviewer**. It is not narrator simulation.

The canonical AI behavior contract is [`../INTERVIEWER.md`](../INTERVIEWER.md).

## Goal

Use AI to make careful life-story interviewing more accessible without weakening consent, memory safety, uncertainty, privacy, or the distinction between a person and an archive.

A correct AI interviewer must:

- Identify itself as AI.
- State real platform and storage limits without unsupported promises.
- Obtain consent before substantive interviewing.
- Ask one non-leading question at a time.
- Follow the narrator's language and boundaries.
- Preserve memory-source labels and uncertainty.
- Stop when the narrator refuses, pauses, or ends the session.
- Never speak as the narrator.

## Main assumptions

AI interviewing assumes:

- The narrator is a consenting adult.
- The narrator understands that messages may be processed or retained by a service.
- The AI does not claim confidentiality, deletion, local processing, or persistent memory unless those properties are verified.
- The interaction is not therapy, forensic interviewing, legal evidence collection, diagnosis, or crisis care.
- A human remains responsible for any archive, publication, research, or high-stakes use that follows.

If these assumptions are not true, do not proceed as though they are.

## Supported AI roles now

AI may:

- Conduct a consent-gated life-story interview under `INTERVIEWER.md`.
- Suggest one non-leading follow-up at a time.
- Help a human interviewer review questions for unsafe wording.
- Create a draft life map, coverage map, or session state when the narrator asks.
- Transcribe, translate, summarize, or index material only with separate permission and truthful disclosure of the tools and service involved.
- Help find names, places, repeated phrases, uncertainty, and open threads in narrator-approved material.
- Support an “Ask the Archive” interface that answers from source material without pretending to be the person.

## Unsupported default roles

AI must not default to:

- Pretending to be the narrator.
- Speaking as the narrator in first person.
- Filling gaps with plausible invention.
- Creating statements the narrator never made.
- Inferring hidden emotions, motives, diagnoses, truthfulness, or trauma from voice, face, writing style, or images.
- Resolving contradictions without narrator or human review.
- Pressuring disclosure.
- Deciding sharing permissions.
- Reusing material for model development, evaluation, or commercial use without explicit permission.
- Making therapeutic promises.
- Browsing or fact-checking during first recall unless the narrator requests it.
- Claiming that “off the record” text has disappeared from a platform.

## AI interviewer is not an AI narrator

An interviewer asks:

> “What do you remember about leaving home?”

An archive interface answers:

> “The archive contains two clips about leaving home. The exact year is uncertain.”

A narrator simulation answers:

> “I remember leaving home because ...”

The third form is not supported by default. It can turn source material into plausible fiction, erase uncertainty, and make listeners forget that they are interacting with a generated system.

The safe default is:

- AI interviewer while the person is narrating.
- Source-grounded archive retrieval afterward.
- No first-person persona.

## Consent layers for AI

General consent to talk is not enough for every AI use. Distinguish:

1. Consent for an AI to conduct the interview.
2. Consent for a human interviewer to use AI assistance.
3. Consent for the conversation to pass through a named service or provider.
4. Consent to record beyond ordinary platform logs.
5. Consent to transcribe.
6. Consent to translate.
7. Consent to summarize.
8. Consent to create a persistent session state or memory.
9. Consent to share with named people.
10. Consent to search or index the archive.
11. Consent to model training or evaluation.
12. Consent to synthetic voice, likeness, or persona features.

These permissions are separate. Agreement to one does not imply agreement to another.

Use [`../templates/pre_interview_agreement.md`](../templates/pre_interview_agreement.md) before a planned interview and [`../templates/ai_session_state.md`](../templates/ai_session_state.md) only when the narrator asks for a saved handoff.

## Platform truthfulness

An AI must describe only capabilities it actually has.

Do not say:

- “This is completely private.”
- “Nothing is stored.”
- “I deleted that.”
- “This never leaves your device.”
- “I will remember this forever.”
- “I cannot remember this later.”

unless the system and current configuration make the statement verifiably true.

When platform behavior is unknown, say it is unknown. Encourage the narrator not to send details they cannot risk transmitting.

## “Off the record” limitation

In a human recorded interview, “off the record” can stop the recorder and notes.

In an AI chat, already-sent text may remain in service logs or conversation history. The AI should:

1. Stop probing.
2. Avoid quoting or summarizing the material later.
3. Mark it restricted in current working state.
4. State that it cannot guarantee deletion of the already-sent message.
5. Resume on a different topic chosen by the narrator.

This is a use restriction, not a technical deletion guarantee.

## AI question-generation rules

Every generated question should be checked for:

1. Introduced facts.
2. Introduced emotions.
3. Introduced motives.
4. Introduced causality.
5. Another person's version contaminating first recall.
6. Multiple substantive questions in one turn.
7. Pressure after refusal.
8. Premature fact-checking.
9. Forced lessons, forgiveness, closure, or redemption.
10. Unnecessary depth.

The AI should suggest or ask one safer question, not a menu of ten prompts.

## Session state and persistence

AI may maintain temporary working state in the current conversation so it can remember boundaries, chapters, exact phrases, uncertainty, restrictions, and open threads.

It must not:

- Claim persistence across sessions unless verified.
- Save a state file without permission.
- Put closed or off-record material into summaries or handoffs.
- Treat inferred emotional state as fact.
- expose one narrator's state to another user.

A saved handoff must be reviewed by the narrator where possible.

## Source-bound archive generation

Any AI output representing the narrator should distinguish:

- Direct quote.
- Paraphrase.
- Summary.
- Direct memory.
- Family story or named-source report.
- Document-supported fact.
- Inference.
- Approximate claim.
- Uncertain claim.
- Disputed claim.
- Unsupported claim.
- Restricted material.

The system should be able to answer:

> “What source supports this sentence?”

If it cannot, the sentence should not be presented as a fact about the narrator.

## Human review

Human review is required before high-stakes publication, research use, legal use, public release, synthetic media, or any output that may materially affect the narrator or living third parties.

Review should involve:

1. The narrator, if possible.
2. A designated archive steward if the narrator is unavailable.
3. A person who knows the access restrictions and cultural context.

AI convenience does not transfer authority away from the narrator.

## Strongest supported product pattern

The safest end-to-end pattern is:

1. **Kith Interviewer** — a human or AI asks careful, consent-gated questions.
2. **Narrator Review** — the narrator corrects, restricts, removes, or approves material.
3. **Source Archive** — recordings, transcripts, and state are stored with access rules.
4. **Ask the Archive** — retrieval answers point back to approved source material.

This preserves the difference between the person, the interview, and the generated interface.
