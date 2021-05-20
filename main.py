import discord
import os
from discord.ext import commands

repository_url = "https://github.com/Khaofang/HokkaiDoge"

bot = commands.Bot(
    command_prefix=[
        "doge ",
        "Doge ",
        "hokkai ",
        "Hokkai ",
        "hokkaidoge ",
        "HokkaiDoge "],
    help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("..."))
    print("I'm ready!")


@bot.command()
async def bark(ctx):
    await ctx.send("WAN WAN!")


@bot.command()
async def help(ctx):
    guide_url = f"{repository_url}/blob/master/GUIDE.md"
    embed = discord.Embed(
        title="Guide for HokkaiDoge Bot",
        description=f"[Click here]({guide_url})",
        colour=discord.Colour.orange())
    await ctx.send(embed=embed)


@bot.command()
async def hi(ctx):
    await ctx.send("Hi!")

bot.run(os.getenv("DISCORD_TOKEN"))
