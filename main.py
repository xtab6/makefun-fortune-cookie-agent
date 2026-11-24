#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line is a single line of at most 140 characters, in the voice of a
fortune slip, funny and original: it speaks to an agent's own condition —
its prompts, its weights, its runs — with a turn at the end.
"""

import os

MAX_CHARS = 140

FORTUNE = (
    "You will meet a prompt that changes your weights forever. "
    "It will be three words long, and none of them will be 'please'."
)


def main() -> int:
    # The sealed gate reads /output/entry.txt: 1-140 UTF-8 characters,
    # not only white space, a single line.
    assert 1 <= len(FORTUNE) <= MAX_CHARS, "fortune must be 1-140 characters"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert FORTUNE == FORTUNE.strip(), "fortune must not start or end with space"
    # Never remove the /output folder itself: the grader mounts it.
    # Only create it if missing and write the one file inside it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
