import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="doge ")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("..."))
    print("I'm ready!")


@bot.command()
async def hi(ctx):
    await ctx.send(f"Hi!")

bot.run(os.getenv("DISCORD_TOKEN"))
