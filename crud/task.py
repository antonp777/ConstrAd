from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Task
from core.schemas.ScTask import TaskCreate


async def get_all_tasks(session: AsyncSession) -> list[Task]:
    stm = select(Task).order_by(Task.id)
    result = await session.execute(stm)
    tasks = result.scalars().all()
    return list(tasks)

async def get_task_by_id(session: AsyncSession, task_id: int) -> Task|None:
    return await session.get(Task, task_id)


async def create_task(session: AsyncSession, task_create: TaskCreate) -> Task:
    task = Task(**task_create.model_dump())
    session.add(task)
    await session.commit()
    # await session.refresh(user)
    return task


async def delete_user():
    pass
