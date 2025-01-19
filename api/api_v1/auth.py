from typing import Annotated

from fastapi import APIRouter, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.models import db_helper
from crud.userService import get_token_by_login_password

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Authentication"]
)

@router.post("/loging")
async def loging_user_service(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                              login: str = Form(),
                              password: str = Form()
                              ):
    return await get_token_by_login_password(session=session, login=login, password=password)