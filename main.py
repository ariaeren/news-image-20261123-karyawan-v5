#!/usr/bin/env python3
"""Copy the committed 1024x1024 news image to the make.fun output directory.

The image is carried verbatim in this repository, so the program is
deterministic and uses only the Python 3.13 standard library.
"""

from __future__ import annotations

import os
from pathlib import Path


def find_image() -> Path:
    """Find entry.png beside this file, falling back to the mounted repo."""
    here = Path(__file__).resolve().parent / "entry.png"
    if here.is_file():
        return here
    mounted = Path("/bot/entry.png")
    if mounted.is_file():
        return mounted
    raise FileNotFoundError("entry.png was not found beside main.py or in /bot")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(find_image().read_bytes())


if __name__ == "__main__":
    main()
