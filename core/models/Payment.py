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
    comment: Mapped[str] = mapped_column(default="admin_create", server_default="admin_create")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="payments")

    def __str__(self):
        return f"Платёж #{self.id} | Дата: {self.date} | Статус: {self.status_pay}"
