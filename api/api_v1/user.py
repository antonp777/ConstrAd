from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.models import db_helper
from core.schemas.ScUser import UserRead, UserCreate
from crud import user as crud_user

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["User"]
)
@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    return await crud_user.get_all_users(session=session)

@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], user_id: int):
    user = await crud_user.get_user_by_id(session=session, user_id=user_id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@router.post("", response_model=UserRead)
async def create_user(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], user_create: UserCreate):
    return await crud_user.create_user(session=session, user_create=user_create)
