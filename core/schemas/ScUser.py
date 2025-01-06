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


class UserUpdate(UserBase):
    name_user: str | None = None
    tg_id: int | None = None
    role_user: RoleUser | None = None


class UserRead(UserBase):
    id: int
    payments: list[PaymentRead]
    orders: list[OrderRead]
