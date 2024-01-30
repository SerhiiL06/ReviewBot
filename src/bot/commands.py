from src.utils.text import help_text, meeting_text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from .buttons.base import keyboards


async def hello_hundler(message: Message):
    await message.answer(meeting_text, reply_markup=keyboards.start_review_button)


async def help_hudler(message: Message):
    await message.answer(help_text)


async def cancel_hudler(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Операцію успішно відмінено")
