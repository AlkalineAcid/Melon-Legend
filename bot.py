import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
import textwrap
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.m'),description="A Discord bot.\n\nHelp Commands",owner_id=402041583593324544)




@bot.command()
async def ping(ctx): """Ping command""" color = discord.Color(value=0x00ff00) em = discord.Embed(color=color, title='Pong!') em.description = f"{bot.latency * 1000:.4f} ms" await ctx.send(embed=em) 
if not os.environ.get('TOKEN'): print("ERROR: Bot token not found.")bot.run(os.environ.get('TOKEN').strip('"'))









