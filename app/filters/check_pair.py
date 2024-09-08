from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database.queries import get_pair

class CheckPair(BaseFilter):
    async def __call__(self, message: Message):        
        if await get_pair(message.from_user.id):
            return True
        return None