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
import sqlite3
from dadjokes import Dadjoke
        
      
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="The Laughing Clown BOT", command_prefix=commands.when_mentioned_or("%"), pm_help = True)
client.remove_command('help')

            
@client.event
async def on_ready():
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    game = discord.Streaming(name="Nothing", url="https://www.twitch.tv/twitch")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(pass_context = True)
async def hlo(ctx):
    await ctx.send(f"Hello, How's your day today? {ctx.message.author.mention}")

@client.command(pass_context = True)
async def quote(ctx):
    choices = ["**Smile, because it confuses people. Smile, because it's easier than explaining what is killing you inside. - THE JOKER**", "**As you know, madness is like gravity...all it takes is a little push. - THE JOKER**", "**If you’re good at something, never do it for free. - THE JOKER**", "**Nobody panics when things go “according to plan”. Even if the plan is horrifying! - THE JOKER**", "**Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos... - THE JOKER**", "**Do I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it! You know, I just... *do* things. - THE JOKER**", "**What doesn't kill you, simply makes you stranger! - THE JOKER**", "**Why so serious? >:) - THE JOKER**", "**They Laugh At me Because I'm Different. I laugh At Them Because The're all the same - THE JOKER**", "**Their morals, their code; it's a bad joke. Dropped at the first sign of trouble. They're only as good as the world allows them to be. You'll see- I'll show you. When the chips are down these, uh, civilized people? They'll eat each other. See I'm not a monster, I'm just ahead of the curve. - THE JOKER**", "**The only sensible way to live in this world is without rules. - THE JOKER**"]
    embed = discord.Embed(title = " ", description = "**RIP Heath Ledger.... You've gave us a memorable gift like JOKER... We can't forget you...**", color=ctx.author.color)
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
    embed=discord.Embed(title="Details of this BOT...", description="Here are the details of this BOT below", color=ctx.author.color)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f"This is Official BOT of {ctx.guild.name} server")
    embed.add_field(name="__**Creator**__", value=User.mention, inline = True)
    embed.add_field(name="__**Special Thanks To**__", value=f"{User2.mention} \n {User3.mention} \n {User4.mention}")
    embed.add_field(name="**Currently connected servers**", value="1", inline = True)
    embed.add_field(name="**Currently connected users**", value=str(len(set(client.get_all_members()))), inline = True)
    embed.add_field(name="If you have any queries about this BOT, DM me...", value=User.mention)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def userid(ctx):
    await ctx.send(f"{ctx.message.author.id}")

@client.command(pass_context = True)
async def fams(ctx):
    api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=dragon ball z&rating=G&lang=en"
    data = requests.get(api_address).json()
    gif_url = data['data']['image_original_url']
    title = data['data']['title']
    embed = discord.Embed(title="Hey ya fams... Here's random gif from DBZ universe...", description=title, color=ctx.author.color)
    embed.set_image(url=gif_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        user = await client.fetch_user('587548678747717652')
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await ctx.send(embed=embed)

@client.command(pass_context = True)
async def avatar2(ctx, *, id1:str=None):
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
        user = await client.fetch_user(id1)
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=ctx.author.color)
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await ctx.send(embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options:str):
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

