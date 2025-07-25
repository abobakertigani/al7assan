# routes/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
from models import Inventory
from schemas.inventory import InventoryCreate, InventoryResponse
from services.inventory_analyzer import get_low_stock_alerts

router = APIRouter(prefix="/inventory", tags=["Inventory"])

# تأكد من إنشاء الجدول
database.Base.metadata.create_all(bind=database.engine)

@router.post("/", response_model=InventoryResponse)
def add_item(item: InventoryCreate, db: Session = Depends(database.get_db)):
    """
    إضافة منتج إلى المخزون
    """
    new_item = Inventory(
        product_name=item.product_name,
        current_stock=item.current_stock,
        min_stock=item.min_stock,
        supplier=item.supplier,
        company_id=item.company_id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=List[InventoryResponse])
def get_inventory(company_id: int, db: Session = Depends(database.get_db)):
    """
    جلب كل مخزون شركة معينة
    """
    items = db.query(Inventory).filter(Inventory.company_id == company_id).all()
    return items

@router.get("/low-stock")
def get_low_stock_alerts_endpoint(company_id: int, db: Session = Depends(database.get_db)):
    """
    الحصول على تنبيهات المخزون المنخفض
    """
    items = db.query(Inventory).filter(Inventory.company_id == company_id).all()
    alerts = get_low_stock_alerts(items)
    return {"alerts": alerts, "total_low_stock": len(alerts)}

@router.put("/{item_id}")
def update_stock(item_id: int, quantity: float, db: Session = Depends(database.get_db)):
    """
    تحديث كمية المخزون (مثلاً: بعد توريد أو بيع)
    """
    item = db.query(Inventory).filter(Inventory.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="المنتج غير موجود")
    
    item.current_stock = quantity
    db.commit()
    return {"message": "تم تحديث الكمية", "new_stock": quantity}

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    """
    حذف منتج من المخزون
    """
    item = db.query(Inventory).filter(Inventory.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="المنتج غير موجود")
    
    db.delete(item)
    db.commit()
    return {"message": "تم حذف المنتج"}
