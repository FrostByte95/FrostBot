import asyncio
from abc import ABC

import asyncpg
import ssl
import os

from db.base import BaseDBWrapper


class DBWrapper(BaseDBWrapper):

    @classmethod
    async def connect(cls):
        pass

    async def raw_sql(self, sql: str):
        """
        Executes raw SQL.
        :param sql: Raw SQL string.
        """
        pass