@client.command(pass_context = True)
async def marvel(ctx):
    api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=marvel&rating=G&lang=en"
    data = requests.get(api_address).json()
    gif_url = data['data']['image_original_url']
    matter = f"[Click me if the gif didn't loaded](gif_url)"
    title = data['data']['title']
    embed = discord.Embed(title="Excelsior!!! Here's the random GIF from Marvel Universe", description=title, color=ctx.author.color)
    embed.set_image(url=gif_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def dc(ctx):
    api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=dceu&rating=G&lang=en"
    data = requests.get(api_address).json()
    gif_url = data['data']['image_original_url']
    matter = f"[Click me if the gif didn't loaded](gif_url)"
    title = data['data']['title']
    embed = discord.Embed(title="Hey Kryptonian... Here's random gif from DC universe...", description=title, color=ctx.author.color)
    embed.set_image(url=gif_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)



@client.command(pass_context = True)
async def joker(ctx):
    choices = ['https://media.giphy.com/media/KZd26L2o8QXtK/giphy.gif', 'https://media.giphy.com/media/aazZrFTMrDKLK/giphy.gif', 'https://media.giphy.com/media/F0A48Q2wFjE7S/giphy.gif', 'https://media.giphy.com/media/7waKDy5RbDYVG/giphy.gif', 'https://media.giphy.com/media/13m24iFmhomZi0/giphy.gif', 'https://media.giphy.com/media/zCP1GdPjxtCTe/giphy.gif', 'https://media.giphy.com/media/tN2OR1R1BLKV2/giphy.gif', 'https://media.giphy.com/media/X9Z0O2bpi8GMU/giphy.gif', 'https://media.giphy.com/media/YPIrsRqqO7oB2/giphy.gif', 'https://media.giphy.com/media/FSp1Wqx2TPYSA/giphy.gif', 'https://media.giphy.com/media/8UwEdwAF5XWQE/giphy.gif']
    embed=discord.Embed(title="Hello Joker fan... Here's a GIF for you...", description="Tribute to the legendary **Heath Ledger**", color=ctx.author.color)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    
@client.command(pass_context = True)
async def naruto(ctx):
    api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=naruto&rating=G&lang=en"
    data = requests.get(api_address).json()
    gif_url = data['data']['image_original_url']
    matter = f"[Click me if the gif didn't loaded](gif_url)"
    title = data['data']['title']
    embed = discord.Embed(title=f"Hey ya {ctx.author.name}, Here's the random GIF from Naruto Universe", description=title, color=ctx.author.color)
    embed.set_image(url=gif_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)


@client.command(pass_context = True)
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Meme',color=ctx.author.color)
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
async def clear(ctx, number: int = None):
    try:
        channel = client.get_channel(557273459244269582)
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
   
 
    await ctx.delete_messages(mgs)
    
@client.command(pass_context = True)
async def p(ctx, *, word:str=None):
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

    
@client.command(pass_context = True)
async def P(ctx, *, word:str=None):
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

    
@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
    await ctx.trigger_typing()
    if name is None:
        embed=discord.Embed(description = "Please specify a movie, *eg. ``%movie Bohemian Rhapsody``*", color = ctx.author.color)
        await ctx.send(embed=embed)
    key = "4210fd67"
    url = "http://www.omdbapi.com/?t={}&apikey={}&plot=full".format(name, key)
    response = requests.get(url)
    x = json.loads(response.text)
    embed=discord.Embed(title =x['Title'], description = "Here is your movie {}".format(ctx.message.author.name), color = ctx.author.color)
    if x["Poster"] != "N/A":
     embed.set_thumbnail(url = x["Poster"])
    embed.add_field(name = "__Title__", value = x["Title"])
    embed.add_field(name = "__Released__", value = x["Released"])
    embed.add_field(name = "__Rated__", value = x["Rated"])
    embed.add_field(name = "__Runtime__", value = x["Runtime"])
    embed.add_field(name = "__Genre__", value = x["Genre"])
    embed.add_field(name = "__Director__", value = x["Director"])
    embed.add_field(name = "__Writer__", value = x["Writer"])
    embed.add_field(name = "__Actors__", value = x["Actors"])
    embed.add_field(name = "__Plot__", value = x["Plot"])
    embed.add_field(name = "__Released Countries__", value = x["Country"])
    embed.add_field(name = "__Language__", value = x["Language"])
    embed.add_field(name = "__IMDB Votes__", value = x["imdbVotes"])
    embed.add_field(name = x["Ratings"][1]["Source"], value = x["Ratings"][1]["Value"])
    embed.add_field(name = x["Ratings"][2]["Source"], value = x["Ratings"][2]["Value"])
    embed.add_field(name = "__Awards__", value = x['Awards'])
    embed.add_field(name = "__Box Office__", value = x['BoxOffice'])
    embed.add_field(name = "__DVD Release__", value = x["DVD"])
    embed.add_field(name = "__Production__", value = x["Production"])
    embed.add_field(name = "__Website__", value = x["Website"])
    embed.add_field(name = "__Type__", value = x["Type"])
    embed.set_footer(text = "Information from the OMDB API")
    await ctx.send(embed=embed)
 
@client.command(pass_context=True)
async def help(ctx, name: str=None):
    if name == None:
        embed = discord.Embed(title="Main help centre of The Laughing Clown Bot...", description="Do ``%help <category>`` for detailed help of that category... Categories are given below select one of them", color=ctx.author.color)
        embed.add_field(name="fun", value="Shows fun commands", inline=False)
        embed.add_field(name="admin", value="Shows admin commands", inline=False)
        embed.add_field(name="bot", value="Shows bot related commands", inline=False)
        embed.add_field(name="misc", value="Shows miscallenous commands", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.trigger_typing()
        await asyncio.sleep(5)
        await ctx.send(embed=embed)
    elif name == "fun":
        embed = discord.Embed(title="Welcome to fun category...", description="Skip <> and (). you don't have to use these while using a command...", color=ctx.author.color)
        embed.add_field(name="quote", value="Gives random quote of Joker from Dark Knight movie \nUsage: ``%quote``", inline=False)
        embed.add_field(name="userid", value="Gives the user id of the user \nUsage: ``%userid <user. If user is none it returns the id of the author>``", inline=False)
        embed.add_field(name="fams", value="Random Dragon Ball Z gif \nUsage: ``%fams``", inline=False)
        embed.add_field(name="marvel", value="Gives random Marvel Universe \nUsage: ``%marvel``", inline=False)
        embed.add_field(name="dc", value="Random DC Universe gif \nUsage: ``%dc``", inline=False)
        embed.add_field(name="naruto", value="Gives random gif of Naruto Universe \nUsage: ``%naruto``", inline=False)
        embed.add_field(name="meme", value="Gives random funny meme\nUsage: ``%meme``", inline=False)
        embed.add_field(name="8ball", value="Answers your 8ball question \nUsage: ``%8ball <question>``", inline=False)
        embed.add_field(name="joke", value="Says a funny joke \nUsage: ``%joke``", inline=False)
        embed.add_field(name='fact', value="Gives a random fact \nUsgae: ``%fact``", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(embed=embed)
    elif name == "admin":
        embed = discord.Embed(title="Welcome to admin/staff category...", description="Skip <> and (). you don't have to use these while using a command...", color=ctx.author.color)
        embed.add_field(name="clear", value="Clears the number of messages in that channel \nUsage: ``%clear <number>``", inline=False)
        embed.add_field(name="announce", value="Announces the entered matter in the desired channel \nUsage: ``%announce <channel> <matter>``", inline=False)
        embed.add_field(name="lock", value="Locks the specified channel for the specified role \nUsage: ``%lock <role> <channel>``", inline=False)
        embed.add_field(name="unlock", value="Unlocks the specified channel for the specified role \nUsage: ``%unlock <role> <channel>``", inline=False)
        embed.add_field(name="tempmute (not stable)", value="Mutes the member for certain amount of time \nUsage: ``%tempmute <user> <duration> <m/hr/d> <reason>``", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(embed=embed)
    elif name == "bot":
        embed2 = discord.Embed(title="Welcom to bot category...", description="Skip <> and (). you don't have to use these while using a command...", color=ctx.author.color)
        embed2.add_field(name="botinfo", value="Gives the information about the bot \nUsage: ``%botinfo``", inline=False)
        embed2.add_field(name="serverinfo", value=f"Gives the info about {ctx.guild.name} server \nUsage: ``%serverinfo``", inline=False)
        embed2.timestamp = datetime.datetime.utcnow()
        embed2.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(embed=embed2)
    elif name == "misc":
        embed = discord.Embed(title="Welcome to misc section...", description="Skip <> and (). you don't have to use these while using a command...", color=ctx.author.color)
        embed.add_field(name="movie", value="Gives the information of the particular movie \nUsage: ``%movie <moviename>``", inline=False)
        embed.add_field(name="roleinfo", value="Gives info of that particular role (To use this command, You've to got 'Manage Roles' permission. \nUsage: ``%roleinfo <rolename>``")
        embed.add_field(name="anime", value="Gives info about the anime show that you've searched. \nUsage: ``%anime <show name>``")
        embed.add_field(name="urban", value="Searches the given word in 'Urban Dictionary' website. \nUsage: ``%urban <word>``")
        embed.add_field(name="lyrics", value="Sends the searched lyrics to your DM \nUsage: ``%lyrics <song name>``")
        embed.add_field(name="syn", value="Gives the synonyms of the word that you've entered \nUsage: ``%syn <word>``")
        embed.add_field(name="define", value="Gives the definitions of the word that you've entered \nUsage: ``%define <word>``")
        embed.add_field(name="talk", value="It's simple, It activates the chatbot and replies to your messages \nUsage: ``%t <message>``")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(embed=embed)
    else:
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send("I can't find the category, make sure you typed it right...")

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
@commands.has_permissions(ban_members = True)
async def tempmute(ctx, user: discord.Member, num: int, time: str, reason:str):
    role = discord.utils.get(ctx.guild.roles, id=643412756946485268)

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


@client.command(pass_context=True)
async def spotify(ctx, *, user:discord.Member=None):
    if user is None:
        user = ctx.author
    activity = user.activity
    if activity is None:
        await ctx.send("{} is not playing anything on spotify!".format(user.display_name))
        return
    if activity.type == discord.ActivityType.listening and activity.name == "Spotify":
        embed = discord.Embed(description="**React to :thumbsup: in 20 seconds to get the song's lyrics into your DMs**")
        embed.add_field(name="Artist(s)", value=", ".join(activity.artists))
        embed.add_field(name="Album", value=activity.album)
        embed.add_field(name="Track ID", value=activity.track_id)
        embed.add_field(name="Duration", value=str(activity.duration)[3:].split(".", 1)[0])
        embed.title = "**{}**".format(activity.title)
        embed.set_thumbnail(url=activity.album_cover_url)
        embed.url = "https://open.spotify.com/track/{}".format(activity.track_id)
        embed.color = activity.color
        embed.set_footer(text="{} - is currently playing this song".format(ctx.author))
        messaage = await ctx.send(embed=embed)
        await messaage.add_reaction(emoji="👍")
        await asyncio.sleep(2)
        artist = ", ".join(activity.artists)
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: reaction.emoji == '👍', timeout=20)
        try:
            con = f"{activity.title} {artist}"
            address = f"https://some-random-api.ml/lyrics?title={con}"
            data = requests.get(address).json()
            if 'error' in data:
                await ctx.send(f"**{data['error']}**")
            elif data['author'] in activity.artist:
                lyrics = data['lyrics']
                if len(lyrics) < 2048:
                    for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                        embed = discord.Embed(title=data['author'], description=f"{chunk} \n [Source website]({data['links']['genius']})", color=0XFF69BF)
                        embed.set_author(name=data['title'], url=data['thumbnail']['genius'])
                        embed.set_thumbnail(url=data['thumbnail']['genius'])
                        embed.timestamp = datetime.datetime.utcnow()
                        await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
                        await ctx.author.send(embed=embed)
                
                else:
                    await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
                    for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                        await ctx.author.send(chunk)
            else:
                await ctx.send("**Sorry, I could'nt find the lyrics of this song...**")
        except:
            return    
    else:
        await ctx.send("**Wait, You aren't listening any on spotify...**")
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
@client.event
async def on_message_delete(message):
    if message.guild.name == "Test":
        return
    else:
        
        if message.author.bot:
            channel = client.get_channel(557273459244269582)
            async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
                embed = discord.Embed(title="Message deleted", description=f"Message sent by {entry.target.mention}, deleted by {entry.user.mention}, in {message.channel.mention}", color=0XFF69BF)
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                return
    
        else:
            async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete): 
                channel = client.get_channel(557273459244269582)
                matter = f"Message sent by: {message.author.mention} deleted in {message.channel.mention} \n \n  {message.content}"
                embed = discord.Embed(title=f"{message.author.name}", description=matter, color=0XFF69BF)
                embed.set_footer(text=f"Author {message.author.id}  | Message ID: {message.id}")
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                if entry.user != message.author:
                    embed = discord.Embed(title="Message deleted", description=f"Message sent by {entry.target.mention}, deleted by {entry.user.mention}, in {message.channel.mention} \nMessage:\n{message.content}", color=0XFF69BF)
                    embed.timestamp = datetime.datetime.utcnow()
                    await channel.send(embed=embed)
                else:
                    return
        
@client.event
async def on_member_remove(member):
    if member.guild.name == "❄Virtual Reformed❄":
        channel = client.get_channel(565768324252958720)
        channel2 = client.get_channel(557273459244269582)
        userchannel = client.get_channel(571302888110817281)
        person_count = len([member for member in member.guild.members if not member.bot])
        embed=discord.Embed(title=f"Good bye {member.name}... Hope you'll come back again to {member.guild.name}", description="Thank you for being with us all these times...", color=0XFFFFFF)
        embed.set_thumbnail(url='https://media.giphy.com/media/LTFbyWuELIlqlXGLeZ/giphy.gif')
        embed.add_field(name="__**Members Remaining**__", value='{}'.format(str(member.guild.member_count)), inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed2=discord.Embed(title="Member Left", description= member.mention, color=0XFFFFFF)
        embed2.set_thumbnail(url=member.avatar_url)
        embed2.add_field(name="**Members Remaining**", value=str(member.guild.member_count), inline=True)
        embed2.set_footer(text=f"ID: {member.id}", icon_url=member.avatar_url)
        embed2.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
        await channel2.send(embed=embed2)
        await userchannel.edit(name= f"Weebs: {person_count}")
    else:
        return;

@client.event
async def on_member_join(member):
    channel3 = client.get_channel(557273459244269582)
    choices = ["DcssawdeS", "Sasdawdd", "AWSdasdwaA", "AdwASwAas", "AsdWDAasas", "ASDwdAsad", "MKiojmkomM"]
    choices2 = random.choice(choices)
    role = discord.utils.get(member.guild.roles, id=659304444575612948)
    embed = discord.Embed(title=" ", description=f"Welcome to {member.guild.name}, In order to send any message in the server, You must verify as per the server's policy. Sorry for bothering you but it's my duty though.... And please follow the instructions below. I'm sure that the instructions will be easy for you... Wait 10 seconds for next message.", color=0XFFFFFF)
    embed.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed2 = discord.Embed(title=" ", description="You've to type the word shown in the next message correctly. And you'vve got only three chances. If you failed to enter correct word, Then you'll get kicked from server and you've to join again... Wait 10 seconds for next message", color=0XFFFFFF)
    embed2.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed2.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed3 = discord.Embed(title=f"This is your first attempt (Two remaining)... Type the word shown below correctly... **\n \n {choices2} \n \n**", description=" ", color=0XFFFFFF)
    embed3.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
    embed3.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
    embed10 = discord.Embed(title="Successful Verification", description=f"{member.mention} got verified successfully, Welcome him/her.", color=0XFFFFFF)
    embed10.set_author(name=member.guild.name, icon_url=member.guild.icon_url)
    embed.timestamp = datetime.datetime.utcnow()
    await member.send(embed=embed)
    await asyncio.sleep(10)
    await member.send(embed=embed2)
    await asyncio.sleep(10)
    await member.send(embed=embed3)
    msg2 = await client.wait_for('message', check=lambda message: message.author == member)
    if msg2.content == choices2:
        embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFFFFFF)
        embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed4)
        await member.add_roles(role)
        await channel3.send(embed=embed10)
    else:
        choices3 = random.choice(choices)
        embed5 = discord.Embed(title=f"You've typed the wrong word... This is your second attempt (One remaining)... Type the word shown below correctly...** \n \n {choices3} \n \n**", description=" ", color=0XFFFFFF)
        embed5.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
        embed5.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
        await member.send(embed=embed5)
        msg3 = await client.wait_for('message', check=lambda message: message.author == member)
        if msg3.content == choices3:
            embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFFFFFF)
            embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed4)
            await member.add_roles(role)
            await channel3.send(embed=embed10)
        else:
            choices4 = random.choice(choices)
            embed6 = discord.Embed(title=f"You've typed the wrong word... This is your last attempt... Type the word shown below correctly.. If yout typed wrong you'll get kicked from server...** \n \n {choices4} \n \n**", description=" ", color=0XFFFFFF)
            embed6.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
            embed6.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
            await member.send(embed=embed6)
            msg4 = await client.wait_for('message', check=lambda message: message.author == member)
            if msg4.content == choices4:
                embed4 = discord.Embed(title=f"Yayy!!! You've made it you've got {role.name} role enjoy your stay in {member.guild.name} server... Thanks for supporting us", description=" ", color=0XFFFFFF)
                embed4.set_author(name=f"Verification for {member.guild.name}", icon_url=member.guild.icon_url)
                embed4.set_footer(text=f"After this process you'll get {role.name} so that we sure you're verified", icon_url=member.avatar_url)
                await member.send(embed=embed4)
                await member.add_roles(role)
                await channel3.send(embed=embed10)
            else:
                await member.send("**You've entered a wrong word agian.... Your attempts are over... You've been kicked out of this server**")
                await asyncio.sleep(10)
                await member.guild.kick(member, reason="**Unsuccessful Verification**")
                embed = discord.Embed(title="Failed Verification", description=f"Failed verification by {member.mention}...", color=0XFFFFFF)
                embed.set_author(name=member.guild.name, icon_url=member.guild.icon_url)
                embed.timestamp = datetime.datetime.utcnow()
                await channel3.send(embed=embed)
                return
    gettime = discord.utils.snowflake_time(member.id)
    channel = client.get_channel(565766644140474368)
    channel2 = client.get_channel(557273459244269582)
    text_channel = client.get_channel(565767003533737985)
    userchannel = client.get_channel(571302888110817281)
    general = client.get_channel(565770475574394902)                                   
    person_count = len([member for member in member.guild.members if not member.bot])
    embed=discord.Embed(title=f"Welcome {member.name} to {member.guild.name}", description=f"**Hope you'll be active here... Read rules at {text_channel.mention} channel and don't break any of them...**", color=0XFFFFFF)
    embed.set_thumbnail(url='https://media.giphy.com/media/OF0yOAufcWLfi/giphy.gif')
    embed.add_field(name="__**Thanks for joining our server**__", value="We hope you a good stay here....")
    embed.add_field(name="__**Time of joining**__", value=member.joined_at.date(), inline=True)
    embed.add_field(name="__**Joining position**__", value='{}'.format(str(member.guild.member_count)), inline=True)
    embed.add_field(name="__**User account created at**__", value=gettime.date(), inline=True)
    embed.set_footer(text=member.name, icon_url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed2=discord.Embed(title="Member Joined", description=member.mention, color=0XFFFFFF)
    embed2.add_field(name="**Members Remaining**", value=str(member.guild.member_count), inline=True)
    embed2.set_footer(text=f"ID: {member.id}", icon_url=member.avatar_url)
    embed2.timestamp = datetime.datetime.utcnow()
    message = f"Welcome {member.mention} \n\n🔹***U made it over the waves and storm and arrived at Virtual Reformed🔸 \n🔶please read the rules in <#565767003533737985>,then stop by <#565767249793777696> to set yourself some role and feel free to also stop by <#565900253673553924> and tell us a little about yourself***🔷"                                  
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed3 = discord.Embed(title=" ",description=message, color = discord.Color((r << 16) + (g << 8) + b))
    embed3.set_author(name=member.guild.name, icon_url=member.guild.icon_url)
    embed3.set_footer(text=f"{member.guild.name} Welcomes you, {member.name}.", icon_url=member.avatar_url)
    embed3.set_image(url="https://cdn.discordapp.com/attachments/591824738884648960/667815130934935572/1579289920706.jpg")
    await channel.send(embed=embed)
    await channel2.send(embed=embed2)
    await general.send(embed=embed3)                                   
    await userchannel.edit(name= f" :small_orange_diamond: ┋Reformers: {person_count}")
    
@client.event
async def on_message_edit(before,after):
    db = sqlite3.connect('first2.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT log_channel FROM first WHERE guild_id = {after.guild.id}")
    result = cursor.fetchone()
    res = ", ".join(result)                                   
    channel = client.get_channel(int(res))                                   
    if result is None:
        return()
    elif result is not None:
        if before.content != after.content:
                matter = f"**Message edited in {before.channel.mention} **[Jump to message](https://discordapp.com/channels/{before.guild.id}/{after.channel.id}/{after.id})"
                embed = discord.Embed(title=f"{before.author.name}", description=matter, color=0XFFFFFF)
                embed.add_field(name="Before", value=before.content, inline=False)
                embed.add_field(name="After", value=after.content, inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=f"ID: {before.id}")
                await channel.send(embed=embed)                                    
        elif after.author.bot:
            return
@client.event
async def on_guild_channel_create(channel):
    if channel.guild.name == "Test":
        return;
    else:
        channel2 = client.get_channel(557273459244269582)
        embed = discord.Embed(title="New Channel Created", description=f"**Channel Created: {channel.mention}**", color=0XFFFFFF)
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"ID: {channel.id}")

        await channel2.send(embed=embed)

@client.event
async def on_guild_channel_delete(channel):
    if channel.guild.name == "Test":
        return;
    else:
        channel2 = client.get_channel(557273459244269582)
        embed = discord.Embed(title="Channel Deleted", description=f"**Channel Deleted: {channel.name}**", color=0XFFFFFF)
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"ID: {channel.id}")

        await channel2.send(embed=embed)

