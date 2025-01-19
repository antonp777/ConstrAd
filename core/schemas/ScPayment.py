from datetime import datetime

from pydantic import BaseModel, ConfigDict

from core.models import StatusPay
from utils.date import date_time


class PaymentBase(BaseModel):
    sum: int
    date: datetime
    status_pay: StatusPay


class PaymentCreate(PaymentBase):
    user_id: int
    status_pay: StatusPay = StatusPay.WAIT
    date: datetime = date_time()
    comment: str

class PaymentUpdate(PaymentBase):
    sum: int | None = None
    date: datetime | None = None
    status_pay: StatusPay | None = None


class PaymentRead(PaymentBase):
    id: int
