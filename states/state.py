from aiogram.dispatcher.filters.state import State, StatesGroup

class GetVacuumState(StatesGroup):
    getTable = State()
    getType = State()
