from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from ..config.database import Base

class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=True)
    plan_name = Column(String, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    is_used = Column(Boolean, default=False)
    used_at = Column(DateTime(timezone=True), nullable=True)
    used_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    mac_address = Column(String, nullable=True)
