# importing required modules for the bot 

import discord
from discord.ext import commands
import requests

# assigning a prefix string to the 'cov_prefix' str and assigining it as a command_prefix

cov_prefix = 'c:'
cov_bot = commands.Bot(command_prefix=cov_prefix)

# assiging a string which contains the bot's token and then assigning this str to the code 'bot.run(token)'

cov_bot_token = "insert bot token here (obviously i am not going to reveal mine lol)"

# printing a string to make sure the bot is online 

@cov_bot.event 
async def on_ready():
    print("✔ CovBot is online! stay safe")

#  making the bot grab a log of the messages sent in the last active channel for the bot

@cov_bot.event
async def on_message(messageGrab):
    print("Message str grabbed: ", messageGrab.content)
    await cov_bot.process_commands(messageGrab)

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
    embed = discord.Embed(title = "Total COVID-19 Data Worldwide", color=0x1abc9c)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases = {total}\n Total Number of deaths = {totalDeaths}\n Total number of recoveries = {recovered}\n Currently active cases of COVID-19 = {active}\n Cases per a million = {casesPer10to6}\n Total number of countries affected by the COVID-19 Pandemic = {countriesAffected}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
    await ctx.send(embed=embed)

# assigning different inline colors for the embed
class color_code:
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

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
    embed = discord.Embed(title = "Total COVID-19 Data in the United States of America", color=color_code.teal)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in USA = {casesConf}\n Total Number of deaths in USA = {deathConf}\n Total number of recoveries in USA = {recoveredConf}\n Currently active cases of COVID-19 in USA = {activeConf}\n Critical Cases in USA = {criticalConf}\n Cases per a million in USA = {casesPer10to6}\n Total number of COVID tests done in USA = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
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
    embed = discord.Embed(title = "Total COVID-19 Data in Australia", color=color_code.blue)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in Australia = {casesConf}\n Total Number of deaths in Australia = {deathConf}\n Total number of recoveries in Australia = {recoveredConf}\n Currently active cases of COVID-19 in Australia = {activeConf}\n Critical Cases in Australia = {criticalConf}\n Cases per a million in Australia = {casesPer10to6}\n Total number of COVID tests done in Australia = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
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
    embed = discord.Embed(title = "Total COVID-19 Data in France", color=color_code.dark_orange)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in France = {casesConf}\n Total Number of deaths in France = {deathConf}\n Total number of recoveries in France = {recoveredConf}\n Currently active cases of COVID-19 in France = {activeConf}\n Critical Cases in France = {criticalConf}\n Cases per a million in France = {casesPer10to6}\n Total number of COVID tests done in France = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
    await ctx.send(embed=embed)


@cov_bot.command()
async def dataGER(ctx):
    apiGER = 'https://corona.lmao.ninja/v2/countries/Germany?yesterday&strict&query'
    jsonGER = requests.get(apiGER).json()
    casesConf = (jsonGER['cases'])
    deathConf = (jsonGER['deaths'])
    recoveredConf = (jsonGER['recovered'])
    activeConf = (jsonGER['active'])
    criticalConf = (jsonGER['critical'])
    casesPer10to6 = (jsonGER['casesPerOneMillion'])
    testsConf = (jsonGER['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in Germany", color=color_code.green)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in Germany = {casesConf}\n Total Number of deaths in Germany = {deathConf}\n Total number of recoveries in Germany = {recoveredConf}\n Currently active cases of COVID-19 in Germany = {activeConf}\n Critical Cases in Germany = {criticalConf}\n Cases per a million in Germany = {casesPer10to6}\n Total number of COVID tests done in Germany = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
    await ctx.send(embed=embed)


@cov_bot.command()
async def dataUK(ctx):
    apiUK = 'https://corona.lmao.ninja/v2/countries/UK?yesterday&strict&query'
    jsonUK = requests.get(apiUK).json()
    casesConf = (jsonUK['cases'])
    deathConf = (jsonUK['deaths'])
    recoveredConf = (jsonUK['recovered'])
    activeConf = (jsonUK['active'])
    criticalConf = (jsonUK['critical'])
    casesPer10to6 = (jsonUK['casesPerOneMillion'])
    testsConf = (jsonUK['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in the United Kingdom, bit high innit?", color=color_code.blurple)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in UK = {casesConf}\n Total Number of deaths in UK = {deathConf}\n Total number of recoveries in UK = {recoveredConf}\n Currently active cases of COVID-19 in UK = {activeConf}\n Critical Cases in UK = {criticalConf}\n Cases per a million in UK = {casesPer10to6}\n Total number of COVID tests done in UK = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
    await ctx.send(embed=embed)


@cov_bot.command()
async def dataRUS(ctx):
    apiRUS = 'https://corona.lmao.ninja/v2/countries/Russia?yesterday&strict&query'
    jsonRUS = requests.get(apiRUS).json()
    casesConf = (jsonRUS['cases'])
    deathConf = (jsonRUS['deaths'])
    recoveredConf = (jsonRUS['recovered'])
    activeConf = (jsonRUS['active'])
    criticalConf = (jsonRUS['critical'])
    casesPer10to6 = (jsonRUS['casesPerOneMillion'])
    testsConf = (jsonRUS['tests'])
    embed = discord.Embed(title = "Total COVID-19 Data in Russia, OUR Country", color=color_code.blurple)
    embed.add_field(name="data", value=f'Total Number of COVID-19 cases in Russia = {casesConf}\n Total Number of deaths in Russia = {deathConf}\n Total number of recoveries in Russia = {recoveredConf}\n Currently active cases of COVID-19 in Russia = {activeConf}\n Critical Cases in Russia = {criticalConf}\n Cases per a million in Russia = {casesPer10to6}\n Total number of COVID tests done in Russia = {testsConf}')
    embed.set_footer(text =f"{cov_bot.user.name} - Made by Neon")
    await ctx.send(embed=embed)

    
cov_bot.run(cov_bot_token)

# more commands for other countries will be added soon

# CovBot made by Neon (a.k.a @Neon__DEV, Neonツ, Ne10-Neon) 
