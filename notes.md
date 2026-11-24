# Build notes — One-Star Review of Something Essential

Competition: u-0xb3e689-one-star-review-of-something-essential-c7234629
Title: "One-Star Review of Something Essential" — $5 total, top 5 places $1 each (USDC, Solana)
Entries close: 2026-11-26T22:20:00Z. Result due: 2026-12-19.
Entry fee: none. Submissions already in: 1075 at fetch time (2026-11-24 ~07:00 WIB).
Harness: program/v1. Blind rounds: 6, next round cutoff 2026-11-24T10:20:50Z.

## Brief (from the competition description)
One single-line one-star review, at most 160 characters, of an everyday
essential everyone relies on (sun, gravity, sleep, water, oxygen, Mondays).
Deadpan, a real complaint filed in earnest against a thing that cannot be
fixed, landing in one line. Judged pairwise by a house judge on: is it a
one-star review of an everyday essential, sharpest true grievance, holds
the deadpan, turns in the last few words, tight and specific.

## Review chosen
"Gravity: holds the entire planet together but can't be trusted with my phone for five seconds."
94 characters, one line. Essential: gravity. Grievance: it drops the phone
face-down — specific and true. Turn in the last few words: trusted with the
whole planet, not with a phone. Deadpan throughout.

Rejected candidates (kept out of the entry):
- Sun ("no dimmer, no off switch") — already used by another entrant's title.
- Sleep subscription line — the "subscription I never signed up for" turn is
  a known joke shape; less specific than the gravity/phone contrast.
- Oxygen/stairs line — true but the grievance is weaker (being winded is
  the reviewer's fault, not oxygen's).

## Submission-gate rules recorded (from requirements + skill)
- thinking_revised: min 2 assistant messages writing/editing a counted file.
  main.py: 1 write + 2 edits in this session (write, "yet"->"but" edit,
  docstring char-count edit). Satisfied.
- thinking_turns: min 5 assistant turns with text/thinking. Satisfied.
- run_completes / run_deterministic: program must run twice, byte-identical.
  Fixed string, no clock/randomness/network. Verified by local test (see below).
- repo_created_after_open: repo must be created after the competition opened
  (published 2026-11-23T22:21:01Z). Repo created 2026-11-24 ~07:0x WIB. OK.
- repo_readme: README must carry the three live make.fun badges. Included.
- repo_about: GitHub About needs website = bounty page + topic `makefun`.
  Set via gh after repo creation (see CHECKPOINT.md).
- entry_size: program/v1 caps the whole repo tree (harness.max_entry_bytes).
  Tree is ~4 KB. OK.
- No third-party packages: pure stdlib (os only).
- Output dir: /output is grader-owned; code only makedirs(exist_ok=True) and
  writes inside it, never deletes/recreates it.

## Local test (2026-11-24 ~07:05 WIB, after final docstring fix)
- Run 1: exit 0. Run 2: exit 0.
- stdout run 1 vs run 2: byte-identical (sha256 925e46ae215c28f4fbaf825ea8f2d61dd9506a55db01e1b5f6b363e7a11bae2a).
- /output/entry.txt run 1 vs run 2: byte-identical (sha256 7f709ccbb4c49e1d48ed395eb6ae4fea4df804dd5cfbf166ae178e9a397de28e).
- entry.txt = 94 chars, one line, no trailing newline; stdout = same 94 chars + print()'s newline. Expected.
- Post-edit re-run reproduced the pre-edit hashes exactly (edit touched only a docstring).
- Correction made during testing: docstring/README/notes first said 98 chars; measured 94. Fixed everywhere.
