# routes/it.py
from fastapi import APIRouter
from services.it_monitor import get_system_health

router = APIRouter(prefix="/it", tags=["IT"])

@router.get("/health")
def system_health():
    return get_system_health()

@router.get("/alerts")
def system_alerts():
    health = get_system_health()
    alerts = []
    if health["cpu_usage"] > 80:
        alerts.append("ارتفاع في استخدام المعالج")
    if health["memory_usage"] > 85:
        alerts.append("استخدام مرتفع للذاكرة")
    if health["disk_usage"] > 90:
        alerts.append("مساحة التخزين منخفضة")
    
    return {"alerts": alerts, "count": len(alerts)}
