from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.assigner import assign_pending

router = APIRouter(prefix="/assignments", tags=["assignments"])

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post("/run")
async def run_assignment(db: Session = Depends(get_db)):
  res = await assign_pending(db)
  return {"assigned": len(res)}
