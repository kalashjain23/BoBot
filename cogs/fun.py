import discord
import requests
from discord.ext import commands


def work():
    url = "http://www.boredapi.com/api/activity/"
    json = (requests.get(url=url)).json()

    return json['activity']


class Fun(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='bored')
    async def bored(self, message):
        work_list = [f'- {work()}' for i in range(5)]
        embed = discord.Embed(title="Looks like you're bored!", color=0x98FB98)
        embed.add_field(name="Tasks that you can do:", value="\n".join(work_list), inline=False)

        await message.channel.send(embed=embed)

    @commands.command(name='lyrics')
    async def lyrics(self, ctx, *, args):
        url = f'https://api.popcat.xyz/lyrics?song={args}'
        response = requests.get(url=url).json()
        try:
            lyrics = response['lyrics']
            embed = discord.Embed(title=f'{args.title()}', description=f"By {response['artist']}\n{lyrics}", color=0x00FFFF)
            embed.set_thumbnail(url=response['image'])
            embed.set_footer(text="Enjoy the music!")
            await ctx.channel.send(embed=embed)
        except KeyError:
            embed = discord.Embed(title=f'Invalid!', description=f"Sorry, don't have lyrics for that :<", color=0x00FFFF)
            embed.set_footer(text='Try again with another song..')
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
