from pathlib import Path


COLUMNS: int = 16
PLACEHOLDER: str = "."


def dump(path: Path, columns: int = COLUMNS, placeholder: str = PLACEHOLDER) -> None:
    with path.open("rb") as f:
        col = 0
        s = ""
        for i, b in zip(range(0, 256), f.read()):
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
