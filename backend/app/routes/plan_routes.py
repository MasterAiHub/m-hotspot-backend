from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..config.database import get_db
from ..models.user import User
from ..models.transaction import Transaction
from typing import List

router = APIRouter()

PLANS = [
    {"id": 1, "name": "QUICK CONNECT", "duration": "30 min", "speed": "2 Mbps", "price": 10},
    {"id": 2, "name": "TURBO HOUR", "duration": "1 hour", "speed": "3 Mbps", "price": 22},
    {"id": 3, "name": "FLEX PASS", "duration": "6 hours", "speed": "4 Mbps", "price": 42},
    {"id": 4, "name": "ULTRA DAY", "duration": "24 hours", "speed": "5 Mbps", "price": 90, "tag": "MOST POPULAR VALUE"},
    {"id": 5, "name": "POWER WEEK", "duration": "7 days", "speed": "7 Mbps", "price": 500, "tag": "Free Midnight Unlimited Bonus"},
    {"id": 6, "name": "UNLIMITED MAX", "duration": "30 days", "speed": "10 Mbps", "price": 1450, "tag": "VIP Priority Peak-Hour Speed"},
]

@router.get("/")
async def get_plans():
    return PLANS

@router.post("/select/{plan_id}")
async def select_plan(plan_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    # Find the plan
    plan = next((p for p in PLANS if p["id"] == plan_id), None)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    # Update user purchase count for loyalty
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.purchase_count += 1
    
    # Record transaction (no payment, just log)
    new_transaction = Transaction(
        user_id=user_id,
        amount=plan["price"],
        payment_method="Direct Selection",
        status="completed"
    )
    db.add(new_transaction)
    
    await db.commit()
    
    return {
        "message": f"Plan '{plan['name']}' added to your session.",
        "details": f"You'll be connected for {plan['duration']} at {plan['speed']}.",
        "purchase_count": user.purchase_count
    }
