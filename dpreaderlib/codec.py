from abc import ABC, abstractmethod
from dataclasses import dataclass
from dpreaderlib.stream import Stream
from math import floor
import struct


@dataclass(frozen=True)
class Codec(ABC):
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def sample_width(self) -> int: raise NotImplementedError()

    @abstractmethod
    def encode(self, stream: Stream) -> bytes: raise NotImplementedError()


class U8Codec(Codec):
    @property
    def sample_width(self) -> int:
        return 1

    def encode(self, stream: Stream) -> bytes:
        bs = bytearray()
        for sample in stream:
            b = round((sample + 1.0) / 2.0 * 255.0)
            bs.append(b)
        return bytes(bs)


class S16LECodec(Codec):
    @property
    def sample_width(self) -> int:
        return 2

    def encode(self, stream: Stream) -> bytes:
        bs = bytearray()
        for sample in stream:
            b = floor(sample * 32768.0)
            bs.extend(struct.pack("<h", b))
        return bytes(bs)
