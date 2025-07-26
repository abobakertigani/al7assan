# modules/aquaculture/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from models import Base
from datetime import datetime

class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))  # "poultry", "fish", "shrimp"
    location = Column(String(200))
    company_id = Column(Integer, ForeignKey("companies.id"))

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    species = Column(String(100))  # "broiler", "layer", "tilapia"
    count = Column(Integer)
    start_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50))  # "active", "harvested", "lost"

class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    ammonia = Column(Float)
    ph = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class FeedingLog(Base):
    __tablename__ = "feeding_logs"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    feed_type = Column(String(100))
    amount_kg = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)

class HealthLog(Base):
    __tablename__ = "health_logs"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    disease = Column(String(100))
    symptoms = Column(String(500))
    treated = Column(Boolean, default=False)
    treatment = Column(String(500))
    date = Column(DateTime, default=datetime.utcnow)