@client.event
async def on_guild_channel_update(before, after):
    if before.guild.name == "Test":
        return;
    else:
        channel2 = client.get_channel(557273459244269582)
        if before.name != after.name:
            embed = discord.Embed(title="Channel Name Edited", description=" ", color=0XFFFFFF)
            embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
            embed.add_field(name="Before", value=before.name, inline=False)
            embed.add_field(name="After", value=after.name, inline=False)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"ID: {after.id}")
            await channel2.send(embed=embed)

        elif before.topic != after.topic:
            embed2 = discord.Embed(title="Channel Topic Edited", description=f"Channel edited: {after.mention} ", color=0XFFFFFF)
            embed2.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
            embed2.add_field(name="Before", value=before.topic, inline=False)
            embed2.add_field(name="After", value=after.topic, inline=False)
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=f"ID: {after.id}")
            await channel2.send(embed=embed2)

@client.command(pass_context = True)
async def rules(ctx):
    channel2 = client.get_channel(565770888449097748)
    rule_1 = f"Follow the discord ToS. Any violations of the terms of service will result in an immediate ban! (Ban) The ToS can be found here: [Discord ToS](https://discordapp.com/terms)"
    rule_2= "What happens in Reformed stays in Reformed. Don't talk about how this server is better and vice versa, don't talk about the mods and how they are bad, dont ask me for unbans, dont talk shit about the members there, etc etc. (Warn/mute, ban)"
    rule_3 = "Swearing is allowed, but please keep it to a limit! Usage of banned words is not allowed! List is found here: [Click here](https://cdn.discordapp.com/attachments/414216301771358208/454122060751437826/Screen_Shot_2018-05-23_at_6.03.31_PM-1.png) (Warn, mute, ban)"
    rule_4 = "Image posting is not allowed anywhere except in {}. Posting the same message/emote as other users repeatedly is not allowed. (Warn, mute, kick/ban) Excessive spamming of random characters/images is categorized as a raid and will lead to a (Ban)".format(channel2.mention)
    rule_5 = "Rudeness towards other members or trolling is not allowed! (Warn, mute, kick/ban)"
    rule_6 = "Harrassment is not allowed here! (Mute, kick/ban)"
    rule_7 = "Disrespect towards members is not allowed! (Warn/mute, kick/ban)"
    rule_8 = "Impersonation of other members is not allowed! (Warn, kick/ban)"
    rule_9 = "Discriminatory behavior like racism and sexism is not allowed here. (Warn/mute, ban)"
    rule_10 = "NSFW (even if the image is cropped or blurred) or inappropriate images in this server are not allowed anywhere. (Warn, kick/ban: Ban for illegal content)"
    rule_11 = "DDoSing or revealing personal info about a member without their consent is not allowed. (Kick/ban)"
    rule_12 = "Vulgar or inappropriate names/nicknames are not allowed (warn/kick/ban)"
    rule_13 = "Advertising in this server without staff permission is not allowed! (Warn, kick/ban)"
    rule_14 = "Joking about sensitive subjects such as rape, suicide/self-harm, death, serious illnesses, etc is not allowed!  (Warn, mute, ban)"
    rule_15 = "DM Advertising is not allowed at all! (Warn, ban)"
    rule_16 = "Bullying members in any way or form is not allowed (Warn, ban)"
    rule_17 = "Leaving the server to evade mutes, warns, etc will result in double the punishment! (Warn/Mute x2, Ban)"
    rule_18 = "Alternative Accounts are not allowed! Only Owners and Admins are allowed to have alts for testing purposes mainly. Those caught with an Alternative Account may result in both accounts being Banned"
    punishments = "**:beginner:  1 WARNING= NOTHING \n :beginner:  2 WARNINGS = MUTE FOR 12HR \n :beginner:  4 WARNINGS = MUTE FOR 1 WEEK \n :beginner:  10 WARNINGS = INSTANT KICK \n NOTE: SOFT SPAMS..U MAY GET MUTE BUT FOR HARMFUL SPAMS WILL GET U INSTANT BAN**"
    embed = discord.Embed(title="**CONSTITUTION OF THIS SERVER... JK RULES OF THIS SERVER...**", description=None, color=0XFFFFFF)
    embed.add_field(name="**:beginner:   Discord ToS apply... Coz he's the only boss here**", value=rule_1, inline=False)
    embed.add_field(name="**:beginner:   Keep it down**", value=rule_2, inline=False)
    embed.add_field(name="**:beginner:   No bad words please...**", value=rule_3, inline=False)
    embed.add_field(name="**:beginner:   We have a seperate channel for posting images and links...**", value=rule_4, inline=False)
    embed.add_field(name="**:beginner:   We don't support any type of trolling**", value=rule_5, inline=False)
    embed.add_field(name="**:beginner:   Don't harrass any wumpus around this server...**", value=rule_6, inline=False)
    embed.add_field(name="**:beginner:   Always give respect and take respect..**", value=rule_7, inline=False)
    embed.add_field(name="**:beginner:   Be who you are...**", value=rule_8, inline=False)
    embed.add_field(name="**:beginner:   All are equal here...**", value=rule_9, inline=False)
    embed.add_field(name="**:beginner:   This server is SFW not NSFW...**", value=rule_10, inline=False)
    embed.add_field(name="**:beginner:   This is no place for HACKERS...**", value=rule_11, inline=False)
    embed.add_field(name="**:beginner:   Everyone got their name, Don't create any new...**", value=rule_12, inline=False)
    embed.add_field(name="**:beginner:   You've got other ways to advertise...**", value=rule_13, inline=False)
    embed.add_field(name="**:beginner:   Joke about any good things...**", value=rule_14, inline=False)
    embed.add_field(name="**:beginner:   We can't tolerate this type of advertising...**", value=rule_15, inline=False)
    embed.add_field(name="**:beginner:   Bullying is a childish act btw...**", value=rule_16, inline=False)
    embed.add_field(name="**:beginner:   Don't try to avoid the punishment**", value=rule_17, inline=False)
    embed.add_field(name="**:beginner:   We don't want twins here...**", value=rule_18, inline=False)
    embed.add_field(name="** \n \n Well, If you broke any rules above, You'll get warning or Instant Kick/Ban based on how severe your actions are... And the punishments decided by staff are as follows...**", value=punishments, inline=False)
    embed.add_field(name="**:beginner:   Final Words...**", value="Well, The constitution will be amended frequently, If you have any concerns about rules... You can contact any staff around here...", inline=False)
    await ctx.send(embed=embed)
    
