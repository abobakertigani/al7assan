# modules/education/schemas.py
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    teacher: str
    schedule: str
    company_id: int

class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    score: float
    exam_type: str
