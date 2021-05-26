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
from datetime import datetime
import requests
import json
import aiohttp
import sqlite3
from dadjokes import Dadjoke
from babel.numbers import format_number
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pytz
from pytz import timezone

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
class Covid(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print('Covid-19 is loaded')

    @commands.command(pass_context=True)
    async def india(self, ctx, *, state:str = None):
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
        url2 = 'https://api.covid19india.org/v4/min/data.min.json'
        headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
            }
        data = requests.request("GET", url, headers=headers).json()
        data2 = requests.get(url2).json()
        active = format_number(data['state_wise'][state]['active'], locale='en_IN')
        confirmed = format_number(data['state_wise'][state]['confirmed'], locale='en_IN')
        recovered = format_number(data['state_wise'][state]['recovered'], locale='en_IN')
        cases_confirmed_today = format_number(data['state_wise'][state]['deltaconfirmed'], locale='en_IN')
        cases_recovered_today = format_number(data['state_wise'][state]['deltarecovered'], locale='en_IN')
        cases_death_today = format_number(data['state_wise'][state]['deltadeaths'], locale='en_IN')
        active2 = data['state_wise'][state]['active']
        confirmed2 = data['state_wise'][state]['confirmed']
        recovered2 = data['state_wise'][state]['recovered']
        active1 = (int(active2)/int(confirmed2))*100
        recovered1 = (int(recovered2)/int(confirmed2))*100
        state_code = data['state_wise'][state]['statecode']
        deaths = format_number(data['state_wise'][state]['deaths'], locale='en_IN')
        deaths2 = data['state_wise'][state]['deaths']
        deaths1 = (int(deaths2)/int(confirmed2))*100
        last_time = data['state_wise'][state]['lastupdatedtime']
        population = format_number(data2[state_code]['meta']['population'], locale='en_IN')
        tested = format_number(data2[state_code]['total']['tested'], locale='en_IN')
        vaccinated = format_number(data2[state_code]['total']['vaccinated'], locale='en_IN')
        sevendayrecovered = format_number(data2[state_code]['delta7']['recovered'], locale='en_IN')
        sevendayconfirmed =  format_number(data2[state_code]['delta7']['confirmed'],locale = 'en_IN')
        sevendaydeaths = format_number(data2[state_code]['delta7']['deceased'], locale='en_IN')
        sevendaytested = format_number(data2[state_code]['delta7']['tested'], locale='en_IN')
        sevendayvaccinated = format_number(data2[state_code]['delta7']['vaccinated'], locale='en_IN')
        source = data2[state_code]['meta']['tested']['source']

        await ctx.send(f"State/UT: **{state} ({state_code})**\nPopulation: **{population}** (As per Census 2011)\nTested samples till date: **{tested}**\nConfirmed till date : **{confirmed}**\nActive till date : **{active} ({round(active1, 2)}%)**\nRecovered till date : **{recovered} ({round(recovered1, 2)}%)**\nDeaths : **{deaths} ({round(deaths1, 2)}%)**\nCases Registered Today : **{cases_confirmed_today}**\nRecovered Cases Today : **{cases_recovered_today}**\nDeath Cases Today : **{cases_death_today}**\n\nSeven Days Average:\nTested: **{sevendaytested}**\nConfirmed: **{sevendayconfirmed}**\nRecovered: **{sevendayrecovered}**\nDeaths: **{sevendaydeaths}**\nVaccinated: **{sevendayvaccinated}**\n\nLast Updated : **{last_time}**\nTotal doses vaccinated untill date: **{vaccinated}**\nSource: {source}")

    @commands.command(pass_contex=True)
    async def districtlist(self, ctx, *, statename:str=None):
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
        headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
            }
        data = requests.request("GET", url, headers=headers).json()
        await ctx.send(f"District names for **{statename}** state:\n")
        districts = list(district_name for district_name in data['state_wise'][statename]['district'])
        await ctx.send(", ".join(districts))

    @commands.command(pass_context=True)
    async def country(self, ctx, *, name:str = None):
        address = f"https://corona.lmao.ninja/v2/countries/{name}"
        data = requests.get(address).json()
        embed = discord.Embed(title=f"COVID-19 stats of {name}", description=None, color=0XFF69BF)
        active_cases = (data['active']/data['cases'])*100
        recovered_cases = (data['recovered']/data['cases'])*100
        death_percentage = (data['deaths']/data['cases'])*100
        lastupdatedraw = data['updated']
        """lastupdated = datetime.fromtimestamp(lastupdatedraw).strftime("%d-%m-%Y")"""
        embed.add_field(name="Continent", value= data['continent'])
        embed.add_field(name="Population", value=format_number(data['population'], locale="en_IN"))
        embed.add_field(name="Confirmed Cases So Far", value= format_number(data['cases'], locale='en_IN'))
        embed.add_field(name="Cases Registered Today", value= f"+{format_number(data['todayCases'], locale='en_IN')}")
        embed.add_field(name="Total Deaths So Far", value= f"{format_number(data['deaths'], locale='en_IN')} ({round(death_percentage, 2)}%)")
        embed.add_field(name="Deaths Registered Today", value= f"+{format_number(data['todayDeaths'], locale='en_IN')}")
        embed.add_field(name="Cases Recovered So Far", value= f"{format_number(data['recovered'], locale='en_IN')} ({round(recovered_cases, 2)}%)")
        embed.add_field(name="Cases Recovered Today", value= format_number(data['todayRecovered'], locale='en_IN'))
        embed.add_field(name="Active Cases So Far", value= f"{format_number(data['active'], locale='en_IN')} ({round(active_cases, 2)}%)")
        embed.add_field(name="Critical Cases So Far", value= format_number(data['critical'], locale='en_IN'))
        embed.add_field(name="One Case Per People", value=format_number(data['oneCasePerPeople'], locale='en_IN'))
        embed.add_field(name="One Death Per People", value=format_number(data['oneDeathPerPeople'], locale='en_IN'))
        embed.add_field(name="One Test Per People", value=format_number(data['oneTestPerPeople'], locale='en_IN'))
        embed.add_field(name="Cases Per One Million", value= format_number(data['casesPerOneMillion'], locale='en_IN'))
        embed.add_field(name="Active Per One Million", value= format_number(data['activePerOneMillion'], locale='en_IN'))
        embed.add_field(name="Recovered Per One Million", value=format_number(data['recoveredPerOneMillion'], locale='en_IN'))
        embed.add_field(name="Critical Cases Per One Million", value=format_number(data['criticalPerOneMillion'], locale='en_IN'))
        embed.add_field(name="Deaths Per One Million", value= format_number(data['deathsPerOneMillion'], locale='en_IN'))
        embed.set_thumbnail(url=data['countryInfo']['flag'])
        embed.add_field(name="Tests Done So Far", value= format_number(data['tests'], locale='en_IN'))
        embed.add_field(name="Tests Done Per Million", value= format_number(data['testsPerOneMillion'], locale='en_IN'))
        """embed.add_field(name="Last Updated", value= lastupdated)"""
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def district(self, ctx, *, state1:str=None):
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
        url2 = 'https://api.covid19india.org/v4/min/data.min.json'
        headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "6b43bde4e3mshb7fd730f56f4c81p183a82jsn529486ba9d6e"
            }
        await ctx.send("Now please enter the district name only...")
        try:
            msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=20)
            state = state1
            data2 = requests.get(url2).json()
            district2 = msg.content
            data = requests.request("GET", url, headers=headers).json()
            data2 = requests.get(url2).json()
            if data['state_wise'][state]['statenotes'] == "":
               statenotes1 = "No Notes From State Govt."
            else:
                statenotes1 =  data['state_wise'][state]['statenotes'].replace("<br>", " ")
            state_code = data['state_wise'][state]['statecode']
            active1 = data['state_wise'][state]['district'][district2]['active']
            active = format_number(data['state_wise'][state]['district'][district2]['active'], locale='en_IN')
            confirmed1 = data['state_wise'][state]['district'][district2]['confirmed']
            confirmed = format_number(data['state_wise'][state]['district'][district2]['confirmed'], locale='en_IN')
            recovered1 = data['state_wise'][state]['district'][district2]['recovered']
            recovered = format_number(data['state_wise'][state]['district'][district2]['recovered'], locale='en_IN')
            cases_confirmed_today = format_number(data['state_wise'][state]['district'][district2]['delta']['confirmed'], locale='en_IN')
            cases_recovered_today = format_number(data['state_wise'][state]['district'][district2]['delta']['recovered'], locale='en_IN')
            cases_death_today = format_number(data['state_wise'][state]['district'][district2]['delta']['deceased'], locale='en_IN')
            active2 = (int(active1)/int(confirmed1))*100
            recovered1 = (int(recovered1)/int(confirmed1))*100
            state_code = data['state_wise'][state]['statecode']
            deaths = data['state_wise'][state]['district'][district2]['deceased']
            deaths1 = format_number(data['state_wise'][state]['district'][district2]['deceased'], locale='en_IN')
            deaths2 = (int(deaths1)/int(confirmed1))*100
            population = format_number(data2[state_code]['districts'][district2]['meta']['population'], locale='en_IN')
            tested = format_number(data2[state_code]['districts'][district2]['total']['tested'], locale='en_IN')
            vaccinated = format_number(data2[state_code]['districts'][district2]['total']['vaccinated'], locale='en_IN')
            sevendayconfirmed = format_number(data2[state_code]['districts'][district2]['delta7']['confirmed'], locale='en_IN')
            sevendayrecovered = format_number(data2[state_code]['districts'][district2]['delta7']['recovered'], locale='en_IN')
            sevendaydeaths = format_number(data2[state_code]['districts'][district2]['delta7']['deceased'], locale='en_IN')
            sevendayvaccinated = format_number(data2[state_code]['districts'][district2]['delta7']['vaccinated'], locale='en_IN')
            last_time = data['state_wise'][state]['lastupdatedtime']
            await ctx.send(f"District:**{district2}**\nPopulation: **{population}** (As per Census 2011)\nTested Samples till date: **{tested}**\nConfirmed cases till date: **{confirmed}**\nActive cases till date: **{active} ({round(active2, 2)}%)**\nRecovered cases till date: **{recovered} ({round(recovered1, 2)}%)**\nDeceased cases till date: **{deaths} ({round(deaths2, 2)}%)**\nCases Registered Today : **{cases_confirmed_today}**\nRecovered Cases Today : **{cases_recovered_today}**\nDeceased Cases Today : **{cases_death_today}**\n\nSeven Days Average:\nConfirmed: **{sevendayconfirmed}**\nRecovered: **{sevendayrecovered}**\nDeaths: **{sevendaydeaths}**\nVaccinated: **{sevendayvaccinated}**\n\nLast Updated : **{last_time}**\nTotal doses vaccinated untill date: **{vaccinated}**\n\nLast Updated : **{last_time}**\nNotes by State Govt:\n**{statenotes1}**")
        except asyncio.TimeoutError:
            await ctx.send("Time's up. Please enter the district name in time and in correct dictation")

def setup(client):
    client.add_cog(Covid(client))
