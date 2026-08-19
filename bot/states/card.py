from aiogram.fsm.state import State, StatesGroup


class CardState(StatesGroup):
    waiting_photo = State()
    waiting_description = State()
    choosing_marketplace = State()
    confirming_concept = State()
    generating = State()
