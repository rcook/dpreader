from pathlib import Path


def nonnegative_int(s: str) -> int:
    value = int(s)
    if value < 0:
        raise ValueError("Value {s} must be a nonnegative int")
    return value


def positive_int(s: str) -> int:
    value = int(s)
    if value <= 0:
        raise ValueError("Value {s} must be a positive int")
    return value


def path(cwd: Path, s: str) -> Path:
    return (cwd / Path(s).expanduser()).resolve()
