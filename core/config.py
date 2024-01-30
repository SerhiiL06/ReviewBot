import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


class GlobalSettings:
    _TOKEN = os.getenv("TELEGRAM_TOKEN")
    _OPENAI = os.getenv("OPENAI")

    @property
    def get_token(self):
        return self._TOKEN

    @property
    def get_openai_token(self):
        return self._OPENAI


settings = GlobalSettings()


bot = Bot(settings.get_token)


dp = Dispatcher(bot, storage=MemoryStorage())
