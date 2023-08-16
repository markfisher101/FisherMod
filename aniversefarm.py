# developed by: @sukrammi
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmAniverseMod(loader.Module):
    """Модуль для автоматического фарминга в игровом боте @aniversecard_bot"""

    strings = {"name": "AniverseFarm"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@aniversecard_bot', "Получить карту")
            await asyncio.sleep(14400)

    @loader.unrestricted
    @loader.ratelimit
    async def cardcmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Автоматический фарминг уже запущен.")
        await message.edit("Автоматический фарминг запущен.")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client)),]

    @loader.unrestricted
    @loader.ratelimit
    async def cardstopcmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический фарминг не запущен.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический фарминг остановлен.")