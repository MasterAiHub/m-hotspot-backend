from pydantic import BaseModel
from typing import Optional

class PlanBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    duration_minutes: int
    speed_limit_mbps: int

class PlanResponse(PlanBase):
    id: int

    class Config:
        from_attributes = True
