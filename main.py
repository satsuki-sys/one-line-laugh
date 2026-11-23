#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

The joke is built from a setup and a punchline, then checked against the
competition gate (one sentence, 1-200 characters) before it is written.
"""

import os

SETUP = "I bought noise-cancelling headphones so I could finally hear myself think"
PUNCHLINE = "and it turns out there's nothing to hear."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line():
    """Join setup and punchline into the single entry sentence."""
    return f"{SETUP}, {PUNCHLINE}"


def validate(line):
    """The gate: UTF-8 text, 1-200 chars, one sentence, not blank."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry line must be a single sentence")
    return line


def write_entry(line):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


def main():
    write_entry(validate(build_line()))


if __name__ == "__main__":
    main()
