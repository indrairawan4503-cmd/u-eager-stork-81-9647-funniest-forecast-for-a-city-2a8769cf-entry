"""Funniest Forecast for a City That Isn't (variant B): Gloomburg.

One flat bulletin line: sunny in Gloomburg, with a 90% chance the sun files
a formal complaint, and residents advised to stay indoors and apologise.
Iterated v5-v8 on this one concept: "formal" makes the complaint
bureaucratic, "Residents advised" keeps the official-bulletin voice, and
the apology lands on the sun itself.

Writes exactly one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The grader sandbox mounts the repo read-only, so the /output write happens
first and any repo-root copy is best-effort inside try/except OSError.
"""

import os

ENTRY_TEXT = (
    "Gloomburg: sunny, with a 90% chance the sun files a formal complaint. "
    "Residents advised to stay indoors and apologise."
)


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
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
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
