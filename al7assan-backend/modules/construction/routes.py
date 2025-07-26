# modules/construction/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import Project, Task
from schemas import ProjectCreate, TaskCreate

router = APIRouter(prefix="/construction", tags=["Construction"])

@router.post("/projects")
def create_project(project: ProjectCreate, db: Session = Depends(database.get_db)):
    new_project = Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    new_task = Task(**task.dict(), status="pending")
    db.add(new_task)
    db.commit()
    return {"message": "تم إنشاء المهمة"}

@router.get("/progress/{project_id}")
def get_progress(project_id: int, db: Session = Depends(database.get_db)):
    tasks = db.query(Task).filter(Task.project_id == project_id).all()
    total = len(tasks)
    completed = len([t for t in tasks if t.status == "completed"])
    progress = (completed / total * 100) if total > 0 else 0
    return {"progress": f"{progress:.1f}%", "completed": completed, "total": total}
