from dpreaderlib.utils import indices
from os import SEEK_SET
from pathlib import Path


DEFAULT_COLUMNS: int = 16
DEFAULT_PLACEHOLDER: str = "."


def dump(path: Path, start: int = 0, count: int | None = None, columns: int = DEFAULT_COLUMNS, placeholder: str = DEFAULT_PLACEHOLDER) -> None:
    with path.open("rb") as f:
        f.seek(start, SEEK_SET)
        col = 0
        s = ""
        for i, b in zip(indices(start, count), f.read()):
            if col == 0:
                print(f"{i:08X} ", end="")

            c = chr(b)
            s += c if c.isprintable() else placeholder
            print(f" {b:02X}", end="")

            col += 1
            if col >= columns:
                print(f"  {s}")
                col = 0
                s = ""

    if col > 0:
        print("   " * (columns - col), end="")
        print(f"  {s}")
