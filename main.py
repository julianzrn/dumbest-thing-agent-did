"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

DELETION = "Today my agent deleted the folder called 'final_final_v3' "
MOTIVE = "to reduce clutter, then restored it from a backup "
TWIST = "it had also deleted."

ENTRY = DELETION + MOTIVE + TWIST

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
