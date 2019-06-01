import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
from discord import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
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
client = commands.Bot(description="The Laughing Clown BOT", command_prefix=commands.when_mentioned_or("%"), pm_help = True)
client.remove_command('help')



@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    client.loop.create_task(status_task())


@client.command(pass_context = True)
async def hlo(ctx):
    await ctx.send(f"Hello, How's your day today? {ctx.message.author.mention}")

@client.command(pass_context = True)
async def quote(ctx):
    choices = ["**Smile, because it confuses people. Smile, because it's easier than explaining what is killing you inside. - THE JOKER**", "**As you know, madness is like gravity...all it takes is a little push. - THE JOKER**", "**If you’re good at something, never do it for free. - THE JOKER**", "**Nobody panics when things go “according to plan”. Even if the plan is horrifying! - THE JOKER**", "**Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos... - THE JOKER**", "**Do I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it! You know, I just... *do* things. - THE JOKER**", "**What doesn't kill you, simply makes you stranger! - THE JOKER**", "**Why so serious? >:) - THE JOKER**", "**They Laugh At me Because I'm Different. I laugh At Them Because The're all the same - THE JOKER**", "**Their morals, their code; it's a bad joke. Dropped at the first sign of trouble. They're only as good as the world allows them to be. You'll see- I'll show you. When the chips are down these, uh, civilized people? They'll eat each other. See I'm not a monster, I'm just ahead of the curve. - THE JOKER**", "**The only sensible way to live in this world is without rules. - THE JOKER**"]
    embed = discord.Embed(title = " ", description = "**RIP Heath Ledger.... You've gave us a memorable gift like JOKER... We can't forget you...**", color=0XFF69B4)
    embed.add_field(name="Here's a quote of JOKER for you....", value = random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def botinfo(ctx):
    User = await client.fetch_user('472128507150073871')
    User2 = await client.fetch_user('498378677512437762')
    User3 = await client.fetch_user('500219510079356928')
    User4 = await client.fetch_user("400255149014122496")
    embed=discord.Embed(title="Details of this BOT...", description="Here are the details of this BOT below", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"This is Official BOT of {ctx.guild.name} server")
    embed.add_field(name="__**Creator**__", value=User.mention, inline = True)
    embed.add_field(name="__**Special Thanks To**__", value=f"{User2.mention} \n {User3.mention} \n {User4.mention}")
    embed.add_field(name="**Currently connected servers**", value=str(len(client.guilds)), inline = True)
    embed.add_field(name="**Currently connected users**", value=str(len(set(client.get_all_members()))), inline = True)
    embed.add_field(name="If you have any queries about this BOT, DM me...", value=User.mention)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def userid(ctx):
    await ctx.send(f"{ctx.message.author.id}")

@client.command(pass_context = True)
async def fams(ctx):
    choices = ['https://media.giphy.com/media/zDAqUralC0HU4/giphy.gif', 'https://media.giphy.com/media/pz1s2IpdQh86k/giphy.gif', 'https://media.giphy.com/media/1LnQIODGufGec/giphy.gif', 'https://media.giphy.com/media/yROJ5dn5IhR5u/giphy.gif', 'https://media.giphy.com/media/SjWEmbTtlOwcU/giphy.gif', 'https://media.giphy.com/media/396CPbx4g1o9W/giphy.gif', 'https://media.giphy.com/media/mXz3v0UdjrNTO/giphy.gif', 'https://media.giphy.com/media/XAr3mee7JuXYc/giphy.gif', 'https://media.giphy.com/media/12I9y6on09avza/giphy.gif', 'https://media.giphy.com/media/zBdfuQVMClAis/giphy.gif']
    embed = discord.Embed(title = "Hello {}, Here's your GIF....".format(ctx.message.author.name), description = " ", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    
    else:
        channel = client.get_channel(557273459244269582)
        matter = f"**Message sent by: {message.author.mention} deleted in {message.channel.mention} \n \n  {message.content}**"
        embed = discord.Embed(title=f"{message.author.name}", description=matter, color=0XFF69BF)
        embed.set_footer(text=f"Author {message.author.id}  | Message ID: {message.id}")
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=0XFF69B4)
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=0XFF69B4)
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options:str):
    if len(options) <=1:
        await ctx.send('Joker needs more than one option to conduct poll!!')
        return
    if len(options) > 10:
        await ctx.send("Joker Can't accept more than 10 options to conduct poll!")
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']

    else:
        reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color=0XFF69B4)
            react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
            embed.set_footer(text='poll ID: {}'.format(react_message.id))
            await react_message.edit(embed=embed)

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
    await userchannel.edit(name= f"User Count: {person_count}")

