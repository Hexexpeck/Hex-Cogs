import os
import sys
from subprocess import check_output
import discord
from discord.ext import commands
from cogs.utils import checks


class GitTools:

    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.group(pass_context=True)
    async def git(self, ctx):
        """Git related commands."""
        if ctx.invoked_subcommand is None:
            await self.bot.say("You do know that you need to pass in a subcommand, right? Use [p]help git for more info.")

    @checks.is_owner()
    @git.command(pass_context=True)
    async def clone(self, ctx, *, repo: str):
        """Lets you git clone a repository. Requires that you have Git installed and a valid repository URL."""
        await self.bot.say("Cloning **{}**, please wait...".format(repo))
        try:
            check_output("git clone " + repo, shell=True)
        except:
            print("[ERROR-GitTools]: Failed to git clone repository.")
            await self.bot.say("Failed to git clone repository **{}**.".format(repo))
        else:
            print("[INFO-GitTools]: Successfully git cloned repository.")
            await self.bot.say("Successfully git cloned repository **{}**".format(repo))

    @checks.is_owner()
    @git.command(pass_context=True)
    async def coginfo(self, ctx):
        """Info about this cog."""
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name="Creator", value="Hexexpeck#8781")
        embed.add_field(name="Version", value="0.1")
        embed.add_field(name="Source", value="https://github.com/Hexexpeck/Hex-Cogs")
        await self.bot.say(embed=embed)

def gitcheck():
    try:
        check_output("git")
    except:
        print("Git not installed. Cannot use this cog.")
    else:
        pass # do nothing

def setup(bot):
    gitcheck()
    n = GitTools(bot)
    bot.add_cog(n)
