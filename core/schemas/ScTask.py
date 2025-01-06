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

class TaskRead(TaskBase):
    id: int
    orders: list[OrderRead]