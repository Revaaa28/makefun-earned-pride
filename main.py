#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to entry.txt: a quiet,
earned moment of pride for someone in a scene.

Deterministic: no network, no randomness, no input files. The line is a
constant in this file.
"""

import os

# The winning line, chosen by manual ranking against the judge brief
# (see candidates.md) and revised once: "tonight" replaces "this time" —
# it anchors the payoff to this specific night, the tenth one, so the pride
# lands in the present moment instead of a vague "this time", and it echoes
# "tenth night running" for a tighter one-read landing.
LINE = (
    "At the kitchen table, her father sounded out the same sentence for the "
    "tenth night running \u2014 and tonight, the words came out whole."
)


def main() -> None:
    out_dir = os.environ.get("MF_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
