#-----Imports-----
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks


#-----Commands----- 
class Help(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot


	#Help
	@commands.command(name = 'help', description = f'❕ les commandes valide (Example: %help)')
	async def help(self, ctx: Interaction, module: str=None):

		if module == None:

			embed = nextcord.Embed(
				title = 'Command list',
				description = f'En savoir plus sur le module de commande spécifique: %help <Module>**',
				color = 0xbdda45
				)

			embed.set_author(
				name = ctx.author.name,
				icon_url = ctx.author.avatar.url
				)

			#Modules
            
			embed.add_field(
				name = '🛡️ Admin',
				value = f'%help admin'
				)
            
			embed.add_field(
				name = '🔥 Prono',
				value = f'%help prono'
				)	

			embed.add_field(
				name = ':five: Quinte',
				value = f'%help quinte'
				)			

			embed.add_field(
				name = '🖼️ skynight',
				value = f'%help dlam'
				)
			embed.add_field(
				name = ':trophy: Resultats',
				value = f'%res Rn Cn'
			)
			embed.add_field(
				name = '📋 Information',
				value = f'%help info'
				)            
            
			await ctx.send(embed = embed)

		elif module == 'moderation':

			embed = nextcord.Embed(
				title = '🛡️ Moderation',
				description = ':red_circle:    ban    : Ban the member\n:red_circle:    kick    : Kick the member\n:green_circle:    clear    : Clear messages\n:red_circle:    report    : Report to the problem\n',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)

		elif module == 'info':

			embed = nextcord.Embed(
				title = '📋 Information',
				description = ':green_circle:   user    : Shows information about User\n:green_circle:   server    : Shows information about Server\n:green_circle: bot : In developing',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)

		elif module == 'quinte':

			embed = nextcord.Embed(
				title = ':five: Quinte',
				description = f'%quinte le programme de quinte paris-turf',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)

		elif module == 'dlam':

			embed = nextcord.Embed(
				title = '🖼️ Skynight',
				description = 'Que la nuit :black_cat: :black_joker: :black_circle:',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)

		elif module == 'prono':

			embed = nextcord.Embed(
				title = '🔥 Prono',
				description = f'%prono [reunion] [course]\n  Ex: %prono r1 c3 \n %prono R4 C5',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)
		
		elif module == 'resultats':
			embed = nextcord.Embed(
				title = ':loudspeaker: Resultats',
				description = f'%resultats [reunion] [course]\n  Ex: **%res r1 c3** \n **%res R4 C5**',
				color = 0xc6c6f5
				)

			await ctx.send(embed = embed)


#-----Run-----
def setup(bot):
	bot.add_cog(Help(bot))
