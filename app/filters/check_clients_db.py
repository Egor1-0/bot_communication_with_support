from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.google_sheet import *

class CheckClientsDB(BaseFilter):
    async def __call__(self, message: Message):
        if message.from_user.id in clients_db:
            if clients_db[int(str(message.from_user.id))]['product']:
                return True
        return False