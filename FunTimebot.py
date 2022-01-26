import discord
from discord.ext import commands, tasks

import json
import os

os.chdir('C:\\Users\\User\\Desktop\\AizenBot_Repository')

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

@bot.event
async def on_ready():
    print("Ready to start!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name="teste")
async def try_teste(ctx):
    name = ctx.author.name
    response = "Estou funcionando desgraça"

    await ctx.send(response)

@bot.command(aliases=['bal'])
async def balance(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author
        await open_account(user)

        users = await get_bank_data()
        user = user

        wallet_amount = users[str(user.id)]["wallet"]
        bank_amount = users[str(user.id)]["bank"]

        embed = discord.Embed(title= "User\'s ballance")
        embed.add_field(name="wallet", value=f"{wallet_amount}")
        embed.add_field(name="bank", value=f"{bank_amount}")

    await ctx.send(embed = embed)

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

bot.run(token)