# Standard Library
import os
import sys
import shutil
import time

# Discord / Red Bot
import discord
from discord.ext import commands
from __main__ import send_cmd_help
from .utils import checks

class Chatter:
    """Chatter cog: talk as your bot using the console. Thanks to MissingNO123 for the inspiration.
    Edited by Obliviatum."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def chatter(self, ctx, *, channel : discord.Channel=None):
        """Start talk mode to send messages as your bot. 
        Enter ~~exit to end the session.

        Example: 
            !chatter #channel - Will let you chat as bot in chosen #channel.
            !chatter          - Will let you chat as bot in the channel you in."""

        author = ctx.message.author
        
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            await self.bot.say("Not allowed to delete messages.")
        except discord.HTTPException:
            await self.bot.say("Failed to delete message.")
        except:
            await self.bot.say("Unknown error encountered, failed to delete message.")

        if channel is None:
            channel = ctx.message.channel
            getChannelObj = self.bot.get_channel(channel.id)
            while True:
                msgInput = await self.bot.wait_for_message(timeout=15, author=author)
                if msgInput is None:
                    await self.bot.send_message(author, "You took too long. canceling chatter session.")
                    break
                elif msgInput.content == "~~exit":
                    await self.bot.delete_message(msgInput)
                    break
                else:
                    await self.bot.delete_message(msgInput)
                    await self.bot.say(msgInput.content)
        else:
            getChannelObj = self.bot.get_channel(channel.id)
            await self.bot.say("Enter your message now. use ~~exit to end session")
            while True:
                msgInput = await self.bot.wait_for_message(timeout=15, author=author)
                if msgInput is None:
                    await self.bot.send_message(author, "You took too long. canceling chatter session.")
                    break
                if msgInput .content == "~~exit":
                    await self.bot.delete_message(msgInput)
                    break
                else:
                    await self.bot.delete_message(msgInput)
                    getChannelObj = self.bot.get_channel(channel.id)
                    await self.bot.send_message(getChannelObj, msgInput.content)

def setup(bot):
    n = Chatter(bot)
    bot.add_cog(n)
