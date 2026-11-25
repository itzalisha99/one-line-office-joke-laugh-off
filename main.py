#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — entry program.

Writes one original one-line office joke to /output/entry.txt.
Stdlib only.

The bounty gate (from the kit's competition.yaml): /output/entry.txt
must be UTF-8 text of 1 to 200 characters, not only white space, on a
single line. validate() enforces exactly that before the write, and
main() reads the file back to prove the bytes on disk are the line.
"""

import os

ENTRY = "The fire drill went off during my performance review. I have never been so grateful to a fire."

MAX_CHARS = 200


def validate(text):
    """Mirror the bounty gate: 1-200 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is over 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the validated line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("entry.txt does not match the validated entry")


if __name__ == "__main__":
    main()
