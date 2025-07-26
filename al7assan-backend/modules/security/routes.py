# modules/security/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import SecurityIncident
from schemas import IncidentCreate

router = APIRouter(prefix="/security", tags=["Security"])

@router.post("/incidents")
def report_incident( IncidentCreate, db: Session = Depends(database.get_db)):
    new_incident = SecurityIncident(**data.dict())
    db.add(new_incident)
    db.commit()
    return {"message": "تم تسجيل الحادث الأمني"}

@router.get("/alerts")
def security_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    unresolved = db.query(SecurityIncident).filter(SecurityIncident.resolved == False).count()
    if unresolved > 0:
        alerts.append({
            "type": "حوادث مفتوحة",
            "message": f"{unresolved} حوادث أمنية لم تُحل بعد",
            "severity": "high"
        })
    return {"alerts": alerts}
