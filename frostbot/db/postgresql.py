import asyncio
from abc import ABC

import asyncpg
import ssl
import os

from base import BaseDBWrapper


class DBWrapper(BaseDBWrapper):
    @classmethod
    async def connect(cls):
        return cls()
