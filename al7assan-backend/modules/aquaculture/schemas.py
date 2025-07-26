# modules/aquaculture/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FarmCreate(BaseModel):
    name: str
    type: str
    location: str
    company_id: int

class BatchCreate(BaseModel):
    farm_id: int
    species: str
    count: int

class SensorDataCreate(BaseModel):
    batch_id: int
    temperature: float
    humidity: float
    ammonia: Optional[float] = None
    ph: Optional[float] = None

class FeedingLogCreate(BaseModel):
    batch_id: int
    feed_type: str
    amount_kg: float

class HealthLogCreate(BaseModel):
    batch_id: int
    disease: str
    symptoms: str
    treatment: Optional[str] = None