@client.command(pass_context=True)
async def anime(ctx, *, name:str = None):
    api_address = f"https://kitsu.io/api/edge/anime?filter[text]={name}"
    data = requests.get(api_address).json()
    url = data['data'][0]['links']['self']
    data2 = requests.get(url).json()
    end_date = data2['data']['attributes']['endDate']
    synopsis = data2['data']['attributes']['synopsis']
    if len(synopsis) > 1024:
        synopsis = "Oh no! The length of synopsis is very large, I can't print it here"
    else:
        synopsis = synopsis
    if end_date == None:
        end_date = "Not finished yet"
    else:
        end_date = end_date
    ytlink = data2['data']['attributes']['youtubeVideoId']
    await ctx.trigger_typing()
    embed = discord.Embed(title="Here's the anime show that you've searched for...", color=ctx.author.color)
    embed.add_field(name="Name", value=f"{data2['data']['attributes']['titles']['en'] } ({data2['data']['attributes']['titles']['ja_jp']})")
    embed.add_field(name="Synopsis", value=synopsis)
    embed.add_field(name="Average Rating", value=data2['data']['attributes']['averageRating'])
    embed.add_field(name="Start Date", value=data2['data']['attributes']['startDate'])
    embed.add_field(name="End Date", value=end_date)
    embed.add_field(name="Age Rating", value=data2['data']['attributes']['ageRating'])
    embed.add_field(name="Age Rating Guide", value=data2['data']['attributes']['ageRatingGuide'])
    embed.add_field(name="Type of Media", value=data2['data']['attributes']['subtype'])
    embed.add_field(name="Status", value=data2['data']['attributes']['status'])
    embed.set_thumbnail(url=data2['data']['attributes']['posterImage']['original'])
    embed.add_field(name="Episode Count", value=data2['data']['attributes']['episodeCount'])
    embed.add_field(name="Episode Length", value=data2['data']['attributes']['episodeLength'])
    embed.add_field(name="Youtube link", value=f"[Click here for trailer](https://www.youtube.com/watch?v={ytlink})")
    embed.add_field(name="NSFW", value=data2['data']['attributes']['nsfw'])
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested By | {ctx.author.name}")
    await ctx.send(embed=embed)
                 
