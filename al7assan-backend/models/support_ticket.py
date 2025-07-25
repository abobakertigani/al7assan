from sqlalchemy import Column, Integer, String, Text, ForeignKey
from models import Base

class SupportTicket(Base):
    __tablename__ = "support_tickets"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    customer_email = Column(String(100))
    description = Column(Text)
    category = Column(String(50))  # finance, logistics, technical, general
    status = Column(String(20), default="open")
    company_id = Column(Integer, ForeignKey("companies.id"))
