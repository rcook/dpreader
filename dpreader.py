from argparse import ArgumentParser
from dpreaderlib.decode import decode
from dpreaderlib.dump import dump
from pathlib import Path
import sys


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
