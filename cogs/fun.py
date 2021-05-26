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
import discogs_client
import aiohttp
from dadjokes import Dadjoke
import pytz
from pytz import timezone

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is loaded')

    @commands.command(pass_context=True)
    async def fams(self, ctx):
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=dragon ball z&rating=G&lang=en"
        data = requests.get(api_address).json()
        gif_url = data['data']['image_original_url']
        title = data['data']['title']
        embed = discord.Embed(title="Hey ya fams... Here's random gif from DBZ universe...", description=title, color=ctx.author.color)
        embed.set_image(url=gif_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def marvel(self, ctx):
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=marvel&rating=G&lang=en"
        data = requests.get(api_address).json()
        gif_url = data['data']['image_original_url']
        matter = f"[Click me if the gif didn't loaded](gif_url)"
        title = data['data']['title']
        embed = discord.Embed(title="Excelsior!!! Here's the random GIF from Marvel Universe", description=title, color=ctx.author.color)
        embed.set_image(url=gif_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send("Success")

    @commands.command(pass_context=True)
    async def dc(self, ctx):
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('gif_key')}&tag=marvel&rating=G&lang=en"
        data = requests.get(api_address).json()
        gif_url = data['data']['image_original_url']
        matter = f"[Click me if the gif didn't loaded](gif_url)"
        title = data['data']['title']
        embed = discord.Embed(title="Excelsior!!! Here's the random GIF from Marvel Universe", description=title, color=ctx.author.color)
        embed.set_image(url=gif_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send("Success")

    @commands.command(pass_context=True)
    async def naruto(self, ctx):
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

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/me_irl/random") as r:
                data = await r.json()
                embed = discord.Embed(title='Meme',color=ctx.author.color)
                embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def aot(self, ctx):
        gif_key = 'WzbK5LbCqMvGDpvxXdq6TEzMe8Za85Az'
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={gif_key}&tag=attack on titan&rating=G&lang=en"
        data1 = requests.get(api_address).json()
        gif_url = data1['data']['image_original_url']
        await ctx.send(gif_url)

    @commands.command(pass_context=True)
    async def aot2(self, ctx):
        gif_key = 'WzbK5LbCqMvGDpvxXdq6TEzMe8Za85Az'
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={gif_key}&tag=attack on titan&rating=G&lang=en"
        data1 = requests.get(api_address).json()
        title = data1['data']['title']
        gif_url = data1['data']['image_original_url']
        await ctx.send(f"{title}\n{gif_url}")

    @commands.command(pass_context=True)
    async def gif(self, ctx, *, name:str=None):
        gif_key = 'WzbK5LbCqMvGDpvxXdq6TEzMe8Za85Az'
        api_address = f"https://api.giphy.com/v1/gifs/random?api_key={gif_key}&tag={name}&rating=G&lang=en"
        data1 = requests.get(api_address).json()
        title = data1['data']['title']
        gif_url = data1['data']['image_original_url']
        await ctx.send(f"{title}\n{gif_url}")

    @commands.command(pass_contex=True)
    async def joke(self, ctx):
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

    @commands.command(pass_context=True, aliases=["8ball"])
    async def roll8ball(self, ctx, *, question: str = None):
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

    @commands.command(pass_context=True)
    async def quiz(self, ctx):
        list1 = ['Japanese Manga & Anime', 'Video Games', 'Film/Movies', 'Television']
        count = 4
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send("Enter the number of option of the category that you want quiz in. You've got 15 seconds to enter your option")
        list2 = list("%d. %s" % (n, a) for n, a in enumerate(list1, start=1))
        await ctx.send("\n".join(list2))
        try:

            category = await self.client.wait_for('message', check=lambda message: message.author==ctx.author, timeout=15)
            num = int(category.content)
            categories = ["31", "15", "11", "14"]
            api_address = f"https://opentdb.com/api.php?amount=10&category={categories[num-1]}"
            json_data = requests.get(api_address).json()
            ques = json_data['results'][0]['question']
            option1 = json_data['results'][0]['correct_answer']
            option2 = json_data['results'][0]['incorrect_answers'][0]
            option3 = json_data['results'][0]['incorrect_answers'][1]
            option4 = json_data['results'][0]['incorrect_answers'][2]
            """options = option1 +" "+ option2 +" "+ option3 +" "+ option4
            options2 = option4 +" "+ option3 +" "+ option2 +" "+ option1
            options3 = option4 +" "+ option1 +" "+ option3 +" "+ option2
            options4 = option4 +" "+ option3 +" "+ option2 +" "+ option1
            choices = [options, options2, options3, options4]"""
            answerslist = [option1, option2, option3, option4]
            shuffled1 = random.sample(answerslist, len(answerslist))
            indexes = [1, 2, 3, 4]
            indexedlist = list("{}. {}".format(index, shuffled) for index, shuffled in zip(indexes, shuffled1))
            await ctx.trigger_typing()
            await asyncio.sleep(3)
            await ctx.send(f"Category: {json_data['results'][0]['category']} \nDifficulty: {json_data['results'][0]['difficulty']}")
            await ctx.send(ques.replace("&#039;", "'").replace('&quot;', '"').replace("&amp;", "&"))
            await ctx.send("\n".join(indexedlist).replace("&#039;", "'").replace('&quot;', '"').replace("&amp;", "&"))
            try:
                msg = await self.client.wait_for('message', check= lambda message: message.author == ctx.author, timeout=20)
                num = int(msg.content)

                if shuffled1[num-1] == answerslist[0]:
                    await ctx.send("**Yayy, You've got it right...**")
                else:
                    await ctx.send(f"**Oh No, It's not the right answer... Correct answer is {json_data['results'][0]['correct_answer']}, Better luck next time.**")
            except asyncio.TimeoutError:
                await ctx.send(f"**Time's up. Correct answer is {json_data['results'][0]['correct_answer']}.**")
        except asyncio.TimeoutError:
            await ctx.send("Oh no! Time is out please try again")

    @commands.command(pass_context=True)
    async def fortune(self, ctx):
        address = "https://helloacm.com/api/fortune/"
        data = requests.get(address).json()
        msg = await ctx.send("Joker is busy writing your fortune.")
        await asyncio.sleep(1)
        await msg.edit(content="Joker is busy writing your fortune..")
        await asyncio.sleep(1)
        await msg.edit(content="Joker is busy writing your fortune...")
        await asyncio.sleep(1)
        await msg.edit(content=f"{data}")

    @commands.command(pass_context=True)
    async def gender(self, ctx, *, name:str = None):
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

    @commands.command(pass_context=True)
    async def dadjoke(self, ctx):
        dadjoke = Dadjoke()
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(dadjoke.joke)

    @commands.command(pass_context=True)
    async def fact(self, ctx):
        address = "https://nekos.life/api/v2/fact"
        data = requests.get(address).json()
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(data['fact'])

    @commands.command(pass_contex=True)
    async def useless(self, ctx):
        url = "https://useless-facts.sameerkumar.website/api"
        data = requests.get(url).json()
        fact = data['data']
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(fact)

    @commands.command(pass_context=True)
    async def spoiler(self, ctx, *, text):
        address = f"https://nekos.life/api/v2/spoiler?text={text}"
        data = requests.get(address).json()
        await ctx.message.delete()
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(data['owo'])

    @commands.command(pass_context=True)
    async def why(self, ctx):
        address = "https://nekos.life/api/why"
        data = requests.get(address).json()
        await ctx.message.delete()
        await ctx.trigger_typing()
        await asyncio.sleep(3)
        await ctx.send(data['why'])


def setup(client):
    client.add_cog(Fun(client))
