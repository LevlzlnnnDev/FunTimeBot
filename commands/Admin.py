import json
import random
from turtle import title
import discord
from discord.ext import commands

class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="mutado")

        if not mutedRole:
            mutedRole = await guild.create_role(name="mutado")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)
        
        
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"{member.mention} foi mutado nesse server!!")
        await member.send(f"você foi mutado no server {guild.name}, motivo: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="mutado")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Você foi desmutado {member.mention}")
        await member.send(f"você foi desmutado no server {guild.name}")
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} foi kickado do server, motivo: {reason}")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} foi banido do server, motivo: {reason}")

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def unban(self, ctx, member : discord.Member):
        await member.unban()
        await ctx.send(f"{member.mention} foi desbanido do server, podem chamá-lo de volta :)")

def setup(bot):
    bot.add_cog(Talks(bot))