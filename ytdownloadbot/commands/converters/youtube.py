from discord.ext import commands
from ytdownloadbot import VALID_URLS

from ...helpers import InvalidURL

class YouTubeURL(commands.Converter):
    async def convert(self, _, url: str) -> str:
        if not any(_url in url for _url in VALID_URLS):
            valid = " or ".join((f"`{url}`" for url in VALID_URLS))
            raise InvalidURL(f"Invalid YouTube URL. Expected: {valid}")
        return f"https://{url}" if not url.startswith("http") else url