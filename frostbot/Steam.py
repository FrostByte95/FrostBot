import asyncio
import steam_async
import discord

from discord.ext import commands


# TODO - implement getting steam wishlist from url https://store.steampowered.com/wishlist/profiles/{Steam64 id}/wishlistdata/
class SteamCommands(commands.Cog, name='Steam', description='Set of commands to interact with Steam api'):
    def __init__(self, bot):
        self.bot = bot
        self._msg_limit = 100

    @commands.group()
    async def steam(self, ctx):
        """Displays Steam account info if available"""
        if ctx.invoked_subcommand is None:
            await ctx.send("Command not implemented")

    @steam.command()
    async def on_sale(self, ctx):
        """Displays wishlist sale items"""
        await ctx.send("Command not implemented")


def setup(bot):
    # TODO - Create DB table if not exists
    print('loading extension Steam...', end='')
    bot.add_cog(SteamCommands(bot))
    print('fin')


def teardown(bot):
    print('unloading extension Steam...', end='')
    bot.remove_cog('Steam')
    print('fin')
