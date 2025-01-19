from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.current_user import get_current_active_auth_user
from core import settings
from core.models import db_helper
from core.schemas.ScOrder import OrderRead, OrderCreate, OrderUpdate
from crud import order as crud_order

router = APIRouter(
    prefix=settings.api.v1.orders,
    tags=["Order"]
)


@router.get("",
            response_model=list[OrderRead])
async def get_orders(token_key: Annotated[bool, Depends(get_current_active_auth_user)],
                     session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    if token_key:
        return await crud_order.get_all_orders(session=session)


@router.get("/{order_id}",
            response_model=OrderRead)
async def get_order_by_id(token_key: Annotated[bool, Depends(get_current_active_auth_user)],
                          session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                          order_id: int):
    if token_key:
        order = await crud_order.get_order_by_id(session=session,
                                                 order_id=order_id)
        if order:
            return order
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")


@router.get("/byUser/{user_id}",
            response_model=list[OrderRead])
async def get_order_by_user_id(token_key: Annotated[bool, Depends(get_current_active_auth_user)],
                               session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                               user_id: int):
    if token_key:
        orders = await crud_order.get_orders_by_user_id(session=session,
                                                        user_id=user_id)
        if orders:
            return orders
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Orders not found")


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_description="Order created successfully")
async def create_order(token_key: Annotated[bool, Depends(get_current_active_auth_user)],
                       session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                       order_create: OrderCreate):
    if token_key:
        return await crud_order.create_order(session=session,
                                             order_create=order_create)


@router.patch("/{order_id}",
              status_code=status.HTTP_202_ACCEPTED,
              response_description="Order update successfully")
async def update_order(token_key: Annotated[bool, Depends(get_current_active_auth_user)],
                       session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                       order_id: int,
                       order_update: OrderUpdate):
    if token_key:
        order = await crud_order.get_order_by_id(session=session,
                                                 order_id=order_id)
        if order:
            return await crud_order.update_order(session=session,
                                                 order=order,
                                                 order_update=order_update)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
