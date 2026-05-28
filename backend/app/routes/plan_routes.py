from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..config.database import get_db
from ..models.plan import Plan
from ..schemas.plan_schema import PlanResponse

router = APIRouter()

@router.get("/", response_model=List[PlanResponse])
async def get_plans(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Plan))
    return result.scalars().all()
