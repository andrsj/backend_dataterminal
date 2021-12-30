from datetime import datetime


from discord.ext.commands import Cog, Context


class Listeners(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} has connected to Discord! by Bot Event")

    @Cog.listener()
    async def on_command(self, ctx: Context):
        print(
            f"{datetime.now().strftime('%H:%M:%S %d/%m/%Y')} "
            f'{ctx.bot.user.name} '
            f'\'{ctx.channel}\' '
            f'{ctx.author} '
            f'\'{ctx.message.content}\''
        )
