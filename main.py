from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from adminPanel.auth_backend import authentication_backend
from api import router as api_router
from core.config import settings
from core.models import db_helper

from adminPanel.UserViews import UserViews
from adminPanel.PaymentViews import PaymentViews
from adminPanel.UserServiceViews import UserServiceViews
from adminPanel.OrderViews import OrderViews
from adminPanel.TaskViews import TaskViews


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan
)
main_app.include_router(api_router)


admin = Admin(main_app, db_helper.engine, authentication_backend=authentication_backend)

admin.add_view(TaskViews)
admin.add_view(UserViews)
admin.add_view(PaymentViews)
admin.add_view(OrderViews)
admin.add_view(UserServiceViews)


if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
