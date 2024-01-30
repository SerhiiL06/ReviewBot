from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from src.bot.buttons import keyboards
from src.utils.text import help_text, meeting_text


async def hello_hundler(message: Message) -> None:
    # work after start command
    await message.answer(meeting_text, reply_markup=keyboards.start_review_button)


async def help_hudler(message: Message) -> None:
    # work after help command
    await message.answer(help_text)


async def cancel_hudler(message: Message, state: FSMContext) -> None:
    # work after cancel command
    await state.finish()
    await message.answer("Операцію успішно відмінено")
