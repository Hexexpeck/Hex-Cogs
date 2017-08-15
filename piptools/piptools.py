import os
import sys
from subprocess import check_output
import discord
from discord.ext import commands
from cogs.utils import checks

try:
    import pip
    pipAvailable = True
except ImportError:
    pipAvailable = False

class PipTools:

    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.group(pass_context=True)
    async def pip(self, ctx):
        """Use Python's pip dependency manager from within Discord. Currently only has upgrade, install, and uninstall commands."""
        if ctx.invoked_subcommand is None:
            await self.bot.say("Hey uh, you do know that you must specify a subcommand, right? Use [p]help pip for more info.")
            await self.bot.send_cmd_help(ctx)

    @checks.is_owner()
    @pip.command(pass_context=True)
    async def install(self, ctx, *, dependency: str):
        """Install a dependency from the Python Package Index."""
        try:
            check_output("pip install " + dependency, shell=True)
        except:
            print("[ERROR-PipTools]: Failed to install dependency.")
            await self.bot.say("Failed to install dependency.")
        else:
            print("[INFO-PipTools]: Dependency install success.")
            await self.bot.say("Dependency successfully installed.")

    @checks.is_owner()
    @pip.command(pass_context=True)
    async def upgrade(self, ctx, *, dependency: str):
        """Upgrades a already installed dependency."""
        try:
            check_output("pip install " + dependency + " --upgrade", shell=True)
        except:
            print("[ERROR-PipTools]: Failed to upgrade dependency.")
            await self.bot.say("Failed to upgrade dependency.")
        else:
            print("[INFO-PipTools]: Dependency upgrade success.")
            await self.bot.say("Dependency upgrade success.")

    @checks.is_owner()
    @pip.command(pass_context=True)
    async def uninstall(self, ctx, *, dependency: str):
        """Uninstalls a already installed dependency. Note that this will not ask to confirm deletion of a dependency, instead it deletes the dependency as soon as a command is received."""
        try:
            check_output("pip uninstall " + dependency + " --yes", shell=True)
        except:
            print("[ERROR-PipTools]: Failed to uninstall dependency.")
            await self.bot.say("Failed to uninstall dependency.")
        else:
            print("[INFO-PipTools]: Dependency uninstall success.")
            await self.bot.say("Dependency uninstall success.")

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def pipcoginfo(self):
        """Info about the PipTools cog."""
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Creator", value="Hexexpeck#8781")
        embed.add_field(name="Version", value="0.2")
        embed.add_field(name="Source", value="https://github.com/Hexexpeck/Hex-Cogs")
        embed.add_field(name="Description", value="A cog that allows you to interact with Python's pip package manager within Discord.")
        embed.add_field(name="Changelog", value="""
v0.2 Changelog:
* Added changelog to cog info
* Added description to cog info
* Command help is now sent when you use the pip command without subcommands.

v0.1 Changelog:
* Initial release
""")
        await self.bot.say(embed=embed)

def setup(bot):
    if pipAvailable is False:
        print("You don't have Python's pip package manager? Weird. Try reinstalling Python without removing any features.")
    else:
        n = PipTools(bot)
        bot.add_cog(n)
