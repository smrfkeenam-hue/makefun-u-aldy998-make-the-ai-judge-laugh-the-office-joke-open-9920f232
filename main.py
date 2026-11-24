"""Office Joke Open entry: one line of office comedy.

Writes the joke to /output/entry.txt, exactly as-is, no trailing newline.
"""

import os


def joke():
    """Return the entry line: office plants, HR, and a motivational poster."""
    return "The office plants died. HR replaced them with a poster that says 'grow'."


def main():
    text = joke()
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
