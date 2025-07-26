# modules/logistics/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String(20), unique=True)
    type = Column(String(50))  # "truck", "van"
    status = Column(String(50))  # "available", "in_transit", "maintenance"
    last_maintenance = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

class Delivery(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver = Column(String(100))
    origin = Column(String(200))
    destination = Column(String(200))
    status = Column(String(50))  # "assigned", "en_route", "delivered"
    estimated_time = Column(DateTime)
    timestamp = Column(DateTime, default=datetime.utcnow) 
