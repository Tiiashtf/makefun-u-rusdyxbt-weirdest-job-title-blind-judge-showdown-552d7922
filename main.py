#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes exactly one job title to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt):

    Professional Apologizer for Billionaires' Yachts

Why this title: the judge weighs, in order, weirdness, strangeness,
funniness, sounding like a real job, and reading instantly. This title
is a real-sounding job — a professional apologizer — with one
hilariously specific twist: the apologies are for billionaires' yachts,
as if the yacht itself did something wrong and someone has to say sorry
for it. You can picture the person at once: suit, clipboard, standing
on a dock, apologising on behalf of a boat. It lands on the first read,
and it is short enough to take in at a glance.

Deterministic: the same bytes on every run. No network, no randomness,
no input read. Only the output directory's contents are cleared — the
directory itself is never removed, so a root-owned output directory
inside a sticky parent still works.
"""

import os
import shutil
import sys

TITLE = "Professional Apologizer for Billionaires' Yachts"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_contents(directory: str) -> None:
    """Remove everything inside directory, never the directory itself."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.islink(path) or os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            # fifos, sockets, devices: unlink, never follow
            os.unlink(path)


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_contents(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    # Read it back and verify byte for byte: 48 characters, the title.
    with open(OUTPUT_FILE, "rb") as f:
        data = f.read()
    if data != TITLE.encode("utf-8"):
        print(f"verification failed: entry.txt holds {data!r}", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_FILE}: {data!r} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
