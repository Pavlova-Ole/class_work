"""используем from для импорта aiogram """
from aiogram.fsm.state import State, StatesGroup


class Anketa(StatesGroup):
    """используем class для создания объектов """
    name = State()
    age = State()
    gender = State()
