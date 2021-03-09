import os
import ssl
import asyncpg
from db.postgresql import DBWrapper

from discord.ext import commands


class FrostBot(commands.Bot):
    """Override functions for custom behavior"""

    def __init__(self, command_prefix, **options):
        self.pool = None
        self.DBWrapper = None
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

        self.DBWrapper = await DBWrapper.create()

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
