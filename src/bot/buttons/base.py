from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
)
from src.bot.utils.text import LOCATION_LIST, REVIEWS_TYPES


class ButtonBase:
    @property
    def location_buttons(self) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.row(
            KeyboardButton(LOCATION_LIST[0]),
            KeyboardButton(LOCATION_LIST[1]),
            KeyboardButton(LOCATION_LIST[2]),
            KeyboardButton(LOCATION_LIST[3]),
        )
        keyboard.add(KeyboardButton(LOCATION_LIST[4]))

        # for el in LOCATION:
        #     keyboard.add(KeyboardButton(el))

        return keyboard

    @property
    def cancel_photo(self):
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.add("Завантажити без фото")
        return keyboard

    @property
    def type_of_review_buttons(self) -> InlineKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            one_time_keyboard=True,
        )

        for el in REVIEWS_TYPES:
            keyboard.add(el)
            # keyboard.add(InlineKeyboardButton(text=el, callback_data=el))

        return keyboard


keyboards = ButtonBase()
