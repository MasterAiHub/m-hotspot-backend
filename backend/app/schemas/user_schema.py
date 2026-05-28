from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    role: str
    is_active: bool = True

class UserResponse(UserBase):
    id: int
    created_at: datetime
    balance: int

    class Config:
        from_attributes = True
