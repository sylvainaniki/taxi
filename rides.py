from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.ride import RideCreate, RideOut
from app.models.ride import Ride

router = APIRouter(prefix="/rides", tags=["rides"])

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post("/", response_model=RideOut)
def create_ride(ride: RideCreate, db: Session = Depends(get_db)):
  r = Ride(**ride.dict())
  db.add(r)
  db.commit()
  db.refresh(r)
  return r

@router.get("/", response_model=list[RideOut])
def list_rides(db: Session = Depends(get_db)):
  return db.query(Ride).all()
