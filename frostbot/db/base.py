import asyncio
import asyncpg
import ssl
import os
from abc import ABC, abstractmethod


class BaseDBWrapper(ABC):
    """Abstract class for Database wrappers."""
    def __init__(self):
        self.conn = None

    @classmethod
    @abstractmethod
    async def connect(cls):
        """Class method used to create DB object and connect to db"""
        pass

    @abstractmethod
    async def raw_sql(self, sql: str):
        """Executes raw sql string."""
        pass

    # TODO: New plan. Remove below. add methods to interact with each table. I'm not building my own ORM

    @abstractmethod
    async def insert(self, table: str, values: tuple):
        """Insert row into table."""
        pass

    @abstractmethod
    async def update(self, table: str, values: dict, condition: str = None):
        """Update row in table.

        """
        pass

    @abstractmethod
    async def delete(self, table: str, condition: str = None):
        """Delete row(s) in table."""
        pass
