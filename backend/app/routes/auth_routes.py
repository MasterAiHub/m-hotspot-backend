from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timedelta
import random
from ..config.database import get_db
from ..config.security import create_access_token
from ..schemas.auth_schema import PhoneRequest, OTPVerify, Token
from ..models.user import User

router = APIRouter()

@router.post("/send-otp")
async def send_otp(request: PhoneRequest, db: AsyncSession = Depends(get_db)):
    # Generate a random 6-digit OTP
    otp = str(random.randint(100000, 999999))
    expiry = datetime.utcnow() + timedelta(minutes=5)
    
    # Check if user exists
    result = await db.execute(select(User).where(User.phone_number == request.phone_number))
    user = result.scalars().first()
    
    if not user:
        # Auto-create user
        user = User(phone_number=request.phone_number)
        db.add(user)
    
    user.otp_code = otp
    user.otp_expiry = expiry
    await db.commit()
    
    # In production, send SMS here. For now, return it in the response for testing.
    return {"message": "OTP sent successfully", "otp_debug": otp}

@router.post("/verify-otp", response_model=Token)
async def verify_otp(request: OTPVerify, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.phone_number == request.phone_number))
    user = result.scalars().first()
    
    if not user or user.otp_code != request.otp_code:
        raise HTTPException(status_code=400, detail="Invalid OTP code")
    
    if datetime.utcnow() > user.otp_expiry:
        raise HTTPException(status_code=400, detail="OTP code expired")
    
    # Clear OTP after verification
    user.otp_code = None
    user.otp_expiry = None
    await db.commit()
    
    access_token = create_access_token(subject=user.id)
    return {"access_token": access_token, "token_type": "bearer"}
