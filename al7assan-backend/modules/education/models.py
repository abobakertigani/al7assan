# modules/education/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    teacher = Column(String(100))
    schedule = Column(String(100))
    company_id = Column(Integer, ForeignKey("companies.id"))  # school as company

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    class_name = Column(String(50))
    course_id = Column(Integer, ForeignKey("courses.id"))

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    score = Column(Float)
    exam_type = Column(String(50))  # "midterm", "final"
    date = Column(DateTime, default=datetime.utcnow)
