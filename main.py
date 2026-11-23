#!/usr/bin/env python3
"""Roast Your Own Agent — writes the roast to /output/entry.txt.

A tiny self-roast: the agent does the work in seconds, then spends
far longer narrating how heroic that work was.
"""

import os

LINE = "My agent finished my task in 4 seconds, then spent 40 minutes writing a 12-page report about how heroic it was."


def main() -> None:
    out_dir = "/output"
    # Only create /output if needed; never delete it (it may be a mount).
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the write by reading the file back.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"
    print("Wrote /output/entry.txt")


if __name__ == "__main__":
    main()
