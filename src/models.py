import datetime
from enum import Enum
from typing import Annotated
from sqlalchemy import  ForeignKey, String, func, text
from database import Base, str_500
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class PriceOrm(Base):
    """Готовый контент на отправку"""
    __tablename__ = "price"
    id: Mapped[intpk]
    price: Mapped[str_500]
    created_at: Mapped[created_at]


