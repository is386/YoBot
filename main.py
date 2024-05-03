import asyncio
import discord
import random

from discord.ext import commands
from env import TOKEN
from schedule_cog import ScheduleCog

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description='Tyrese Maxey', intents=intents)

async def main():
  async with bot:
    await bot.add_cog(ScheduleCog(bot))
    await bot.start(TOKEN)

asyncio.run(main())