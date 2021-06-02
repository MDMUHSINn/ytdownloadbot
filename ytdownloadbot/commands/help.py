from .converters import Cog

from discord.errors import Forbidden
from discord.ext import commands

from discord import Color, Embed
from typing import Optional

class Help(commands.Cog):
    """
        Send this help message
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    async def send_embed(self, ctx, embed):
        try:
            await ctx.send(embed=embed)
        except Forbidden:
            try:
                await ctx.send("I need permissions to send embeds")
            except Forbidden:
                await ctx.author.send(
                    f"I need permissions to send messages in channel `{ctx.channel.name}` "
                    f"of guild `{ctx.guild.name}`", embed=embed)

    @commands.command()
    async def help(self, ctx, cog: Optional[Cog] = None):
        prefix = self.bot.command_prefix
        embed = Embed(title=f"Command list. Prefix: `{prefix}`", color=Color.blue(),
                    description=f"Use `{prefix} <category>` to get more information "
                                "about a specific category")

        if cog is None:
            cogs_desc = "\n".join(
                (f"`{cog}` {self.bot.cogs[cog].__doc__}" for cog in self.bot.cogs)
            )

            embed.add_field(name="Categories", value=cogs_desc, inline=False)
        else:
            embed = Embed(title=f"{cog.qualified_name} - Commands", color=Color.dark_blue(),
                    description=cog.__doc__)

            for command in cog.get_commands():
                if not command.hidden:
                    if command.aliases:
                        aliases = " or {}".format(" or ".join((f"`{prefix}{alias}`" for alias in command.aliases)))
                    else:
                        aliases = ""

                    embed.add_field(name = f"`{prefix}{command.name}`{aliases}",
                                    value=command.help, inline=False)

        await self.send_embed(ctx, embed)

def setup(bot):
    bot.add_cog(Help(bot))