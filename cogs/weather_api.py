from discord.ext import commands

from APIs import weather


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather')
    async def weather(self, message, *, city):
        self.description = weather.weather(city)
        if self.description != "ERROR!!":
            output = f'''```cs
Weather in {city.title()}: "{self.description}"\nTemperature: "{weather.temp(city.lower())}°C"```'''
            await message.channel.send(output)
        else:
            await message.channel.send('''''''```cs\n"Oopsie! Looks like an error!"```''')


def setup(bot):
    bot.add_cog(Weather(bot))
