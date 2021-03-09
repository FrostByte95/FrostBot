import asyncio
import asyncpg
import ssl
import os
from abc import ABC, abstractmethod


class BaseDBWrapper(ABC):
    def __init__(self):
        self.conn = None

    @classmethod
    @abstractmethod
    async def create(cls):
        pass