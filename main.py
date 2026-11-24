#!/usr/bin/env python3
"""Write one single-sentence horror line to /output/entry.txt.

v2 (revised from v1): the draft was past tense and reported the scare
once, then stopped. The revision moves it into the present tense so
the dread is still happening ("Every night ... shows"), adds a
concrete time anchor ("empty since Tuesday") so the horror has a
history, and replaces the passive "was humming" with "has learned
his lullaby" — the thing in the wall is not just making a sound, it
is studying the child, and the imitation is the scare that outlasts
the line. The last word still lands the blow.
"""

from pathlib import Path

TEXT = (
    "Every night the baby monitor shows my son asleep, but his crib "
    "has been empty since Tuesday, and something small inside the "
    "wall has learned his lullaby."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
