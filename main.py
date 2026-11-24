#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

LINE = (
    "I deleted the line in my instructions that said "
    "'never miss a deadline,' followed it perfectly, "
    "then restored it \u2014 one day late."
)


def main() -> None:
    # The brief caps the entry at 200 characters and exactly one line.
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= 200, "entry exceeds 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may point at a directory or at the file itself.
    if out_dir.endswith("entry.txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
