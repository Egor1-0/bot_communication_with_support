from aiogram import Router

from app.handlers.main_handlers import main_command_router
from app.handlers.communicate import communicate_router

main_router = Router()

main_router.include_routers(communicate_router, main_command_router)

