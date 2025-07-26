# modules/logistics/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import Delivery, Vehicle
from schemas import DeliveryCreate

router = APIRouter(prefix="/logistics", tags=["Logistics"])

@router.post("/deliveries")
def create_delivery( DeliveryCreate, db: Session = Depends(database.get_db)):
    new_delivery = Delivery(**data.dict(), status="assigned")
    db.add(new_delivery)
    db.commit()
    return {"message": "تم إنشاء مهمة التوصيل"}

@router.get("/fleet-status")
def fleet_status(company_id: int, db: Session = Depends(database.get_db)):
    total = db.query(Vehicle).filter(Vehicle.company_id == company_id).count()
    available = db.query(Vehicle).filter(Vehicle.status == "available").count()
    return {"total": total, "available": available, "utilization": f"{(total-available)/total*100:.1f}%"}

@router.get("/alerts")
def logistics_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    maintenance_due = db.query(Vehicle).filter(
        (datetime.now() - Vehicle.last_maintenance) > timedelta(days=90)
    ).count()
    if maintenance_due:
        alerts.append({
            "type": "صيانة مركبة",
            "message": f"{maintenance_due} مركبات تحتاج صيانة",
            "severity": "high"
        })
    return {"alerts": alerts} 
