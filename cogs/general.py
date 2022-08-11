import discord
from discord.ext import commands


class General(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, message):  # Takes the message by the user as the parameter
        if message.author == commands.bot:  # If the bot is the one sending messages, it will ignore
            return
        embed = discord.Embed(title="Sup BoBo *wink* *wink*", color=0xFF69B4)
        await message.channel.send(embed=embed)

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Lack of Permissions!", color=0xDC143C)
            embed.add_field(name="Manage messages permission required", value="Ask the admins for the power!")
            
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
