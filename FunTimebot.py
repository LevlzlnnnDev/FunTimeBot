from ast import If
from turtle import title
from unicodedata import name
from discord.ext import commands

import json
import os

os.chdir('C:\\Users\\User\\Desktop\\FuntimeBot')

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "", "ChannelId" : ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]
channelId = configData["ChannelId"]

bot = commands.Bot(prefix)

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {} 
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 100

    with open("mainbank.json", "w") as f:
        json.dump(users,f,indent=4)
        return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

        return users

async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("mainbank.json", "w") as f:
        json.dump(users,f,indent=4)
    bal = [users[str(user.id)]["wallet"]],users[str(user.id)["bank"]]
    return bal

def load_cogs(bot):
    bot.load_extension("manager")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)
bot.run(token)