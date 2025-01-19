import asyncio

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import User
from core.schemas.ScUser import UserCreate, UserUpdate


async def get_all_users(session: AsyncSession) -> list[User]:
    stm = (select(User).
           options(joinedload(User.payments),
                   joinedload(User.orders),
                   selectinload(User.tasks)).
           order_by(User.id))
    result = await session.execute(stm)
    users = result.unique().scalars().all()
    return list(users)


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    stm = (select(User).
           where(User.id == user_id).
           options(joinedload(User.payments),
                   joinedload(User.orders),
                   selectinload(User.tasks)))
    result = await session.execute(stm)
    try:
        return result.unique().scalars().one()
    except SQLAlchemyError:
        return None


async def get_user_by_tg_id(session: AsyncSession, tg_id: int) -> User | None:
    stm = (select(User).
           where(User.tg_id == tg_id).
           options(joinedload(User.payments),
                   joinedload(User.orders),
                   selectinload(User.tasks)))
    result = await session.execute(stm)
    try:
        return result.unique().scalars().one()
    except SQLAlchemyError:
        return None


async def create_user(session: AsyncSession, user_create: UserCreate) -> HTTPException:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()

    # await session.refresh(user)
    return HTTPException(status_code=status.HTTP_201_CREATED, detail=f"User created successfully. Id = {user.id}")


async def update_user(session: AsyncSession, user: User, user_update: UserUpdate) -> HTTPException:
    for name, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, name, value)
    await session.commit()
    return HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f"User update successfully")


async def delete_user():
    pass
