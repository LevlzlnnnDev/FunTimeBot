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

        @commands.Cog.listener()
        async def on_command_error(self, ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                msg = '**Vá com calma amigo**, tente novamente em {:.2f} segundos'.format(error.retry_after)
                await ctx.send(msg)

        @commands.Cog.listener()
        async def on_command_error(self, ctx, error):
            if isinstance(self, error, commands.CommandNotFound):
                embed = discord.Embed(
                    title='Oops!',
                    description='Error: {}'.format(error),
                    colour=discord.Colour.orange()
                )
                await ctx.send(embed=embed, delete_after=10.0)

    
def setup(bot):
    bot.add_cog(Manager(bot))
