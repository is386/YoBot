import datetime

from discord import Embed
from discord.ext import commands, tasks
from env import CHANNEL_ID, SCHEDULE_HOUR, SCHEDULE_MINUTE, TZ_IDENTIFIER, YO_EMOJI, NO_EMOJI
from zoneinfo import ZoneInfo

time = datetime.time(hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE, tzinfo=ZoneInfo(TZ_IDENTIFIER))

def check_reaction(reaction, user):
    return str(reaction.emoji) in [YO_EMOJI, NO_EMOJI]

class ScheduleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        channel = self.bot.get_channel(CHANNEL_ID)

        message = await channel.send(embed=Embed(title="Yo or No?", color=0x006BB6))
        await message.add_reaction(YO_EMOJI)
        await message.add_reaction(NO_EMOJI)

        reaction_count = 0
        while True:
            reaction, user = await self.bot.wait_for('reaction_add', check=check_reaction)
            
            if str(reaction.emoji) == NO_EMOJI:
                await channel.send("@everyone thats gonna be a **NO** from me")
                break
            elif str(reaction.emoji) == YO_EMOJI:
                reaction_count += 1

            if reaction_count == 3:
                await channel.send("@everyone **YO**, hop on voice chat")
                break