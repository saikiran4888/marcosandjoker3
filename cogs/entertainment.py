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
import pytz
from pytz import timezone

class Entertainment(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Entertainment is loaded')
    
    @commands.command(pass_context=True)
    async def movie(self, ctx, *, name:str=None):
        await ctx.trigger_typing()
        url = f"http://www.omdbapi.com/?s={name}&apikey=4210fd67"
        data = requests.get(url).json()
        if data['Response'] == "False":
            await ctx.send("Oh no! There isn't any movie(s) with this name in the database.")
        else:
            count = str(data['Search']).count('Title')
            titles = list(data['Search'][x]['Title'] for x in range(count))
            years = list(data['Search'][x]['Year'] for x in range(count))
            list3 = list("%d. %s" % (n, a) for n, a in enumerate(titles, start=1))
            list1 = list("{} ({})".format(title, year) for title, year in zip(list3, years))
            list2 = '\n'.join(list1)
            await ctx.send(f"Here are the results for your search:\n\n{list2}\n\nEnter the number of the movie to get more details. You've got 15 seconds to enter your option.")
            try:            
                num = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
                num2 = int(num.content)
                movieid = data['Search'][num2-1]['imdbID']
                url = "http://www.omdbapi.com/?i={}&apikey=4210fd67&plot=full".format(movieid)
                x = requests.get(url).json()
                plot = x['Plot']
                embed=discord.Embed(title =x['Title'], description = "Here is your movie {}".format(ctx.message.author.name), color = ctx.author.color)
                if x["Poster"] != "N/A":
                    embed.set_thumbnail(url = x["Poster"])
                """imdb = x['Ratings'][0]['Value']"""
                """rotten = x['Ratings'][1]['Value']"""
                if len(plot) > 1024:
                    url2 = "http://www.omdbapi.com/?t={}&apikey=4210fd67&plot=short".format(movieid)
                    x = requests.get(url2).json()
                    plot = x['Plot']
                else:
                    plot = plot
                count1 = str(x["Ratings"]).count("Value")
                if x['Ratings'] ==[]:
                    metacritic = "N/A"
                    imdb = "N/A"
                    rotten = "N/A"
                elif 'Rotten Tomatoes' and "Metacritic" not in x['Ratings']:
                    rotten = "N/A"
                    metacritic = "N/A"
                    imdb = x['Ratings'][0]['Value']        
                elif "Metacritic" not in x['Ratings']:
                    imdb = x['Ratings'][0]['Value']
                    rotten = x['Ratings'][1]['Value']            
                    metacritic = "N/A"
                else:
                    metacritic = x['Ratings'][2]['Value']
                    imdb = x['Ratings'][0]['Value']
                    rotten = x['Ratings'][1]['Value']
        
                embed.add_field(name = "__Title__", value = x["Title"])
                embed.add_field(name = "__Released__", value = x["Released"])
                embed.add_field(name = "__Rated__", value = x["Rated"])
                embed.add_field(name = "__Runtime__", value = x["Runtime"])
                embed.add_field(name = "__Genre__", value = x["Genre"])
                embed.add_field(name = "__Director__", value = x["Director"])
                embed.add_field(name = "__Writer__", value = x["Writer"])
                embed.add_field(name = "__Actors__", value = x["Actors"])
                embed.add_field(name = "__Plot__", value = plot)
                embed.add_field(name = "__Countries__", value = x["Country"])
                embed.add_field(name = "__Language(s) Used__", value = x["Language"])
                embed.add_field(name = "__IMDB Votes__", value = x["imdbVotes"])
                embed.add_field(name = f"__IMDB Rating__", value = imdb)
                embed.add_field(name = f"__Rotten Tomatoes__", value = rotten)
                embed.add_field(name = f'__Metacritics__', value = metacritic)
                embed.add_field(name = "__Awards__", value = x['Awards'])
                embed.add_field(name = "__Box Office__", value = x['BoxOffice'])
                embed.add_field(name = "__DVD Release__", value = x["DVD"])
                embed.add_field(name = "__Production__", value = x["Production"])
                embed.add_field(name = "__Website__", value = x["Website"])
                embed.add_field(name = "__Type__", value = x["Type"])
                embed.set_footer(text = "Information from the OMDB API")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)
            except asyncio.TimeoutError:
                await ctx.send("Oh No! Timeout expired. Please execute the command once again.")

    @commands.command(pass_context=True)
    async def spotify(self, ctx):
        local_tz = pytz.timezone('Asia/Calcutta')
        user = ctx.author
        activity = user.activity
        if activity is None:
            await ctx.send("{} is not playing anything on spotify!".format(user.display_name))
            return
        if activity.type == discord.ActivityType.listening and activity.name == "Spotify":
            client_id = "3de4994a8c99485ab153804b7cfa6ff4"
            client_secret = "b0c797bb009346e8b77608eadbfb3545"
            client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            result = sp.track(activity.track_id)
            release_date = result['album']['release_date']
            explicit = result['explicit']
            embed = discord.Embed(description="**React to :thumbsup: in 20 seconds to get the song's lyrics into your DMs**")
            embed.add_field(name="Artist(s)", value=", ".join(activity.artists))
            embed.add_field(name="Album", value=activity.album)
            embed.add_field(name="Track ID", value=activity.track_id)
            embed.add_field(name="Release date", value = release_date)
            embed.add_field(name="Explicit", value= explicit)
            embed.add_field(name="Duration", value=str(activity.duration)[3:].split(".", 1)[0])
            embed.add_field(name="Song started at", value=activity.start.astimezone(local_tz).strftime("%d-%m-%Y %I:%M %p %Z"))
            embed.add_field(name="Song ending at", value=activity.end.astimezone(local_tz).strftime("%d-%m-%Y %I:%M %p %Z"))
            embed.title = "**{}**".format(activity.title)
            embed.set_thumbnail(url=activity.album_cover_url)
            embed.url = "https://open.spotify.com/track/{}".format(activity.track_id)
            embed.color = activity.color
            embed.set_footer(text="{} - is currently playing this song".format(ctx.author))
            messaage = await ctx.send(embed=embed)
            await messaage.add_reaction(emoji="👍")
            await asyncio.sleep(2)
            artist = ", ".join(activity.artists)
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: reaction.emoji == '👍', timeout=20)
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
            except asyncio.TimeoutError:
                return    
        else:
            await ctx.send("**Wait, You aren't listening any on spotify...**")
            return                                   
    
    @commands.command(pass_context=True)
    async def lyrics(self, ctx, *, track:str=None):
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
                    
    @commands.command(pass_context=True)
    async def anime(self, ctx, *, name:str = None):
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
 

def setup(client):
    client.add_cog(Entertainment(client))
