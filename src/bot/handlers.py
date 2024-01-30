from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from src.bot.buttons.base import keyboards

from src.bot.commands import hello_hundler, help_hudler, cancel_hudler
from src.utils.text import (
    LOCATION_LIST,
    REVIEWS_TYPES,
    select_location_text,
    select_location_error_text,
    select_type_of_review_text,
    select_photo_text,
    waiting_for_comment_text,
    gratitude_text,
)
from .states import ReviewState
from src.bot.logic import save_photo, generate_answer_with_ai, save_review
from core.config import bot


async def start_review(message: Message, state: FSMContext):
    await message.answer(
        select_location_text,
        reply_markup=keyboards.location_buttons,
    )

    await state.set_state(ReviewState.waiting_location.state)


async def set_comment(message: Message, state: FSMContext):
    if message.text.lower() not in LOCATION_LIST:
        # if user set uncorrect location name we're asking him to do it again
        await message.answer(select_location_error_text)
        return

    await state.update_data(
        user_id=message.from_user.id, location=message.text.capitalize()
    )

    await message.answer(
        select_type_of_review_text,
        reply_markup=keyboards.type_of_review_buttons,
    )

    await state.set_state(ReviewState.waiting_comment.state)


async def set_photo(message: Message, state: FSMContext):
    # save state of comment data
    await state.update_data(comment=message.text)

    if message.text.lower() in REVIEWS_TYPES:
        # if user select template answer we save him reviews and send gratitude message
        await save_review(state, "auto")
        await message.answer(
            gratitude_text,
            reply_markup=keyboards.start_review_button,
        )
        return

    if message.text.lower() == "залишити коментар":
        # ask the user to write a review
        await message.answer(waiting_for_comment_text)
        await state.set_state(ReviewState.waiting_comment.state)
        return

    await message.answer(
        select_photo_text,
        reply_markup=keyboards.cancel_photo,
    )

    await state.set_state(ReviewState.waiting_photo.state)


async def send_review(message: Message, state: FSMContext):
    # generate answer using OpenAI
    answer = await generate_answer_with_ai(state)

    # send answer to user and save data in DB
    await message.answer(answer, reply_markup=keyboards.start_review_button)
    await save_review(state, "manually")

    await message.answer(reply_markup=keyboards.start_review_button)


async def send_review_with_image(message: Message, state: FSMContext):
    # download review photo and take path to save in DB
    url = await save_photo(message, bot)
    await state.update_data(image_url=url)

    # generate answer using OpenAI
    answer = await generate_answer_with_ai(state)

    # send answer to user and save data in DB
    await message.answer(answer, reply_markup=keyboards.start_review_button)
    await save_review(state, "manually")


async def register_handlers(db: Dispatcher):
    # register commands handlers
    db.register_message_handler(hello_hundler, commands=["start"])
    # dp.register_message_handler(help_hudler, commands=["help"])
    # dp.register_message_handler(cancel_hudler, commands=["cancel"])
    # dp.register_message_handler(start_review, commands=["review"], state="*")

    # # register message handlers
    # dp.register_message_handler(start_review, regexp="Залишити відгук", state="*")
    # dp.register_message_handler(set_comment, state=ReviewState.waiting_location)
    # dp.register_message_handler(set_photo, state=ReviewState.waiting_comment)
    # dp.register_message_handler(
    #     send_review_with_image, content_types=["photo"], state="*"
    # )
    # dp.register_message_handler(
    #     send_review, content_types=["text"], state=ReviewState.waiting_photo
    # )
