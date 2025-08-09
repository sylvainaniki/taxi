from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models import user as muser, driver as mdriver, ride as mride
from app.core.security import hash_password

def run():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    if not db.query(muser.User).first():
        admin = muser.User(email="admin@aquiles.taxi", hashed_password=hash_password("admin"), role=muser.UserRole.admin)
        dispatch = muser.User(email="dispatch@aquiles.taxi", hashed_password=hash_password("dispatch"), role=muser.UserRole.dispatcher)
        db.add_all([admin, dispatch])

    if not db.query(mdriver.Driver).first():
        drivers = [
            mdriver.Driver(name="Anthony", phone="0600000001", home_lat=43.6045, home_lng=1.4442),
            mdriver.Driver(name="Chris", phone="0600000002", home_lat=43.61, home_lng=1.43),
            mdriver.Driver(name="Nina", phone="0600000003", home_lat=43.59, home_lng=1.45),
        ]
        db.add_all(drivers)

    if not db.query(mride.Ride).first():
        now = datetime.utcnow()
        rides = [
            mride.Ride(reference="C-1001", pickup_lat=43.606, pickup_lng=1.443, drop_lat=43.63, drop_lng=1.45,
                    earliest=now + timedelta(minutes=20), latest=now + timedelta(minutes=60), pax=1, priority=1),
            mride.Ride(reference="C-1002", pickup_lat=43.61, pickup_lng=1.46, drop_lat=43.64, drop_lng=1.42,
                    earliest=now + timedelta(minutes=10), latest=now + timedelta(minutes=40), pax=2),
        ]
        db.add_all(rides)

    db.commit()
    db.close()

if __name__ == "__main__":
    run()
