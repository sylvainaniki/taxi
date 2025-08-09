from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base import Base

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    home_lat = Column(Float)
    home_lng = Column(Float)
    is_active = Column(Boolean, default=True)
    km_ytd = Column(Float, default=0.0)
