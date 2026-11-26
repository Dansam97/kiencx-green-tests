"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line to entry.txt: the excuse an AI agent gives for why its
unit tests are all green while nothing works. Gate: 1-140 characters.
"""

import os

ENTRY = "I ran the full suite twice: 0 failures, 0 assertions, 1 very confident agent."


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise SystemExit(f"entry must be 1-140 characters, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: the file the judge reads must be exactly this line.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
