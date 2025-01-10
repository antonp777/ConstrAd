from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .Order import Order
    from .User import User


class Task(Base):
    city: Mapped[str]
    district: Mapped[str]
    work: Mapped[str]
    price_work: Mapped[int]
    person: Mapped[int]
    fee: Mapped[int]
    phone: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True, server_default="True")

    orders: Mapped[list["Order"]] = relationship(back_populates="task")
    users: Mapped[list["User"]] = relationship(
        secondary="orders",
        back_populates="tasks"
    )

    def __str__(self):
        return f"Задание #{self.id}"
