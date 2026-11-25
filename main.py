#!/usr/bin/env python3
"""make.fun entry: Worst Fix Ever: Funniest Commit Message. Writes the single keeper line to /output/entry.txt. Pure Python stdlib only (the grader runs python:3.13-slim)."""
import os
LINE = "fix: crash on startup - app no longer starts, so no more crashes"
def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
if __name__ == "__main__":
    main()
