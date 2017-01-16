import os
import sys
# import discord
from discord.ext import commands

class Violence:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def punch(self, ctx, *, user : discord.Member):
        """Punch a user."""
        await self.bot.say("OUCH! " + user.mention + " just got punched in the face with a metal fist!")

    @commands.command(pass_context=True)
    async def rob(self, ctx, *, user : discord.Member):
        """Rob a user."""
        await self.bot.say("The now poor " + user.mention + " was robbed and the thief took his wallet with only $2 in it, his house, and his car.")

    @commands.command(pass_context=True)
    async def bully(self, ctx, *, user : discord.Member):
        """Bully a user."""
        await self.bot.say("He went to school. Sadly this time, " + user.mention + " got bullied and the bully left scars all over him.")

    @commands.command(pass_context=True)
    async def lunchmoney(self, ctx, *, user : discord.Member):
        """GIVE ME YOUR LUNCH MONEY!"""
        await self.bot.say("HEY YOU! YEAH YOU! GIVE ME YOUR LUNCH MONEY, " + user.mention + " ! YOU DOUCHE!")

def setup(bot):
    bot.add_cog(Violence(bot))