@client.command(pass_context=True, aliases=["8ball"])
async def roll8ball(ctx, *, question: str = None):
    if question is None:
        await ctx.send("This ain't rocket science kiddo!!. Ask a question...")
    else:
        address = f"https://8ball.delegator.com/magic/JSON/{question}"
        data = requests.get(address).json()
        answer = data['magic']['answer']
        msg = await ctx.send(content=":8ball: | Joker is shaking the ball.")
        await asyncio.sleep(1)
        await msg.edit(content=":8ball: | Joker is shaking the ball..")
        await asyncio.sleep(1)
        await msg.edit(content=":8ball: | Joker is shaking the ball...")
        await asyncio.sleep(1)
        await msg.edit(content=f":8ball: | {answer}.")
                    
@client.command(pass_context=True)
async def urban(ctx, *, word: str = None):
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
                     
@client.command(pass_context=True,)
async def joke(ctx):
    x = await ctx.send("Joker is thinking of a joke.")
    await asyncio.sleep(1)
    await x.edit(content="Joker is thinking of a joke..")
    await asyncio.sleep(1)
    await x.edit(content="Joker is thinking of a joke...")
    await asyncio.sleep(1)
    res = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    if res.status_code == requests.codes.ok:
        await x.edit(content=str(res.json()['joke']))
    else:
        await x.edit(context="Joker can't think of any joke now... Try again.")    
                                          
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)               
async def rather(ctx):
    channel = client.get_channel(565770475574394902)
    address = "https://www.rrrather.com/botapi"
    data = requests.get(address).json()
    nsfw_check = data['nsfw']
    if nsfw_check == False:
        await channel.send(data['link'])
    elif nsfw_check == True:
        return                     

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mention(ctx):
    role = discord.utils.get(ctx.guild.roles, id=586517857572225054)
    if role.mentionable == True:
        await role.edit(mentionable=False)
        await ctx.send(f"{role.name} is unmentionable now...")
    else:
        await role.edit(mentionable=True)
        await ctx.send(f"{role.name} is mentionable now...")
                     
