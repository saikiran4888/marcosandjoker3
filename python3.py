import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
from discord import Spotify
import os
import functools
import time
import datetime
import requests
import json
import aiohttp



async def status_task():
    while True:
        await client.change_presence(status=discord.Status.online)
        
      
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="The Laughing Clown BOT", command_prefix=commands.when_mentioned_or("*"), pm_help = True)
client.remove_command('help')



@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    client.loop.create_task(status_task())


@client.command(pass_context = True)
async def hello(ctx):
    await ctx.send(f"Hello, How's your day today? {ctx.message.author.mention}")
    
@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    
    else:
        channel = client.get_channel(557273459244269582)
        matter = f"Message sent by: {message.author.mention} deleted in {message.channel.mention} \n \n  {message.content}"
        embed = discord.Embed(title=f"{message.author.name}", description=matter, color=0XFF69BF)
        embed.set_footer(text=f"Author {message.author.id}  | Message ID: {message.id}")
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
        
@client.event
async def on_member_remove(member):
    channel = client.get_channel(565768324252958720)
    channel2 = client.get_channel(557273459244269582)
    userchannel = client.get_channel(571302888110817281)
    person_count = len([member for member in member.guild.members if not member.bot])
    embed=discord.Embed(title=f"Good bye {member.name}... Hope you'll come back again to {member.guild.name}", description="Thank you for being with us all these times...", color=0XFF69B4)
    embed.set_thumbnail(url='https://media.giphy.com/media/LTFbyWuELIlqlXGLeZ/giphy.gif')
    embed.add_field(name="__**Members Remaining**__", value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed2=discord.Embed(title="Member Left", description= member.mention, color=0XFF69B4)
    embed2.set_thumbnail(url=member.avatar_url)
    embed2.add_field(name="**Members Remaining**", value=str(member.guild.member_count), inline=True)
    embed2.set_footer(text=f"ID: {member.id}", icon_url=member.avatar_url)
    embed2.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
    await channel2.send(embed=embed2)
    await userchannel.edit(name= f"Weebs: {person_count}")

@client.event
async def on_member_join(member):
    choices = ["DcssawdeS", "Sasdawdd", "AWSdasdwaA", "AdwASwAas", "AsdWDAasas", "ASDwdAsad", "MKiojmkomM"]
    choices2 = random.choice(choices)
    role = discord.utils.get(member.guild.roles, id=516303012671520769)
    embed = discord.Embed(title=" ", description=f"Welcome to {member.guild.name}, In order to send any message in the server, You must verify as per the server's policy. Sorry for bothering you but it's my duty though.... And please follow the instructions below. I'm sure that the instructions will be easy for you... Wait 15 seconds for next message.", color=0XFF69BF)
    embed.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed2 = discord.Embed(title=" ", description="You've to type the word shown in the next message correctly. And you'vve got only three chances. If you failed to enter correct word, Then you'll get kicked from server and you've to join again... Wait 15 seconds for next message", color=0XFF69BF)
    embed2.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed2.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed3 = discord.Embed(title=f"This is your first attempt (Two remaining)... Type the word shown below correctly... **\n \n {choices2} \n \n**", description=" ", color=0XFF69BF)
    embed3.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed3.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    await member.send(embed=embed)
    await asyncio.sleep(15)
    await member.send(embed=embed2)
    await asyncio.sleep(15)
    await member.send(embed=embed3)
    msg2 = await client.wait_for('message', check=lambda message: message.author == member)
    if msg2.content == choices2:
        embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us**", description=" ", color=0XFF69BF)
        embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed4)
        await member.add_roles(role)
    else:
        choices3 = random.choice(choices)
        embed5 = discord.Embed(title=f"You've typed the wrong word... This is your second attempt (One remaining)... Type the word shown below correctly...** \n \n {choices3} \n \n**", description=" ", color=0XFF69BF)
        embed5.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed5.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed5)
        msg3 = await client.wait_for('message', check=lambda message: message.author == member)
        if msg3.content == choices3:
            embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFF69BF)
            embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed4)
            await member.add_roles(role)
        else:
            choices4 = random.choice(choices)
            embed6 = discord.Embed(title=f"You've typed the wrong word... This is your last attempt... Type the word shown below correctly.. If yout typed wrong you'll get kicked from server...** \n \n {choices4} \n \n**", description=" ", color=0XFF69BF)
            embed6.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed6.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed6)
            msg4 = await client.wait_for('message', check=lambda message: message.author == member)
            if msg4.content == choices4:
                embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFF69BF)
                embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
                embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
                await member.send(embed=embed4)
                await member.add_roles(role)
            else:
                await member.send("**You've entered a wrong word agian.... Your attempts are over... You've been kicked out of this server**")
                await member.guild.kick(member, reason="**Unsuccessful Verification**")
                return
    gettime = discord.utils.snowflake_time(member.id)
    channel = client.get_channel(565766644140474368)
    channel2 = client.get_channel(557273459244269582)
    text_channel = client.get_channel(565767003533737985)
    userchannel = client.get_channel(571302888110817281)
    person_count = len([member for member in member.guild.members if not member.bot])
    embed=discord.Embed(title=f"Welcome {member.name} to {member.guild.name}", description=f"**Hope you'll be active here... Read rules at {text_channel.mention} channel and don't break any of them...**", color=0XFF69B4)
    embed.set_thumbnail(url='https://media.giphy.com/media/OF0yOAufcWLfi/giphy.gif')
    embed.add_field(name="__**Thanks for joining our server**__", value="We hope you a good stay here....")
    embed.add_field(name="__**Time of joining**__", value=member.joined_at.date(), inline=True)
    embed.add_field(name="__**Joining position**__", value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name="__**User account created at**__", value=gettime.date(), inline=True)
    embed.set_footer(text=member.name, icon_url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed2=discord.Embed(title="Member Joined", description=member.mention, color=0XFF69B4)
    embed2.add_field(name="**Members Remaining**", value=str(member.guild.member_count), inline=True)
    embed2.set_footer(text=f"ID: {member.id}", icon_url=member.avatar_url)
    embed2.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
    await channel2.send(embed=embed2)
    await userchannel.edit(name= f"Weebs: {person_count}")
    
@client.event
async def on_message_edit(before,after):
    if before.content != after.content:
        channel = client.get_channel(557273459244269582)
        matter = f"**Message edited in {before.channel.mention} **[Jump to message](https://discordapp.com/channels/{before.guild.id}/{after.channel.id}/{after.id})"
        embed = discord.Embed(title=f"{before.author.name}", description=matter, color=0XFF69B4)
        embed.add_field(name="Before", value=before.content, inline=False)
        embed.add_field(name="After", value=after.content, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"ID: {before.id}")
        await channel.send(embed=embed)
        
@client.event
async def on_guild_channel_create(channel):
    channel2 = client.get_channel(557273459244269582)
    embed = discord.Embed(title="New Channel Created", description=f"**Channel Created: {channel.mention}**", color=0XFF69BF)
    embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"ID: {channel.id}")

    await channel2.send(embed=embed)

