#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message (make.fun).

Writes one commit message for the bug fix that made everything worse:
the startup crash is "fixed" because the app no longer starts at all,
so there are no more crashes. Pure stdlib only.
"""
import os

ENTRY = "fix: crash on startup - app no longer starts, so no more crashes"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
