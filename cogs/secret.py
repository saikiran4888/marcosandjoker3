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
from subprocess import check_output
import os
import functools
import time
import datetime
import sqlite3
import aiohttp
from io import BytesIO
import requests
from babel.numbers import format_currency
from babel.numbers import format_number
import locale
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from collections import Counter
import pytz
from pytz import timezone

class Secret(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Secret is loaded')

    @commands.command(pass_context=True)
    async def avatar2(self, ctx, *, id1:str=None):
        if id is None:
            user = ctx.message.author
            embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
            embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
            embed.set_image(url = ctx.message.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            user = await self.client.fetch_user(id1)
            embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
            embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_image(url = user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(pass_context = True)
    async def P(self, ctx, *, word:str=None):
        if ctx.guild.name == "Test":

            if ctx.channel.is_nsfw():
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://api.reddit.com/r/{word}/random") as r:
                        data = await r.json()
                        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                        embed = discord.Embed(title=data[0]['data']['children'][0]['data']['title'],color = discord.Color((r << 16) + (g << 8) + b))
                        embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                        embed.url = data[0]["data"]["children"][0]["data"]["url"]
                        embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
                        embed.timestamp = datetime.datetime.utcnow()
                        await ctx.send(embed=embed)

            else:
                await ctx.send("**Nah! Nah! Nah! This has to be a NSFW channel, fucker!!!**")
        else:
            return

    @commands.command(pass_context=True)
    async def p(self, ctx, *, word:str=None):
        if ctx.guild.name == "Test":
            if ctx.channel.is_nsfw():
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://api.reddit.com/r/{word}/random") as r:
                        data = await r.json()
                        await ctx.send(f"{data[0]['data']['children'][0]['data']['url']} \n **{data[0]['data']['children'][0]['data']['title']}**")
            else:
                 await ctx.send("**Nah! Nah! Nah! This has to be a NSFW channel, fucker!!!**")
        else:
            return

    @commands.command(pass_context=True)
    async def neko(self, ctx, *, name:str=None):
        if ctx.guild.name == "Test":
            if ctx.channel.is_nsfw():
                list1 = ['femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'v3', 'hololewd', 'nekoapi_v3.1', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo']
            #word = [word for word in list1 if name is in list1]
                if name in list1:
                    address = f"https://nekos.life/api/v2/img/{name}"
                    data = requests.get(address).json()
                    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                    color = discord.Color((r << 16) + (g << 8) + b)
                    embed = discord.Embed(title=name, description=" ", color=color)
                    embed.url = data['url']
                    image = data['url']
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_image(url=image)
                    embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                elif name == "help":
                    helplist = ", ".join(list1)
                    await ctx.send(f"Available args:\n ```{helplist}``` \n ``&neko <args>``")
            else:
                await ctx.send("**Nah! Nah! Nah! This has to be a NSFW channel, fucker!!!**")
        else:
            return

    @commands.command(pass_context=True)
    async def h(self, ctx, *, name:str=None):
        if ctx.guild.name == "Test":
            if ctx.channel.is_nsfw():
                list1 = ['hass', 'hmidriff', 'pgif', '4k', 'hentai', 'holo', 'hneko', 'neko', 'hkitsune', 'kemonomimi', 'anal', 'hanal', 'gonewild', 'kanna', 'ass', 'pussy', 'thigh', 'hthigh', 'gah', 'coffee', 'food']
            #word = [word for word in list1 if name is in list1]
                if name in list1:
                    address = f"https://nekobot.xyz/api/image?type={name}"
                    data = requests.get(address).json()
                    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                    color = discord.Color((r << 16) + (g << 8) + b)
                    embed = discord.Embed(title=name, description=" ", color=color)
                    embed.url = data['message']
                    image = data['message']
                    embed.set_image(url=image)
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                elif name == "help":
                    helplist = ", ".join(list1)
                    await ctx.send(f"Available args:\n ```{helplist}``` \n ``&neko <args>``")
            else:
                await ctx.send("**Nah! Nah! Nah! This has to be a NSFW channel, fucker!!!**")
        else:
            return


def setup(client):
    client.add_cog(Secret(client))
