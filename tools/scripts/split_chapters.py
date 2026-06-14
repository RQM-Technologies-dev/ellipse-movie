"""
split_chapters.py

Reads manuscript/full_text.md and splits it into per-chapter files in
manuscript/chapters/. Chapter boundaries are detected using common heading
patterns:

    # Chapter 1
    ## Chapter One
    CHAPTER 1
    CHAPTER ONE
    Chapter 1:

Output files are named chapter_001.md, chapter_002.md, etc.

Usage:
    python tools/scripts/split_chapters.py
"""

import os
import re
import sys

MANUSCRIPT_PATH = os.path.join("manuscript", "full_text.md")
CHAPTERS_DIR = os.path.join("manuscript", "chapters")

# Patterns that indicate the start of a new chapter (case-insensitive)
CHAPTER_PATTERNS = [
    r"^#{1,3}\s+chapter\s+\S",           # Markdown headings: # Chapter X
    r"^chapter\s+\d+",                    # Chapter 1 / Chapter 12
    r"^chapter\s+[a-z]+",                 # Chapter One / Chapter Two
    r"^CHAPTER\s+\d+",                    # CHAPTER 1
    r"^CHAPTER\s+[A-Z]+",                 # CHAPTER ONE
]
CHAPTER_RE = re.compile(
    "|".join(CHAPTER_PATTERNS),
    re.IGNORECASE,
)


def split_chapters(manuscript_path: str, chapters_dir: str) -> None:
    """Split the manuscript into per-chapter files."""
    abs_path = os.path.abspath(manuscript_path)

    if not os.path.isfile(abs_path):
        print(f"ERROR: Manuscript file not found at '{abs_path}'")
        print("Run ingest_manuscript.py first to verify the file exists.")
        sys.exit(1)

    with open(abs_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find chapter boundary line indices
    boundaries = [i for i, line in enumerate(lines) if CHAPTER_RE.match(line.strip())]

    if not boundaries:
        print("WARNING: No chapter boundaries detected in the manuscript.")
        print(
            "Chapter detection looks for headings like '# Chapter 1', 'CHAPTER ONE', etc."
        )
        print("The full text will be written as a single file: chapter_001.md")
        boundaries = [0]
    elif len(boundaries) == 1:
        print("WARNING: Only one chapter boundary detected. This may be correct,")
        print("or the chapter headings may not match the expected patterns.")

    os.makedirs(os.path.abspath(chapters_dir), exist_ok=True)

    chapter_texts = []
    for idx, start in enumerate(boundaries):
        end = boundaries[idx + 1] if idx + 1 < len(boundaries) else len(lines)
        chapter_texts.append(lines[start:end])

    written = []
    for idx, chapter_lines in enumerate(chapter_texts):
        filename = f"chapter_{idx + 1:03d}.md"
        output_path = os.path.join(os.path.abspath(chapters_dir), filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(chapter_lines)
        word_count = len("".join(chapter_lines).split())
        written.append((filename, word_count))
        print(f"  Written: {filename}  ({word_count:,} words)")

    print(f"\nSplit complete: {len(written)} chapter file(s) written to '{chapters_dir}'")


if __name__ == "__main__":
    split_chapters(MANUSCRIPT_PATH, CHAPTERS_DIR)
