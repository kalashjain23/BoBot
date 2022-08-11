import discord
import requests
from discord.ext import commands


class PopCat(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='lyrics')
    async def lyrics(self, ctx, *, args):
        url = f'https://api.popcat.xyz/lyrics?song={args}'
        response = requests.get(url=url).json()
        lyrics = response['lyrics']
        embed = discord.Embed(title=f'{args.title()}', description=f"By {response['artist']}\n{lyrics}", color=0x00FFFF)
        embed.set_thumbnail(url=response['image'])
        embed.set_footer(text="Enjoy the music!")
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(PopCat(bot))
