# routes/marketing.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Sale
from services.marketing_analyzer import analyze_customers

router = APIRouter(prefix="/marketing", tags=["Marketing"])

@router.get("/insights")
def get_marketing_insights(company_id: int, db: Session = Depends(get_db)):
    sales = db.query(Sale).filter(Sale.company_id == company_id).all()
    
    data = [
        {
            "customer_id": s.customer_id,
            "total_spent": s.amount,
            "frequency": 1,  # يمكن تحسينه لاحقًا
            "last_purchase": s.date
        }
        for s in sales
    ]
    
    result = analyze_customers(data)
    return result
