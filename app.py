import discord
from discord.ext import commands
from discord.utils import get
class DiscordClient:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        self.bot = commands.Bot(command_prefix='!',intents=intents, case_insensitve=True)
    async def start_status(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Dark Moded!"))

    async def add_role(self,user_id):
        guild = self.bot.get_guild(686310388023033902)
        role = guild.get_role(9316020307688161582)
        user = guild.get_member(int(user_id))
        await user.add_roles(role)
