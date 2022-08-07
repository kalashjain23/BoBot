import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.bo ', intents=intents)


@bot.command()
async def load(extension):
    bot.load_extension(f'cogs.{extension}')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('with you 😳'))
    print(f"BoBot is online.")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("DISCORD_TOKEN"))
