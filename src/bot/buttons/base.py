from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from .text import LOCATION, REVIEWS_TYPES


class ButtonBase:
    @property
    def location_buttons(self) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=False, one_time_keyboard=True, row_width=2
        )
        for el in LOCATION:
            keyboard.add(el)

        return keyboard

    @property
    def cancel_photo(self):
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=False, one_time_keyboard=True, row_width=2
        )

        keyboard.add("Завантажити без фото")
        return keyboard

    @property
    def type_of_review_buttons(self) -> InlineKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup()

        for el in REVIEWS_TYPES:
            keyboard.add(el)
            # keyboard.add(InlineKeyboardButton(text=el, callback_data=el))

        return keyboard


keyboards = ButtonBase()
