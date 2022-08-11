import discord
from discord.ext import commands
from APIs import kawai_api


class Gifs(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
        self.url = None

    @commands.command(name='hug')
    async def hug(self, ctx, args=None):
        if ctx.author.name == ctx.message.mentions[0].name:
            await ctx.channel.send(f"Don't worry, you're not alone :pleading_face:")
        elif args is not None:
            self.url = kawai_api.get_response('hug')
            embed = discord.Embed(color=0x00FFFF)
            embed.set_image(url=self.url)
            await ctx.channel.send(f'**{ctx.author.name}** hugs **{ctx.message.mentions[0].name}** :flushed:', embed=embed)
        else:
            embed = discord.Embed(color=0x00FFFF)
            embed.set_author(name=f'OK but hug who?? :<<')
            await ctx.channel.send(embed=embed)

    @commands.command(name='blush')
    async def blush(self, ctx):
        self.url = kawai_api.get_response('blush')
        embed = discord.Embed(color=0x00FFFF)
        embed.set_image(url=self.url)
        await ctx.channel.send(f"**{ctx.author.name}'s** blushing :flushed:", embed=embed)

    @commands.command(name='cuddle')
    async def cuddle(self, ctx, args=None):
        if ctx.author.name == ctx.message.mentions[0].name:
            await ctx.channel.send(f"Don't worry, you're not alone :pleading_face:")
        elif args is not None:
            self.url = kawai_api.get_response('cuddle')
            embed = discord.Embed(color=0x00FFFF)
            embed.set_image(url=self.url)
            await ctx.channel.send(f'**{ctx.author.name}** cuddles **{ctx.message.mentions[0].name}** :pleading_face:', embed=embed)
        else:
            embed = discord.Embed(color=0x00FFFF)
            embed.set_author(name=f'OK but cuddle who?? :<<')
            await ctx.channel.send(embed=embed)

    @commands.command(name='dance')
    async def dance(self, ctx):
        self.url = kawai_api.get_response('dance')
        embed = discord.Embed(color=0x00FFFF)
        embed.set_image(url=self.url)
        await ctx.channel.send(f"Ayyoo, **{ctx.author.name}** got da moves! :flushed:", embed=embed)


def setup(bot):
    bot.add_cog(Gifs(bot))
