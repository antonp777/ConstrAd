from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    task_fee: int
    task_person: int
    date: datetime

class OrderCreate(OrderBase):
    user_id: int
    task_id: int

class OrderRead(OrderBase):
    id: int