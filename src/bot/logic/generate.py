from openai import OpenAI
from core.config import settings
from aiogram.dispatcher import FSMContext
from src.bot.utils.promt import system_promt

client = OpenAI(api_key=settings.get_openai_token)


async def generate_answer(state: FSMContext) -> str:
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
