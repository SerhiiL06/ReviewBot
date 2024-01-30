from aiogram import Dispatcher, Bot

from core.config import bot, dp

from src.bot.handlers import register_hundlers

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand


import asyncio


async def main():
    BotCommand(command="help", description="Про що цей бот")

    await register_hundlers(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
