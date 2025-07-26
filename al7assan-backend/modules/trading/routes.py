# modules/trading/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import SalesOrder, Inventory
from schemas import OrderCreate

router = APIRouter(prefix="/trading", tags=["Trading"])

@router.post("/orders")
def create_order( OrderCreate, db: Session = Depends(database.get_db)):
    inventory = db.query(Inventory).filter(Inventory.product_id == data.product_id).first()
    if not inventory or inventory.quantity < data.quantity:
        raise HTTPException(status_code=400, detail="الكمية غير متوفرة")
    
    total = db.query(Product).filter(Product.id == data.product_id).first().selling_price * data.quantity
    new_order = SalesOrder(
        product_id=data.product_id,
        customer=data.customer,
        quantity=data.quantity,
        total_amount=total
    )
    inventory.quantity -= data.quantity
    db.add(new_order)
    db.commit()
    return {"message": "تم تنفيذ الطلب", "total": total}

@router.get("/alerts")
def trading_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    low_stock = db.query(Inventory).filter(Inventory.quantity < 10).count()
    if low_stock:
        alerts.append({
            "type": "نفاد المخزون",
            "message": f"{low_stock} منتجات منخفضة الكمية",
            "severity": "high"
        })
    return {"alerts": alerts}
