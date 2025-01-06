from typing import Optional

from pydantic import BaseModel, ConfigDict

from core.models import RoleUser

from core.schemas.ScOrder import OrderRead
from core.schemas.ScPayment import PaymentRead


class UserBase(BaseModel):
    name_user: str
    tg_id: int
    role_user: RoleUser


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    payments: list[PaymentRead] | None
    orders: list[OrderRead] | None
