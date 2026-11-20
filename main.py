import discord
import dotenv
import os

dotenv.load_dotenv('secrets.env')
bot_token = str(os.getenv("DISCORD_TOKEN"))

bot = discord.Bot()

cogs_list = [
    'truthdare',
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"{bot.user} is online")

bot.run(bot_token)