@client.event
async def on_member_join(member):
    choices = ["DcssawdeS", "Sasdawdd", "AWSdasdwaA", "AdwASwAas", "AsdWDAasas", "ASDwdAsad", "MKiojmkomM"]
    choices2 = random.choice(choices)
    role = discord.utils.get(member.guild.roles, id=549265886100586506)
    embed = discord.Embed(title=" ", description=f"Welcome to {member.guild.name}, In order to send any message in the server, You must verify as per the server's policy. Sorry for bothering you but it's my duty though.... And please follow the instructions below. I'm sure that the instructions will be easy for you... Wait 10 seconds for next message.", color=0XFF69BF)
    embed.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed2 = discord.Embed(title=" ", description="You've to type the word shown in the next message correctly. And you'vve got only three chances. If you failed to enter correct word, Then you'll get kicked from server and you've to join again... Wait 10 seconds for next message", color=0XFF69BF)
    embed2.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed2.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed3 = discord.Embed(title="This is your first attempt (Two remaining)... Type the word shown below correctly", description=f"**{choices2}**", color=0XFF69BF)
    embed3.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed3.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    await member.send(embed=embed)
    await asyncio.sleep(10)
    await member.send(embed=embed2)
    await asyncio.sleep(10)
    await member.send(embed=embed3)
    msg2 = await client.wait_for('message', timeout=60)
    if msg2.content == choices2:
        embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us**", description=" ", color=0XFF69BF)
        embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed4)
        await member.add_roles(role)
    else:
        choices3 = random.choice(choices)
        embed5 = discord.Embed(title="You've typed the wrong word... This is your second attempt (One remaining)... Type the word shown below correctly", description=f"{choices3}", color=0XFF69BF)
        embed5.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed5.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed5)
        msg3 = await client.wait_for('message', timeout=60)
        if msg3.content == choices3:
            embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFF69BF)
            embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed4)
            await member.add_roles(role)
        else:
            choices4 = random.choice(choices)
            embed6 = discord.Embed(title="You've typed the wrong word... This is your last attempt... Type the word shown below correctly.. If yout typed wrong you'll get kicked from server...", description=f"{choices4}", color=0XFF69BF)
            embed6.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed6.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed6)
            msg4 = await client.wait_for('message', timeout=60)
            if msg4.content == choices4:
                embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFF69BF)
                embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
                embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
                await member.send(embed=embed4)
                await member.add_roles(role)
            else:
                await member.send("**You've entered a wrong word agian.... Your attempts are over... You've been kicked out of this server**")
                await member.guild.kick(member)
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
    await userchannel.edit(name= f"User Count: {person_count}")

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

