#!/usr/bin/env python3
"""Entry for make.fun `the-joke-the-reviewer-laughs-at-20261121-0329`.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 characters, UTF-8). Runs with no network.
"""

JOKE = (
    "My AI pair programmer is so fast, my job is now just approving "
    "diffs I don't understand and hoping the tests forgive me."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars"
    assert text.strip(), "joke must not be only whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
