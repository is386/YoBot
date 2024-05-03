import datetime

from discord import Embed
from discord.ext import commands, tasks
from env import CHANNEL_ID, SCHEDULE_HOUR, SCHEDULE_MINUTE, TZ_IDENTIFIER, YO_EMOJI, NO_EMOJI
from zoneinfo import ZoneInfo

time = datetime.time(hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, tzinfo=ZoneInfo(TZ_IDENTIFIER))

class ScheduleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        embed = Embed(title="Yo or No?", color=0x006BB6)
        channel = self.bot.get_channel(CHANNEL_ID)
        message = await channel.send(embed=embed)
        await message.add_reaction(YO_EMOJI)
        await message.add_reaction(NO_EMOJI)