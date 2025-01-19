from pydantic import BaseModel

from core.schemas.ScOrder import OrderRead



class TaskBase(BaseModel):
    city: str
    district: str
    work: str
    price_work: int
    person: int
    fee: int
    phone: str


class TaskCreate(TaskBase):
    is_active: bool


class TaskUpdate(TaskBase):
    city: str | None = None
    district: str | None = None
    work: str | None = None
    price_work: int | None = None
    person: int | None = None
    fee: int | None = None
    phone: str | None = None
    is_active: bool | None = None


class TaskRead(TaskBase):
    id: int
    is_active: bool
    orders: list[OrderRead]


class TaskIdRead(TaskBase):
    id: int
    is_active: bool
