import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.models import User, db_helper


async def get_user_by_id_with_tasks(session: AsyncSession, user_id: int) -> User:
    stm = select(User).where(User.id == user_id).options(selectinload(User.tasks))
    user = await session.scalar(stm)
    return user

async def get_user_by_id_with_task(session: AsyncSession, user_id: int):
    user = await get_user_by_id_with_tasks(session, user_id)
    print(user.id, "tasks:")
    for task in user.tasks:
        print("-", task.id)
async def demo(session: AsyncSession):
    await get_user_by_id_with_task(session, 1)

async def main():
    async with db_helper.session_factory() as session:
        await demo(session)

if __name__ == "__main__":
    asyncio.run(main())
