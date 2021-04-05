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

    async def insert(self, table: str, values: tuple):
        """
        Inserts row into table.
        :param table: table to insert into.
        :param values: tuple of values to insert
        """
        pass

    async def update(self, table: str, values: dict, condition: str = None):
        """
        Update rows in table based on condition

        """
        pass

    async def delete(self, table: str, condition: str = None):
        pass