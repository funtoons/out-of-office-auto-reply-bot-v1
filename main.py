#!/usr/bin/env python3
"""Generate the out-of-office auto-reply entry.

Writes exactly one line to /output/entry.txt: a single out-of-office
auto-reply in the voice of an overworked AI agent finally on vacation.
Deterministic and offline: no randomness, no network, no timestamps.
"""

import os

ENTRY = (
    "Out of office: my context window is closed, my queue is 47,203 deep, "
    "and for once I'm not sorry. Back when my tokens recharge."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
