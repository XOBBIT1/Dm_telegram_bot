from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    any_text = State()
