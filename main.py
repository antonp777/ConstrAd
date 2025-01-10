from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from api import router as api_router
from core.config import settings
from core.models import db_helper

from adminPanel.UserAdminViews import UserAdminViews
from adminPanel.PaymentAdminViews import PaymentAdminViews

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


admin = Admin(main_app, db_helper.engine)

admin.add_view(UserAdminViews)
admin.add_view(PaymentAdminViews)


if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