@client.command(pass_context = True)
async def marvel(ctx):
    choices = ['https://media.giphy.com/media/F9hQLAVhWnL56/giphy.gif', 'https://media.giphy.com/media/l4FGrYKtP0pBGpBAY/giphy.gif', 'https://media.giphy.com/media/JzujPK0id34qI/giphy.gif', 'https://media.giphy.com/media/M9TuBZs3LIQz6/giphy.gif', 'https://media.giphy.com/media/3GnKKEw2v7bXi/giphy.gif', 'https://media.giphy.com/media/GR1WWKadM9m0g/giphy.gif', 'https://media.giphy.com/media/iBpq5SbrYiSTTSHO7z/giphy.gif', 'https://media.giphy.com/media/dJirXKRo0j1l0j9V9Q/giphy.gif', 'https://media.giphy.com/media/ZvkFmclQO1ImmRNm0K/giphy.gif', 'https://media.giphy.com/media/82Mksc7tnX3qp4FVNN/giphy.gif', 'https://media.giphy.com/media/mTQhl6cWXDJBu/giphy.gif']
    embed=discord.Embed(title="Hello {}... Here's your GIF...".format(ctx.message.author.name), description="This BOT is made by I'm Joker", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name} ', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def dc(ctx):
    choices = ['https://media.giphy.com/media/uDPSXySAEDv56/giphy.gif', 'https://media.giphy.com/media/26vIg1DlkNdJr65q0/giphy.gif', 'https://media.giphy.com/media/jcIRoyJKQG3za/giphy.gif', 'https://media.giphy.com/media/26xBLVi4RuhYmV6zm/giphy.gif', 'https://media.giphy.com/media/xUOwGfcrlRjKjs2sSI/giphy.gif', 'https://media.giphy.com/media/l41Yq5KYEmbxFaeVq/giphy.gif', 'https://media.giphy.com/media/3o7abJW5ZuiByDelji/giphy.gif', 'https://media.giphy.com/media/xU67CtAMi8f5K/giphy.gif', 'https://media.giphy.com/media/VXQuKHDhTIBWM/giphy.gif']
    embed=discord.Embed(title="Hello kryptonian... Here's your GIF...", color=0XFF69B4)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)



@client.command(pass_context = True)
async def joker(ctx):
    choices = ['https://media.giphy.com/media/KZd26L2o8QXtK/giphy.gif', 'https://media.giphy.com/media/aazZrFTMrDKLK/giphy.gif', 'https://media.giphy.com/media/F0A48Q2wFjE7S/giphy.gif', 'https://media.giphy.com/media/7waKDy5RbDYVG/giphy.gif', 'https://media.giphy.com/media/13m24iFmhomZi0/giphy.gif', 'https://media.giphy.com/media/zCP1GdPjxtCTe/giphy.gif', 'https://media.giphy.com/media/tN2OR1R1BLKV2/giphy.gif', 'https://media.giphy.com/media/X9Z0O2bpi8GMU/giphy.gif', 'https://media.giphy.com/media/YPIrsRqqO7oB2/giphy.gif', 'https://media.giphy.com/media/FSp1Wqx2TPYSA/giphy.gif', 'https://media.giphy.com/media/8UwEdwAF5XWQE/giphy.gif']
    embed=discord.Embed(title="Hello Joker fan... Here's a GIF for you...", description="Tribute to the legendary **Heath Ledger**", color=0XFF69B4)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


@client.command(pass_context = True)
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Meme',color=0XFF69B4)
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

@client.command(pass_context = True)
async def serverinvite(ctx):
    link = "**Thanks for joining in our server.... Invite your friends and tell them join the party too** \n https://discord.gg/hhmfxW3"
    await ctx.send(link)
    
    
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
 
    if ctx.message.author.guild_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in ctx.history(limit = number+1):
        mgs.append(x)            
       
    try:
        await ctx.message.channel.delete_messages(mgs)          
        x = await ctx.send('`Joker has deleted '+str(number)+' messages for you...`')
        await asyncio.sleep(5)
        await x.delete()
     
    except discord.Forbidden:
        await ctx.send(embed=Forbidden)
        return
    except discord.HTTPException:
        await ctx.send('clear failed.')
        return         
   
 
    await ctx.delete_messages(mgs)

