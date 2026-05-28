from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..config.database import get_db
from ..models.voucher import Voucher
import random
import string

router = APIRouter()

@router.get("/dashboard")
async def reseller_dashboard(db: AsyncSession = Depends(get_db)):
    # Mock data for reseller
    return {
        "balance": 5000,
        "total_vouchers_sold": 154,
        "commission_earned": 1250,
        "recent_sales": [
            {"date": "2024-05-28", "plan": "ULTRA DAY", "amount": 90},
            {"date": "2024-05-27", "plan": "POWER WEEK", "amount": 500}
        ]
    }

@router.post("/buy-vouchers")
async def buy_vouchers(plan_id: int, quantity: int, db: AsyncSession = Depends(get_db)):
    # In a real app, deduct from reseller balance here
    codes = []
    for _ in range(quantity):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        voucher = Voucher(code=code, plan_name=f"Plan {plan_id}", is_used=False)
        db.add(voucher)
        codes.append(code)
    
    await db.commit()
    return {"message": "Vouchers purchased successfully", "codes": codes}
