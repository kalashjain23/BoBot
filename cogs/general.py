import discord
from discord.ext import commands


class General(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Lack of Permissions!", color=0xDC143C)
            embed.add_field(name="Manage messages permission required", value="Ask the admins for the power!")
            
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
