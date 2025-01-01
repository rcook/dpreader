from dpreaderlib.codec import Codec, S16LECodec, U8Codec
from dpreaderlib.stream import Stream
from enum import Enum


class Encoding(Enum):
    _codec: Codec

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, codec_type: type[Codec]):
        self._codec = codec_type()

    @property
    def sample_width(self) -> int:
        return self._codec.sample_width

    def encode(self, stream: Stream) -> bytes:
        return self._codec.encode(stream)

    U8 = U8Codec
    S16LE = S16LECodec
