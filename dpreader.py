from argparse import ArgumentParser
from dpreader.header import Header
from dpreader.utils import dump
from dpreader.value_reader import ValueReader
from pathlib import Path
import sys


def decode(path: Path) -> None:
    with ValueReader.open(path) as f:
        header = Header.decode(f)
        print(header.title)
        for i in range(0, 4):
            name = f"blob{i}"
            blob = getattr(header, name)
            print(f"  {name}: {blob.hex(sep=' ')}")


def main(cwd: Path, argv: list[str]):
    def path_type(s: str) -> Path:
        return (cwd / Path(s)).resolve()
    parser = ArgumentParser(prog="dpreader")
    parsers = parser.add_subparsers(required=True)

    p = parsers.add_parser(name="decode")
    p.add_argument("path", type=path_type)
    p.set_defaults(func=lambda args: decode(path=args.path))

    p = parsers.add_parser(name="dump")
    p.add_argument("path", type=path_type)
    p.set_defaults(func=lambda args: dump(path=args.path))

    args = parser.parse_args(argv)
    args.func(args=args)


if __name__ == "__main__":
    main(cwd=Path.cwd(), argv=sys.argv[1:])
