# models/company.py
from sqlalchemy import Column, Integer, String, Text
from models import Base  # نستورد Base من models/__init__.py

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(100))
    phone = Column(String(20))
    address = Column(Text)
    created_at = Column(String(20))  # يمكن استخدام DateTime لاحقًا
