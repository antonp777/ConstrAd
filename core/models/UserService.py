from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .model_enum import RoleUserService


class UserService(Base):
    login: Mapped[str]
    password: Mapped[bytes]
    tg_id: Mapped[int] = mapped_column(BigInteger)
    role_user: Mapped[RoleUserService]
    token: Mapped[str] = mapped_column(default="None", server_default="None")
    is_active: Mapped[bool] = mapped_column(default=True, server_default="True")

    def __str__(self):
        return f"Администратор ID: {self.id} | Имя: {self.login} | ID Telegram: {self.tg_id}"
