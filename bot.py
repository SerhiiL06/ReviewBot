from core.config import dp
from aiogram import executor
from src.bot.handlers import register_handlers


import asyncio


async def main():
    await register_handlers(dp)
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
