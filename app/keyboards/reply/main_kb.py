from aiogram.types import ReplyKeyboardRemove   
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard(is_admin: bool):
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Картридж")
    keyboard.button(text="Румбокс")
    # if is_admin:
    #     keyboard.button(text="Открыть панель администратора") 
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)


del_kb = ReplyKeyboardRemove()