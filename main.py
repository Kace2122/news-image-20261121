#!/usr/bin/env python3
"""news-image-20261121 entry: "The World Today", Saturday 21 November 2026.

The program copies the front-page image held in this repository to the
grader's output directory. It uses only the standard library, reads no
network, and writes the same bytes on every run: a plain file copy, so
the two grading runs are byte-identical by construction.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
