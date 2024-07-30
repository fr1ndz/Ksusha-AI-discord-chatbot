import discord
from discord.ext import commands
from config import DISCORD_TOKEN
from commands import chat

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='chat')
async def chat_command(ctx, *, prompt):
    await chat(ctx, prompt=prompt)

bot.run(DISCORD_TOKEN)