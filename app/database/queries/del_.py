from sqlalchemy import update, select, delete

from app.database.models import Pair
from app.database.session import async_session


async def delete_pair(tg_id):
    async with async_session() as session:
        if await session.scalar(select(Pair).where(Pair.tg_user_id_1 == tg_id)):
            await session.execute(delete(Pair).where(Pair.tg_user_id_1 == tg_id))
            await session.commit()

        elif await session.scalar(select(Pair).where(Pair.tg_user_id_2 == tg_id)):
            await session.execute(delete(Pair).where(Pair.tg_user_id_2 == tg_id))
            await session.commit()