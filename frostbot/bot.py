import discord
import asyncpg
import time
import os
import ssl

from discord.ext import commands

import logging

logging.basicConfig(level=logging.INFO)


class MyBot(commands.Bot):
    """Override functions for custom behavior"""

    def __init__(self, command_prefix, **options):
        self.pool = None
        super().__init__(command_prefix, **options)

    async def start(self, *args, **kwargs):
        print("Connecting to DB")
        # Workaround for ssl error when using heroku
        ssl_certs = ssl.create_default_context(cafile="")
        ssl_certs.check_hostname = False
        ssl_certs.verify_mode = ssl.CERT_NONE

        # Connecting to DB get connection string from heroku config vars, set max number of connection to 18. Heroku
        # only allows 20 connections for free DB. set to 18 as buffer in case we need to open connection while app is
        # running
        self.pool = await asyncpg.create_pool(os.getenv("DATABASE_URL"), max_size=18, ssl=ssl_certs)
        await super().start(*args, **kwargs)

    async def close(self):
        # Disconnect from voice channels
        for vc in self.voice_clients:
            await vc.disconnect()

        print("Disconnecting from DB")
        # Close DB connections
        if self.pool is not None:
            await self.pool.close()
        await super().close()


description = '''A bot used to spam channels'''''

bot = MyBot(command_prefix=commands.when_mentioned_or('$'), description=description)
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_connect():
    print(time.asctime(time.localtime(time.time())))
    print('Connected to Discord')


@bot.event
async def on_ready():
    print(time.asctime(time.localtime(time.time())))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

    # TODO: Move to command to start/stop/replay. Remove VC on disconnect
    KGLW = "Polygondwanaland 24/7"
    try:
        for guild in bot.guilds:
            if "Bot testing" in guild.name:  # only work in test server
                if not any(KGLW in v.name for v in guild.voice_channels):  # create voice channel if not exists
                    overwrites = {guild.default_role: discord.PermissionOverwrite(speak=False)}
                    category = None
                    for cat in guild.categories:
                        if "VOICE" or "voice" in cat.name:
                            category = cat
                            break
                    await guild.create_voice_channel(KGLW, overwrites=overwrites, category=category)
                for vchannel in guild.voice_channels:  # connect to voice channel and play
                    if KGLW in vchannel.name:
                        # vc = await vchannel.connect()
                        # source = await discord.FFmpegOpusAudio.from_probe("Polygondwanaland.opus")
                        # vc.play(source)
                        break
    except Exception as e:
        print("exception occurred, error: " + str(e))


@bot.event
async def on_disconnect():
    print(time.asctime(time.localtime(time.time())))
    print("Disconnected from discord")


@bot.event
async def on_resumed():
    print(time.asctime(time.localtime(time.time())))
    print("Reconnected to discord")


@bot.command(description='Reloads commands')
async def reload(ctx):
    await ctx.send('reloading commands')
    bot.reload_extension('Startup')
    await ctx.send('reload complete')


@bot.command(description='Loads extension')
async def load(ctx, extension: str):
    await ctx.send('Loading extension ' + extension)
    try:
        bot.load_extension(extension)
        await ctx.send(extension + ' has been loaded')
    except:
        await ctx.send("Failed to load extension")


@bot.command(description='Removes extension')
async def removex(ctx, extension: str):
    await ctx.send('Removing extension ' + extension)
    try:
        bot.unload_extension(extension)
        await ctx.send(extension + ' has been removed')
    except:
        await ctx.send("Failed to remove extension.\n"
                       "Restarting the bot mey be required")


@bot.command(description='Lists extensions')
async def extensions(ctx):
    temp = ''
    for k in bot.extensions.keys():
        temp += str(k) + '\n'
    await ctx.send(temp)


bot.load_extension('Startup')

bot.run(TOKEN)
