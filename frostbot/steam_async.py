from steam.steamid import SteamID
import discord
import asyncio
import re

steam2Pattern = re.compile(r"STEAM_[0-9]:[0-9]:[0-9]+")
steam3Pattern = re.compile(r"\[[A-Z]:[1-4]:\d{1,10}\]")


async def get_steam_user(bot, id: str):
    if id.isdigit() or steam2Pattern.match(id) or steam3Pattern.match(id):
        return await bot.loop.run_in_executor(None, SteamID, id)
    else:
        return await bot.loop.run_in_executor(None, SteamID.from_url, f"https://steamcommunity.com/id/{id}/")


def get_steam_user_sync(bot, id: str):
    if id.isdigit() or steam2Pattern.match(id) or steam3Pattern.match(id):
        return SteamID(id)
    else:
        return SteamID.from_url(f"https://steamcommunity.com/id/{id}/")
