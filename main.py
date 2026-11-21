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


def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
