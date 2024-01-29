from aiogram import Dispatcher, Bot

from core.config import settings

from src.bot.handlers import register_hundlers

from aiogram.contrib.fsm_storage.memory import MemoryStorage


import asyncio


async def main():
    bot = Bot(settings.get_token)

    app = Dispatcher(bot, storage=MemoryStorage())

    await register_hundlers(app)

    await app.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
