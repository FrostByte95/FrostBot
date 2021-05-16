import asyncio
import asyncpg
import ssl
import os
import discord
from typing import Union, Optional
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

    # Guilds
    @abstractmethod
    async def add_guild(self, guild: discord.Guild):
        """Add Guild to DB"""
        pass

    @abstractmethod
    async def get_guild_list(self):
        """returns list of guilds in DB"""
        pass

    @abstractmethod
    async def get_guild(self, guild: discord.Guild):
        """returns a guild in db"""
        pass

    @abstractmethod
    async def update_guild(self, guild: discord.Guild):
        """Update guild in DB"""
        pass

    @abstractmethod
    async def remove_guild(self, guild: discord.Guild):
        """Remove Guild from DB"""
        pass

    # Guild config
    # Guild config should be created when guild is added to db
    @abstractmethod
    async def get_guild_config(self, guild: discord.Guild):
        """Returns full guild config"""
        pass

    @abstractmethod
    async def get_msg_limit(self, guild: discord.Guild):
        """returns msg limit"""
        pass

    @abstractmethod
    async def set_msg_limit(self, guild: discord.Guild, msg_limit: int):
        """sets msg limit"""
        pass

    @abstractmethod
    async def get_notify_general(self, guild: discord.Guild):
        """returns General Notification channel"""
        pass

    @abstractmethod
    async def get_notify_admin(self, guild: discord.Guild):
        """returns Admin Notification channel"""
        pass

    @abstractmethod
    async def get_notify_steam(self, guild: discord.Guild):
        """returns steam Notification channel"""
        pass

    @abstractmethod
    async def set_notify_general(self, guild: discord.Guild, channel: discord.TextChannel):
        """sets General Notification channel"""
        pass

    @abstractmethod
    async def set_notify_admin(self, guild: discord.Guild, channel: discord.TextChannel):
        """sets Admin Notification channel"""
        pass

    @abstractmethod
    async def set_notify_steam(self, guild: discord.Guild, channel: discord.TextChannel):
        """sets steam Notification channel"""
        pass

    # Channels
    @abstractmethod
    async def add_channel(self, channel: Union[discord.TextChannel, discord.VoiceChannel], msg_limit: int = None):
        """
        Add Channel to Guild

        :param channel: Discord channel object. Can be either text or voice channel
        :param msg_limit: #The number of messages the bot can send to the channel per command.
        """
        pass

    @abstractmethod
    async def get_channel_list(self, guild: Optional[discord.Guild] = None):
        """
        Gets list of channels

        :param guild: Guild to get channels from. Defaults to None to get every channel in DB.
        """
        pass

    @abstractmethod
    async def get_channel(self, channel: Union[discord.TextChannel, discord.VoiceChannel]):
        """Gets Channel from ID"""
        pass

    @abstractmethod
    async def update_channel(self, channel: Union[discord.TextChannel, discord.VoiceChannel], msg_limit: int = None):
        """Update channel in DB"""
        pass

    @abstractmethod
    async def remove_channel(self, channel: Union[discord.TextChannel, discord.VoiceChannel]):
        """Remove channel from DB"""
        pass

    # Users
    @abstractmethod
    async def add_user(self, user: discord.Member):
        """Add user to DB"""
        # When implementing we are also adding them to a guild in DB.
        # If user already exist just add them to a guild
        pass

    @abstractmethod
    async def get_user_list(self, guild: Optional[discord.Guild] = None):
        """
        returns list of users in DB

        :param guild: Retrieves users from specified guild
        """
        pass

    @abstractmethod
    async def get_user(self, user: discord.Member):
        """Returns a user based on their ID. This will return info from multiple tables"""
        pass

    @abstractmethod
    async def update_user(self, user: discord.Member):
        """Update user in DB"""
        pass

    @abstractmethod
    async def remove_user(self, user: discord.Member):
        """Remove user from DB"""
        pass

    # Steam
    @abstractmethod
    async def add_steam(self, user: discord.Member, steam64: int, steam_vanity: str = None, notify: bool = False):
        """Add steam profile to user"""
        pass

    @abstractmethod
    async def get_steam_list(self):
        """returns list of steam profiles in DB"""
        pass

    @abstractmethod
    async def get_steam_notify(self):
        """returns list of steam profiles in DB with notify enabled"""
        pass

    @abstractmethod
    async def get_steam(self, user: discord.Member):
        """returns a steam profile based on their user ID"""
        pass

    @abstractmethod
    async def get_steam64(self, steam64: int):
        """returns a steam profile based on their steam64 ID"""
        pass

    @abstractmethod
    async def update_steam(self, user: discord.Member, steam64: int, steam_vanity: str = None, notify: bool = None):
        """Update steam profile in DB"""
        pass

    @abstractmethod
    async def remove_steam(self):
        """Remove steam profile from user"""
        pass

    # TODO: Below this line is unfinished
    # Music Player
    @abstractmethod
    async def add_music_player(self):
        """Add music_player to DB"""
        pass

    @abstractmethod
    async def get_music_player_list(self):
        """returns list of music_player in DB"""
        pass

    @abstractmethod
    async def get_music_player(self):
        """returns a music_player based on its ID"""
        pass

    @abstractmethod
    async def update_music_player(self):
        """Update music_player in DB"""
        pass

    @abstractmethod
    async def remove_music_player(self):
        """Remove music_player from DB"""
        pass

    # Playlist
    @abstractmethod
    async def add_playlist(self):
        """Add playlist to DB"""
        pass

    @abstractmethod
    async def get_playlist_list(self):
        """returns list of playlists in DB"""
        pass

    @abstractmethod
    async def get_playlist(self):
        """returns a playlist based on its ID"""
        pass

    @abstractmethod
    async def update_playlist(self):
        """Update playlist in DB"""
        pass

    @abstractmethod
    async def remove_playlist(self):
        """Remove playlist from DB"""
        pass

    # TODO: Remove below when done
    @abstractmethod
    async def add_(self):
        """Add _ to DB"""
        pass

    @abstractmethod
    async def get__list(self):
        """returns list of _ in DB"""
        pass

    @abstractmethod
    async def get_(self):
        """returns a _ based on their ID"""
        pass

    @abstractmethod
    async def update_(self):
        """Update _ in DB"""
        pass

    @abstractmethod
    async def remove_(self):
        """Remove _ from DB"""
        pass
