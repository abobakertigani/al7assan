# models/inventory.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    current_stock = Column(Float, default=0)
    min_stock = Column(Float, default=10)  # الحد الأدنى
    supplier = Column(String(100))
    company_id = Column(Integer, ForeignKey("companies.id"))
