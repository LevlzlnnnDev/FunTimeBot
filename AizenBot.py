import discord
from discord.ext import commands, tasks

import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "a!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(prefix)

@bot.event
async def on_ready():
    print("Ready to start!")
    boss_raid.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name="teste")
async def try_teste(ctx):
    name = ctx.author.name
    response = "Estou funcionando senhor " + name

    await ctx.send(response)

@tasks.loop(seconds=10)#hours = 1
async def boss_raid():
    channel = bot.get_channel(887766308991692822)

    await channel.send("loop")

bot.run(token)