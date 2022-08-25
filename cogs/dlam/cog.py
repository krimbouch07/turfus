from time import timezone
import nextcord
import requests
import json
from nextcord.ext import commands
from datetime import date, datetime

class Details(commands.Cog, name="Details"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="course")
    async def course(self, ctx: commands.Context, cc=None, cc2=None ):

        n= "0 popo"
        today = date.today()
        timz = today.strftime(f"%d%m%Y")
                 
        turfbed = nextcord.Embed(
                    title="Command Usage:",
                    description= n ,
                    timestamp= datetime(month=today.strftime(f"%m"), year=today.strftime(f"%Y"))
                )
        await ctx.send(embed=turfbed)



def setup(bot: commands.Bot):
    bot.add_cog(Details(bot))
