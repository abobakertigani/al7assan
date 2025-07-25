# services/hr_analyzer.py
from datetime import datetime, timedelta
from models import Employee

def get_contract_alerts(employees):
    """
    إرجاع قائمة بالعقود التي ستنتهي قريبًا
    """
    alerts = []
    today = datetime.today().date()
    
    for emp in employees:
        if emp.contract_end_date:
            days_left = (emp.contract_end_date - today).days
            if 0 < days_left <= 30:
                alerts.append({
                    "employee_id": emp.id,
                    "name": emp.name,
                    "position": emp.position,
                    "days_left": days_left,
                    "action": "تجديد العقد"
                })
    return alerts

def suggest_promotions(employees):
    """
    اقتراح ترقيات بناءً على الخبرة والراتب
    """
    suggestions = []
    for emp in employees:
        if emp.hire_date:
            tenure = (datetime.today().date() - emp.hire_date).days
            if tenure > 365 * 2 and emp.salary < 10000:
                suggestions.append({
                    "employee_id": emp.id,
                    "name": emp.name,
                    "current_salary": emp.salary,
                    "suggested_increase": round(emp.salary * 0.15, 2),
                    "reason": "خبرة تزيد عن سنتين وراتب منخفض"
                })
    return suggestions
