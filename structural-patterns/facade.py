from abc import ABC
from dataclasses import dataclass
from typing import Literal, Any


# 3-rd party library classes

@dataclass(kw_only=True)
class File(ABC):
    filename: str = None
    buffer: Any = None

    def save(self):
        print(f'Saving file {self.filename}')


class VideoFile(File): ...


@dataclass
class Codec(ABC): ...


class CodecFactory:
    @staticmethod
    def extract(file: File) -> Codec:
        format = file.filename.split('.')[-1]

        match format:
            case 'mp4': return MPEG4CompressionCodec()
            case 'ogg': return OggCompressionCodec()
            case _: raise Exception('Unsupported codec passed')


class OggCompressionCodec(Codec): ...


class MPEG4CompressionCodec(Codec): ...


class BitrateReader:
    @staticmethod
    def read(filename: str, codec: Codec):
        print(f'Reading bitrate from {filename}')
        # ... return buffer

    @staticmethod
    def convert(buffer, codec: Codec):
        print(f'Converting bitrate to {codec}')
        # ... return converted buffer


# Facade class
class VideoConverter:
    @staticmethod
    def convert(filename: str, format: Literal['mp4', 'ogg']) -> File:
        file = VideoFile(filename=filename)
        source_codec = CodecFactory.extract(file)

        match format:
            case 'mp4': dest_codec = MPEG4CompressionCodec()
            case 'ogg': dest_codec = OggCompressionCodec()
            case _: raise Exception('Unsupported codec format passed')

        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, dest_codec)

        new_filename = f'{''.join(filename.split('.')[:-1])}.{format}'

        return File(filename=new_filename, buffer=result)


def main(filename: str, format: Literal['mp4', 'ogg']) -> None:
    mp4 = VideoConverter.convert(filename, format)
    mp4.save()

if __name__ == '__main__':
    main('vid.ogg', 'mp4')
    '''
    Reading bitrate from vid.ogg
    Converting bitrate to MPEG4CompressionCodec()
    Saving file vid.mp4
    '''

    main('vid.mp4', 'ogg')
    '''
    Reading bitrate from vid.mp4
    Converting bitrate to OggCompressionCodec()
    Saving file vid.ogg
    '''
