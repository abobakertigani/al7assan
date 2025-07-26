# modules/construction/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    location = Column(String(200))
    budget = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String(100))
    assigned_to = Column(String(100))
    status = Column(String(50))  # "pending", "in_progress", "completed"
    due_date = Column(DateTime)

class SiteVisit(Base):
    __tablename__ = "site_visits"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    inspector = Column(String(100))
    findings = Column(String(500))
    timestamp = Column(DateTime, default=datetime.utcnow)
