import discord
from discord.ext import commands

from APIs import bored


class Fun(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='bored')
    async def bored(self, message):
        embed = discord.Embed(title="Looks like you're bored!", color=0x98FB98)
        embed.add_field(name="Tasks that you can do:", value=f"- {bored.work()}\n- {bored.work()}\n- {bored.work()}\n- {bored.work()}\n- {bored.work()}", inline=False)

        await message.channel.send(embed=embed)

    @commands.command(name="hello")
    async def hello(self, message):  # Takes the message by the user as the parameter
        if message.author == commands.bot:  # If the bot is the one sending messages, it will ignore
            return
        embed = discord.Embed(title="Sup BoBo *wink* *wink*", color=0xFF69B4)
        await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
