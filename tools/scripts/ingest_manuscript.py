"""
ingest_manuscript.py

Reads manuscript/full_text.md, confirms the file exists, and prints a word
count and rough page estimate. Does not modify the file.

Usage:
    python tools/scripts/ingest_manuscript.py
"""

import os
import sys

MANUSCRIPT_PATH = os.path.join("manuscript", "full_text.md")
WORDS_PER_PAGE = 250  # standard estimate for a novel page


def ingest_manuscript(path: str) -> None:
    """Verify the manuscript file exists and print basic statistics."""
    abs_path = os.path.abspath(path)

    if not os.path.isfile(abs_path):
        print(f"ERROR: Manuscript file not found at '{abs_path}'")
        print("Please place your manuscript text in manuscript/full_text.md")
        sys.exit(1)

    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    word_count = len(words)
    page_estimate = word_count / WORDS_PER_PAGE

    print(f"Manuscript found: {abs_path}")
    print(f"  Characters : {len(text):,}")
    print(f"  Words      : {word_count:,}")
    print(f"  Pages (est): {page_estimate:.0f}  (at {WORDS_PER_PAGE} words/page)")

    if word_count == 0:
        print("\nWARNING: The manuscript file appears to be empty.")
        print("Upload your manuscript text to manuscript/full_text.md and run this script again.")


if __name__ == "__main__":
    ingest_manuscript(MANUSCRIPT_PATH)
