from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from src.bot.buttons.base import keyboards

from src.bot.utils.text import meeting_text
from src.bot.utils.text import LOCATION_LIST
from .states import ReviewState
from .logic.save_photo import save_photo
from .logic.generate import generate_answer
from .logic.save_review import save_review
from core.config import bot
from datetime import datetime


async def hello_hundler(message: Message):
    await message.answer(text=meeting_text)


async def start_review(message: Message, state: FSMContext):
    await message.answer(
        text="Оберіть одну з локацій наших магазинів",
        reply_markup=keyboards.location_buttons,
    )

    await state.set_state(ReviewState.waiting_location.state)


async def set_comment(message: Message, state: FSMContext):
    if message.text.capitalize() not in LOCATION_LIST:
        await message.answer("Будь ласка вибері конкретну назву локації")
        return
    await state.update_data(user_id=message.from_user.id, location=message.text)

    await message.answer(
        "Ви можете вибрати один із можливих варіантів відрука, або написати свій відгук та за бажанням додати до нього фото",
        reply_markup=keyboards.type_of_review_buttons,
    )

    await state.set_state(ReviewState.waiting_comment.state)


async def set_photo(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)

    if message.text == "Все чисто!":
        await save_review(state, "auto")
        await message.answer("Дякуємо за ваш відгук, нам важливий кожен клієнт!")
        return

    if message.text.lower() == "залишити коментар":
        await state.set_state(ReviewState.waiting_comment.state)
        return

    await message.answer(
        "Також ви можете завантажити фото по бажанню!",
        reply_markup=keyboards.cancel_photo,
    )

    await state.set_state(ReviewState.waiting_photo.state)


async def send_review(message: Message, state: FSMContext):
    await message.delete()

    answer = await generate_answer(state)
    await message.answer(answer)
    await save_review(state, "manually")


async def send_review_with_image(message: Message, state: FSMContext):
    url = await save_photo(message, bot)

    await state.update_data(image_url=url)

    answer = await generate_answer(state)
    await message.answer(answer)

    await save_review(state, "manually")


async def register_hundlers(db: Dispatcher):
    db.register_message_handler(hello_hundler, commands=["start"])
    db.register_message_handler(start_review, commands=["review"], state="*")
    db.register_message_handler(set_comment, state=ReviewState.waiting_location)
    db.register_message_handler(set_photo, state=ReviewState.waiting_comment)
    db.register_message_handler(
        send_review_with_image, content_types=["photo"], state="*"
    )
    db.register_message_handler(
        send_review, content_types=["text"], state=ReviewState.waiting_photo
    )
