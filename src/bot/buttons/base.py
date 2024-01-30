from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
)
from src.utils.text import LOCATION_LIST, REVIEWS_TYPES


class ButtonBase:
    CANCEL_BUTTON = "Відмінити 🛑"

    @property
    def start_review_button(self) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add("Залишити відгук")

        return keyboard

    @property
    def location_buttons(self) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.row(KeyboardButton(LOCATION_LIST[0]), KeyboardButton(LOCATION_LIST[1]))
        keyboard.row(KeyboardButton(LOCATION_LIST[2]), KeyboardButton(LOCATION_LIST[3]))
        keyboard.add(KeyboardButton(LOCATION_LIST[4]))
        keyboard.add(KeyboardButton(self.CANCEL_BUTTON))

        return keyboard

    @property
    def cancel_photo(self):
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.add("Завантажити без фото")
        keyboard.add(KeyboardButton(self.CANCEL_BUTTON))
        return keyboard

    @property
    def type_of_review_buttons(self) -> InlineKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(
            one_time_keyboard=True,
        )

        for el in REVIEWS_TYPES:
            keyboard.add(KeyboardButton(el))

        return keyboard


keyboards = ButtonBase()
