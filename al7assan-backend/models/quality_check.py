# models/quality_check.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models import Base

class QualityCheck(Base):
    __tablename__ = "quality_checks"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    defective_count = Column(Integer, default=0)
    defect_type = Column(String(100))
    inspector = Column(String(100))
    check_date = Column(Date)
    notes = Column(String(255))
    company_id = Column(Integer, ForeignKey("companies.id"))
