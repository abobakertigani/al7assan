# modules/solar/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from models import SolarSite, Inverter, EnergyProduction
from schemas import SiteCreate, ProductionCreate

router = APIRouter(prefix="/solar", tags=["Solar Energy"])

@router.post("/sites")
def create_site(site: SiteCreate, db: Session = Depends(database.get_db)):
    new_site = SolarSite(**site.dict())
    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    return new_site

@router.post("/production")
def log_production( ProductionCreate, db: Session = Depends(database.get_db)):
    new_log = EnergyProduction(**data.dict())
    db.add(new_log)
    db.commit()
    return {"message": "تم تسجيل الإنتاج"}

@router.get("/performance/{site_id}")
def get_performance(site_id: int, db: Session = Depends(database.get_db)):
    site = db.query(SolarSite).filter(SolarSite.id == site_id).first()
    production = db.query(EnergyProduction).filter(EnergyProduction.inverter_id.in_(
        db.query(Inverter.id).filter(Inverter.site_id == site_id)
    )).all()
    
    total = sum(p.energy_kwh for p in production)
    return {"site": site.name, "total_kwh": total, "status": "healthy"}

@router.get("/alerts")
def solar_alerts(company_id: int, db: Session = Depends(database.get_db)):
    alerts = []
    offline = db.query(Inverter).filter(Inverter.status == "offline").all()
    if offline:
        alerts.append({
            "type": "عطل في المحول",
            "message": f"{len(offline)} محولات معطلة",
            "severity": "high"
        })
    return {"alerts": alerts}
