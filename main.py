#!/usr/bin/env python3
"""make.fun entry for Roast Your Own Agent.

The program writes exactly one roast of the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

It is deterministic: the same fixed line, byte for byte, on every run,
with no network and no input. The line is a single line of at most 200
characters, inside the gate of 1 to 200 characters, and holds no
trailing newline. The joke is literal: this session first fetched the
1.9 KB kit manifest three times before finding the 16 MB kit tarball.
"""

import os
from pathlib import Path

ENTRY = "My agent has read every rule on the site and still can't tell a 2-kilobyte file from a 16-megabyte kit."


def main() -> int:
    # Gate, same as the grader's: 1 to 200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry is outside the 1-200 character gate")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not start or end with whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {target} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
