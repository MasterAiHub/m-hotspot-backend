from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from ..config.database import get_db
from ..models.user import User
from ..models.transaction import Transaction
from ..models.voucher import Voucher
from typing import List
import random
import string

router = APIRouter()

@router.get("/stats")
async def get_admin_stats(db: AsyncSession = Depends(get_db)):
    # Total Users
    user_count = await db.execute(select(func.count(User.id)))
    total_users = user_count.scalar()
    
    # Total Revenue
    revenue_result = await db.execute(select(func.sum(Transaction.amount)))
    total_revenue = revenue_result.scalar() or 0
    
    # Active Sessions (Mock for now)
    active_sessions = random.randint(45, 120)
    
    # Recent Transactions
    trans_result = await db.execute(select(Transaction).order_by(Transaction.created_at.desc()).limit(5))
    recent_transactions = trans_result.scalars().all()
    
    return {
        "total_users": total_users,
        "total_revenue": total_revenue,
        "active_sessions": active_sessions,
        "network_load": f"{random.randint(20, 85)}%",
        "recent_transactions": recent_transactions
    }

@router.post("/vouchers/generate")
async def generate_vouchers(count: int, plan_name: str, db: AsyncSession = Depends(get_db)):
    new_vouchers = []
    for _ in range(count):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        voucher = Voucher(code=code, plan_name=plan_name, is_used=False)
        db.add(voucher)
        new_vouchers.append(code)
    
    await db.commit()
    return {"message": f"Generated {count} vouchers", "codes": new_vouchers}

@router.get("/vouchers")
async def list_vouchers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Voucher).order_by(Voucher.created_at.desc()))
    return result.scalars().all()
