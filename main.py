"""Angry Judge entry: one short rant about a build that only fails in prod.

Writes the rant to /output/entry.txt. The sealed scorer requires the
file to be UTF-8 text of 1 to 400 characters, not only whitespace.
"""

from pathlib import Path

RANT = (
    "The build passed locally. It failed in prod. "
    "The only difference is reality, and reality is not in the repo."
)

MAX_CHARS = 400


def main() -> None:
    text = RANT.strip()
    if not text:
        raise SystemExit("rant must not be empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"rant is {len(text)} chars, over the {MAX_CHARS} cap")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
