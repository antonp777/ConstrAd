from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .model_enum import StatusTask

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
    status_task: Mapped[StatusTask]

    orders: Mapped[list["Order"]] = relationship(back_populates="task")