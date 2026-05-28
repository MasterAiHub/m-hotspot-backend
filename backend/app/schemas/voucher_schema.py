from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VoucherBase(BaseModel):
    plan_id: int

class VoucherCreate(VoucherBase):
    count: int = 1

class VoucherResponse(BaseModel):
    id: int
    code: str
    plan_id: int
    is_used: bool
    used_at: Optional[datetime]
    expires_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True

class VoucherRedeem(BaseModel):
    code: str
    mac_address: str
