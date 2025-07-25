from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from models import Base
from datetime import datetime

class ProductionRecord(Base):
    __tablename__ = "production_records"
    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String(100))
    operation = Column(String(100))  # production, maintenance, failure
    output_count = Column(Integer, default=0)
    defect_count = Column(Integer, default=0)
    failure_type = Column(String(100), nullable=True)
    notes = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    company_id = Column(Integer, ForeignKey("companies.id"))
