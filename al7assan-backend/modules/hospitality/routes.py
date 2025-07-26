# modules/hospitality/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import Booking
from schemas import BookingCreate

router = APIRouter(prefix="/hospitality", tags=["Hospitality"])

@router.post("/bookings")
def create_booking( BookingCreate, db: Session = Depends(database.get_db)):
    new_booking = Booking(**data.dict(), status="confirmed")
    db.add(new_booking)
    db.commit()
    return {"message": "تم الحجز بنجاح"}

@router.get("/occupancy/{hotel_id}")
def get_occupancy(hotel_id: int, db: Session = Depends(database.get_db)):
    total_bookings = db.query(Booking).filter(Booking.hotel_id == hotel_id).count()
    active = db.query(Booking).filter(
        Booking.hotel_id == hotel_id,
        Booking.check_in <= datetime.utcnow(),
        Booking.check_out >= datetime.utcnow()
    ).count()
    occupancy = (active / total_bookings * 100) if total_bookings > 0 else 0
    return {"occupancy_rate": f"{occupancy:.1f}%"}
