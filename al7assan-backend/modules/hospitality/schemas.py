# modules/hospitality/schemas.py
from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    hotel_id: int
    guest_name: str
    check_in: datetime
    check_out: datetime
    room_type: str 
