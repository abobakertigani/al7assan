# modules/security/schemas.py
from pydantic import BaseModel

class IncidentCreate(BaseModel):
    type: str
    location: str
    description: str
    reported_by: str
    company_id: int 
