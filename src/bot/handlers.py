from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from src.bot.buttons.base import keyboards
from src.bot.utils.text import meeting_text, regex_location
from .states import ReviewState
from core.config import bot
import requests
from .utils.api_urls import ADD_REVIEW
from core.mongo import Review


async def hello_hundler(message: Message):
    await message.answer(text=meeting_text)


async def start_review(message: Message, state: FSMContext):
    await message.answer(
        text="Оберіть одну з локацій наших магахинів",
        reply_markup=keyboards.location_buttons,
    )

    await state.set_state(ReviewState.waiting_location.state)


async def set_comment(message: Message, state: FSMContext):
    await state.update_data(location=message.text)

    await message.answer(
        "Ви можете вибрати один із можливих варіантів відрука, або написати свій відгук та за бажанням додати до нього фото",
        reply_markup=keyboards.type_of_review_buttons,
    )

    await state.set_state(ReviewState.waiting_comment.state)


async def set_photo(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)

    await message.answer(
        "Також ви можете завантажити фото по бажанню!",
        reply_markup=keyboards.cancel_photo,
    )


async def register_hundlers(db: Dispatcher):
    db.register_message_handler(hello_hundler, commands=["start"])
    db.register_message_handler(start_review, commands=["review"], state="*")
    db.register_message_handler(set_comment, state=ReviewState.waiting_location)
    db.register_message_handler(set_photo, state=ReviewState.waiting_comment)
    # db.register_message_handler(set_photo, state=ReviewState.waiting_photo)
