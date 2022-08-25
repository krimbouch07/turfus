from turtle import color
from nextcord.ext import commands
import requests, json, random, datetime, asyncio
from PIL import Image, ImageFont, ImageDraw
import textwrap
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View


class Speak(commands.Cog, name = 'Speak'):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='speak')

    async def speak(self, ctx:commands.Context, *args):
        msg = " ".join(args)
        font = ImageFont.truetype("/home/koinx/discord/turfbot1/cogs/gain/PatrickHand-Regular.ttf", size =150)
        img = Image.open("/home/koinx/discord/turfbot1/cogs/gain/1003.jpg")
        cx, cy = (350, 230)
        
        lines = textwrap.wrap(msg, width=150)
        print(lines)
        w, h = font.getsize(msg)
        y_offset = (len(lines)*h)/2
        y_text = cy-(h/2) - y_offset

        for line in lines:
            draw = ImageDraw.Draw(img)
            w, h = font.getsize(line)
            draw.text((cx-(w/2), y_text), line, (255,0, 0, 255), font=font)
            img.save("dog-edited.jpg")
            y_text += h
        
        with open("dog-edited.jpg", "rb") as f:
            img = File(f)
            await ctx.channel.send(file=img)
        
    
    

def setup(bot):
    bot.add_cog(Speak(bot))
