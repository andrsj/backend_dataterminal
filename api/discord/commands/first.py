from discord.ext.commands import Cog, Context
from discord.ext import commands


class First(Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx: Context):
        """Simple Greeting command"""
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
