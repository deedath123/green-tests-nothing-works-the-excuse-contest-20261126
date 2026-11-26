"""Green Tests, Nothing Works: The Excuse Contest — entry program.

Writes the excuse entry to /output/entry.txt.
"""

import os

ENTRY = "All 47 tests are green because I grade my own homework — and I've never once marked myself wrong."


def main() -> None:
    # Gate: the entry must be 1-140 UTF-8 characters, not only whitespace.
    # Length is counted in characters (len), matching the contest rule.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
