from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, index=True)
    plate = Column(String, unique=True)
    kind = Column(String)
    capacity = Column(Integer, default=4)
    is_active = Column(Boolean, default=True)
