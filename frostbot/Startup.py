import asyncio
import asyncpg

import discord
from discord.ext import commands


class GeneralCommands(commands.Cog, name='General', description='General Bot commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_message(self, message):
        if "$GME" in message.content and message.author.id != self.bot.user.id:  # GME Meme
            await message.reply("💎✋HOLD. BUY THE DIP. 💎✋ $GME 🚀🚀🚀🌚 ")

    @commands.command()
    async def echo(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Goodbye cruel world")
        await ctx.bot.logout()

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("I'm sorry " + ctx.author.mention + " , I'm afraid I can't do that.")

    @commands.command()
    @commands.is_owner()
    async def debug(self, ctx):
        """Prints userdata to stdout"""
        print("----DEBUG----")
        print(ctx.author)
        print("-----END-----")

    @commands.command()
    @commands.is_owner()
    async def test_responses(self, ctx, index: int):
        await ctx.send(self.responses[index])


def setup(bot):
    print('loading extensions')
    bot.add_cog(GeneralCommands(bot))
    bot.load_extension('annoy')
    bot.load_extension('Steam')
    print('fin')


def teardown(bot):
    print('unloading extensions')
    bot.remove_cog('General')
    bot.unload_extension('annoy')
    bot.unload_extension('Steam')
    print('fin')
