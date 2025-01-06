from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from core.schemas.ScUser import UserCreate


async def get_all_users(session: AsyncSession) -> list[User]:
    stm = select(User).order_by(User.id)
    result = await session.execute(stm)
    users = result.scalars().all()
    return list(users)

async def get_user_by_id(session: AsyncSession, user_id: int) -> User|None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user


async def delete_user():
    pass
