# schemas/hr.py
from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: str
    position: str
    salary: float
    hire_date: date
    company_id: int

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True  # بدلاً من orm_mode في إصدارات حديثة من Pydantic
