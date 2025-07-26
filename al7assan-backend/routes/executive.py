# routes/executive.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.executive_dashboard import generate_daily_report
from routes.hr import get_contract_alerts
from routes.inventory import get_low_stock_alerts
from routes.production import predict_maintenance
from routes.quality import analyze_defects

router = APIRouter(prefix="/executive", tags=["Executive"])

@router.get("/daily-report")
def get_daily_report(company_id: int, db: Session = Depends(get_db)):
    # جلب البيانات من الأنظمة
    hr_data = get_contract_alerts(db.query(Employee).filter(Employee.company_id == company_id).all())
    inv_data = get_low_stock_alerts(db.query(Inventory).filter(Inventory.company_id == company_id).all())
    maint_data = predict_maintenance([...])  # سيتم تعبئته من قاعدة البيانات
    qual_data = analyze_defects([...])

    report = generate_daily_report(
        hr_alerts=hr_data,
        finance_prediction={},
        inventory_alerts=inv_data,
        quality_report=qual_data,
        maintenance_alert=maint_data
    )
    return report
