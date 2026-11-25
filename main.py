"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes a single weird job title, one line, to /output/entry.txt.
The title is a plain constant: a real-sounding job with one
hilariously specific twist, short enough to read at a glance.

No network, no input, no secrets. Deterministic: every run writes
the same bytes.
"""

import os
import shutil

TITLE = "Senior Professional Apologizer for Other People's Dogs"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run
    # this with a root-owned output dir inside a sticky parent, where
    # deleting the directory fails with EPERM. Create it if missing,
    # then clear only its contents.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    # Write exactly the title, no trailing newline, so the file is
    # one line of 54 characters (gate: 1-60 characters, UTF-8).
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
