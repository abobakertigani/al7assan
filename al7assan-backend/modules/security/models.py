# modules/security/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from models import Base
from datetime import datetime

class SecurityIncident(Base):
    __tablename__ = "security_incidents"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(100))  # "intrusion", "cyber", "theft"
    location = Column(String(200))
    description = Column(Text)
    reported_by = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    resolved: bool = Column(Boolean, default=False)
    company_id = Column(Integer, ForeignKey("companies.id"))

class SurveillanceLog(Base):
    __tablename__ = "surveillance_logs"
    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(String(50))
    event_type = Column(String(100))  # "motion", "face_recognition"
    timestamp = Column(DateTime, default=datetime.utcnow)
    image_url = Column(String(500))
