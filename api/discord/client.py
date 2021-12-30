import discord
from discord.ext import commands


from api.discord.commands.first import First
from api.discord.commands.listeners import Listeners

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.add_cog(First(bot))
bot.add_cog(Listeners(bot))
