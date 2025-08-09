from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from app.models import ride as mride, driver as mdriver, assignment as massign
from app.services.osrm_client import route_duration_minutes

WEIGHTS = dict(w_eta=0.6, w_detour=0.2, w_balance=0.2)
MAX_PICKUP_ETA_MIN = 25

async def assign_pending(db: Session) -> List[massign.Assignment]:
    pending: List[mride.Ride] = db.query(mride.Ride).filter(mride.Ride.status==mride.RideStatus.pending).all()
    drivers: List[mdriver.Driver] = db.query(mdriver.Driver).filter(mdriver.Driver.is_active==True).all()

    results: List[massign.Assignment] = []
    now = datetime.utcnow()
    for ride in pending:
        best = None
        for d in drivers:
            eta_min = await route_duration_minutes((ride.pickup_lat, ride.pickup_lng), (d.home_lat, d.home_lng))
            arrival = now.timestamp()/60 + eta_min
            latest_min = ride.latest.timestamp()/60
            if eta_min > MAX_PICKUP_ETA_MIN or arrival > latest_min:
                continue
            detour = 0.0
            balance = d.km_ytd
            score = WEIGHTS['w_eta']*eta_min + WEIGHTS['w_detour']*detour + WEIGHTS['w_balance']*balance
            if best is None or score < best['score']:
                best = dict(driver=d, eta=eta_min, score=score)
        if best:
            assign = massign.Assignment(
                ride_id=ride.id,
                driver_id=best['driver'].id,
                eta_to_pickup_min=best['eta'],
                score=best['score'],
                assigned_at=datetime.utcnow(),
            )
            ride.status = mride.RideStatus.assigned
            db.add(assign)
            results.append(assign)
    db.commit()
    return results
