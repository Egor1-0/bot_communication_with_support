from aiogram import Router, F
from aiogram.types import Message

import app.keyboards as kb
from app.database.queries import get_pair
from app.filters import CheckPair, NotStop
from app.database.queries import delete_pair

communicate_router = Router()

communicate_router.message.filter(CheckPair())

@communicate_router.message(NotStop())
async def communicate(message: Message):
    pair = (await get_pair(message.from_user.id))[0]
    # print(pair[0])
    await message.bot.copy_message(chat_id=pair, from_chat_id=message.chat.id, message_id=message.message_id)


@communicate_router.message(~NotStop())
async def pause_communicate(message: Message):
    pair = (await get_pair(message.from_user.id))[0]
    await message.answer(f"Диалог с {pair} прерван", reply_markup=await kb.cont_comm(pair))
    await message.bot.send_message(chat_id=pair, 
                                   text="Менеджер отошёл, но скоро вернётся." 
                                   "Ожидайте его сообщения. Учтите, что отправленные сообщения не дойдут до менеджера.")
    await delete_pair(message.from_user.id)