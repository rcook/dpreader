from dpreaderlib.header import Header
from dpreaderlib.value_reader import ValueReader
from pathlib import Path


def decode(path: Path) -> None:
    with ValueReader.open(path) as f:
        header = Header.decode(f)
        print(header.title)
        for i in range(0, 4):
            name = f"blob{i}"
            blob = getattr(header, name)
            print(f"  {name}: {blob.hex(sep=' ')}")
