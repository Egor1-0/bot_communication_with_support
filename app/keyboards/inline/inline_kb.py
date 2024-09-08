from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.keyboards.inline.call_data import ContComm

async def cont_comm(user_id: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Возобновить", 
                    callback_data=ContComm(
                                            action="cont",
                                            us_id=user_id
                                            ).pack())
    return keyboard.as_markup()