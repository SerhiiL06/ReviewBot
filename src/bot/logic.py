from openai import OpenAI
from core.config import settings
from aiogram.dispatcher import FSMContext
from src.utils.promt import system_promt

client = OpenAI(api_key=settings.get_openai_token)


from aiogram.types import Message


async def save_photo(message: Message):
    result = await message.photo[-1].download(
        destination_dir=f"/Users/serega/Desktop/courses/ReviewBot/media/"
    )

    return result.name


from core.mongo import Review
from aiogram.dispatcher import FSMContext
from datetime import datetime


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
