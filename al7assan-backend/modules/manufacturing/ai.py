# modules/manufacturing/ai.py
import pandas as pd
import random

def predict_maintenance(line_id: int, last_maintenance: str):
    """
    تنبؤ بموعد الصيانة التالية
    """
    days_since = (datetime.now() - datetime.fromisoformat(last_maintenance)).days
    if days_since > 25:
        return "موعد الصيانة قريباً"
    return "لا حاجة للصيانة الآن"

def optimize_production_schedule(orders):
    """
    تحسين جدول الإنتاج
    """
    return sorted(orders, key=lambda x: x['priority'], reverse=True)
