from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from auth.auth_helper import creation_token_for_user_service
from core.models import UserService
from core.schemas.ScUserService import UserServiceCreate, UserServiceUpdate

from auth.utils import hash_password, validate_password


async def get_all_users_service(session: AsyncSession) -> list[UserService]:
    stm = (select(UserService).
           order_by(UserService.id)
           )
    result = await session.execute(stm)
    users = result.unique().scalars().all()
    return list(users)


async def get_user_service_by_id(session: AsyncSession, user_id: int) -> UserService | None:
    stm = (select(UserService).
           where(UserService.id == user_id)
           )
    result = await session.execute(stm)
    try:
        return result.unique().scalars().one()
    except SQLAlchemyError:
        return None


async def get_user_service_by_login(session: AsyncSession, user_login: str) -> UserService | None:
    stm = (select(UserService).
           where(UserService.login == user_login)
           )
    result = await session.execute(stm)
    try:
        return result.unique().scalars().one()
    except SQLAlchemyError:
        return None


async def get_token_by_login_password(session: AsyncSession, login: str, password: str) -> str | HTTPException:
    stm = (select(UserService).
           where(UserService.login == login)
           )
    result = await session.execute(stm)
    try:
        user: UserService = result.unique().scalars().one()
        if validate_password(password=password, hashed_password=user.password):
            return user.token
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    except SQLAlchemyError:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


async def create_user_service(session: AsyncSession, user_create: UserServiceCreate) -> HTTPException:
    user = UserService(**user_create.model_dump())

    # Шифрование пароля
    user.password = hash_password(user_create.password)

    session.add(user)
    await session.flush()

    # Создание токена
    user.token = creation_token_for_user_service(user=user).access_token
    # await session.refresh(user)
    await session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail=f"User created successfully. Id = {user.id}")


async def update_user_service(session: AsyncSession, user: UserService,
                              user_update: UserServiceUpdate | None, token_update: bool = False) -> HTTPException:
    if user_update:
        for name, value in user_update.model_dump(exclude_unset=True).items():
            setattr(user, name, value)
        if user_update.password is not None:
            user.password = hash_password(user_update.password)

    if token_update:
        user.token = creation_token_for_user_service(user).access_token
    await session.commit()
    return HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f"User update successfully")
