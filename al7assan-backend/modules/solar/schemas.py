# modules/solar/schemas.py
from pydantic import BaseModel
from datetime import datetime

class SiteCreate(BaseModel):
    name: str
    location: str
    capacity_kw: float
    company_id: int

class ProductionCreate(BaseModel):
    inverter_id: int
    energy_kwh: float
    irradiance: float
