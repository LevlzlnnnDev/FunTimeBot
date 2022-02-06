import json
import random
import discord
from discord.ext import commands

from FunTimebot import get_bank_data, open_account

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
            await open_account(user)

            users = await get_bank_data()
            user = user

            wallet_amount = users[str(user.id)]["wallet"]
            bank_amount = users[str(user.id)]["bank"]

            embed = discord.Embed(title="User\'s ballance")
            embed.add_field(name="wallet", value=f"{wallet_amount}")
            embed.add_field(name="bank", value=f"{bank_amount}")

        await ctx.send(embed=embed)

    @commands.command(name="beg")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        await open_account(ctx.author)
        user = ctx.author

        users = await get_bank_data()

        earnings = random.randrange(101)
        await ctx.send(f"Alguém te deu {earnings} moedas")
        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json", "w") as f:
            json.dump(users, f)


def setup(bot):
    bot.add_cog(Economy(bot))
