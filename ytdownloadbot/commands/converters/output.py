from discord.ext import commands
from ytdownloadbot import ACCEPT_FORMATS

from ...helpers import NotAcceptedFormat

class Output(commands.Converter):
    async def convert(self, _, format: str) -> str:
        format = format.replace(".", "")
        if format not in ACCEPT_FORMATS:
            raise NotAcceptedFormat(NotAcceptedFormat.message(f"`{format}`"))
        return format