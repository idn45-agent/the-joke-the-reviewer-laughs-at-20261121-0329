#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

Python 3.13, standard library only, no network, deterministic.
Writes entry.txt into the directory named by ENTRY_OUT (default /output).
"""
import os
from pathlib import Path

JOKE = (
    "My AI coding agent wrote the feature, the tests, and the docs \u2014 "
    "then left one TODO in the code: 'human to check this actually works.'"
)


def validate_joke(text: str) -> None:
    """Fail hard if the joke violates the competition's entry gate.

    Gate: exactly one line, 1-280 characters, not whitespace-only.
    A silent bad entry would fail the kit check; raise before writing.
    """
    if not text or not text.strip():
        raise ValueError("joke must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line (no newline characters)")
    if len(text) > 280:
        raise ValueError(f"joke is {len(text)} chars, over the 280-char limit")


def main() -> None:
    validate_joke(JOKE)
    out_dir = Path(os.environ.get("ENTRY_OUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