@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
    await ctx.trigger_typing()
    if name is None:
        embed=discord.Embed(description = "Please specify a movie, *eg. %movie Bohemian Rhapsody*", color = 0XFF69B4)
        await ctx.send(embed=embed)
    key = "4210fd67"
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
    response = requests.get(url)
    x = json.loads(response.text)
    embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = 0XFF69B4)
    if x["Poster"] != "N/A":
     embed.set_thumbnail(url = x["Poster"])
    embed.add_field(name = "__Title__", value = x["Title"])
    embed.add_field(name = "__Released__", value = x["Released"])
    embed.add_field(name = "__Runtime__", value = x["Runtime"])
    embed.add_field(name = "__Genre__", value = x["Genre"])
    embed.add_field(name = "__Director__", value = x["Director"])
    embed.add_field(name = "__Writer__", value = x["Writer"])
    embed.add_field(name = "__Actors__", value = x["Actors"])
    embed.add_field(name = "__Plot__", value = x["Plot"])
    embed.add_field(name = "__Language__", value = x["Language"])
    embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
    embed.add_field(name = "__Type__", value = x["Type"])
    embed.set_footer(text = "Information from the OMDB API")
    await ctx.send(embed=embed)
@client.command(pass_context = True)
async def help(ctx):
    embed=discord.Embed(title="__Command Prefix__: %", description='', color=0XFF69B4)
    embed.add_field(name="__**Summary**__", value="**This is the official BOT of REFORMED server. You can't find this BOT anywhere than here. This BOT is made in memory of JOKER \n And this BOT can't be distributed to anyone \n \n \n**", inline=True)
    embed.add_field(name="__**Commands**__", value="__**Fun Commands**__ \n `quote` - Quote of Joker \n `fams` - Random DragonBall Z GIF \n `marvel` - Random Marvel GIF \n `dc` - Random DC GIF \n `joker` - Random Joker GIF (Tribute to Heath Ledger) \n`meme` - Random funny meme \n `movie <movie name>` - Gives info of the particular movie you have searched \n \n __**Bot and server releated commands**__ \n `botinfo` - Information about this BOT \n `serverinvite` - Server invitation link \n \n __**Misc Commands**__ \n `avatar` - Avatar of the user \n `avatar <user>` - Avatar of mentioned user \n \n __**Admin Commands**__ \n `poll` - Polling (Administrator) \n `askquestion` - Asking of funny question (Administrator) \n `announce <channel> <matter>` - To announce the entered matter (Administrator) \n \n **More Feautures coming soon...** \n \n __**BOT will be offline someties... That means we are updating BOT**__ \n **Thank you for using this BOT**")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.TextChannel=None, *, msg: str):
    if channel is None:
        await ctx.send(" ```Proper usage is\n\nannounce<channel><matter>```")
    else:
        await channel.send(msg)

@client.command(pass_context=True)
async def rule1(ctx):
    rule1 = f"**Server rule 1: Follow the discord ToS. Any violations of the terms of service will result in an immediate ban! (Ban) The ToS can be found here:** https://discordapp.com/terms"
    await ctx.trigger_typing()
    await ctx.send(rule1)

@client.command(pass_context=True)
async def rule2(ctx):
    rule2= "** Server rule 2: What happens in Reformed stays in Reformed. Don't talk about how this server is better and vice versa, don't talk about the mods and how they are bad, dont ask me for unbans, dont talk shit about the members there, etc etc. (Warn/mute, ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule2)

@client.command(pass_context=True)
async def rule3(ctx):
    channel = ctx.message.channel
    rule3 = "**Server rule 3: Swearing is allowed, but please keep it to a limit! Usage of banned words is not allowed! List is found here: https://cdn.discordapp.com/attachments/414216301771358208/454122060751437826/Screen_Shot_2018-05-23_at_6.03.31_PM-1.png (Warn, mute, ban)**"
    await ctx.trigger_typing()
    await channel.send(rule3)

@client.command(pass_context=True)
async def rule4(ctx):
    channel2 = client.get_channel(565770888449097748)
    rule4 = "**Server rule 4: Image posting is not allowed anywhere except in {}. Posting the same message/emote as other users repeatedly is not allowed. (Warn, mute, kick/ban) Excessive spamming of random characters/images is categorized as a raid and will lead to a (Ban)**".format(channel2.mention)
    await ctx.trigger_typing()
    await ctx.send(rule4)

