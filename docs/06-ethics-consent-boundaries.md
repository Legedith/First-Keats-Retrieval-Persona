# Ethics, Consent, and Boundaries

## Core rule

The narrator's control is not a courtesy. It is the foundation of the method.

Do not record first and ask permission later. Do not begin an AI interview without disclosing that the interviewer is AI and stating the platform limits you actually know.

## Goal and assumptions

The goal is informed, ongoing, specific consent.

This assumes:

- The narrator is a consenting adult.
- The narrator can understand and change the permissions being discussed.
- The interviewer states its identity and capabilities truthfully.
- A human custodian is available for any high-stakes archive, publication, research, or legal use.

If capacity, coercion, safety, or legal authority is uncertain, use a more specialized process.

## Consent is ongoing and layered

Consent may be needed separately for:

1. Having the conversation.
2. A human interviewer, AI interviewer, or AI-assisted interviewer.
3. Processing by a named platform or provider.
4. Recording beyond ordinary platform logs or chat history.
5. Transcription.
6. Translation.
7. Summarization.
8. Creating persistent AI session state or memory.
9. Storage.
10. Sharing with specific people.
11. Publication or donation.
12. Search indexing or an “Ask the Archive” interface.
13. Research or product evaluation.
14. Model training or fine-tuning.
15. Commercial reuse.
16. Use after death or incapacity.
17. Synthetic voice, likeness, or first-person persona.

These are not the same thing.

A person may agree to an AI interview but not a saved summary. They may agree to family sharing but not public release. They may agree to transcription but not model training. They may agree today and change their mind later, subject to real technical and legal deletion limits.

## Pre-interview agreement

Before recording or substantive AI interviewing, cover:

> “What are we trying to preserve?”  
> “Who or what will conduct the interview?”  
> “Who may listen or read?”  
> “Who may not?”  
> “Are there topics we should avoid?”  
> “Are there topics where I should ask before continuing?”  
> “Can you pause or stop at any time?”  
> “Can you later restrict, seal, correct, or request removal of material?”  
> “What are the actual platform, storage, and deletion limits?”  
> “What should happen to this material after death or incapacity?”

Use [`../templates/pre_interview_agreement.md`](../templates/pre_interview_agreement.md).

## Topic boundaries

Classify topics into four groups.

### Open

The narrator is comfortable discussing the topic.

### Ask first

The interviewer must pause and ask permission before entering or deepening the topic.

Example:

> “Would it be okay to ask about your marriage, or should we leave that for another time?”

### Closed

Do not ask. Do not return in a reworded form.

### Unknown

Treat as sensitive until clarified.

## Human off-record rule

In a human-recorded session, if the narrator says “off the record”:

- Stop recording.
- Do not keep a hidden transcript.
- Do not write detailed notes unless the narrator agrees.
- Do not later summarize the off-record material.
- Resume only when the narrator agrees.

A true off-record boundary changes the record itself.

## AI-chat off-record limitation

An AI chat may not be able to remove text that has already been sent to the service.

If the narrator says “off the record,” the AI should:

1. Stop probing.
2. Avoid quoting, summarizing, or reusing the material later.
3. Mark it restricted in current working state.
4. State briefly that the service may retain already-sent text and the AI cannot guarantee deletion.
5. Resume on a different topic chosen by the narrator.

Do not promise that the message disappeared. Encourage narrators not to transmit details they cannot risk sending to the service.

## Platform truthfulness

Do not claim:

- Complete confidentiality.
- No storage.
- Local-only processing.
- Successful deletion.
- No human review.
- No model training.
- Persistent memory.
- No persistent memory.

unless the statement is verified for the actual system and configuration.

When behavior is unknown, say it is unknown. Provide the relevant settings or policy only when known and current.

## Sharing levels

Each recording, chat, clip, transcript, state file, or story can have its own sharing level.

Suggested levels:

- Narrator only.
- Interviewer only.
- Named people only.
- Immediate family.
- Extended family.
- All descendants.
- Research team under an approved process.
- Public.
- Sealed until a date.
- Sealed until after death.
- Permanently private.

