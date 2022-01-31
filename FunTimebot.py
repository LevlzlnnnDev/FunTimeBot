from ast import If
from turtle import title
import discord
from discord.ext import commands, tasks

import json
import random
import os
import time

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

@bot.event
async def on_ready():
    print("Ready to start!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Vá com calma amigo**, tente novamente em {:.2f} segundos'.format(error.retry_after)
        await ctx.send(msg)

@bot.event
async def on_message(message):
    reactionadd = False
    randomreact = random.randrange(101)

    if randomreact > 80:
        reactionadd = True
    else:
        reactionadd = False

    if reactionadd == True:
        await message.add_reaction('🐦')

# @bot.event
# async def on_raw_reaction_add(payload, ctx):
#     emoji = payload.emoji.name
#     user = ctx.author
#     users = await get_bank_data()
#     await open_account(ctx.author)

#     if emoji == '🐦':
#         earnings = random.randrange(1000)
#         users[str(user.id)]["bank"] += earnings

#     await ctx.send(f"Você achou o passáro vermelho, adicionadas {earnings} moedas em sua conta :)")

#     with open("mainbank.json", "w") as f:
#         json.dump(users, f)


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

@bot.command(name="beg")
@commands.cooldown(1,60,commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101) 
    await ctx.send(f"Alguem te deu {earnings} moedas")
    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

# @bot.command(name="with")
# async def withdraw(ctx,amount = None):
#     await open_account(ctx.author)

#     if amount == None:
#         await ctx.send("Você se esqueceu de colocar a quantia amigo, tente novamente")
#         return
    
#     bal = await update_bank(ctx.author)

#     amount = int(amount)
#     if amount>bal[0]:
#         await ctx.send("Você está tentando retirar muito mais do que tem em, vai ser cobrado")
#         return
    
#     if amount<bal[0]:
#         await ctx.send("A quantidade tem que ser acima de 0, senão n tem como meu parceiro")
#         return

#     await update_bank(ctx.author,amount)
#     await update_bank(ctx.author,-1*amount,"bank")

#     await ctx.send(f"Você retirou {amount} moedas do banco")

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