from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserResponse(BaseModel):
    id: int
    phone_number: str
    full_name: str
    purchase_count: int
    created_at: datetime

    class Config:
        from_attributes = True
