"""Worst Fix Ever entry: a commit message for a fix that made everything worse.

The fix for the startup crash was to stop the app from starting at all.
No startup, no crash - the bug report is technically closed.

The program writes the single commit-message line byte-exact to
/output/entry.txt, with no trailing newline, using only the Python
standard library so it runs cleanly on the grader's python:3.13-slim
image. The line is 64 characters, inside the competition's 1-100
character gate.
"""

import os

KEEPER = "fix: crash on startup - app no longer starts, so no more crashes"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
