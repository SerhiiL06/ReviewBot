from aiogram.types import Message
from aiogram import Bot


async def save_photo(message: Message, bot: Bot):
    result = await message.photo[-1].download(
        destination_dir=f"/Users/serega/Desktop/courses/ReviewBot/media/"
    )

    return result.name
