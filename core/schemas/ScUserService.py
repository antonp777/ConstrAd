from pydantic import BaseModel

from core.models import RoleUserService
from core.schemas.ScOrder import OrderRead
from core.schemas.ScPayment import PaymentRead
from core.schemas.ScTask import TaskIdRead


class UserServiceBase(BaseModel):
    login: str
    tg_id: int
    role_user: RoleUserService


class UserCreate(UserServiceBase):
    password: str


class UserUpdate(UserServiceBase):
    login: str | None = None
    tg_id: int | None = None
    role_user: RoleUserService | None = None
    is_active: bool | None = None
    password: str | None = None


class UserRead(UserServiceBase):
    id: int
    is_active: bool
