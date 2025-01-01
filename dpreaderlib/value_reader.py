from dpreaderlib.helpers import read_bytes, read_obj
from io import BufferedReader
from pathlib import Path
from types import TracebackType
from typing import Any, TypeVar


_T0 = TypeVar("_T0", bound="ValueReader")


class ValueReader:
    _stream: BufferedReader

    @classmethod
    def open(cls: type[_T0], path: Path) -> _T0:
        stream = path.open("rb")
        return cls(stream=stream)

    def __init__(self, stream: BufferedReader) -> None:
        self._stream = stream

    def __enter__(self):
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        if not self._stream.closed:
            self._stream.close()

    def read_bytes(self, size: int) -> bytes:
        return read_bytes(self._stream, size)

    def read_int_be(self) -> int:
        return read_obj(int, self._stream, ">I")

    def read_ascii(self, size: int) -> str:
        return self.read_bytes(size).decode("ascii")

    def expect_bytes(self, expected: list[int]) -> None:
        def values_equal(p: tuple[Any, Any]) -> bool:
            return p[0] == p[1]
        values = self.read_bytes(len(expected))
        assert all(map(values_equal, zip(expected, values)))

    def expect_int_be(self, expected: int) -> None:
        value = self.read_int_be()
        assert value == expected

    def expect_ascii(self, expected: str) -> None:
        value = self.read_ascii(len(expected))
        assert value == expected

    def skip_bytes(self, size: int) -> None:
        read_bytes(self._stream, size)
