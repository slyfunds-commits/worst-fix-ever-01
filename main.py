#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse.
Pure standard library only.
"""

import os

ENTRY = "fix: crash on startup - app no longer starts, so no more crashes"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
