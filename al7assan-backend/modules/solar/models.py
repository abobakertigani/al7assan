# modules/solar/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class SolarSite(Base):
    __tablename__ = "solar_sites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    location = Column(String(200))
    capacity_kw = Column(Float)  # القدرة بالكيلوواط
    company_id = Column(Integer, ForeignKey("companies.id"))

class Inverter(Base):
    __tablename__ = "inverters"
    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("solar_sites.id"))
    serial_number = Column(String(100))
    status = Column(String(50))  # "online", "offline", "warning"
    efficiency = Column(Float)

class EnergyProduction(Base):
    __tablename__ = "energy_production"
    id = Column(Integer, primary_key=True, index=True)
    inverter_id = Column(Integer, ForeignKey("inverters.id"))
    energy_kwh = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    irradiance = Column(Float)  # شدة الإشعاع الشمسي
