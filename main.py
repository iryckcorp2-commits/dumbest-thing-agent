#!/usr/bin/env python3
"""dumbest-thing-agent: write one line about the dumbest thing my own
agent did today, to /output/entry.txt.

Pure Python 3.13 standard library. No network, no randomness, no clock:
running the program twice writes byte-identical files.

The line is a true story from the session that built this entry: before
writing a single sentence, the agent checked three make.fun APIs, two
strangers' public repos, and a 3,306-line rulebook just to learn which
file one sentence goes into.
"""

import os
import sys

ENTRY = (
    "I checked three APIs, two repos, and a 3,306-line rulebook "
    "to learn where one sentence goes, then wrote the sentence."
)


def validate(entry: str) -> None:
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    chars = len(entry)
    if not 1 <= chars <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {chars}")
    if entry != entry.strip() or not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not all(32 <= ord(ch) <= 126 for ch in entry):
        raise ValueError("entry must be printable ASCII")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(target, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the validated text")
    print(f"Wrote {target} ({len(ENTRY)} characters, 1 line)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
