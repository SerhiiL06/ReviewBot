from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.utils.text import LOCATION_LIST, REVIEWS_TYPES, cancel_write_review


class ButtonBase:
    @property
    def start_review_button(self) -> ReplyKeyboardMarkup:
        # start review button
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add("Залишити відгук 📋")

        return keyboard

    @property
    def location_buttons(self) -> ReplyKeyboardMarkup:
        # list of location name
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.row(KeyboardButton(LOCATION_LIST[0]), KeyboardButton(LOCATION_LIST[1]))
        keyboard.row(KeyboardButton(LOCATION_LIST[2]), KeyboardButton(LOCATION_LIST[3]))
        keyboard.add(KeyboardButton(LOCATION_LIST[4]))
        keyboard.add(KeyboardButton(cancel_write_review))

        return keyboard

    @property
    def cancel_photo(self) -> ReplyKeyboardMarkup:
        # select review without photo
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )

        keyboard.add("Завантажити без фото")
        keyboard.add(KeyboardButton(cancel_write_review))
        return keyboard

    @property
    def type_of_review_buttons(self) -> ReplyKeyboardMarkup:
        # list of review type
        keyboard = ReplyKeyboardMarkup(
            one_time_keyboard=True,
        )

        keyboard.row(KeyboardButton(REVIEWS_TYPES[0]), KeyboardButton(REVIEWS_TYPES[1]))

        keyboard.add(KeyboardButton("залишити коментар"))
        keyboard.add(KeyboardButton(cancel_write_review))

        return keyboard


keyboards = ButtonBase()
