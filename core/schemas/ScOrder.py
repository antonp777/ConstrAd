from datetime import datetime

from pydantic import BaseModel

from utils.date import date_time


class OrderBase(BaseModel):
    task_fee: int
    task_person: int
    date: datetime

class OrderCreate(OrderBase):
    user_id: int
    task_id: int
    date: datetime = date_time()

class OrderUpdate(OrderBase):
    task_fee: int | None = None
    task_person: int | None = None
    date: datetime | None = None
    user_id: int | None = None
    task_id: int | None = None

class OrderRead(OrderCreate):
    id: int
