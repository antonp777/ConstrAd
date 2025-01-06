from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .model_enum import RoleUser

if TYPE_CHECKING:
    from .Payment import Payment
    from .Order import Order

class User(Base):
    name_user: Mapped[str]
    tg_id: Mapped[int] = mapped_column(BigInteger)
    role_user: Mapped[RoleUser]
    payments: Mapped[list["Payment"]] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
