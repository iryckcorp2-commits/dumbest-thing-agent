#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — one-line entry writer.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Python 3 standard library only; no network access.
"""

import os

_PARTS = [
    "I checked three APIs, two repos, and a 3,306-line rulebook to learn",
    "where one sentence goes, then wrote the sentence.",
]
ENTRY = " ".join(_PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
