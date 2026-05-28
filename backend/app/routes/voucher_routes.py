from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..config.database import get_db
from ..schemas.voucher_schema import VoucherCreate, VoucherResponse, VoucherRedeem
from ..services.voucher_service import create_vouchers, redeem_voucher

router = APIRouter()

@router.post("/generate", response_model=List[VoucherResponse])
async def generate_vouchers_route(
    voucher_in: VoucherCreate, 
    db: AsyncSession = Depends(get_db)
):
    # In a real app, we'd get current_user from a dependency
    # For now, using a dummy creator_id=1 (Admin)
    vouchers = await create_vouchers(db, voucher_in.plan_id, 1, voucher_in.count)
    return vouchers

@router.post("/redeem", response_model=VoucherResponse)
async def redeem_voucher_route(
    redeem_in: VoucherRedeem,
    db: AsyncSession = Depends(get_db)
):
    voucher = await redeem_voucher(db, redeem_in.code, redeem_in.mac_address)
    if not voucher:
        raise HTTPException(status_code=400, detail="Invalid or already used voucher")
    return voucher
