# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="employee")
    company_id = Column(Integer, ForeignKey("companies.id"))  # ✅ الآن الجدول موجود
    is_active = Column(Boolean, default=True)
