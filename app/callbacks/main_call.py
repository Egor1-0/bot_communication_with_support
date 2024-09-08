from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.database.queries import push_pair
from app.keyboards import ContComm

call_router = Router()


@call_router.callback_query(ContComm.filter(F.action == "cont"))
async def communicate(callback: CallbackQuery, callback_data: ContComm):
    await callback.answer()
    await callback.message.answer("Диалог возобновлен")
    await callback.bot.send_message(chat_id=callback_data.us_id, text="Менеджер на связи. Он готов ответить на ваши вопросы.")
    await push_pair(callback.from_user.id, callback_data.us_id)