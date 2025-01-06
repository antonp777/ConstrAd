from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.models import db_helper
from core.schemas.ScPayment import PaymentRead, PaymentCreate, PaymentUpdate
from crud import payment as crud_payment

router = APIRouter(
    prefix=settings.api.v1.payments,
    tags=["Payment"]
)
@router.get("", response_model=list[PaymentRead])
async def get_payments(session: AsyncSession = Depends(db_helper.session_getter)):
    return await crud_payment.get_all_payments(session=session)

@router.get("/{payment_id}", response_model=PaymentRead)
async def get_payment_by_id(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                            payment_id: int):
    payment = await crud_payment.get_payment_by_id(session=session, payment_id=payment_id)
    if payment:
        return payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

@router.get("/byUser/{user_id}", response_model=PaymentRead)
async def get_payment_by_user_id(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                                 user_id: int):
    payments = await crud_payment.get_payment_by_user_id(session=session, user_id=user_id)
    if payments:
        return payments
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payments not found")

@router.post("", response_model=PaymentCreate)
async def create_payment(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                         payment_create: PaymentCreate):
    return await crud_payment.create_payment(session=session, payment_create=payment_create)

@router.patch("/{payment_id}", response_model=PaymentRead)
async def update_payment(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                        payment_id: int,
                        payment_update: PaymentUpdate):
    payment = await crud_payment.get_payment_by_id(session=session, payment_id=payment_id)
    if payment:
        return await crud_payment.update_payment(session=session, payment=payment, payment_update=payment_update)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")