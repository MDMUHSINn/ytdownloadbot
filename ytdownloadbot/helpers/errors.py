from typing import Optional


class DownloaderFinished(Exception):
    """Raised when Downloader instance is already finished"""


class InvalidURL(Exception):
    """Raised when URL is not compatible with YouTube URL format"""


class NotAcceptedFormat(Exception):
    """Raised when format is not accepted"""
    @staticmethod
    def message(format: Optional[str] = None) -> str:
        return (f"{format if format is not None else 'The specified format'}"
                " is not one of the accepted formats")


class StreamNotFound(Exception):
    """Raised when no Stream is found on filtering"""
