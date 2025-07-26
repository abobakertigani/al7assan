# modules/logistics/schemas.py
from pydantic import BaseModel
from datetime import datetime

class DeliveryCreate(BaseModel):
    vehicle_id: int
    driver: str
    origin: str
    destination: str
    estimated_time: datetime 