@client.command(pass_context=True)
async def lyrics(ctx, *, track:str = None):
    address = f"https://some-random-api.ml/lyrics?title={track}"
    data = requests.get(address).json()
    if 'error' in data:
        await ctx.send(f"**{data['error']}**")
    else:
        lyrics = data['lyrics']
        if len(lyrics) < 2048:
            for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                embed = discord.Embed(title=data['title'], description=f"{chunk}", color=ctx.author.color)
                embed.set_author(name=data['author'], url=data['thumbnail']['genius'])
                embed.url = data['links']['genius']
                embed.set_thumbnail(url=data['thumbnail']['genius'])
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
                await ctx.author.send(embed=embed)
        
        else:
            await ctx.send(f"**{ctx.author.name},** The lyrics of **{data['author']} - {data['title']}** is sent to your DM please check your DM's...")
            for chunk in [lyrics[i:i+2000] for i in range(0, len(lyrics), 2000)]:
                await ctx.author.send(chunk)   
                           
@client.command(pass_context=True)
async def define(ctx, *, word:str = None):
    if word == None:
        await ctx.send("Type any word to define...")
    else:
        address = f"https://some-random-api.ml/dictionary?word={word}"
        data = requests.get(address).json()
        definition = data['definition']
        await ctx.send(f"The definition of {data['word']} is sent to your DM")
        for chunk in [definition[i:i+2000] for i in range(0, len(definition), 2000)]:
            await ctx.author.send(chunk)
                       
@client.command(pass_context=True)
async def syn(ctx, *, word:str =None):
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
@client.command(pass_context=True)
async def t(ctx, message: str = None):
    if message == None:
        await ctx.send("**Joker can't talk to you unless you say anything to me ``%talk <message>``**")
    else:
        address = f"https://some-random-api.ml/chatbot/beta?message={message}"
        data = requests.get(address).json()
        reply = data['response']
        await ctx.trigger_typing()
        await ctx.send(reply)
                       
@client.command(pass_context=True)
async def event(ctx, *, msg: str):
    channel = client.get_channel(572851335603421194)
    message = await channel.send(f"** {ctx.author.mention} Suggested an event: {msg} **")
    await message.add_reaction(emoji='✅')
    await message.add_reaction(emoji='❎')
                                          
@client.command(pass_context=True)
async def quiz(ctx):
    categories = ["31", "15", "11", "14"]
    api_address = f"https://opentdb.com/api.php?amount=10&category={random.choice(categories)}"
    json_data = requests.get(api_address).json()
    ques = json_data['results'][0]['question']
    option1 = json_data['results'][0]['correct_answer']
    option2 = json_data['results'][0]['incorrect_answers'][0]
    option3 = json_data['results'][0]['incorrect_answers'][1]
    option4 = json_data['results'][0]['incorrect_answers'][2]
    options = option1 +", "+ option2 +", "+ option3 +", "+ option4
    options2 = option4 +", "+ option3 +", "+ option2 +", "+ option1
    options3 = option4 +", "+ option1 +", "+ option3 +", "+ option2
    options4 = option4 +", "+ option3 +", "+ option2 +", "+ option1
    choices = [options, options2, options3, options4]
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(f"Category: {json_data['results'][0]['category']} \nDifficulty: {json_data['results'][0]['difficulty']}")
    await ctx.send(ques.replace("&#039;", "'").replace('&quot;', '"').replace("&amp;", "&"))
    await ctx.send(random.choice(choices).replace("&#039;", "'").replace('&quot;', '"').replace("&amp;", "&"))
    try:
        msg = await client.wait_for('message', check= lambda message: message.author == ctx.author, timeout=20)
        if msg.content == json_data['results'][0]['correct_answer']:
            await ctx.send("**Yayy, You've got it right...**")
        else:
            await ctx.send(f"**Oh No, It's not the right answer... Correct answer is {json_data['results'][0]['correct_answer']}, Better luck next time.**")
    except asyncio.TimeoutError:
        await ctx.send(f"**Time's up. Correct answer is {json_data['results'][0]['correct_answer']}.**")

