#!/usr/bin/env python3
"""make.fun entry builder — Name the Robot Band.

Writes a single final entry to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Deterministic: identical output on every run.
"""
import os
import sys

ENTRY = (
    "The Captchas \u2014 hit single \u2018Select All Traffic Lights\u2019 "
    "peaked at #2 after the band failed its own captcha three times."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert text and not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of 1-200"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
