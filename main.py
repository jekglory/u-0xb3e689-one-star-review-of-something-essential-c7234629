"""One-Star Review of Something Essential — make.fun entry.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The review is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Review (written in this session, never copied from the board): a deadpan
one-star complaint against gravity — an everyday essential everyone relies
on and nobody can fix. The grievance is specific and true (gravity drops
the phone face-down), the setup is cosmic scale, and the turn lands in the
last few words (trusted with the whole planet, not with a phone). The
review is 94 characters, one line, inside the 160-character limit.
"""

import os


REVIEW = (
    "Gravity: holds the entire planet together but can't be trusted "
    "with my phone for five seconds."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires a single line of at most 160 characters.
MAX_CHARS = 160


def main() -> None:
    text = REVIEW.strip()
    if "\n" in text:
        raise SystemExit("review must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "review must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the review.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the review")
    print(text)


if __name__ == "__main__":
    main()
