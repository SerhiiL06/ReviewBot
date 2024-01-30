from aiogram.dispatcher import FSMContext
from openai import OpenAI

from core.config import BASE_DIR, settings
from src.utils.promt import system_promt

client = OpenAI(api_key=settings.get_openai_token)


from aiogram.types import Message


async def cancel_operation(state: FSMContext, message: Message):
    await state.finish()
    return await message.answer("Ви в будь-який час можете знову це зробити :)")


async def save_photo(message: Message):
    result = await message.photo[-1].download(destination_dir=BASE_DIR / "media")

    return result.name


from datetime import datetime

from aiogram.dispatcher import FSMContext

from core.mongo import Review


async def save_review(state: FSMContext, method: str):
    await state.update_data(
        method=method,
        create_date=datetime.now(),
    )
    data = await state.get_data()
    Review.insert_one(data)

    await state.finish()


async def generate_answer_with_ai(state: FSMContext) -> str:
    user_review = await state.get_data()
    anser = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_promt,
            },
            {
                "role": "user",
                "content": user_review.get("comment"),
            },
        ],
    )

    return anser.choices[0].message.content
