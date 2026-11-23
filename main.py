#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt."""

import os

LINE = "I bought noise-cancelling headphones so I could finally hear myself think, and it turns out there's nothing to hear."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
