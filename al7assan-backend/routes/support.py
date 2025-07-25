# routes/support.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import SupportTicket
from schemas.support import TicketCreate, TicketResponse
from services.customer_classifier import classify_complaint, generate_auto_reply

router = APIRouter(prefix="/support", tags=["Support"])

# تأكد من إنشاء الجدول
database.Base.metadata.create_all(bind=database.engine)

@router.post("/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(database.get_db)):
    """
    إنشاء تذكرة دعم جديدة + تصنيف تلقائي + رد آلي
    """
    category = classify_complaint(ticket.description)
    auto_reply = generate_auto_reply(category)

    new_ticket = SupportTicket(
        customer_name=ticket.customer_name,
        customer_email=ticket.customer_email,
        description=ticket.description,
        category=category,
        status="open",
        company_id=ticket.company_id
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return {
        **new_ticket.__dict__,
        "auto_reply": auto_reply
    }

@router.get("/", response_model=List[TicketResponse])
def get_tickets(company_id: int, status: str = None, db: Session = Depends(database.get_db)):
    """
    جلب تذاكر الدعم حسب الحالة (open, closed)
    """
    query = db.query(SupportTicket).filter(SupportTicket.company_id == company_id)
    if status:
        query = query.filter(SupportTicket.status == status)
    return query.all()

@router.put("/{ticket_id}/close")
def close_ticket(ticket_id: int, db: Session = Depends(database.get_db)):
    """
    إغلاق تذكرة دعم
    """
    ticket = db.query(SupportTicket).filter(SupportTicket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="التذكرة غير موجودة")
    
    ticket.status = "closed"
    db.commit()
    return {"message": "تم إغلاق التذكرة"}
