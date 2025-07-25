# models/employee.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    position = Column(String(100))
    salary = Column(Float)
    hire_date = Column(Date)
    company_id = Column(Integer, ForeignKey("companies.id"))
