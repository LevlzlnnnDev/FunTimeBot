import json
import random
import discord
from discord.ext import commands

from FunTimebot import get_bank_data, open_account


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teste")
    async def try_teste(self, ctx):
        name = ctx.author.name
        response = "Estou funcionando desgraça"

        await ctx.send(response)
    
def setup(bot):
    bot.add_cog(Talks(bot))
