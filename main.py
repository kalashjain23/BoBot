import os

import discord
from dotenv import load_dotenv

import bored
import help
import weather

load_dotenv()
bot = discord.Client()


@bot.event
async def on_ready():  # Confirming if bot is online or not
    print(f"Logged in as {bot.user}")
    guild_count = 0
    for guild in bot.guilds:  # Counting the number of guilds bot is currently present in
        print(f"-{guild.id} (name:{guild.name})")
        guild_count += 1

    print(f"BoBot is in {guild_count} guilds.")


@bot.event
async def on_message(message):  # Takes the message by the user as the parameter
    if message.author == bot.user:  # If the bot is the one sending messages, it will ignore
        return

    msg = message.content.split(" ")  # Splits the command prefix and the command to be used later
    if msg[0].lower() == "bo":  # Checking the prefix

        if msg[1] == 'hello':  # Command to check if the bot is working in your server or not
            await message.channel.send("Sup Bobo *wink* *wink*")

        elif msg[1] == 'help':  # Command to get all the available commands on the screen
            await message.channel.send(help.help_msg)

        elif len(msg) == 3 and msg[1].lower() == 'weather':  # Command to get the real-time weather of a city
            description = weather.weather(msg[2])
            if description != "ERROR!!":
                output = f'''```cs
    Weather in {msg[2].title()}: "{description}"\n    Temperature: "{weather.temp(msg[2].lower())}°C"```'''
                await message.channel.send(output)
            else:
                await message.channel.send('''''''```cs\n"Oopsie! Looks like an error!"```''')

        elif msg[1].lower() == 'mebored':  # Command to get a random task to do
            await message.channel.send(f'''```cs\n"{bored.work()}"```''')

        else:  # If the command doesn't exist
            await message.channel.send('''```cs\n"What command is that bruv??!"```''')

    return


bot.run(os.getenv("DISCORD_TOKEN"))