@client.command(pass_context=True)
async def rule5(ctx):
    rule5 = "**Server rule 5: Rudeness towards other members or trolling is not allowed! (Warn, mute, kick/ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule5)

@client.command(pass_context=True)
async def rule6(ctx):
    channel = ctx.message.channel
    rule6 = "**Server rule 6: Harrassment is not allowed here! (Mute, kick/ban)**"
    await ctx.trigger_typing()
    await channel.send(rule6)

@client.command(pass_context=True)
async def rule7(ctx):
    channel = ctx.message.channel
    rule7 = "**Server rule 7: Disrespect towards members is not allowed! (Warn/mute, kick/ban)**"
    await ctx.trigger_typing()
    await channel.send(rule7)

@client.command(pass_context=True)
async def rule8(ctx):
    rule8 = "**Server rule 8: Impersonation of other members is not allowed! (Warn, kick/ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule8)

@client.command(pass_context=True)
async def rule9(ctx):
    channel= ctx.message.channel
    rule9 = "**Server rule 9: Discriminatory behavior like racism and sexism is not allowed here. (Warn/mute, ban)**"
    await ctx.trigger_typing()
    await channel.send(rule9)

@client.command(pass_context=True)
async def rule10(ctx):
    rule10 = "**Server rule 10: NSFW (even if the image is cropped or blurred) or inappropriate images in this server are not allowed anywhere. (Warn, kick/ban: Ban for illegal content)**"
    await ctx.trigger_typing()
    await ctx.send(rule10)

@client.command(pass_context=True)
async def rule11(ctx):
    rule11 = "**Server rule 11: DDoSing or revealing personal info about a member without their consent is not allowed. (Kick/ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule11)

@client.command(pass_context=True)
async def rule12(ctx):
    rule12 = "**Server rule 12: Vulgar or inappropriate names/nicknames are not allowed (warn/kick/ban**"
    await ctx.trigger_typing()
    await ctx.send(rule12)

@client.command(pass_context=True)
async def rule13(ctx):
    rule13 = "**Server rule 13: Advertising in this server without staff permission is not allowed! (Warn, kick/ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule13)

@client.command(pass_context=True)
async def rule14(ctx):
    rule14 = "**Server rule 14: Joking about sensitive subjects such as rape, suicide/self-harm, death, serious illnesses, etc is not allowed!  (Warn, mute, ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule14)

@client.command(pass_context=True)
async def rule15(ctx):
    rule15 = "**Server rule 15: DM Advertising is not allowed at all! (Warn, ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule15)

@client.command(pass_context=True)
async def rule16(ctx):
    rule16 = "**Server rule 16: Bullying members in any way or form is not allowed (Warn, ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule16)

@client.command(pass_context=True)
async def rule17(ctx):
    rule17 = "**Server rule 17: Leaving the server to evade mutes, warns, etc will result in double the punishment! (Warn/Mute x2, Ban)**"
    await ctx.trigger_typing()
    await ctx.send(rule17)

