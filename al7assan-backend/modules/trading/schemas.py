# modules/trading/schemas.py
from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: int
    customer: str
    quantity: int
    company_id: int 
