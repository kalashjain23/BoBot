from discord.ext import commands
from APIs import kawai_api


class Kawaii(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
        self.url = None

    @commands.command(name='hug')
    async def hug(self, message):
        self.url = kawai_api.get_response('hug')
        await message.channel.send(f'{self.url}')

    @commands.command(name='blush')
    async def blush(self, message):
        self.url = kawai_api.get_response('blush')
        await message.channel.send(f'{self.url}')

    @commands.command(name='cuddle')
    async def cuddle(self, message):
        self.url = kawai_api.get_response('cuddle')
        await message.channel.send(f'{self.url}')

    @commands.command(name='dance')
    async def dance(self, message):
        self.url = kawai_api.get_response('dance')
        await message.channel.send(f'{self.url}')


def setup(bot):
    bot.add_cog(Kawaii(bot))
