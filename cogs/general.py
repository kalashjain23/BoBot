from discord.ext import commands


class General(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"BoBot is online.")


def setup(bot):
    bot.add_cog(General(bot))
