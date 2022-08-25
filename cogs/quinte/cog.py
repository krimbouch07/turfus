import nextcord
from nextcord.ext import commands


class Quinte(commands.Cog, name = 'Quinte'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="quinte")
    async def quinte(self, ctx: commands.Context):
        await ctx.send("https://www.paris-turf.com/quinte/aujourdhui")

    

def setup(bot: commands.Bot):
    bot.add_cog(Quinte(bot))