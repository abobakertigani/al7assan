# modules/hse/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from models import Base
from datetime import datetime

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"
    id = Column(Integer, primary_key=True, index=True)
    hazard = Column(String(100))  # "fire", "electric", "fall"
    likelihood = Column(String(20))  # "low", "medium", "high"
    impact = Column(String(20))
    control_measures = Column(Text)
    company_id = Column(Integer, ForeignKey("companies.id"))

class SafetyInspection(Base):
    __tablename__ = "safety_inspections"
    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(100))
    inspector = Column(String(100))
    findings = Column(Text)
    corrected: bool = Column(Boolean, default=False)
    date = Column(DateTime, default=datetime.utcnow)

class IncidentReport(Base):
    __tablename__ = "incident_reports"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(100))  # "injury", "near_miss"
    description = Column(Text)
    reported_by = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    company_id = Column(Integer, ForeignKey("companies.id"))