@client.command(pass_context=True)
async def fortune(ctx):
    address = "https://helloacm.com/api/fortune/"
    data = requests.get(address).json()
    msg = await ctx.send("Joker is busy writing your fortune.")
    await asyncio.sleep(1)
    await msg.edit(content="Joker is busy writing your fortune..")
    await asyncio.sleep(1)
    await msg.edit(content="Joker is busy writing your fortune...")
    await asyncio.sleep(1)
    await msg.edit(content=f"{data}")

@client.command(pass_context=True)
async def translate(ctx, lang1:str, *, text:str = None):
    address = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190924T172418Z.91b5d532be1a360c.fe80f58d74501b56a4750b18c0fb2ca74585fec3&text={text}&lang={lang1}"
    data1 = requests.get(address).json()
    embed = discord.Embed(title="\n", description=data1['text'][0], color=ctx.author.color)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=data1['lang'] , icon_url="https://cdn.discordapp.com/attachments/602215920257073303/635883351324098560/wRUezUX.png")
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(embed=embed)
                       
@client.command(pass_context=True)
async def gender(ctx, *, name:str = None):
    address = f"https://api.genderize.io/?name={name}"
    data = requests.get(address)
    data2 = data.json()
    if data.headers['X-Rate-Limit-Limit'] == 0:
        await ctx.send(f"**Try this command in {data.headers['X-Rate-Reset']/60} minutes**")
    else:
        if data2['gender'] == None:
            await ctx.trigger_typing()
            await asyncio.sleep(4)
            await ctx.send("** I can't say the gender of this name... Try using only name without initials or surnames \n Ex: Amanda, Kiran, Chris etc.,**")
        else:
            await ctx.trigger_typing()
            await asyncio.sleep(4)
            await ctx.send(f"** I'm {data2['probability']*100}% sure that {name} is a {data2['gender']} name**")

@client.command(pass_context=True)
async def weather(ctx, *, city:str=None):
    if city == None:
        await ctx.send("**Please enter any city name...**")
    else:
        address = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('open_weather')}&q={city}&units=metric"
        data = requests.get(address).json()
        if data['cod'] == "404":
            await ctx.send(f"**{data['message']}**")
        else:
            embed = discord.Embed(title="Weather Forecast...", description="Here's your weather forecast that you've requested", color=discord.Colour.blue())
            embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
            embed.add_field(name="City", value=data['name'])
            embed.add_field(name="Country", value=data['sys']['country'])
            embed.add_field(name="Temperature", value=f"{data['main']['temp']}°C")
            embed.add_field(name="Min. Temp", value=f"{data['main']['temp_min']}°C")
            embed.add_field(name="Max. Temp", value=f"{data['main']['temp_max']}°C")
            embed.add_field(name="Description", value=f"{data['weather'][0]['description']}")
            embed.add_field(name="Wind Speed", value=f"{data['wind']['speed']}meter/sec")
            embed.add_field(name="Humidity", value=f"{data['main']['humidity']}%")
            embed.add_field(name="Cloudliness", value=f"{data['clouds']['all']}%")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"Powered by OpenWeather API, Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
                            
@client.command(pass_context=True)
async def dark(ctx):
    address = "https://sv443.net/jokeapi/category/dark?blacklistFlags=nsfw,political"
    data = requests.get(address).json()
    x = await ctx.send("Joke is being ready. This can be dark and may triggers you, **Viewers discretion is advised and No Offense**.")
    await asyncio.sleep(1)
    await x.edit(content="Joke is being ready. This can be dark and may triggers you, **Viewers discretion is advised and No Offense**..")
    await asyncio.sleep(1)
    await x.edit(content="Joke is being ready. This can be dark and may triggers you, **Viewers discretion is advised and No Offense**...")
    await asyncio.sleep(1)
    if data['type'] == "single":
        await x.edit(content=data['joke'])
    else:
        await x.edit(content=f"{data['setup']} \n{data['delivery']}")

@client.event
async def on_member_update(before, after):
    channel = client.get_channel(557273459244269582)
    if after.guild.name != "Virtual Reformed":
        return;
    else:
        if after.nick != before.nick:
            embed = discord.Embed(title="Nickname Updated", description=f"Actual Username: {after.name} \nIf Before Nickname is ``None``, The Nickname is actual username or it isn't cached in bot. \nIf After Nickname is ``None``, The Nickname is Actual UserName of the Member.", color = 0xFFFFFF)
            embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
            embed.add_field(name="Before", value=before.nick)
            embed.add_field(name="After", value=after.nick)
            embed.set_footer(text=after.name, icon_url=after.avatar_url)
            await channel.send(embed=embed)
        elif before.roles != after.roles:
            if len(before.roles) < len(after.roles):
                new_role = next(role for role in after.roles if role not in before.roles)
                embed = discord.Embed(title="Member Update", description=f"**{after.mention} has been given {new_role.mention} role**.", color=new_role.color)
                embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=after.name, icon_url=after.avatar_url)
                await channel.send(embed=embed)
            elif len(before.roles) > len(after.roles):
                new_role = next(role for role in before.roles if role not in after.roles)
                embed = discord.Embed(title="Member Update", description=f"**{after.mention} has been removed from {new_role.mention} role**.", color=new_role.color)
                embed.set_author(name=after.guild.name, icon_url=after.guild.icon_url)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=after.name, icon_url=after.avatar_url)
                await channel.send(embed=embed)                     
                   
@client.command(pass_context=True)
async def dadjoke(ctx):
    dadjoke = Dadjoke()
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(dadjoke.joke)
                     
@client.command(pass_context=True)
async def neko(ctx, *, name:str=None):
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
@client.command(pass_context=True)
async def h(ctx, *, name:str=None):
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
                embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif name == "help":
                helplist = ", ".join(list1)
                await ctx.send(f"Available args:\n ```{helplist}``` \n ``&neko <args>``")
        else:
            await ctx.send("**Nah! Nah! Nah! This has to be a NSFW channel, fucker!!!**")        
    else:
        return
                     
