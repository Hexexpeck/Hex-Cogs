# import discord
from discord.ext import commands
import urllib
try:
    import urllib2
except ImportError:
    pass
try:
    import urllib.request
except ImportError:
    pass

class FileRetriever:
    """Cog that retrieves the file located at the direct URL to the file specified."""

    @commands.command(pass_context=True)
    async def retrieve(self, ctx, *, url: str, name: str):
        """Retrieves a file off of the Internet, must provide a direct link to the file (with HTTP prefix) and exact name of the file (with extension)."""
        try:
            urllib.request.urlretrieve(url, name)
        except:
            await self.bot.say("Failed to retrieve file " + name + " off of " + url + " . Try again.")
        else:
            await self.bot.say("Successfully retrieved file " + name + " off of " + url + " . ")

def setup(bot):
    n = FileRetriever(bot)
    bot.add_cog(n)