@client.event
async def on_guild_channel_delete(channel):
    channel2 = client.get_channel(557273459244269582)
    embed = discord.Embed(title="Channel Deleted", description=f"**Channel Deleted: {channel.name}**", color=0XFF69BF)
    embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"ID: {channel.id}")

    await channel2.send(embed=embed)

@client.event
async def on_guild_channel_update(before, after):
    channel2 = client.get_channel(557273459244269582)
    if before.name != after.name:
        embed = discord.Embed(title="Channel Name Edited", description=" ", color=0XFF69BF)
        embed.set_author(name=after.guild.name, icon_url=after.guild.name)
        embed.add_field(name="Before", value=before.name, inline=False)
        embed.add_field(name="After", value=after.name, inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"ID: {after.id}")
        await channel2.send(embed=embed)

    elif before.topic != after.topic:
        embed2 = discord.Embed(title="Channel Topic Edited", description=f"Channel edited: {after.mention} ", color=0XFF69BF)
        embed2.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
        embed2.add_field(name="Before", value=before.topic, inline=False)
        embed2.add_field(name="After", value=after.topic, inline=False)
        embed2.timestamp = datetime.datetime.utcnow()
        embed2.set_footer(text=f"ID: {after.id}")
        await channel2.send(embed=embed2)
        
client.run(os.getenv('TOKEN'))
