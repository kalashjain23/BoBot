import discord
from discord.ext import commands

from APIs import weather


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather')
    async def weather(self, message, *, city):
        self.description = weather.weather(city)
        if self.description != "ERROR!!":
            embed = discord.Embed(title=f"{city.title()}", color=0x00FFFF)
            embed.add_field(name="Weather Condition", value=f"{self.description}", inline=False)
            embed.add_field(name="Temperature", value=f"{weather.temp(city.lower())}°C", inline=False)

            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="Errorrrr", color=0x00FFFF)
            embed.add_field(name="Huh! What city is that??", value="Try with a valid city next time!", inline=False)

            await message.channel.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Missing Argument", color=0x00FFFF)
            embed.add_field(name="Non-existent city hmm?", value="Try this command with a city next time!", inline=True)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Weather(bot))
