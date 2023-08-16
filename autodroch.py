#developed by: @sukrammi
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class AutoDrochMod(loader.Module):
    """Модуль для автоматической дрочки и выращивания хуя в боте @xyu_epta_bot"""

    strings = {"name": "AutoDroch"}

    def __init__(self):
        self.tasks = []

    async def a_run(self, client):
        while True:
            await message.send_message("/drochnut@hyu_epta_bot")
            await asyncio.sleep(3900)

    async def b_run(self, client):
        while True:
            await message.send_message("/dick@hyu_epta_bot")
            await asyncio.sleep(21600)


    @loader.unrestricted
    @loader.ratelimit
    async def drochcmd(self, message):
        """Запустить автоматическую дрочку"""
        if self.tasks:
            return await message.edit("Авто дрочка уже запущена.")
        await message.edit("Авто дрочка запущена.")
        client = message.client
        self.tasks = [asyncio.create_task(self.a_run(message)), asyncio.create_task(self.b_run(message))]

    @loader.unrestricted
    @loader.ratelimit
    async def drochoffcmd(self, message):
        """Остановить автоматическую дрочку"""
        if not self.tasks:
            return await message.edit("Авто дрочка не запущена.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Авто дрочка остановлена.")