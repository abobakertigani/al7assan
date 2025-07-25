# routes/finance.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import models
from schemas.finance import InvoiceCreate, InvoiceResponse

router = APIRouter(prefix="/finance", tags=["Finance"])

# تأكد من إنشاء الجدول
models.Base.metadata.create_all(bind=database.engine)

@router.post("/invoices", response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(database.get_db)):
    """
    إنشاء فاتورة جديدة
    """
    new_invoice = models.Invoice(
        invoice_number=invoice.invoice_number,
        customer_name=invoice.customer_name,
        amount=invoice.amount,
        due_date=invoice.due_date,
        status=invoice.status,
        company_id=invoice.company_id
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice

@router.get("/invoices", response_model=List[InvoiceResponse])
def get_invoices(company_id: int, status: str = None, db: Session = Depends(database.get_db)):
    """
    جلب فواتير شركة معينة (بحسب الحالة اختياري)
    """
    query = db.query(models.Invoice).filter(models.Invoice.company_id == company_id)
    if status:
        query = query.filter(models.Invoice.status == status)
    return query.all()

@router.get("/invoices/{inv_id}", response_model=InvoiceResponse)
def get_invoice(inv_id: int, db: Session = Depends(database.get_db)):
    """
    عرض فاتورة معينة
    """
    inv = db.query(models.Invoice).filter(models.Invoice.id == inv_id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="الفاتورة غير موجودة")
    return inv

@router.put("/invoices/{inv_id}", response_model=InvoiceResponse)
def update_invoice(inv_id: int, invoice: InvoiceCreate, db: Session = Depends(database.get_db)):
    """
    تحديث فاتورة
    """
    inv = db.query(models.Invoice).filter(models.Invoice.id == inv_id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="الفاتورة غير موجودة")

    inv.invoice_number = invoice.invoice_number
    inv.customer_name = invoice.customer_name
    inv.amount = invoice.amount
    inv.due_date = invoice.due_date
    inv.status = invoice.status

    db.commit()
    db.refresh(inv)
    return inv

@router.delete("/invoices/{inv_id}")
def delete_invoice(inv_id: int, db: Session = Depends(database.get_db)):
    """
    حذف فاتورة
    """
    inv = db.query(models.Invoice).filter(models.Invoice.id == inv_id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="الفاتورة غير موجودة")

    db.delete(inv)
    db.commit()
    return {"message": "تم حذف الفاتورة بنجاح"}
