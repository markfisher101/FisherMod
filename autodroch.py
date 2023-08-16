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
    """Модуль для автоматической дрочки и выращивания хуя в боте @xyu_epta_bot
    Использовать команду старта в чате где нужно фармить."""

    strings = {"name": "AutoDroch"}

    def __init__(self):
        self.tasks = []

    async def a_run(self, message):
        while True:
            await message.reply("/dick@xyu_epta_bot")
            await asyncio.sleep(21600)
            await message.reply("/drochnut@xyu_epta_bot")
            await asyncio.sleep(3960)

    @loader.unrestricted
    @loader.ratelimit
    async def drochcmd(self, message):
        """Запустить автодрочку в боте"""
        if self.tasks:
            return await message.edit("Автодрочка уже запущена.")
        await message.edit("Автодрочка запущена.")
        self.tasks = [asyncio.create_task(self.a_run(message)),]

    @loader.unrestricted
    @loader.ratelimit
    async def drochstopcmd(self, message):
        """Остановить автодрочкуг в боте"""
        if not self.tasks:
            return await message.edit("Автодрочка не запущена.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автодрочка остановлена.")