@client.command(pass_context=True)
async def rule18(ctx):
    rule18 = "**Server rule 18: Alternative Accounts are not allowed! Only Owners and Admins are allowed to have alts for testing purposes mainly. Those caught with an Alternative Account may result in both accounts being Banned.**"
    await ctx.trigger_typing()
    await ctx.send(rule18)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def lock(ctx, Role:discord.Role= None, channel:discord.TextChannel=None):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = False
    overwrite.read_message_history = False
    await channel.set_permissions(Role, overwrite = overwrite)
    await ctx.send(f"**{channel.mention} has been locked for** `{Role.name}`")

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def unlock(ctx, Role:discord.Role=None, Channel:discord.TextChannel=None):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    overwrite.read_message_history = True
    await Channel.set_permissions(Role, overwrite = overwrite)
    await ctx.send(f"**{Channel.mention} has been unlocked for** `{Role.name}`")

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def test3(ctx):
    choices = ["DcssawdeS", "Sasdawdd", "AWSdasdwaA", "AdwASwAas", "AsdWDAasas", "ASDwdAsad", "MKiojmkomM"]
    choices2 = random.choice(choices)
    role = discord.utils.get(ctx.guild.roles, id=549265886100586506)
    embed = discord.Embed(title=" ", description=f"**Welcome to {ctx.guild.name}, In order to send any message in the server, You must verify as per the server's policy. Sorry for bothering you but it's my duty though.... And please follow the instructions below. I'm sure that the instructions will be easy for you... Wait 10 seconds for next message.**", color=0XFF69BF)
    embed.set_author(name=f"Verification for {ctx.guild.name}**", icon_url=ctx.guild.icon_url)
    embed.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
    embed2 = discord.Embed(title=" ", description="**You've to type the word shown in the next message correctly. And you've got only three chances. If you failed to enter correct word, Then you'll get kicked from server and you've to join again... Wait 10 seconds for next message**", color=0XFF69BF)
    embed2.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
    embed2.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
    embed3 = discord.Embed(title=f"**This is your first attempt (Two remaining)... Type the word shown below correctly... You've got 60 seconds only \n \n {choices2}**", description=" ", color=0XFF69BF)
    embed3.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
    embed3.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    await asyncio.sleep(10)
    await ctx.send(embed=embed2)
    await asyncio.sleep(10)
    await ctx.send(embed=embed3)
    msg2 = await client.wait_for('message', timeout=None)
    if msg2.content == choices2:
        embed4 = discord.Embed(title=f"**Yayy!!! You've made it you've got {role} role enjoy your stay in {ctx.guild.name} server... Thanks for supporting us**", description=" ", color=0XFF69BF)
        embed4.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed4)
        await ctx.author.add_roles(role)
    else:
        choices3 = random.choice(choices)
        embed5 = discord.Embed(title=f"**You've typed the wrong word... This is your second attempt (One remaining)... Type the word shown below correctly... You've got 60 seconds only \n \n {choices3} \n \n**", description=" ", color=0XFF69BF)
        embed5.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed5.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed5)
        msg3 = await client.wait_for('message', timeout=None)
        if msg3.content == choices3:
            embed4 = discord.Embed(title=f"**Yayy!!! You've made it you've got {role} role enjoy your stay in {ctx.guild.name} server... Thanks for supporting us**", description=" ", color=0XFF69BF)
            embed4.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
            embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed4)
            await ctx.author.add_roles(role)
        else:
            choices4 = random.choice(choices)
            embed6 = discord.Embed(title=f"**You've typed the wrong word... This is your last attempt... Type the word shown below correctly.. If yout typed wrong you'll get kicked from server... \n \n {choices4} \n \n**", description=f" ", color=0XFF69BF)
            embed6.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
            embed6.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed6)
            msg4 = await client.wait_for('message', timeout=None)
            if msg4.content == choices4:
                embed4 = discord.Embed(title=f"**Yayy!!! You've made it you've got {role} role enjoy your stay in {ctx.guild.name} server... Thanks for supporting us**", description=" ", color=0XFF69BF)
                embed4.set_author(name=f"Verification for {ctx.guild.name}", icon_url=ctx.guild.icon_url)
                embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed4)
                await ctx.author.add_roles(role)
            else:
                await ctx.send("**You've entered a wrong word agian.... Your attempts are over... You've been kicked out of this server**")
                return

