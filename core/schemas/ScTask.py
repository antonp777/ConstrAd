from pydantic import BaseModel

from core.models import StatusTask

from core.schemas.ScUser import OrderRead


class TaskBase(BaseModel):
    city: str
    district: str
    work: str
    price_work: int
    person: int
    fee: int
    phone: str
    status_task: StatusTask

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    city: str | None = None
    district: str | None = None
    work: str | None = None
    price_work: int | None = None
    person: int | None = None
    fee: int | None = None
    phone: str | None = None
    status_task: StatusTask | None = None

class TaskRead(TaskBase):
    id: int
    orders: list[OrderRead]