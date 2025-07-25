from pydantic import BaseModel
from datetime import date

class InventoryCreate(BaseModel):
    product_name: str
    current_stock: float
    min_stock: float
    supplier: str
    company_id: int

class InventoryResponse(InventoryCreate):
    id: int
    class Config:
        from_attributes = True
