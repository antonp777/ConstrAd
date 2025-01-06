from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.models import db_helper
from core.schemas.ScTask import TaskRead, TaskCreate, TaskUpdate
from crud import task as crud_task

router = APIRouter(
    prefix=settings.api.v1.tasks,
    tags=["Task"]
)
@router.get("", response_model=list[TaskRead])
async def get_tasks(session: AsyncSession = Depends(db_helper.session_getter)):
    return await crud_task.get_all_tasks(session=session)

@router.get("/{task_id}", response_model=TaskRead)
async def get_task_by_id(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_id: int):
    task = await crud_task.get_task_by_id(session=session, task_id=task_id)
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@router.post("", response_model=TaskRead)
async def create_task(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_create: TaskCreate):
    return await crud_task.create_task(session=session, task_create=task_create)


@router.patch("/{task_id}", response_model=TaskUpdate)
async def update_task(session: Annotated[AsyncSession, Depends(db_helper.session_getter)], task_id: int, task_update: TaskUpdate):
    task = await crud_task.get_task_by_id(session=session, task_id=task_id)
    if task:
        return await crud_task.update_task(session=session, task=task, task_update=task_update)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
