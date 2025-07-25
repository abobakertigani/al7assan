# routes/production.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
from models import ProductionRecord
from schemas.production import RecordCreate, RecordResponse
from services.production_analyzer import predict_maintenance

router = APIRouter(prefix="/production", tags=["Production"])

# تأكد من إنشاء الجدول
database.Base.metadata.create_all(bind=database.engine)

@router.post("/", response_model=RecordResponse)
def log_production(record: RecordCreate, db: Session = Depends(database.get_db)):
    """
    تسجيل حدث في خط الإنتاج (عطل، إنتاج، صيانة)
    """
    new_record = ProductionRecord(
        machine_name=record.machine_name,
        operation=record.operation,
        output_count=record.output_count,
        defect_count=record.defect_count,
        failure_type=record.failure_type,
        notes=record.notes,
        company_id=record.company_id
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/maintenance-alert")
def get_maintenance_alert(company_id: int, db: Session = Depends(database.get_db)):
    """
    تحليل سجلات الأعطال والتنبؤ بالصيانة
    """
    records = db.query(ProductionRecord).filter(
        ProductionRecord.company_id == company_id,
        ProductionRecord.failure_type.isnot(None)
    ).all()

    failure_data = [
        {
            "date": r.timestamp.date().isoformat(),
            "machine": r.machine_name,
            "type": r.failure_type
        }
        for r in records
    ]

    result = predict_maintenance(failure_data)
    return result

@router.get("/", response_model=List[RecordResponse])
def get_records(company_id: int, machine: str = None, db: Session = Depends(database.get_db)):
    """
    جلب سجلات الإنتاج (بحسب الماكينة اختياريًا)
    """
    query = db.query(ProductionRecord).filter(ProductionRecord.company_id == company_id)
    if machine:
        query = query.filter(ProductionRecord.machine_name == machine)
    return query.all()
