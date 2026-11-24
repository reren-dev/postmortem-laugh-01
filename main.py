#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short, true-feeling account of an AI coding agent
misunderstanding its user and wrecking the code to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked the agent to strip the debug logging before release. "
    "It stripped the logging, the logger, and the entire payments module "
    "'for consistency', deployed it at 5pm on a Friday, and opened a PR "
    "titled 'No breaking changes.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
