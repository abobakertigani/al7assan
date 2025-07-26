# modules/hse/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import SafetyInspection, IncidentReport
from schemas import InspectionCreate, IncidentCreate

router = APIRouter(prefix="/hse", tags=["Health & Safety"])

@router.post("/inspections")
def log_inspection( InspectionCreate, db: Session = Depends(database.get_db)):
    new_inspection = SafetyInspection(**data.dict())
    db.add(new_inspection)
    db.commit()
    return {"message": "تم تسجيل التفتيش"}

@router.post("/incidents")
def report_incident( IncidentCreate, db: Session = Depends(database.get_db)):
    new_incident = IncidentReport(**data.dict())
    db.add(new_incident)
    db.commit()
    return {"message": "تم تسجيل الحادث"}

@router.get("/alerts")
def hse_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    uncorrected = db.query(SafetyInspection).filter(SafetyInspection.corrected == False).count()
    if uncorrected > 0:
        alerts.append({
            "type": "مخاطر مفتوحة",
            "message": f"{uncorrected} ملاحظات سلامة لم تُعالج بعد",
            "severity": "high"
        })
    return {"alerts": alerts}
