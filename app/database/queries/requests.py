from sqlalchemy import update, select

from app.database.models import Pair
from app.database.session import async_session


async def get_pair(tg_id: int):
    async with async_session() as session:
        if await session.scalar(select(Pair).where(Pair.tg_user_id_1 == tg_id)):
            return (await session.execute(select(Pair.tg_user_id_2).where(Pair.tg_user_id_1 == tg_id))).fetchone()
        elif await session.scalar(select(Pair).where(Pair.tg_user_id_2 == tg_id)):
            return (await session.execute(select(Pair.tg_user_id_1).where(Pair.tg_user_id_2 == tg_id))).fetchone()