# modules/hse/schemas.py
from pydantic import BaseModel
from datetime import datetime

class InspectionCreate(BaseModel):
    area: str
    inspector: str
    findings: str

class IncidentCreate(BaseModel):
    type: str
    description: str
    reported_by: str
    company_id: int
