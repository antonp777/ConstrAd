from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import User
from core.schemas.ScUser import UserCreate, UserUpdate


async def get_all_users(session: AsyncSession) -> list[User]:
    stm = select(User).options(joinedload(User.payments), joinedload(User.orders)).order_by(User.id)
    result = await session.execute(stm)
    users = result.unique().scalars().all()
    return list(users)

async def get_user_by_id(session: AsyncSession, user_id: int) -> User|None:
    stm = select(User).where(User.id == user_id).options(joinedload(User.payments), joinedload(User.orders))
    result = await session.execute(stm)
    return result.unique().scalars().one()


async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user

async def update_user(session: AsyncSession, user: User, user_update: UserUpdate) -> User:
    for name, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user():
    pass
