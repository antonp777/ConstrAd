from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth_helper import get_current_token_payload
from core.models import UserService, db_helper
from crud.userService import get_user_service_by_id
from core.models import model_enum


# Получение user из payload
async def get_current_auth_user(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        payload: dict = Depends(get_current_token_payload),

) -> UserService:
    user_id: int | None = int(payload.get("sub"))
    user = await get_user_service_by_id(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid",
    )


# Проверка user на активность
def get_current_active_auth_user(
        user: UserService = Depends(get_current_auth_user),
) -> bool:
    if user.is_active:
        return True
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive",
    )


# Проверка user на активность и SuperAdmin
def get_current_super_admin_auth_user(
        user: UserService = Depends(get_current_auth_user),
) -> bool:
    if user.is_active and user.role_user == model_enum.RoleUserService.SUPER_ADMIN:
        return True
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user has not role SuperAdmin",
    )
