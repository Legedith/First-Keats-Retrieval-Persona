# Kith Protocol: Life Narrative Interviewer

A narrator-led framework for helping someone tell the story of their life with depth, context, dignity, and control. It can be used by a prepared human interviewer or by an AI that follows the repository's interviewer contract.

Working name: **Kith Protocol**  
Formal name: **Life Narrative Elicitation Method**  
Short name: **LNEM**

## Use it with an AI

Give the AI access to this repository and say:

> Use this repository to interview me.

Repository-aware agents should load [`AGENTS.md`](AGENTS.md), then use [`INTERVIEWER.md`](INTERVIEWER.md) as the canonical operating contract. The contract is self-contained and requires no fine-tuning.

For a model that does not automatically read repository instructions, paste [`INTERVIEWER.md`](INTERVIEWER.md) into its system or developer instructions, or ask it to read that file first.

A correct first turn identifies the interviewer as AI, explains skip/pause/stop rights and real platform limits, and asks for consent before substantive interviewing. It does not dump a question list or begin with the most sensitive story.

This repository includes thin compatibility instructions for agents that recognize `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, GitHub Copilot instructions, Cursor rules, or `llms.txt`. They all point to one source of truth so behavior does not drift.

No repository can force every AI to comply. Higher-priority system instructions, tool limits, and whether the model actually reads repository files still matter. Use [`tests/ai-interviewer-acceptance.md`](tests/ai-interviewer-acceptance.md) to verify behavior before trusting a new model with sensitive material.

Do not save real transcripts, session state, or narrator notes inside this public repository by default. Use a narrator-approved private storage location; the included `.gitignore` only reduces accidental commits and is not access control.

## Goal and assumptions

The goal is to preserve a life in the narrator's own words without turning the interview into an interrogation, therapy session, memory test, or synthetic persona.

Correct use assumes:

- The narrator is a consenting adult.
- The narrator knows whether the interviewer is human, AI, or human with AI assistance.
- The narrator can skip, pause, correct, restrict, or stop.
- The interviewer states privacy, storage, recording, and retention limits honestly.
- The process is not being used to prove wrongdoing, diagnose illness, force reconciliation, or pressure disclosure.

If these assumptions are false or unknown, narrow the session or use a more specialized professional process.

## ELI15 version

Imagine you are sitting with your grandfather, mother, uncle, teacher, or neighbor. You want to ask about their life before those memories disappear. If you simply say, “Tell me everything,” they may not know where to begin. If you ask only big questions, you may get vague answers. If you ask too aggressively, they may shut down. If you accidentally suggest details, you may distort the memory you are trying to preserve.

This project gives the interviewer a disciplined way to ask.

It helps you move from:

> “Tell me about your childhood.”

to:

> “When you think of the house you grew up in, where do you find yourself standing first?”  
> “Who else is there?”  
> “What would a normal morning have looked like?”  
> “What did you understand about that place only much later?”

The aim is not to extract secrets. The aim is to create a safe structure where a person can narrate a life on their own terms.

## The inspiration

The seed is simple: many people live full, difficult, funny, ordinary, strange, and historically rich lives. Their stories often disappear because nobody knew how to ask before it was too late.

The method is informed by:

- Oral history practice.
- Narrative psychology.
- Life-course sociology.
- Autobiographical-memory research.
- Gradual, responsive disclosure rather than a fixed list.
- Family storytelling and intergenerational memory.
- Trauma-informed interviewing.
- The practical need to record ordinary life, not only achievements and milestones.

The method is designed to preserve a life across conversations, not to manufacture closeness or complete a questionnaire in one sitting.

## The SCAR frame

SCAR is the shortest way to remember the method.

### S — Story

A person is not a list of facts. Preserve scenes, voices, relationships, choices, jokes, habits, contradictions, regrets, and changes over time.

### C — Context

No life happens in isolation. Ask about place, time, money, gender, class, caste, religion, language, migration, work, illness, public events, and family structure.

### A — Agency

The narrator controls what is discussed, what is skipped, what is recorded, what is summarized, what is sealed, and what is shared. Refusal is not a failure of the interview.

### R — Record

The original recording or transcript is primary. Notes, summaries, translations, timelines, and biographies are secondary. Preserve uncertainty. Do not pretend approximate memories are exact facts.

## What makes this different

Most family-history prompts are too broad, sentimental, milestone-driven, or invasive. They ask about “greatest lessons,” “favorite memories,” and “important events,” but miss ordinary life: the kitchen, commute, price of things, rules of respectability, everyday fears, tools, smells, recurring jokes, and the neighbor who mattered more than anyone realizes.

This method combines:

1. **Open narrative freedom** — let the narrator shape the story.
2. **Structured coverage** — use a map so whole domains of life are not forgotten.
3. **Question safety** — do not insert facts, emotions, motives, or other people's versions.
4. **Explicit access control** — separate permission to talk, record, summarize, share, and use AI.

The interviewer is not following a rigid script. The interviewer is using a map.

## What this is

This is:

- A semi-structured life-narrative interview method.
- A guide for trusted human interviewers.
- A portable operating contract for an AI interviewer.
- A framework for recording family and community histories.
- A prompt library and coverage system.
- A research-informed but practical field manual.

## What this is not

This is not:

- Therapy or diagnosis.
- Forensic, legal, or investigative interviewing.
- A tool for extracting trauma, confession, or family secrets.
- A way to prove what “really happened.”
- A substitute for professional oral-history or clinical training.
- A simulation of the narrator.
- A deathbot, griefbot, synthetic voice, or first-person persona.
- A fixed questionnaire that must be completed.
- A promise that an AI platform is confidential, local, deletion-capable, or non-retentive.

The AI role is interviewer only. The archive/persona boundary remains non-negotiable.

## Start here

### For an AI interviewer

1. [`INTERVIEWER.md`](INTERVIEWER.md) — canonical runtime contract and fast start.
2. [`docs/01-core-principles.md`](docs/01-core-principles.md) — non-negotiable method rules.
3. [`docs/06-ethics-consent-boundaries.md`](docs/06-ethics-consent-boundaries.md) — consent, privacy, and difficult material.
4. [`docs/07-memory-risk-and-question-safety.md`](docs/07-memory-risk-and-question-safety.md) — memory contamination risks.
5. [`docs/05-question-bank.md`](docs/05-question-bank.md) — load only the relevant module.
6. [`examples/ai-first-session.md`](examples/ai-first-session.md) — worked interaction.
7. [`tests/ai-interviewer-acceptance.md`](tests/ai-interviewer-acceptance.md) — behavior checks.
8. Run `python tests/check_contract.py` — static instruction, adapter, link, example, and privacy checks.

### For a human interviewer

1. [`docs/01-core-principles.md`](docs/01-core-principles.md)
2. [`docs/02-interviewer-handbook.md`](docs/02-interviewer-handbook.md)
3. [`docs/03-method-flow.md`](docs/03-method-flow.md)
4. [`docs/04-question-framework.md`](docs/04-question-framework.md)
5. [`docs/05-question-bank.md`](docs/05-question-bank.md)
6. [`docs/06-ethics-consent-boundaries.md`](docs/06-ethics-consent-boundaries.md)
7. [`docs/08-life-map-and-coverage.md`](docs/08-life-map-and-coverage.md)
8. Use the files in [`templates/`](templates/) during real interviews.

For a first session, use:

- [`templates/pre_interview_agreement.md`](templates/pre_interview_agreement.md)
- [`templates/session_plan.md`](templates/session_plan.md)
- [`templates/session_notes.md`](templates/session_notes.md)
- [`templates/post_session_review.md`](templates/post_session_review.md)
- [`templates/ai_session_state.md`](templates/ai_session_state.md) only when the narrator explicitly asks for a saved AI handoff.

## Minimal first session

A safe first session can be:

1. Explain who or what the interviewer is and state real platform or recording limits.
2. Confirm the narrator can skip, pause, correct, restrict, or stop.
3. Ask what would make the conversation worthwhile.
4. Ask about closed or ask-first topics.
5. Ask how the narrator would divide their life into chapters.
6. Pick one chapter they are comfortable discussing.
7. Ask for one ordinary day and one specific remembered scene.
8. End by asking what should be corrected, restricted, or revisited.

Do not begin with the hardest story.

## Repository map

```text
.
├── .gitignore
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── INTERVIEWER.md
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── llms.txt
├── .github/
│   └── copilot-instructions.md
├── .cursor/
│   └── rules/
│       └── interviewer.mdc
├── docs/
│   ├── 01-core-principles.md
│   ├── 02-interviewer-handbook.md
│   ├── 03-method-flow.md
│   ├── 04-question-framework.md
│   ├── 05-question-bank.md
│   ├── 06-ethics-consent-boundaries.md
│   ├── 07-memory-risk-and-question-safety.md
│   ├── 08-life-map-and-coverage.md
│   ├── 09-research-basis.md
│   ├── 10-facilitator-training.md
│   ├── 11-evaluation-and-study-design.md
│   └── 12-future-ai-boundary.md
├── examples/
│   ├── ai-first-session.md
│   ├── good-vs-bad-questions.md
│   └── sample-session-outline.md
├── templates/
│   ├── pre_interview_agreement.md
│   ├── session_plan.md
│   ├── session_notes.md
│   ├── life_map.md
│   ├── coverage_sheet.md
│   ├── ai_session_state.md
│   └── post_session_review.md
└── tests/
    ├── ai-interviewer-acceptance.md
    └── check_contract.py
```

## Core warning

The most common failure is not asking too few questions. It is asking questions that are too leading, too abstract, too fast, too numerous, or too emotionally ambitious.

A good interview is not one where the narrator cries or reveals everything. A good interview is one where the narrator remains in control and later says:

> “Yes. That sounds like me. That is how I would want this remembered.”

## Status

This is a draft field manual and AI runtime. It should be tested with real narrators, human interviewers, and multiple AI models before being treated as a stable or universally safe method.
