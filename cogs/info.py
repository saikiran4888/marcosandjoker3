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
from datetime import datetime as datetime1
import sqlite3
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
import translators as ts

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Info is loaded')

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(pass_context=True)
    async def pincode(self, ctx, pincode:str=None):
        url = f"https://api.postalpincode.in/pincode/{pincode}"
        data = requests.get(url).json()
        count = str(data[0]['PostOffice']).count('Name')
        message = data[0]['Message']
        names = list(data[0]['PostOffice'][x]['Name'] for x in range(count))
        blocks = list(data[0]['PostOffice'][x]['Block'] for x in range(count))
        list1 = list("{} ({},".format(name, block) for name, block in zip(names, blocks))
        regions = list(data[0]['PostOffice'][x]['Division'] for x in range(count))
        list2 = list("{} {})".format(main, region) for main, region in zip(list1, regions))
        list3 = '\n\n'.join(list2)
        await ctx.send(f"{message}\n{list3}")

    @commands.command(pass_context = True)
    async def botinfo(self, ctx):
        User = await self.client.fetch_user('472128507150073871')
        User2 = await self.client.fetch_user('498378677512437762')
        User3 = await self.client.fetch_user('500219510079356928')
        User4 = await self.client.fetch_user("400255149014122496")
        embed=discord.Embed(title="Details of this BOT...", description="Here are the details of this BOT below", color=ctx.author.color)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
        embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_author(name=f"This is Official BOT of {ctx.guild.name} server")
        embed.add_field(name="__**Creator**__", value=User.mention, inline = True)
        embed.add_field(name="__**Special Thanks To**__", value=f"{User2.mention} \n {User3.mention} \n {User4.mention}")
        embed.add_field(name="**Currently connected servers**", value="1", inline = True)
        embed.add_field(name="**Currently connected users**", value=str(len(set(self.client.get_all_members()))), inline = True)
        embed.add_field(name="If you have any queries about this BOT, DM me...", value=User.mention)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member=None):
        if user != None:
            embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
            embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
            embed.set_image(url = user.avatar_url)
            embed.set_footer(text=f"Requested by {user.name}", icon_url=f'{user.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            user = ctx.author
            embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
            embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
            embed.set_footer(text=f"Requested by {user.name}", icon_url=f"{user.avatar_url}")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_image(url = user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def urban(sekf, ctx, *, word:str=None):
        await ctx.trigger_typing()
        address = f"http://api.urbandictionary.com/v0/define?term={word}"
        data = requests.get(address).json()
        matter = data['list'][0]['definition'].replace("[", "").replace("]", "")
        embed = discord.Embed(title=data['list'][0]['word'], description=f"{matter} \n[Click me for alternate definitions]({data['list'][0]['permalink']})", color=ctx.author.color)
        embed.add_field(name="Example", value=data['list'][0]['example'].replace("[", "").replace("]", ""), inline=False)
        embed.add_field(name="Upvotes", value=data['list'][0]['thumbs_up'], inline = True)
        embed.add_field(name="Downvotes", value=data['list'][0]['thumbs_down'], inline = True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Written by {data['list'][0]['author']} on Urban dictionary")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def define(self, ctx, *, word:str = None):
        if word == None:
            await ctx.send("Type any word to define...")
        else:
            address = f"https://some-random-api.ml/dictionary?word={word}"
            data = requests.get(address).json()
            definition = data['definition']
            await ctx.send(f"The definition of {data['word']} is sent to your DM")
            for chunk in [definition[i:i+2000] for i in range(0, len(definition), 2000)]:
                await ctx.author.send(chunk)

    @commands.command(pass_context=True)
    async def syn(self, ctx, *, word:str =None):
        if word == None:
            await ctx.trigger_typing()
            await asyncio.sleep(3)
            await ctx.send("Type any word to find synonyms for it...")
        else:
            address = f"https://words.bighugelabs.com/api/2/27faccbe1b03a1577c7f167a9b88bebf/{word}/json"
            data = requests.get(address).json()
            noun = data['noun']['syn']
            noun2 = ", ".join(noun)
            embed = discord.Embed(title=f"Here's the synonym(s) for {word} that I could find...", description=noun2, color=ctx.author.color)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def translate(self, ctx, lang1:str, *, text:str = None):
        translated = ts.google(text, to_language=lang1, is_detail_result=True)
        data = translated
        pro1 = data[0][0]
        pro2 = data[1][0][0][1]
        original = text
        trans = data[1][0][0][5][0][0]
        """await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(translated)
        await ctx.send(f'{pro1}, {pro2}, {original}, {trans}')"""
        await ctx.send(f"Original text: {text}\nOriginal Pronounciation: {pro1}\nTranslated text: {trans}\n Translated pronounciation: {pro2}")
        await ctx.send(trans)

    @commands.command(pass_context=True)
    async def translate2(self, ctx, lang1:str, *, text:str = None):
        translated = ts.google(text, to_language=lang1, is_detail_result=True)
        data = translated
        pro1 = data[0][0]
        pro2 = data[1][0][0][1]
        original = text
        trans = data[1][0][0][5][0][0]
        """await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(translated)
        await ctx.send(f'{pro1}, {pro2}, {original}, {trans}')
        await ctx.send(f"Original text: {text}\nOriginal Pronounciation: {pro1}\nTranslated text: {trans}\n Translated pronounciation: {pro2}")"""
        await ctx.send(trans)

    """@translate.error
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Oh no! I can't find the language to be translated.")"""

    @commands.command(pass_context=True)
    async def transhelp(self, ctx):
        print(ts._google.language_map)

    @commands.command(pass_contex=True)
    async def weather(self, ctx, *, city:str=None):
        if city == None:
            await ctx.send("**Please enter any city name...**")
        else:
            address = f"http://api.openweathermap.org/data/2.5/weather?appid=f2e8d829021f0bb51351afb8a104b709&q={city}&units=metric"
            data = requests.get(address).json()
            if data['cod'] == "404":
                await ctx.send(f"**{data['message']}**")
            else:
                sunriseraw = data['sys']['sunrise']
                sunsetraw = data['sys']['sunset']
                updatedraw =  data['dt']
                updated = datetime1fromtimestamp(updatedraw).strftime("%d-%m-%Y %I:%M %p")
                sunrise = datetime1.fromtimestamp(sunriseraw).strftime("%d-%m-%Y %I:%M %p")
                sunset = datetime1.fromtimestamp(sunsetraw).strftime("%d-%m-%Y %I:%M %p")
                embed = discord.Embed(title="Weather Forecast...", description="Here's your weather forecast that you've requested", color=discord.Colour.blue())
                embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
                embed.add_field(name="City", value=data['name'])
                embed.add_field(name="Country", value=data['sys']['country'])
                embed.add_field(name="Temperature", value=f"{data['main']['temp']}°C")
                embed.add_field(name="Temperature Feels Like", value=f"{data['main']['feels_like']}°C")
                embed.add_field(name="Min. Temp", value=f"{data['main']['temp_min']}°C")
                embed.add_field(name="Max. Temp", value=f"{data['main']['temp_max']}°C")
                embed.add_field(name="Sunrise", value=sunrise)
                embed.add_field(name="Sunset", value=sunset)
                embed.add_field(name="Description", value=f"{data['weather'][0]['description']}")
                embed.add_field(name="Wind Speed", value=f"{data['wind']['speed']}meter/sec")
                embed.add_field(name="Wind Direction (degrees)", value=f"{data['wind']['deg']}°")
                embed.add_field(name="Wind Gust", value=f"{data['wind']['gust']}meter/sec")
                embed.add_field(name="Humidity", value=f"{data['main']['humidity']}%")
                embed.add_field(name="Cloudliness", value=f"{data['clouds']['all']}%")
                embed.add_field(name="Last Updated", value=updated)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=f"Powered by OpenWeather API, Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
