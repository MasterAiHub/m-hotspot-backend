from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.voucher import Voucher
from ..models.plan import Plan
from ..utils.generators import generate_voucher_code
from datetime import datetime, timedelta

async def create_vouchers(db: AsyncSession, plan_id: int, creator_id: int, count: int = 1):
    vouchers = []
    for _ in range(count):
        voucher = Voucher(
            code=generate_voucher_code(),
            plan_id=plan_id,
            created_by=creator_id
        )
        db.add(voucher)
        vouchers.append(voucher)
    await db.commit()
    return vouchers

async def redeem_voucher(db: AsyncSession, code: str, mac_address: str):
    result = await db.execute(select(Voucher).where(Voucher.code == code))
    voucher = result.scalars().first()
    
    if not voucher or voucher.is_used:
        return None
    
    # Get plan details to set expiry
    plan_result = await db.execute(select(Plan).where(Plan.id == voucher.plan_id))
    plan = plan_result.scalars().first()
    
    voucher.is_used = True
    voucher.used_at = datetime.utcnow()
    voucher.mac_address = mac_address
    voucher.expires_at = datetime.utcnow() + timedelta(minutes=plan.duration_minutes)
    
    await db.commit()
    await db.refresh(voucher)
    return voucher
