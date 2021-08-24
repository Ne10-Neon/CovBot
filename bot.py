# importing required modules for the bot 

import discord
from discord.ext import commands
import requests

# assigning a prefix string to the 'cov_prefix' str and assigining it as a command_prefix

cov_prefix = 'c:'
cov_bot = commands.Bot(command_prefix=cov_prefix)

# assiging a string which contains the bot's token and then assigning this str to the code 'bot.run(token)'

cov_bot_token = "insert your bot token here (obviously im not going to reveal my bot's token LOL)"

# printing a string to make sure the bot is online 

@cov_bot.event 
async def on_ready():
    print("✔ CovBot is online! stay safe")

#  making the bot grab a log of the messages sent in the last active channel for the bot

#@cov_bot.event
#async def on_message(messageGrab):
    #print("Message str grabbed: ", messageGrab.content)
    #cov_bot.process_commands(messageGrab)

# giving the first command, which will send all the covid data worldwide from the api to the discord server 

@cov_bot.command()
async def totalData(ctx):
    totalC_api = 'https://corona.lmao.ninja/v2/all?yesterday='
    totalC_json = requests.get(totalC_api).json()
    total = (totalC_json['cases'])
    totalDeaths = (totalC_json['deaths'])
    recovered = (totalC_json['recovered'])
    active = (totalC_json['active'])
    casesPer10to6 = (totalC_json['casesPerOneMillion'])
    countriesAffected = (totalC_json['affectedCountries'])
    embed = discord.Embed(title = "Total COVID-19 Data Worldwide")
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases = {total}\n Total Number of deaths = {totalDeaths}\n Total number of recoveries = {recovered}\n Currently active cases of COVID-19 = {active}\n Cases per a million = {casesPer10to6}\n Total number of countries affected by the COVID-19 Pandemic = {countriesAffected}')
    await ctx.send(embed=embed)

# adding individual countries' data command and using the same API that was used in the COVID-19 Case software made by Neon (me)

@cov_bot.command()
async def dataUSA(ctx):
    apiUSA = 'https://corona.lmao.ninja/v2/countries/USA?yesterday&strict&query'
    jsonUSA = requests.get(apiUSA).json()
    casesConf = (jsonUSA['cases'])
    deathConf = (jsonUSA['deaths'])
    recoveredConf = (jsonUSA['recovered'])
    activeConf = (jsonUSA['active'])
    criticalConf = (jsonUSA['critical'])
    casesPer10to6 = (jsonUSA['casesPerOneMillion'])
    testsConf = (jsonUSA['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in USA")
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in USA = {casesConf}\n Total Number of deaths in USA = {deathConf}\n Total number of recoveries in USA = {recoveredConf}\n Currently active cases of COVID-19 in USA = {activeConf}\n Critical Cases in USA = {criticalConf}\n Cases per a million in USA = {casesPer10to6}\n Total number of COVID tests done in USA = {testsConf}')
    await ctx.send(embed=embed)

@cov_bot.command()
async def dataAU(ctx):
    apiAU = 'https://corona.lmao.ninja/v2/countries/Australia?yesterday&strict&query'
    jsonAU = requests.get(apiAU).json()
    casesConf = (jsonAU['cases'])
    deathConf = (jsonAU['deaths'])
    recoveredConf = (jsonAU['recovered'])
    activeConf = (jsonAU['active'])
    criticalConf = (jsonAU['critical'])
    casesPer10to6 = (jsonAU['casesPerOneMillion'])
    testsConf = (jsonAU['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in Australia")
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in Australia = {casesConf}\n Total Number of deaths in Australia = {deathConf}\n Total number of recoveries in Australia = {recoveredConf}\n Currently active cases of COVID-19 in Australia = {activeConf}\n Critical Cases in Australia = {criticalConf}\n Cases per a million in Australia = {casesPer10to6}\n Total number of COVID tests done in Australia = {testsConf}')
    await ctx.send(embed=embed)


@cov_bot.command()
async def dataFRA(ctx):
    apiFRA = 'https://corona.lmao.ninja/v2/countries/Australia?yesterday&strict&query'
    jsonFRA = requests.get(apiFRA).json()
    casesConf = (jsonFRA['cases'])
    deathConf = (jsonFRA['deaths'])
    recoveredConf = (jsonFRA['recovered'])
    activeConf = (jsonFRA['active'])
    criticalConf = (jsonFRA['critical'])
    casesPer10to6 = (jsonFRA['casesPerOneMillion'])
    testsConf = (jsonFRA['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in France")
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in France = {casesConf}\n Total Number of deaths in France = {deathConf}\n Total number of recoveries in France = {recoveredConf}\n Currently active cases of COVID-19 in France = {activeConf}\n Critical Cases in France = {criticalConf}\n Cases per a million in France = {casesPer10to6}\n Total number of COVID tests done in France = {testsConf}')
    await ctx.send(embed=embed)

    
cov_bot.run(cov_bot_token)

# more commands for other countries will be added soon

# CovBot made with love and python by Neon (a.k.a @Neon__DEV, Neonツ, Ne10-Neon) 
