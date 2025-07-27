# routes/hr.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import models
from schemas.hr import EmployeeCreate, EmployeeResponse
from services.hr_analyzer import get_contract_alerts, suggest_promotions

router = APIRouter(prefix="/hr", tags=["HR"])

# تأكد من إنشاء الجدول
models.Base.metadata.create_all(bind=database.engine)

@router.post("/employees", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate, db: Session = Depends(database.get_db)):
    """
    إضافة موظف جديد
    """
    new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        position=employee.position,
        salary=employee.salary,
        hire_date=employee.hire_date,
        company_id=employee.company_id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.get("/employees", response_model=List[EmployeeResponse])
def get_employees(company_id: int, db: Session = Depends(database.get_db)):
    """
    جلب جميع موظفي شركة معينة
    """
    employees = db.query(models.Employee).filter(models.Employee.company_id == company_id).all()
    return employees

@router.get("/employees/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(database.get_db)):
    """
    جلب موظف معين
    """
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")
    return emp


@router.get("/hr-dashboard")
def get_hr_dashboard(company_id: int, db: Session = Depends(database.get_db)):
    employees = db.query(Employee).filter(Employee.company_id == company_id).all()

    return {
        "total_employees": len(employees),
        "contract_alerts": get_contract_alerts(employees),
        "promotion_suggestions": suggest_promotions(employees)
    }

@router.put("/employees/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, employee: EmployeeCreate, db: Session = Depends(database.get_db)):
    """
    تحديث بيانات موظف
    """
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")

    emp.name = employee.name
    emp.email = employee.email
    emp.position = employee.position
    emp.salary = employee.salary
    emp.hire_date = employee.hire_date

    db.commit()
    db.refresh(emp)
    return emp

@router.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(database.get_db)):
    """
    حذف موظف
    """
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")

    db.delete(emp)
    db.commit()
    return {"message": "تم حذف الموظف بنجاح"}
