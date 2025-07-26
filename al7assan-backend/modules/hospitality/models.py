# modules/hospitality/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    location = Column(String(200))
    stars = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    guest_name = Column(String(100))
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    room_type = Column(String(50))
    status = Column(String(50))  # "confirmed", "checked_in", "completed"

class GuestFeedback(Base):
    __tablename__ = "guest_feedback"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    rating: int = Column(Integer)  # 1-5
    comments = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
