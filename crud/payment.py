from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Payment
from core.schemas.ScPayment import PaymentCreate, PaymentUpdate


async def get_all_payments(session: AsyncSession) -> list[Payment]:
    stm = select(Payment).order_by(Payment.id)
    result = await session.execute(stm)
    orders = result.scalars().all()
    return list(orders)


async def get_payment_by_id(session: AsyncSession, payment_id: int) -> Payment | None:
    return await session.get(Payment, payment_id)


async def get_payment_by_user_id(session: AsyncSession, user_id: int) -> list[Payment]:
    stm = select(Payment).where(Payment.user_id == user_id)
    result = await session.execute(stm)
    payments = result.scalars().all()
    return list(payments)


async def create_payment(session: AsyncSession, payment_create: PaymentCreate) -> Payment:
    payment = Payment(**payment_create.model_dump())
    session.add(payment)
    await session.commit()
    # await session.refresh(user)
    return payment

async def update_payment(session: AsyncSession, payment: Payment, payment_update: PaymentUpdate) -> Payment:
    for name, value in payment_update.model_dump(exclude_unset=True).items():
        setattr(payment, name, value)
    await session.commit()
    return payment
