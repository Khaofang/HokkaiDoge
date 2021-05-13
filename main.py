import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "doge ")

@client.event
async def on_ready():
  await client.change_presence(status = discord.Status.idle, activity = discord.Game("..."))
  print("I'm ready!")

@client.command()
async def hi(ctx) :
  await ctx.send(f"Hi!")

client.run(os.getenv("DISCORD_TOKEN"))
