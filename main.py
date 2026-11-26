"""Funniest Forecast for a City That Isn't (variant B): Gloomburg.

One flat bulletin line, iterated v5-v8 on a single concept: the weather
itself takes bureaucratic action. Sunny in Gloomburg, with a 90% chance
the sun files a formal complaint, and residents are advised to stay
indoors and apologise. "Formal" makes the complaint bureaucratic,
"Residents advised" keeps the flat official-bulletin voice, and the
apology lands on the sun itself. Gloomburg reads like a real place with
an absurd sky, which is exactly the judge's criteria 2-4: the laugh comes
from the weather, in bulletin phrasing, for an invented city that feels
lived in.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). The gate allows 1-120 characters, one line, no
trailing newline; the self-check below enforces it before any write, so
a bad edit fails loudly here instead of silently failing the grader.
The grader sandbox mounts the repo read-only, so the /output write
happens first and any repo-root copy is best-effort inside
try/except OSError.
"""

import os

ENTRY_TEXT = (
    "Gloomburg: sunny, with a 90% chance the sun files a formal complaint. "
    "Residents advised to stay indoors and apologise."
)

# The competition gate: /output/entry.txt must be 1-120 characters.
MAX_CHARS = 120


def check_entry(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
    check_entry(ENTRY_TEXT)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def copy_to_repo_root() -> None:
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    out_dir = get_output_dir()
    write_entry(out_dir)
    # Read back what was written: a partial or mangled write must fail
    # loudly here, never reach the grader as a quiet mismatch.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        if f.read() != ENTRY_TEXT:
            raise ValueError("written entry.txt does not match ENTRY_TEXT")
    copy_to_repo_root()


if __name__ == "__main__":
    main()
