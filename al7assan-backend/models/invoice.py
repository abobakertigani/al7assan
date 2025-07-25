# models/invoice.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from models import Base 

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True)
    customer_name = Column(String(100))
    amount = Column(Float)
    due_date = Column(Date)
    status = Column(String(20))  # paid, unpaid, overdue
    company_id = Column(Integer, ForeignKey("companies.id"))
