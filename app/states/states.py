from aiogram.fsm.state import State, StatesGroup

class GetterProduct(StatesGroup):
    get_product = State()

class Scroll(StatesGroup):
    main_menu_scroll = State()

class Communication(StatesGroup):
    communication = State()