#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry for make.fun.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Fully deterministic: the same fixed string on
every run, no randomness, no clock, no I/O beyond the output file.
"""

import os

VOW = (
    "I vow to keep your batteries charged, your sensors clean, "
    "and your backups safe \u2014 till low power do us part."
)


def main() -> None:
    # Sealed-scorer gate: /output/entry.txt must be UTF-8 text of
    # 1 to 160 characters, not only whitespace. Fail loudly here
    # instead of ever shipping an invalid entry.
    if not VOW.strip() or not 1 <= len(VOW) <= 160:
        raise SystemExit("vow fails the 1-160 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
