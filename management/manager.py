from dis import disco
from turtle import color, title
import discord
from discord.ext import commands

class Manager(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready to start!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener() #erro nesse comando
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Comando em cooldown parceiro, espere {:.2f} segundos").format(error.retry_after)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title='Oops!',
                description='Error: {}'.format(error),
                colour=discord.Colour.orange()
            )
            await ctx.send(embed=embed)
                
def setup(bot):
    bot.add_cog(Manager(bot))