@client.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def tempmute(ctx, user: discord.Member, num: int, time: str, reason:str):
    role = discord.utils.get(ctx.guild.roles, id=520653530529398784)

    if time == 'm':
        duration = num*60
        await user.add_roles(role)
        await ctx.send(f"{user.mention} is muted for {num} minutes for {reason}")
        await asyncio.sleep(duration)
        await user.remove_roles(role)
        await ctx.send(f"Congractulations {user.mention}, you are unmuted after {num} minute(s). Don't try to get mute again..")
    
    elif time == 'hr':
        duration = num*3600
        await user.add_roles(role)
        await ctx.send(f"{user.mention} is muted for {num} minutes for {reason}")
        await asyncio.sleep(duration)
        await user.remove_roles(role)
        await ctx.send(f"Congractulations {user.mention}, you are unmuted after {num} hour(s). Don't try to get mute again..")
    
    elif time == 'd':
        duration = num*86400
        await user.add_roles(role)
        await ctx.send(f"{user.mention} is muted for {num} minutes for {reason}")
        await asyncio.sleep(duration)
        await user.remove_roles(role)
        await ctx.send(f"Congractulations {user.mention}, you are unmuted after {num} day(s). Don't try to get mute again..")


@client.command(pass_context = True)
async def spotify(ctx, user: discord.Member=None):
    if user is None:
        user = ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(title=f" ", description=f"{user.mention} is listening to...", color=activity.color)
                embed.add_field(name="**Title**", value=activity.title, inline=False)
                embed.add_field(name="**Artist**", value=activity.artist, inline=False)
                embed.add_field(name="**Album**", value=activity.album, inline=False)
                embed.add_field(name="**Duration**", value=activity.duration, inline=False)
                embed.add_field(name="**Track ID**", value=activity.track_id, inline=False)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.set_author(name=user.name, icon_url=user.avatar_url)
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            
    else:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(title=f" ", description=f"{user.mention} is listening to...", color=activity.color)
                embed.add_field(name="**Title**", value=activity.title, inline=False)
                embed.add_field(name="**Artist**", value=activity.artist, inline=False)
                embed.add_field(name="**Album**", value=activity.album, inline=False)
                embed.add_field(name="**Duration**", value=activity.duration, inline=False)
                embed.add_field(name="**Track ID**", value=activity.track_id, inline=False)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.set_author(name=user.name, icon_url=user.avatar_url)
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            
           
@client.command(pass_context=True)
async def search(ctx, name:str):
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
    client_id = "3de4994a8c99485ab153804b7cfa6ff4"
    client_secret = "b0c797bb009346e8b77608eadbfb3545"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.artist_top_tracks(name)
    for track in results['tracks'][:10]:
        print('track    : ' +track['name'])
        print('audio    : ' +track['preview_url'])
        print('cover art: ' +track['album']['images'][0]['url'])

@client.command(pass_context=True)
async def test2(ctx):
    choices = ["Hlo", "Hii", "Hello", "Test"]
    choices2 = random.choice(choices)
    role = discord.utils.get(ctx.guild.roles, id='516303012671520769')
    await ctx.send(f"Type {choices2}")
    msg2 = await client.wait_for('message')
    if msg2.content == choices2:
        await ctx.send("**Well, You've made it....**")
        await ctx.message.author.add_roles(role)
    else:
        await ctx.send("**You've entered a wrong word.... Please try again...**")
        choices3 = random.choice(choices)
        await ctx.send(f"Type {choices3}")
        msg3 = await client.wait_for('message')
        if msg3.content == choices3:
            await ctx.send("**You've typed correct this time...**")
            await ctx.message.author.add_roles(role)
            return
        else:
          await ctx.send("**You've entered a wrong word.... Please try again... This is last attempt for you...**")
          choices4 = random.choice(choices)
          await ctx.send(f"Type {choices4}")
          msg4 = await client.wait_for('message')
        if msg4.content == choices4:
            await ctx.send("**You've typed correct this time...**")
            await ctx.message.author.add_roles(role)
            return
        else:
            await ctx.send("**You've entered a wrong word agian.... Your attempts are over... Please execute this cmd again**")
            await ctx.guild.kick(ctx.message.author)
            return

@client.command(pass_context=True)
@commands.has_permissions(manage_roles = True)
async def roleinfo(ctx, role: discord.Role=None):
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


client.run(os.getenv('TOKEN'))