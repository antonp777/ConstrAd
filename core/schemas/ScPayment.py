from datetime import datetime

from pydantic import BaseModel

from core.models import StatusPay



class PaymentBase(BaseModel):
    sum: int
    date: datetime
    status_pay: StatusPay


class PaymentCreate(PaymentBase):
    user_id: int


class PaymentRead(PaymentBase):
    id: int
