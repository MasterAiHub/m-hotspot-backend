from pydantic import BaseModel
from typing import Optional

class PhoneRequest(BaseModel):
    phone_number: str

class OTPVerify(BaseModel):
    phone_number: str
    otp_code: str

class Token(BaseModel):
    access_token: str
    token_type: str
