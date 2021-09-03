from discord.ext import commands
import discord
from helper import *

intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command()
async def sp(ctx,member:discord.Member):
    if str(member.activity) == "Spotify":
        embed=discord.Embed(title=f"{member.name} Spotify",description=f"Song: **{member.activity.title}**\nAlbum: **{member.activity.album}**\nAuthor: **{member.activity.artist}**\nDuration: **{strfdelta(member.activity.duration, '{M}:{S}')}**",color=discord.Color.green())

        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f"**{member.name}** Is not listening to music.",color=discord.Color.red())

        await ctx.send(embed=embed)

bot.run("token-here")
