# import discord
from discord.ext import commands
import random

class Dank:
    """donk."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def donk(self, *, user: discord.Member):
        """you too donk m8."""
        await self.bot.say("my m8 " + user.mention + " over here is too donk for y'all.")

    @commands.command()
    async def dankometer(self, *, user: discord.Member):
        """how donk is this user?"""
        person = user.mention
        if user.id == self.bot.user.id:
            await self.bot.say("m8 dont even try to r8 the donkest person in this universe m8. im too donk for you to handle.")
        else:
            donkrating = {}
            donkrating['1'] = "{0}, your donk-o-meter rating is 1/10. ew get away from me".format(person)
            donkrating['2'] = "{0}, your donk-o-meter rating is 2/10. gtfo".format(person)
            donkrating['3'] = "{0}, your donk-o-meter rating is 3/10. bad".format(person)
            donkrating['4'] = "{0}, your donk-o-meter rating is 4/10. sorta bad".format(person)
            donkrating['5'] = "{0}, your donk-o-meter rating is 5/10. not bad and not good.".format(person)
            donkrating['6'] = "{0}, your donk-o-meter rating is 6/10. sorta improving.".format(person)
            donkrating['7'] = "{0}, your donk-o-meter rating is 7/10. ok things are starting to get donk.".format(person)
            donkrating['8'] = "{0}, your donk-o-meter rating is 8/10. well then someone is donk.".format(person)
            donkrating['9'] = "{0}, your donk-o-meter rating is 9/10. ( ͡° ͜ʖ ͡°)".format(person)
            donkrating['10'] = "{0}, your donk-o-meter rating is 10/10. ayy lmao you dank af m9.".format(person)
            donkrating['11'] = "{0}, your donk-o-meter rating is 11/10. m8 how tho only the donkest of the donk get this rating.".format(person)
            donkrating['broken'] = "{0}, your donk-o-meter rating was so donk it broke the scale m8.".format(person)
            donkrating['unknown'] = "{0}, your donk-o-meter rating is so low you can't even get 0 on the scale.".format(person)

            await self.bot.say('**{0}**'.format(random.choice([donkrating[i] for i in donkrating])))
def setup(bot):
    n = Dank(bot)
    bot.add_cog(n)
