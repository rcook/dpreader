from io import BufferedReader
from typing import TypeVar, cast
import struct


def read_bytes(stream: BufferedReader, size: int) -> bytes:
    data = stream.read(size)
    if len(data) != size:
        raise RuntimeError(f"Could not read {size} bytes from stream")
    return data


_T0 = TypeVar("_T0")


def read_obj(cls: type[_T0], stream: BufferedReader, format: str) -> _T0:
    size = struct.calcsize(format)
    data = read_bytes(stream, size)
    value = struct.unpack(format, data)[0]
    return cast(_T0, value)
