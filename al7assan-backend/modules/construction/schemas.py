# modules/construction/schemas.py
from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    location: str
    budget: float
    start_date: datetime
    end_date: datetime
    company_id: int

class TaskCreate(BaseModel):
    project_id: int
    name: str
    assigned_to: str
    due_date: datetime
