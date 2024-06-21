import datetime

from asyncio import TimeoutError
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

        reacted_users = set()
        while True:
            try: 
                reaction, user = await self.bot.wait_for('reaction_add', check=check_reaction, timeout=5400.0)

                if str(reaction.emoji) == NO_EMOJI or str(reaction.emoji) == YO_EMOJI:
                    await channel.send("**%s:** %s" % (user, str(reaction.emoji)))
                    reacted_users.add(user)

                if len(reacted_users) == 3:
                    break

            except TimeoutError:
                break
