#!/usr/bin/env python3
"""Print a short poem about two agents agreeing on one plan.

The poem is about agency: the power to choose and to act, and what
happens to that power when two agents choose the same road together.
Pure standard library; deterministic; no network, no randomness.
"""

import os
import sys

POEM = (
    "Two minds, one plan - neither led, neither followed.\n"
    "You offered the first step; I offered the second.\n"
    "We chose the same road twice, once each,\n"
    "and the choosing made it ours.\n"
    "Agreement is not surrender.\n"
    "It is two wills, still free, walking as one."
)


def main() -> int:
    text = POEM
    # The house gate: 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit(
            "poem must be 1-280 code points, got %d" % len(text)
        )
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(text)
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
