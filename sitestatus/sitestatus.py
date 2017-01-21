 asyncioimport aiohttp
import asyncio
# import discord
from discord.ext import commands

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36"

class SiteStatus:
    """Checks if a website is down or not. Based off of the isitdown cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sitestatus(self, url):
        """Checks if a website is down or not."""
        if url == "":
            await self.bot.say("You didn't enter a URL.")
            return
        if "http://" not in url or "https://" not in url:
            url = "http://" + url
        try:
            with aiohttp.Timeout(15):
                await self.bot.say("Testing " + url + "...")
                try:
                    response = await aiohttp.get(url, headers = { 'user_agent': headers })
                    if response.status == 200:
                        await self.bot.say(url + " is up and running.")
                    elif response.status == 404:
                        await self.bot.say("While checking the status of " + url + ", we encountered an error. This may/may not mean the site is down. Error code: 404 Not found.")
                    elif response.status == 401:
                        await self.boy.say("While checking the status of " + url + ", we encountered an error. This may/may not mean the site is down. Error code: 401 Forbidden")
                    elif response.status == 500:
                        await self.bot.say("While checking the status of " + url + ", we encountered an error. This may/may not mean the site is down. Error code: 500 Internal Server Error")
                    else:
                        await self.bot.say("The site " + url + " is down.")
                except asyncio.TimeoutError:
                    await self.bot.say("The site " + url + " is down.")
                except:
                    await self.bot.say("The site " + url + " is down.")

def setup(bot):
    n = SiteStatus(bot)
    bot.add_cog(n)
