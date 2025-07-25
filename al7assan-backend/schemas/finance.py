# schemas/finance.py
from pydantic import BaseModel
from datetime import date

class InvoiceCreate(BaseModel):
    invoice_number: str
    customer_name: str
    amount: float
    due_date: date
    status: str  # "paid", "unpaid", "overdue"
    company_id: int

class InvoiceResponse(InvoiceCreate):
    id: int

    class Config:
        from_attributes = True
