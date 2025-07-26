# modules/aquaculture/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import Farm, Batch, SensorData, FeedingLog, HealthLog
from schemas import FarmCreate, BatchCreate, SensorDataCreate, FeedingLogCreate, HealthLogCreate

router = APIRouter(prefix="/aquaculture", tags=["Aquaculture"])

@router.post("/farms")
def create_farm(farm: FarmCreate, db: Session = Depends(database.get_db)):
    new_farm = Farm(**farm.dict())
    db.add(new_farm)
    db.commit()
    db.refresh(new_farm)
    return new_farm

@router.get("/farms/{farm_id}/batches")
def get_batches(farm_id: int, db: Session = Depends(database.get_db)):
    return db.query(Batch).filter(Batch.farm_id == farm_id).all()

@router.post("/sensors")
def log_sensor(data: SensorDataCreate, db: Session = Depends(database.get_db)):
    new_log = SensorData(**data.dict())
    db.add(new_log)
    db.commit()
    return {"message": "تم تسجيل بيانات المستشعر"}

@router.post("/feeding")
def log_feeding(log: FeedingLogCreate, db: Session = Depends(database.get_db)):
    new_log = FeedingLog(**log.dict())
    db.add(new_log)
    db.commit()
    return {"message": "تم تسجيل التغذية"}

@router.get("/alerts")
def get_alerts(company_id: int, db: Session = Depends(database.get_db)):
    # تنبيهات ذكية
    alerts = []

    # مثال: إذا كانت درجة الحرارة > 30
    high_temp = db.query(SensorData).filter(SensorData.temperature > 30).all()
    if high_temp:
        alerts.append({
            "type": "حرارة عالية",
            "message": f"تم رصد حرارة عالية في {len(high_temp)} قراءات",
            "severity": "high"
        })

    # أمونيا عالية
    high_ammonia = db.query(SensorData).filter(SensorData.ammonia > 5).all()
    if high_ammonia:
        alerts.append({
            "type": "تلوث بأمونيا",
            "message": "مستوى الأمونيا مرتفع — خطر على الأسماك",
            "severity": "high"
        })

    return {"alerts": alerts}
