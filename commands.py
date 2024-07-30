import discord
from discord.ext import commands
from model import generate_response

async def chat(ctx, *, prompt):
    if not prompt:
        await ctx.send("Пожалуйста задайте вопрос")
        return

    response_text = generate_response(prompt)
    if response_text:
        for chunk in [response_text[i:i + 1900] for i in range(0, len(response_text), 1900)]:
            await ctx.send(chunk)
    else:
        await ctx.send("An error occurred while processing your request.")