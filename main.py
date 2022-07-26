import discord
import os
import weather, bored
from dotenv import load_dotenv
import help

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild_count = 0
    for guild in bot.guilds:
        print(f"-{guild.id} (name:{guild.name})")
        guild_count += 1

    print(f"BoBot is in {guild_count} guilds.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "bo help":
        await message.channel.send(help.help_msg)

    if message.content.startswith("bo"):
        msg = message.content.split(" ")

        if msg[1] == 'hello':
            await message.channel.send("Sup Bobo *wink* *wink*")

        if len(msg) == 3 and msg[1] == 'weather':
            description = weather.weather(msg[2])
            if description != "ERROR!!":
                output = f'''```cs
    Weather in {msg[2].title()}: "{description}"\n    Temperature: "{weather.temp(msg[2])}°C"```'''
                await message.channel.send(output)

            else:
                await message.channel.send('''''''```cs\n"Oopsie! Looks like an error!"```''')

        if msg[1] == 'mebored':
            await message.channel.send(bored.work())

    return


bot.run(DISCORD_TOKEN)
