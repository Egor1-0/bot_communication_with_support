from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Pair(Base):
    __tablename__ = "pairs"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_user_id_1: Mapped[int] = mapped_column(BigInteger)
    tg_user_id_2: Mapped[int] = mapped_column(BigInteger)