Sensitive stories should default to narrower access.

## Third-party privacy

A narrator can tell a story involving another person, but that does not erase the other person's privacy.

Be careful with:

- Medical history.
- Mental health.
- Addiction.
- Violence.
- Abuse.
- Sexual relationships.
- Paternity or adoption.
- Money, debt, inheritance.
- Crime or accusations.
- Political risk.
- Caste, religion, migration, or identity-based risk.
- Stories about living people who cannot respond.

Consider marking such material restricted by default. Do not treat an allegation in a life interview as a verified fact.

## Family and system power dynamics

Family interviews are not neutral. AI interviews are not neutral either.

A narrator may self-censor because the interviewer is:

- A child.
- A parent.
- A spouse.
- A sibling.
- A person from a more powerful gender, caste, class, religion, institution, or generation.
- Someone who benefits from a particular version of the story.
- Someone who was part of the painful event.
- An AI system the narrator believes is authoritative, private, always correct, or impossible to refuse.

The method should allow another interviewer, private additions, shorter sessions, or no interview.

AI must not use endless availability, rapid follow-ups, personalization, praise, or claims of neutrality to pressure disclosure.

## Difficult material

Do not chase trauma.

If the narrator becomes distressed or says the topic is difficult:

> “Would you like to continue, pause, change topics, or stop?”

Do not say:

> “This will help you heal.”

Do not say:

> “You need closure.”

Do not say:

> “People should know the truth.”

Do not infer distress, trauma, or diagnosis from writing style, voice, face, or images. Use only the narrator's words and directly observable interaction signals.

The narrator controls the boundary.

## Current danger or crisis

If the narrator indicates immediate current danger, pause the life-history interview and follow the applicable safety process. Do not continue eliciting narrative detail while immediate safety is unresolved.

This method is not crisis care.

## After difficult material

Before ending, ask one question at a time:

> “Do you want any restrictions on what we just discussed?”  
> “Do you want this kept, sealed, excluded from summaries, or removed where possible?”  
> “Would you like to return to something lighter before stopping?”

End with stabilization and control, not intensity.

## For narrators with cognitive impairment

This method is not designed as a dementia, capacity, or clinical protocol.

If capacity is uncertain:

- Use shorter sessions.
- Use simpler consent checks.
- Involve legally appropriate decision-makers.
- Avoid sensitive topics unless the person clearly wants to speak.
- Preserve dignity.
- Do not pressure exact recall.
- Do not use apparent chat fluency as proof of capacity.
- Seek professional guidance where needed.

## For minors

This method is designed for adults.

Do not use it with minors without a separate child-safe protocol, guardian consent where legally required, safeguards against coercion, and a clear plan for mandatory-reporting or safeguarding duties where applicable.

## Storage location and public repositories

Interview instructions may live in a public repository. Narrator material should not.

By default, do not place transcripts, session state, recordings, identifying notes, or access-control decisions inside this repository or any other public Git history. `.gitignore` helps prevent accidental additions but does not remove data already committed, uploaded, cached, logged, or shared.

Before saving narrator material, agree on:

- The exact storage location.
- Who controls and can access it.
- Whether it is encrypted.
- How backups, exports, and deletion requests work.
- Whether Git, cloud sync, model memory, analytics, or human review are involved.

Use a private location outside the method repository unless the narrator has explicitly approved publication after review.

## AI use

General interview consent is not permission for unrestricted AI use.

AI involvement may include:

- Conducting the interview.
- Assisting a human interviewer.
- Transcription.
- Translation.
- Summarization.
- Persistent memory or state.
- Search.
- Voice synthesis.
- Persona simulation.
- Model training or evaluation.

Each requires the appropriate separate permission.

Default rule:

> No model training, synthetic voice, synthetic likeness, or first-person narrator persona unless the narrator explicitly opted in while alive and capable, with the exact use and system identified.

See [`12-future-ai-boundary.md`](12-future-ai-boundary.md) and [`../INTERVIEWER.md`](../INTERVIEWER.md).
