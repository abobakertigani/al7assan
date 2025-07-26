# modules/manufacturing/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LineCreate(BaseModel):
    name: str
    company_id: int

class OrderCreate(BaseModel):
    line_id: int
    product_name: str
    planned_qty: int
    start_date: datetime
    end_date: datetime

class QualityCreate(BaseModel):
    order_id: int
    passed: bool
    defects_count: int
    inspector: str
