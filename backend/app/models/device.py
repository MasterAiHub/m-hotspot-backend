from sqlalchemy import Column, Integer, String, ForeignKey
from ..config.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    device_name = Column(String, nullable=False)
    mac_address = Column(String, nullable=True)
