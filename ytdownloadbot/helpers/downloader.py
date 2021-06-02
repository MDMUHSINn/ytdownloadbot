from .errors import DownloaderFinished, NotAcceptedFormat, StreamNotFound

from moviepy.audio.io.AudioFileClip import AudioFileClip
from typing import Any, BinaryIO, Optional
from pytube import Stream, YouTube


class Downloader(YouTube):
    def __init__(self, url: str, format: str):
        super().__init__(
            url,
            on_complete_callback=lambda *args: self.complete_callback(*args)
        )

        self._stream: Stream = None

        self._finished: bool = False

        self.url: str = url
        self.format: str = format
        self.output: str = ""

    @property
    def finished(self):
        return self._finished

    @property
    def stream(self):
        return self._stream

    def complete_callback(self, stream: Any, file_path: str):
        self.output = file_path
        self._stream = stream

        if stream.includes_audio_track and not stream.includes_video_track:
            output = f"{file_path[:-4]}.mp3"
            with AudioFileClip(file_path) as sound:
                sound.write_audiofile(output)

            self.output = output

        self._finished = True

    def filter_by_format(self, format: str) -> "Stream":
        if format == "audio":
            return self.streams.get_audio_only()
        elif format == "video":
            return self.streams.get_highest_resolution()
        elif format in ("mp3", "mp4"):
            query = self.streams.filter(file_extension=format)

            if format == "mp3":
                stream = query.get_audio_only()
            else:
                stream = query.get_highest_resolution()
            if stream is not None:
                return stream

            raise StreamNotFound()
        raise NotAcceptedFormat()

    def start(self, buffer: Optional[BinaryIO] = None):
        if not self.finished:
            stream = self.filter_by_format(self.format.lower())

            if buffer is not None:
                stream.stream_to_buffer(buffer)
            else:
                stream.download()
        else:
            raise DownloaderFinished()

    def __str__(self) -> str:
        return self.output
