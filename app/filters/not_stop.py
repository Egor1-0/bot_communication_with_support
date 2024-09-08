from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import ADMIN_ID

class NotStop(BaseFilter):
    async def __call__(self, message: Message):
        print(message.from_user.id, ADMIN_ID)
        if int(message.from_user.id) != int(ADMIN_ID):
            return True
        if message.text:
            if message.text.lower() != 'пауза':
                return True
            return False
        return True