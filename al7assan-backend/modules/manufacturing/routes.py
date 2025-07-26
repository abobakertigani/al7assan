# modules/manufacturing/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import ProductionLine, ProductionOrder, QualityCheck
from schemas import LineCreate, OrderCreate, QualityCreate

router = APIRouter(prefix="/manufacturing", tags=["Manufacturing"])

@router.post("/lines")
def create_line(line: LineCreate, db: Session = Depends(database.get_db)):
    new_line = ProductionLine(**line.dict(), status="stopped")
    db.add(new_line)
    db.commit()
    db.refresh(new_line)
    return new_line

@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(database.get_db)):
    new_order = ProductionOrder(**order.dict())
    db.add(new_order)
    db.commit()
    return {"message": "تم إنشاء أمر الإنتاج"}

@router.get("/efficiency/{line_id}")
def get_efficiency(line_id: int, db: Session = Depends(database.get_db)):
    line = db.query(ProductionLine).filter(ProductionLine.id == line_id).first()
    if not line:
        raise HTTPException(status_code=404, detail="الخط غير موجود")
    
    # مثال بسيط: الكفاءة = المنتجات / الوقت
    return {"efficiency": line.efficiency, "status": line.status}

@router.get("/alerts")
def get_manufacturing_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    low_efficiency = db.query(ProductionLine).filter(ProductionLine.efficiency < 60).all()
    if low_efficiency:
        alerts.append({
            "type": "كفاءة منخفضة",
            "message": f"{len(low_efficiency)} خطوط إنتاج بكفاءة أقل من 60%",
            "severity": "high"
        })
    return {"alerts": alerts}
