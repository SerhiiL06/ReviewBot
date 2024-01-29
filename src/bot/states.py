from aiogram.dispatcher.filters.state import State, StatesGroup


class ReviewState(StatesGroup):
    waiting_location = State()
    waiting_comment = State()
    waiting_photo = State()
