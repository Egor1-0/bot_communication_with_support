from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager

import app.keyboards.reply.main_kb as kb
from app.google_sheet import * 
from app.states.states import Scroll

from config import ADMIN_ID


main_command_router = Router()


@main_command_router.message(CommandStart())
async def start(message: Message):
    load_data()  # Загружаем данные при старте

    welcome_text = "Привет! Какой товар вас интересует? Выберите из списка."
    welcome_text += "\nТакже у вас есть доступ к панели администратора."

    await message.answer(welcome_text, reply_markup=kb.main_keyboard(message.from_user.id == ADMIN_ID))


@main_command_router.message(Command('reply'), F.from_user.id == int(ADMIN_ID))
async def reply(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=Scroll.main_menu_scroll)