from sqlalchemy import update, select

from app.database.models import Pair
from app.database.session import async_session


async def push_pair(tg_id_1: int, tg_id_2: int):
    async with async_session() as session:
        session.add(Pair(tg_user_id_1=tg_id_1, tg_user_id_2=tg_id_2))
        await session.commit()