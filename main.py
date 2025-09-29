import discord
from discord.ext import commands
import os

TOKEN = "YOUR TOKEN" # You have to insert.
WEBEMBED_URL = "https://webembed-8st0.onrender.com/embed?description="
TRANSPARENT_SEQUENCE = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|
|||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​
||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" # If it's not necessary, delete this.
bot = commands.Bot(command_prefix="!", self_bot=True) # If you want to change prefix, change " ! -> The prefix want to change ".
 

@bot.command()
async def embed(ctx, *, text): # If you want to change command, change " embed -> The command want to change ".
    await ctx.message.delete()

    safe_text = text.replace(" ", "+")
    message_to_send = f"{TRANSPARENT_SEQUENCE}{WEBEMBED_URL}{safe_text}"

    await ctx.send(message_to_send)

bot.run(TOKEN, bot=False)  # If it’s for you to use a selfbot, you must set " bot=False ".
