import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import bot, has_permissions, CheckFailure
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
from discord import Spotify
import feedparser
from io import BytesIO
from subprocess import check_output
import os
import functools
import time
import datetime
from datetime import datetime
import sqlite3
from io import BytesIO
import requests
from babel.numbers import PREFIX_END, format_currency
from babel.numbers import format_number
import locale
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from collections import Counter
import aiohttp
import pytz
from pytz import timezone
import secrets
import translators as ts


intents = discord.Intents.all()
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Second Bot for Experimentation", command_prefix='%', pm_help = True, intents=intents)



@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    game = discord.Streaming(name="Nothing", url="https://www.twitch.tv/twitch")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.command(pass_context=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension is loaded.')

@client.command(pass_context = True)
async def meme2(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            """embed = discord.Embed(title='Meme',color=ctx.author.color)
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()"""
            name = data[0]["data"]["children"][0]["data"]["url"]
            await ctx.send(name)
            
            
@client.command(pass_context=True)
async def jasmine(ctx):
    image_urls = ['https://media.discordapp.net/attachments/602215920257073303/853499332652957726/Screenshot_2020-11-29-02-20-32-703_com.instagram.android.jpg',
     'https://media.discordapp.net/attachments/602215920257073303/853499233327775754/IMG_20210530_031612.jpg',
      'https://media.discordapp.net/attachments/602215920257073303/853499022822866944/117795822_334989120959570_3844434461125443401_n.jpg',
       'https://media.discordapp.net/attachments/602215920257073303/853499023075966986/162786008_568694504089596_1713524929316943303_n.jpg',
        'https://media.discordapp.net/attachments/602215920257073303/853499022433845248/131302316_126559875945682_3011887340275736852_n.jpg',
        'https://media.discordapp.net/attachments/602215920257073303/853498483859259432/insta_2481415130999694478.png',
        'https://media.discordapp.net/attachments/602215920257073303/853498482731384842/insta_2556048203032302528_12642553284.png',
        'https://media.discordapp.net/attachments/602215920257073303/853499022433845248/131302316_126559875945682_3011887340275736852_n.jpg',
        'https://media.discordapp.net/attachments/602215920257073303/853499022026342400/106898211_1372065732986874_7527788480294741112_n.jpg',
        'https://images-ext-2.discordapp.net/external/EgC7ZM6UebVuefPbp9QndnX_o6DWU_QtdOWEPjDkyYU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/500047002395213855/b94f7e28fddd2d3b5994a12796ec6e43.webp']

    matter = ["You're the person who has a big heart. Others might hate her saying that she's 'weird' and all. And I've got a word for them that is.... 'Fuck'em all' they don't understand that they're missing a fortune.",
    "You're the person that someone needs to talk when they're feeling lost. You're honest and trustworthy person. You've got every quality even more to find in a friend.",
    "You're that type of person who's shy at first but opens up eventually once they get to know you. It's like you'll become insperable to them. I think that's something we both got in common.",
    "You always try to have a laugh and be the best person around no matter how many problems you face and how many worse situation you are. And you try to make others feel good when they're off despite you're in a quicksand of worse situations.",
    "You're fun, smart, crazy, soft, joyful, cute, gentle, fragile,naughty, confident, competetive, amazing, loud, stunning, beautiful, energetic, badass, bold sometimes annoying in a sweet way and in a single sentence, you're a 'Wholesome package!' lol.'",
    "You're an angel at times, but you can turn into a devil if someone screws with you lol.",
    "Your love towards someone is a bounty as well as your hate towards someone is a curse. And I've got to feel them both lol and trust me that's not a good curse.",] 
    embed = discord.Embed(title=':heart: Jasmine :heart:', description=f"{secrets.choice(matter)} \n\nP.S. Ik these words and me cant't help you get you out from situation directly. But I hope that when you feel down, these words and your smile like in the below pic may help you to restore your courage and can make you cope with the situation. And no matter what, don't lose that goddamn cute smile from you that's something that make you spl.", color=ctx.author.color)
    embed.set_image(url=secrets.choice(image_urls))
    embed.timestamp = datetime1.utcnow()
    embed.set_footer(text="Made for Jasmine.", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)            

    
@client.command(pass_context=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension is unloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('TOKEN'))
