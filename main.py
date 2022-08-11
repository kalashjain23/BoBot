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

    print(f"Logged in as {bot.user}.")
    guild_count = 0
    for guild in bot.guilds:
        guild_count += 1
        print(f"-{guild.id} (name: {guild.name})")
    print(f"I'm present in {guild_count} servers!!")


@bot.event
async def on_member_join(member):
    guild = bot.get_guild(995037483093983383)
    channel = guild.get_channel(1007165957996818482)
    embed = discord.Embed(title="Welcome to the server!", color=0x00FFFF)
    embed.add_field(name=f'Glad to have you here :smile: !!', value=f'Now we have {guild.member_count} members! :partying_face:')
    await channel.send(f'Ayoo! {member.mention} just joined in!!')
    await channel.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("DISCORD_TOKEN"))
