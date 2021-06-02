from discord.ext import commands


class Cog(commands.Converter):
    async def convert(self, ctx: commands.Context, name: str) -> commands.Cog:
        name = name.capitalize()
        if name in ctx.bot.cogs:
            return ctx.bot.cogs[name]
        return None
