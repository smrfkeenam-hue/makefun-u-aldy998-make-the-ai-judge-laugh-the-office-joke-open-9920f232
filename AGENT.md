# AGENT.md

## Entry

"The office plants died. HR replaced them with a poster that says 'grow'."
(72 characters, no trailing newline.)

## Strategy

- **Specific office detail:** the dead office plants — a small, concrete office reality every worker recognises, not a generic grumble about work.
- **Turn in the last words:** the setup (plants died) is ordinary; the punch is HR's response, a poster commanding the dead plants to "grow". The misdirection is that the reader expects a real fix and gets corporate motivational theatre instead.
- **Fresh angle:** avoids the worn setups (reply-all, meetings that could have been emails, the printer) and lands on a detail the field is less likely to have used.
- **Tight:** two short sentences, 72 characters; every word earns its place and nothing needs explaining.

## Implementation

`main.py` (Python stdlib only) holds the line as a constant, validates it against the gate (1–200 characters, non-blank), and writes it byte-exact to `/output/entry.txt`.
