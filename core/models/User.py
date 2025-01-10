from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .Payment import Payment
    from .Order import Order
    from .Task import Task


class User(Base):
    name_user: Mapped[str]
    tg_id: Mapped[int] = mapped_column(BigInteger)
    is_active: Mapped[bool] = mapped_column(default=True, server_default="True")
    payments: Mapped[list["Payment"]] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
    tasks: Mapped[list["Task"]] = relationship(
        secondary="orders",
        back_populates="users"
    )

    def __str__(self):
        return f"Пользователь ID: {self.id} | Имя: {self.name_user} | ID Telegram: {self.tg_id}"
