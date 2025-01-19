from fastapi import APIRouter

from core.config import settings
from .user import router as user_router
from .order import router as order_router
from .task import router as task_router
from .payment import router as payment_router
from .userService import router as user_service_router
from .auth import router as auth_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)
router.include_router(
    auth_router
)

router.include_router(
    user_router
)
router.include_router(
    order_router
)
router.include_router(
    task_router
)
router.include_router(
    payment_router
)
router.include_router(
    user_service_router
)


