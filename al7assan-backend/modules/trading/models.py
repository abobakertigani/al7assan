# modules/trading/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(50))  # "pharma", "solar", "electronics"
    cost_price = Column(Float)
    selling_price = Column(Float)
    company_id = Column(Integer, ForeignKey("companies.id"))

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    location = Column(String(100))
    last_updated = Column(DateTime, default=datetime.utcnow)

class SalesOrder(Base):
    __tablename__ = "sales_orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer = Column(String(100))
    quantity = Column(Integer)
    total_amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
