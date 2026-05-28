from sqlalchemy import Column, Integer, String, Float
from ..config.database import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    speed_limit_mbps = Column(Integer, nullable=False)
    data_limit_gb = Column(Integer, nullable=True) # Optional data cap
