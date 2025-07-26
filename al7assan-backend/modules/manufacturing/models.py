# modules/manufacturing/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class ProductionLine(Base):
    __tablename__ = "production_lines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    status = Column(String(50))  # "running", "stopped", "maintenance"
    efficiency = Column(Float, default=0.0)
    company_id = Column(Integer, ForeignKey("companies.id"))

class ProductionOrder(Base):
    __tablename__ = "production_orders"
    id = Column(Integer, primary_key=True, index=True)
    line_id = Column(Integer, ForeignKey("production_lines.id"))
    product_name = Column(String(100))
    planned_qty = Column(Integer)
    produced_qty = Column(Integer, default=0)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

class QualityCheck(Base):
    __tablename__ = "quality_checks"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("production_orders.id"))
    passed: bool = Column(Boolean, default=True)
    defects_count = Column(Integer, default=0)
    inspector = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)

class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"
    id = Column(Integer, primary_key=True, index=True)
    line_id = Column(Integer, ForeignKey("production_lines.id"))
    issue = Column(String(200))
    action_taken = Column(String(500))
    scheduled_by = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
