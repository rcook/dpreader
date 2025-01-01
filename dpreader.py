from argparse import ArgumentParser
from dpreaderlib.arg_types import nonnegative_int, path, positive_int
from dpreaderlib.decode import decode
from dpreaderlib.dump import DEFAULT_COLUMNS, dump
from functools import partial
from pathlib import Path
import sys


def main(cwd: Path, argv: list[str]):
    this_path = partial(path, cwd)

    parser = ArgumentParser(prog="dpreader")
    parsers = parser.add_subparsers(required=True)

    p = parsers.add_parser(name="decode")
    p.add_argument("path", type=this_path)
    p.set_defaults(func=lambda args: decode(path=args.path))

    p = parsers.add_parser(name="dump")
    p.add_argument("path", type=this_path)
    p.add_argument("--start", type=nonnegative_int, default=0)
    p.add_argument("--count", type=nonnegative_int, default=None)
    p.add_argument("--columns", type=positive_int, default=DEFAULT_COLUMNS)
    p.set_defaults(
        func=lambda args: dump(
            path=args.path,
            start=args.start,
            count=args.count,
            columns=args.columns))

    args = parser.parse_args(argv)
    args.func(args=args)


if __name__ == "__main__":
    main(cwd=Path.cwd(), argv=sys.argv[1:])
