from pydantic import BaseModel

from core.schemas.ScOrder import OrderRead
from core.schemas.ScPayment import PaymentRead
from core.schemas.ScTask import TaskIdRead


class UserBase(BaseModel):
    name_user: str
    tg_id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name_user: str | None = None
    tg_id: int | None = None
    is_active: bool | None = None


class UserRead(UserBase):
    id: int
    is_active: bool
    payments: list[PaymentRead]
    orders: list[OrderRead]
    tasks: list[TaskIdRead]

class UserIdRead(UserBase):
    id: int
    is_active: bool

