# routes/quality.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import QualityCheck
from services.quality_analyzer import analyze_defects

router = APIRouter(prefix="/quality", tags=["Quality"])

@router.get("/report")
def get_quality_report(company_id: int, db: Session = Depends(get_db)):
    checks = db.query(QualityCheck).filter(QualityCheck.company_id == company_id).all()
    
    data = [
        {
            "product": c.product_name,
            "defect_type": c.defect_type,
            "quantity": c.defective_count,
            "date": c.check_date
        }
        for c in checks if c.defective_count > 0
    ]
    
    return analyze_defects(data)
