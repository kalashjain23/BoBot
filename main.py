import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    guild_count = 0
    for guild in bot.guilds:
        print(f"-{guild.id} (name:{guild.name})")
        guild_count += 1

    print(f"BoBot is in {guild_count} guilds.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("bo"):
        msg = message.content.split("bo ", 1)[1]

        if msg == 'hello':
            await message.channel.send("Sup Bobo *wink* *wink*")
    return

bot.run(DISCORD_TOKEN)
