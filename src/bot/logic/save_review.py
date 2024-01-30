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
