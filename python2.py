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
import translators as ts


intents = discord.Intents.all()
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Second Bot for Experimentation", command_prefix='&', pm_help = True, intents=intents)



@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    game=discord.Game("Nothing")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)

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
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} extension is unloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('TOKEN'))
