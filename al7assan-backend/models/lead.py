# models/lead.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20))
    field = Column(String(50))  # مجال العمل
    package = Column(String(20))  # باقة مطلوبة
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
