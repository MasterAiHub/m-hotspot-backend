from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.sql import func
from ..config.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    voucher_id = Column(Integer, ForeignKey("vouchers.id"))
    router_id = Column(Integer, ForeignKey("routers.id"))
    mac_address = Column(String, nullable=False)
    ip_address = Column(String)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    bytes_in = Column(Float, default=0)
    bytes_out = Column(Float, default=0)
    is_active = Column(Boolean, default=True)
