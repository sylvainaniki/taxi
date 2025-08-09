from pydantic import BaseModel
from datetime import datetime

class RideCreate(BaseModel):
    reference: str
    pickup_lat: float
    pickup_lng: float
    drop_lat: float
    drop_lng: float
    earliest: datetime
    latest: datetime
    pax: int = 1
    vehicle_kind: str = "berline"
    priority: int = 0

class RideOut(RideCreate):
    id: int
    status: str
    class Config:
        from_attributes = True
