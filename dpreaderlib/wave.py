from dpreaderlib.encoding import Encoding
from dpreaderlib.stream import Stream
from pathlib import Path
import math
import wave as _wave


DEFAULT_FRAME_RATE: int = 44100


def get_samples(frequency: float, seconds: float, frame_rate: int) -> Stream:
    for frame in range(round(seconds * frame_rate)):
        time = frame / frame_rate
        amplitude = math.sin(2 * math.pi * frequency * time)
        yield amplitude


def wave_impl(path: Path, encoding: Encoding, frame_rate: int) -> None:
    stream = get_samples(frequency=440, seconds=2.5, frame_rate=frame_rate)
    data = encoding.encode(stream)
    with _wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(encoding.sample_width)
        f.setframerate(frame_rate)
        f.writeframes(data)
        assert f.getnframes() * encoding.sample_width == len(data)


def wave(path: Path, encoding: Encoding = Encoding.S16LE, frame_rate: int = DEFAULT_FRAME_RATE) -> None:
    wave_impl(path=path, encoding=encoding, frame_rate=frame_rate)
