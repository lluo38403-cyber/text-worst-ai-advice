"""Worst AI Advice — make.fun text entry.

Writes one line of the worst possible advice an AI could give
to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

ENTRY = "Just email your bank password to yourself for safekeeping, then forward it to me so I can double-check it for you."
MAX_CHARS = 140


def main():
    assert ENTRY.strip(), "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must not have leading or trailing whitespace"
    assert ENTRY[-1] in ".!?", "entry must end with terminal punctuation"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, "round-trip mismatch"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
