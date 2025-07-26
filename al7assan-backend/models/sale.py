# models/sale.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from models import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    customer_name = Column(String(100))
    amount = Column(Float)
    date = Column(Date)
    product = Column(String(100))
    company_id = Column(Integer, ForeignKey("companies.id"))
