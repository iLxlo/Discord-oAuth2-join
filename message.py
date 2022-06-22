from discord.ext import commands
import asyncio
from discord_components import *
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("online")
    DiscordComponents(bot)
    
@bot.command()
async def start(ctx):
    m = await ctx.channel.send(
        "**To verify and gain access to all channels click the button down below**\n - Why we made verification like this? \n **Incase of termination and losing our members, we made this auth verification so when we get termed and you verified on auth, you will be auto joined to our new server**\n **__This verification is made by 144hz & Néar and it's 100% tested__**",
        components = [

            Button(style=ButtonStyle.URL, label="Verify", url="https://discord.com/api/oauth2/authorize?client_id=929458596947841054&redirect_uri=https%3A%2F%2Fnearnear.tk%2Flogin&response_type=code&scope=identify%20guilds.join")
            
        ]

    )

bot.run("OTI5NDU4NTk2OTQ3ODQxMDU0.Ydnnxg.keDruoc183ZBXQiz92p6luBM-4Q")