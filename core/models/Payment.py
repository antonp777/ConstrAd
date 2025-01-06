from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, date
from .model_enum import StatusPay

if TYPE_CHECKING:
    from .User import User
class Payment(Base):
    sum: Mapped[int]
    date: Mapped[date]
    status_pay: Mapped[StatusPay]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="payments")
