#!/usr/bin/env python3
"""Angry Judge entry: write the rant to /output/entry.txt."""

import os

ENTRY = "The build passed locally. It failed in prod. The only difference is reality, and reality is not in the repo."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters.
    if not 1 <= len(ENTRY) <= 400 or not ENTRY.strip():
        raise SystemExit("entry fails length gate: %d chars" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
