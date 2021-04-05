import os
import ssl
import asyncpg
import importlib
import settings

from discord.ext import commands


class FrostBot(commands.Bot):
    """Override functions for custom behavior"""

    def __init__(self, command_prefix, **options):
        self.DB = None

        super().__init__(command_prefix, **options)

    async def start(self, *args, **kwargs):
        print("Connecting to DB")

        self.DB = await get_class(settings.DB_BACKEND).connect()

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


def get_class(class_str: str):
    module, class_name = class_str.rsplit(".", 1)
    return getattr(importlib.import_module(module), class_name)
