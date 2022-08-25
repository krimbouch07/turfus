import nextcord
import requests
import json
import random
from nextcord import Interaction
from nextcord.ext import commands
from datetime import date

class Prono(commands.Cog, name="Prono"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="prono")
    async def prono(self, ctx: Interaction, cc=None, cc2=None ):

        try:
            if cc and cc2 is None:
                turfbed = nextcord.Embed(
                    title="Command Usage:",
                    description="%prono [reunion] [course] Ex: **%prono R1 C3**\n **prono r1 c8**",
                    color = 0xc6c6f5
                )
                await ctx.send(embed=turfbed)

            else:
                cc = cc.upper()
                cc2 = cc2.upper()
                today = date.today()
                d1 = today.strftime(f"%d%m%Y")
                

                    # returns JSON object as a dictionary

                    # Iterating through the json
                    # list
                if cc == "R1":
                        n = 0
                elif cc == "R2":
                        n = 1
                elif cc == "R3":
                        n = 2
                elif cc == "R4":
                        n = 3
                elif cc == "R5":
                        n = 4
                else:
                        turfbed = nextcord.Embed(
                            title="**Command Usage:**",
                            description=f"%prono [reunion course] Ex: %prono r1 c3",
                        )
                        await ctx.send(embed=turfbed)
                url = "https://raw.githubusercontent.com/krimbouch07/myrepo/main/turf.json"
                url2 = ("https://online.turfinfo.api.pmu.fr/rest/client/7/programme/" + d1 + "/" + cc + "/" + cc2)

                data = requests.get(url)
                data2 = requests.get(url2)
                openjs = data.json()
                openjs2 = data2.json()
                prono = openjs["reunion"][n][cc][cc2]
                nomcourse = openjs2["libelle"]
                npartants = openjs2["nombreDeclaresPartants"]
                randomlist = random.sample(range(1,npartants), 5)
                converted_list = [str(element) for element in randomlist]
                joined_string = "-".join(converted_list)
                #member = ctx.author
                #memberAvatar = member.avatar.url
                
                turfbed = nextcord.Embed(
                        title= cc + cc2 + " " + ":horse:" + " " + nomcourse
                    )
                turfbed.add_field(
                        name="**PRONOSTIC:**",
                        value=f"**" + prono + "**",
                        inline=True,
                    )
                turfbed.add_field(
                        name= "**FlashProno**",
                        value= "**" + joined_string + "**",
                        inline= True,
                )
                turfbed.add_field(
                        name = "BaTaTa",
                        value = f"-BATATA Bot, votre spécialiste des paris hippiques en ligne, vous donne toutes les clés pour réussir avec ses pronostics.",
                        inline=False,
                    )
                turfbed.set_thumbnail(url=f"https://images-ext-2.discordapp.net/external/AEdJ-6GNwINxfsMSgSC0b0ne0syduNgjb0DKrF4qhT0/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/999113473529229352/f55306014b1fa345397ba4b6f80c6f13.png")
                #turfbed.set_image(url= listurl)

                turfbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar.url)
                
                await ctx.send(embed=turfbed)

                   

        except:
            turfbed = nextcord.Embed(
                title="Invalid courses ou reunion.",
            )
            turfbed.set_author(name="Error!")
            await ctx.send(embed=turfbed)


def setup(bot: commands.Bot):
    bot.add_cog(Prono(bot))
