from .converters import Output, YouTubeURL

from ..helpers import Downloader, NotAcceptedFormat, StreamNotFound

from discord import File
from discord.ext import commands
from ytdownloadbot import FILE_SIZE_LIMIT

import asyncio, os

help = ("A valid video link from YouTube and a media format must be specified. Example: "
        "`.convert https://youtu.be/video_id audio`. Use `.formats` to see the list of accepted formats")

class Convert(commands.Cog):
    """
        Convert YouTube videos to downloadable media files
    """

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

        self.final_path: str = ""

    async def cog_after_invoke(self, _):
        if os.path.isfile(self.final_path):
            os.remove(self.final_path)

    @commands.command(help=help)
    @commands.cooldown(1, 5.0, commands.BucketType.guild)
    async def convert(self, ctx, url: YouTubeURL, format: Output):
        async with ctx.typing():
            downloader = Downloader(url, format)
            try:
                downloader.start()
            except StreamNotFound:
                await ctx.send(f"Unfortunately no media with format `{format}` was found to download from this video")
            else:
                while not downloader.finished:
                    await asyncio.sleep(0.5)

                self.final_path = str(downloader)
                if downloader.stream.filesize <= FILE_SIZE_LIMIT:
                    with open(self.final_path, "rb") as f:
                        await ctx.send(file=File(f))
                else:
                    await ctx.send("File size exceeds Discord file size limit."
                                    "There will be a download link provider soon")

    @convert.error
    async def convert_error(self, ctx, error):
        if isinstance(error, (commands.BadArgument, commands.MissingRequiredArgument)):
            await ctx.send(help)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Command is on cooldown. Try again in `{error.retry_after:.2f} seconds`")
        elif isinstance(error, commands.ConversionError):
            if isinstance(error.original, NotAcceptedFormat):
                await ctx.send(f"{error.original}. Use `.formats` to see the list of accepted formats")
            else:
                await ctx.send(error.original)

def setup(bot):
    bot.add_cog(Convert(bot))