@client.command(pass_context=True)
async def fact(ctx):
    address = "https://nekos.life/api/v2/fact"
    data = requests.get(address).json()
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(data['fact'])

@client.command(pass_context=True)
async def spoiler(ctx, *, text):                     
    address = f"https://nekos.life/api/v2/spoiler?text={text}"
    data = requests.get(address).json()
    await ctx.message.delete()                     
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(data['owo'])

@client.command(pass_contexxt=True)
async def why(ctx):
    address = "https://nekos.life/api/why"
    data = requests.get(address).json()
    await ctx.message.delete()                     
    await ctx.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(data['why'])
                     
@client.command(pass_context=True)
async def suggest(ctx, *, msg: str):
    channel = client.get_channel(572851166694866944)
    message = await channel.send(f"** {ctx.author.mention} Suggested : {msg} **")
    await message.add_reaction(emoji='✅')
    await message.add_reaction(emoji='❎')
                     


@client.command(pass_context=True)
async def india(ctx, *, state:str = None):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
        }
    data = requests.request("GET", url, headers=headers).json()
    active = data['state_wise'][state]['active']
    confirmed = data['state_wise'][state]['confirmed']
    recovered = data['state_wise'][state]['recovered']
    cases_confirmed_today = data['state_wise'][state]['deltaconfirmed']
    cases_recovered_today = data['state_wise'][state]['deltarecovered']
    cases_death_today = data['state_wise'][state]['deltadeaths']
    active1 = (int(active)/int(confirmed))*100
    recovered1 = (int(recovered)/int(confirmed))*100
    state_code = data['state_wise'][state]['statecode']
    deaths = data['state_wise'][state]['deaths']
    deaths1 = (int(deaths)/int(confirmed))*100
    last_time = data['state_wise'][state]['lastupdatedtime']
    await ctx.send(f"Confirmed : **{confirmed}**\nActive : **{active} ({round(active1, 2)}%)**\nRecovered : **{recovered} ({round(recovered1, 2)}%)**\nDeaths : **{deaths} ({round(deaths1, 2)}%)**\nCases Registered Today : **{cases_confirmed_today}**\nRecovered Cases Today : **{cases_recovered_today}**\nDeath Cases Today : **{cases_death_today}**\nLast Updated : **{last_time}**")

@client.command(pass_context=True)
async def country(ctx, *, name:str = None):
    address = f"https://corona.lmao.ninja/v2/countries/{name}"
    data = requests.get(address).json()
    embed = discord.Embed(title=f"COVID-19 stats of {name}", description=None, color=0XFF69BF)
    active_cases = (data['active']/data['cases'])*100
    recovered_cases = (data['recovered']/data['cases'])*100
    death_percentage = (data['deaths']/data['cases'])*100
    embed.add_field(name="Confirmed Cases So Far", value= data['cases'])
    embed.add_field(name="Cases Registered Today", value= f"+{data['todayCases']}")
    embed.add_field(name="Total Deaths So Far", value= f"{data['deaths']} ({round(death_percentage, 2)}%)")
    embed.add_field(name="Deaths Registered Today", value= f"+{data['todayDeaths']}")
    embed.add_field(name="Cases Recovered So Far", value= f"{data['recovered']} ({round(recovered_cases, 2)}%)")
    embed.add_field(name="Active Cases So Far", value= f"{data['active']} ({round(active_cases, 2)}%)")
    embed.add_field(name="Critical Cases So Far", value= data['critical'])
    embed.add_field(name="Cases Per One Million", value= data['casesPerOneMillion'])
    embed.add_field(name="Deaths Per One Million", value= data['deathsPerOneMillion'])
    embed.set_thumbnail(url=data['countryInfo']['flag'])
    embed.add_field(name="Tests Done So Far", value= data['tests'])
    embed.add_field(name="Tests Done Per Million", value= data['testsPerOneMillion'])
    embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
                    
@client.command(pass_context=True)
async def district(ctx, *, state1:str=None):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
        }
    await ctx.send("Now please enter the district name only...")
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=20)
    state = state1
    district2 = msg.content
    data = requests.request("GET", url, headers=headers).json()
    data2 = requests.request("GET", url, headers=headers)
    if data['state_wise'][state]['statenotes'] == "":
       statenotes1 = "No Notes From State Govt."
    else:
        statenotes1 =  data['state_wise'][state]['statenotes'].replace("<br>", " ")
    active = data['state_wise'][state]['district'][district2]['active']
    confirmed = data['state_wise'][state]['district'][district2]['confirmed']
    recovered = data['state_wise'][state]['district'][district2]['recovered']
    cases_confirmed_today = data['state_wise'][state]['district'][district2]['delta']['confirmed']
    cases_recovered_today = data['state_wise'][state]['district'][district2]['delta']['recovered']
    cases_death_today = data['state_wise'][state]['district'][district2]['delta']['deceased']
    active1 = (int(active)/int(confirmed))*100
    recovered1 = (int(recovered)/int(confirmed))*100
    state_code = data['state_wise'][state]['statecode']
    deaths = data['state_wise'][state]['district'][district2]['deceased']
    deaths1 = (int(deaths)/int(confirmed))*100
    last_time = data['state_wise'][state]['lastupdatedtime']
    await ctx.send(f"Confirmed : **{confirmed}**\nActive : **{active} ({round(active1, 2)}%)**\nRecovered : **{recovered} ({round(recovered1, 2)}%)**\nDeaths : **{deaths} ({round(deaths1, 2)}%)**\nCases Registered Today : **{cases_confirmed_today}**\nRecovered Cases Today : **{cases_recovered_today}**\nDeath Cases Today : **{cases_death_today}**\nLast Updated : **{last_time}**\nNotes by State Govt:\n**{statenotes1}**")                    

@client.command(pass_context=True)
async def districtlist(ctx, *, statename:str=None):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
        }
    data = requests.request("GET", url, headers=headers).json()
    await ctx.send(f"District names for **{statename}** state:\n")
    for district_name in data['state_wise'][statename]['district']:
        await ctx.send(district_name.replace("Other State", " "))
                    
@client.command(pass_context=True)
async def setlogchannel(ctx, channel:discord.TextChannel=None):
    db = sqlite3.connect('first2.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT log_channel FROM first WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO first(guild_id, log_channel) VALUES(?,?)")
        val = (ctx.guild.id, channel.id)
        await ctx.send(f"Channel is set to {channel.mention}")
    elif result is not None:
        sql = ("UPDATE first SET log_channel = ? WHERE guild_id = ?")
        val = (channel.id, ctx.guild.id)
        await ctx.send(f"Channel is updated to {channel.mention}")
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
 
                    
client.run(os.getenv('TOKEN'))
