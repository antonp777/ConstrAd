from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Order
from core.schemas.ScOrder import OrderCreate


async def get_all_orders(session: AsyncSession) -> list[Order]:
    stm = select(Order).order_by(Order.id)
    result = await session.execute(stm)
    orders = result.scalars().all()
    return list(orders)


async def get_order_by_id(session: AsyncSession, order_id: int) -> Order | None:
    return await session.get(Order, order_id)


async def get_orders_by_user_id(session: AsyncSession, user_id: int) -> list[Order]:
    stm = select(Order).where(Order.user_id == user_id)
    result = await session.execute(stm)
    orders = result.scalars().all()
    return list(orders)


async def create_order(session: AsyncSession, order_create: OrderCreate) -> Order:
    order = Order(**order_create.model_dump())
    session.add(order)
    await session.commit()
    # await session.refresh(user)
    return order


async def delete_user():
    pass
