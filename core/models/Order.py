from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, date

if TYPE_CHECKING:
    from .User import User
    from .Task import Task
class Order(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    task_fee: Mapped[int]
    task_person: Mapped[int]
    date: Mapped[date]


    user: Mapped["User"] = relationship(back_populates="orders")
    task: Mapped["Task"] = relationship(back_populates="orders")



