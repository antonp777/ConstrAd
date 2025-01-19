from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import Task
from core.schemas.ScTask import TaskCreate, TaskUpdate
from tg.helper_tg import send_task_to_chanel


async def get_all_tasks(session: AsyncSession) -> list[Task]:
    stm = select(Task).options(joinedload(Task.orders), selectinload(Task.users)).order_by(Task.id)
    result = await session.execute(stm)
    tasks = result.unique().scalars().all()
    return list(tasks)


async def get_task_by_id(session: AsyncSession, task_id: int) -> Task | None:
    stm = select(Task).where(Task.id == task_id).options(joinedload(Task.orders))
    result = await session.execute(stm)
    try:
        return result.unique().scalars().one()
    except SQLAlchemyError:
        return None


async def create_task(session: AsyncSession, task_create: TaskCreate) -> Task:
    task = Task(**task_create.model_dump())
    session.add(task)
    await session.commit()

    # Отправка задания в канал
    if task_create.is_active:
        await send_task_to_chanel(city=task_create.city,
                                  district=task_create.district,
                                  work=task_create.work,
                                  price_work=task_create.price_work,
                                  person=task_create.person,
                                  fee=task_create.fee
                                  )
    # await session.refresh(user)
    return task


async def update_task(session: AsyncSession, task: Task, task_update: TaskUpdate) -> Task:
    for name, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, name, value)
    await session.commit()

    # Отправка задания в канал
    if task.is_active and task.person > 0:
        await send_task_to_chanel(city=task.city,
                                  district=task.district,
                                  work=task.work,
                                  price_work=task.price_work,
                                  person=task.person,
                                  fee=task.fee
                                  )
    return task


async def delete_user():
    pass
