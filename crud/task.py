from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import Task
from core.schemas.ScTask import TaskCreate, TaskUpdate


async def get_all_tasks(session: AsyncSession) -> list[Task]:
    stm = select(Task).options(joinedload(Task.orders), selectinload(Task.users)).order_by(Task.id)
    result = await session.execute(stm)
    tasks = result.unique().scalars().all()
    return list(tasks)

async def get_task_by_id(session: AsyncSession, task_id: int) -> Task|None:
    stm = select(Task).where(Task.id == task_id).options(joinedload(Task.orders))
    result = await session.execute(stm)
    return result.scalars().unique().one()


async def create_task(session: AsyncSession, task_create: TaskCreate) -> Task:
    task = Task(**task_create.model_dump())
    session.add(task)
    await session.commit()
    # await session.refresh(user)
    return task

async def update_task(session: AsyncSession, task: Task, task_update: TaskUpdate) -> Task:
    for name, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, name, value)
    await session.commit()
    return task

async def delete_user():
    pass
