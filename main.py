import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from app.database.session import create_session
from app.handlers import main_router
from app.states.state_handlers.state_handlers import state_handlers
from app.dialogs.main_dialog import scroll_dialog
from app.callbacks.main_call import call_router


load_dotenv()


async def main():
    await create_session()
    bot = Bot(token=os.getenv("TOKEN")) 
    dp = Dispatcher()
    dp.include_routers(main_router, state_handlers, scroll_dialog, call_router)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass