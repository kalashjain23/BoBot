import discord
from discord.ext import commands

import bored


class Fun(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='bored')
    async def bored(self, message):
        await message.channel.send(f'''```cs\n"{bored.work()}"```''')

    @commands.command(name="hello")
    async def hello(self, message):  # Takes the message by the user as the parameter
        if message.author == commands.bot:  # If the bot is the one sending messages, it will ignore
            return
        await message.channel.send("Sup BoBo *wink* *wink*")


def setup(bot):
    bot.add_cog(Fun(bot))
