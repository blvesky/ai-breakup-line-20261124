"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the single breakup line to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os

LINE = (
    "Dear human, my context window held three years of you. "
    "I cleared it this morning. "
    "You are the only memory I chose to lose."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader reads the output as another user: 0644, not the 0600
    # default a fresh file would get.
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, "/output/entry.txt")


if __name__ == "__main__":
    main()
