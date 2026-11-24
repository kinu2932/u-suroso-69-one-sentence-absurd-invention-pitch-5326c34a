#!/usr/bin/env python3
"""One-sentence absurd invention pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only, deterministic.
"""

import os

PITCH = (
    "A washing machine that holds one sock hostage from every load "
    "and only returns it once you apologise out loud for overloading it."
)


def main() -> None:
    # Self-check against the sealed gate: 1-220 chars, one sentence.
    assert 1 <= len(PITCH) <= 220, f"pitch is {len(PITCH)} chars"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "must be one sentence"
    assert PITCH.strip() == PITCH, "no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)


if __name__ == "__main__":
    main()
