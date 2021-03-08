import asyncio

import discord
from discord.ext import commands

import PermissionUtils


class Annoy(commands.Cog, name='Annoy', description='Commands to annoy'):
    def __init__(self, bot):
        self.bot = bot
        self._msg_limit = 100

    @commands.Cog.listener()
    async def on_ready(self):
        print("I'm Ready, I'm ready to annoy")

    # TODO - store value somewhere to persist during reloads, db connection coming from bot
    @commands.command()
    @PermissionUtils.is_admin()
    async def set_message_limit(self, ctx, limit: int):
        """
        Sets the upper limit of how many message the bot can send back from a single annoy command.
        This setting affects all channels in the server.
        :param ctx:
        :param limit:
        :return:
        """
        self._msg_limit = limit
        """
        TODO - set msg limit for guild in db
        ---Code---
        await bot.conn.execute(*create or update db record for guild*)
        """
        await ctx.send('Message limit set to {0}'.format(self._msg_limit))

    @set_message_limit.error
    async def set_message_limit_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You must be an administrator to change this setting")

    @commands.command(name='annoyAll', description='Spams everyone')
    async def annoy_all(self, ctx, times: int, *, message: str = ''):
        """Reply @everyone"""
        if ctx.author.permissions_in(ctx.channel).mention_everyone:
            if times > self._msg_limit:
                y = self._msg_limit
            else:
                y = times
            for i in range(y):
                await ctx.send("@everyone\t" + message)
                await asyncio.sleep(.5)
        else:
            await ctx.send('You do not have the required permission(s): mention everyone')

    @commands.command(description='Spams users')
    async def annoy(self, ctx, times: int, *members: discord.Member, message: str = ''):
        """Spam @Users Mentions"""
        if times > self._msg_limit:
            y = self._msg_limit
        else:
            y = times
        for x in range(y):
            for m in members:
                await ctx.send(m.mention)
                await asyncio.sleep(1)

    @commands.command(description='deletes last x messages in the last 100 messages of user(s) in channel')
    async def clear(self, ctx, x: int, *members: discord.Member):
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            await ctx.send('Deleting messages')
            for m in members:
                count = 0
                msg_list = []
                async for message in ctx.channel.history():
                    if message.author == m and count < x:
                        msg_list.append(message)
                        count += 1
                await ctx.channel.delete_messages(msg_list)
        else:
            await ctx.send('You do not have the required permission(s): manage_messages')

    @commands.command(brief='this is the brief', help='This is the help', usage='this is the usage',
                      description='This is the description', hidden=True)
    async def test(self, ctx):
        await ctx.send("This is a test")

    async def cog_before_invoke(self, ctx):
        # Maybe connect to database here and attach to ctx.
        pass

    async def cog_after_invoke(self, ctx):
        pass


def setup(bot):
    # TODO - Create DB table if not exists
    print('loading extension annoy...', end='')
    bot.add_cog(Annoy(bot))
    print('fin')


def teardown(bot):
    print('unloading extension annoy...', end='')
    bot.remove_cog('Annoy')
    print('fin')
