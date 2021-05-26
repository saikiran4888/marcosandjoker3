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
from datetime import datetime
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

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin is loaded')

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def poll (self, ctx, question, *options:str):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        color = discord.Color((r << 16) + (g << 8) + b)
        if len(options) <=1:
            await ctx.send('Joker needs more than one option to conduct poll!!')
            return
        if len(options) > 10:
            await ctx.send("Joker Can't accept more than 10 options to conduct poll!")
            return

        if len(options) == 2 and options[0] == '0' and options[1] == '1':
            reactions = ['👍\u20e3', '👎\u20e3']

        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '10\U0001f51f']

            description = []
            for x, option in enumerate(options):
                description += '\n{} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color= color)
            react_message = await ctx.send(embed=embed)
            for reaction in reactions[:len(options)]:
                await react_message.add_reaction(reaction)
            embed.set_footer(text='poll ID: {}'.format(react_message.id))
            await react_message.edit(embed=embed)

    @commands.command(pass_Context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number: int = None):
        try:
            channel = self.client.get_channel(557273459244269582)
            mgss = number+1
            await ctx.message.channel.purge(limit=mgss)
            x = await ctx.send('`Joker has deleted '+str(number)+' messages for you...`')
            await asyncio.sleep(5)
            await x.delete()
            embed = discord.Embed(title=" ", description=f"**Bulk Delete in {ctx.channel.mention} {number+1} messages deleted**", color=ctx.author.color)
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(embed=Forbidden)
            return
        except discord.HTTPException:
            await ctx.send('clear failed.')
            return


        await ctx.delete_messages(mgss)

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, channel: discord.TextChannel=None, *, message: str):
        if channel is None:
            await ctx.send(" ```Proper usage is\n\nannounce<channel><matter>```")
        else:
            await channel.send(message)

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, Role:discord.Role= None, channel:discord.TextChannel=None):
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = False
        overwrite.read_message_history = False
        await channel.set_permissions(Role, overwrite = overwrite)
        await ctx.send(f"**{channel.mention} has been locked for** `{Role.name}`")

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, Role:discord.Role=None, Channel:discord.TextChannel=None):
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.read_message_history = True
        await Channel.set_permissions(Role, overwrite = overwrite)
        await ctx.send(f"**{Channel.mention} has been unlocked for** `{Role.name}`")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True)
    async def roleinfo(self, ctx, role: discord.Role=None):
        embed = discord.Embed(title=f"Here's the info of {role} role...", description=" ", color=role.color)
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed.add_field(name="ID", value=role.id, inline=False)
        embed.add_field(name="Name", value=role.name, inline=False)
        embed.add_field(name="Permissions", value=role.permissions, inline=False)
        embed.add_field(name="Guild/Server", value=ctx.guild.name, inline=False)
        embed.add_field(name="The role is shown seperately from others", value=role.hoist, inline=False)
        embed.add_field(name="Position of the role", value=role.position, inline=False)
        embed.add_field(name="Time of creation", value=role.created_at.strftime("%d-%m-%Y %H:%M:%S"), inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
