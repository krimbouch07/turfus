from ast import Interactive
import nextcord
import requests
import json
from nextcord.ext import commands
from datetime import date

class Resultats(commands.Cog, name="Resultats"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="res")
    async def res(self, ctx: Interactive, cc=None, cc2=None ):

        try:
            if cc and cc2 is None:
                turfbed = nextcord.Embed(
                    title="Command Usage:",
                    description=f"%res [reunion] [course] Ex: **%res R1 C3**",
                )
                await ctx.send(embed=turfbed)

            else:
                cc = cc.upper()
                cc2 = cc2.upper()
                today = date.today()
                #d1 = today.strftime(f"%d%m%Y")
                d1 = "11082022"
                url = ("https://offline.turfinfo.api.pmu.fr/rest/client/7/programme/" + d1 + "/" + cc + "/" + cc2)
                data = requests.get(url)
                openjs = data.json()
                prono  = openjs["ordreArrivee"][0][0]
                prono1 = openjs["ordreArrivee"][1][0]
                prono2 = openjs["ordreArrivee"][2][0]
                prono3 = openjs["ordreArrivee"][3][0]
                prono4 = openjs["ordreArrivee"][4][0]
                urlpic = openjs["photosArrivee"][2]["url"]
                commentaire = openjs["commentaireApresCourse"]["texte"]
                prono0 = f' ``` {prono}-{prono1}-{prono2}-{prono3}-{prono4} ```'

                nomcourse = openjs["libelle"]
                    # returns JSON object as a dictionary

                    # Iterating through the json
                    # list
                
                member = ctx.author
                memberAvatar = member.avatar.url
                
                    
                turfbed = nextcord.Embed(
                        title= ":horse_racing:" + nomcourse
                    )
                turfbed.add_field(
                        name="Arrivee final",
                        value=  prono0 , 
                        inline=False,
                    )
                turfbed.add_field(
                        name= "Commentaire",
                        value= commentaire,
                        inline=False,
                )
                
                turfbed.set_footer(text= member.name, icon_url = member.avatar.url)
                turfbed.set_thumbnail(url=memberAvatar)
                turfbed.set_image(url=urlpic)

                await ctx.send(embed=turfbed)

                   

        except:
            turfbed = nextcord.Embed(
                title="Arrivee indisponible",
            )
            turfbed.set_author(name="Error!")
            await ctx.send(embed=turfbed)


def setup(bot: commands.Bot):
    bot.add_cog(Resultats(bot))
