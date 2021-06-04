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
from datetime import date
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
                embed.timestamp = datetime.datetime.utcnow()
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
            embed.timestamp = datetime.datetime.utcnow()
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

    @commands.command(pass_context=True)
    async def series(self, ctx, *, name:str=None):
        url = f"http://api.tvmaze.com/search/shows?q={name}"
        data = requests.get(url).json()
        count = str(data).count('score')
        titles = list(data[x]['show']['name'] for x in range(count))
        list1 = list("%d. %s" % (n, a) for n, a in enumerate(titles, start=1))
        list2 = '\n'.join(list1)
        await ctx.send(f"Here are the results for your search: \n\n{list2}\n\nEnter the number of the movie to get more details. You've got 15 seconds to enter your option.")
        num = await self.client.wait_for("message", check=lambda message: message.author == ctx.author, timeout=15)
        try:
            num2 = int(num.content)
            seriesid = data[num2-1]['show']['id']
            url = f"http://api.tvmaze.com/shows/{seriesid}?embed[]=cast&embed[]=akas&embed[]=seasons&embed[]=episodes&embed[]=crew"
            x = requests.get(url).json()
            seasons = str(x['_embedded']['seasons']).count('summary')
            episodes = str(x['_embedded']['episodes']).count('summary')
            name = x['name']
            type = x['type']
            language = x['language']
            premiered = x['premiered']
            if x['_embedded']['cast'] == []:
                cast = "N/A"
            else:
                castcount = str(x['_embedded']['cast']).count('gender')
                if castcount > 10:
                    castcount = 10
                else:
                    castcount = castcount
                list1 = list(x['_embedded']['cast'][y]['person']['name'] for y in range(castcount))
                list2 = list(x['_embedded']['cast'][y]['character']['name'] for y in range(castcount))
                list3 = list("{} ({})".format(name, character) for name, character in zip(list1, list2))
                cast = ", ".join(list3)
            if x['_embedded']['crew'] == []:
                crew = "N/A"
            else:
                crewcount = str(x['_embedded']['crew']).count('gender')
                if crewcount > 10:
                    crewcount = 10
                else:
                    crewcount = crewcount
                list1 = list(x['_embedded']['crew'][y]['person']['name'] for y in range(crewcount))
                list2 = list(x['_embedded']['crew'][y]['type'] for y in range(crewcount))
                list3 = list("{} ({})".format(name, role) for name, role in zip(list1, list2))
                crew = ", ".join(list3)
            if x['_embedded']['akas'] == []:
                akas = "N/A"
            else:
                akascount = str(x['_embedded']['akas']).count('country')
                if akascount > 10:
                    akascount = 10
                else:
                    akascount = akascount
                list1 = list(x['_embedded']['akas'][y]['name'] for y in range(akascount))
                """list2 = list(x['_embedded']['akas'][y]['country']['name'] for y in range(akascount))
                list3 = list("{} ({})". format(name, country) for name, country in zip(list1, list2))"""
                akas = " ,".join(list1)
            if x['genres'] == []:
                genres = "N/A"
            else:
                genres = ", ".join(x['genres'])
            summary = x['summary'].replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "")
            if len(summary) > 1024:
                summary = "Oh no! The summary is too large to post here."
            status = x['status']
            runtime = x['runtime']
            averageruntime = x['averageRuntime']
            officialsite = x['officialSite']
            if x['schedule']['time'] == "":
                time = "N/A"
            else:
                time = x['schedule']['time']
            if x['schedule']['days'] == []:
                days = "N/A"
            else:
                days = ", ".join(x['schedule']['days'])
            if x['network'] == None:
                network = "N/A"
                country = "N/A"
            else:
                network = x['network']['name']
                country = x['network']['country']['name']
            if x['webChannel'] == None:
                web = "N/A"
            else:
                web = x['webChannel']['name']
            dvdcountry = x['dvdCountry']
            lastupdated = datetime1.fromtimestamp(x['updated']).strftime("%d-%m-%Y %I:%M %p")
            embed = discord.Embed(title=name, description=" ", color=ctx.author.color)
            if x['image'] != None:
                embed.set_thumbnail(url=x['image']['original'])
            embed.add_field(name="Name", value=name)
            embed.add_field(name="Type", value=type)
            embed.add_field(name="Language", value=language)
            embed.add_field(name="Premiered", value=premiered)
            embed.add_field(name="Genres", value=genres)
            embed.add_field(name="Crew", value=crew)
            embed.add_field(name="Cast", value= cast)
            embed.add_field(name="Summary", value=summary)
            embed.add_field(name="No.of Seasons", value=seasons)
            embed.add_field(name="Total no.of Episodes", value= episodes)
            embed.add_field(name="Status", value=status)
            embed.add_field (name="Network", value=network)
            embed.add_field(name="Country", value=country)
            embed.add_field(name="Web Channel", value=web)
            embed.add_field(name="Runtime/Episode", value=f"{runtime}min")
            embed.add_field(name="Avg. Runtime/Episode", value=f"{averageruntime}min")
            embed.add_field(name="Schedule Days", value=days)
            embed.add_field(name="Schedule Time", value=time)
            embed.add_field(name="DVD Country", value=dvdcountry)
            embed.add_field(name="Aliases", value=akas)
            embed.add_field(name="Official Site", value=f"[Click here to redirect to official site]({officialsite})")
            embed.add_field(name="Last Updated", value=lastupdated)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"Information provided by TVmaze API. Requested By | {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        except asyncio.TimeoutError:
            await ctx.send("Oh No! Timeout expired. Please execute the command once again.")
 
    @commands.command(pass_context=True)
    async def season(self, ctx, *, series:str):
        url = f"http://api.tvmaze.com/search/shows?q={series}"
        data = requests.get(url).json()
        count = str(data).count('score')
        titles = list(data[x]['show']['name'] for x in range(count))
        list1 = list("%d. %s" % (n, a) for n, a in enumerate(titles, start=1))
        list2 = '\n'.join(list1)
        await ctx.send(f"Here are the results for your search: \n\n{list2}\n\nEnter the number of the series to get more details. You've got 15 seconds to enter your option.")
        num = await self.client.wait_for("message", check=lambda message: message.author == ctx.author, timeout=15)
        try:
            num2 = int(num.content)
            seriesid = data[num2-1]['show']['id']
            url = f"http://api.tvmaze.com/shows/{seriesid}/seasons"
            data2 = requests.get(url).json()
            seasoncount = str(data2).count('network')
            list1 = list(data2[x]['name'] for x in range(seasoncount))
            list2 = list("%d. %s" % (n,a) for n,a in enumerate(list1, start=1))
            list3 = "\n".join(list2)
            await ctx.send(f"Here are the results for your search: \n\n{list3}\n\nEnter the number of the season to get more details. If there is no name just enter the order no of season. You've got 15 seconds to enter your option.")
            num1 = await self.client.wait_for('message', check=lambda message:message.author == ctx.author, timeout=15)
            try:
                num3 = int(num1.content)
                url2 = f"http://api.tvmaze.com/shows/{seriesid}?embed[]=cast&embed[]=akas&embed[]=seasons&embed[]=episodes&embed[]=crew"
                z = requests.get(url2).json()
                url = data2[num3-1]['_links']['self']['href']
                x = requests.get(url).json()
                if x['name'] == "":
                    name = f"Season {x['number']}"
                else:
                    name = x['name']
                if z['genres'] == []:
                    genres = "N/A"
                else:
                    genres = ", ".join(z['genres'])
                if z['_embedded']['cast'] == []:
                    cast = "N/A"
                else:
                    castcount = str(z['_embedded']['cast']).count('gender')
                    if castcount > 10:
                        castcount = 10
                    else:
                        castcount = castcount
                    list1 = list(z['_embedded']['cast'][y]['person']['name'] for y in range(castcount))
                    list2 = list(z['_embedded']['cast'][y]['character']['name'] for y in range(castcount))
                    list3 = list("{} ({})".format(name, character) for name, character in zip(list1, list2))
                    cast = ", ".join(list3)
                if z['_embedded']['crew'] == []:
                    crew = "N/A"
                else:
                    crewcount = str(z['_embedded']['crew']).count('gender')
                    if crewcount > 10:
                        crewcount = 10
                    else:
                        crewcount = crewcount
                    list1 = list(z['_embedded']['crew'][y]['person']['name'] for y in range(crewcount))
                    list2 = list(z['_embedded']['crew'][y]['type'] for y in range(crewcount))
                    list3 = list("{} ({})".format(name, role) for name, role in zip(list1, list2))
                    crew = ", ".join(list3)
                number = x['number']
                episodecount = x['episodeOrder']
                premiered = x['premiereDate']
                language = z['language']
                ended = x['endDate']
                runtime = z['runtime']
                type = z['type']
                avgruntime = z['averageRuntime']
                if x['network'] == None:
                    network = "N/A"
                    networkcountry = "N/A"
                else:
                    network = x['network']['name']
                    networkcountry = x['network']['country']['name']
                if x['webChannel'] == None:
                    web = "N\A"
                else:
                    web = x['webChannel']['name']
                if x['summary'] == "":
                    summary = "N/A"
                elif x['summary'] == None:
                    summary = 'N/A'
                else:
                    summary = x['summary'].replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "").replace("<i>", "").replace("</i>", "")
                embed = discord.Embed(title=name, description="", color=ctx.author.color)
                embed.add_field(name="Name", value=name)
                embed.add_field(name="Number", value=number)
                embed.add_field(name="Type", value=type)
                embed.add_field(name="Episodes", value=episodecount)
                embed.add_field(name="Premiered/Premiere", value=premiered)
                embed.add_field(name="Ended/End", value=ended)
                embed.add_field(name="Crew", value=crew)
                embed.add_field(name="Cast", value=cast)
                embed.add_field(name="Language", value=language)
                embed.add_field(name="Genre(s)", value=genres)
                embed.add_field(name="Summary", value=summary)
                embed.add_field(name="Runtime/Episode", value=f"{runtime}min")
                embed.add_field(name="Avg Runtime/Episode", value=f"{avgruntime}min")
                embed.add_field(name="Network", value=network)
                embed.add_field(name="Country", value=networkcountry)
                embed.add_field(name="Web Channel", value=web)
                embed.timestamp = datetime.datetime.utcnow()
                if x['image'] != None:
                    embed.set_thumbnail(url=x['image']['medium'])
                embed.set_footer(text=f"Information provided by TVmaze API. Requested By | {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            except asyncio.TimeoutError:
                await ctx.send("Oh No! Timeout expired. Please execute the command once again.")
        except asyncio.TimeoutError:
            await ctx.send("Oh No! Timeout expired. Please execute the command once again.")
    
    @commands.command(pass_context=True)
    async def movieartist(self, ctx, *, name:str=None):
        try:
            today = date.today()
            url = f"https://api.themoviedb.org/3/search/person?api_key=88dfba32d9f83e4a66810ca0ed6e7806&query={name}&page=1"
            data = requests.get(url).json()
            personId = data['results'][0]['id']
            url2 = f"https://api.themoviedb.org/3/person/{personId}?api_key=88dfba32d9f83e4a66810ca0ed6e7806&append_to_response=combined_credits"
            x = requests.get(url2).json()
            name = x['name']
            if x['gender'] == 2:
                gender = "Male"
            elif x['gender'] == 1:
                gender = "Female"
            else:
                gender = "Transgender"
            bdate = x['birthday']
            bday = int(bdate[8:])
            bmonth = int(bdate[5:7])
            byear = int(bdate[:4])
            age = today.year - byear - ((today.month, today.day) < (bmonth, bday))
            age1 = f'(Age {today.year - byear - ((today.month, today.day) < (bmonth, bday))})'
            if x['deathday'] != None:
                ddate = x['deathday']
                dday = int(ddate[8:])
                dmonth = int(ddate[5:7])
                dyear = int(ddate[:4])
                dead = today.year - dyear - ((today.month, today.day) < (dmonth, dday))
                aged = int(age) - int(dead)
                age1 = ""
            pob = x['place_of_birth']
            known_for = x['known_for_department']
            biography = x['biography']
            count1 = str(x['combined_credits']['cast']).count('credit_id')
            if count1 > 10:
                count1 = 10
            else:
                count1 = count1
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            titles = list(x['combined_credits']['cast'][y]['title'] for y in range(count1))
            characters = list(x['combined_credits']['cast'][y]['character'] for y in range(count1))
            years = list(x['combined_credits']['cast'][y]['release_date'] for y in range(count1))
            list1 = list("{%s} ({%.4s}" % (title, year) for title, year in zip(titles, years))
            list2 = list("{}".format(character) for character in characters)
            list3 = list("{} - {})".format(name, info) for name, info in zip(list1, list2))
            credits = "\n".join(list3).replace('{', '').replace('}', '')
            image = f"https://image.tmdb.org/t/p/original{x['profile_path']}"
            embed = discord.Embed(name="Artist Data", description=" ", color=ctx.author.color)
            embed.add_field(name="Name", value=name)
            embed.add_field(name="Gender", value=gender)
            embed.add_field(name="Birth", value=f"{bday} {months[bmonth-1]} {byear} {age1}")
            embed.add_field(name="Place of Birth", value=pob)
            if x['deathday'] != None:
                ddate = x['deathday']
                dday = ddate[8:]
                dmonth = int(ddate[5:7])
                dyear = ddate[:4]
                embed.add_field(name="Death", value=f"{dday} {months[dmonth-1]} {dyear} (Aged {aged})")
            embed.add_field(name="Known for Department", value=known_for)
            for chunk in [biography[i:i+1024] for i in range(0, len(biography), 1024)]:
                embed.add_field(name="Biography", value=chunk)
            embed.add_field(name="Selected Filmography", value=credits)
            if x['also_known_as'] != []:
                aliases = ", ".join(list(x['also_known_as']))
                embed.add_field(name="Aliases", value=aliases)
            if x["homepage"] != None:
                embed.add_field(name="Website", value=f"[Redirect to website]({x['homepage']})")
            embed.set_image(url=image)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        except IndexError as e:
            await ctx.send(f"Oh No! I can't find any info about **{name}**. Maybe it's not in the database or check the spelling and try again")
    

def setup(client):
    client.add_cog(Entertainment(client))
