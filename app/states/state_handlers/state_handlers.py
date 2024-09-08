from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import app.keyboards.reply.main_kb as kb
from app.google_sheet import * 
from app.filters import CheckClientsDB
from app.states.states import GetterProduct
from config import CHANNEL_ID

state_handlers = Router()


@state_handlers.message(F.text.in_(["Картридж", "Румбокс"]))
async def choose_product(message: Message, state: FSMContext):
    product = message.text
    clients_db[message.from_user.id] = {'product': product, 'issue': None}

    await message.answer(f"Вы выбрали: {product}. Напишите вашу проблему.",
                     reply_markup=kb.del_kb)

    await state.set_state(GetterProduct.get_product)
    

@state_handlers.message(CheckClientsDB(), GetterProduct.get_product)
async def receive_issue(message: Message, state: FSMContext):
    user_id = message.from_user.id
    clients_db[user_id]['issue'] = message.text

    await message.answer('Спасибо! Мы получили вашу проблему. Мы свяжемся с вами скоро.')

    await message.bot.send_message(chat_id=CHANNEL_ID, text=f"Новый запрос от {user_id}: {clients_db[user_id]['product']} - {message.text}")

    save_to_google_sheets(user_id, clients_db[user_id]['product'], message.text)

    await state.clear()