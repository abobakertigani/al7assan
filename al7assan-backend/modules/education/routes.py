# modules/education/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import Course, Student, Grade
from schemas import CourseCreate, GradeCreate

router = APIRouter(prefix="/education", tags=["Education"])

@router.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(database.get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.post("/grades")
def add_grade( GradeCreate, db: Session = Depends(database.get_db)):
    new_grade = Grade(**data.dict())
    db.add(new_grade)
    db.commit()
    return {"message": "تم إضافة الدرجة"}

@router.get("/performance/{student_id}")
def get_student_performance(student_id: int, db: Session = Depends(database.get_db)):
    grades = db.query(Grade).filter(Grade.student_id == student_id).all()
    avg = sum(g.score for g in grades) / len(grades) if grades else 0
    return {"student_id": student_id, "average": round(avg, 2), "total": len(grades)}
