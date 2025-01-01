from dataclasses import dataclass
from dpreaderlib.value_reader import ValueReader
from typing import TypeVar


_T0 = TypeVar("_T0", bound="Header")


@dataclass(frozen=True)
class Header:
    blob0: bytes
    blob1: bytes
    blob2: bytes
    title: str
    blob3: bytes

    @classmethod
    def decode(cls: type[_T0], f: ValueReader) -> _T0:
        f.expect_int_be(0x04071324)
        f.expect_bytes([0x00])
        blob0 = f.read_bytes(3)
        f.expect_bytes([0x00])
        blob1 = f.read_bytes(3)
        f.expect_bytes([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00])
        blob2 = f.read_bytes(4)
        title = f.read_ascii(8).rstrip()
        f.expect_bytes([0x00] * 6)
        f.expect_bytes([0x00, 0x02] * 4 + [0x00])
        blob3 = f.read_bytes(1)
        f.expect_bytes([0x00] * 6)
        f.expect_bytes([0x08])
        f.expect_bytes([0x00] * 4)
        f.expect_bytes([0x03])
        f.expect_ascii("CONT")
        f.expect_bytes([0x00] * 12)
        f.expect_bytes([0x00, 0x10])
        f.expect_bytes([0x00] * 2)
        f.expect_bytes([0x00] * 4)
        f.expect_ascii("MTR_FILE")
        f.expect_bytes([0x00] * 4)
        f.expect_bytes([0x00] * 6)
        f.expect_bytes([0xa0, 0x8c])
        f.expect_bytes([0x00] * 4)
        f.expect_ascii("MIS_FILE")
        f.expect_bytes([0x00] * 8)
        return cls(
            blob0=blob0,
            blob1=blob1,
            blob2=blob2,
            title=title,
            blob3=blob3)
