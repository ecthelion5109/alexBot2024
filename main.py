import discord
from discord.ext import commands
import requests
import webserver
from token import TOKEN
# import os 

# TOKEN = os.getenv("TOKEN_DISCORDBOT2024")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# pip install requests
# pip install python.py
# pip install audioop-lts


@bot.event
async def on_ready():
	print(f"corriendo... {bot.user}")




@bot.command()
async def test(context, arg):
	await context.send(arg)











webserver.keep_alive()
bot.run(TOKEN)