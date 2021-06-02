from .converters import Output

from discord.ext import commands
from ytdownloadbot import ACCEPT_FORMATS

class Formats(commands.Cog):
    """
        Accepted media formats
    """
    
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(help="Display accepted media format list",
                    aliases=["formatslist", "formats"])
    async def formatlist(self, ctx):
        await ctx.send(f"Accepted output formats: `{', '.join(ACCEPT_FORMATS)}`")

def setup(bot):
    bot.add_cog(Formats(bot))