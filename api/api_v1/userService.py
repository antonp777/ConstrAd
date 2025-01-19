from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.current_user import get_current_super_admin_auth_user, get_current_active_auth_user
from core import settings
from core.models import db_helper
from core.schemas.ScUserService import UserServiceRead, UserServiceCreate, UserServiceUpdate
from crud import userService as crud_user_service

router = APIRouter(
    prefix=settings.api.v1.users_service,
    tags=["UserService"]
)


@router.get("",
            response_model=list[UserServiceRead])
async def get_users(token_key: Annotated[bool, Depends(get_current_super_admin_auth_user)],
                    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                    ):
    if token_key:
        return await crud_user_service.get_all_users_service(session=session)


@router.get("/{user_id}",
            response_model=UserServiceRead)
async def get_user_by_id(token_key: Annotated[bool, Depends(get_current_super_admin_auth_user)],
                         session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                         user_id: int):

    if token_key:
        user = await crud_user_service.get_user_service_by_id(session=session,
                                                              user_id=user_id)
        if user:
            return user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_description="User created successfully")
async def create_user(token_key: Annotated[bool, Depends(get_current_super_admin_auth_user)],
                      session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                      user_create: UserServiceCreate):
    if token_key:
        return await crud_user_service.create_user_service(session=session,
                                                           user_create=user_create)


@router.patch("/{user_id}",
              status_code=status.HTTP_202_ACCEPTED,
              response_description="User update successfully")
async def update_user(token_key: Annotated[bool, Depends(get_current_super_admin_auth_user)],
                      session: Annotated[AsyncSession, Depends(db_helper.session_getter)], user_id: int,
                      user_update: UserServiceUpdate):
    if token_key:
        user = await crud_user_service.get_user_service_by_id(session=session,
                                                              user_id=user_id)
        if user:
            return await crud_user_service.update_user_service(session=session,
                                                               user=user,
                                                               user_update=user_update)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
