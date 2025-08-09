from sqlalchemy import Column, Integer, Float, DateTime
from app.db.base import Base

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    ride_id = Column(Integer, index=True, nullable=False)
    driver_id = Column(Integer, index=True, nullable=False)
    eta_to_pickup_min = Column(Float)
    detour_km = Column(Float, default=0.0)
    score = Column(Float)
    assigned_at = Column(DateTime)
