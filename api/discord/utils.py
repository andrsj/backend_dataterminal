from typing import Optional


from discord import Guild, Member


from api.discord.client import bot


async def send_message(message, channel_id):
    channel = bot.get_channel(channel_id)
    await channel.send(message)
    return channel


def get_guild_member_by_id(user_id: str, guild: Guild) -> Optional[Member]:
    users = [m for m in guild.members if m.id == int(user_id)]
    return users[0] if users else None
